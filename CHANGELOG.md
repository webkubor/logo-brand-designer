# 更新记录

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
