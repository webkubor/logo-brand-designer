# logo-brand-designer

为项目设计、重设计或验收品牌标识的 agent skill。先核对生产资料与用户要求，再交付 design token、设计理念、透明底 1:1 SVG、离线评审 HTML 和真实截图。

## 安装

克隆到用户级 skill 目录，仓库根目录即 skill 入口：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/webkubor/logo-brand-designer.git ~/.agents/skills/logo-brand-designer
```

安装后在支持该目录的 agent 中重新加载 skills。若目标目录已有文件，先比较再更新；ZCode 的 `~/.zcode/skills/` 同名副本优先级更高，需要一并核对。

## 使用

```text
用 logo-brand-designer 为当前项目做 logo；先读取生产资料，沿用我提供的 token、理念和 SVG，交付透明底 1:1 SVG、独立评审 HTML 与真实截图，并注明来源和实际验收范围。
```

支持首次设计（无旧图）、重设计对照、共用或独立深底版本。详细流程见 [SKILL.md](SKILL.md)，manifest 字段见 [references/reuse.md](references/reuse.md)。

## 生成评审页

生成器使用 Python 3.9+ 标准库，无第三方依赖。按 [manifest 示例](references/manifest-example.json) 准备 `delivery/manifest.json` 与其中引用的素材、来源文件；示例含占位路径，需替换后使用。本地输入路径以 manifest 所在目录为根。

```bash
SKILL_DIR="$HOME/.agents/skills/logo-brand-designer"
DELIVERY_DIR="./delivery"
python3 "$SKILL_DIR/scripts/build_review.py" \
  --manifest "$DELIVERY_DIR/manifest.json" \
  --out "$DELIVERY_DIR/review.html"
```

在浏览器打开 `review.html`，可离线切换浅底、深底、棋盘与 32/64/128px，下载素材/JSON，复制含完整 SVG 的任务。

生成器只检查结构，不渲染像素或生成截图。透明度、留白、颜色和 32px 可辨性需另用渲染器与浏览器实测，真实截图保存到交付目录 `screenshots/`，记录来源及测试范围。

## 开发

在仓库根目录运行：

```bash
python3 -m unittest discover -s tests -v
```

测试实际调用生成 CLI，覆盖首次设计、深底素材、安全 SVG 与路径边界。CI 在 Ubuntu 上运行同一命令。

[MIT License](LICENSE)
