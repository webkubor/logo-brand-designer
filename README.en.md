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

## Brand mark gallery

<!-- logo-wall:start -->
<table>
  <tr><td align="center"><a href="https://github.com/webkubor/nativecrew"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/nativecrew/logo.svg" width="80" height="80" alt="NativeCrew"></a></td><td align="center"><a href="https://github.com/xianling-music/xianling-music"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/xianling-music/logo-light.svg" width="80" height="80" alt="仙灵音乐"></a></td><td align="center"><a href="https://github.com/webkubor/chat-mood-gen"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/chat-mood-gen/mark-v4.svg" width="80" height="80" alt="Chat Mood Gen"></a></td><td align="center"><a href="https://github.com/webkubor/wallpaper-generator"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/wallpaper-generator/mark-v4.svg" width="80" height="80" alt="氛围壁纸工坊（wallpaper-generator）"></a></td><td align="center"><a href="https://github.com/webkubor/claude-usage-statusline"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/claude-usage-statusline/mark-v3.svg" width="80" height="80" alt="claude-usage-statusline"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/cortexos-dev/.github"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/cortexos-dev/logo.svg" width="80" height="80" alt="CortexOS"></a></td><td align="center"><a href="https://github.com/webkubor/device-passport"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/device-passport/mark-v3.svg" width="80" height="80" alt="device-passport"></a></td><td align="center"><a href="https://github.com/webkubor/dsh-llm-hub"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/dsh-llm-hub/mark-v3.svg" width="80" height="80" alt="dsh-llm-hub"></a></td><td align="center"><a href="https://github.com/webkubor/facet"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/facet/mark-v3.svg" width="80" height="80" alt="Facet"></a></td><td align="center"><a href="https://github.com/webkubor/fovea"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/fovea/logo.svg" width="80" height="80" alt="Fovea"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/webkubor/free-imgbed"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/free-imgbed/mark-v3.svg" width="80" height="80" alt="free-imgbed"></a></td><td align="center"><a href="https://github.com/webkubor/harnessweight"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/harnessweight/logo.svg" width="80" height="80" alt="HarnessWeight"></a></td><td align="center"><a href="https://github.com/webkubor/kyvault"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/kyvault/logo.svg" width="80" height="80" alt="Ky · Kyvault 桌面版"></a></td><td align="center"><a href="https://github.com/museav-ai/.github"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/museav-ai/logo.svg" width="80" height="80" alt="MUSE AV"></a></td><td align="center"><a href="https://github.com/webkubor/reel-kit"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/reel-kit/mark-v3.svg" width="80" height="80" alt="reel-kit"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/webkubor/scorecard"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/scorecard/mark-v3.svg" width="80" height="80" alt="Scorecard"></a></td><td align="center"><a href="https://github.com/supercli-site/supercli"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/supercli/mark-v3.svg" width="80" height="80" alt="SuperCLI"></a></td><td align="center"><a href="https://github.com/webkubor/vite-plugin-agent-eyes"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/vite-plugin-agent-eyes/mark-v3.svg" width="80" height="80" alt="vite-plugin-agent-eyes"></a></td><td align="center"><a href="https://github.com/webkubor/voxflow"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/voxflow/mark-v3.svg" width="80" height="80" alt="VoxFlow 声流"></a></td><td align="center"><a href="https://github.com/supercli-site/xiaobai-kanban"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/xiaobai-kanban/logo.svg" width="80" height="80" alt="小白看板"></a></td></tr>
</table>
<!-- logo-wall:end -->

[Brand asset catalog](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md) · [Explore the full showcase](https://webkubor.github.io/logo-brand-designer/en/#cases) · [Skill instructions](SKILL.md) · [Offline review guide](references/reuse.md) · [Submit a project](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)

Code and documentation use the [MIT license](LICENSE). Product marks belong to their respective owners. See the [legal notice](https://webkubor.github.io/logo-brand-designer/legal/).
