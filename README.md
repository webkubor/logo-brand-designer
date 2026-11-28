# Logo Brand Designer

**从黑白轮廓到透明底 SVG，和你的 AI 助手一起把 Logo 做出来。**

这是给 Codex、Claude Code 等 AI 助手使用的开源技能。适合给新产品设计 Logo、更新旧标识，或把现有标识适配到插件侧栏和浏览器标签。

[![Release](https://img.shields.io/github/v/release/webkubor/logo-brand-designer)](https://github.com/webkubor/logo-brand-designer/releases/latest) [![Tests](https://github.com/webkubor/logo-brand-designer/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/webkubor/logo-brand-designer/actions/workflows/test.yml) [![License](https://img.shields.io/github/license/webkubor/logo-brand-designer)](LICENSE) [![Website](https://img.shields.io/badge/Website-GitHub%20Pages-57348d)](https://webkubor.github.io/logo-brand-designer/)

[官网与作品墙](https://webkubor.github.io/logo-brand-designer/) · [本地评审工作台](references/workbench.md) · [更新记录](CHANGELOG.md) · [English](README.en.md)

## 开始设计

```bash
npx skills add webkubor/logo-brand-designer
```

安装后，在项目里告诉你的 AI 助手：

> 用 logo-brand-designer 给这个项目设计 Logo。先读产品介绍，给我几种黑白轮廓。等我选定形态后再试配色，最后给我看深浅背景和小尺寸的效果。

也可以克隆仓库运行 `./install.sh`，用 `./install.sh --list` 查看安装位置。离线评审工具需要 Python 3.9+。

## 从候选到交付

1. **选形。** 并排比较黑白候选，记下识别点和淘汰理由。
2. **定色。** 保持轮廓，比较不同配色在深浅背景上的表现。
3. **评审。** 打开本地工作台选方案，也可以直接写修改建议，保存到时间线。
4. **交付。** 导出透明底 SVG、颜色规范、设计说明和离线评审页。按插件、应用或浏览器的实际使用场景检查小图。

## 看一次真实评审

下图是 Godbot 标识探索当时的浏览器截图。三款蓝紫候选和评审意见都保存在归档示例里，可用来走一遍选形、配色、比较和文字反馈。

[![Godbot 标识候选与文字反馈输入框](examples/godbot-experiment/screenshots/review.png)](examples/godbot-experiment/README.md)

## 已用在产品里的标识

<!-- logo-wall:start -->
<table>
  <tr><td align="center"><a href="https://github.com/webkubor/nativecrew"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/nativecrew/logo.svg" width="80" height="80" alt="NativeCrew"></a></td><td align="center"><a href="https://github.com/xianling-music/xianling-music"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/xianling-music/logo-light.svg" width="80" height="80" alt="仙灵音乐"></a></td><td align="center"><a href="https://github.com/webkubor/chat-mood-gen"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/chat-mood-gen/mark-v4.svg" width="80" height="80" alt="Chat Mood Gen"></a></td><td align="center"><a href="https://github.com/webkubor/wallpaper-generator"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/wallpaper-generator/mark-v4.svg" width="80" height="80" alt="氛围壁纸工坊（wallpaper-generator）"></a></td><td align="center"><a href="https://github.com/webkubor/claude-usage-statusline"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/claude-usage-statusline/mark-v3.svg" width="80" height="80" alt="claude-usage-statusline"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/cortexos-dev/.github"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/cortexos-dev/logo.svg" width="80" height="80" alt="CortexOS"></a></td><td align="center"><a href="https://github.com/webkubor/device-passport"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/device-passport/mark-v3.svg" width="80" height="80" alt="device-passport"></a></td><td align="center"><a href="https://github.com/webkubor/dsh-llm-hub"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/dsh-llm-hub/mark-v3.svg" width="80" height="80" alt="dsh-llm-hub"></a></td><td align="center"><a href="https://github.com/webkubor/facet"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/facet/mark-v3.svg" width="80" height="80" alt="Facet"></a></td><td align="center"><a href="https://github.com/webkubor/fovea"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/fovea/logo.svg" width="80" height="80" alt="Fovea"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/webkubor/free-imgbed"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/free-imgbed/mark-v3.svg" width="80" height="80" alt="free-imgbed"></a></td><td align="center"><a href="https://github.com/webkubor/harnessweight"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/harnessweight/logo.svg" width="80" height="80" alt="HarnessWeight"></a></td><td align="center"><a href="https://github.com/webkubor/kyvault"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/kyvault/logo.svg" width="80" height="80" alt="Ky · Kyvault 桌面版"></a></td><td align="center"><a href="https://github.com/museav-ai/.github"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/museav-ai/logo.svg" width="80" height="80" alt="MUSE AV"></a></td><td align="center"><a href="https://github.com/webkubor/reel-kit"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/reel-kit/mark-v3.svg" width="80" height="80" alt="reel-kit"></a></td></tr>
  <tr><td align="center"><a href="https://github.com/webkubor/scorecard"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/scorecard/mark-v3.svg" width="80" height="80" alt="Scorecard"></a></td><td align="center"><a href="https://github.com/supercli-site/supercli"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/supercli/mark-v3.svg" width="80" height="80" alt="SuperCLI"></a></td><td align="center"><a href="https://github.com/webkubor/vite-plugin-agent-eyes"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/vite-plugin-agent-eyes/mark-v3.svg" width="80" height="80" alt="vite-plugin-agent-eyes"></a></td><td align="center"><a href="https://github.com/webkubor/voxflow"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/voxflow/mark-v3.svg" width="80" height="80" alt="VoxFlow 声流"></a></td><td align="center"><a href="https://github.com/supercli-site/xiaobai-kanban"><img src="https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@cc56e320c368c3011547d8c960888b1c212dfb64/xiaobai-kanban/logo.svg" width="80" height="80" alt="小白看板"></a></td></tr>
</table>
<!-- logo-wall:end -->

[图床标识清单](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md) · [打开完整作品墙](https://webkubor.github.io/logo-brand-designer/#cases) · [查看技能说明](SKILL.md) · [生成离线评审页](references/reuse.md) · [提交社区作品](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)

代码与文档使用 [MIT 许可证](LICENSE)。案例标识的权利归各产品所有者。详见[法律声明](https://webkubor.github.io/logo-brand-designer/legal/)。
