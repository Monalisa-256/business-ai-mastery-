"""Self-contained integration tests for the public ZIP importer."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'tools' / 'extract_zips.py'


class ZipImporterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.dest = self.root / 'repo'
        self.dest.mkdir()
        self.inbox = self.root / 'uploads'
        self.inbox.mkdir()

    def make_zip(self, name, files):
        zpath = self.inbox / name
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            for arcname, content in files.items():
                z.writestr(arcname, content)
        return zpath

    def run_tool(self, *args, success=True):
        p = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args), '--dest', str(self.dest)],
            text=True, capture_output=True,
        )
        if success and p.returncode != 0:
            self.fail(f'Unexpected extractor error: {p.stderr}\n{p.stdout}')
        if not success and p.returncode == 0:
            self.fail(f'Expected failure, but succeeded: {p.stdout}')
        return p

    def test_any_zip_name_and_repo_wrapper_removal(self):
        z = self.make_zip('Any Course Name 2026.zip', {
            'some-public-course/README.md': '# Hello',
            'some-public-course/01-foundations/start.md': 'Getting started',
            'some-public-course/assets/figure.svg': '<svg/>',
        })
        self.run_tool(z)
        self.assertEqual((self.dest / 'README.md').read_text(), '# Hello')
        self.assertTrue((self.dest / 'assets/figure.svg').exists())
        self.assertFalse((self.dest / 'some-public-course').exists())

    def test_idempotent_identical_files(self):
        z = self.make_zip('repeat.zip', {'book/README.md': '# One'})
        self.run_tool(z)
        p = self.run_tool(z)
        self.assertIn('1 identical', p.stdout)
        self.assertEqual(len(list(self.dest.rglob('README.md'))), 1)

    def test_changed_existing_file_errors_by_default(self):
        z = self.make_zip('change.zip', {'book/README.md': '# New'})
        (self.dest / 'README.md').write_text('# Old')
        self.run_tool(z, success=False)
        self.assertEqual((self.dest / 'README.md').read_text(), '# Old')

    def test_replace_does_not_make_duplicate_filename(self):
        z = self.make_zip('change.zip', {'book/README.md': '# New'})
        (self.dest / 'README.md').write_text('# Old')
        self.run_tool(z, '--on-conflict', 'replace')
        self.assertEqual((self.dest / 'README.md').read_text(), '# New')
        self.assertEqual(sorted(p.name for p in self.dest.iterdir()), ['README.md'])

    def test_genuine_docs_folder_not_stripped(self):
        z = self.make_zip('docs.zip', {'docs/guide.md': 'Hello'})
        self.run_tool(z)
        self.assertTrue((self.dest / 'docs/guide.md').exists())
        self.assertFalse((self.dest / 'guide.md').exists())

    def test_force_strip_only_one_folder(self):
        z = self.make_zip('nested.zip', {'outer/docs/guide.md': 'Hello'})
        self.run_tool(z, '--strip-wrapper', 'always')
        self.assertTrue((self.dest / 'docs/guide.md').exists())

    def test_repeated_outer_wrapper(self):
        z = self.make_zip('double.zip', {'book/book/README.md': '# Read', 'book/book/assets/plot.svg': 'x'})
        self.run_tool(z)
        self.assertTrue((self.dest / 'README.md').exists())
        self.assertFalse((self.dest / 'book').exists())

    def test_blocks_path_traversal(self):
        z = self.make_zip('bad.zip', {'../evil.md': 'Bad'})
        self.run_tool(z, success=False)
        self.assertFalse((self.root / 'evil.md').exists())

    def test_blocks_windows_path_traversal(self):
        z = self.make_zip('badwindows.zip', {'..\\evil.md': 'Bad'})
        self.run_tool(z, success=False)

    def test_blocks_protected_workflow(self):
        z = self.make_zip('evil.zip', {'.github/workflows/pwn.yml': 'on: push'})
        self.run_tool(z, success=False)

    def test_rejects_symlink_members(self):
        zpath = self.inbox / 'symbolic.zip'
        with zipfile.ZipFile(zpath, 'w') as z:
            info = zipfile.ZipInfo('link')
            info.create_system = 3
            info.external_attr = (0o120777 << 16)
            z.writestr(info, 'target')
        self.run_tool(zpath, success=False)

    def test_import_all_any_extension_and_cleanup(self):
        self.make_zip('First Set.zip', {'course/README.md': 'One'})
        self.make_zip('Photos.ZIP', {'assets/photo.webp': b'abc'})
        self.run_tool('--all', '--source', self.inbox, '--on-conflict', 'replace', '--delete-archives')
        self.assertEqual((self.dest / 'README.md').read_text(), 'One')
        self.assertTrue((self.dest / 'assets/photo.webp').exists())
        self.assertEqual(list(self.inbox.glob('*')), [])

    def test_dry_run_does_not_change_files(self):
        z = self.make_zip('preview.zip', {'repo/README.md': 'Hello'})
        p = self.run_tool(z, '--dry-run')
        self.assertIn('DRY RUN', p.stdout)
        self.assertFalse((self.dest / 'README.md').exists())

    def test_case_insensitive_collisions_blocked(self):
        z = self.make_zip('clash.zip', {'README.md': 'A', 'readme.md': 'B'})
        self.run_tool(z, success=False)


if __name__ == '__main__':
    unittest.main()
