# 更新记录

## [0.8.0] - 2026-11-25

> **一句话摘要**：在评审页记录阶段建议，定稿后按项目既有流程归集素材并核验交付结果。

### ✨ 新增特性 (What's New)

- 本地评审工作台增加“补充建议”输入框，可直接保存当前阶段的意见，并在时间线上回看；每条最多 500 字。
- 技能的最终交付增加素材归集步骤：项目已指定素材库时，沿用已有 CLI、目录与索引规则，提交适合分发的定稿素材，并记录实际路径与链接。没有指定素材库时仍保留本地交付，不引入新的云服务依赖。

### ⚡️ 体验与性能优化 (Improvements)

- 归集时保留母版、manifest、评审页和真实截图的来源记录；相同素材复用已有来源，新版本使用新路径，便于后续项目引用。

### 🐛 缺陷修复 (Bug Fixes)

- 交付指令要求分别核验本地入库、远端推送和链接内容，避免将 CLI 打印链接误报为已发布；不把未批准候选或受限资料随正式素材公开上传。

### ⚠️ 破坏性变更与迁移 (Breaking Changes & Migration)

- 无破坏性变更（100% 向后兼容）。现有评审 manifest 可继续使用，素材库按当前项目配置选择。

### 📦 安装与升级 (Install & Upgrade)

支持导入 Skill 的工具可下载本版的 `logo-brand-designer-0.8.0.skill`。也可安装指定版本；以下源码安装方式需要已配置 GitHub SSH：

```bash
git clone --branch v0.8.0 git@github.com:webkubor/logo-brand-designer.git logo-brand-designer-0.8.0
cd logo-brand-designer-0.8.0
./install.sh --copy
```

## [0.7.2] - 2026-11-24

> **一句话摘要**：在本地工作台分阶段确认 Logo，从黑白轮廓、深浅底配色一路收到透明 SVG 定稿。

### ✨ 新增特性 (What's New)

- 新增[本地 Logo 评审工作台](https://github.com/webkubor/logo-brand-designer/blob/v0.7.2/references/workbench.md)。可记录形态、配色和定稿选择，切换浅底、深底与透明网格，下载原始 SVG。进度和决定保存在本机，重启后可恢复。
- [品牌设计官网](https://webkubor.github.io/logo-brand-designer/#journey)展示 NativeCrew 和仙灵music 的实际设计过程，[社区展台](https://webkubor.github.io/logo-brand-designer/showcase/)开放作品投稿。

### ⚡️ 体验与性能优化 (Improvements)

- 新增黑白轮廓与配色参考。确定轮廓后以原稿为母版比较色层、渐变和深浅底效果。
- 字标验收增加轮廓化要求。派生图标按真实相邻颜色检查对比度，并在实际宿主中核对显示。

### 🐛 缺陷修复 (Bug Fixes)

- 修复仙灵music 案例链接与社交分享图，使案例指向独立产品站。

### ⚠️ 破坏性变更与迁移 (Breaking Changes & Migration)

- 无破坏性变更（100% 向后兼容）。现有评审 manifest 可继续使用，本地工作台是可选入口。

### 📦 安装与升级 (Install & Upgrade)

支持导入 Skill 的工具可直接下载本页的 `logo-brand-designer-0.7.2.skill`。也可安装指定版本：

```bash
git clone --branch v0.7.2 https://github.com/webkubor/logo-brand-designer.git logo-brand-designer-0.7.2
cd logo-brand-designer-0.7.2
./install.sh --copy
```

## [0.6.0] - 2026-11-10

> 在已有品牌基础上设计应用图标，并在评审页检查深浅主题的小尺寸效果。

### ✨ 新增特性 (What's New)

- 增加侧栏图标、应用图标和 favicon 的派生流程，核实宿主渲染方式、背景、主题及实际尺寸。
- 离线评审页支持 `iconAsset` 和可选的 `iconDarkAsset`，同时展示 16px 与 24px 预览。

### ⚡️ 体验与性能优化 (Improvements)

- 补充英文使用说明、Agent 索引和技能触发边界用例。

### 🐛 缺陷修复 (Bug Fixes)

- 解释独立 SVG 作为图片加载时不会继承宿主文字颜色，避免误判深色主题图标。
- 修复 CI 系统升级导致 Python 3.9 测试环境不可用的问题。

### ⚠️ 破坏性变更与迁移 (Breaking Changes & Migration)

- 本版新增 manifest 字段均为可选；评审页预览仍需结合实际宿主截图验收。

### 📦 安装与升级 (Install & Upgrade)

```bash
git clone https://github.com/webkubor/logo-brand-designer.git
cd logo-brand-designer
./install.sh
```
