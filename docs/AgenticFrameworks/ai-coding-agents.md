# AI Coding Agents

## Overview

AI coding agents are purpose-built autonomous tools that read codebases, plan changes, execute them using real development tools (terminal, editor, browser), and iterate on the results. Unlike general agentic frameworks (LangChain, CrewAI, etc.) which are libraries for building agents, these products are fully-assembled agents aimed at software engineers — accelerating coding tasks from bug fixes to full feature implementation.

The category spans terminal-first CLIs, IDE extensions, cloud sandboxes, and standalone IDE products. As of mid-2026 the field is crowded, with strong open-source contenders alongside proprietary cloud offerings.

---

## Comparison Table

| Tool | Vendor | Interface | License | LLM Support | Notable Differentiator |
|---|---|---|---|---|---|
| **Claude Code** | Anthropic | CLI + IDE + web | Proprietary | Claude (Anthropic) | Deepest agentic loop; swarm & daemon support; MCP-native |
| **OpenAI Codex** | OpenAI | Cloud / Desktop / Web | Proprietary | GPT-5.4+ (OpenAI) | Cloud sandbox; parallel tasks; computer-use model |
| **Gemini CLI** | Google | Terminal CLI | Apache 2.0 | Gemini (multi-provider) | Open-source; Google Search grounding; free tier |
| **Kiro** | Amazon / AWS | Agentic IDE | Proprietary | Claude (Bedrock) + Amazon Nova | Spec-driven development; agent hooks; AWS-native |
| **Devin** | Cognition | Cloud + Desktop | Proprietary (SaaS) | Proprietary model | Fully autonomous end-to-end engineer; $20/month |
| **Cline** | Cline (open source) | VS Code extension / CLI | Apache 2.0 | 30+ providers | HITL approval per action; largest VS Code install base |
| **Goose** | Block (Square) | Desktop + CLI | Apache 2.0 | 15+ providers | Donated to Linux Foundation; Rust-based; 70+ MCP extensions |
| **OpenCode** | OpenCode (open source) | Terminal TUI / Desktop / IDE | MIT | 75+ providers | Plan/Build mode; LSP diagnostics; 147K GitHub stars |
| **Pi** | earendil.works | Terminal CLI | MIT | 15+ providers | Radical minimalism: 4 tools, sub-1K-token system prompt |

---

## Claude Code

