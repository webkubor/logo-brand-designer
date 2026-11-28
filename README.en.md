# Logo Brand Designer

**Design a logo with your AI assistant, from monochrome sketches to a transparent SVG.**

An open source skill for Codex, Claude Code, and other compatible assistants. Use it to create a product mark, revisit an existing identity, or adapt a mark to a plugin sidebar or browser tab.

[![Release](https://img.shields.io/github/v/release/webkubor/logo-brand-designer)](https://github.com/webkubor/logo-brand-designer/releases/latest) [![Tests](https://github.com/webkubor/logo-brand-designer/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/webkubor/logo-brand-designer/actions/workflows/test.yml) [![License](https://img.shields.io/github/license/webkubor/logo-brand-designer)](LICENSE) [![Website](https://img.shields.io/badge/Website-GitHub%20Pages-57348d)](https://webkubor.github.io/logo-brand-designer/)

[Website and showcase](https://webkubor.github.io/logo-brand-designer/en/) · [Local review workbench](references/workbench.md) · [Changelog](CHANGELOG.md) · [中文](README.md)

## Quick start

```bash
npx skills add webkubor/logo-brand-designer
```

Ask your assistant:

> Use logo-brand-designer for this project. Read the product brief, show me a few monochrome shapes, and wait for my choice before exploring color. Show the selected mark on light and dark backgrounds and at small sizes.

You can also clone the repo and run `./install.sh`. The offline review tools require Python 3.9+.

## How it works

1. Compare monochrome shapes and record why each direction was kept or dropped.
2. Keep the chosen outline while trying color treatments on light and dark backgrounds.
3. Choose options or write feedback in the local review workbench. Notes appear in the timeline.
4. Export transparent SVGs, color specifications, design notes, and an offline review page. Check small icons in the intended product surface.

## A real review session

This browser screenshot comes from the archived Godbot design exercise. The case preserves three blue and violet concepts and the feedback workflow.

[![Godbot logo concepts and written feedback form](examples/godbot-experiment/screenshots/review.png)](examples/godbot-experiment/README.md)

## Shipped work

NativeCrew uses the orange mark in its DSH plugin. 仙灵music uses the mauve waveform in its workbench header and browser tab. The showcase also features Ambient Wallpaper Studio and Chat Mood Gen.

[Explore the full showcase](https://webkubor.github.io/logo-brand-designer/en/#cases) · [Skill instructions](SKILL.md) · [Offline review guide](references/reuse.md) · [Submit a project](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)

Code and documentation use the [MIT license](LICENSE). Product marks belong to their respective owners. See the [legal notice](https://webkubor.github.io/logo-brand-designer/legal/).
