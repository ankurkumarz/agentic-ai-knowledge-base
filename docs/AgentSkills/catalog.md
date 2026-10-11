---
type: Reference
title: Agent Skills Catalog
description: A curated catalog of open-source agent skills and skill-adjacent tools installable into Claude Code, Codex, Cursor, Gemini CLI, and compatible harnesses.
tags: [agent-skills, skills-catalog, agentic-ai]
timestamp: 2026-10-10T00:00:00Z
---

# Agent Skills Catalog

## Overview

This catalog tracks open-source agent skills and skill-adjacent repositories that extend AI coding agents (Claude Code, Codex, Cursor, Gemini CLI, and compatible harnesses) with reusable, on-demand workflows. Skills are installed into a project or user-global scope and invoked via slash commands or by referencing the SKILL.md directly in agent context.

For the underlying standard and authoring format, see [Agent Skills / SKILLS.md](../Standards/skills.md).

---

## Catalog

### diagram-design
**Repository:** [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

An editorial diagram skill that renders diagrams as self-contained HTML + SVG files. Covers 44 diagram types — architecture diagrams, sequence diagrams, quadrant charts, flow diagrams, and more — without shadows, Mermaid, or external dependencies. Each diagram is a single `.html` file openable by double-clicking.

| Attribute | Detail |
|---|---|
| Install | `npx skills add cathrynlavery/diagram-design` |
| Claude Code | `/plugin marketplace add cathrynlavery/diagram-design` |
| Codex | `codex plugin marketplace add cathrynlavery/diagram-design` |
| Output format | Self-contained HTML + SVG (no external dependencies) |
| Diagram types | 44, including architecture, sequence, quadrant, flow |
| Branding | Brand palette and fonts via a one-time onboard command |
| Publisher | LittleMight (Cathryn Lavery) |

**Key capabilities:**
- Accepts plain-language instructions: "Give me a sequence of a bearer call with token refresh on 401"
- Supports brand onboarding: `Onboard diagram-design to https://yoursite.com` pulls the site's palette and fonts
- Auto-update supported via Claude Code marketplace; cross-agent symlink structure supports Cursor, Gemini CLI, Windsurf, Amp, and Warp
- Official builds only from this repository; third-party re-listings are unofficial copies

---

### brag
**Repository:** [latent-spaces/brag](https://github.com/latent-spaces/brag)

A skill that turns a finished project into a short, shareable launch video — music, motion, and share copy — with one command. `/brag` authors the story angle and hands a composition brief to [Hyperframes](https://hyperframes.dev) for rendering. Output is a `brag-output/` folder containing the plan, brief, share copy, and `brag.mp4`.

| Attribute | Detail |
|---|---|
| Install (cross-agent) | `npx skills add https://github.com/latent-spaces/brag --skill brag` |
| Claude Code | `/plugin marketplace add latent-spaces/brag` → `/plugin install brag@brag` |
| Codex | `codex plugin marketplace add latent-spaces/brag` |
| No-install variant | [letsbrag.app](https://letsbrag.app) — paste a URL, get a video |
| Runtime dependencies | Node.js 22+, FFmpeg, Hyperframes CLI (`npx hyperframes`) |
| Slim variant | `/brag-slim` — single-file skill for Opus 5.5 (no Hyperframes required) |

**Key capabilities:**
- Tone steering: `/brag --tone "fake Series A launch from 2016"`
- Optional voiceover via Kokoro through Hyperframes: `/brag --voice`
- On Opus 5.5, `/brag` auto-switches to `/brag-slim`; pass `--full` to keep the Hyperframes workflow
- Cross-agent symlink structure auto-detected by Google Antigravity, opencode, and Codex CLI

---

### openrig
**Repository:** [mvschwarz/openrig](https://github.com/mvschwarz/openrig)

An open-source system for building and running persistent networks of AI coding agents. OpenRig wraps individual agent harnesses (Claude Code, Codex) into a YAML-defined team with roles, shared context, and owned work. A lead agent coordinates specialists across teams and surfaces decisions requiring human attention.

| Attribute | Detail |
|---|---|
| Install | `npm install -g @openrig/cli` then `rig setup` |
| Current version | v0.6.8 |
| Supported harnesses | Claude Code, OpenAI Codex (same rig, managed together) |
| Runtime requirements | Node.js 22 or 24, tmux, macOS or Linux (WSL2 on Windows) |
| Persistence model | Agents maintain roles, shared context, and work state across sessions |
| State storage | SQLite |

**Key capabilities:**
- Define the full agent team in YAML; boot with one command
- Claude Code and Codex operate in the same rig as a unified system
- Per-seat permission policies; lifecycle commands (`rig up`, `rig down`) prompt for confirmation
- Lead agent can coordinate specialists and bring decisions to the user
- `rig doctor` for runtime diagnostics

**Relationship to skills:** OpenRig is a harness-level tool rather than a single SKILL.md skill. It extends the harness layer by managing a *team* of harnesses. Relevant to the [Agent Harness](../AgentHarness/agent-harness.md) and [Harness Engineering](../AgentHarness/harness-engineering.md) sections.

---

### Agent-Reach
**Repository:** [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

A skill that equips AI agents with internet access across a broad range of platforms and content types — Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu (Little Red Book), RSS, LinkedIn, and more — using a zero-API-fee, multi-backend routing architecture. Each platform has a primary and fallback backend; when one access path is blocked, the skill switches to the next without user intervention.

| Attribute | Detail |
|---|---|
| Install | Tell your agent: `帮我安装 Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md` |
| Update | Tell your agent: `帮我更新 Agent Reach: ...docs/update.md` |
| Compatible agents | Claude Code, OpenClaw, Cursor, Windsurf, and any CLI-capable agent |
| Cost | Fully free; optional server proxy ~$1/month for server deployments |
| Diagnostics | `agent-reach doctor` — checks which paths are live and how to fix failures |
| Privacy | Cookies stored locally only; fully open source |

**Platform coverage (selected):**

| Platform | Zero-config | With setup |
|---|---|---|
| Web pages | Any URL | — |
| YouTube | Subtitle extraction + search | — |
| RSS/Atom | Any feed | — |
| GitHub | Public repos + search | Private repos, issues, PRs |
| Twitter/X | Single tweets | Search, timeline, long-form |
| Reddit | — | Search, posts, comments |
| Bilibili | Search + video details | Subtitles (OpenCLI) |
| XiaoHongShu | — | Search + read (OpenCLI or Cookie-Editor) |
| LinkedIn | Public pages (Jina Reader) | Profiles, company pages, job search |

**Key capabilities:**
- Multi-backend routing: if yt-dlp is blocked by Bilibili's risk controls, the skill auto-switches to bili-cli (as of June 2026)
- Self-configuring: the agent guides setup step by step when told "帮我配 XXX"
- `agent-reach install --system` flag gates any system-level changes behind explicit user approval

---

### caveman
**Repository:** [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)

A token compression skill and proxy for AI coding agents. Caveman instructs the agent to respond in controlled, minimal English — answer first, one idea per sentence, no filler — while leaving code, paths, error messages, and numbers byte-for-byte intact. The proxy mode reduces input tokens across whole sessions; the skill mode affects only agent outputs.

| Attribute | Detail |
|---|---|
| Install (proxy + skill) | `npm install -g @caveman-ai/cli && caveman setup --install` |
| Supports | Claude Code, Codex, Gemini, Aider, Kilo, Qwen, Opencode, Hermes, OpenClaw, Pi |
| Input token reduction (proxy) | 33.2% fewer input tokens across whole sessions (54-run study, 18/18 correct) |
| Web page size reduction | 129.8× smaller pages for agent browsing vs. Playwright snapshots |
| Output cost reduction | 1.4–2.4× cheaper (Adobe Research, 8 models, 5 datasets) |
| Cited by | Adobe Research (CAVEWOMAN paper), JetBrains (86-task A/B, p=0.82, no quality loss), Elastic (Elasticsearch Labs) |

**Skill variants:**

| Command | Token count (example) | Description |
|---|---|---|
| `/caveman` | ~20 tokens | Standard caveman voice |
| `/ultracave` | ~14 tokens | More compressed |
| `/megacave` | ~13 tokens | Maximum compression (cross-lingual) |

**Key design rules:**
- Answer first, one idea per sentence (based on ASD-STE100 controlled English, ≤20 words/sentence)
- Negations (`not`, `never`, `no`, `only`), numbers, and units are never dropped
- Code, commands, paths, error messages, and existing comments are reproduced verbatim
- Security warnings, irreversible actions, and confused users always get full sentences
- Agent prompts from the user are never rewritten (Adobe Research found this backfires)

---

### andrej-karpathy-skills
**Repository:** [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

A single `CLAUDE.md` file encoding four coding-agent behavior principles derived from Andrej Karpathy's public observations about LLM coding pitfalls. The file is designed to be merged with project-specific `CLAUDE.md` instructions or installed as a Claude Code plugin.

| Attribute | Detail |
|---|---|
| Install (Claude Code plugin) | `/plugin marketplace add forrestchang/andrej-karpathy-skills` → `/plugin install andrej-karpathy-skills@karpathy-skills` |
| Install (per-project CLAUDE.md) | `curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md` |
| Cursor | `.cursor/rules/karpathy-guidelines.mdc` included in repo |
| License | MIT |

**The four principles:**

| Principle | Problem addressed | Core rule |
|---|---|---|
| Think Before Coding | Wrong assumptions, hidden confusion | State assumptions explicitly; ask rather than guess; present multiple interpretations; push back when warranted |
| Simplicity First | Overcomplication, bloated abstractions | Minimum code that solves the problem; no speculative features, no unrequested abstractions; if 200 lines could be 50, rewrite it |
| Surgical Changes | Orthogonal edits, touching unrelated code | Touch only what the request requires; don't refactor adjacent code; mention (don't delete) pre-existing dead code |
| Goal-Driven Execution | Vague success criteria requiring constant clarification | Transform imperative tasks into verifiable goals with explicit success criteria; loop until verified |

**Key insight (Karpathy):** "LLMs are exceptionally good at looping until they meet specific goals. Don't tell it what to do, give it success criteria and watch it go."

---

## Comparison Summary

| Skill / Repo | Category | Primary Benefit | Install method | Harness scope |
|---|---|---|---|---|
| [diagram-design](https://github.com/cathrynlavery/diagram-design) | Diagram generation | 44 diagram types, self-contained HTML+SVG | `npx skills add` / marketplace | Claude Code, Codex, Cursor, Gemini CLI, Windsurf, Amp |
| [brag](https://github.com/latent-spaces/brag) | Video generation | One-command project launch video | `npx skills add` / marketplace | Claude Code, Codex, opencode, Google Antigravity |
| [openrig](https://github.com/mvschwarz/openrig) | Multi-agent harness | Persistent YAML-defined agent teams | `npm install -g @openrig/cli` | Claude Code + Codex (joint) |
| [Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Internet access | Multi-platform browsing (zero API fees) | Agent-driven install via URL | Claude Code, OpenClaw, Cursor, Windsurf |
| [caveman](https://github.com/juliusbrussee/caveman) | Token compression | 33%+ fewer input tokens, same answers | `npm install -g @caveman-ai/cli` | Claude Code, Codex, Gemini, Aider, Kilo, and more |
| [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Agent behavior | 4 principles reducing costly LLM coding mistakes | `CLAUDE.md` append / marketplace | Claude Code, Cursor |

---

## See Also

- [Agent Skills / SKILLS.md Standard](../Standards/skills.md)
- [Agent Harness](../AgentHarness/agent-harness.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)
- [AI Coding Agents Overview](../AICodingAgents/ai-coding-agents.md)
- [Claude Code](../AICodingAgents/claude-code.md)
- [SkillOpt — Automated Skill Document Optimization](../PromptEngineering/skillopt.md)
- [AI Agent Skill Security Scanners](../SecurityFrameworks/skill-scanners.md)
- [Context Engineering — Anthropic](../ContextEngineering/anthropic.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md)

## References

- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — Editorial diagram design skill for Claude Code, Codex, Copilot, Cursor, and compatible harnesses; 44 diagram types as self-contained HTML+SVG
- [latent-spaces/brag](https://github.com/latent-spaces/brag) — Agent skill that turns a finished project into a launch video with music, motion, and share copy
- [mvschwarz/openrig](https://github.com/mvschwarz/openrig) — Open-source system for building persistent multi-agent networks from Claude Code and Codex harnesses
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — Multi-platform internet-access skill with zero API fees and multi-backend fallback routing
- [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman) — Token compression skill and proxy; 33.2% fewer input tokens across whole sessions, cited by Adobe Research and JetBrains
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — CLAUDE.md encoding four LLM coding-behavior principles derived from Andrej Karpathy's observations
