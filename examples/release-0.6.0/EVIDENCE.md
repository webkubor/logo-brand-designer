# 0.6.0 发布媒体 · 真实渲染与验证证据

本目录是 `logo-brand-designer` 0.6.0 的发布媒体：真实渲染的当前版本截图、可播放视频，以及每一步验证的命令与实际输出。

- 生成环境：macOS（darwin 24.3.0），worktree `promo/app-icon`，HEAD `0a66128`
- 浏览器：Google Chrome 157.0.8103.50（Playwright 1.58.0 驱动 `channel="chrome"`，非模拟）
- 渲染器：`rsvg-convert` /opt/homebrew/bin；`ffmpeg` /opt/homebrew/bin
- 图像校验：Pillow 12.1.1
- 素材来源：全部派生自仓库既有 `examples/cortexos/corner/mark.svg`，**未新增品牌设计**

---

## 1. 评审页生成（真实工具输出）

```bash
cd examples/release-0.6.0
python3 ../../scripts/build_review.py --manifest manifest.json --out review.html
```

实际输出：

```
OK: 1 project(s) -> …/examples/release-0.6.0/review.html
结构校验通过。仅做结构检查；未解码/渲染像素，未验证透明度、留白、非空图、token 与实际颜色一致性或 32px 可辨性。需要另行真实渲染并目视验收。
```

退出码 `0`。过程中工具两次真实拦截并已修正：缺 `<title>` 时报 `ERROR: probe.asset 缺少非空 title`；`sourceFiles` 指向不存在文件时报 `ERROR: sourceFiles 文件不存在：EVIDENCE.md`。

> 注意：上面这段「结构校验通过」是工具自述，**不等于像素验收**。像素与行为验收见第 3、4 节。

---

## 2. 素材与透明底真实渲染

```bash
rsvg-convert -w 16 -h 16 assets/mark.svg -o /tmp/fix/m-16.png   # 24 / 32 / 128 同理
```

Pillow 逐像素读取 alpha 通道（`convert("RGBA")` 后统计 A 通道）：

| 尺寸 | alpha 包围盒 | 完全不透明像素 | 半透明像素 | 总像素 |
|---|---|---|---|---|
| 16px | (1, 1, 15, 15) | 97 | 58 | 256 |
| 24px | (2, 2, 22, 22) | 238 | 94 | 576 |
| 32px | (3, 2, 30, 29) | 432 | 128 | 1024 |
| 128px | (14, 11, 117, 114) | 7667 | 514 | 16384 |

结论：SVG 无底色 rect，渲染结果确有 alpha 通道、四周有真实透明边（16px 包围盒未触边），主体不空。

### 对比度实测（WCAG 相对亮度公式）

```
primary       #4F46E5 on #FFFFFF = 6.29:1
accent        #5EEAD4 on #FFFFFF = 1.48:1
gHot_end      #22D3EE on #FFFFFF = 1.81:1
gA_dark_end   #312E81 on #FFFFFF = 11.42:1
primary       #4F46E5 on #0D1117 = 3.01:1
accent        #5EEAD4 on #0D1117 = 12.79:1
gHot_end      #22D3EE on #0D1117 = 10.47:1
gA_dark_end   #312E81 on #0D1117 = 1.66:1
```

说明：`accent #5EEAD4` 是浅底上的浅色，只在深底使用（12.79:1）；这是示例素材的既有用色，未改动。

---

## 3. 浏览器行为验证（真实 Chrome 驱动真实 review.html）

用 Playwright 驱动系统 Chrome 打开 `review.html`（`file://`），点击页面上的真实按钮并读取真实 DOM。

### 3.1 派生图标深底切换与 caption

有 `iconDarkAsset` 时（`assets/app-icon-dark.svg`，仅把 `gA` 渐变两端换成深色档，几何未改）：

| 背景 | caption 实际文本 | 图标 data URI 长度 |
|---|---|---|
| 浅底 | `应用图标 · 主版本 · 24px / 16px（宿主实际底色另行核对）` | 1434 |
| 深底 | `应用图标 · 深色版 · 24px / 16px（宿主实际底色另行核对）` | **1454** |
| 棋盘 | `应用图标 · 主版本 · 24px / 16px（宿主实际底色另行核对）` | 1434 |

深底时 data URI 长度由 1434 变为 1454，说明**确实换成了深色版素材**，不是仅改文案。

### 3.2 无深底素材时回退主图

把 `iconDarkAsset` 从 manifest 移除后重新生成 `review.html`，同一浏览器复测：

