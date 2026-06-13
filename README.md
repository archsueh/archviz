# archviz

Restrained 2D information visualization skill pack for AI agents.

Every visualization starts with a **brief read** and **three dials** — not a default template.

> **3D spatial visualization** has been split into [archviz-3d](https://github.com/archsueh/archviz-3d).

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-0.3.0-blue.svg)

---
Neutrals
Warm Paper
#f5f0eb · default surface
Paper Beige
#e8e4e0 · 3D floor / legacy
Mist White
#f5f5f4 · Swiss surface
Stone Gray
#a8a29e · border / lines
Pebble
#d6d3d1 · tertiary fill
Ink Navy
#1B365D · primary text
Warm Ink
#44403c · secondary text
Charcoal
#292524 · Stone Mono text
Accents — one per diagram set, never both
International Klein Blue #002FA7
Lemon #FFD500
Contrast rule: luminance(0.299R+0.587G+0.114B) < 128 → light text, ≥ 128 → dark text. Light warm surfaces never take near-white text; Mist White text is legal only on accent or dark fills.

Palette systems
System	surface	text	border	accent	Use
Warm Paper	#f5f0eb	#1B365D	#a8a29e	—	Default, academic
Swiss Neutral	#f5f5f4	#1B365D	#d6d3d1	—	Clean, print
IKB Accent	#e4e8f0	#0a0a0a	#94a3b8	#002FA7	guizang Swiss
Lemon Accent	#f0f4e0	#0a0a0a	#a8b898	#FFD500	Tech
Stone Mono	#e7e5e4	#292524	#a8a29e	—	Austerity
Type scale — 越大越细，越小越粗
Role	Sample	Spec
Diagram title	三层闭环架构	15–16px · weight 200
Node label / body	陪伴证据 · evidence	13–14px · weight 300 · ≤8 汉字
Caption / legend	实线=主流程 · 虚线=反馈	11–13px · weight 500–600
Node vocabulary — shape is semantics
process
过程
[ ] · 1px stone
core
数据主权
(( )) · 2px accent — the one emphasis
decision
判定
{ } · 1px
artifact
.md
[[ ]] · pebble fill
actor
(( )) · 1px
Edge semantics
─────►  primary (solid)
- - -►  secondary (dashed)
═════►  emphasized (2px accent, max one)
──标注──►  labeled (explicit semantics)
Legend mandatory if >2 edge types appear. Max 4–5 subgraphs · 50 nodes hard cap · sharp corners · no emoji · no gradients · no pie.

archviz-skills · DESIGN.md visual catalog · Stitch DESIGN.md format · MIT
## Screenshot Material

<img width="1280" height="633" alt="hair-dryer-exploded" src="https://github.com/user-attachments/assets/9ed240f9-81bc-4ef5-8823-550f080b974c" />
<img width="1280" height="633" alt="hair-dryer-assembled" src="https://github.com/user-attachments/assets/9793fe6a-1832-442d-a1b7-20e2e1526c64" />

Open the complete screenshot sheet:
[examples/git-push-release-workflow.html](examples/git-push-release-workflow.html)

Self-contained HTML screenshot sheet with Wes Anderson palette, command table, and Mermaid source. Open in a browser, enter full screen, and capture the final visual.

Mermaid source:
[examples/git-push-release-workflow.mmd](examples/git-push-release-workflow.mmd)

---

## What this is

A skill for AI agents (Claude Code, Hermes, Codex, etc.) that generates **rational, minimalist, restrained visualizations**. Not just Mermaid — supports ASCII/termaid terminal rendering, self-contained HTML, Python (Plotly), Obsidian Canvas, draw.io handoff guidance, and Three.js 3D archviz.

## Design philosophy

`archviz-skills` treats every diagram as a small **DESIGN.md artifact**: a plain-text design contract that an agent can read, execute, and audit. The goal is not to make diagrams prettier by default; the goal is to make their visual language explicit enough that another agent can reproduce the same taste without guessing.

Every output should expose five things:

| Layer | What it answers | Required evidence |
|---|---|---|
| Atmosphere | What should this feel like? | Palette + density + restraint |
| Tokens | What exact values are allowed? | Hex values, line weights, type scale |
| Components | What recurring pieces exist? | Nodes, arrows, legends, labels |
| Layout | How does information collapse? | Direction, caps, fallbacks |
| Guardrails | What must never happen? | Anti-patterns + validation gates |

This is adapted from the `awesome-design-md` pattern: `DESIGN.md` is the visual truth source, `SKILL.md` is the execution protocol, and examples prove the contract works.

