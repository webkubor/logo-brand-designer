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

| 产品 | 应用场景 |
| --- | --- |
| NativeCrew | 陶橙标识已用于 DSH 插件图标。 |
| 仙灵music | 暮紫音波用于工作台顶栏和浏览器标签。 |
| 氛围壁纸工坊 | 青柚渐变用于浏览器标签和安装图标。 |
| Chat Mood Gen | 青潮渐变用于编辑器、浏览器标签和安装图标。 |

[打开完整作品墙](https://webkubor.github.io/logo-brand-designer/#cases) · [查看技能说明](SKILL.md) · [生成离线评审页](references/reuse.md) · [提交社区作品](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)

代码与文档使用 [MIT 许可证](LICENSE)。案例标识的权利归各产品所有者。详见[法律声明](https://webkubor.github.io/logo-brand-designer/legal/)。
