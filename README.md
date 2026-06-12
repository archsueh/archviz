[git-push-release-workflow.html](https://github.com/user-attachments/files/28890337/git-push-release-workflow.html)# archviz-skills



Restrained information visualization skill pack for AI agents.

Every visualization starts with a **brief read** and **three dials** — not a default template.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-0.2.5-blue.svg)

---

## 截图素材 / Screenshot Material (v0.2.5)

<img width="1280" height="633" alt="building-structure" src="https://github.com/user-attachments/assets/fc457280-9304-4f63-9c7e-f7a7a9a6e145" />
<img width="1280" height="633" alt="teaching-building" src="https://github.com/user-attachments/assets/326091c3-d191-45a7-b8b9-2b770a7c9a24" />
<img width="1280" height="633" alt="teaching-building-exploded" src="https://github.com/user-attachments/assets/64a8f9a4-9f00-4b21-b7d0-612a9a742109" />
<img width="1280" height="633" alt="hair-dryer-exploded" src="https://github.com/user-attachments/assets/72212731-f70b-47c1-a8d7-5a59faea8d31" />
<img width="1280" height="633" alt="hair-dryer-assembled" src="https://github.com/user-attachments/assets/50c82da6-f839-4bf7-a14a-98fc245eb496" />
<img width="1280" height="633" alt="floorplan" src="https://github.com/user-attachments/assets/502034a9-ebef-4d91-a864-059475a353c2" />
<img width="1280" height="633" alt="building-structure" src="https://github.com/user-attachments/assets/c2e37374-dfb4-4f17-9e30-81c36988c000" />


[Uploadin<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Git Push 发布工作流 | archviz-skills v0.2.5</title>
  <style>
    :root {
      --surface: #d8b87c;
      --text: #1B365D;
      --accent: #f4a731;
      --border: #9eae4c;
      --light: #fbf1c7;
      --dark: #3c3836;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
      background: #f5f0eb;
      color: var(--text);
      margin: 0;
      padding: 40px 20px;
      line-height: 1.7;
    }
    .container {
      max-width: 1100px;
      margin: 0 auto;
      background: white;
      border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      overflow: hidden;
      border: 1px solid var(--border);
    }
    .header {
      background: var(--surface);
      color: var(--text);
      padding: 32px 48px;
      text-align: center;
      border-bottom: 4px solid var(--accent);
    }
    .header h1 {
      margin: 0 0 8px;
      font-size: 28px;
      font-weight: 600;
    }
    .header .version {
      font-size: 14px;
      opacity: 0.8;
      letter-spacing: 1px;
    }
    .content {
      padding: 48px;
    }
    .diagram {
      background: #f9f6f0;
      padding: 32px;
      border-radius: 8px;
      border: 1px solid var(--border);
      margin-bottom: 40px;
    }
    .diagram h2 {
      margin-top: 0;
      font-size: 18px;
      color: var(--text);
      border-bottom: 2px solid var(--accent);
      padding-bottom: 8px;
    }
    .mermaid {
      background: white;
      padding: 20px;
      border-radius: 6px;
    }
    .explanation {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      margin-bottom: 40px;
    }
    .step {
      background: #f9f6f0;
      padding: 24px;
      border-radius: 8px;
      border-left: 5px solid var(--accent);
    }
    .step h3 {
      margin: 0 0 12px;
      font-size: 16px;
      color: var(--accent);
    }
    .step p, .step li {
      font-size: 15px;
      color: var(--dark);
    }
    .table-container {
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 24px 0;
    }
    th, td {
      padding: 12px 16px;
      text-align: left;
      border-bottom: 1px solid var(--border);
    }
    th {
      background: var(--surface);
      color: var(--text);
      font-weight: 600;
    }
    .highlight {
      background: #fff8e7;
      font-family: monospace;
      padding: 2px 6px;
      border-radius: 3px;
    }
    .footer {
      background: #f5f0eb;
      padding: 24px 48px;
      font-size: 13px;
      color: #666;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .screenshot-tip {
      background: #e8f0e8;
      border: 1px solid var(--border);
      padding: 12px 16px;
      border-radius: 6px;
      font-size: 13px;
      color: var(--text);
    }
    @media (max-width: 800px) {
      .explanation { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="version">archviz-skills v0.2.5 • Darwin Self-Evolution</div>
      <h1>Git Push 发布工作流</h1>
      <p style="margin: 8px 0 0; opacity: 0.9;">图文并茂示例 • 使用 Wes Anderson (Moonrise Kingdom) 暖有机调色</p>
    </div>

    <div class="content">
      <div class="diagram">
        <h2>发布流程图（Wes Anderson Variant）</h2>
        <div class="mermaid">
flowchart TD
    subgraph 准备阶段["准备阶段 Prep"]
        V["validate_frontmatter<br/>+ check_files"]
        D["Dry-run 摘要<br/>用户 Enter 确认"]
    end

    subgraph Git操作["Git 操作 Git Operations"]
        GA["git add -A"]
        GC{"working tree 干净?"} 
        GT["git tag -f v0.2.5"]
        GP["git push origin main --tags<br/>★ 核心 git push 推送"]
    end

    subgraph 发布["GitHub 发布 Release"]
        GR["gh release create<br/>带安装 notes"]
        GV["打印验证与多代理安装指令"]
    end

    V --> D --> GA --> GC
    GC -->|需提交| GT
    GC -->|干净| GT
    GT --> GP --> GR --> GV

    classDef push fill:#d8b87c,stroke:#f4a731,stroke-width:3px,color:#1B365D
    class GP push
        </div>
      </div>

      <div class="explanation">
        <div class="step">
          <h3>1. 准备阶段</h3>
          <p>脚本执行严格 frontmatter 校验 + 文件检查，然后打印 dry-run 摘要并等待确认。这是 G0-G6 门控的体现。</p>
        </div>
        <div class="step">
          <h3>2. Git 操作（核心）</h3>
          <p><span class="highlight">git push origin main --tags</span> 是整个流程的<strong>决定性推送</strong>。它将本地 tag 与变更同步到 GitHub。没有这一步，release 无法完成。</p>
          <ul>
            <li>git add -A</li>
            <li>git commit（干净则跳过）</li>
            <li>git tag -f v0.2.5</li>
            <li><strong>git push ... --tags</strong></li>
          </ul>
        </div>
      </div>

      <div class="table-container">
        <h2 style="font-size:16px; margin-bottom:12px;">命令速查表</h2>
        <table>
          <tr><th>步骤</th><th>命令</th><th>说明</th></tr>
          <tr><td>推送</td><td><code>git push origin main --tags</code></td><td>★ 核心 git push，将 tag 推送到远程</td></tr>
          <tr><td>打标</td><td><code>git tag -f v0.2.5</code></td><td>强制创建/更新版本标签</td></tr>
          <tr><td>发布</td><td><code>gh release create v0.2.5 ...</code></td><td>创建 GitHub Release，附带安装说明</td></tr>
        </table>
      </div>

      <div style="background:#f9f6f0; padding:20px; border-radius:8px; border:1px solid var(--border);">
        <p><strong>与 0.2.5 自进化关联：</strong>本次 darwin 评估（97/100）后新增的 Version Bump Process 检查表，正是通过此 git push 流程发布的。所有变更使用绝对路径，符合 darwin-skill 要求。</p>
        <p style="margin-bottom:0;">完整发布脚本：<code>/Users/mac/Developer/archviz-skills/scripts/publish-skill.py</code></p>
      </div>
    </div>

    <div class="footer">
      <div>
        推荐截图方式：<span class="screenshot-tip">浏览器打开此 HTML → F11 全屏 → 使用系统截图工具（Cmd+Shift+4）或 CleanShot 捕获完整内容。推荐 16:9 或 2:1 比例。</span>
      </div>
      <div style="font-size:12px; opacity:0.7;">Wes Anderson palette • surface #d8b87c • accent #f4a731 • 60-30-10 克制设计</div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({ 
      startOnLoad: true,
      theme: 'base',
      flowchart: { curve: 'basis' }
    });
  </script>
</body>
</html>g git-push-release-workflow.html…]()

