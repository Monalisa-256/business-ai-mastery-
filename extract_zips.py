#!/usr/bin/env python3
"""Safely import ZIP contents into a GitHub repository without extra wrappers.

Requires only Python 3.10+ and the standard library.

Usage:
  python tools/extract_zips.py 'uploads/My Course 2026.zip' --dest . --on-conflict replace
  python tools/extract_zips.py --all --source uploads --dest . --on-conflict replace --delete-archives
  python tools/extract_zips.py --all --dry-run

Default protection: changed files cause an error. Choose --on-conflict replace
for deliberate in-place updates, without duplicate numbered filenames.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import stat
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

# A single folder named 'assets' or 'docs' is probably meaningful, not a ZIP wrapper.
KNOWN_CONTENT_FOLDERS = {
    'assets','images','img','docs','documentation','src','source','lib','tests',
    'test','content','examples','scripts','tools','uploads','public','static',
    'data','media','chapters','lessons','figures','illustrations','diagrams',
    '01-foundations','02-business-management','03-content-creation',
    '04-practical-workflows','05-real-world-examples','06-reference',
}
REPO_MARKERS = {
    'readme.md','start-here.md','license','license.md','contributing.md',
    '.gitignore','package.json','pyproject.toml','cargo.toml','go.mod',
    'mkdocs.yml','index.md','requirements.txt',
}
# ZIPs are data input. Never let an uploaded ZIP replace the extraction system.
PROTECTED_TOPLEVEL = {'.git', '.github', 'tools', 'uploads'}
PROTECTED_FILENAMES = {'.env', '.env.local', '.env.production', 'setup-zip-extractor.md'}
IGNORED_COMPONENTS = {'__MACOSX', '.DS_Store', 'Thumbs.db'}


class ExtractionError(Exception):
    """An unsafe or ambiguous archive, or a disallowed file collision."""


@dataclass
class Item:
    name: str
    file: Path
    digest: str
    size: int
    archive: Path


def digest_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def normalise_name(raw: str) -> tuple[str, ...]:
    # ZIP paths use '/'. Treat backslashes as separators, too, for Windows safety.
    if not raw or '\x00' in raw:
        raise ExtractionError(f'Invalid archive path: {raw!r}')
    name = raw.replace('\\', '/')
    if name.startswith('/') or name.startswith('//') or re.match(r'^[a-zA-Z]:', name):
        raise ExtractionError(f'Absolute archive path blocked: {raw!r}')
    parts = name.rstrip('/').split('/')
    if any(part in ('', '.', '..') for part in parts):
        raise ExtractionError(f'Traversal or invalid archive path blocked: {raw!r}')
    # Windows permits reserved names/path shenanigans in archive entries; reject control chars.
    if any(any(ord(ch) < 32 for ch in part) for part in parts):
        raise ExtractionError(f'Control character in ZIP path: {raw!r}')
    return tuple(parts)


def is_metadata(parts: tuple[str, ...]) -> bool:
    return any(p in IGNORED_COMPONENTS or p.startswith('._') for p in parts)


def determine_strip(paths: list[tuple[str, ...]], policy: str) -> int:
    """Identify unmistakable ZIP root directories, not actual content folders.

    auto: strip if a sole root directory contains a repository-root marker,
    or is a repeated wrapper (course/course/README.md). Never strip a known
    content directory such as docs/ or assets/ without explicit --always.
    """
    if policy == 'never' or not paths:
        return 0
    depth = 0
    current = paths
    while current and all(len(p) > 1 for p in current):
        if policy == 'always' and depth >= 1:
            break  # Force-strip only the outermost folder; keep meaningful inner folders.
        roots = {p[0] for p in current}
        if len(roots) != 1:
            break
        root = next(iter(roots))
        if policy == 'always':
            eligible = True
        else:
            remaining = [p[1:] for p in current]
            has_marker = any(len(p) == 1 and p[0].casefold() in REPO_MARKERS for p in remaining)
            repeated = all(len(p) > 1 and p[0] == root for p in remaining)
            eligible = root.casefold() not in KNOWN_CONTENT_FOLDERS and (has_marker or repeated)
        if not eligible:
            break
        depth += 1
        current = [p[1:] for p in current]
    return depth


def check_protected(parts: tuple[str, ...], allow_config_files: bool) -> None:
    if not parts:
        raise ExtractionError('Empty target after wrapper removal')
    if not allow_config_files:
        if parts[0].casefold() in PROTECTED_TOPLEVEL or parts[-1].casefold() in PROTECTED_FILENAMES:
            raise ExtractionError(f'Protected repository configuration path: {"/".join(parts)}')


def validate_destination(target: Path, root: Path) -> None:
    # Resolve existing symlinks. Never write outside the repository through a link.
    try:
        target.resolve(strict=False).relative_to(root)
    except ValueError as exc:
        raise ExtractionError(f'Path would escape destination: {target}') from exc
    node = root
    for component in target.relative_to(root).parts:
        node = node / component
        if node.is_symlink():
            raise ExtractionError(f'Existing symlink in destination path: {node}')
    if target.exists() and not target.is_file():
        raise ExtractionError(f'Cannot replace directory or special file: {target}')
    for parent in target.parents:
        if parent == root:
            break
        if parent.exists() and not parent.is_dir():
            raise ExtractionError(f'Parent is not a directory: {parent}')


def discover_archives(args: argparse.Namespace) -> list[Path]:
    archives = [Path(p).expanduser().resolve() for p in args.archives]
    if args.all or not archives:
        folder = Path(args.source).expanduser()
        if folder.exists():
            archives.extend(p.resolve() for p in folder.rglob('*') if p.is_file() and p.suffix.casefold() == '.zip')
    archives = sorted(set(archives), key=lambda p: str(p).casefold())
    for p in archives:
        if not p.is_file() or p.suffix.casefold() != '.zip':
            raise ExtractionError(f'Expected a .zip archive: {p}')
    return archives


def stage_archives(args: argparse.Namespace, root: Path, staging: Path, archives: list[Path]) -> tuple[dict[Path, Item], int, int]:
    selected: dict[Path, Item] = {}
    case_names: dict[str, str] = {}
    declared_bytes = 0
    count = 0
    ignored = 0
    for archive in archives:
        try:
            with zipfile.ZipFile(archive) as z:
                # ZIP CRCs are checked as each member is streamed below. Avoid
                # testzip(): it would expand files before checking size limits.
                entries: list[tuple[zipfile.ZipInfo, tuple[str, ...]]] = []
                for info in z.infolist():
                    parts = normalise_name(info.filename)
                    if is_metadata(parts):
                        ignored += 1
                        continue
                    mode = (info.external_attr >> 16) & 0o170000
                    if mode not in (0, stat.S_IFREG, stat.S_IFDIR):
                        raise ExtractionError(f'Symlink or special ZIP entry blocked: {info.filename}')
                    if info.is_dir():
                        continue
                    if info.flag_bits & 1:
                        raise ExtractionError(f'Encrypted ZIP file is unsupported: {info.filename}')
                    if info.file_size > args.max_file_mb * 1024 * 1024:
                        raise ExtractionError(f'File exceeds configured size limit: {info.filename}')
                    if info.file_size > 0 and info.compress_size > 0 and info.file_size / info.compress_size > 10000:
                        raise ExtractionError(f'Extreme compression ratio blocked: {info.filename}')
                    declared_bytes += info.file_size
                    count += 1
                    if count > args.max_files or declared_bytes > args.max_total_mb * 1024 * 1024:
                        raise ExtractionError('Archives exceed overall count or uncompressed size limits')
                    entries.append((info, parts))
                strip = determine_strip([parts for _, parts in entries], args.strip_wrapper)
                print(f'Archive: {archive.name} | {len(entries)} files | wrapper levels removed: {strip}')
                for info, parts in entries:
                    dst_parts = parts[strip:]
                    check_protected(dst_parts, args.allow_config_files)
                    target = root.joinpath(*dst_parts)
                    validate_destination(target, root)
                    key = target.relative_to(root).as_posix().casefold()
                    name = target.relative_to(root).as_posix()
                    if key in case_names and case_names[key] != name:
                        raise ExtractionError(f'Case-insensitive path collision: {case_names[key]!r} / {name!r}')
                    case_names[key] = name
                    tmp_path = staging / f'content_{count:07}_{len(selected):07}.tmp'
                    hasher = hashlib.sha256()
                    size = 0
                    with z.open(info, 'r') as source, tmp_path.open('wb') as output:
                        for block in iter(lambda: source.read(1024 * 1024), b''):
                            size += len(block)
                            if size > args.max_file_mb * 1024 * 1024:
                                raise ExtractionError(f'Expanded file too large: {info.filename}')
                            hasher.update(block)
                            output.write(block)
                    item = Item(name, tmp_path, hasher.hexdigest(), size, archive)
                    prev = selected.get(target)
                    if prev:
                        if prev.digest == item.digest:
                            tmp_path.unlink()
                            continue
                        if args.on_conflict == 'error':
                            raise ExtractionError(f'Different content targets the same path across ZIPs: {item.name}')
                        if args.on_conflict == 'skip':
                            tmp_path.unlink()
                            continue
                        prev.file.unlink()
                    selected[target] = item
        except (zipfile.BadZipFile, EOFError, NotImplementedError) as exc:
            raise ExtractionError(f'Invalid, corrupt, or unsupported ZIP: {archive.name}: {exc}') from exc
    return selected, count, ignored


def execute(args: argparse.Namespace) -> int:
    root = Path(args.dest).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    archives = discover_archives(args)
    if not archives:
        print(f'No ZIP files found in {args.source!r}. Nothing to extract.')
        return 0
    if args.delete_archives and args.on_conflict == 'skip':
        raise ExtractionError('Avoid deleting archives when skipped changes might need review. Use error or replace.')
    with tempfile.TemporaryDirectory(prefix='.zip-import-stage-', dir=root) as temp:
        selected, scanned, ignored = stage_archives(args, root, Path(temp), archives)
        new: list[tuple[Path, Item]] = []
        updated: list[tuple[Path, Item]] = []
        identical = 0
        skipped_changes = 0
        for path, item in selected.items():
            if not path.exists():
                new.append((path, item))
            elif digest_of(path) == item.digest:
                identical += 1
            elif args.on_conflict == 'error':
                raise ExtractionError(f'Different file already exists: {item.name}. Use --on-conflict replace to update.')
            elif args.on_conflict == 'skip':
                skipped_changes += 1
            else:
                updated.append((path, item))
        print(f'Preflight: {len(new)} new, {len(updated)} updated, {identical} identical, {skipped_changes} skipped changes; {ignored} OS metadata entries ignored.')
        if args.dry_run:
            print('DRY RUN: no files were changed.')
            return 0
        for path, item in new + updated:
            path.parent.mkdir(parents=True, exist_ok=True)
            os.chmod(item.file, 0o644)
            os.replace(item.file, path)
        print(f'Extraction complete: {len(new)} added, {len(updated)} replaced, {identical} unchanged.')
    if args.delete_archives:
        for p in archives:
            p.unlink()
            print(f'Removed processed upload: {p}')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('archives', nargs='*', help='Any ZIP filename, quoted if it contains spaces; optional when using --all')
    parser.add_argument('--all', action='store_true', help='Find every .zip file below --source (case-insensitive)')
    parser.add_argument('--source', default='uploads', help='Folder scanned by --all (default: uploads)')
    parser.add_argument('--dest', default='.', help='Output repository folder (default: current directory)')
    parser.add_argument('--strip-wrapper', choices=('auto', 'always', 'never'), default='auto', help='Remove redundant outer folder(s); auto protects real docs/assets folders')
    parser.add_argument('--on-conflict', choices=('error', 'skip', 'replace'), default='error', help='Changed existing files: error (safe default), skip, or replace')
    parser.add_argument('--dry-run', action='store_true', help='Preview extraction and validate ZIPs without modifying files')
    parser.add_argument('--delete-archives', action='store_true', help='Remove uploaded ZIP files only after successful extraction')
    parser.add_argument('--allow-config-files', action='store_true', help='TRUSTED ARCHIVES ONLY: allow changes to .github/, tools/ and other protected paths')
    parser.add_argument('--max-file-mb', type=int, default=100, help='Maximum size of one expanded file (default: 100 MiB)')
    parser.add_argument('--max-total-mb', type=int, default=500, help='Maximum expanded size across archives (default: 500 MiB)')
    parser.add_argument('--max-files', type=int, default=20000, help='Maximum file entries across archives (default: 20000)')
    args = parser.parse_args()
    try:
        return execute(args)
    except (ExtractionError, OSError, RuntimeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