| 背景 | caption 实际文本 | 图标 data URI 长度 |
|---|---|---|
| 浅底 | `应用图标 · 主版本 · 24px / 16px（宿主实际底色另行核对）` | 1434 |
| 深底 | `应用图标 · 主版本 · 24px / 16px（宿主实际底色另行核对）` | **1434** |
| 棋盘 | `应用图标 · 主版本 · 24px / 16px（宿主实际底色另行核对）` | 1434 |

深底时长度不变（1434），caption 保持「主版本」，即**回退到主图且文案如实标注主版本**，没有残留深色版。

### 3.3 页面无 JS 错误

`capture-report.json` 中 `console_errors: []`、`page_errors: []`。

---

## 4. 视频与 GIF：真实编码 + 真实浏览器播放

### 4.1 录制

Playwright `record_video` 录制真实 Chrome 页面操作（切浅/深/棋盘底、32/64/128px），产物为 VP8 webm，再由 ffmpeg 转码：

```bash
ffmpeg -y -i <recorded>.webm \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -preset medium -crf 23 \
  -movflags +faststart -r 30 review-0.6.0.mp4

ffmpeg -y -i <recorded>.webm \
  -vf "fps=12,scale=840:-1:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3" \
  -loop 0 review-0.6.0.gif
```

### 4.2 MP4 合规性（ffprobe + box 解析 + 全量解码）

```
codec_name=h264   profile=High   pix_fmt=yuv420p   width=1120   height=940   r_frame_rate=30/1
duration=13.933008   size=308729
```

顶层 box 顺序 `['ftyp', 'moov', 'free', 'mdat']` → **`moov` 在 `mdat` 之前，即 faststart 生效**，GitHub/浏览器可边下边播。

全量解码校验 `ffmpeg -v error -i review-0.6.0.mp4 -f null -` 无任何输出（无解码错误）。

### 4.3 真实浏览器播放（HTTP + Range，模拟 GitHub 静态托管）

用带 HTTP Range 支持的本地静态服务托管**真实文件**，在真实 Chrome 中加载 `<video>` 与 `<img>`：

```
HTTP: {"status": 200, "content_type": "video/mp4", "accept_ranges": "bytes", "content_length": "308729"}
Range GET → 206 Partial Content, content-range: bytes 0-1023/308729
MP4: {"readyState": 4, "duration": 13.933008, "videoWidth": 1120, "videoHeight": 940,
      "currentTime": 1.8718, "paused": false, "error": null, "t0": 0, "t1": 1.8619, "advanced": true}
GIF: {"naturalWidth": 840, "naturalHeight": 705, "complete": true}
=== PLAYBACK VERDICT: PASS ===
```

`readyState: 4`（HAVE_ENOUGH_DATA）、`paused: false`、`error: null`、`currentTime` 从 0 推进到 1.86 秒，证明**真实浏览器真的在解码并播放**，不是只看了文件头。

播放实拍：`screenshots/playback-mp4-in-browser.png`、`screenshots/playback-gif-in-browser.png`。

---

## 5. GitHub 内「可直接播放」的机制结论（服务端实测）

这是本次发布媒体的**关键约束**，已用 GitHub 服务端 API 核实，不是推测。

```bash
gh api -X POST markdown --input -   # {"text": "...", "mode": "gfm", "context": "webkubor/logo-brand-designer"}
```

实测结果：

| 输入 | GitHub 返回 |
|---|---|
| `<video src="a.mp4" controls></video>` | `<p dir="auto"></p>` — **video 标签被剥离** |
| `<video src="…/user-attachments/assets/<uuid>" controls>` | `<p dir="auto"></p>` — 同样被剥离 |
| `![Video](media/x.mp4)` | `<p dir="auto"><a …><img src="media/x.mp4" …></a></p>` |
| `![alt](a.png)` / `<a href="a.mp4">` | 正常保留 |

换 `mode: markdown` 复测，结论一致（video 一律被剥离，img/a 正常）。

同时核对 `github/html-pipeline` 的 `sanitization_filter.rb`：`WHITELIST[:elements]` 为

```
h1 h2 h3 h4 h5 h6 h7 h8 br b i strong em a pre code img tt
div ins del sup sub p ol ul table thead tbody tfoot blockquote
dl dt dd kbd q samp var hr ruby rt rp li tr td th s strike summary details
```

**不含 `video`**。

