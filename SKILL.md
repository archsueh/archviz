---
name: archviz-skills
description: |
  Restrained information visualization skill pack. Every visualization starts with a brief read and three dials.
  Supports Mermaid, ASCII, data charts, process diagrams, and information icons.
  Not limited to Mermaid. Text-first, preview-compatible, anti-slop.
version: 0.0.4
author: archsueh
license: MIT
triggers: |
  diagram, visualization, chart, gantt, sankey, mindmap, xychart, 可视化, 架构图, 流程图, 信息图, 甘特图
---

# archviz-skills

> Every rule is **contextual**. Read the brief first, then pull only what fits.

---

## QUICK REFERENCE (agent loads this in <5 seconds)

```
Dials:      COMPLEXITY=4  DENSITY=3  RESTRAINT=8
Palette:    surface=#e8e4e0  text=#f5f5f4  border=#a8a29e  accent=#002FA7 (max 1)
Init:       %%{init: {'theme':'base','themeVariables':{'primaryColor':'#e8e4e0','primaryTextColor':'#f5f5f4','primaryBorderColor':'#a8a29e','lineColor':'#a8a29e','tertiaryColor':'#d6d3d1','fontSize':'13px'}}}%%
Contrast:   luminance(0.299R+0.587G+0.114B) < 128 → light text, ≥ 128 → dark text
Labels:     ≤6 words / ≤8 Chinese chars / no ALL CAPS
Gantt:      codes only inside block + table beside + ASCII fallback / min 3w
Anti-slop:  no purple default / no rainbow / no flowchart-for-everything / no pie
```

**Type selection (fast):**
| Data | Type | Template |
|---|---|---|
| Hierarchical | mindmap | — |
| Sequential | flowchart LR/TD | — |
| System/layered | flowchart TD + subgraph | — |
| Comparison/ranking | xychart-beta (bar) | — |
| Proportional | treemap or stacked bar | — |
| Timeline | gantt | `mermaid/gantt.mmd` |
| Distribution | histogram/box | `mermaid/distribution.mmd` |
| Correlation | scatter/heatmap | `python/scatter-plot.py` |
| Flow/network | sankey | `mermaid/sankey.mmd` |
| Funnel/conversion | funnel chart | `html/funnel.html` |
| Decision/evaluation | decision matrix (table) | `mermaid/decision-matrix.mmd` |
| State transitions | stateDiagram-v2 | `mermaid/state-machine.mmd` |
| Dependencies | dependency graph | `mermaid/dependency-network.mmd` |
| Multi-criteria scoring | radar or diverging bar | `html/radar.html` / `mermaid/diverging-bar.mmd` |
| Simple (≤5 items) | **TABLE, not chart** | — |

**Mixed types** (when data spans categories):
- Process + timeline → flowchart with gantt sub-section (split into 2 diagrams)
- Hierarchy + comparison → mindmap with leaf annotations (table beside)
- Flow + metrics → sankey with tooltip/badge annotations
- Decision + scoring → decision matrix → radar for top candidates
- **Rule: never combine >2 types in one diagram. Split instead.**

**Degradation strategy** (when data is too complex):
1. >50 nodes → split into 2-3 linked diagrams with shared legend
2. >7 categories → aggregate into "Other" + detail diagram
3. Mixed data types → identify primary relationship, table the rest
4. Preview environment fails → ASCII fallback (always prepared)
5. Mermaid syntax error → flowchart TD + subgraph (most compatible)

**Environment routing:**
| Env | Output |
|---|---|
| Obsidian/preview | lightweight Mermaid / ASCII / self-contained HTML |
| Terminal | pure ASCII (pyfiglet, boxes) |
| Deliverables | Python (Plotly/Matplotlib) |

Full rules → DESIGN.md. Templates → templates/.

---

## 0. BRIEF INFERENCE

Before generating, read these signals:

1. **Context** — paper, design log, PPT, product doc, personal note
2. **Content type** — hierarchical, sequential, relational, quantitative, temporal
3. **Audience** — reviewers, clients, dev team, self
4. **Vibe** — "restrained", "clean", "academic", "playful"
5. **Existing style** — match palette/font/layout already established
6. **Constraints** — accessibility, print, projection, dark mode
7. **Environment** — Obsidian, terminal, deliverables

Output one line: **"Reading this as: \<type> for \<audience>, \<vibe>, \<palette>."**

**4-layer analysis** (from anydesign): Identity → System → Components → Layout. Mark confidence: ✅/⚠️/❓.

**Anti-default:** No purple gradients, no rainbow nodes, no centered symmetry, no flowchart-for-everything, no default theme.

---

## 1. THREE DIALS

| Dial | Default | Range |
|---|---|---|
| COMPLEXITY | 4 | 1(minimal)–10(dense) |
| DENSITY | 3 | 1(airy)–10(packed) |
| RESTRAINT | 8 | 1(expressive)–10(austere) |

Inference: "academic" → 3-5/2-3/9-10 · "playful" → 5-8/3-5/3-5 · "data report" → 6-8/6-8/5-7

---

## 2. TOKENS

