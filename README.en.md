# logo-brand-designer

An AI agent skill for designing and reviewing brand marks, wordmarks, and derived app icons. It asks the agent to inspect existing brand assets, test distinctiveness, document color sources, and review actual renders before delivery.

[Website](https://webkubor.github.io/logo-brand-designer/en/) · [中文说明](README.md) · [Skill instructions](SKILL.md)

## Real projects

| Mark | Project | How it was designed |
|---|---|---|
| <img src="docs/assets/nativecrew.png" width="72" alt="NativeCrew mark"> | [NativeCrew](https://www.npmjs.com/package/@dsh-plugins/nativecrew), a DSH agent workbench | Layered orange color follows one silhouette. The transparent icon ships with the plugin. |
| <img src="docs/assets/museav-music-light.svg" width="96" alt="MuseAV Music mauve waveform mark"> | [MuseAV Music](https://www.museav.top/ecosystem), a music release workbench | A monochrome waveform came first, followed by a mauve palette. Light and dark SVGs are used in the workbench and tab icon. |

See the [CortexOS concept gallery](examples/cortexos/) for five exploratory designs. If you used the skill, [submit your project](https://github.com/webkubor/logo-brand-designer/issues/new?template=showcase.yml) to the [community showcase](https://webkubor.github.io/logo-brand-designer/showcase/).

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