结论：
- README 里原生 `<video>` 不会被 GitHub 渲染成播放器，`<video>` 标签在服务端就被删掉了。
- **GIF 以 `![](…)` 内联引用时，浏览器会直接自动播放** → 这是 GitHub 页面内「可直接播放」的可靠形式，本目录 `media/review-0.6.0.gif` 即为此用。
- **MP4 以 `![](…)` / 链接引用不会自动播放**，需外链到可直放地址（如 `user-attachments`）由浏览器播放；本目录 MP4 为 H.264 + faststart + yuv420p 的浏览器通用规格，可直接用于外链或作为下载物。

---

## 6. 产物清单

| 文件 | 说明 | 来源 |
|---|---|---|
| `review.html` | 0.6.0 离线评审页（内嵌素材，无网依赖） | `scripts/build_review.py` 生成 |
| `manifest.json` | 生成评审页的清单 | 本目录 |
| `assets/mark.svg` | 主标志（派生自 `examples/cortexos/corner/mark.svg`，仅补 `<title>`） | 既有素材 |
| `assets/app-icon.svg` | 派生应用图标槽位素材（几何同主标志） | 既有素材 |
| `assets/app-icon-dark.svg` | 深底派生图标（几何未改，仅 `gA` 渐变换深色档） | 既有素材派生 |
| `screenshots/review-{light,dark,checker}.png` | 三种底色的整页实拍 | 真实 Chrome 截图 |
| `screenshots/canvas-{light,dark,checker}-0.png` | 单个画布特写 | 真实 Chrome 截图 |
| `screenshots/icon-{light,dark,checker}.png` | 派生图标行特写 | 真实 Chrome 截图 |
| `screenshots/review-size-128.png` | 128px 尺寸状态整页 | 真实 Chrome 截图 |
| `screenshots/playback-{mp4,gif}-in-browser.png` | 视频/GIF 播放实拍 | 真实 Chrome 截图 |
| `media/review-0.6.0.mp4` | H.264 + faststart，浏览器可直放 | ffmpeg 编码自真实录屏 |
| `media/review-0.6.0.gif` | GitHub README 内联自动播放用 | ffmpeg 编码自真实录屏 |
| `capture-report.json` | 截图脚本的 DOM 状态、控制台错误、文件 sha256 | 真实运行产物 |

### sha256

```
8a512a8ba23a0f5e5e2a27ce569f6cf834854fac68c2bbaba5ad7aac6fa17c22  media/review-0.6.0.mp4
edf8122f3021e3f60df71584a539685703d766732a5c4834f2c5d2bbf0934a75  media/review-0.6.0.gif
be40b4c75121c6dfdc04f9cae4be0c61c341b5b67342db1c53b473c9f4d839f3  review.html
```

（以 `shasum -a 256` 实测输出为准，见下方「复核命令」。）

---

## 7. 复核命令

```bash
cd examples/release-0.6.0
shasum -a 256 media/review-0.6.0.mp4 media/review-0.6.0.gif review.html assets/*.svg
ffprobe -v error -show_entries stream=codec_name,profile,pix_fmt,width,height \
  -show_entries format=duration,size -of default=noprint_wrappers=1 media/review-0.6.0.mp4
ffmpeg -v error -i media/review-0.6.0.mp4 -f null -          # 无输出即解码干净
```

---

## 8. 未做 / 未验证项（如实记录）

- **未推送、未发版**：本目录仅本地提交，按任务要求不推送、不发布。
- **未做 GitHub 线上页面实看**：本次不推送，因此无法以匿名访客打开真实 README 页面确认播放器。GitHub 侧结论来自 `gh api -X POST markdown` 服务端实测与 `html-pipeline` 白名单核对，属服务端行为核实，但**不等同于在真实仓库页面上目视确认**。
- **未做 16px 视觉可辨性人工判读**：16px 仅有像素级 alpha 与数量统计（97 不透明 + 58 半透明像素），没有真人判读结论。
- **未做色觉模拟、任意彩底测试**：仅覆盖评审页自带的浅底 #FFFFFF / 深底 #0D1117 / 棋盘三种。
- **未做宿主槽位实拍**：24px / 16px 是在评审页模拟槽位中验证，真实宿主（如侧栏、插件列表、favicon）底色与渲染方式未实测。
- **未做无障碍播放心测**：未使用读屏软件验证 caption 文本朗读。
- **示例素材非定稿品牌**：`assets/*` 派生自仓库既有 CortexOS 示例标志，对外发布前应替换为已确认资产。
