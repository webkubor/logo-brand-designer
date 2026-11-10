# 更新记录

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
