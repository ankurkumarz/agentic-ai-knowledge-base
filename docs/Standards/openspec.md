# OpenSpec

## Overview

**OpenSpec** is an open-source, lightweight framework for spec-driven development (SDD) with AI coding assistants, developed by Fission AI. Rather than keeping requirements in ephemeral chat history, OpenSpec introduces a structured specification layer so humans and AI align on requirements before implementation begins. The framework is designed to be fluid and iterative — not rigid or waterfall — and serves both brownfield and greenfield projects at any scale. As of April 2026, the project had 50.1k GitHub stars and is actively maintained under the MIT license.

*(Updated: the page previously described OpenSpec as "upcoming" and in "early development"; as of v1.3.1 it is a production-grade tool with a large community.)*

## Core Design Philosophy

Three foundational principles guide OpenSpec:

- **Agree before building** — specifications are written and reviewed before implementation starts, reducing back-and-forth corrections.
- **Stay organized** — every change proposal lives in a dedicated folder with consistent artifact structure, keeping context outside chat history.
- **Work fluidly** — any artifact can be updated at any time; there are no rigid phase gates between specification and implementation.

The philosophy is summarized by its maintainers as: *"fluid not rigid, iterative not waterfall, easy not complex, built for brownfield not just greenfield, scalable from personal projects to enterprises."*

## Artifact Structure

Each change proposal creates a dedicated directory containing four artifact types:

| Artifact | File | Purpose |
|---|---|---|
| Proposal | `proposal.md` | Rationale, scope, and overview of the change |
| Specifications | `specs/` directory | Requirements and scenario-driven acceptance criteria |
| Design | `design.md` | Technical approach and architectural decisions |
| Tasks | `tasks.md` | Numbered implementation checklist for the AI agent |

Completed proposals are moved to a timestamped archive folder via `/opsx:archive`, keeping the working directory clean.

## Primary Workflow: `/opsx` Commands

OpenSpec uses slash commands as its primary interface for artifact-guided development:

| Command | Action |
|---|---|
| `/opsx:propose <idea>` | Generates the full change folder (proposal, specs, design, tasks) |
| `/opsx:apply` | Executes all tasks systematically — component creation, styling, integration |
| `/opsx:archive` | Moves completed change to archive; updates specs for future iterations |
| `/opsx:new` | Starts a new change proposal |
| `/opsx:continue` | Resumes work on an existing proposal |
| `/opsx:ff` | Fast-forwards through multiple tasks |
| `/opsx:verify` | Validates implementation against the specification |
| `/opsx:bulk-archive` | Archives multiple completed changes at once |
| `/opsx:onboard` | Onboards an existing project into OpenSpec |

## Installation and Requirements

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

- **Node.js**: 20.19.0 or higher required
- **Package managers**: npm, pnpm, yarn, bun, and nix supported
- **Language**: TypeScript (99.1% of codebase)
- **Latest version**: v1.3.1 (April 21, 2026)
- **Update**: `openspec update` regenerates agent instructions and activates latest slash commands

**Telemetry**: Anonymous telemetry collects only command names and version numbers; automatically disabled in CI environments; opt out via `OPENSPEC_TELEMETRY=0`.

## Tool Integration

OpenSpec works with 25+ AI assistants and development tools, including Claude, GitHub Copilot, VS Code, Cursor, and others. This tool-agnosticism is a deliberate design choice — it does not lock users into a specific IDE or model vendor.

**Community schemas** extend the base framework: third-party opinionated workflow bundles are distributed as standalone repositories, allowing teams to share and version their own conventions on top of OpenSpec primitives.

## Comparison with Alternatives

| Dimension | OpenSpec | GitHub Spec Kit | AWS Kiro |
|---|---|---|---|
| Weight | Lightweight, minimal setup | Heavier, Python dependency | Proprietary IDE-centric |
| Phase gates | None — fluid updates throughout | Rigid phase structure | Structured to Kiro workflows |
| Tool scope | 25+ AI assistants, tool-agnostic | GitHub-native | Kiro IDE / AWS toolchain |
| Project type | Brownfield + greenfield | Primarily greenfield | AWS-integrated projects |
| Open source | MIT | N/A | Proprietary |
| Installation | `npm install -g` | Python setup | IDE plugin |

OpenSpec's primary differentiator is that it solves unpredictability when requirements live only in chat history, without imposing a heavyweight process. The Thoughtworks Technology Radar (Vol. 34) categorizes it as "New" and notes it "focuses on spec deltas rather than complete upfront specification — well-suited for brownfield systems."

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Model selection | Not all models handle spec generation equally | Use high-reasoning models; Claude Opus 4.7 and Codex 5.5 recommended |
| Context management | Long chat history degrades AI spec quality | Start with clean context windows before `/opsx:apply` |
| Architectural changes | Ad-hoc AI edits to architecture cause drift | Submit an OpenSpec proposal before implementing any architectural change |
| Brownfield adoption | Existing projects lack a specification baseline | Use `/opsx:onboard` to generate initial specs from the current codebase |
| Spec hygiene | Artifacts become stale if not maintained | Archive completed proposals; update specs on each iteration before re-proposing |

## Use Cases

- **Feature development**: Propose, specify, and implement discrete features with full artifact trail
- **Brownfield refactoring**: Onboard existing codebases and incrementally capture specs for change areas
- **API design**: Write specs for endpoints and let AI generate implementation against them
- **Multi-session work**: Artifacts persist across sessions, giving AI agents recoverable context
- **Team collaboration**: Shared spec folder in version control provides single source of truth for requirements

## See Also

- [Agentic AI Foundation](./agentic-ai-foundation.md)
- [AGENTS.md Standard](./agents-md.md)
- [Model Context Protocol](./mcp.md)
- [Agent2Agent (A2A) Protocol](./agent2agent.md)
- [AG-UI Protocol](./README.md)
- [AgentHarness Engineering](../AgentHarness/harness-engineering.md)
- [Context Engineering](../ContextEngineering/)
- [Production Best Practices: Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)

## References

- [Fission-AI/OpenSpec GitHub Repository](https://github.com/Fission-AI/OpenSpec) — official source, MIT license, v1.3.1
- [Thoughtworks Technology Radar Vol. 34](../AgenticTechStack/thoughtworks-radar-vol34.md) — categorized as "New"; assessment of OpenSpec vs. BMAD and Kiro