- 使用 Wes Anderson (Moonrise Kingdom) 暖有机配色（surface `#d8b87c` 暖米 + accent `#f4a731` 赤陶 + border `#9eae4c` 鼠尾草），完美契合 huashu 60-30-10 + 克制 editorial 风格。
- 嵌入完整发布流程图（git push 步骤 ★ 高亮）。
- 带丰富中文/英文图文说明：准备阶段、Git 操作核心、GitHub 发布 + 命令速查表。
- 页面底部自带截图提示（浏览器打开 → F11 全屏 → 系统截图工具捕获，推荐 16:9 或宽屏）。
- 自包含，无需依赖，打开即用。

**示例 PNG 截图**（从 Mermaid 渲染，已嵌入主页）：

![git push 发布流程图](docs/screenshots/git-push-release-workflow.png)

源文件（GitHub 直接渲染 Mermaid）：  
[examples/git-push-release-workflow.mmd](examples/git-push-release-workflow.mmd)

此示例同时用于演示本次 0.2.5 darwin 自进化后的发布流程（meta）。

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

### 0.1.6 Optimization References
This release incorporates patterns from the following projects (reviewed for draw.io handoff, Drawnix/Plait support, terminal rendering, skill composition, refinement loops, etc.):

- [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) — Generate draw.io diagrams from natural language (presets, vision self-check, refinement, codebase-to-diagram, exports)
- [plait-board/drawnix](https://github.com/plait-board/drawnix) — Open-source whiteboard tool with mind maps, flowcharts, freehand, Markdown/Mermaid support
- [markdown-viewer/skills](https://github.com/markdown-viewer/skills) — Opinionated agent skills for diagrams and visualizations in Markdown
- [fasouto/termaid](https://github.com/fasouto/termaid) — Render Mermaid diagrams as Unicode art in terminal (18 types, themes, Python API)
- [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) — Next.js web app integrating AI with draw.io diagrams (natural language create/modify)
- [Rss3208/Visiomaster](https://github.com/Rss3208/Visiomaster) — AI visualization and diagram generation patterns

See full optimization plan and details in [CHANGELOG.md](CHANGELOG.md) (0.1.6 section).

---

## License

MIT
