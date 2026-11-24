# logo-brand-designer

给 Codex、Claude Code 和其他支持 Agent Skills 的工具用的 **Logo 设计技能**。和 Agent 一起比较轮廓、选定配色，再拿到透明底 SVG、浏览器图标和能独立打开的评审页。

[官网](https://webkubor.github.io/logo-brand-designer/) · [社区作品](https://webkubor.github.io/logo-brand-designer/showcase/) · [English](README.en.md)

## 已用在产品里的 Logo

| Logo | 产品 | 设计过程 |
|---|---|---|
| <img src="docs/assets/nativecrew.png" width="80" alt="NativeCrew 的陶橙标识"> | [NativeCrew](https://www.npmjs.com/package/@dsh-plugins/nativecrew) · DSH 多 Agent 团队工作台 | 先确定单一外轮廓，再用宽幅陶橙色层做出深浅。成品已用于插件图标。 |
| <img src="docs/assets/museav-music-light.svg" width="116" alt="MuseAV Music 的暮紫音波标识"> | [MuseAV Music](https://www.museav.top/ecosystem) · Suno 作品整理与发行工作台 | 在黑白稿选定 01B 音波，接着在深浅背景比较配色。定稿为 02 暮紫，已用于工作台顶栏与标签页。 |

这些标识供案例展示，品牌权利归各产品所有者。

## 安装和使用

安装到支持 Agent Skills 的工具：

```bash
npx skills add webkubor/logo-brand-designer
```

也可以克隆仓库后运行 `./install.sh`。安装脚本负责放置 Skill，离线评审页生成器使用 Python 3.9+ 标准库。运行 `./install.sh --list` 可查看安装位置。

安装后把需求交给你的 Agent，例如：

> 用 logo-brand-designer 给我的项目设计 Logo。先看产品和现有品牌资料，给我几种黑白轮廓。选定形态后，保留原轮廓做配色，再给我看深浅背景和小尺寸的效果。

## 从设计到落地

1. **定形。** 比较黑白剪影和小尺寸识别，选中的轮廓保存为源文件。
2. **定色。** 让同一款轮廓在深浅背景上比较色彩，记录最终色值和渐变定义。
3. **验收。** 实际渲染检查透明画布、留白和小图可辨性。确认后交付标志、字标组合及所需图标，在产品里核对显示。

[技能说明](SKILL.md) · [离线评审页生成方法](references/reuse.md) · [更新记录](CHANGELOG.md)

## 分享你的作品

[提交 Logo 作品](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml)，填写公开的项目名、图片、简介和链接。提交会同步到[社区展台](https://webkubor.github.io/logo-brand-designer/showcase/)，访客可以直接打开你的项目。

仓库代码与文档使用 [MIT](LICENSE)。
