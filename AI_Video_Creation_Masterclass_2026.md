# THE AI VIDEO CREATION MASTERCLASS

### A complete, illustrated field manual for AI movies, unscripted shows, speaking characters, recurring series, cartoons, podcasts, advertisements, documentaries and professional video production

**Edition:** November 23, 2026  
**Audience:** Complete beginners → intermediate creators → advanced producers and builders  
**Focus:** Real-world methods, named tools and model families, reusable prompts, budget planning, quality control, and ethical publishing  
**Format:** Markdown + nine original, locally bundled SVG illustrations. Links and model names were researched as of the edition date; vendor features, pricing, access and terms can change.

![AI video production cover — prompt, reference, generation, editing](AI_Video_Masterclass_Assets/00_cover.png)

> **The fundamental principle:** AI video is not one technology. A finished production usually combines a *thinking system* (an LLM), a *visual system* (image/video generator), a *performance system* (voice and animation), and an *editing system*. The right combination depends on whether you need a generated movie scene, a person reading speech, a spontaneous conversation, or a consistent recurring cast.

> **Scope and honesty:** “All AI video models” changes daily and cannot be exhaustively enumerated in a static guide. This handbook covers the major model *families*, leading commercial and open-weight models verified for late 2026, and the surrounding tools necessary to produce real work. A named platform may host several different models; model menus change. All example films, shows, hosts and characters in this guide are fictional.

---

## TABLE OF CONTENTS

