# logo-brand-designer

An AI agent skill for designing and reviewing brand marks, wordmarks, and derived app icons. It asks the agent to inspect existing brand assets, test distinctiveness, document color sources, and review actual renders before delivery.

[中文说明](README.md) · [Skill instructions](SKILL.md) · [Example](examples/cortexos/)

## Install

```bash
git clone https://github.com/webkubor/logo-brand-designer.git
cd logo-brand-designer
./install.sh
```

Run `./install.sh --list` to inspect destinations without installing. The installer supports several local agent skill directories; see the Chinese README for options.

## Use

Ask your agent: “Use logo-brand-designer to design a logo for this project. Inspect the existing brand assets and colors, show distinct directions with a mark and wordmark, and provide a review page and real screenshots.”

For an existing brand, ask for a derived icon and specify the host application. Check its actual rendering method, theme, background and size. The review manifest accepts an optional `iconAsset` to preview the icon at 16 and 24 pixels.

The review generator uses Python 3.9+ and the standard library. It checks asset structure; it does not establish visual quality, pixel transparency, or legibility. Verify those with real rendered screenshots and visual review.

MIT license.