**Core principles:**
- Brief-first, anti-slop
- Text-first, preview-compatible
- One accent max, contrast-checked
- Environment-aware (Obsidian / terminal / deliverables / 3D)
- Editable-handoff aware (`.drawio` guidance when Mermaid is not enough)
- Design-contract first: no template ships without tokens, intent, constraints, and validation notes

**Mode routing:**
- **Default (2D infoviz)** — charts, flowcharts, gantt, sankey, tables, teaching diagrams
- **3D archviz** — only when the brief mentions building, floorplan, structure, section cut, or walkthrough (`templates/html/threejs-*.html`)
- **Editable handoff** — use draw.io mode when the user needs a diagram that can be edited by architects, teachers, or engineering teams after generation

---

## Quick start

```bash
git clone https://github.com/archsueh/archviz-skills.git
# Claude Code / Codex
cp -r archviz-skills ~/.claude/skills/
# Hermes Agent
cp -r archviz-skills ~/.hermes/skills/creative/archviz-skills
```

---

## Structure

```
archviz-skills/
├── SKILL.md              # Execution workflow + anti-patterns
├── DESIGN.md             # Design system, Stitch 9-section format (+ Extended: taxonomy, Aver, 3D)
├── preview.html          # Visual catalog: palettes, type scale, node/edge styles
├── README.md             # This file
├── CONTRIBUTING.md       # Contribution guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT
├── templates/
│   ├── mermaid/          # 15 .mmd templates
│   ├── ascii/            # 4 .txt templates
│   ├── html/             # 21 .html templates (incl. threejs-archviz)
│   ├── python/           # 5 .py templates
│   ├── canvas/           # 2 canvas handoff templates
│   ├── obsidian-canvas/  # 3 Obsidian Canvas templates
│   └── excalidraw/       # 1 Excalidraw template
├── examples/
│   ├── git-push-release-workflow.html  # **图文并茂截图素材**（Wes Anderson 配色，自包含 HTML，直接打开截图）
│   ├── git-push-release-workflow.mmd   # 图文并茂 git push 发布流程 (Wes Anderson variant)
│   ├── mermaid-demo.md                 # Mermaid bar + flow + gantt
│   ├── teaching-building-3d.html       # 4-floor building walkthrough
│   ├── course-admission-flow.mmd       # Teaching funnel
│   └── python-demo.py                  # Plotly scatter + line
└── references/           # Detailed rules (gantt, style, validation, draw.io, terminal routing)
```

---

## Templates

| Category | Count | Types |
|---|---|---|
| Mermaid | 15 | gantt, sankey, distribution, diverging-bar, network, architecture, scoring, intro, closed-loop, funnel, decision-matrix, state-machine, dependency-network |
| ASCII | 4 | flowchart, architecture, gantt, icon-system |
| HTML | 21 | bubble, bullet-graph, funnel, gauge, heatmap, line, radar, sunburst, treemap, waffle, waterfall, self-contained, threejs-archviz, threejs-floorplan, plus advanced chart templates |
| Python | 5 | scatter-plot, box-plot, candlestick, parallel-coordinates, viz template |
| Canvas | 6 | canvas, Obsidian Canvas, Excalidraw handoff templates |

---

## Design system

[DESIGN.md](DESIGN.md) follows the Stitch DESIGN.md 9-section format (per [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)):

1. Visual Theme & Atmosphere (+ Agent-Readable Contract)
2. Color Palette & Roles — semantic names + hex + role, 5 palette systems, luminance contrast gate
3. Typography Rules (越大越细 hierarchy)
4. Component Stylings — nodes, edges, groups, gantt, tables, Mermaid init
5. Layout Principles — three dials + whitespace philosophy
6. Depth & Elevation — flat by doctrine
7. Do's and Don'ts
8. Responsive Behavior + degradation strategy
9. Agent Prompt Guide — quick color reference + ready-to-use prompts

Extended sections: visualization taxonomy (Few + Shneiderman), Aver signature patterns, 3D archviz (Three.js + animejs), draw.io handoff rules, terminal routing, scene contracts, validation gates.

[preview.html](preview.html) is the visual catalog (swatches, type scale, node/edge vocabulary) — open it in a browser.

---

## Related

### Core dependencies
- [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) — Official Mermaid
- [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) — 10.3k stars
- [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) — Swiss PPT
- [anydesign](https://github.com/archsueh/anydesign) — Design analysis

---

## License

MIT