Defined in DESIGN.md. Summary:

| Token | Warm Paper | Swiss | IKB |
|---|---|---|---|
| surface | #e8e4e0 | #f5f5f4 | #e4e8f0 |
| text | #f5f5f4 | #1B365D | #0a0a0a |
| border | #a8a29e | #d6d3d1 | #94a3b8 |
| accent | — | — | #002FA7 |

**Rules:** Max 1 accent. No AI-purple. Same doc = same palette. Contrast check mandatory.

---

## 3. TYPOGRAPHY

越大越细，越小越粗：Large=200(ExtraLight) · Body=300(Light) · Small=500-600(SemiBold)

Labels: ≤6 words · ≤8 Chinese chars · no ALL CAPS · same language per diagram

---

## 4. LAYOUT

- Mindmap: auto-layout
- Flowchart: LR for processes, TD for hierarchies
- Max 4-5 subgraphs, short noun labels
- Non-symmetric unless content demands it
- Hard cap: 50 nodes → split

---

## 5. CONTENT DENSITY

| Data | Format |
|---|---|
| 2-3 items | Table |
| 4-8 items | Bar chart |
| Proportional | Treemap/stacked |
| Sequential | Flowchart |
| Hierarchical | Mindmap |
| Timeline | Gantt |

Simple comparison (≤5 items) → TABLE, not chart.

---

## 6. SHAPE CONSISTENCY

- Border radius: sharp (0) by default. Never mix.
- Line weight: 1px default, 2px accent. No 3px+.
- Icons: sparingly (1 per group max). No emoji.

---

## 7. QUALITY RULES

**Do:** Cite hex/px · Infer semantic roles · Mark confidence (✅/⚠️/❓) · Match document style

**Don't:** Generic descriptions · Colors without hex · Invent tokens · Ignore context

---

## 8. OUTPUT TEMPLATE

```yaml
---
diagram: [name]
type: [mindmap|flowchart|xychart-beta|gantt|...]
context: [paper|log|PPT|note]
dials: {complexity: N, density: N, restraint: N}
tokens: {surface: "#e8e4e0", text: "#f5f5f4", border: "#a8a29e", accent: "#002FA7"}
confidence: {palette: "✅", layout: "✅", nodes: "⚠️"}
---
```

---

## 9. WORKFLOW

1. Brief + 4-layer analysis (§0)
2. Set dials (§1)
3. Choose type + environment (§2 + QR table)
4. Apply tokens (DESIGN.md)
5. Apply typography (§3)
6. Apply layout (§4)
7. Check density (§5)
8. Quality audit (§7)
9. Generate code
10. Validate (render test or alignment check)
11. Embed (caption first = finding)

**Pre-gen checklist:** Brief done? Dials set? Tokens locked? Labels short? Gantt: codes+table+ASCII?

---

## 10. GANTT (hard rules)

- Inside gantt block: ultra-short codes only (V1.1, A1, B3)
- Full names: mandatory table immediately after
- ASCII fallback: always include
- Min bar: 3w. Merge short tasks.
- Section: 3-6 tasks. Group by phase.

---

## 11. ASCII MODE

Box-drawing chars in monospace. Max 80 columns.

| Shape | Char |
|---|---|
| Regular node | `┌─┐└─┘` |
| Important | `╔═╗╚═╝` |
| Decision | `╭─╮╰─╯` |
| Primary flow | `─────►` |
| Secondary | `- - -►` |
| Emphasized | `═════►` |

Tools: `pyfiglet` (headers), `boxes` (borders), `cowsay` (annotations)

---

## 12. TEMPLATES

Actual files live in `templates/`. Current inventory (do not hardcode counts in prompts):

```
templates/
├── mermaid/    11 files (flowchart, mindmap, gantt, sankey, scoring, network, distribution, diverging-bar, intro, architecture, closed-loop variants)
├── ascii/       4 files (flowchart, architecture, gantt, icon-system)
├── html/       12 files (bubble, bullet-graph, funnel, gauge, heatmap, line, radar, sunburst, treemap, waffle, waterfall, self-contained)
└── python/      5 files (scatter-plot, box-plot, candlestick, parallel-coordinates, viz template)
```

Prefer reading the specific template file under `templates/<mode>/` at use time instead of relying on this list.
---

## 13. TROUBLESHOOTING

| Issue | Fix |
|---|---|
| Mindmap fails | Use flowchart/subgraph |
| Architecture-beta lexer error | Use flowchart TD + subgraph (preview-compatible) |
| Gantt text overflow | Codes only + table + ASCII fallback |
| Theme too flashy | Force solarized-light/nord-light |
| Text unreadable | Check contrast rule (QR) |
| Too many nodes | Split into subgraphs |

---

## 14. RESOURCES

- [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) — Official
- [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) — 10.3k stars
- [mermaid-rs-renderer](https://github.com/1jehuang/mermaid-rs-renderer) — Fast Rust
- [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) — Swiss PPT
- [anydesign](https://github.com/archsueh/anydesign) — Design analysis

Full design system → DESIGN.md · Detailed rules → references/ · Research → research/