1. [Quick-start: choose your kind of AI video](#1-quick-start-choose-your-kind-of-ai-video)
2. [Every major video format and technique](#2-every-major-video-format-and-technique)
3. [How the underlying AI models actually work](#3-how-the-underlying-ai-models-actually-work)
4. [The 2026 video model atlas](#4-the-2026-video-model-atlas)
5. [The complete creator tool directory](#5-the-complete-creator-tool-directory)
6. [The end-to-end production pipeline](#6-the-end-to-end-production-pipeline)
7. [Truly unscripted, improvised and semi-scripted AI videos](#7-truly-unscripted-improvised-and-semi-scripted-ai-videos)
8. [Making voices sound human](#8-making-voices-sound-human)
9. [Making AI people and performances look human](#9-making-ai-people-and-performances-look-human)
10. [Consistent characters, locations and recurring series](#10-consistent-characters-locations-and-recurring-series)
11. [Animation, cartoons, animals, fantasy and special formats](#11-animation-cartoons-animals-fantasy-and-special-formats)
12. [Camera direction, editing and audio post-production](#12-camera-direction-editing-and-audio-post-production)
13. [Eight complete, worked video recipes](#13-eight-complete-worked-video-recipes)
14. [The prompt engineering masterclass](#14-the-prompt-engineering-masterclass)
15. [Fixing common AI video failures](#15-fixing-common-ai-video-failures)
16. [Quality control, testing and production standards](#16-quality-control-testing-and-production-standards)
17. [Credits, costs, hardware and cost modeling](#17-credits-costs-hardware-and-cost-modeling)
18. [Legal rights, consent, safety and platform monetization](#18-legal-rights-consent-safety-and-platform-monetization)
19. [Publishing, growth and making money](#19-publishing-growth-and-making-money)
20. [Advanced creator automation and local AI](#20-advanced-creator-automation-and-local-ai)
21. [A 30-day learning plan](#21-a-30-day-learning-plan)
22. [Copy-ready templates and worksheets](#22-copy-ready-templates-and-worksheets)
23. [Glossary](#23-glossary)
24. [Official sources, manuals and further learning](#24-official-sources-manuals-and-further-learning)

---

# 1. QUICK-START: CHOOSE YOUR KIND OF AI VIDEO

![Choose a video workflow based on the outcome](AI_Video_Masterclass_Assets/08_decision_map.png)

Don't start by paying for the most famous AI video app. Start by deciding what the finished viewer should experience.

| Your outcome | Most direct method | Beginner-friendly starting stack | Main challenge |
|---|---|---|---|
| A fictional movie scene | Text-to-video or image-to-video | Google Flow / Kling / Runway + CapCut | Consistent action, faces and multiple shots |
| Two people chatting naturally | AI dialogue + two voices + talking characters | Language model + ElevenLabs + Hedra/HeyGen + editor | Turn-taking, voice timing, listening reactions |
| **Genuinely unscripted AI host** | Live conversational avatar | LiveAvatar / Tavus / D-ID with a conversational model | Latency, interruptions, moderation and recording |
| A news/educational presenter | Talking avatar from text or audio | HeyGen / Synthesia | Credibility, accurate facts and natural delivery |
| A multi-episode drama | Character references + shot-by-shot production | LTX Studio + image generator + Kling/Runway + editor | Character and story continuity |
| A cartoon/animated series | Style bible + consistent character art + animated shots | Image tool + LTX Studio + video model + voice | Repeatable style and expressive movement |
| A faceless documentary | Research + narration + images/B-roll | Descript/InVideo/Pictory + voice + editor | Original reporting, evidence and narrative |
| Product ads / UGC-style clips | AI advertising actor + real product visuals | Arcads / Creatify / HeyGen | Honest product claims, rights and conversion |
| Music video | Music + visual concept + beat-matched shots | Licensed/original music + Runway/Kling + editor | Timing and art direction |
| Dubbing into another language | Translation + voice adaptation + optional lip sync | ElevenLabs Dubbing / HeyGen Translation | Idiom, accent, timing and permissions |
| Animated speaking animals | Original animal character + speech-driven animation | Image tool + Hedra/alternative audio-video model | Mouth, paws, anatomy and style |
| Live AI interview/game-show character | Real-time voice/LLM/video loop | Tavus / LiveAvatar / D-ID | Conversational reliability and production setup |

**Three recommended learning stacks:**

- **Entry-level:** an image/idea tool + Google Flow or Kling + CapCut. Make a 20–40 second finished story before adding services.
- **Speaking-character creator:** HeyGen or Hedra + ElevenLabs (only if you need more voice control) + CapCut/Descript.
- **Recurring cinematic-series producer:** character reference system + LTX Studio for planning + one or two generation models + DaVinci Resolve + a maintained series bible.

**A useful distinction:** Some companies bundle multiple models. Runway and Adobe Firefly can give access to partner models; a branded interface is not proof that every clip uses that company's proprietary foundation model. Inspect the model selector and credit estimate before generating.

---

# 2. EVERY MAJOR VIDEO FORMAT AND TECHNIQUE

![The principal AI video model families](AI_Video_Masterclass_Assets/02_model_families.png)

## 2.1 Video *products* versus video *generation methods*

A **product/platform** is the interface you visit (for example, Runway or HeyGen). A **model** is the underlying AI system performing a job (for example, Gen-4.5 or Veo 3.1). A **mode** is how you give inputs to it (text-to-video, image-to-video, video-to-video, etc.). A **workflow** is the complete chain producing the final publishable result.

### The major modes

| Mode | Input → output | What it can do | What it does *not* guarantee |
|---|---|---|---|
| **Text-to-video (T2V)** | Written prompt → moving scene | Invent people, places, camera work and action | Same actor across separate renders |
| **Image-to-video (I2V)** | Reference image + motion instructions → clip | Animate a controlled-looking character/scene | Perfect preservation of every object |
| **Frames/keyframes-to-video** | Start/end or several stills → interpolated motion | Design transitions and controlled shot endpoints | Accurate physical motion between frames |
| **Reference-to-video** | Character/object/location reference(s) → clip | Increase visual continuity | Locked identity in every pose |
| **Video-to-video (V2V)** | Existing footage + instruction → changed footage | Restyle, modify setting/clothing, replace elements | Preservation of all original details |
| **Video inpainting** | Clip + selected region → changed region | Remove/replace parts of a shot | Seamless tracking under hard occlusions |
| **Outpainting/reframing** | Clip/image → expanded canvas | Convert framing and extend backgrounds | Perfect newly invented off-screen content |
| **Video extension** | Existing last frames → added duration | Continue an action or atmosphere | Long-horizon consistency |
| **Audio-driven video** | Voice/audio + character image/video → performance | Animate mouth and often expressions | Physically natural full-body acting |
| **Talking avatar** | Avatar + words or audio → presenter video | Reliable repeatable host delivery | Live thought or spontaneous reasoning |
| **Performance transfer** | Recorded actor + target character → animated/modified performance | Preserve acting, gesture or movement | Exact face/hand fidelity without review |
| **Motion/pose guidance** | Tracking/pose/depth maps → scene motion | Guide body/camera structure | Correct anatomy in every frame |
| **Motion graphics / infographic video** | Data/text/design assets → animated graphics | Explainers, titles, charts | Automatic factual accuracy |
| **Real-time conversational avatar** | Microphone → listener/LLM/voice/avatar response | Unscripted dialogue or interactive host | An automatically edited final episode |
| **Stock-based AI video assembly** | Topic/text → stock clips + voice + captions | Fast explainers and faceless videos | That the video footage was generated by AI |
| **Dubbing / localization** | Original video → translated voice/captions/lips | Multiple languages | Cultural accuracy without checking |
| **AI-supported editing** | Existing video → edits/captions/reframing | Fast post-production | Ownership of source footage |
| **Open-weight/local generation** | Model checkpoint + local GPU/pipeline → clip | Fine control, privacy, programmable workflows | Low hardware cost or automatic commercial rights |

## 2.2 The kinds of content you can publish

- **Narrative:** drama, romance, comedy, science fiction, horror, thriller, fantasy, fairy tales, anthology series, mockumentaries.
- **Conversation:** talk shows, two-host podcasts, debates, live interviews, fictional counseling scenes, panel discussions, reality-show-style fiction.
- **Person-led:** fictional influencers, tutorials, explainers, presenter videos, virtual brand ambassadors, digital twins of consenting adults.
- **Faceless:** history, science, education, narrated stories, cooking explanations, travel-style illustrations, product guides.
- **Graphic and animated:** 2D cartoons, 3D-style animation, anime-inspired original worlds, stop-motion aesthetics, typography videos, music visualizers, video-game trailers.
- **Business:** product demonstrations, employee training, e-commerce ads, pitch videos, localized marketing, onboarding videos.
- **Interactive:** livestream-like AI characters, conversational product experts, virtual museum guides, game NPCs and educational agents.

> “Unscripted” needs careful definition. A language model generating a complete fictional conversation *before rendering* is **automatically authored**, not live. A microphone-driven avatar replying to new speech in real time is **interactive**, but your final published video still requires recording and editing.

---

# 3. HOW THE UNDERLYING AI MODELS ACTUALLY WORK

The following is a practical, simplified explanation. Exact model architectures are proprietary for many products. A marketing description of a model is **not** a published engineering specification.

## 3.1 Text and multimodal language models: the *brains*

An LLM can take instructions, read context and produce words. In video production, it can act as a writer, producer, improv actor, editor's assistant, continuity checker or interactive host. Common choices include ChatGPT-family language models, Gemini, Claude, and open-weight language models such as Qwen, depending on access and requirements.

**A useful mental model:** You give it a role + facts + current situation + previous dialogue; it predicts a useful next response. It cannot, by itself, guarantee that a video generator will depict the response correctly.

For unscripted dialogue, keep these separate:

1. **Character personality** — what kind of person the AI is pretending to be.
2. **World state** — verified facts and what the character currently knows.
3. **Conversation state** — who spoke last, topic, unresolved questions, emotional state.
4. **Generation rules** — how long a turn can be, when to stop, how to avoid repetition and unsafe claims.
5. **Voice and rendering** — how the spoken response becomes audible and visible.

## 3.2 Image generation models: the *art department*

Image generators create controlled visual reference material: character portraits, costume studies, locations, props, thumbnails, background plates and keyframes. Many modern systems use diffusion/flow-style generative techniques or related learned image-generation methods.

**Why images are important even if you want video:** Video models have to decide appearance *and* motion at once. Creating a strong reference still reduces ambiguity. A reference image is not a perfect identity lock, but it is often the best first control.

**Common image tools and model families:** Midjourney (its V8.1 line is documented in 2026), ChatGPT image generation, Google Nano Banana image models, Adobe Firefly Image, Leonardo AI, Ideogram, Recraft, Seedream, Freepik and local Stable Diffusion/FLUX workflows. Some of those are hosted apps, others are underlying models. [Midjourney updates](https://updates.midjourney.com/v8-1-is-now-the-default-model/) · [Adobe partner-model docs](https://helpx.adobe.com/creative-cloud/apps/generative-ai/non-adobe-models-in-adobe-products.html)

## 3.3 Diffusion/flow and latent video models: the *camera unit*

A common modern architecture creates a series of related frames using a learned denoising/flow process, often operating on a compressed representation called a **latent**. Many use Transformer-style processing to handle spatial relationships and changes over time. Some generate audio separately; other models jointly produce synchronized audio and video.

A simplified conceptual pipeline:

```text
Text prompt / images / prior frames / audio / references
             ↓
     Text + visual encoders
             ↓
   A compressed space-time representation
             ↓
  Learned video generation/denoising network
             ↓
   Decode into moving image frames
             ↓
  Native audio (if supported) OR separate sound design
             ↓
       Video clip file
```

This explains several familiar artifacts: a face may drift between frames, a hand may grow an extra finger, a cup may disappear, or a camera move may make an object morph. The system is synthesizing *plausible* frame sequences, not running a reliable physics simulation or tracking all props like a conventional 3D production.

**Technical vocabulary:**

- **DiT:** Diffusion Transformer; a Transformer-based generation backbone used by some modern visual/audio models.
- **Latent:** Compressed representation, not the finished pixels/audio samples.
- **Conditioning:** Reference information controlling a generation (text, image, keyframe, pose, audio).
- **Sampling steps / guidance:** Generation settings exposed by some systems; higher numbers do not automatically mean better footage.
- **Seed:** Randomness initialization. Reusing it may assist reproducibility under identical settings, but does not guarantee character consistency across different scenes.
- **LoRA:** Lightweight model adaptation; useful in supported local workflows for styles or characters but requires appropriate training data and rights.
- **Temporal consistency:** Whether subject, geometry and motion remain coherent across frames.
- **Native audio:** Audio generated by the video model; not equivalent to importing a separately produced soundtrack.

LTX's open model documentation explicitly describes a synchronized audio-video, DiT-based system. See the [LTX open-source model overview](https://docs.ltx.io/open-source-model/getting-started/overview/).

## 3.4 Lip-sync models: turning audio into a visible speaking performance

A lip-sync system estimates mouth and often facial movement from sound and applies it to a source face, image or video. It may work on the whole head or primarily the mouth region. Results depend on the pose, lighting, occlusion, audio quality and model.

**Example:** Photograph of fictional host Maya + a 20-second voice track → talking portrait with facial movements. This is much easier than asking a cinematic model to preserve exact dialogue across multiple independent generations, though full-body movement may be limited.

## 3.5 Text-to-speech (TTS), speech-to-speech and voice cloning

- **TTS:** Generate speech from words. Best for repeatable narration and dialogue where you know the lines.
- **Expressive TTS:** Adds style, emotion, delivery cues and multi-speaker behavior.
- **Speech-to-speech:** Use an actual performed audio recording as the timing/acting reference, then transform the vocal identity using a tool that permits that use.
- **Voice cloning:** Produce a model resembling an authorized recorded voice. Providers have different verification policies; never assume someone else's voice is clonable simply because you obtained a sample.
- **Speech recognition (ASR/STT):** Convert speech to text for captions, transcription or live conversational agent input.
- **Speaker diarization:** Identify which person spoke when.
- **Voice activity detection (VAD):** Detect speech segments/turn endings in a live conversation.

For believable fictional actors, **speech-to-speech plus a human performance** can outperform TTS-only workflows in difficult emotional scenes because the acting and pacing are already present in the input.

## 3.6 A live AI human is a *system*, not just one model

![The conversational avatar loop](AI_Video_Masterclass_Assets/03_unscripted_loop.png)

A real-time AI character commonly combines:

1. **Input:** mic, text, camera or another AI agent's words.
2. **Perception:** ASR, optionally visual recognition.
3. **Reasoning:** LLM + personality + memory + guardrails.
4. **Turn management:** VAD, interruptions, silence handling, maximum turn length.
5. **Speech output:** streaming TTS or speech-to-speech conversation model.
6. **Avatar renderer:** face, mouth, expressions and video stream.
7. **Transport:** low-latency streaming, frequently WebRTC.
8. **Recording / moderation:** record authorized sessions, handle failure, review before publication.

Tavus, LiveAvatar and D-ID provide versions of this functionality; their autonomy levels, integration requirements and pricing are not identical. [Tavus CVI](https://www.tavus.io/cvi) · [LiveAvatar overview](https://help.heygen.com/en/articles/12758516-introducing-liveavatar) · [D-ID real-time architecture](https://docs.d-id.com/docs/realtime-overview)

## 3.7 Why a one-hour movie is not one generation

Even a model claiming 20–30 seconds of output is not a reliable substitute for the whole filmmaking process. Separate generations differ in lighting, props, voice timbre, actor identity and spatial layout. Producers therefore work shot-by-shot, generate alternatives, record dialogue, cut on action, maintain reference assets and use editing to construct the story.

---

# 4. THE 2026 VIDEO MODEL ATLAS

> **Model-version snapshot:** November 23, 2026. These are examples of leading or technically important lines, **not** a claim that each is enabled in every country or account. A product may show “Fast,” “Turbo,” “Lite” or credit-specific variants. Always inspect the live model selector, terms, and credit preview.

## 4.1 Current commercial video-generation families

| Model / family | Developer or access point | Input and typical role | Audio / continuity notes | Verify |
|---|---|---|---|---|
| **Veo 3.1** | Google, via Flow / API routes | High-quality cinematic T2V, I2V and reference-guided scenes | Supports native audio; spoken audio remains imperfect, especially short dialogue | [Model](https://deepmind.google/models/veo/) · [Flow help](https://support.google.com/flow/answer/16352836) |
| **Gemini Omni Flash 1.2** | Google Flow | Newer supported Flow generation/editing workflows; use product menu to check exact modes | Do not conflate all Omni modes with Veo modes | [Flow model support](https://support.google.com/flow/answer/16352836) |
| **Veo 3.1 Lite / Fast / Quality variants** | Google Flow (plan-dependent) | Speed/quality choices for supported Flow operations | Google had announced retirement of some older variants for Dec. 5, 2026 | [Flow help](https://support.google.com/flow/answer/16352836) |
| **Gen-4.5** | Runway | Cinematic T2V/I2V with motion and prompt control | Audio availability varies by product route; review final sound separately | [Runway help](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5) |
| **Gen-4 / Gen-4 Turbo** | Runway | Reference-driven and faster video options | Good for comparative takes; not necessarily all features of Gen-4.5 | [Model/credit catalogue](https://academy.runwayml.com/models-pricing) |
| **Aleph 2.0** | Runway API and tools | Video editing / transformation | Best understood as a video-edit model, not just T2V | [Developer models](https://docs.dev.runwayml.com/guides/models/) |
| **Kling 4.0** | Kling AI / Kuaishou | Cinematic, reference/multimodal video and more controlled storytelling | Professional-grade positioning; compare variants and available native-audio settings | [Official launch](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-officially-launches-next-generation-kling-40-raising/) |
| **Seedance 2.5** | ByteDance / Dreamina and partner interfaces | Multimodal audio-video generation, references and longer single-pass scenes | Vendor describes up to 30-second single-pass generation; that is not a full episode | [Seed blog](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) |
| **Ray3.2** | Luma | Video generation, references and sophisticated editing/Modify workflows | Useful for controlled changes to existing footage | [Official update](https://lumalabs.ai/news/introducing-ray-3-2) |
| **Pika 2.5** | Pika | Short-form stylized motion and I2V | Pikaframes can interpolate between multiple stills | [Pika](https://creation.pika.art/apps/pika-2-5) |
| **Pika H3 Flex** | Pika model hub | Multi-reference/omni-reference workflow | Inspect current availability and feature limits | [Model menu](https://creation.pika.art/apps?tab=models) |
| **PixVerse V6** | PixVerse | Fast short-form video and creative effects | Useful for social/experimental work | [Launch](https://pixverse.ai/en/blog/pixverse-launches-v6-advancing-ai-video-generation) |
| **Firefly Video Model** | Adobe Firefly | Brand/design-oriented generative video | Firefly also hosts partner models with different terms | [Adobe models](https://helpx.adobe.com/firefly/web/create-mood-boards/firefly-boards/partner-models-to-generate-videos.html) |
| **Higgsfield cinematic model tools** | Higgsfield / Cinema Studio | Character-centric video, controlled camera moves and ad workflows | Soul ID adds a distinct character-consistency layer | [Official explainer](https://higgsfield.ai/creator-hub/help-center/getting-started/what-is-higgsfield) |
| **LTX Studio models and integrated providers** | Lightricks / LTX Studio | Storyboards, scenes, generators, edits and character Elements | Different models can be selected for different stages | [Official help](https://help.ltx.io/hc/en-us/p/ltx-studio) |
| **Midjourney video** | Midjourney | Animate selected images; short creative motion | Image-generation model version ≠ video-model version | [Video documentation](https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video) |

**A necessary 2026 correction:** Sora's app/web experience was discontinued April 26, 2026, and the API was slated for discontinuation September 24, 2026. Do not start a new course or business plan that assumes the old Sora service is still available. [OpenAI's discontinuation notice](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)

### How to compare models intelligently

Use a repeatable test set: one close-up face speaking, one two-character conversation, one moving hand interacting with a prop, one wide shot with camera movement, one character-reference shot and one scene with realistic environmental audio. Keep aspect ratio, prompt intent, shot duration and acceptance criteria as comparable as possible. Score motion, identity, speech, physics, audio, prompt following, time and cost. Marketing highlight reels are not controlled comparisons.

## 4.2 Important open-weight/local video models

| Model family | What it is | Useful modes | Reality check | Official source |
|---|---|---|---|---|
| **LTX-2.5 (open weights)** | Lightricks audiovisual generative model | Text/image/video-guided audio-video generation; native multishot support | Hardware and license requirements vary; “open weights” does not automatically mean unrestricted reuse | [LTX docs](https://docs.ltx.io/open-source-model/getting-started/overview/) |
| **LTX-2.3 in LTX products** | Lightricks video model available in product/API contexts | Video generation, native portrait and audio improvements | Product version labels and open checkpoints can differ | [LTX models help](https://help.ltx.io/hc/en-us/p/models) |
| **Wan2.2** | Wan video model checkpoints and code | T2V, I2V, and variants including speech-to-video (S2V) | Check *exact* checkpoint, terms and GPU needs | [Official GitHub](https://github.com/Wan-Video/Wan2.2) |
| **HunyuanVideo-1.5** | Tencent's comparatively lightweight open video model | Text/image-to-video generation with associated tools | Model weights, dependencies and checkpoint licenses must be read separately | [Official GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) |
| **HunyuanVideo original** | Earlier Tencent video foundation system | Research/local workflows | Primarily useful for comparison or established pipelines | [Official GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo) |
| **CogVideoX** | Open research video model family | Text/image video via supported local interfaces | Generally older than late-2026 flagship commercial offerings | [ComfyUI model overview](https://github.com/Comfy-Org/ComfyUI) |
| **Mochi, Cosmos, Kandinsky-video families** | Additional research/open families | Specialized video pipelines in supported interfaces | More technical; features and licenses differ | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) |

**Warning about names:** A hosted website claiming “Wan 2.7” does not prove there are official open-weight 2.7 files you can legally download. Hosted partner-node model access and openly released local checkpoints are different things. Use the model author's actual repository and license, not random download mirrors.

## 4.3 Image/character models commonly used *before* video

| Tool/model | Strongest use | Why it matters for video |
|---|---|---|
| Midjourney image line (including 2026 V8.1 documentation) | Strong concept art and photographic looks | Create the hero frames and character sheet |
| ChatGPT image generation | Iterating on concepts and references conversationally | Build repeatable assets and prompts |
| Google Nano Banana family | Image generation/editing within Google workflows | Reference images usable alongside Flow |
| Adobe Firefly Image / partner models | Brand-design and commercially managed workflows | Integrates into Adobe post-production |
| Leonardo AI | Characters and art direction | Generate many outfits and angles |
| OpenArt character system | Reusable character identity | Recurring cast for videos |
| Higgsfield Soul ID | A learned consistent identity asset | Reuse an original character face in later scenes |
| Seedream | Multireference image editing | Character / prop / location reference building |
| Ideogram | Legible titles / poster art | Thumbnail and graphics production |
| Recraft | Graphic illustration / vector output | Style guides, posters, diagrams, brand marks |
| Stable Diffusion / FLUX workflows | Programmable image creation and fine-tuning | LoRA-based asset libraries with technical control |

## 4.4 Voice and conversational *model* families

| Model / platform family | Primary use | Best for | Key consideration |
|---|---|---|---|
| **Eleven v4** | High-quality expressive TTS | Drama, character dialogue, narration | Quality and expressiveness; evaluate chosen voice |
| **Eleven v4 Turbo** | Low-latency expressive speech | Real-time dialogue | Speed and quality vary by settings |
| **Eleven v3 / v3 Conversational** | Earlier expressive speech modes | Emotion-directed dialogue | Check current supported API mode |
| **Eleven Multilingual v2 / Flash v2.5** | Stable or fast speech | Long-form consistency / rapid generation | Language and latency trade-offs |
| **ElevenAgents** | Integrated conversational voice agents | Real-time interactions | Includes agent orchestration beyond standalone TTS |
| **Cartesia Sonic 3** | Fast streaming speech | Conversational systems | Low-latency text-to-speech, not video by itself |
| **Hume Octave** | Expressive speech and voice design | Distinct characters and vocal intent | Compare style/voice control with TTS alternatives |
| **Murf** | Business voiceover platform | Narration and explainers | Less focused on cinematic visual generation |
| **Fish Audio** | Voice generation / API workflows | Alternative speech voices | Evaluate licensing and voice rights |
| **Deepgram / AssemblyAI / Whisper-family ASR** | Speech recognition and transcription | Agent inputs, captions and editing | Accuracy differs by accent, noise and language |

Sources: [ElevenLabs model catalogue](https://elevenlabs.io/docs/overview/models) · [Eleven v4 announcement](https://elevenlabs.io/blog/eleven-v4) · [Cartesia Sonic 3 via AWS](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart) · [Hume Octave](https://www.hume.ai/octave)

## 4.5 Avatar model/renderer lines

**HeyGen:** A platform with multiple avatar-generation generations and product modes; its current help center discusses Avatar IV/V/VI and Video Agent, while LiveAvatar is a separate real-time offering. Do not assume “Avatar IV” and “LiveAvatar” perform the same job. [HeyGen Avatar IV](https://help.heygen.com/en/articles/11269603-heygen-avatar-iv-complete-guide) · [Credits and Avatar 6](https://help.heygen.com/en/articles/15126059-how-to-use-credits-on-heygen)

**Hedra:** An expressive character-performance platform that began with speaking-character animation and expanded into broader creative generation. Character-3 and Omnia are named in its provider updates; read current features before selecting a mode. [Hedra updates](https://hedra.me/blogs/feature-announcements-and-updates)

**Tavus:** A real-time video-persona platform; a “face”/replica supplies the visual identity, while a persona plus turn-taking, perception and LLM layers drive interaction. [Tavus CVI](https://www.tavus.io/cvi)

**D-ID:** Talking presenters and real-time agents that stream animated avatar responses via integrations. [Real-time docs](https://docs.d-id.com/docs/realtime-overview)

**Synthesia:** An avatar/presenter production environment, especially for training, education and business. Interactive capabilities, availability and commercial plan details should be checked directly. [Synthesia](https://www.synthesia.io/)

---
# 5. THE COMPLETE CREATOR TOOL DIRECTORY

A useful creator may use only three tools, but should understand the wider landscape. The descriptions below say **what a product is for**, not that it is always the highest-performing or least expensive. If an exact model is missing in a tool's menu, do not assume a blog screenshot proves access.

## 5.1 Cinematic video and motion platforms

| Tool | Official site | Primary role | Ideal user | Watch out for |
|---|---|---|---|---|
| Google Flow | [Flow](https://labs.google/fx/tools/flow) | Google video generation, references, scene creation, editing features | Beginners through professionals | Models and credit requirements vary by tier |
| Runway | [Runway](https://runway.com/) | Generation, references, editing, motion tools and multi-model access | Film-oriented creators | Credits may run out fast at premium settings |
| Kling AI | [Kling](https://kling.ai/) | Cinematic scenes and action with multiple model variants | Dramas, films, ads | Different Kling versions/tiers behave differently |
| Dreamina / Seedance | [Dreamina](https://dreamina.capcut.com/) | Seedance audiovisual generation and reference workflows | Narrative and social creators | Geographic/plan availability and rights vary |
| Luma | [Luma](https://lumalabs.ai/) | Generation and modifying real or generated footage | VFX and visual experimentation | Controlling a long narrative remains difficult |
| Pika | [Pika](https://pika.art/) | Short motion clips, keyframes, playful effects | Social and stylized shorts | Not a full editing or screenplay suite |
| PixVerse | [PixVerse](https://pixverse.ai/) | Generative short video and effects | Quick experiments | Verify quality and aspect modes in your tier |
| Higgsfield | [Higgsfield](https://higgsfield.ai/) | Character consistency, cinematic camera actions and marketing | AI influencer or short-film creators | Marketplace/feature names change frequently |
| Adobe Firefly | [Firefly](https://www.adobe.com/products/firefly.html) | Video generation with Adobe and partner models | Design and professional teams | Partner outputs have their own conditions |
| LTX Studio | [LTX Studio](https://ltx.studio/) | Projects, shot generation, storyboard and timeline | Episode and advertisement producers | Not every task is a one-click generation |
| OpenArt | [OpenArt](https://openart.ai/) | Character creation, image generation and animated workflows | Creators requiring recurring characters | Check model selection and usage costs |
| Hailuo | [Hailuo](https://hailuoai.video/) | Image/text motion generation | Experimentation | Verify actual current model and terms |
| Midjourney Video | [Midjourney](https://www.midjourney.com/) | Short animation of still images | Artists working image-first | Final long-form editing is external |

**How to test a cinematic generator:** Create the same three-shot scene in two tools. Record generation cost, retries, identity errors, motion quality, dialogue synchronization and time saved in editing. Keep the one that passes *your* test instead of using a generic ranking.

## 5.2 Talking presenters and avatar tools

| Tool | Official site | What you actually provide | Best use | Limit |
|---|---|---|---|---|
| HeyGen | [heygen.com](https://www.heygen.com/) | Text/audio + selected or trained avatar | Presenter, talking fictional host, multilingual videos | Pre-rendered avatars are not live autonomous agents |
| Synthesia | [synthesia.io](https://www.synthesia.io/) | Presenter + script/audio and scene design | Training, education, businesses | Less appropriate for physical-action dramas |
| Hedra | [hedra.com](https://www.hedra.com/) | Character image/asset + speech/audio and prompts | Expressive character speeches, stylized portraits | Test face/hand quality per model |
| D-ID | [d-id.com](https://www.d-id.com/) | Portrait/avatar + text/audio; agent setup for live mode | Talking portraits, live agents | API and app workflows differ |
| Captions | [captions.ai](https://captions.ai/) | Footage/AI actors/script | Social talking-head edits and creator tools | Features may be subscription-dependent |
| Arcads | [arcads.ai](https://www.arcads.ai/) | Product/offer + ad script + AI actor | UGC-style ad creative | Never imply a fictional actor used the product |
| Creatify | [creatify.ai](https://creatify.ai/) | Product info or link + AI actor | Ecommerce and branded video ads | Verify real product claims |
| Colossyan | [colossyan.com](https://www.colossyan.com/) | Text + avatar scenes | Business learning content | Not a cinematic physics generator |
| Elai | [elai.io](https://elai.io/) | Slides/script + presenter | Explainers and training | Confirm current product/support status |

### Which talking-avatar choice should you test?

- **Same presenter every week:** HeyGen or Synthesia.
- **Expressive fictional face, limited shot length:** Hedra or an expressive lip-sync route.
- **Someone who answers new questions in real time:** LiveAvatar, Tavus, or D-ID Agents.
- **Short ads:** Arcads or Creatify.
- **Your own digital twin:** Use provider consent/identity verification; do not upload another person's recording as if you own their likeness.

## 5.3 Truly real-time interactive video humans

| System | Site / docs | Core approach | Beginner caution |
|---|---|---|---|
| LiveAvatar | [liveavatar.com](https://www.liveavatar.com/) / [docs](https://docs.liveavatar.com/) | Streaming avatar + conversational controls | A custom setup may require developer work and different usage billing |
| Tavus CVI | [tavus.io/cvi](https://www.tavus.io/cvi) | Realtime video persona + perception, turn management, speech | API-first; understand session charges |
| D-ID Agents | [docs](https://docs.d-id.com/docs/agent-session-quickstart) | Avatar agent sessions streaming replies | Requires configuration, testing and moderation |
| HeyGen's live offering | [official help](https://help.heygen.com/en/articles/12758516-introducing-liveavatar) | Related to but different from pre-rendered HeyGen videos | Do not assume the Creator video plan covers extensive live sessions |

A real-time video agent may need a computer application, website or live-call interface. Merely opening its marketing page may not provide a fully configured, standalone “two AI people podcast” button.

## 5.4 Voice, music, translation, captions and sound

| Tool | Official site | Main job | Use it when |
|---|---|---|---|
| ElevenLabs | [elevenlabs.io](https://elevenlabs.io/) | Expressive voices, speech models, agents, dubbing | Voice personality matters |
| Cartesia | [cartesia.ai](https://cartesia.ai/) | Streaming low-latency voices | Building live conversations |
| Hume | [hume.ai](https://www.hume.ai/) | Expressive voice and voice-focused interactions | Emotional speech is a priority |
| Murf | [murf.ai](https://murf.ai/) | Presenter/business voiceovers | Corporate or instructional narration |
| Fish Audio | [fish.audio](https://fish.audio/) | Alternative voice generation | Comparing voices/models/terms |
| Wondercraft | [wondercraft.ai](https://www.wondercraft.ai/) | Audio conversations, podcasts and production | Generating multi-speaker audio projects |
| Gemini Notebook / NotebookLM | [Notebook](https://notebooklm.google.com/) | Source-grounded conversational Audio Overviews | Podcast-style discussions from research |
| Suno | [suno.com](https://suno.com/) | Songs / music generation | Original music with appropriate plan rights |
| Eleven Music | [ElevenLabs Music](https://elevenlabs.io/music) | AI music | Soundtrack options |
| Stable Audio | [stableaudio.com](https://stableaudio.com/) | Audio/music generation | Sound effects or musical beds |
| Adobe Podcast | [podcast.adobe.com](https://podcast.adobe.com/) | Recording enhancement and spoken audio | Cleaning poor dialogue recordings |
| Auphonic | [auphonic.com](https://auphonic.com/) | Speech leveling and sound post | Podcast or interview loudness consistency |
| Deepgram | [deepgram.com](https://deepgram.com/) | Speech recognition and voice AI | Custom live agents and transcription |
| AssemblyAI | [assemblyai.com](https://www.assemblyai.com/) | ASR, diarization and speech intelligence | Automated transcripts / speaker timing |

**Why two voice tools can be redundant:** If your video generator already gives you good synchronized speech, you may need only sound cleanup. If it produces poor speech or you need a fixed character voice over many episodes, use separate audio-generation and lip-sync steps.

## 5.5 Image, design and visual identity

| Tool | Official site | Primary value |
|---|---|---|
| Midjourney | [midjourney.com](https://www.midjourney.com/) | Filmic stills, environments and mood references |
| ChatGPT Images | [chatgpt.com](https://chatgpt.com/) | Conversational image creation and precise revisions |
| Leonardo AI | [leonardo.ai](https://leonardo.ai/) | Character, game, environment and concept assets |
| OpenArt | [openart.ai](https://openart.ai/) | Saved character identities and image/video flows |
| Higgsfield Soul ID | [higgsfield.ai](https://higgsfield.ai/) | Persistent fictional/authorized facial identity |
| Freepik | [freepik.com](https://www.freepik.com/) | Creative assets and multiple generation tools |
| Ideogram | [ideogram.ai](https://ideogram.ai/) | Titles, typography-heavy thumbnails and posters |
| Recraft | [recraft.ai](https://www.recraft.ai/) | Vectors, icons and design-oriented images |
| Canva | [canva.com](https://www.canva.com/) | Titles, graphics, basic video and social packaging |
| Blender | [blender.org](https://www.blender.org/) | Actual editable 3D models, cameras, lights, rigging and animation |

**Important 3D distinction:** A picture *styled like* 3D animation is still a flat generated image/video. If you need a truly editable mesh, skeletal rig, physically controllable camera, UV map, or game-ready asset, you may need a 3D creation and animation system such as Blender or specialized text/image-to-3D tools. Video models do not automatically provide true 3D scene files.

## 5.6 Editing and finishing

| Tool | Site | What it offers | Best for |
|---|---|---|---|
| CapCut | [capcut.com](https://www.capcut.com/) | Timeline edit, captions, effects, voice and mobile-friendly workflows | Beginners and vertical shorts |
| DaVinci Resolve | [Blackmagic](https://www.blackmagicdesign.com/products/davinciresolve) | Professional editing, color and sound | Films and ambitious series |
| Adobe Premiere | [Adobe](https://www.adobe.com/products/premiere.html) | NLE editing and Adobe interoperability | Professional producers |
| Descript | [descript.com](https://www.descript.com/) | Edit spoken videos through transcript text | Podcasts and presenters |
| InVideo AI | [invideo.io](https://invideo.io/) | Topic-to-video draft with narration/visual assembly | Faceless explainers |
| Pictory | [pictory.ai](https://pictory.ai/) | Article/script to video | Narrated content |
| OpusClip | [opus.pro](https://www.opus.pro/) | Recut long content into social clips | Repurposing podcasts/interviews |
| Topaz Video | [topazlabs.com](https://www.topazlabs.com/) | Denoise, upscale, restore and enhance | Final visual polish |
| VEED | [veed.io](https://www.veed.io/) | Online captions, edits and AI features | Collaborative/social finishing |
| Canva video editor | [canva.com](https://www.canva.com/) | Templates, captions, design and video | Simple promotional videos |
| OBS Studio | [obsproject.com](https://obsproject.com/) | Screen/video recording and streaming | Capturing interactive avatar sessions |

When working with exact source text, Descript's text-based editing is excellent; in a dialogue-heavy episode, however, don't automatically remove *every* filler sound or pause. Emotion depends on breathing, hesitation and silence. [Descript's editor](https://www.descript.com/video-editing)

---

# 6. THE END-TO-END PRODUCTION PIPELINE

![Concept to publication diagram](AI_Video_Masterclass_Assets/01_pipeline.png)

This section demonstrates how to move from an idea to a completed 45-second video using **a fictional café conversation**. It works as a general workflow for films, series, social videos and ads.

## Stage A — Define the output

Write down:

- **Audience:** Who is watching? (e.g., young adults who enjoy comedy-drama.)
- **Format:** 16:9 episode, 9:16 short, live avatar, or audio podcast with visuals.
- **Duration:** e.g., 45 seconds, 3 minutes or 10 minutes.
- **Style:** naturalistic handheld, polished commercial, 2D cartoon, documentary, etc.
- **Narrative promise:** What question or feeling keeps viewers watching?
- **Disclosure:** Could this be mistaken for genuine documentary evidence or a real person?
- **Success criteria:** “Same characters, clear dialogue, believable reaction, 1080p, no obvious hands/face errors.”

**Our worked example:** *The Apartment Upstairs*, Episode 0. Two original characters have a tense conversation in a café. The protagonist discovers something, but the video ends on a small reveal.

## Stage B — Create a series bible or single-video brief

**Minimum facts for each character:** name/ID, appearance, clothes, accent, distinctive mannerisms, motivation, relationships and authorized voice/reference files. **For each location:** a still image, lighting, camera geography, major furniture/props and permitted changes between shots.

## Stage C — Generate still references and approve them

A solid character-reference package includes a front-facing portrait, left/right three-quarter angle, waist-up view, full-body view, neutral/angry/happy expressions and costume references. Label them unambiguously: `MAYA-01_front.png`, `MAYA-01_3q_left.png`, etc. Do not feed every image to a model that only supports one reference; follow the input specification for that mode.

**Quality gate:** Does the face look like the same *original* person across stills? Are hairstyle, proportions, complexion and wardrobe clear? Resolve issues *before* spending expensive video credits.

## Stage D — Design the voice

Choose an authorized voice from the provider or record the original performance. Save voice IDs/configuration and pronunciation guidance. Generate a short test with names, laughter, disagreement and a normal sentence. Listen critically for rhythm and accent authenticity.

For a regional voice, **don't equate “English spoken in a country” with a generic accent preset**. If the voice model does not accurately represent an accent, use an original voice actor or a verified authorized voice sample rather than forcing stereotypical pronunciation.

## Stage E — Break the scene into shots

![Six-shot pilot storyboard](AI_Video_Masterclass_Assets/04_storyboard.png)

| Shot ID | Length | Picture | Audio | Production technique |
|---|---:|---|---|---|
| 01 | 6 s | Exterior/establishing café | Street ambience | T2V or I2V with no speaking |
| 02 | 7 s | Maya close-up | “You knew, didn't you?” | Voice-first lip-sync or native dialogue |
| 03 | 7 s | Daniel close-up | “I wanted to tell you.” | Same fixed voice & reference |
| 04 | 8 s | Two-shot | Interruption, nervous response | Generate shot or composited reaction |
| 05 | 9 s | Maya listening | Silence + chair sound | I2V reaction shot |
| 06 | 8 s | Wider reveal | Short final line + café noise | Native shot or controlled image-to-video |
| **Total** | **45 s** | | | |

Use **one main action per generation**. A fifteen-action prompt often produces confused action and camera cuts. Generate several takes, record what failed and keep an alternate shot that can cover an awkward transition.

## Stage F — Generate the video

**Basic steps in most apps:** Open a project → select video mode → select model/quality/aspect ratio → upload permitted references → paste prompt → specify duration if offered → preview credit estimate → generate → inspect frame by frame → save approved output and metadata.

**Model choice by shot:**

- 01 café wide shot: a visually strong cinematic video generator.
- 02/03 dialogue: a speech-specific avatar/lip-sync system for exact words or a native-audio video generator for spontaneous short lines.
- 04 two-person conversation: separate speakers and reactions if multi-person lip sync breaks down.
- 05 silent reaction: image-to-video can work well because there is no exact speech to match.
- 06 transition/reveal: a cinematic model or keyframe-based generation.

## Stage G — Edit

Make a timeline, arrange best takes, trim weak first/last frames, add audio, balance volume, add titles and optional subtitles. Verify that reaction shots line up with what the other character said. When time permits, create J-cuts and L-cuts: let sound continue across a picture cut.

## Stage H — Quality-control and export

Watch with sound and then without sound. Look at hands, mouths, eyes, props, logos, text, lighting, direction of movement, room tone, voice identity and continuity. Export the needed aspect ratio and inspect the compressed upload file on a phone as well as a desktop.

**Practical starter delivery:** 1080 × 1920 for Shorts/Reels/TikTok, or 1920 × 1080 for standard YouTube/TV-style widescreen, provided your assets actually support the resolution. Use widely compatible H.264 MP4 if your editor and platform support it; adjust fps to the source and delivery standard rather than inventing extra frames unnecessarily.

---

# 7. TRULY UNSCRIPTED, IMPROVISED AND SEMI-SCRIPTED AI VIDEOS

This is the core difference between a human-looking AI video and an AI video that *thinks and responds*. There are **six production methods**, each with different complexity and creative control.

## 7.1 Method A — Spontaneous dialogue generated within one video prompt

**What happens:** You supply a scenario, characters and emotional beats; the audiovisual video model invents a short exchange. **Not truly live**: the whole clip is generated as one asset.

**Ideal for:** 5–15 seconds of casual conversation, funny skits, unexpected reactions, scene tests.

```text
Create one continuous 8-second fictional scene in a modest café.
Two original adult friends, Maya and Daniel, discuss a surprising message.
Maya starts with a skeptical question. Daniel answers with amused hesitation.
Generate believable conversational wording suited to this short shot.
Natural eye contact, gentle hand movement, real listening reactions.
Warm window light, subtle handheld medium two-shot, café room tone.
No narration, no on-screen text, no formal presentation style.
```

**Problems:** The model might choose trivial dialogue, switch speakers, invent a different language, lose lip sync, or end mid-word. Ask for one short conversational beat rather than a whole argument.

## 7.2 Method B — Automatically improvised transcript, then rendered

**What happens:** An LLM writes lines from a situation without you manually scripting every word; you render speech afterward. This is *semi-scripted production* because the completed transcript becomes fixed before audio/video rendering.

**Recipe:**

1. Ask a language model to create two characters with contrasting goals.
2. Define an ordinary topic plus a hidden tension.
3. Generate **one turn at a time**, not an uninterrupted essay.
4. Review each line for realism, factual safety and repetitive phrasing.
5. Split by speaker; assign saved voice IDs.
6. Synthesize and save audio for each speaker.
7. Animate each face or generate reaction clips.
8. Edit the dialogue into a believable rhythm and publish.

**Copy-ready conversation instruction:**

```text
You are the dialogue director for a fictional two-person podcast.
Characters:
- MAYA: witty, direct, skeptical, sometimes teases; concise phrases.
- DANIEL: measured, curious, politely disagrees; avoids lectures.
Topic: Does social media improve romantic relationships?
Rules:
- Generate 14–20 speaking turns; each turn normally 1–3 sentences.
- Make replies react to the *previous* turn, not to a generic outline.
- Include one misunderstanding, two clarifying questions, and a real change of mind.
- Occasional laughter or silence is fine, but never insert constant fillers.
- Do not invent facts or quote fake survey statistics.
- End with a memorable question, not a generic call-to-action.
- Output a table: speaker | line | emotional intent | suggested shot.
```

**Why this often beats native dialogue:** You control the exact words, audio, captions and editing. It can feel spontaneous even though you rendered a fixed conversation after approval.

## 7.3 Method C — AI podcast from sources

**What happens:** You provide reading material to a source-grounded notebook/podcast tool; it generates an Audio Overview or host-style discussion. Google’s NotebookLM/“Gemini Notebook” branding may depend on product interface and account. [Google's Audio/Video Overview descriptions](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/)

**Best for:** Explaining complicated material in a friendly back-and-forth voice.

**Steps:** Upload trustworthy sources → select Audio Overview → choose length/focus where offered → listen and fact-check → obtain authorized/exportable audio → use an editor to add slides, source visuals or animated hosts. Do not assume the audio is suitable for commercial reuse without checking the product's terms and source rights.

**Caution:** AI hosts can simplify inaccurately or misrepresent the certainty of your sources. Check quotes, statistics and claims.

## 7.4 Method D — Truly live human ↔ AI video host

**What happens:** A human asks a question and a video-avatar agent replies without a fixed transcript. Products to investigate: Tavus, LiveAvatar and D-ID real-time agents.

**Practical sequence:**

1. Create an original or consented avatar/persona.
2. Set the voice and conversational language.
3. Write instructions about personality, topic limits, response length, and what the agent must admit it does not know.
4. Set up the live session through the product's dashboard or documented integration.
5. Test microphone input, interruption behavior, speech delay, connection quality and audio clipping.
6. Record a session with clear permission using the app's recording feature, OBS or another supported recorder.
7. Edit the best portions into a publishable video; disclose the AI host appropriately.

**Persona prompt example:**

```text
IDENTITY: You are AMINA, an original fictional adult AI science-show host.
Your existence as an AI character must be clear to viewers.
OBJECTIVE: Interview a human about a new science idea using follow-up questions.
STYLE: Curious, grounded, warm, occasional light humor; no speeches.
VOICE: Speak in complete but short turns (normally 10–35 words).
LISTENING: Acknowledge the answer before asking a follow-up.
TRUTH: Do not invent research, publications, quotes or measurements.
CONVERSATION: If interrupted, stop speaking and respond to the new input.
BOUNDARIES: Never claim to be a real human or a licensed professional.
ENDING: After 8–12 useful exchanges, ask one closing question and summarize.
```

**Live technical requirements:** stable connection, audio input/output permissions, mic monitoring, turn detection/VAD, speech recognition if used, TTS or native speech output, avatar video stream, session time limits, storage permission and a moderation strategy.

## 7.5 Method E — Two autonomous AI agents talking to each other

This is the closest to a *fully AI-run unscripted show*. Do not run two agents in an uncontrolled infinite loop. Give them distinct roles, a moderator, and a clear stopping rule.

**A safe architecture:**

```text
Show producer sets topic / word limits / factual sources
                    ↓
           HOST A (LLM persona)
                    ↓ spoken/text turn
           HOST B (LLM persona)
                    ↓ spoken/text turn
          MODERATOR / CONTROLLER
        ┌───────────┴───────────┐
   Continue?                  Stop?
   New turn                   Final wrap-up
        ↓                          ↓
  Voice synthesis             Mix / edit / publish
        ↓
  Audio-driven avatar for A and B
```

**Pseudo-code, not a provider API implementation:**

```python
max_turns = 18
history = []
for turn in range(max_turns):
    speaker = "Maya" if turn % 2 == 0 else "Daniel"
    reply = generate_llm_turn(
        persona=personas[speaker],
        conversation=history[-10:],
        facts=approved_source_notes,
        max_words=45,
    )
    if violates_rules(reply) or repeats_prior_turn(reply, history):
        reply = revise_turn(reply, constraints="short, specific, grounded")
    history.append({"speaker": speaker, "text": reply})
    audio = synthesize_voice(reply, approved_voice_id[speaker])
    save_audio_and_transcript(turn, audio, reply)
    if producer_or_moderator_says_end(history):
        break
render_and_edit_session(history)
```

**Real engineering considerations:**

- **Interruption and turn-taking:** Avoid simultaneous audio unless you intentionally support cross-talk; most talking-avatar renderers don't naturally support overlapping speakers.
- **Memory window:** Summarize important previous turns so the conversation stays coherent.
- **Fact boundaries:** For non-fiction topics, restrict claims to a retrieval-supported source packet and allow “I don't know.”
- **Repetition control:** Detect paraphrased repetition, not just exact matching strings.
- **Safety:** Prevent defamatory gossip about real people, harmful impersonation and fabricated accusations.
- **Stop condition:** Duration, maximum number of turns, topic exhaustion or moderator signal.
- **Production:** Save isolated WAV/MP3 tracks by speaker and the transcript, not just one combined recording.

## 7.6 Method F — Human-directed improv, AI-performed

A *human director* provides the first line or acting audio, the AI improvises the reply, and the person keeps directing. This is a highly controllable hybrid for film scenes: you retain the spontaneous energy but don't surrender the story to an uncontrolled agent.

### When to use each method

| If you need… | Choose… |
|---|---|
| Short made-up conversation, no exact words | A: native video audio |
| Good edited storytelling, exact captions | B: transcript then audio/video |
| Discussion from source documents | C: source-based audio overview |
| A digital human responding to a viewer | D: live human ↔ AI avatar |
| A podcast with two AI-run hosts | E: two agents and a moderator |
| Natural acting with strong creative control | F: directed improvisation / speech-to-speech |

---

# 8. MAKING VOICES SOUND HUMAN

The secret is not a “humanize” switch. It is control over **performance, pace, pronunciation, emotional intention, the recording chain, and the mix**.

## 8.1 Voice construction step by step

1. **Choose an ethical voice source:** a licensed platform voice, an actor who agreed to the use, or your own voice.
2. **Create a voice identity card:** vocal age range, register, accent, pace, energy, diction, laugh style, emotional range.
3. **Create a short voice test:** 4–6 lines containing a question, ordinary statement, excitement, a name, and disagreement.
4. **Pick the model according to goal:** expressive TTS for drama, lower-latency TTS for live agents, stable narration model for long content.
5. **Generate in short segments:** easier to replace one bad sentence without rerendering an entire episode.
6. **Direct the acting:** specify intention, not just an emotion label. “Trying not to sound worried” is more useful than “sad.”
7. **Listen to audio without video:** bad audio acting becomes obvious when you remove the visual distraction.
8. **Process gently:** remove hiss and clicks; don't over-compress and eliminate every breath.
9. **Save the voice IDs, settings and pronunciation dictionary** for later episodes.

## 8.2 How to direct emotion

| Weak direction | Better direction | Why it works |
|---|---|---|
| “Make her sad” | “She is trying to sound normal while hiding disappointment” | Specific inner conflict |
| “Angry man” | “He keeps his voice low because someone is sleeping nearby” | Controls volume and tension |
| “Happy voice” | “She receives unexpectedly good news, then catches herself laughing” | Gives a progression |
| “Natural conversation” | “Reply to the other person's last question in 1–2 sentences, then wait” | Sets realistic turn length |
| “Ugandan accent” | “Use a natural, tested Ugandan English voice if offered; preserve clear pronunciation of named words” | Avoids caricature and model guesswork |

Some ElevenLabs models support performance/audio tags and multi-speaker synthesis. The exact tags and input syntax vary; follow [its model documentation](https://elevenlabs.io/docs/overview/models) rather than assuming every engine interprets them identically.

## 8.3 A complete emotional line example

**Context:** Maya thinks Daniel concealed a family secret. She isn't shouting; she is hurt.

**Flat dialogue:** “You knew about it. Why didn't you tell me?”

**Performance note:** *Keep the first sentence quiet and certain. Pause. Ask the second question more slowly, with disappointment, not rage.*

**Edit note:** Keep 300–700 ms of purposeful silence before Daniel replies, then show his reaction before the first word. That pause may do more for realism than a high-cost video model.

## 8.4 What “humanization” should not mean

Avoid random filler words (“um” every sentence), manufactured stutters, aggressive breath insertion, unnecessary background noise, fake claims of being a real person, and unlicensed celebrity/creator voice cloning. **A believable human performance has intentional imperfections, not random errors.**

### Regional accents and multilingual production

Always test proper nouns, currencies, local expressions, code-switching, and speech rate with a native listener. The availability of “English” does not guarantee authenticity for a particular locality. Translation must also preserve tone, politeness and idioms; a word-for-word dub can be grammatically correct but socially unnatural.

### Rights caution for cloning

ElevenLabs documents separate instant/professional cloning rules and professional verification. Importantly, its own cloning guidelines state that you cannot create a Professional Voice Clone of another person simply because they provided a sample or consent—use the permitted alternatives such as sharing their own verified voice under that service's rules. Read the current [voice cloning overview](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning) and [use policy](https://elevenlabs.io/use-policy).

---

# 9. MAKING AI PEOPLE AND PERFORMANCES LOOK HUMAN

## 9.1 The seven layers of visual believability

1. **Identity:** A recognizable consistent face, body proportions, clothing and hair.
2. **Motion:** Plausible movement of the neck, shoulders, eyes and hands.
3. **Speech synchronization:** Mouth shapes roughly match phonemes and timing; jaw movements are not exaggerated.
4. **Expression:** Smiling, frowning, gaze changes and reaction beats are motivated by what happens.
5. **Physical continuity:** Objects remain stable; fingers grasp rather than melt through objects.
6. **Image realism:** Lighting, skin detail, hair and depth remain consistent with the environment.
7. **Sound realism:** Room tone, dialogue position, music and sound effects fit the apparent scene.

## 9.2 Build a reliable reference character

![Character reference feeding recurring episodes](AI_Video_Masterclass_Assets/05_character_bible.png)

Create the following assets for an **original fictional** actor:

```text
characters/
  MAYA-01/
    identity.md                 # canonical description
    front.png                   # primary approved reference
    three_quarter_left.png
    three_quarter_right.png
    full_body.png
    expression_neutral.png
    expression_surprised.png
    wardrobe_default.png
    voice_test.wav
    voice_config.md
    continuity_notes.md
```

**Identity card:**

```yaml
id: MAYA-01
name: Maya
fictional: true
age_in_story: 28
appearance:
  complexion: deep brown
  hair: shoulder-length natural twists
  eyes: warm brown
  silhouette: average height, relaxed posture
wardrobe_default: mustard jacket, charcoal top, dark jeans
voice:
  source: licensed_original_voice
  accent: natural tested voice; avoid accent stereotypes
  pace: quick when excited, slower when upset
mannerisms:
  - pauses briefly before a joke
  - holds eye contact when challenging someone
continuity_rules:
  - never alter the character's identity between shots
  - retain jacket color in consecutive café scenes
  - keep voice profile stable across episodes
```

### Three approaches to recurring character consistency

- **Reference images:** Fastest beginner option. Use the same vetted image(s) in every shot where supported.
- **Named character systems:** LTX Studio Elements, OpenArt Characters and Higgsfield Soul ID offer structured ways to reuse a character asset. Features differ, but all aim to reduce repeated identity drift. [LTX Elements guide](https://ltx.io/blog/how-to-create-a-consistent-character) · [OpenArt help](https://openart.ai/help/) · [Higgsfield overview](https://higgsfield.ai/creator-hub/help-center/getting-started/what-is-higgsfield)
- **Fine-tuned models/LoRAs:** Advanced local workflow using properly licensed reference datasets. More setup, but often useful for a large universe with many recurring views.

None guarantees absolute identity preservation. Check eyes, jawline, hairline, teeth, hands, clothing, props and color relationships frame by frame.

## 9.3 Direct a human-like performance

Instead of writing “very realistic person speaking,” describe the *observable behavior*:

> “Maya looks at Daniel after he finishes. She holds her gaze for half a second, glances at his phone, then answers with a restrained smile. Her shoulders remain relaxed. She is not making a dramatic gesture.”

That is clearer than: “extremely realistic, perfect acting, lots of emotion, beautiful cinematic video.”

**Direction to avoid:** Six emotions at once, constant head motion, every actor speaking simultaneously, complex hand-object interactions within a few seconds, exaggerated movie camera motion at all times.

## 9.4 The audio-first technique

For important dialogue:

1. Generate or record final acting audio.
2. Lock the waveform and sentence timing.
3. Animate speaker A for A's line; animate speaker B for B's line.
4. Create extra silent listening/reaction shots.
5. Cut between the speakers, sometimes showing the listener while the speaker continues.
6. Add ambient sound and subtle continuity effects.

This frequently produces more convincing dialogue than a single complicated two-person prompt.

## 9.5 Realistic phone footage versus film footage

**Phone-video realism:** Less stylized light, moderate handheld movement, ordinary backgrounds, imperfect framing, realistic exposure and typical phone perspective. Avoid fake phone UI overlays suggesting the footage is authentic if it is not.

**Cinematic realism:** Controlled lighting, deliberate focal length/perspective, motivated motion, planned composition, shot/reverse-shot continuity, expressive sound design and consistent grading.

**Aesthetic realism is not historical authenticity.** A realistic-looking AI “news clip” is still synthetic. Label it clearly where appropriate.

---
# 10. CONSISTENT CHARACTERS, LOCATIONS AND RECURRING SERIES

Producing a series is closer to running a small animation studio than making a single social post. The challenge is not simply “generate 20 minutes.” It is **recreating a consistent fictional world in thousands of individual visual and audio decisions**.

## 10.1 The five documents every series needs

1. **Series bible:** premise, tone, theme, setting, ongoing questions, audience promise and boundaries.
2. **Character bible:** physical references, voice, mannerisms, relationships, goals, contradictions and what each character knows.
3. **Location bible:** establishing photos/art, room layout, furniture, lighting, ambient audio, geography and recurring props.
4. **Season arc:** major conflict, episode hooks, reversals, resolutions and how the characters evolve.
5. **Continuity log:** final decisions after each finished episode; costumes, dates, prop status, injuries, secrets and events must remain consistent.

## 10.2 Example: develop a six-episode fictional mini-series

**Title:** *The Apartment Upstairs*  
**Format:** Six episodes × 3 minutes  
**Genre:** Urban comedy-drama  
**Audience:** Short-form episodic fiction viewers  
**Logline:** Maya, a sharp-tongued tenant, becomes convinced the quiet person upstairs is hiding a secret, but each attempt to investigate creates a new misunderstanding.

| Episode | Main story problem | Emotional turn | End hook |
|---|---|---|---|
| 01 | Strange sounds in the building | Curiosity → suspicion | A note appears under Maya's door |
| 02 | A misunderstood conversation | Suspicion → embarrassment | Daniel recognizes the handwriting |
| 03 | A missing package | Accusation → doubt | A camera reveals a surprising visitor |
| 04 | The visitor's real purpose | Pride → vulnerability | Maya must ask for help |
| 05 | The secret comes to light | Conflict → relief | Someone else has misunderstood them |
| 06 | Neighbors work together | Reconciliation | A funny last reversal opens a future season |

Each episode needs **one contained dramatic question**. Short AI series benefit from strong scene boundaries because maintaining continuity across dozens of cuts can be costly.

## 10.3 Plan one episode with a beat sheet

An episode beat sheet answers *why this scene exists*. Example for a three-minute episode:

| Time | Beat | Visual strategy |
|---|---|---|
| 0:00–0:12 | Hook: the strange sound returns | Quick sound-led establishing shot |
| 0:12–0:35 | Maya investigates | Two short I2V shots with location reference |
| 0:35–1:15 | Maya and Daniel argue | Audio-first shot/reverse-shot |
| 1:15–1:50 | They find a clue | Insert of a recurring prop, reaction close-ups |
| 1:50–2:32 | Wrong assumption exposed | Dialogue close-ups + wide shot |
| 2:32–3:00 | Reveal/cliffhanger | Controlled hero shot + final audio beat |

For each beat, list camera size, emotion, reference assets, speaking order and whether the motion is simple or difficult. If you only need a close-up reaction, avoid spending credits on a scene with five people walking, dancing and speaking at once.

## 10.4 Maintaining set geography

Conventional films obey spatial relationships; AI clips often don't. Draw an overhead map of the room. Mark doors, windows, actors, eyelines and the side of the conversation where the camera will stay. Without that, your edit may show a window on the left in one shot and on the opposite wall in the next.

**180-degree rule:** For a dialogue, imagine a line between the two characters. Keep your main cameras on the same side of that line unless you deliberately motivate crossing it. This maintains screen direction and eyelines.

## 10.5 Save approved takes and settings

```text
TheApartmentUpstairs/
  00_ADMIN/
    budget.csv
    production_log.csv
    licenses_and_permissions.md
  01_BIBLE/
    show_bible.md
    season_outline.md
    continuity_log.md
  02_CAST/
    MAYA-01/
    DANIEL-01/
  03_SETS/
    cafe/
    apartment/
  04_AUDIO/
    voices/
    dialogues/
    ambience/
    music/
  05_EPISODES/
    E01/
      beat_sheet.md
      shot_list.csv
      references/
      generations/
      approved/
      project_files/
      exports/
  06_MARKETING/
    thumbnails/
    trailers/
    subtitles/
```

Store **prompt, model/version, setting, source references, generation ID, seed (if exposed), credit cost, result, issue and final acceptance status**. This is invaluable when revising Episode 1 or recreating a location months later.

## 10.6 Keeping voices consistent across a season

Save the selected voice ID, model version, speaking pace, notes on pronunciation, voice processing chain, and approved benchmark line. If you change the model, compare the same line before switching an established character. Consider human direction/performance notes as part of the voice bible.

## 10.7 A practical reality about long episodes

A 20-minute episode is 1,200 finished seconds. If your average *usable* shot is 7 seconds, the timeline may need roughly 172 shots, before transitions and cutaways. More dialogue can use longer held shots, while action may need more cuts. **This is an illustration, not a universal shot count.** The real production bottleneck is often generating *approved footage*, not generating initial attempts.

---

# 11. ANIMATION, CARTOONS, ANIMALS, FANTASY AND SPECIAL FORMATS

## 11.1 Cartoon series

**Recommended approach:** Define a strong style bible (line weight, palette, proportions, character silhouettes, backgrounds) → generate consistent still characters → create a small set of expressions and poses → animate short scenes → record voices → edit with consistent music and sound design.

**Example cartoon prompt:**

```text
Original 2D animated comedy, clean hand-painted backgrounds and restrained
character animation. Two fictional animal roommates discuss a missing cake.
Use character reference images exactly for visual identity and costumes.
One shot: medium shot of the rabbit turning slowly toward the fox, raising
one eyebrow; no spoken dialogue in this generation. Keep the room layout,
line style and color palette identical to the approved setting sheet.
```

**Why silent generation can help:** Cartoon character art may animate nicely without accurate talking mouth shapes. Add deliberate audio-driven mouth animation afterward for reliable dialogue.

## 11.2 Talking animals

Combine original animal-character art with expressive voice and compatible audio-driven animation. Do not expect every human-avatar model to handle nonhuman mouths or moving ears. Test a brief 5–10 second clip with a simple sentence and reaction. For an anthropomorphic animal, a consistent mouth/snout shape matters more than perfect photorealistic fur.

## 11.3 Music videos

1. Use **your own composition** or licensed music, or generate original music under a plan allowing the intended use.
2. Build a mood board from the beat, lyrical themes and color palette.
3. Map musical phrases, drops and transitions to shot changes.
4. Generate hero frames and short clips; avoid trying to lip-sync a fast complete song in one take.
5. Edit on the beat, but preserve visual storytelling beyond constant cutting.
6. Check music copyright, composition/master rights, image rights and platform rules before publishing.

**Music edit sheet example:** 0–8 s mysterious opening; 8–20 s verse with character; 20–30 s build; 30–45 s chorus and energetic camera; 45–60 s visual resolution. Adjust to the actual track.

## 11.4 Advertisements / product videos

**Always start with the product facts.** For a physical object, collect real and accurate front/back photos, dimensions, functions, disclaimers, availability and permitted logos. Use generative clips for creative context; use actual product footage where precision matters. Do not invent product capabilities, fake customer experiences or “before and after” evidence.

**Ad structure:** Hook → problem → product accurately introduced → genuine differentiator → demonstration → action. Use Arcads/Creatify/HeyGen for actor-style ad delivery, and a video generator for visual B-roll only where needed.

## 11.5 Historical and documentary content

Use original narration, primary research, licensed archives and clearly designated illustrations/reconstructions. Never label AI-created depictions as “actual archival footage,” and distinguish uncertain interpretations from evidence. Interview-style reenactments should not falsely appear to feature a real historic person's authentic voice or direct words.

## 11.6 Architectural, real-estate and product visualization

Reference-first generation can animate concept images, but model outputs can invent walls, windows, measurements, doors and product details. Treat generated visuals as conceptual unless verified against actual plans or photographed property. A beautiful rendered camera walkthrough is not a measured building survey.

## 11.7 Interactive stories and games

A live conversation agent makes sense if viewers can influence responses; a prerecorded story is more reliable if the narrative must follow an exact arc. For a playable character in a real game, you may also need character rigs, state machines, asset formats and the engine's runtime (Unity, Unreal, Godot, etc.). Generating a film clip does not produce a functional game character.

---

# 12. CAMERA DIRECTION, EDITING AND AUDIO POST-PRODUCTION

![Example multitrack timeline of an AI video](AI_Video_Masterclass_Assets/06_editor_timeline.png)

## 12.1 Film grammar every AI creator should learn

| Term | Meaning | Why it matters |
|---|---|---|
| Establishing shot | Wide view showing location | Orients viewer and covers continuity gaps |
| Wide shot (WS) | Whole bodies/setting | Action and geography |
| Medium shot (MS) | Waist-up or similar | Conversational body language |
| Close-up (CU) | Face/important detail | Emotional response |
| Insert shot | Focus on object/phone/note | Story facts without demanding complex acting |
| Reaction shot | Listener processing event | Makes dialogue believable |
| Shot/reverse-shot | Alternating views between speakers | Builds conversations from separate renders |
| Static camera | Little or no movement | Most reliable for talking faces |
| Handheld | Small organic camera motions | Documentary and phone-video feel |
| Dolly / tracking | Camera moves with subject | Creates motion depth; can stress generation |
| Pan / tilt | Camera rotates | Reveals scene geography |
| Rack focus | Shift focus between subjects | Directs attention; requires coherent depth |
| Match cut | A visual/action relationship links two cuts | Hides changes when executed carefully |
| J-cut | Next scene's audio starts before picture cut | Natural conversation transitions |
| L-cut | Previous scene's audio continues over new picture | Emphasizes reactions and avoids jumpiness |
| Room tone | Continuous ambient sound | Unifies separately generated shots |

A good prompt typically defines camera **size**, **movement** and **subject action**; but adding five camera movements in a six-second clip is counterproductive. [Runway prompting guide](https://academy.runwayml.com/guides/prompting-guide) · [Google Veo guide](https://deepmind.google/models/veo/prompt-guide/)

## 12.2 A beginner shot-edit workflow in CapCut

1. Create a new project and select 9:16 or 16:9 as appropriate.
2. Import approved AI-generated video clips and the dialogue audio.
3. Put the main video clips on the timeline in storytelling order.
4. Add and align audio tracks; turn off duplicate embedded audio where inappropriate.
5. Trim starts/ends to remove generation glitches.
6. Cut to reaction shots where lips or body motion are weak.
7. Add room tone across the entire scene; use fades at clip boundaries.
8. Add subtitles, checking every word and speaker.
9. Balance audio; reduce background music during important speech.
10. Export and inspect the finished file, not just the editor preview.

**Why generate isolated audio tracks?** If a voice line sounds wrong, you can replace only that voice while keeping the other character and music intact.

## 12.3 Professional sequence in DaVinci Resolve/Premiere

Organize bins by episode/scene/shot, set project resolution and frame rate, synchronize dialogue, create picture edit, do sound editing, color-match shots, add visual effects, subtitles, delivery titles, and export multiple masters for different platforms. Save the editable project and source media, not just the final MP4.

## 12.4 Sound design for realism

- **Ambience:** A consistent café/room tone bridges cut points; use licensed or original effects.
- **Foley:** Small physical sounds (cup down, footsteps, chair, keys) create credibility.
- **Dialogue:** Main focus; avoid drowning it with constant music.
- **Space:** A large hall needs different reverberation from a bedroom.
- **Continuity:** A motorbike that passes in one angle should not restart unnaturally in the next.
- **Music:** Use for emotional structure rather than covering poor scenes.

You can often make a mediocre-looking generated scene feel more watchable by carefully selecting reaction timing and mixing good sound. You cannot fully repair a visibly deformed face with music.

## 12.5 Formats and delivery

| Aspect | Common use | Typical canvas |
|---|---|---|
| 9:16 | Shorts, Reels, TikTok | 1080 × 1920 |
| 16:9 | YouTube, widescreen film | 1920 × 1080 |
| 1:1 | Some social/advertising placements | 1080 × 1080 |
| 4:5 | Feed posts and some advertisements | 1080 × 1350 |

Generated “4K” may mean native 4K, a high-quality render, or an upscale—check the model/output method. Keep an editable master, a distribution MP4, a subtitle file (SRT or VTT), clean audio stems where possible, a thumbnail and an asset/license record.

---

# 13. EIGHT COMPLETE WORKED VIDEO RECIPES

Each recipe includes the stack, what to prepare, a concrete procedure and the test that tells you whether it worked. Product interfaces are subject to change; steps are intentionally expressed as stable tasks rather than unreliable button coordinates.

## Recipe 1 — 30-second realistic talking AI host

**Target:** A fictional adult host gives a cheerful short introduction to a science channel.

**Stack:** Character portrait or approved avatar → HeyGen or Hedra → CapCut.

**Inputs:** Character ID, 75–95 words of text, approved voice, 9:16 layout, channel title.

**Process:**

1. Create/select an authorized AI avatar; approve the face and framing.
2. Write an intro in conversational sentences rather than formal announcements.
3. Choose a voice consistent with your character; test one line before the full piece.
4. Generate the speaking video using text or pre-generated audio, as supported.
5. Watch for lip timing, blinking, hand gestures and words cut at beginning/end.
6. Put the clip in CapCut, insert title/captions and optional B-roll, and export vertically.

**Example intro:** “Why does your phone know where you are, even when the map app is closed? Today we'll explain the main signals it uses, what they can and can't reveal, and which settings actually change location access.”

**Pass condition:** The lips follow the words; pronunciation is clear; the presenter looks consistent; the claims can be supported.

## Recipe 2 — 45-second fictional cinematic scene

**Stack:** ChatGPT/Midjourney/OpenArt images → Google Flow or Kling → ElevenLabs if exact dialogue is needed → CapCut/Resolve.

**Procedure:** Create two character reference images → create café setting image → generate an establishing shot → record/generate two short lines → create each character's speaking close-up → create a silent reaction → generate the final reveal → edit using the [storyboard](#stage-e--break-the-scene-into-shots). For native video audio, compare its performance to the separate voice approach before spending credits on a full scene.

**Pass condition:** Clear geography, recognizable people, plausible performance and a beginning/middle/end. The objective is **one finished story**, not five attractive unrelated video clips.

## Recipe 3 — Unscripted two-host audio podcast with animated heads

**Stack:** Language model or Gemini Notebook → ElevenLabs/Wondercraft if you want controlled voices → two original host portraits → Hedra/HeyGen → Descript/CapCut.

**Procedure:** Supply source brief → instruct the AI hosts to alternate short turns and ask questions → review for factual claims → generate separate audio tracks by host → animate each host in short takes → create silent listener shots → cut together → add podcast set graphics and captions.

**Important:** This is *not live autonomous conversation* unless turns are actually generated and spoken during the session. It's more controllable and usually easier to publish.

**Pass condition:** Each line clearly responds to the preceding line, voices are distinct and no single host gives a five-minute essay unless the format intentionally calls for it.

## Recipe 4 — Live interactive AI interviewer

**Stack:** Tavus / LiveAvatar / D-ID agent → approved fictional avatar → desktop microphone and streaming setup → OBS recording → editor.

**Procedure:** Set AI-host persona → configure questions and allowed source packet → test conversation for latency and interruptions → record a real session with informed participant consent → verify no unsafe or unsupported claims → edit the session → label the avatar appropriately.

**Pass condition:** The host responds to *new unanticipated answers*, not just plays back previously scripted lines.

## Recipe 5 — A three-minute episode pilot

**Stack:** LTX Studio + character reference system + Kling/Runway/Seedance + voice tool + Resolve.

**Procedure:** Build cast/location bible → create 8–12 narrative beats → split beats into 25–40 potential shots as needed → select which shots need exact dialogue → generate references and footage → use continuity log → combine picture/audio → quality-control → save a reusable episode template.

**Pass condition:** The same protagonists are recognizable across scenes and the story remains coherent without reading explanatory captions.

## Recipe 6 — Animated animal comedy short

**Stack:** Original illustrated animal character + reference-based animator/video model + expressive audio + editor.

**Prompt:**

```text
Original family-friendly 2D animated scene. A clever fox holds an empty cake
plate, trying to appear innocent while a rabbit points at crumbs on the table.
One restrained comic reaction: the fox blinks twice and slowly looks at the
crumbs. Preserve the approved character sheet, palette, line art and props.
Fixed medium two-shot. No text or speech generated in this visual pass.
```

Generate a short spoken exchange separately and animate mouth motion with a tool that supports the chosen animal style. If the lip-sync tool cannot handle snouts, redesign the shot as a reaction/voiceover scene and keep the animal silent on screen.

## Recipe 7 — Faceless factual explainer

**Stack:** Research + voice recording or ElevenLabs → licensed/generative B-roll → InVideo/Pictory/Descript/CapCut.

**Procedure:** Pick a precise question → research and record sources → outline four factual beats → draft clear narration → create a visual plan for each sentence → assemble real sources/illustrations → mark synthetic reconstructions where applicable → edit for pacing → correct captions and publish.

**Pass condition:** The video tells the audience something true, evidenced and original—not just generic stock footage behind a robotic paragraph.

## Recipe 8 — Multilingual product training video

**Stack:** Real product demonstration + original voice/approved avatar → HeyGen/ElevenLabs dubbing → editor.

**Procedure:** Film or verify the real product process → finish an accurate primary-language version → translate with terminology glossary → human-check the target language → generate dub and optional permitted lip sync → add localized subtitles → review cultural context and product claims → export each language variant.

**Pass condition:** A native speaker verifies the terminology and the video does not visually misstate the product's behavior. [ElevenLabs dubbing](https://elevenlabs.io/docs/overview/capabilities/dubbing) · [HeyGen translation languages](https://help.heygen.com/en/articles/11391941-video-translation-languages-we-support)

---

# 14. THE PROMPT ENGINEERING MASTERCLASS

![Anatomy of the prompt](AI_Video_Masterclass_Assets/07_prompt_formula.png)

A strong prompt is a *small production brief*. Describe observable subject/action, not ten abstract adjectives. The more you can supply as stable references, the less the model has to invent.

## 14.1 The core prompt formula

```text
[Subject identity/reference] in [place and time].
[One specific action or interaction].
[Camera framing] + [one movement or fixed camera].
[Light and visual aesthetic].
[Relevant emotion and body language].
[Sound: exact words OR general dialogue cue OR ambience].
[Aspect ratio, duration and no-go constraints as supported by model].
```

For native dialogue, add an optional `SPEAKER A:` / `SPEAKER B:` section if the target model supports clearly marked dialogue; otherwise treat it as descriptive text and verify the output. Not every model reliably executes explicit speaker tags.

## 14.2 Prompt pair: weak versus good

**Weak:** `A woman is shocked by a message. Cinematic, 4k, hyperrealistic.`

**Better:**

```text
A medium close-up of Maya, an original fictional woman matching the supplied
character reference, in a quiet café at 4 p.m. She reads a message on a phone,
pauses, lowers it and looks toward her unseen friend. Her expression shifts
from confusion to restrained disbelief. Warm natural window light, static
shoulder-level camera, shallow background depth, subtle café ambience.
One continuous 7-second action; no dialogue, no titles, no extra people.
```

Why better: the shot has a start, visible change, defined duration, camera and audio. It isn't asking the generator to invent the entire story.

## 14.3 Copy-ready prompt pack: 12 scenarios

### A. Realistic casual phone vlog

```text
Original fictional adult creator speaking informally to a phone camera in a
normal bedroom. Simple daylight, realistic skin and background detail,
slightly imperfect but steady handheld framing. She explains one helpful tip
in conversational English, with thoughtful pauses and restrained gestures.
No dramatic camera moves, false phone interface, exaggerated beauty filter
or background music. This is a disclosed synthetic character.
```

### B. Emotional two-person dialogue

```text
Reference-locked fictional adults Maya and Daniel face each other across a
small kitchen table. Maya quietly says [short exact line, if the selected model
supports dialogue control]. Daniel looks down before answering. One continuous
medium two-shot, warm kitchen practical light, natural room tone. No third
character, no subtitles. Keep their existing faces and costumes.
```

### C. Documentary reconstruction

```text
Clearly fictional historical-style reconstruction of a 19th-century market,
not authentic archive footage. Wide establishing shot with period-appropriate
architecture and clothing selected from research references. Camera gently
moves forward; no identifiable real historical individuals speak. No modern
signage. Label as AI reconstruction in the final edit.
```

### D. Cartoon reaction

```text
Original flat-color 2D cartoon fox in the approved kitchen background.
The fox notices an empty cookie jar and slowly lifts one eyebrow, then turns
to camera. Clean line art, squash-and-stretch only in the eyebrow/body motion,
consistent palette, fixed medium shot. Silent animation; no text.
```

### E. Product hero shot

```text
Use the accurate provided product reference without altering its brand marks,
shape, ports or labels. Controlled rotating-camera commercial shot on a clean
neutral studio surface with soft rim light and believable reflections.
Do not invent new buttons, features or dimensions. No claims or captions.
```

### F. Quiet environment B-roll

```text
Early-morning city street after rainfall. A bus passes gently in the distance,
subtle reflected light on pavement, pedestrians walking naturally.
Locked-off wide framing, realistic motion, environmental ambience only,
no speaking subjects and no fictional shop signage emphasized.
```

### G. Speaker reaction shot

```text
Close-up of Daniel matching the approved character reference. He listens to
someone just off-camera, breathes in, hesitates and gives a small reluctant
nod. No spoken dialogue; no exaggerated facial movement. Keep background
and lighting consistent with Scene 04.
```

### H. Social vertical food video

```text
9:16 overhead close-up of an original food preparation scene, hands carefully
arranging ingredients on a clean table. A single straightforward action with
realistic food texture and stable object shape. Bright natural window light.
No invented ingredient labels; narration will be added in post-production.
```

### I. Fantasy cinematic scene

```text
A lone original fantasy traveler in weathered teal robes crosses a stone
bridge over a misty valley. The camera tracks slowly from behind as fabric
moves in the breeze. Soft dawn light, believable gravity and grounded
footsteps. One continuous action; no morphing creatures or sudden costume
changes. Ambient wind only.
```

### J. Music-video performance shot

```text
Original adult performer in a minimalist red-lit studio, holding a relaxed
pose and turning toward the camera on a musical accent. Smooth dolly-in,
subtle atmospheric haze, cohesive red/black palette. No generated lyrics,
no lip movements requiring exact sync; final song will be aligned in edit.
```

### K. Social advertisement UGC-style scene

```text
Original clearly fictional AI brand presenter speaking in a normal home
setting about a verified product feature supplied in the product brief.
Natural daylight and clear delivery. No fake personal testimonial, no claims
of having used the product, and no misleading before/after results.
Product close-ups will be authentic source footage inserted during editing.
```

### L. Long-form series dialogue cutaway

```text
Silent insert shot inside the established apartment set: a handwritten note
rests beside a ceramic cup. Camera gently pushes toward the note without
changing the paper, table or cup. The wording on the note is supplied as a
separately composited graphic during edit to avoid generative text errors.
Warm evening light matches Scene E02-S07.
```

## 14.4 Prompts for writers, directors and continuity assistants

**Series architect:**

```text
Build a six-episode outline for a fictional [genre] show aimed at [audience].
Each episode should have one central conflict, three distinct scene changes,
a reversal, character development, and a compelling ending. Return a table:
episode, premise, characters, turning point, required locations, hooks.
Avoid unfilmable visual spectacle given a small AI-video production budget.
```

**Shot-list generator:**

```text
Convert this beat sheet to a practical AI-video shot list. For each shot
provide: ID, duration, camera size/motion, subject, visible action,
character reference IDs, spoken line or silent, ambience, risk level,
recommended generation mode (T2V/I2V/audio-driven), and continuity notes.
Prefer short physically simple shots, inserts, and reaction coverage.
```

**Continuity reviewer:**

```text
Compare Episode 02 notes to the master series bible. Find contradictions
in appearance, clothing, props, geography, timing, character knowledge,
relationships, voice and location lighting. Return conflicts ranked by
severity, the evidence, and a minimal fix. Do not invent missing facts.
```

**Dialogue humanizer:**

```text
Revise these fictional dialogue lines to sound like two particular
characters in an everyday conversation. Keep their original intentions
and facts unchanged. Cut speeches, use specific reactions and genuine
follow-up questions, vary turn length and allow a few purposeful pauses.
Avoid random filler words, caricatured accents and unsupported claims.
```

**Factual explainer reviewer:**

```text
Review this proposed narration against the supplied source packet only.
Identify factual assertions not supported by the packet, ambiguous numbers,
misleading visuals, invented quotes and missing qualifications. Suggest
corrected phrasing; do not fabricate supporting citations.
```

## 14.5 A prompt iteration protocol

After a bad clip, don't randomly add more adjectives. Diagnose one variable at a time:

1. Is identity wrong? Improve/simplify the reference, reduce complex motion, or switch to a character system.
2. Is action wrong? Shorten the prompt; make the action singular and visible.
3. Is audio wrong? Move dialogue to audio-first workflow.
4. Is camera wrong? Ask for fixed camera; add motion only after framing works.
5. Is timing wrong? Generate shorter shot, trim in editor, or split into two cuts.
6. Is physics wrong? Use live-action reference/performance transfer or redesign the shot with an insert and reaction.
7. Is text wrong? Add exact titles/captions in the editor rather than asking the scene generator to synthesize tiny readable text.

Save both successful prompts and the failure notes. It is the fastest route to a repeatable personal workflow.

---

# 15. FIXING COMMON AI VIDEO FAILURES

| Symptom | Likely reason | First fix | If still broken |
|---|---|---|---|
| Face changes between scenes | Identity not anchored, conflicting prompts | Use same approved reference + exact character asset | Create a different angle from source image or character system |
| Lips do not match voice | Audio/video generated independently or long line | Audio-first lip-sync and shorter segments | Edit with cutaways and reaction shots |
| Hands deform | Complex motion or poor occlusion handling | Reduce gestures; use closer controlled shot | Reshoot with real performance or cut to face/object |
| Object disappears | Unstable temporal/object memory | Simplify interaction and camera movement | Create separate insert for object |
| Voice sounds robotic | Flat TTS delivery / inappropriate model | Add acting direction, change voice model | Human perform + permitted speech-to-speech |
| Two hosts sound alike | Same voice settings/weak casting | Choose genuinely different voices and pacing | Direct each voice with unique language habits |
| Dialogue repeats | Poor context and lack of stop condition | Short turn caps + summary of prior turns | Add moderator and repetition detection |
| Live agent speaks over user | Incorrect VAD/turn-taking | Tune interruption handling and end-of-turn logic | Use push-to-talk for a reliable recording |
| Character moves unnaturally | Too many actions in one generation | One action, static camera | Use performance or pose guidance |
| Sudden random camera moves | Prompt ambiguous/cut-like instructions | Specify one continuous shot | Use keyframes or edit camera motion externally |
| Style inconsistent | Different references/models | Lock palette, style bible, lighting and reference | Use same model/settings where possible |
| Generated text misspelled | Weak text fidelity under motion | Add graphics in editing | Use an accurate composited title/prop |
| Real footage doesn't match | Lighting/color and audio differ | Color grade and consistent room tone | Regenerate weak shots with stronger references |
| Subtitles wrong | ASR not accurate | Manually proofread names and terms | Provide corrected transcription to editor |
| Video has a watermark | Plan/source restriction | Use an authorized output route and check terms | Upgrade only if economics justify it; don't strip rights/attribution controls illicitly |
| “Commercial use” unclear | Different plan/model licenses | Read plan and specific partner model terms | Contact vendor or choose clearer licensed route |
| Credits disappear quickly | Long/repeated high-tier attempts | Draft in cheap mode, approve stills first | Track cost per *approved* second |
| Scene ends mid-sentence | Clip too short | Shorten wording or lengthen shot if supported | Separate into another shot and edit sound over cut |

### Debugging checklist when a clip fails

```text
[ ] Is the prompt asking for too many simultaneous events?
[ ] Is one reference image contradictory or blurry?
[ ] Did I specify exact words when the model cannot guarantee them?
[ ] Did I use the right generation mode for the task?
[ ] Can I tell the same story with two simpler shots?
[ ] Can I solve this with editing, sound or compositing instead?
[ ] Has the model or platform changed since the tutorial I followed?
[ ] Did I record this failed generation's cost and cause?
```

---

# 16. QUALITY CONTROL, TESTING AND PRODUCTION STANDARDS

## 16.1 A scoring rubric for every approved shot

Score each 0–5; don't force a clip into the final edit because generation was expensive.

| Dimension | 0–1: reject | 2–3: repairable | 4–5: good |
|---|---|---|---|
| Identity | Wrong person | Minor drift | Consistent references |
| Motion | Visible morphing | Occasional awkwardness | Believable action |
| Facial expression | Uncanny/wrong | Slightly mismatched | Motivated performance |
| Speech/lip sync | Wrong speaker/major offset | Minor timing error | Clear synchronization |
| Environment | Broken/unstable | Small continuity issue | Spatially coherent |
| Prompt adherence | Wrong event | Partial result | Main action correct |
| Edit suitability | Unusable cut | Can cover with cutaways | Strong start/end handles |
| Sound | Missing/wrong | Reparable mix | Consistent and intelligible |

**Suggested gate:** Reject anything with a major identity, safety, physical or narration error irrespective of total score. Otherwise, aim for 80% of possible score or document a specific repair plan. That threshold is a recommended workflow rule, not an industry standard.

## 16.2 Review at four levels

- **Frame level:** hands, teeth, background objects, text, reflections, face geometry.
- **Shot level:** action makes sense; no jarring morph; timing suitable for editing.
- **Scene level:** continuity between angles, voice identity, room tone, emotional logic.
- **Episode level:** story, rights/disclosure, factual accuracy, pacing and viewer clarity.

## 16.3 A comparative model test plan

Prepare six fixed prompts covering T2V, I2V, dialogue, action, product precision, and camera movement. Generate three takes per model under a fixed test budget. Have a reviewer score outputs blind if possible. Record each model/version, date, format, quality setting, wait time and cost. The winner is the system that produces the most **usable footage per dollar and hour** for your chosen content—not simply the most eye-catching one.

## 16.4 Accessibility

Create legible captions, consider audio description when relevant, check readability on mobile, avoid rapid flashing effects, keep speech intelligible, and don't rely solely on color to communicate important content. If you publish in more than one language, revise captions independently rather than auto-translating without review.

---
# 17. CREDITS, COSTS, HARDWARE AND COST MODELING

## 17.1 Different vendors charge differently

You may encounter **monthly plans**, **generation credits**, **credits per second**, **credits per render**, **premium avatar minutes**, **voice characters**, **API tokens/minutes**, **GPU seconds**, **separate storage**, **resolution surcharges**, **commercial add-ons**, and **enterprise agreements**. Never compare “$20/month” to “$30/month” without knowing how much usable footage each plan yields.

### Verified reference points at publication

| Service | Published reference point | Why you still need to check in-app |
|---|---|---|
| Runway | Standard shows 625 monthly credits, and annual billing at **$12/month equivalent** | The model's per-second credit cost determines output; 625 credits is shown as about 52 seconds of Gen-4.5 generation | 
| Google Flow | A free entry experience and **50 daily credits** in eligible cases | Eligibility, actual models, credit rules, country and subscription tier vary |
| HeyGen | Creator plan examples show **$29/month** in its 2026 credit-based plan explanations | Different avatar engines, translations, resolution and API usage consume credits differently |
| ElevenLabs | Starter has a **$6/month standard reference**; promotions may temporarily change first payment | Character/credit allowances and use rights differ among plans |
| Kling AI | Credit-driven pricing with promotions and model-dependent costs | 4.0, quality, audio and resolution change pricing; check current tool quote |
| Tavus / LiveAvatar | Live conversations are generally usage/session-sensitive | Streaming minute limits, session minimums and custom avatars matter much more than a generic monthly price |

Official references: [Runway pricing](https://runway.com/pricing) · [Flow pricing](https://labs.google/fx/tools/flow) · [HeyGen credit guide](https://help.heygen.com/en/articles/15126059-how-to-use-credits-on-heygen) · [ElevenLabs pricing](https://elevenlabs.io/pricing) · [Tavus pricing](https://www.tavus.io/pricing). Prices and offers in this table are *not* guaranteed quotes, and taxes, currency conversion or plan changes may apply.

## 17.2 The most important cost formula

**The cost of the final video is not the cost of one generation.**

```text
Final usable seconds = finished duration × share that is AI-generated footage
Generated seconds required = usable seconds × average attempts per accepted second
Model generation cost = generated seconds × effective cost per generated second
Total = model generations + voice + avatars + music + editing + assets
        + storage + licenses + taxes + human review
```

Example (*illustrative rates, NOT an actual vendor quote*):

- Desired **3-minute** AI-heavy pilot = 180 usable video seconds.
- Average **2.5 generation attempts** per accepted second.
- Effective model rate assumed **$0.15 per generated second**.
- Generated seconds needed ≈ `180 × 2.5 = 450 seconds`.
- Illustrative video generation ≈ `450 × $0.15 = $67.50`.
- Add voice, thumbnails, any paid editor, music licensing and human review.

If the prompt only makes usable footage half the time, raising the model's output resolution can make costs worse before it improves the final video. **Create cheap previews or still references first.**

## 17.3 Budgeting tiers: illustrative, not promises

| Type of creator | Rough planning envelope per month | Reasonable production goal |
|---|---:|---|
| Learning with free tools | $0–$25 | 3–5 proof-of-concept clips, one short finished edit |
| Small social creator | $25–$100 | Short videos, limited paid voice and/or video credits |
| Regular avatar/presenter creator | $40–$150 | Repeatable talking videos and localization trials |
| Cinematic short-film creator | $100–$350+ | A more ambitious pilot with many retakes |
| Studio/multi-series team | Hundreds to thousands+ | Multiple episodes, editors, assets, storage and QA |

Actual costs can fall outside these ranges. They are illustrative budgets for planning, not verified vendor package totals.

## 17.4 Building your own cost sheet

| Column | Example | Meaning |
|---|---|---|
| `shot_id` | E01-S03 | Traceable generation |
| `tool/model` | Runway Gen-4.5 | Record specific model version |
| `target_duration_s` | 7 | Usable finished duration |
| `generation_duration_s` | 8 | Rendered seconds |
| `attempts` | 3 | How many tries |
| `credits_each` | 96 | Illustrative, verify live |
| `credits_total` | 288 | Credit use |
| `approved_s` | 6 | Actually usable footage |
| `issues` | weak hands / lip drift | Reasons for retry |
| `status` | approved | Helps producer avoid double-spending |

You can measure **cost per approved second**, **percentage of generations approved**, **average shots per episode**, and **audio repair rate**. Those are more useful than chasing a discount banner.

## 17.5 Local generation hardware

**Cloud apps** spare you most GPU setup. **Open-weight/local models** can provide workflow control but require compatible GPU memory, drivers, dependencies, storage, model licenses and time. Hardware needs vary substantially by checkpoint, resolution, frames, precision, quantization, offloading and optimization. A provider may advertise a low-VRAM route that is much slower than the full-quality standard route.

Before buying hardware:

1. Verify the specific checkpoint's requirements from the author.
2. Separate disk space from GPU VRAM and system RAM.
3. Check whether Windows/Linux/macOS support is documented for your selected workflow.
4. Try a small, hosted test first if possible.
5. Calculate electricity, cloud GPU rental, maintenance and training time.
6. Validate the model/license actually permits your intended commercial output.

---

# 18. LEGAL RIGHTS, CONSENT, SAFETY AND PLATFORM MONETIZATION

This section is educational and is **not legal advice**. Rights depend on your jurisdiction, sources, platform and provider terms. When publishing commercial work, consult appropriate professional advice for important disputes or rights questions.

## 18.1 A simple rights matrix

| Asset | What must be cleared | Evidence to save |
|---|---|---|
| Character portrait | Original or licensed image; no unauthorized personal likeness | Prompt/project info, image license, consent if applicable |
| Voice/voice clone | Voice license and provider's verification rules | Permission, voice selection, plan/terms snapshot |
| Music | Composition/master and generated music plan terms | Licenses, receipts, track generation records |
| Stock footage | Proper license for platform, ads, edits | Stock-site license/asset ID |
| Logos/brand material | Trademark use and factual accuracy | Brand authorization or applicable basis |
| Real human recording | Image/voice/performer's informed permission | Written release, intended uses, date |
| Source document | Right to quote, adapt or redistribute if applicable | URLs, source/license and quotation record |
| AI output | Model service terms plus rights in inputs | Model/version, subscription, prompt and output |

## 18.2 AI video and copyright

In the United States, the Copyright Office's 2025 report explains that using AI to **assist** a human-authored work does not automatically eliminate copyrightability. But an output created without sufficient human authorship may not receive protection for its purely AI-generated elements. This is a nuanced issue; do not assume you automatically own exclusive copyright over everything the model produces. [U.S. Copyright Office AI study](https://www.copyright.gov/ai/) · [Part 2 summary](https://www.copyright.gov/newsnet/2025/1060.html)

Practical steps: save your human script, shot decisions, edits, original artwork, acting, sound design, compositing, logs and source licenses. Document meaningful creative contributions rather than relying solely on the final prompt.

## 18.3 Likeness and voice consent

Never train or generate a realistic digital double of a real person without valid permission or another clearly lawful basis. A public social-media recording is not automatically a voice-cloning license. Special caution applies to children, vulnerable people, private individuals, deceased individuals and public figures. Provider terms may be stricter than the law.

**A safer creative default:** Invent original adult fictional characters and original voices. If using a real consenting performer, document scope, compensation, medium, territory, term, training rights, revocation/data-retention procedure and future reuse.

## 18.4 Honest representation and synthetic-media disclosure

Your audience should not be misled into believing fictional scenes are genuine documentary evidence, customer testimonials, emergencies or real-world footage when that distinction matters.

- **YouTube:** Creators must disclose realistic AI-generated or meaningfully altered content in covered cases using its AI disclosure workflow; the relevant implementation/policy can change. [YouTube disclosure help](https://support.google.com/youtube/answer/14328491)
- **YouTube monetization:** Original and authentic creative work matters. Repetitive, mass-produced or inauthentic material may be ineligible, even if it uses AI. AI assistance itself does not automatically bar monetization. [YouTube monetization policies](https://support.google.com/youtube/answer/1311392)
- **TikTok:** Its help center requires labeling of AI-generated material involving realistic images, video or audio in covered circumstances. [TikTok AI-generated content help](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)
- **Other platforms:** Check current Meta, advertising network and country-specific rules rather than assuming YouTube policies apply everywhere.

**Sample disclosure text for fictional series:**

> This is an original fictional story featuring AI-generated characters and scenes. Voices and visuals are synthesized and edited by the production team. No real event is depicted.

**Sample disclosure for documentary reconstructions:**

> Illustrative AI reconstruction. Not original archival footage. Narration is based on the cited sources.

## 18.5 Privacy, security and data handling

Before uploading a person's face, voice, company materials, home address, client document or unreleased product design, examine the provider's data handling and training policies. Store consent securely; limit access to raw identity footage; use approved cloud storage and avoid copying account/API secrets into prompts or shared video projects.

For live avatar sessions, notify participants if recording and make sure audio/video handling complies with applicable recording-consent laws and organizational requirements. Keep agent logs out of public distribution until reviewed.

## 18.6 Risk checklist before publishing

```text
[ ] I have the right to use the face/voice/identity represented.
[ ] My music and stock assets are licensed for this distribution.
[ ] I did not fabricate authentic testimony, medical evidence or customer results.
[ ] Claims about real people and products have been checked.
[ ] AI-generated realistic content is disclosed where required.
[ ] Platform monetization and ad policies have been reviewed.
[ ] I read model-specific commercial terms, not just the platform homepage.
[ ] The uploaded final video has no accidental private information.
[ ] I saved the asset/license record and the human creative project files.
```

---

# 19. PUBLISHING, GROWTH AND MAKING MONEY

## 19.1 Choose a sustainable format

An original series with memorable characters can build repeat viewers. A faceless explainer can create educational value. A presenter can teach. An AI ad workflow can support client projects. The common thread is **audience usefulness or entertainment**—not simply posting high volumes of generic generated clips.

### Possible revenue routes

- Advertising revenue where a platform and your content are eligible.
- Sponsorships and branded content with accurate disclosure and claims.
- Commissioned ads, training videos, translated videos and social edits for clients.
- Licensing original characters, artwork or format rights where legally protectable.
- Subscription/community-supported original series or educational projects.
- Service packages: research, script, synthetic presenter, localizations, subtitling and post-production.

Do not assume any of these guarantees a particular income. Rates, eligibility, rights and audience demand change.

## 19.2 Create a strong episode package

For each release, prepare: final video, verified title, eye-catching *accurate* thumbnail, 1–3-sentence description, required synthetic-media label, captions/subtitles, content warnings if relevant, related episode link, and a simple question that invites genuine viewer reaction.

Avoid an unbroken assembly line of nearly identical content. Your channel benefits from original narration, research, creative development, good pacing, and well-chosen stories.

## 19.3 Measure what matters

| Measure | What it tells you | Response to weak result |
|---|---|---|
| First 2–5 seconds retention | Is the opening compelling? | Stronger hook or clearer first shot |
| Average watch time | Does the pacing hold attention? | Tighten repetitive sections |
| Completion rate | Does the story deliver? | Shorten, improve ending or clarity |
| Returning viewers | Do people care about recurring characters? | Deepen relationships and episodic hooks |
| Saves/shares | Is content valuable or funny? | Focus on useful insight or memorable scene |
| Production cost per view/episode | Is your process financially sustainable? | Reduce retakes, simplify scene design |
| Viewer comments | Are accents, dialogue, and facts credible? | Improve review and local authenticity |

## 19.4 Your first publishing plan

Release **three** distinct 30–60 second pilots in one week rather than signing up for ten tools. Test (A) talking presenter, (B) fictional dialogue, (C) visually led short. Compare production time, cost per usable second, enjoyment of making them and viewer response. Choose one format to develop into a four-part series.

---

# 20. ADVANCED CREATOR AUTOMATION AND LOCAL AI

## 20.1 When to use ComfyUI

[ComfyUI](https://github.com/Comfy-Org/ComfyUI) is a node-based system for reproducible generative workflows. You can chain reference-image preparation, sampling, model loading, depth/pose control, video generation, enhancement and export. Its workflows can be saved and reused. [ComfyUI workflow gallery](https://comfy.org/hub/workflows/)

**Conceptual node graph:**

```text
Approved character image     Prompt + negative constraints
              └─────────────┬──────────────┘
                      Input conditioning
                             ↓
                 Model/checkpoint + settings
                             ↓
                  Video generation/sampling
                             ↓
                    Decode video frames
                             ↓
               Frame inspection + enhancement
                             ↓
                    Audio join / video mux
                             ↓
                      MP4 / archive
```

This is a **conceptual diagram**, not a promise that specific node names exist in every ComfyUI release. The workflow may need plugins/models compatible with your GPU and licensing.

## 20.2 When to use APIs

A developer can automate render queues, trigger new shots, log credits, save outputs to storage, run quality checks and notify a human editor. Hosted model API services include vendor APIs, fal.ai, Replicate and other model gateways. API support changes faster than product marketing; use official API schemas rather than copying untested code.

**Automatable stages:**

1. Read a reviewed shot-list CSV.
2. Validate text and reference assets.
3. Submit a generation only when rights/credits are authorized.
4. Poll or receive completion results.
5. Store clip, metadata, prompt, timing and cost.
6. Produce contact sheets and QC checklist for a human reviewer.
7. Move approved footage into an editing project.
8. Preserve version history and retry only rejected shots.

**Do not fully automate:** permission decisions, sensitive claims, fact-checking, disclosures and final approval of realistic people or real-world representations.

## 20.3 Optional local voice and lip sync

Local speech recognition, TTS and audio-driven animation tools may reduce vendor reliance, but differ widely in quality and licensing. Wav2Lip is historically influential as an audio-to-lip-sync research implementation; the public repository includes noncommercial restrictions, so **do not assume a business can use it freely**. [Wav2Lip repository](https://github.com/Rudrabha/Wav2Lip)

Before deploying any voice model, verify local language quality, real-time speed, terms, security and human review requirements.

## 20.4 Team roles for a serious AI production

Even an AI-heavy production can benefit from a **showrunner/writer**, **AI art director**, **character/reference lead**, **voice and sound editor**, **shot generation operator**, **video editor**, **continuity supervisor**, **quality reviewer**, and **rights/fact checker**. A solo creator may perform all these roles, but treating them as separate checklists prevents mistakes.

## 20.5 An advanced production system design

```text
PROJECT DATABASE (characters, sets, episodes, licenses)
                       │
        ┌──────────────┴───────────────┐
        │                              │
 STORY/SHOT PLANNER              REFERENCE LIBRARY
        │                              │
        └──────────────┬───────────────┘
                       ↓
              GENERATION QUEUE
           ┌───────────┼───────────┐
           │           │           │
      Video model  Voice model   Image model
           │           │           │
           └───────────┴───────────┘
                       ↓
             REVIEW / APPROVAL GATE
                       ↓
              TIMELINE / MIX / GRADE
                       ↓
             RIGHTS + FACT + QC GATE
                       ↓
            PLATFORM-SPECIFIC EXPORTS
```

Model outputs are **draft production assets** until reviewed. Automation should preserve traceability, not erase it.

---

# 21. A 30-DAY LEARNING PLAN

| Days | What to learn | Deliverable |
|---|---|---|
| 1–2 | Video modes; inspect Flow, Runway, Kling menus | Compare T2V and I2V for a single prompt |
| 3–4 | Images, references and framing | Make one consistent original character sheet |
| 5–6 | Camera terms and one-action prompting | Three coherent 5–8 second shots |
| 7 | Basic editing | First 20-second silent sequence |
| 8–9 | Voice casting and expressive TTS | Two contrasting approved voices |
| 10–11 | Lip-sync and talking avatars | 15–30 second talking portrait |
| 12–13 | Dialogue timing and reaction shots | 30-second two-person conversation |
| 14 | Sound mixing and captions | Complete 45-second fictional scene |
| 15–16 | Source-driven audio overview or improv transcript | 1–2 minute conversational audio segment |
| 17–18 | Live agent basics | Test a live AI character and interruption handling |
| 19 | Unscripted recording | A short recorded AI interview or moderated AI-to-AI test |
| 20–21 | Continuity and character bible | Season/cast/location reference packet |
| 22–23 | Storyboard and episodic structure | Six-episode season outline + pilot beat sheet |
| 24–26 | Shot generation and audio-first edit | A 2–3 minute pilot episode |
| 27 | Rights, commercial terms and platform policies | Project rights/disclosure checklist |
| 28 | Quality assurance | Frame, shot, scene and episode QA report |
| 29 | Format/thumbnail/captions | A complete publish-ready episode package |
| 30 | Review costs and outcomes | Choose one sustainable production workflow |

**Minimum equipment:** a usable computer or smartphone, stable internet for cloud services, headphones, an audio recorder or microphone if you use live/own-voice methods, and enough storage. A modern GPU is **not mandatory** for most cloud-first workflows.

**Learning rule:** Finish and review small projects. Watching model demos for a month is not equivalent to making a single complete video.

---
# 22. COPY-READY TEMPLATES AND WORKSHEETS

The following templates can be pasted into a Markdown document, a spreadsheet or a project-management app. They are independent of the AI tool you choose.

## 22.1 One-page production brief

```markdown
# VIDEO PRODUCTION BRIEF
**Project / episode:**
**Owner / producer:**
**Date / version:**
**Platform / target audience:**
**Runtime:**
**Aspect ratio / delivery resolution:**
**Genre / tone / visual style:**
**Logline (one sentence):**
**Viewer promise (why watch?):**
**Beginning / middle / end:**
**Main characters:**
**Character reference IDs:**
**Locations / prop references:**
**Dialogue method:** (native / generated transcript / recorded / live)
**Voice method:** (TTS / actor / speech-to-speech / real-time)
**Video model(s) to test:**
**Editing tool:**
**Music, licenses and source material:**
**Factual-review needs:**
**Realism / disclosure label:**
**Budget and maximum retries:**
**Definition of done:**
```

## 22.2 Character bible worksheet

```markdown
# CHARACTER [ID]
**Fictional or real person?**
**If real, what valid permissions/restrictions apply?**
**Name, age in story, pronouns:**
**Story role and goals:**
**Appearance:**
**Hair / complexion / face geometry / height:**
**Default costume / exceptions:**
**Approved visual references:**
**Voice source and provider voice ID:**
**Accent / pronunciation dictionary:**
**Pacing and emotional range:**
**Mannerisms (2–4):**
**What this person knows now:**
**Relationships:**
**Never-change rules:**
**Episode-specific changes:**
**Last reviewed:**
```

## 22.3 Shot list CSV template

```csv
shot_id,episode,scene,target_s,aspect,camera,subject_id,location_id,visible_action,audio_mode,dialogue_line,reference_file,model,model_version,estimated_credits,actual_credits,attempts,approved_s,issue,status
E01-S01,E01,1,6,16:9,wide,NONE,CAFE-01,"Rainy café establishing shot",ambience,"",cafe_front.png,TBD,TBD,0,0,0,0,"",planned
E01-S02,E01,1,7,16:9,close-up,MAYA-01,CAFE-01,"Maya reads phone then looks up",voice_first,"You knew, didn't you?",maya_front.png,TBD,TBD,0,0,0,0,"",planned
```

## 22.4 Prompt and experiment log

```markdown
| Date | Clip ID | Model + version | Mode | References | Prompt revision | Seconds | Credits | Result | Lesson |
|---|---|---|---|---|---|---:|---:|---|---|
| 2026-11-23 | E01-S02-A | Video model/version | I2V | MAYA-01 | r1 | 8 | [fill] | eye drift | hold camera static |
| 2026-11-23 | E01-S02-B | Video model/version | I2V | MAYA-01 | r2 | 8 | [fill] | accepted | prompt reduced to one action |
```

## 22.5 Simple episode continuity log

```markdown
# CONTINUITY / EPISODE 02
- [ ] Maya wears the same outfit in consecutive scenes.
- [ ] Daniel's voice settings match previous episodes.
- [ ] Café doorway, window and table remain on the same sides.
- [ ] The note's text matches the actual story.
- [ ] Characters do not know secrets that have not been revealed.
- [ ] Injuries, phones and props persist logically.
- [ ] Camera direction is understandable between dialogue cuts.
- [ ] The synthetic-content disclosure is accurate.
```

## 22.6 A fictional unscripted-show format sheet

```markdown
# SHOW: TWO MINDS, ONE QUESTION
**Host A:** Maya — skeptical, witty; challenges weak assumptions.
**Host B:** Daniel — thoughtful, asks for supporting evidence.
**Topic source packet:** [approved URLs or source text]
**Maximum turns:** 18
**Typical turn length:** 10–45 words
**Opening:** Host A poses one clear question.
**Middle:** Each host asks at least two genuine follow-ups.
**Required moment:** One disagreement resolved through clarification.
**Facts policy:** Never invent survey results, quotes or citations.
**Interruption handling:** Stop when the other speaker begins.
**Ending condition:** 18 turns, 4 minutes, or producer stop.
**Voice IDs:** [approved voices only]
**Avatar asset IDs:** [original/authorized identities]
**Output:** transcript + isolated audio tracks + approved video segments.
**Human review:** required before upload.
```

## 22.7 Permission and release checklist (not a legal contract)

```markdown
**Contributor / identity:**
**Project:**
**What will be captured:** image / voice / performance / other
**What AI processing is planned:**
**Which service providers will receive files:**
**Purpose and platforms:**
**Commercial use intended?**
**Territory, duration, future model training and reuse scope:**
**Storage/access and withdrawal procedure:**
**Compensation and credit:**
**Date / permission record:**
**Special restrictions:**
```

A real release should be drafted and reviewed to fit local law, especially for paid talent and commercial uses.

## 22.8 An example subtitles file (SRT)

```srt
1
00:00:00,500 --> 00:00:03,000
MAYA: You knew, didn't you?

2
00:00:03,500 --> 00:00:06,600
DANIEL: I wanted to tell you.

3
00:00:07,000 --> 00:00:08,700
MAYA: Then why didn't you?
```

These are illustrative timestamps. Recalculate subtitle timings using the final audio, not a generated transcript's estimated duration.

## 22.9 Platform-specific getting-started walkthroughs

The exact interface may change; this section names stable actions and points to official instructions instead of pretending every user sees the same buttons.

### Google Flow — create a first cinematic clip

1. Open [Flow](https://labs.google/fx/tools/flow), sign in and check eligibility, model menu and remaining credits.
2. Choose the appropriate text/image video workflow; use the [Flow model capability page](https://support.google.com/flow/answer/16352836) to see what the selected model supports.
3. If your chosen mode accepts references, upload a clean character or scene image.
4. Enter a concise prompt with one action, framing, lighting and optional sound.
5. Choose landscape/portrait, duration and quality from the available menu.
6. Inspect the generation charge, render and watch the result with sound.
7. Save the approved clip and its exact prompt; iterate one change at a time.

**Sample first test:** “A locked-off medium shot of an original adult café worker wiping a counter, looking up, then smiling subtly. Warm window daylight, realistic natural motion, only soft café ambience, six seconds.”

### Runway — compare a text prompt to an image-guided shot

1. Open [Runway](https://runway.com/) and view the video model selector.
2. Use a supported T2V model for a scene with no established identity.
3. Try a corresponding I2V attempt with your approved still and a **motion-focused** prompt.
4. Keep camera language simple: “Fixed medium shot. Subject turns head slightly and places cup down.”
5. Generate multiple drafts within a predefined credit limit.
6. Compare identity preservation, motion and start/end editing handles.
7. Use the output in an external editor for longer sequences.

Follow [Runway's current guide](https://help.runwayml.com/hc/en-us/articles/37425232841875-Getting-Started-with-Generative-Video) and [prompting guide](https://academy.runwayml.com/guides/prompting-guide).

### Kling — create one character-driven short

1. Open [Kling](https://kling.ai/), inspect offered models and account credits.
2. Choose T2V for a new scene or I2V/reference modes where supported.
3. Use a short prompt focused on action and camera rather than a long screenplay.
4. If you need spoken audio, verify that the *selected Kling variant* supports your intended audio behavior.
5. Generate, inspect faces/hands/lips, and save approved takes.
6. Compare at least one 4.0 generation with an available faster/lower-cost mode before deciding on your production standard.

See the [official Kling 4.0 product announcement](https://kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling?tab=all).

### HeyGen — create a speaking presenter

1. Open [HeyGen](https://www.heygen.com/) and select a permitted avatar or create an authorized personal avatar.
2. Choose the speaking-video/avatar engine available under your tier.
3. Enter a short text message or provide compatible audio.
4. Assign a voice and check pronunciation before rendering the full video.
5. Set composition, background and format.
6. Preview credit usage, render, and review lips/expressions.
7. Export and polish with accurate captions and supporting shots.

For photo-driven characters use [Avatar IV help](https://help.heygen.com/en/articles/11269603-heygen-avatar-iv-complete-guide); for a genuinely live responding avatar, use [LiveAvatar](https://help.heygen.com/en/articles/12758516-introducing-liveavatar), not an ordinary prerecorded avatar template.

### ElevenLabs — build consistent dialogue audio

1. Open [ElevenLabs](https://elevenlabs.io/) and review available voice models and credits.
2. Choose a licensed/platform voice, or create only a voice identity you have rights to use.
3. Test normal dialogue, emphasis, questions and names.
4. Use a suitable model such as a current expressive speech engine for edited dialogue or a low-latency model for live interactions.
5. Render one short line per character turn; keep speaker recordings separate.
6. Fix unnatural intonation, punctuation, pace or pronunciation.
7. Export aligned dialogue tracks and use a compatible character animation tool.

See the [official model matrix](https://elevenlabs.io/docs/overview/models) and [voice cloning rules](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning).

### LTX Studio — prepare a recurring series

1. Open [LTX Studio](https://ltx.studio/) and create a project.
2. Define the main story, characters and locations.
3. Build saved Elements for recurring cast/sets where supported.
4. Create the storyboard or planned shot sequence.
5. Assign references to shots and choose compatible generation settings.
6. Render clips, revise problem shots selectively and assemble a timeline.
7. Export draft scenes for proper final editing and continuity review.

See the [official production tutorial](https://ltx.io/blog/ltx-studio-tutorial) and [Elements guide](https://ltx.io/blog/how-to-create-a-consistent-character).

### Descript / CapCut — finish the clip

Import your video/audio; align dialogue; cut poor frames and repeated sentences; add reaction shots and B-roll; correct captions; balance voice/music/ambience; export a platform-appropriate MP4. Descript is particularly useful for transcript-based spoken editing, while CapCut offers a familiar timeline for quick social clips. [Descript](https://www.descript.com/video-editing) · [CapCut](https://www.capcut.com/)

---

# 23. GLOSSARY

| Term | Definition |
|---|---|
| Agent | Software that uses a model plus context/rules/tools to pursue a task or converse |
| ASR / STT | Automatic speech recognition / speech to text |
| Audio-first | Locking/perfecting sound before producing final animated visuals |
| Avatar | Digital representation of a person or character |
| B-roll | Supporting footage overlaid between/over main action or narration |
| Character bible | Approved visual, vocal and story record for a recurring character |
| Checkpoint | Stored model weights for inference or training |
| Clip | One piece of generated/recorded footage |
| Conditioning | Information that constrains or guides generation |
| Continuity | Story and visual consistency across shots and episodes |
| CVI | Conversational Video Interface (a Tavus product concept) |
| Diarization | Identifying speakers in recorded speech |
| Diffusion | Generative process often based on progressively denoising learned representations |
| DiT | Diffusion Transformer |
| Digital twin | Authorized digital likeness modeled after a person |
| Dubbing | Translating/replacing spoken content, often preserving timing |
| EDL | Edit decision list; cut/timing information |
| Embedding | Numeric representation used by machine-learning models |
| Establishing shot | Shot that communicates the location or scene geography |
| Foley | Created or selected physical action sound effects |
| FPS | Frames per second |
| Frame interpolation | Producing intermediate frames to change motion timing/smoothness |
| Generative video | AI-created moving imagery from text, images or other conditioning |
| I2V | Image-to-video |
| Inpainting | Re-generating only a specified area |
| J-cut / L-cut | Audio transitions crossing a picture edit |
| Keyframe | A defined frame used to guide animation or editing |
| Latency | Delay between input and output, important for real-time agents |
| Latent | Learned compressed representation from which output can be decoded |
| Lipsync | Mapping speech to visible mouth/facial movement |
| LLM | Large language model |
| LoRA | Low-rank adaptation used for lightweight model adaptation |
| Model | Trained AI system; separate from the product/interface hosting it |
| Multimodal | Works with multiple input/output kinds: text, images, audio, video |
| Native audio | Sound generated within an audiovisual model, rather than added separately |
| NLE | Non-linear editing software, e.g., Resolve/Premiere |
| Open weights | Model weights released for use under stated conditions; not inherently unrestricted |
| Outpainting | Generate beyond existing image/video boundaries |
| Performance transfer | Apply movement/expressions from recorded motion to another subject |
| Persona | Assigned identity and behavioral instructions for an agent |
| Prompt | Input instructions or description guiding generation |
| Prompt adherence | How accurately a model follows directions |
| Reference image | Approved visual input used for appearance/style guidance |
| Render | Generate/export video, audio or graphics |
| S2V | Speech/audio-to-video |
| SFX | Sound effects |
| Shot | One continuous camera view in a story |
| Shot/reverse-shot | Alternating angles of a conversation |
| Sound stem | Separate audio element/track, e.g., dialogue, music or effects |
| Speech-to-speech | Transform performance audio into another authorized voice/style |
| Storyboard | Planned sequence of images representing shots |
| T2V | Text-to-video |
| Temporal consistency | Visual and motion stability over time |
| TTS | Text-to-speech |
| Turn-taking | Logic deciding when each conversational speaker starts/stops |
| V2V | Video-to-video modification |
| VAD | Voice activity detection |
| VAE | Variational autoencoder; common compression component in generation models |
| Video extension | Generate additional duration after an existing clip |
| Voice clone | Model output reproducing vocal characteristics of an authorized person |
| WebRTC | Technology often used for low-latency interactive audio/video |

---

# 24. OFFICIAL SOURCES, MANUALS AND FURTHER LEARNING

This guide favors original company documentation and product announcements over unsourced ranking lists. **Accessed/reviewed for the November 23, 2026 edition.** URLs may change. The links here are learning resources, not endorsements or affiliate offers.

## Video model research and production manuals

1. [Google DeepMind: Veo model and capabilities](https://deepmind.google/models/veo/)
2. [Google DeepMind: Veo prompt guide](https://deepmind.google/models/veo/prompt-guide/)
3. [Google Flow: current models and supported features](https://support.google.com/flow/answer/16352836)
4. [Google Flow: credit charging](https://support.google.com/flow/answer/16526234)
5. [Google Flow: get started](https://support.google.com/flow/answer/16353333)
6. [Runway: Gen-4.5 help](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5)
7. [Runway: generative video basics](https://help.runwayml.com/hc/en-us/articles/37425232841875-Getting-Started-with-Generative-Video)
8. [Runway Academy: prompting guide](https://academy.runwayml.com/guides/prompting-guide)
9. [Runway: model / credit information](https://academy.runwayml.com/models-pricing)
10. [Runway: shot-list planning](https://runway.com/resources/ai-shot-list)
11. [Kling 4.0 official announcement](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-officially-launches-next-generation-kling-40-raising/)
12. [ByteDance: Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
13. [Luma: Ray3.2 announcement](https://lumalabs.ai/news/introducing-ray-3-2)
14. [Pika model 2.5](https://creation.pika.art/apps/pika-2-5)
15. [PixVerse V6](https://pixverse.ai/en/blog/pixverse-launches-v6-advancing-ai-video-generation)
16. [Adobe Firefly: video partner models](https://helpx.adobe.com/firefly/web/create-mood-boards/firefly-boards/partner-models-to-generate-videos.html)
17. [Midjourney video documentation](https://docs.midjourney.com/hc/en-us/articles/37460773864589-Video)
18. [Midjourney image model V8.1 update](https://updates.midjourney.com/v8-1-is-now-the-default-model/)
19. [OpenAI: Sora service discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)

## Series, character consistency, open models and local generation

20. [LTX Studio: official production tutorial](https://ltx.io/blog/ltx-studio-tutorial)
21. [LTX Studio: character Elements consistency](https://ltx.io/blog/how-to-create-a-consistent-character)
22. [LTX: open model overview](https://docs.ltx.io/open-source-model/getting-started/overview/)
23. [Wan2.2: official open model repository](https://github.com/Wan-Video/Wan2.2)
24. [Tencent HunyuanVideo-1.5: official repository](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)
25. [ComfyUI: official repository](https://github.com/Comfy-Org/ComfyUI)
26. [ComfyUI: workflow examples](https://comfy.org/hub/workflows/)
27. [OpenArt: character and reference help](https://openart.ai/help/)
28. [Higgsfield: Soul ID and production modes](https://higgsfield.ai/creator-hub/help-center/getting-started/what-is-higgsfield)

## Voices, talking characters and genuinely live agents

29. [ElevenLabs: speech model catalogue](https://elevenlabs.io/docs/overview/models)
30. [ElevenLabs: Eleven v4 release](https://elevenlabs.io/blog/eleven-v4)
31. [ElevenLabs: voice cloning rules](https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning)
32. [ElevenLabs: dubbing documentation](https://elevenlabs.io/docs/overview/capabilities/dubbing)
33. [HeyGen: Avatar IV complete guide](https://help.heygen.com/en/articles/11269603-heygen-avatar-iv-complete-guide)
34. [HeyGen: Avatar/Video Agent credits](https://help.heygen.com/en/articles/15126059-how-to-use-credits-on-heygen)
35. [HeyGen: LiveAvatar introduction](https://help.heygen.com/en/articles/12758516-introducing-liveavatar)
36. [HeyGen: translation languages](https://help.heygen.com/en/articles/11391941-video-translation-languages-we-support)
37. [Tavus: Conversational Video Interface](https://www.tavus.io/cvi)
38. [D-ID: realtime architecture](https://docs.d-id.com/docs/realtime-overview)
39. [D-ID: live agent quickstart](https://docs.d-id.com/docs/agent-session-quickstart)
40. [Hedra: product updates](https://hedra.me/blogs/feature-announcements-and-updates)
41. [Hume: Octave expressive speech](https://www.hume.ai/octave)
42. [AWS: Cartesia Sonic 3 overview](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart)
43. [Google: notebook audio and video overviews](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/)

## Editing, budgets, ethics and publishing

44. [Descript: transcript-based editing](https://www.descript.com/video-editing)
45. [Runway: published pricing](https://runway.com/pricing)
46. [Google Flow: published product tiers](https://labs.google/fx/tools/flow)
47. [HeyGen: credit-based plans](https://help.heygen.com/en/articles/15125761-heygen-credit-based-pricing-plans-subscriptions-explained)
48. [ElevenLabs: published pricing](https://elevenlabs.io/pricing)
49. [Tavus: published pricing](https://www.tavus.io/pricing)
50. [ElevenLabs: prohibited-use policy](https://elevenlabs.io/use-policy)
51. [YouTube: generative AI disclosure](https://support.google.com/youtube/answer/14328491)
52. [YouTube: monetization and repetitive/inauthentic content](https://support.google.com/youtube/answer/1311392)
53. [TikTok: AI-generated content labeling](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)
54. [U.S. Copyright Office: copyright and AI](https://www.copyright.gov/ai/)
55. [Wav2Lip research repository and license](https://github.com/Rudrabha/Wav2Lip)

---

## FINAL RECOMMENDATION: WHAT TO MASTER FIRST

If you remember only one production formula, make it this:

**Clear story or viewer purpose → original/approved references → natural voice/performance → short controlled video shots → careful editing → quality/rights review → publication.**

For **fictional cinematic video**, start with one strong video generator plus a competent editor. For **a talking human**, begin with an avatar platform. For **real unscripted conversations**, use a conversational AI plus real-time audio/avatar orchestration. For **series**, spend time on character bibles and continuity before spending money on many video renders.

The goal is not to use every model. It is to understand which system owns each part of the production, how to diagnose its weaknesses, and how to assemble outputs into a coherent, genuinely worthwhile video.

*End of the November 23, 2026 masterclass. Update model/version, availability, pricing and policy checks when beginning a new production.*
