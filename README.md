# logo-brand-designer

**给零基础用户的 Logo 设计技能。** 告诉 Codex 或 Claude Code 你的产品做什么，就能一步步选轮廓、选配色，拿到有辨识度的透明底 SVG、浏览器图标和评审页。

[在用标识展示](https://webkubor.github.io/logo-brand-designer/#cases) · [English](README.en.md) · [法律声明](https://webkubor.github.io/logo-brand-designer/legal/)

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

[技能说明](SKILL.md) · [离线评审页](references/reuse.md) · [本地评审工作台](references/workbench.md) · [更新记录](CHANGELOG.md)

仓库代码与文档使用 [MIT](LICENSE)。
