---
name: motion-primitives
description: Reference React + Framer Motion (motion/react) animated components — accordions, dialogs, dock, magnetic buttons, text effects, tilt, spotlight, carousel, and more. Use when the user needs a ready-made, accessible, customizable animated UI primitive rather than building motion from scratch. Copy the relevant component from components/ into the project and adjust props; do not use as a package dependency.
---

# motion-primitives

Vendored from [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) (MIT).
Not a package — these are copy-paste source components (same model as shadcn/ui), each a
single self-contained `.tsx` file under `components/` built on React + `motion/react`
(Framer Motion) + Tailwind CSS.

## When to use

Reach for one of these when the task needs a specific, well-crafted animated interaction
and reinventing it would be wasted effort: an accordion, a magnetic hover button, a
morphing dialog/popover, a spotlight or glow hover effect, animated numbers/text (loop,
morph, roll, scramble, shimmer), a tilt card, an infinite slider, a dock, or a
transition panel.

## How to use

1. Pick the matching file from `components/` (33 available — see list below).
2. Read it, then copy it into the target project's component directory (e.g.
   `components/ui/` or `components/motion/`), adjusting the import path for `cn`/utility
   helpers to match the project's own setup.
3. Ensure the project has `motion` (npm package, formerly `framer-motion`) and Tailwind
   CSS installed — these components assume both.
4. Adapt props/styling to the project's design tokens rather than using verbatim.

## Available components

accordion, animated-background, animated-group, animated-number, border-trail, carousel,
cursor, dialog, disclosure, dock, glow-effect, image-comparison, in-view,
infinite-slider, magnetic, morphing-dialog, morphing-popover, progressive-blur,
scroll-progress, sliding-number, spinning-text, spotlight, text-effect, text-loop,
text-morph, text-roll, text-scramble, text-shimmer-wave, text-shimmer, tilt,
toolbar-dynamic, toolbar-expandable, transition-panel

Live demos and docs for each: https://motion-primitives.com/
