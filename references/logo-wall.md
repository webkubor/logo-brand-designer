# 图床与作品墙同步

[free-imgbed 品牌资产清单](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md)登记现役标识、待核验和待设计项目，`brand/*.json` 记录每个项目的标识路径和状态。每次定稿，按图床原有入库方式归档，再更新品牌清单。旧标识需要替换时，先切换使用方的引用。

在图床提交已推到主分支后，刷新本仓的 README 和官网作品墙：

```sh
git -C /path/to/free-imgbed fetch origin main
python3 scripts/sync_logo_wall.py /path/to/free-imgbed
```

脚本读取图床远端主分支的清单，只展示 `ready` 的素材。同一图床文件只展示一次，归档在评审页的探索稿继续留在原案例中。图片链接固定到生成时的图床提交，便于核对来源。提交前核对图片可访问、链接指向正确项目，再发布作品墙。

[待设计项目](https://github.com/webkubor/free-imgbed/blob/main/BRAND-ASSETS.md#待设计或核验)以图床清单为入口。作品墙的标识数是可展示的去重数量，统计产品覆盖时另以产品清单逐项对照。
