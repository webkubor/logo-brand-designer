#!/usr/bin/env python3
"""CortexOS logo 探索稿：标志 + 字标锁定组合，纯 SVG 生成。

用法：python3 examples/cortexos/build.py   （需要 rsvg-convert 渲染 PNG 预览）
输出：每个方案的 mark.svg / lockup-light.svg / lockup-dark.svg，以及 README 用的展板 PNG。
这些是 skill 的示例产出，不是 CortexOS 的定稿品牌。
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "Avenir Next, Helvetica Neue, Arial, sans-serif"
DEFS = '''<defs>
<linearGradient id="gA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4F46E5"/><stop offset="1" stop-color="#7C3AED"/></linearGradient>
<linearGradient id="gB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0EA5E9"/><stop offset="1" stop-color="#2563EB"/></linearGradient>
<linearGradient id="gHot" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5EEAD4"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
<linearGradient id="gV" x1="0" y1="20" x2="0" y2="180" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#7C3AED"/><stop offset="1" stop-color="#2563EB"/></linearGradient>
<clipPath id="cPar"><path d="M70 20 H130 L100 180 H40 Z"/></clipPath>
<clipPath id="cCirc"><circle cx="100" cy="100" r="80"/></clipPath>
</defs>'''

def bands():
    out = []
    for i in range(5):
        y = 20 + i * 32
        shift = -16 if i == 2 else 0
        fill = "url(#gHot)" if i == 2 else "url(#gV)"
        out.append(f'<g transform="translate({shift},0)"><rect x="0" y="{y}" width="200" height="26" fill="{fill}" clip-path="url(#cCirc)"/></g>')
    return "".join(out)

# 每个方案：(名称, 一句话想法, 标志 SVG 片段，坐标系 200x200)
MARKS = {
    "intersect": ("交汇", "两片平行斜面错位相叠，重叠处是人与 Agent 交汇出的控制空间。",
        '<path d="M70 20 H130 L100 180 H40 Z" fill="url(#gA)"/>'
        '<path d="M105 40 H165 L135 200 H75 Z" fill="url(#gB)"/>'
        '<path d="M105 40 H165 L135 200 H75 Z" fill="url(#gHot)" clip-path="url(#cPar)"/>'),
    "corner": ("切角", "完整的方块是组织空间，被切下的一角向外推出，是秩序里的一次突破。",
        '<path d="M22 38 H100 L162 100 V178 H22 Z" fill="url(#gA)"/>'
        '<path d="M120 18 H182 V80 Z" fill="url(#gHot)"/>'),
    "breakout": ("出框", "粗框围出一个空间，核心从开口处穿出去，掌控与越界同时成立。",
        '<path fill-rule="evenodd" fill="url(#gA)" d="M20 20 H180 V72 H152 V48 H48 V152 H152 V128 H180 V180 H20 Z"/>'
        '<rect x="100" y="78" width="80" height="44" rx="4" fill="url(#gHot)"/>'),
    "raster": ("光栅", "五道平行光栅组成一个整体，中间一道错位，秩序里只有一处被打破。",
        bands()),
    "ascend": ("跃迁", "两级方块排成秩序，第三块转成菱形跃起，表示从排列到突破。",
        '<rect x="14" y="128" width="46" height="46" rx="4" fill="url(#gB)"/>'
        '<rect x="72" y="100" width="46" height="46" rx="4" fill="url(#gA)"/>'
        '<rect x="132" y="38" width="46" height="46" rx="4" fill="url(#gHot)" transform="rotate(45 155 61)"/>'),
}

def mark_svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="CortexOS 标志">{DEFS}{body}</svg>'

def lockup_svg(body, dark):
    txt = "#F4F5F8" if dark else "#14151B"
    bg = '<rect width="820" height="220" rx="24" fill="#0B0C10"/>' if dark else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 220" width="820" height="220" role="img" aria-label="CortexOS">{DEFS}{bg}'
            f'<g transform="translate(14,10)">{body}</g>'
            f'<text x="240" y="142" font-family="{FONT}" font-weight="600" font-size="96" letter-spacing="-2" fill="{txt}">Cortex<tspan fill="url(#gA)">OS</tspan></text></svg>')

def inner(svg):
    return svg.split(">", 1)[1].rsplit("</svg>", 1)[0]

def render(path, width):
    subprocess.run(["rsvg-convert", "-w", str(width), path, "-o", path[:-4] + ".png"], check=True)

def main():
    rows = []
    for key, (name, idea, body) in MARKS.items():
        d = os.path.join(HERE, key); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "mark.svg"), "w").write(mark_svg(body))
        open(os.path.join(d, "lockup-light.svg"), "w").write(lockup_svg(body, False))
        open(os.path.join(d, "lockup-dark.svg"), "w").write(lockup_svg(body, True))
        rows.append((key, name, idea, body))
    # 展板：每行 浅底横版 | 深底横版 | 标志 64/32/16
    W, RH = 1960, 260
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{RH*len(rows)+40}" viewBox="0 0 {W} {RH*len(rows)+40}"><rect width="100%" height="100%" fill="#F3F4F7"/>']
    for i, (key, name, idea, body) in enumerate(rows):
        y = 20 + i * RH
        parts.append(f'<rect x="20" y="{y}" width="820" height="220" rx="24" fill="#FFFFFF"/>')
        parts.append(f'<svg x="20" y="{y}" width="820" height="220" viewBox="0 0 820 220">{inner(lockup_svg(body, False))}</svg>')
        parts.append(f'<svg x="860" y="{y}" width="820" height="220" viewBox="0 0 820 220">{inner(lockup_svg(body, True))}</svg>')
        for j, s in enumerate((96, 48, 24)):
            parts.append(f'<svg x="{1710 + [0, 110, 170][j]}" y="{y + 110 - s//2}" width="{s}" height="{s}" viewBox="0 0 200 200">{inner(mark_svg(body))}</svg>')
    parts.append("</svg>")
    gallery = os.path.join(HERE, "gallery.svg")
    open(gallery, "w").write("".join(parts)); render(gallery, 1960)
    # 封面：深底大图，单个方案（切角）居中
    hero = os.path.join(HERE, "hero.svg")
    body = MARKS["corner"][2]
    open(hero, "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="560" viewBox="0 0 1600 560">{DEFS}'
        f'<rect width="1600" height="560" fill="#0B0C10"/>'
        f'<svg x="390" y="170" width="820" height="220" viewBox="0 0 820 220">{inner(lockup_svg(body, True))}</svg>'
        f'<text x="800" y="470" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#8A8FA3">标志 + 字标 · 纯 SVG · 浅底深底与小尺寸实测</text></svg>')
    render(hero, 1600)
    for key in MARKS:
        render(os.path.join(HERE, key, "mark.svg"), 400)

if __name__ == "__main__":
    main()