**Type**: Agentic coding system (CLI + IDE + web)
**Vendor**: Anthropic
**Docs**: [code.claude.com](https://code.claude.com)

Anthropic's flagship coding agent. Claude Code operates at the project level — reading the full codebase, planning changes across multiple files, executing them, running tests, and iterating on failures. As of May 2026, the majority of code at Anthropic is written by Claude Code, with engineers focusing on architecture and orchestrating multiple agents in parallel.

### Architecture (revealed by source leak, April 2026)

A source map shipped accidentally with npm package v2.1.88 exposed 512,000 lines of TypeScript across 1,900 files. Key architectural details:

- **Query Engine** (46,000 lines): The kernel scheduler handling all LLM API calls, streaming, caching, and orchestration.
- **Tool system**: 40+ discrete capabilities, each implemented as a separate module with its own permission gate.
- **Sub-agent spawning**: Claude Code can spawn sub-agents with restricted toolsets, each in an isolated context — enabling agent swarms.
- **KAIROS**: An autonomous daemon mode referenced 150+ times in the source; enables scheduled background tasks independent of user sessions.
- **44 feature flags**: Many capabilities were behind flags not yet publicly released at the time of the leak.
- **18+ hook types**: Including pre-session injection and post-compaction hooks that reinsert agent identity after context compression.

### Key Capabilities (Code with Claude 2026)

- **Multi-agent orchestration**: Manager agent delegates to parallel worker agents.
- **Dreaming**: Scheduled process reviews agent sessions and memory stores, extracts patterns, curates long-term memory so agents improve over time.
- **Outcomes**: A grading agent scores and re-runs tasks autonomously.
- **Context Infrastructure**: 1M-token window, flat pricing, server-side compaction, per-turn context editing.
- **MCP-native**: Integrates with any service that exposes an MCP server (databases, internal APIs, monitoring, documentation).
- **Webhooks**: Agents can subscribe to and respond to external events.

### Autonomy Level

Roughly Level 3–4 (analogous to autonomous driving): operates without human intervention under specific conditions, with supervision at key decision points. Task horizon expanded from minutes (early 2025) to hours (late 2025) to continuous operation (2026).

| Dimension | Signal |
|---|---|
| License | Proprietary |
| LLM | Claude (Anthropic) |
| Open source | No (source partially revealed by accident) |
| MCP support | Yes (native) |
| Sub-agent / swarm | Yes |
| Production readiness | GA |

---

## OpenAI Codex

**Type**: Cloud coding agent (web + desktop + API)
**Vendor**: OpenAI
**Docs**: [openai.com/codex](https://openai.com/codex)

Launched April 2025, Codex is OpenAI's agentic coding platform. Unlike CLI tools, it operates in isolated cloud sandboxes preloaded with the user's repository, with internet access disabled during task execution to enforce security boundaries. Tasks run in parallel across projects.

### Key Features

- **Cloud sandbox**: Each task runs in a secure, isolated container preloaded with the target repository.
- **Parallel execution**: Multiple agents can work on separate tasks simultaneously, compressing weeks of work.
- **Skills**: Codex goes beyond writing code — it understands the codebase, produces documentation, and aligns with team standards.
- **Automations**: Codex works unprompted on routine tasks: issue triage, alert monitoring, CI/CD pipeline maintenance.
- **Computer use (GPT-5.4)**: The underlying model has native computer-use capabilities, enabling complex multi-application workflows.
- **Codex Security**: Application-security agent that identifies and proposes fixes for vulnerabilities (launched March 2026).
- **In-app browser + SSH**: Agents can browse, connect to remote dev boxes, and interact with external systems.
- **Windows support**: Desktop app available on Windows as of March 2026.
- **90+ plugins**: Extended via a plugin ecosystem.

| Dimension | Signal |
|---|---|
| License | Proprietary (SaaS) |
| LLM | GPT-5.4+ (OpenAI) |
| Open source | No |
| Sandbox | Cloud-isolated container |
| Production readiness | GA |

---

## Gemini CLI

**Type**: Terminal coding agent (open-source CLI)
**Vendor**: Google
**GitHub**: [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — Apache 2.0
**Language**: TypeScript (Node.js)

Open-source terminal agent that brings Gemini models directly into command-line workflows. Built in TypeScript (98% of codebase). The free tier provides 60 requests/min and 1,000 requests/day via OAuth, making it accessible without API billing.

### Key Features

- **Google Search grounding**: Built-in real-time web search to augment code-related queries with current information.
- **Multimodal input**: Supports PDFs, images, and sketches alongside text.
- **GEMINI.md**: Project-specific context files (analogous to CLAUDE.md / AGENTS.md) for per-project agent behavior.
- **MCP support**: Custom integrations via the Model Context Protocol.
- **Conversation checkpointing**: Save and resume sessions across invocations.
- **Token caching**: Optimization for long sessions.
- **GitHub integration**: Automated PR review and issue triage via GitHub Actions.
- **Non-interactive mode**: JSON output for scripting and CI pipelines.
- **Vertex AI integration**: Enterprise access with higher rate limits via Google Cloud.

### Pricing

| Auth method | Rate limit | Cost |
|---|---|---|
| OAuth (free) | 60 req/min, 1K req/day | Free |
| API key | 1K req/day | Free (within Gemini free tier) |
| Vertex AI | Higher limits | Usage-based |

| Dimension | Signal |
|---|---|
| License | Apache 2.0 |
| LLM | Gemini (multi-provider via API) |
| Open source | Yes |
| MCP support | Yes |
| Production readiness | GA |

---

## Kiro

**Type**: Agentic IDE
**Vendor**: Amazon / AWS
**Docs**: [kiro.dev](https://kiro.dev)

AWS's agentic IDE, launched mid-2025. Kiro's defining characteristic is **spec-driven development** — natural-language specifications are the source of truth, and code is a build artifact generated, verified, and kept in sync by agents running on Amazon Bedrock. It routes between Claude Sonnet for reasoning-heavy specs and Amazon Nova for high-throughput code generation.

### Key Features

- **Spec-driven development**: Write a spec in natural language; agents generate, verify, and maintain the code. Specs are versioned, reviewed, and owned like code.
- **Agent Hooks**: Event-driven hooks fire on file save, PR open, and repo events — automatically running tests, updating documentation, regenerating fixtures, or cascading spec changes.
- **Multi-model routing**: Claude Sonnet for complex reasoning; Amazon Nova for throughput-intensive code generation. Unified via Bedrock.
- **Persistent context**: Context is maintained across sessions, enabling tasks that run autonomously for hours or days.
- **Multimodal input**: Processes files, codebases, docs, images, repo maps, git diffs, terminal output, URLs, and external docs via MCP.
- **Broad language support**: Python, Java, JavaScript, TypeScript, C#, Go, Rust, PHP, Ruby, Kotlin, C, C++, shell, SQL, Scala, JSON, YAML, HCL.
- **AGENTS.md / KIRO.md**: Project-specific agent instructions for per-project behavior.
- **MCP support**: External integrations via Model Context Protocol.

| Dimension | Signal |
|---|---|
| License | Proprietary (AWS) |
| LLM | Claude Sonnet + Amazon Nova (via Bedrock) |
| Open source | No |
| Spec-driven | Yes (unique differentiator) |
| Production readiness | GA |

---

## Devin

**Type**: Autonomous AI software engineer (cloud SaaS + desktop)
**Vendor**: Cognition AI
**Docs**: [devin.ai](https://devin.ai)

Devin is the most autonomous end-to-end coding agent in the category. Unlike assistant-style tools that require approval at each step, Devin takes a Jira ticket, bug report, or feature request and manages the full engineering lifecycle: planning, coding, testing, debugging, and proposing the pull request.

### Key Features

- **Sandboxed environment**: Operates inside a secure environment with a terminal, code editor, and browser — enabling API documentation lookup, StackOverflow searches, and shell execution.
- **Dynamic re-planning**: When blocked, Devin alters its strategy without human intervention (v3.0, 2026).
- **Autonomous error recovery**: When code fails compilation or tests, Devin reads error logs and iterates to a fix.
- **Desktop computer use (v2.2, Feb 2026)**: Full Linux desktop with the ability to launch, interact with, and test desktop applications.
- **Legacy code migration**: Ingests massive legacy codebases (COBOL, Fortran, Objective-C) and refactors into modern languages.
- **Code Review (Devin Review)**: First-pass code review catching logic errors, missing edge cases, and style violations before human reviewers.
- **Enterprise adoption**: Goldman Sachs piloted Devin across its 12,000-person engineering team (July 2025).
- **Valuation**: Cognition in talks to raise at a $25B valuation (April 2026).

### Pricing (as of 2026)

| Plan | Price | Notes |
|---|---|---|
| Core | $20/month | Entry tier (reduced from $500/month in April 2025) |
| Higher tiers | Variable | More parallelism and advanced features |

| Dimension | Signal |
|---|---|
| License | Proprietary (SaaS) |
| LLM | Proprietary model |
| Open source | No |
| Autonomy | Highest in category (minimal HITL) |
| Production readiness | GA |

---

## Cline

**Type**: VS Code extension + CLI + SDK (open source)
**Vendor**: Cline (VC-backed open source)
**GitHub**: [cline/cline](https://github.com/cline/cline) — Apache 2.0
**Installs**: 5M+ (VS Code Marketplace + Open VSX), 61K+ GitHub stars

Cline is the most-installed open-source AI coding agent in VS Code. It reads the codebase, creates and edits files, runs terminal commands, and drives a real browser via Puppeteer — with human-in-the-loop approval at each step.

### Key Features

- **Plan/Act mode**: In Plan mode, Cline explores the codebase and asks clarifying questions. Switch to Act mode to execute with per-action approval.
- **HITL by default**: Every file edit and terminal command requires approval — a deliberate design choice for safety.
- **30+ LLM providers**: Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, OpenRouter, DeepSeek, xAI Grok, Mistral, local models via Ollama/LM Studio, and more.
- **MCP Marketplace**: Plugin ecosystem for databases, observability, and internal tools.
- **Cline SDK**: Powers Cline across VS Code, JetBrains, and CLI interfaces.
- **Enterprise (Cline Teams, July 2025)**: SSO, RBAC, centralized billing, usage dashboards, audit logs, self-hosted/VPC deployment.
- **Browser automation**: Real browser control via Puppeteer for web-facing tasks.

| Dimension | Signal |
|---|---|
| License | Apache 2.0 |
| LLM | 30+ providers |
| Open source | Yes |
| Primary interface | VS Code extension |
| HITL | Yes (mandatory) |
| Production readiness | GA (enterprise tier available) |

---

## Goose

**Type**: Open-source AI agent (desktop + CLI + API)
**Vendor**: Block (Square/Cash App) — donated to Linux Foundation
**GitHub**: [block/goose](https://github.com/block/goose) — Apache 2.0
**Language**: Rust
**Stars**: 44.7K+

Originally developed as an internal tool at Block, Goose was open-sourced in 2025 and donated to the **Linux Foundation's Agentic AI Foundation** in December 2025, alongside Anthropic's MCP and OpenAI's AGENTS.md. It is not exclusively a coding agent — it handles research, writing, automation, data analysis, and any multi-step workflow.

### Key Features

- **15+ LLM providers**: Anthropic, OpenAI, Google Gemini, local models via Ollama, and others.
- **70+ MCP extensions**: Databases, APIs, browsers, GitHub, Google Drive, and more — all via the Model Context Protocol open standard.
- **Rust-based**: Performance and portability advantages over Python/Node alternatives.
- **Zero cost option**: Run with local models via Ollama at no cost; pay cloud provider API fees if using hosted models — Goose itself charges nothing.
- **Desktop app + CLI + API**: Multiple interfaces for different workflows.
- **Not coding-only**: General-purpose agent capable of research, writing, automation, and data analysis in addition to coding.
- **Foundation-backed**: Governance and long-term sustainability via the Linux Foundation's Agentic AI Foundation.

| Dimension | Signal |
|---|---|
| License | Apache 2.0 |
| LLM | 15+ providers (local + cloud) |
| Open source | Yes (Linux Foundation) |
| Language | Rust |
| MCP extensions | 70+ |
| Production readiness | GA |

---

## OpenCode

**Type**: Open-source terminal coding agent (TUI + Desktop + IDE)
**Vendor**: OpenCode (community open source)
**GitHub**: [opencode-ai/opencode](https://github.com/opencode-ai/opencode) — MIT
**Stars**: 147K GitHub stars, 6.5M monthly developers (April 2026)

OpenCode is one of the fastest-growing open-source projects in recent history. A GitHub Copilot partnership (January 2026) lets all paid Copilot subscribers authenticate directly into OpenCode, significantly expanding its user base.

### Key Features

- **Plan/Build mode**: The agent drafts what it intends to do before touching any files; you review and provide feedback before switching to Build mode to execute. Reduces unwanted changes.
- **LSP integration**: Built-in Language Server Protocol support gives the agent access to real compiler diagnostics — errors and fix suggestions are grounded in actual compiler output rather than model hallucination.
- **75+ providers**: OpenAI, Anthropic Claude, Google Gemini, local LLMs via Ollama, and many others. Switch models without restarting.
- **Terminal TUI**: First-class terminal UI for power users.
- **Desktop app + IDE extension**: Available across all major developer interfaces.
- **GitHub Copilot integration**: Direct authentication for Copilot subscribers (January 2026).

| Dimension | Signal |
|---|---|
| License | MIT |
| LLM | 75+ providers |
| Open source | Yes |
| Primary interface | Terminal TUI |
| LSP diagnostics | Yes (unique differentiator) |
| Production readiness | GA |

---

## Pi

**Type**: Minimal terminal coding agent (CLI)
**Vendor**: earendil.works (created by Mario Zechner, of libGDX)
**GitHub**: [earendil-works/pi](https://github.com/earendil-works/pi) — MIT

Pi's thesis is radical minimalism: a coding agent needs exactly four tools (read, write, edit, bash) and a system prompt under 1,000 tokens. Everything else is opt-in via a typed extension system. This makes it the most composable and privacy-friendly option in the category.

### Key Features

- **4-tool core**: read, write, edit, bash — derived from the observation that frontier models already understand what a coding agent is without extensive scaffolding.
- **15+ LLM providers**: Anthropic, OpenAI, Google Gemini, Ollama, and others. Switch models mid-session with a simple command.
- **Zero SaaS backend**: Runs entirely in the terminal with no cloud backend. Data handling is delegated entirely to the model provider you choose (Azure OpenAI, AWS Bedrock, Ollama, etc.).
- **Extensibility**: Customizable via extensions, skills, prompt templates, and themes. Bundle and share as Pi packages via npm or git.
- **Project context**: Auto-loads from `AGENTS.md` and `SYSTEM.md` files in the project root.
- **Compaction**: Customizable context compaction that summarizes older messages to prevent performance degradation in long sessions.
- **Enterprise compliance**: No SaaS backend means no data leaves the model provider of your choosing — avoids compliance obstacles when using Azure OpenAI or AWS Bedrock with private endpoints.

| Dimension | Signal |
|---|---|
| License | MIT |
| LLM | 15+ providers (no lock-in) |
| Open source | Yes |
| Backend | None (zero SaaS) |
| System prompt | < 1,000 tokens |
| Production readiness | GA |

---

## Positioning Map

These tools occupy distinct positions across two axes: **interface** (terminal ↔ full IDE) and **autonomy** (HITL-first ↔ fully autonomous).

```
                   HIGH AUTONOMY
                        │
          Devin ────────┤
                        │
   OpenAI Codex ────────┤
                        │
     Claude Code ───────┤
                        │
          Kiro ─────────┤──────────────── IDE
TERMINAL ───────────────┼──────────────────────
     Gemini CLI ─────────┤
                        │
        OpenCode ────────┤
                        │
           Goose ────────┤
                        │
            Cline ───────┤ (HITL-first)
                        │
              Pi ────────┤
                        │
                  LOW AUTONOMY (HITL)
```

---

## Best Practices

| Use Case | Recommended Tool(s) |
|---|---|
| Maximum autonomy, minimal supervision | Devin, Claude Code (KAIROS mode) |
| Cloud-isolated task parallelism | OpenAI Codex |
| Open source, self-hosted, compliance-sensitive | Pi, OpenCode, Cline, Goose |
| AWS ecosystem, spec-driven workflows | Kiro |
| VS Code integration with strong HITL | Cline |
| Free tier with Google Search grounding | Gemini CLI |
| General-purpose agent (not just coding) | Goose |
| Multi-provider flexibility, LSP diagnostics | OpenCode |

---

## See Also

- [Agent Development Frameworks Overview](README.md)
- [Frameworks Technology Radar](solutions.md)
- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md)
- [Context Engineering](../ContextEngineering/strategies.md)
- [ProductionBestPractices — Deployment](../ProductionBestPractices/deployment.md)
- [AllThingsAnthropic](../AllThingsAnthropic/README.md)
- [AllThingsOpenAI](../AllThingsOpenAI/README.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)
- [AllThingsAWS](../AllThingsAWS/README.md)

## References

- [Claude Code product page](https://www.anthropic.com/product/claude-code) — Anthropic's agentic coding system
- [The New Stack: Claude Code source leak](https://thenewstack.io/claude-code-source-leak/) — 512K lines of TypeScript accidentally exposed via npm source map; reveals swarms, KAIROS daemon, 44 feature flags
- [OpenAI Codex](https://openai.com/codex/) — OpenAI's cloud coding agent
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli) — Google's open-source terminal AI agent
- [Kiro](https://kiro.dev/) — Amazon's spec-driven agentic IDE
- [Devin](https://devin.ai/) — Cognition's autonomous AI software engineer
- [Cline GitHub](https://github.com/cline/cline) — Open-source VS Code coding agent
- [Goose GitHub](https://github.com/block/goose) — Block's open-source AI agent (Linux Foundation)
- [OpenCode](https://opencode.ai/) — Open-source terminal coding agent; 147K GitHub stars
- [Pi GitHub](https://github.com/earendil-works/pi) — Minimal 4-tool terminal coding harness
- [InfoQ: Claude Code source leak](https://www.infoq.com/news/2026/04/claude-code-source-leak/) — Packaging error exposed source map in npm v2.1.88
