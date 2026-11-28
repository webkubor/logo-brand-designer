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
  <tr><td align="center"><a href="https://webkubor.github.io/kyvault/"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/kyvault/app-preview.png" width="80" height="80" alt="Ky · Kyvault 桌面版"></a></td><td align="center"><a href="https://github.com/webkubor/nativecrew"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/nativecrew/logo.svg" width="80" height="80" alt="NativeCrew"></a></td><td align="center"><a href="https://music.museav.top/"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/xianling-music/logo-light.svg" width="80" height="80" alt="仙灵music"></a></td><td align="center"><a href="https://wechat.webkubor.online/"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/chat-mood-gen/mark-v4.svg" width="80" height="80" alt="Chat Mood Gen"></a></td><td align="center"><a href="https://wallpaper.webkubor.online/"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/wallpaper-generator/mark-v4.svg" width="80" height="80" alt="氛围壁纸工坊"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/webkubor/claude-usage-statusline"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/claude-usage-statusline/mark-v3.svg" width="80" height="80" alt="claude-usage-statusline"></a></td><td align="center"><a href="https://github.com/webkubor/facet"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/facet/mark-v3.svg" width="80" height="80" alt="Facet"></a></td><td align="center"><a href="https://github.com/webkubor/fovea"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/fovea/logo.svg" width="80" height="80" alt="Fovea"></a></td><td align="center"><a href="https://github.com/webkubor/free-imgbed"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/free-imgbed/mark-v3.svg" width="80" height="80" alt="free-imgbed"></a></td><td align="center"><a href="https://github.com/webkubor/harnessweight"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/harnessweight/logo.svg" width="80" height="80" alt="HarnessWeight"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/supercli-site/supercli"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/supercli/mark-v3.svg" width="80" height="80" alt="SuperCLI"></a></td><td align="center"><a href="https://github.com/webkubor/vite-plugin-agent-eyes"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/vite-plugin-agent-eyes/mark-v3.svg" width="80" height="80" alt="vite-plugin-agent-eyes"></a></td><td align="center"><a href="https://xiaobai.supercli.site/"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@29eabaa7e83eca4026a05cf4b729664751e35569/xiaobai-kanban/logo.svg" width="80" height="80" alt="小白看板"></a></td></tr>
</table>
<!-- logo-wall:end -->

[Brand asset catalog](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md) · [Explore the full showcase](https://webkubor.github.io/logo-brand-designer/en/#cases) · [Skill instructions](SKILL.md) · [Offline review guide](references/reuse.md) · [Submit a project](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)

Code and documentation use the [MIT license](LICENSE). Product marks belong to their respective owners. See the [legal notice](https://webkubor.github.io/logo-brand-designer/legal/).
