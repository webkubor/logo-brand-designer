# 本地 Logo 评审工作台

用一个浏览器页面看形态、配色和最终确认。页面从本地读取评审 manifest，进度和选择保存到独立 JSON。服务用 Python 3.9+ 标准库，运行于 macOS 或 Linux。

## 开始一个项目

为形态和配色各准备一份[评审 manifest](reuse.md)。每份清单包含该阶段候选及素材。配色清单应使用已确认的形态。配色文件尚未生成时，可以先填写未来会用的文件路径。

在 Skill 仓库运行：

```bash
python3 scripts/review_workbench.py serve \
  --title "我的项目 · Logo 评审" \
  --shape-manifest ./design/shape.json \
  --color-manifest ./design/color.json \
  --state ./design/review-state.json
```

打开命令显示的本机地址。先确认形态，再确认配色，最后单独确认定稿。更换上游选择会清除受影响的后续确认。候选文件更新后，还可核对保存的素材指纹。

## 让 Agent 更新进度

每次产出或修改一批候选后，Agent 追加一条进度消息：

```bash
python3 scripts/review_workbench.py note \
  --stage color \
  --message "已根据确认的形态补齐三个配色候选。"
```

保持页面打开，新记录会自动显示。切换端口时，`note` 用 `--url` 指明服务地址。重启服务时继续传入同一个状态文件，即可恢复记录。

服务只监听 `127.0.0.1`。设计资料、候选图和选择都在本机。想公开案例时，使用另行提供的社区投稿入口。
