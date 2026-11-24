"""本地 Logo 评审服务。复用 manifest，并把进度和设计确认写入同一个状态文件。"""

import argparse
import fcntl
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from build_review import load_manifest


STAGES = ("shape", "color", "final")
UI = Path(__file__).with_suffix(".html")


class Review:
    """管理一个设计任务、候选清单和可追溯的选择。"""

    def __init__(self, state, shape, color, title):
        self.path = state
        self.title = title
        self.manifests = {"shape": shape, "color": color}
        self.lock = Lock()
        self.state = json.loads(state.read_text()) if state.exists() else {
            "revision": 0, "decisions": {}, "events": [],
        }

    def candidates(self):
        options = {}
        errors = {}
        for stage, manifest in self.manifests.items():
            options[stage] = []
            if manifest is None or not manifest.exists():
                continue
            try:
                projects = load_manifest(manifest)["projects"]
                for item in projects:
                    light = item["assets"]["asset"]
                    dark = item["assets"]["darkAsset"] or light
                    evidence = light["sha256"] + dark["sha256"]
                    options[stage].append({
                        "id": item["id"], "name": item["name"],
                        "sha": hashlib.sha256(evidence.encode()).hexdigest(),
                        "light": light["dataUri"], "dark": dark["dataUri"],
                        "rationale": " ".join(item["rationale"]),
                    })
            except (KeyError, ValueError, OSError) as exc:
                errors[stage] = "候选清单暂不可读。检查 manifest 和素材后刷新。"
                print(f"{stage}: {exc}", flush=True)
        return options, errors

    def record(self, payload, decision=False):
        stage = payload.get("stage")
        if stage not in STAGES:
            raise ValueError("未知评审阶段。")
        message = payload.get("message", "")
        if not isinstance(message, str) or len(message) > 500:
            raise ValueError("记录需要在 500 字以内。")
        event = {
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "kind": "decision" if decision else "note", "stage": stage,
            "message": message.strip(),
        }
        with self.lock:
            state = self.state
            choices = dict(state["decisions"])
            if decision:
                if payload.get("revision") != state["revision"]:
                    raise ValueError("进度已变化。刷新页面后再确认。")
                options, _ = self.candidates()
                previous = {step: next((item for item in options[step]
                                        if item["id"] == choices.get(step, {}).get("id")
                                        and item["sha"] == choices.get(step, {}).get("sha")), None)
                            for step in ("shape", "color")}
                if stage in ("color", "final") and previous["shape"] is None:
                    raise ValueError("先确认当前版本的形态。")
                if stage == "final":
                    selected = previous["color"]
                else:
                    selected = next((item for item in options[stage]
                                     if item["id"] == payload.get("candidate")
                                     and item["sha"] == payload.get("sha")), None)
                if selected is None:
                    raise ValueError("候选素材已更新。刷新评审后再确认。")
                if stage == "final" and not all(
                    selected[tone].startswith("data:image/svg+xml;") for tone in ("light", "dark")
                ):
                    raise ValueError("请先提供浅底和深底所用的 SVG，再确认定稿。")
                choice = {key: selected[key] for key in ("id", "name", "sha")}
                if choices.get(stage) != choice:
                    for downstream in STAGES[STAGES.index(stage) + 1:]:
                        choices.pop(downstream, None)
                choices[stage] = choice
                event["choice"] = choice
            elif not event["message"]:
                raise ValueError("填写要记录的进度。")
            new_state = {
                "revision": state["revision"] + 1, "decisions": choices,
                "events": [*state["events"], event],
            }
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=self.path.parent,
                                             prefix=".logo-review-", delete=False) as handle:
                pending = Path(handle.name)
                try:
                    json.dump(new_state, handle, ensure_ascii=False, indent=2)
                    handle.flush()
                    os.fsync(handle.fileno())
                    os.replace(pending, self.path)
                finally:
                    pending.unlink(missing_ok=True)
            self.state = new_state


class Handler(BaseHTTPRequestHandler):
    """只开放同源页面、评审候选和两种记录入口。"""

    def send(self, body, code=200, mime="application/json"):
        if isinstance(body, dict):
            body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", f"{mime}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; img-src data:; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def valid_host(self):
        return self.headers.get("Host") == f"127.0.0.1:{self.server.server_port}"

    def do_GET(self):
        if not self.valid_host():
            return self.send({"error": "请使用服务显示的本机地址。"}, 403)
        review = self.server.review
        if self.path == "/":
            return self.send(UI.read_bytes(), mime="text/html")
        if self.path == "/api/state":
            return self.send({"title": review.title, **review.state})
        if self.path == "/api/options":
            options, errors = review.candidates()
            return self.send({"options": options, "errors": errors})
        self.send({"error": "页面不存在。"}, 404)

    def do_POST(self):
        origin = self.headers.get("Origin")
        if not self.valid_host() or (origin and origin != f"http://{self.headers['Host']}"):
            return self.send({"error": "只接受本机同源请求。"}, 403)
        if self.path not in ("/api/note", "/api/decisions"):
            return self.send({"error": "页面不存在。"}, 404)
        decision = self.path == "/api/decisions"
        if self.headers.get_content_type() != "application/json" or (decision and not origin):
            return self.send({"error": "请求格式不受支持。"}, 415)
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 4096:
                raise ValueError("记录过长或为空。")
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict):
                raise ValueError("记录格式有误。")
            self.server.review.record(payload, decision)
        except (ValueError, OSError) as exc:
            return self.send({"error": str(exc)}, 400)
        self.send({"ok": True})


def main():
    """启动本地评审页面，或追加一条供页面自动刷新的进度。"""
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest="mode", required=True)
    server = modes.add_parser("serve")
    server.add_argument("--state", required=True, type=Path)
    server.add_argument("--shape-manifest", type=Path)
    server.add_argument("--color-manifest", type=Path)
    server.add_argument("--title", default="Logo 评审")
    server.add_argument("--port", type=int, default=8765)
    note = modes.add_parser("note")
    note.add_argument("--url", default="http://127.0.0.1:8765")
    note.add_argument("--stage", choices=STAGES, required=True)
    note.add_argument("--message", required=True)
    args = parser.parse_args()
    if args.mode == "note":
        url = urlsplit(args.url)
        if url.scheme != "http" or url.hostname != "127.0.0.1" or url.username or url.path not in ("", "/"):
            parser.error("--url 只接受本机评审地址。")
        data = json.dumps({"stage": args.stage, "message": args.message}).encode()
        request = Request(args.url.rstrip("/") + "/api/note", data=data,
                          headers={"Content-Type": "application/json"})
        try:
            with urlopen(request, timeout=5):
                print("进度已记入评审。")
        except HTTPError as exc:
            parser.exit(1, json.load(exc)["error"] + "\n")
        except URLError:
            parser.exit(1, "本机评审服务未连接。\n")
        return
    state = args.state.resolve()
    state.parent.mkdir(parents=True, exist_ok=True)
    with state.with_suffix(state.suffix + ".lock").open("a") as guard:
        try:
            fcntl.flock(guard, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.exit(1, "该评审已有服务在运行。\n")
        with ThreadingHTTPServer(("127.0.0.1", args.port), Handler) as service:
            service.review = Review(state, args.shape_manifest, args.color_manifest, args.title)
            print(f"http://127.0.0.1:{service.server_port}/", flush=True)
            try:
                service.serve_forever()
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
