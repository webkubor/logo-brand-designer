# 图床与作品墙同步

[free-imgbed 品牌资产清单](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md)登记现役标识、待核验和待设计项目，`brand/*.json` 记录每个项目的标识路径和状态。每次定稿，按图床原有入库方式归档，再更新品牌清单。旧标识需要替换时，先切换使用方的引用。

在图床提交已推到主分支后，刷新本仓的 README 和官网作品墙：

```sh
git -C /path/to/free-imgbed fetch origin main
python3 scripts/sync_logo_wall.py /path/to/free-imgbed
```

作品墙从 [已核对的项目与用图](current-logo-projects.json) 读取展示范围。更新这份清单前，核对项目仓库或官网仍可访问，记录实际使用的素材和证据。每个项目只放一张卡，卡片直接链接到项目或官网。桌面应用可用安装包里的图标核对图床预览。图床里标为 `ready` 的记录仍须完成现场核对。

脚本只读取已推送的图床文件，并把图片链接固定到对应提交。未获通过的设计及评审过程留在工作目录。经授权的演示案例单独标记。历史文件的迁移或移除需先核对已有引用。
