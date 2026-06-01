# Pi (pi.dev)

## Overview

Pi is a minimal, open-source terminal coding agent harness built around a single design thesis: a coding agent needs exactly four tools — read, write, edit, bash — and a system prompt under 1,000 tokens. Everything else is opt-in via a typed TypeScript extension system.

Created by Mario Zechner (the author of libGDX), Pi is published as an MIT-licensed monorepo at [earendil-works/pi](https://github.com/earendil-works/pi). It ships as the coding-agent harness you can reshape: where commercial tools bake in features, Pi ships a minimal core and exposes every dimension — tools, context management, skills, themes, and UI — as replaceable components.

Pi's design directly instantiates the [Agent = Model + Harness](./agent-harness.md) equation: the four-tool core is the harness substrate, and the extension system is how teams rebuild the harness around their workflow rather than adapting their workflow to the tool.

## Core Architecture

### Four Built-in Tools

Pi's complete built-in tool surface:

| Tool | Description |
|---|---|
| `read` | Read file contents from the working directory |
| `write` | Create new files |
| `edit` | Modify existing files (targeted edits, not full rewrites) |
| `bash` | Execute shell commands |

This four-tool core is derived from an observation about frontier model behavior: models already understand the coding agent task without extensive scaffolding. A sub-1,000-token system prompt paired with four tools is sufficient to achieve capable coding behavior; additional tools and prompts are situational and opt-in.

### Deliberate Omissions

Pi explicitly omits several features common in other coding agents. Each omission is a design decision, not a gap:

| Feature | Pi's Position | Extension Path |
|---|---|---|
| MCP support | Not built-in; CLI tools work via READMEs | Build MCP integration via extensions |
| Sub-agents | Not built-in | Available via extensions or third-party Pi packages |
| Permission popups | Not built-in; Pi prefers container isolation | Build custom approval flows via extensions |
| Plan mode | Not built-in | File-based plans or custom extension |
| To-do tracking | Not built-in | Files or custom extension |
| Background bash | Not built-in; `tmux` recommended for observability | — |

This philosophy avoids the feature bloat that degrades context management and legibility in heavier tools. Users build exactly what their workflow needs, nothing more.

## Component Packages

Pi is a TypeScript monorepo with six packages:

| Package | Role |
|---|---|
| `@mariozechner/pi-ai` | Unified multi-provider LLM API (Anthropic, OpenAI, Google, Azure, Bedrock, etc.) |
| `@mariozechner/pi-agent-core` | Runtime engine: tool calling, state management, session lifecycle |
| `@mariozechner/pi-coding-agent` | Interactive coding agent CLI — the primary user-facing product |
| `@mariozechner/pi-tui` | Terminal UI library with differential rendering |
| `@mariozechner/pi-web-ui` | Web components for AI chat interfaces |
| `@mariozechner/pi-pods` | CLI for managing vLLM deployments on GPU pods |

A Slack integration (`pi-mom`) delegates messages to the coding agent, enabling conversational coding workflows over Slack.

## Customization Framework

Pi's extensibility model has four layers that can be bundled into shareable Pi Packages:

### Extensions

TypeScript modules with full system access. Extensions can:
- Add custom tools
- Register commands and keyboard shortcuts
- Handle events and inject UI components
- Inject messages before each turn (feedforward context)
- Filter message history (context management)
- Implement RAG or custom retrieval
- Build long-term memory
- Add sub-agent spawning, permission gates, SSH execution, MCP integration, or custom editors

Extensions cover the full harness surface — any capability another tool ships built-in can be reproduced as a Pi extension.

### Skills

Reusable agent capabilities following the Agent Skills standard. Skills are invoked via `/skill:name` — either manually by the user or automatically by the agent based on context. They implement the progressive disclosure pattern: capability definitions are loaded on demand rather than injected into every turn.

### Prompt Templates

Reusable Markdown-based prompts stored locally and expanded via `/templatename` syntax. Templates support `{{variable}}` interpolation for parameterized workflows.

### Themes

Visual customization with hot-reloading capability. Built-in options include `dark` and `light`; custom themes are supported.

### Pi Packages

Extensions, skills, prompts, and themes bundled together and distributed via npm or git. Installation supports pinned versions and HTTPS sources:

```
pi install @myorg/pi-package
pi install git+https://github.com/user/pi-package#v1.2.0
```

## Multi-Provider Support

Pi is provider-agnostic and bring-your-own-key. The same agent loop runs against any supported provider with no code changes:

- **Subscription-based**: Anthropic Claude Pro/Max, OpenAI ChatGPT Plus/Pro, GitHub Copilot
- **API key providers**: Anthropic, OpenAI, Azure OpenAI, Google Gemini, Vertex AI, Amazon Bedrock, DeepSeek, Groq, Cerebras, Mistral, xAI, OpenRouter, Vercel AI Gateway, Cloudflare, and others including Chinese-market platforms
- **Local models**: Ollama and compatible local inference servers

Users switch providers via `/model` or `Ctrl+L` mid-session.

## Session Management

Sessions are stored as JSONL files with a tree structure that enables in-place branching without file duplication. Sessions auto-save to `~/.pi/agent/sessions/` organized by working directory.

| Feature | Description |
|---|---|
| **Branching** | `/tree` navigates the session tree; jump to any previous point and continue from there |
| **Forking** | Create a new session from any previous user message |
| **Cloning** | Duplicate an active branch into a new session file |
| **Compaction** | Automatic or manual summarization of older messages when approaching context limits; fully customizable via extensions |

## Context and Project Integration

Pi loads context from `AGENTS.md` and `CLAUDE.md` files in both global (`~/.pi/`) and project-local (`.pi/`) directories. Project-specific instructions and conventions are injected at session start — the same mechanism documented in [Context Engineering Strategies](../ContextEngineering/strategies.md).

Configuration lives in `~/.pi/agent/settings.json` (global) or `.pi/settings.json` (project-scoped).

## Programmatic Integration

Pi supports four operating modes beyond interactive use:

| Mode | Use Case |
|---|---|
| Interactive (default) | Developer-facing terminal agent |
| Print / JSON | Scripted invocations with structured output |
| RPC | Process integration via strict LF-delimited JSONL over stdin/stdout |
| SDK | Embed agent sessions directly in Node.js applications |

```typescript
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});
```

## Supply Chain Security

Pi applies supply chain security practices uncommon in open-source agent tooling:

- Pinned exact versions for all external dependencies
- Lockfile verification and controlled lifecycle scripts
- Shrinkwrap generation for reproducible installs
- Automated security audits via CI workflows

## Comparison with Other Coding Agent Harnesses

| Dimension | Pi | Claude Code | Flue | OpenCode |
|---|---|---|---|---|
| Core tools | 4 (read, write, edit, bash) | 40+ | Filesystem + shell + grep + glob | 6 (read, write, edit, bash, browser, search) |
| System prompt size | < 1,000 tokens | ~55,000 tokens | Configurable | ~15,000 tokens |
| Extensibility | TypeScript extensions + packages | Hooks + MCP | TypeScript + skills | Plugins |
| MCP support | Via extension | Native | Native | Native |
| Sub-agents | Via extension | Native | Via tasks | Native |
| LLM providers | 15+ (bring-your-own-key) | Claude only (Anthropic) | Multi-provider | 75+ |
| Backend | None (zero SaaS) | Anthropic cloud | Optional | None |
| License | MIT | Proprietary | Apache-2.0 | MIT |
| Primary language | TypeScript | TypeScript | TypeScript | TypeScript / Rust |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Starting with too many extensions | Defeating Pi's minimal-core thesis from the start | Begin with the four-tool core; add extensions only when a specific gap is identified through use |
| Context rot in long sessions | Performance degrading as session history grows | Configure compaction via extension; set explicit session length limits |
| Provider lock-in | Workflows built around a single model's quirks | Test against two or more providers before hardening a Pi workflow |
| Missing MCP capabilities | Need protocol-standard tool connectivity | Implement MCP integration as a Pi extension; community packages exist for common MCP servers |
| No built-in permission gates | Autonomous actions without human checkpoints | Deploy in a container and build a custom approval extension for side-effecting tools |
| Skill discovery | Users don't know which skills are available | Maintain a project-level AGENTS.md that documents installed skills and their invocation syntax |
| Package version drift | Pi packages pinned to old versions | Use `pi update` regularly; pin to semantic version ranges rather than latest |

## See Also

- [Agent Harness](./agent-harness.md) — foundational harness concepts; Pi directly implements the Agent = Model + Harness equation
- [Harness Engineering](./harness-engineering.md) — feedforward/feedback control model; Pi's extension system maps to both guide and sensor categories
- [Flue](../AgenticFrameworks/flue.md) — TypeScript harness framework; complementary to Pi (framework-builder vs. terminal agent)
- [AI Coding Agents](../AgenticFrameworks/ai-coding-agents.md) — comparative landscape including Pi in context
- [Standards: Agent Skills](../Standards/skills.md) — the Agent Skills standard that Pi's skill system follows
- [Context Engineering Strategies](../ContextEngineering/strategies.md) — context injection patterns; Pi's AGENTS.md loading and compaction align with these
- [Production Best Practices: Security](../ProductionBestPractices/security.md) — Pi's zero-backend model and supply-chain practices align with least-privilege recommendations

## References

- [Pi Coding Agent — pi.dev](https://pi.dev/) — official product site
- [GitHub: earendil-works/pi (pi-mono)](https://github.com/earendil-works/pi) — MIT-licensed source repository; 225+ releases as of mid-2026
- [npm: @mariozechner/pi-coding-agent](https://www.npmjs.com/package/@mariozechner/pi-coding-agent) — published package with installation instructions
- [GitHub: can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) — community-built Pi extension with hash-anchored edits, LSP, browser, and sub-agent support
- [Pi Coding Agent — Product Hunt](https://www.producthunt.com/products/pi-coding-agent-3) — launch listing: "the coding-agent harness you can make your own"
- [Building Pi: A Minimal, Extensible Coding Agent Framework — ZenML LLMOps Database](https://www.zenml.io/llmops-database/building-pi-a-minimal-extensible-coding-agent-framework) — design rationale and architecture overview
