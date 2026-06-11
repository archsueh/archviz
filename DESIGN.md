# DESIGN.md — archviz-skills Design System

Plain-text design system for all visualizations. Inspired by VoltAgent/awesome-design-md + Google Stitch DESIGN.md.

---

## Atmosphere

- **Restrained Swiss + Warm Paper**: Clean grids, generous whitespace, hairline as scalpel, structure over decoration
- **Anti-slop**: No purple gradients, no rainbow nodes, no centered symmetry, no flowchart-for-everything
- **Text-first, preview-compatible**: Primary output is .mmd that renders cleanly in Obsidian/GitHub/Typora. architecture-beta only for dedicated render pipelines
- **Data-first**: Make the "why" visible in structure, not decoration

---

## Tokens

**Color** (one system per diagram set, max 1 accent):

| System | surface | text | border | accent | Use |
|---|---|---|---|---|---|
| Warm Paper | #e8e4e0 | #f5f5f4 | #a8a29e | — | Default, academic |
| Swiss Neutral | #f5f5f4 | #1B365D | #d6d3d1 | — | Clean, print |
| IKB Accent | #e4e8f0 | #0a0a0a | #94a3b8 | #002FA7 | guizang Swiss |
| Lemon Accent | #f0f4e0 | #0a0a0a | #a8b898 | #FFD500 | Tech |
| Stone Mono | #e7e5e4 | #f5f5f4 | #a8a29e | — | Austerity |

**Contrast**: luminance(0.299R+0.587G+0.114B) < 128 → light text, ≥ 128 → dark text

**Typography** (越大越细，越小越粗):
- Large titles: weight 200 (ExtraLight), 15-16px
- Body: weight 300 (Light), 13-14px
- Small: weight 500-600 (SemiBold), 11-13px
- Chinese: ≤8 chars/line, consistent language per diagram

**Line & Shape**: 1px default, 2px accent. Sharp corners. No thick borders, no emoji, no gradients.

---

## Visualization Taxonomy

Based on Few's 7 relationships + Shneiderman's 6 data types + teaching/academic gaps:

| Category | Types | Anti-default | Template |
|---|---|---|---|
| Ranking/Comparison | Bar, Column, Radar (≤7), Bullet | ≤5 items → TABLE | `diverging-bar.mmd` |
| Temporal | Line, Area, Gantt, Calendar Heatmap | Gantt: codes+table+ASCII | `gantt.mmd` |
| Part-to-Whole | Stacked Bar, Treemap, Sunburst | **Avoid pie/donut** | `html/treemap.html` |
| Distribution | Histogram, Box Plot, Violin, Dot | — | `distribution.mmd` |
| Correlation | Scatter, Heatmap, Bubble, Network | — | `python/scatter-plot.py` |
| Hierarchical | Tree, Treemap, Circle Packing | — | — |
| Flow | Sankey, Chord, Flowchart | — | `sankey.mmd` |
| Funnel/Conversion | Funnel chart, Pipeline stages | Max 7 stages, label with % | `funnel.mmd` |
| Decision/Evaluation | Decision matrix, Weighted scorecard | Table-first, radar for ≤7 criteria | `decision-matrix.mmd` |
| State Transitions | State diagram, Lifecycle | Max 10 states, label transitions | `state-machine.mmd` |
| Dependencies | Dependency graph, Critical path | Cluster by layer, highlight blockers | `dependency-network.mmd` |
| Geospatial | Choropleth, Bubble Map | Use sparingly | — |

**Choosing by data shape** (quick heuristic):
- "Which is better?" → comparison (bar/radar/table)
- "How does it flow?" → sankey/flowchart
- "What converts/drops?" → funnel
- "What depends on what?" → dependency graph
- "What are the states?" → state diagram
- "How to decide?" → decision matrix + radar

---

## Layout Rules

**Dials** (baseline 4/3/8):
- COMPLEXITY 4: ≤25-50 nodes
- DENSITY 3: generous whitespace
- RESTRAINT 8: monochrome + one accent

**Preferred types** (compatibility first):
- System/layered → flowchart TD + subgraph (primary for .md source)
- Hierarchical → mindmap (strip `<br/>`, use `/` separators)
- Process → flowchart TD/LR
- Scoring → xychart-beta or mindmap
- Subgraphs max 4-5, labels ≤8 Chinese chars, non-symmetric

---

## Anti-Homogenization

- Never ship plain default without brief + dials + custom init
- One accent family, vary lightness not hue
- Make "why" visible (ritual edges, sovereign core)
- Match existing document palette

**Variation for recurring concepts**: Same concept in one document = different "shots" each time. Vary type (flowchart → mindmap → architecture), emphasis (ritual edges → core → zoom), perspective (full system → from ritual → from core). Serves content rhythm, not decoration.

---

## Shape Vocabulary

| Shape | Mermaid | ASCII |
|---|---|---|
| Process | `[]` | `┌─┐└─┘` |
| Important | `(( ))` | `╔═╗╚═╝` |
| Decision | `{}` | `╭─╮╰─╯` |
| Data | `[[]]` | `[artifact]` |
| Actor | `(( ))` | `o actor` |

**Arrow semantics**: solid=primary, dashed=secondary, labeled=explicit. Legend if >2 types.

---

## Signature Patterns (Aver domain)

- Core = .md 数据主权 (sovereign, strongest border)
- Three layers as groups: Money / Knowledge / Sentiment
- Ritual edges labeled explicitly (购入仪式, 卖出告别, etc.)
- Single IKB accent for core connections

---

## Validation

**Pre-gen**: Brief done? Dials set? Tokens locked? Labels short? Gantt: codes+table+ASCII?

**Post-gen**: Render test? No overlaps? Legend present? Matches document style?

**Error recovery**: Simplify → switch type → ASCII fallback. Never ship without validation.

---

See SKILL.md for execution workflow. See templates/ for concrete examples.
