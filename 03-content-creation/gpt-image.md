# GPT Image 2.6

**What you will be able to do:** Create believable campaign backgrounds while preserving a real product.

> **Updated:** 20 November 2026. Interface, account access and available models can change.

![GPT Image 2.6](../assets/illustrations/product-lighting.svg)

*Original instructional artwork. Diagram labels are conceptual, not screenshots of a vendor interface.*

## Core guidance from the expanded handbook

*Image generation, precise editing and production concepts*

### Where this tool earns its place

OpenAI describes Sunburst as a detailed image option and Flare as a faster iteration option. The models can generate and edit visuals, with available controls that vary by interface. Choose image generation for fictional illustration or concept work; use real photographs when advertising an actual item.

### Before the first prompt

Start with a creative brief, reference images you own or may use, and a decision about which elements may change. Specify subject, setting, position, camera view, material, light, colour behaviour and empty space. For a product campaign, add “preserve the uploaded product unchanged” only when using an editing workflow that can respect that constraint, then inspect the image anyway.

### A complete business exercise

For a bakery campaign, photograph the real loaf against a plain surface. Generate several background concepts without bread in them, choosing one consistent with the shop’s physical space. Place the real loaf into the scene using a controlled composite; inspect scale, shadow and label. Produce a square hero image and detail crops rather than repeatedly rerendering the object.

### Copy ready prompt for this tool

> Create an editorial photograph background for a local bakery’s real bread product. A lightly worn wooden table beside an east facing window in late morning. Soft daylight falls across a folded linen cloth and two crumbs. Camera at table height, 50 mm photographic feel, warm neutral colour and realistic shadows. Leave an uncluttered area on the right where we will place our approved bread photograph. No text, logos, glowing effects, synthetic packaging or extra bread.

### When the result is weak

If the light feels plastic, describe the single source and what it touches. If it invents a product label, remove all generated lettering and add approved type in a design editor. If scale drifts across a set, lock the real object photograph and change backgrounds instead.

### Human editorial finish

Real surfaces have small imperfections: a crease, a slight scuff, uneven light. Use genuine observations instead of prompting for fake candid stories. Edit out repeating scene tropes such as perfect water droplets and identical heroic reflections.

### Approval boundary and common errors

Inspect full resolution, product truth, provenance, consent and any policy on realistic synthetic images.

**Official reference:** [GPT Image 2.6 Sunburst and Flare product guidance](https://developers.openai.com/api/docs/guides/image-generation)

## First session: from a blank workspace to a reviewable result

1. Decide whether the task needs generation, editing or a photograph of the actual item.
2. Collect one reference image for approved shape, one for mood and any negative space requirement.
3. Choose image quality and aspect ratio according to the available interface; API model names are not guaranteed to appear in the app.
4. Generate a single controlled composition before requesting variants.
5. Inspect product geometry, lighting, text and shadows at full size.
6. Composite the authentic product photo where fidelity matters and add final copy in an editor.

## Prompt ladder: simple, evidence based and advanced

The prompts below are teaching examples. Replace fictional context with approved records. A tool that does not support freeform prompting may require you to perform the equivalent steps through its own interface.

### First pass

```text
Describe three lighting arrangements for a tabletop image of an amber glass bottle. Use a real material reference and suggest where the label could be added later.
```

### Image instruction

```text
Create an editorial tabletop background with cream plaster and a worn oak surface, soft morning light from the left, realistic shadow and empty central space for an approved product photograph. No label, bottle, floating particles or text.
```

### Precise revision

```text
Keep the composition and lighting intact. Reduce the strength of the table reflection, remove the extra vase and increase empty space above the intended product position. Do not modify unrelated areas.
```

## What an acceptable result looks like

The preferred result gives a compositing artist believable light direction and usable empty space. It is not proof that the real product was photographed in that environment.

## If the first version disappoints

If reflective surfaces become impossible, ask for a matte surface. If a product develops extra caps or labels, replace it with the genuine object rather than claiming the render is accurate.

## Human editorial finish

A few credible textures and actual material details provide personality. A slogan does not need simulated lens flare to sound trustworthy.

## Practice assignment

Using a fictional or appropriately protected version of the case, complete **create believable campaign backgrounds while preserving a real product**. Save an evidence inventory, the first draft, a precise correction request and the reviewed deliverable. Write a short comparison showing what the revision genuinely improved.

## Approval and success test

Does the final exported image match the actual product and clearly communicate what is an illustration?

> **Model detail:** OpenAI distinguishes GPT Image 2.6 Sunburst and Flare in the API. A model identifier seen in the API is not guaranteed to be a visible selection in every consumer image interface.

## Related reading

[Prompt anatomy](../01-foundations/prompting-fundamentals.md) · [Context engineering](../01-foundations/context-engineering.md) · [Humanisation](../01-foundations/humanization.md) · [Reference index](../06-reference/sources-and-updates.md)

## Image lab: art direction with preservation rules

A useful image prompt describes a photographed event in physical terms: subject, materials, setting, light, lens position and intended crop. *Create a stunning premium product shot* does not tell the system what matters. For a genuine commercial product, supply approved reference photographs and declare which features must not change. When identity matters, use the actual photograph as the truthful source of product appearance.

```text
Create a 4:5 editorial campaign background for the attached amber
bottle. Keep the bottle geometry, cap, label placement, colour and
visible markings from the supplied reference unchanged. Place it on
unglazed stone beside a folded linen napkin. Late afternoon window
light enters from camera left; shadows fall right. Camera at bottle
height, neutral 50 mm photographic perspective, believable reflections
and surface texture. Leave uncluttered space above left for text to be
added later. Do not invent a logo, ingredient, printed claim, extra
bottle, floating splash or coloured glow. Show a short list of features
you preserved and any details you could not preserve reliably.
```

**Review in passes.** Pass one checks physical identity: number of parts, proportions, label and material. Pass two checks environmental logic: shadows, reflections, scale and hands. Pass three checks the crop and negative space for a headline. If the model distorts the label, return to an actual photographed product and use generation only for a background or concept image.

**Avoid the synthetic look.** Excessive rim lights, chrome reflections, wet surfaces, perfect symmetry and impossible shallow depth of field all compete with the product. Real editorial art direction uses an intentional imperfection: a lived-in tabletop, irregular linen fold and natural light falloff. This is not a request to fake damage or misrepresent the item.

**Technical note:** OpenAI's 2026 image release describes GPT Image 2.6 Sunburst and Flare with different speed/control characteristics, plus API options including SVG and animated GIF generation. The ChatGPT interface may expose the experience differently. Check the actual tool's export and editing options before committing a workflow.

**Official reference:** [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting).
