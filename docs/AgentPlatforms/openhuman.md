# OpenHuman (TinyHumans AI)

## Overview

OpenHuman is an open-source (GPL-3.0) desktop personal AI agent developed by TinyHumans AI, launched in beta on May 13, 2026. It positions itself as a "personal AI super intelligence" — a local-first agent that ingests data from 118+ connected services, builds a persistent 1-billion-token memory of the user's life and work, and acts autonomously on their behalf. The project hit GitHub trending on its first day (+1,694 stars/day) and reached 27k+ stars within two weeks of launch. *(Updated: as of mid-June 2026, the [GitHub repository](https://github.com/tinyhumansai/openhuman) reports 32.5k+ stars and 3,060+ commits, indicating sustained active development since the May 2026 beta.)*

The project explicitly positions itself against three other hyper-personal/coding assistant products in its README: **Claude Cowork**, **[OpenClaw](openclaw.md)**, and **[Hermes Agent](hermes-agent.md)** — emphasizing open-source availability, minimal vendor dependencies, and local-first workflow retention as differentiators. Claude Cowork is not yet covered elsewhere in this wiki.

Unlike task-scoped coding agents, OpenHuman is designed as a long-lived companion: it continuously absorbs context from email, calendars, code repositories, and messaging platforms, then uses that context to answer questions, complete tasks, and participate in video meetings as a speaking avatar.

---

## Key Capabilities

### NeoCortex Memory Layer

The central differentiator is **NeoCortex** — TinyHumans' proprietary persistent memory system:

- Processes up to **10 million tokens at 4,000 tokens/second** to build a living knowledge graph
- Supports up to **1 billion tokens** of cumulative cross-session memory
- Data is canonicalized into **≤3k-token Markdown chunks**, scored for importance, and folded into hierarchical summary trees
- All data stored in **SQLite on the local machine** — not sent to a cloud data store
- Auto-fetch pulls fresh data from connected services every **20 minutes**
- Storage format is **Obsidian-compatible**: the memory vault opens directly in Obsidian for inspection and editing

### Third-Party Integrations (118+)

One-click OAuth connections managed via the **Composio connector layer**:

| Category | Representative Services |
|---|---|
| Email & Calendar | Gmail, Google Calendar |
| Storage & Docs | Google Drive, Notion, Dropbox |
| Code & Dev | GitHub, Linear, Jira |
| Communication | Slack |
| Finance | Stripe |
| And many more | 110+ additional services |

The integration pipeline automatically ingests new data and folds it into the Memory Tree without manual prompting.

### Agent Toolbelt

Built-in tools available to the agent for task execution:

| Group | Tools |
|---|---|
| **Web** | Web search, web scraping |
| **Coding** | Filesystem read/write, git, lint, test runner, grep |
| **Voice** | Speech-to-text (STT) input, ElevenLabs TTS output |
| **Meetings** | Live Google Meet agent (see Mascot below) |

### Mascot and Voice Interface

OpenHuman ships a **real-time animated desktop mascot** with full voice capabilities:

- **STT in**: dictate tasks and questions via microphone
- **ElevenLabs TTS out**: the mascot speaks responses with lip-sync animation
- **Google Meet integration**: the mascot joins a Google Meet call as a real participant — it listens to all speakers, takes notes directly into the Memory Tree, speaks back into the call when it has something to contribute, and pipes its animated face as the camera feed

### Automatic Model Routing

A built-in router dispatches each task to the optimal LLM based on declared hints:

| Routing Hint | Target |
|---|---|
| `hint:reasoning` | Frontier reasoning model |
| `hint:fast` | Low-cost, low-latency model |
| vision tasks | Vision-capable model |

The default managed experience proxies all model calls through the OpenHuman backend under a single subscription — users do not manage separate API keys for Anthropic, OpenAI, Google, etc. Self-hosted API key configuration is also supported for 200+ models.

### TokenJuice Compression

Every tool call result, scraped page, email body, and search payload passes through **TokenJuice** before reaching any LLM:

- HTML-to-Markdown conversion
- URL shortening and deduplication
- Output deduplication across tool calls
- Claimed reduction in cost and latency of **up to 80%**

---

## Architecture

| Component | Details |
|---|---|
| **Primary language** | Rust 62.1%, TypeScript 33.9%, JavaScript/Shell/CSS/HTML (remainder) |
| **Frontend** | TypeScript + React 19 |
| **Desktop framework** | Tauri (Rust-based cross-platform desktop) |
| **Memory backend** | SQLite on-device; Obsidian-compatible Markdown vault |
| **Integration layer** | Composio connector (OAuth management + data ingestion) |
| **Model access** | OpenHuman managed backend (default) or self-hosted API keys |
| **Token compression** | TokenJuice (in-process, before LLM calls) |
| **OS support** | macOS, Windows, Linux |
| **License** | GPL-3.0 |

### Installation

The project's GitHub README recommends native, signed package managers over the curl/PowerShell scripts, since the scripts lack separate cryptographic signatures:

| Platform | Method |
|---|---|
| macOS (recommended) | Homebrew tap: `brew tap tinyhumansai/core && brew install openhuman`; or signed `.dmg` from GitHub Releases |
| Linux — Debian/Ubuntu (recommended) | Signed APT repository with GPG verification, or `.deb` from GitHub Releases |
| Linux — Arch (recommended) | AUR package `openhuman-bin` |
| Windows (recommended) | Signed `.msi` installer from GitHub Releases |
| macOS / Linux (quick, less verified) | `curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh \| bash` |
| Windows (quick, less verified) | PowerShell: `irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 \| iex` |

No terminal or config file required to get started — GUI onboarding flow handles first-run setup.

**Local development requirements:** Git, Node.js 24+, pnpm 10.10.0, Rust 1.93.0 (with rustfmt and clippy), CMake, Ninja, ripgrep, plus platform-specific desktop build dependencies.

### Contributing

The repository documents two contributor paths: `CONTRIBUTING.md` for experienced developers and `CONTRIBUTING-BEGINNERS.md` for AI-assisted newcomers. Active contributors are tracked in a GitHub "Hall of Fame" and receive free merchandise and Discord access.

---

## Privacy and Data Model

OpenHuman follows a **local-first architecture**: all memory, vault data, and SQLite state live on the user's machine. A local LLM handles low-level summarization and tooling to keep sensitive data off cloud endpoints.

The **managed experience** (default) does route some traffic through TinyHumans servers:
- Model call proxying and routing
- OAuth flow management via Composio
- Web search proxying

Users who want fully air-gapped operation can configure self-hosted models and opt out of managed services, though integration OAuth flows then require self-managed Composio setup.

---

## Security Considerations

OpenHuman inherits the same **toxic flow trifecta** risk as OpenClaw and Hermes: private data access + untrusted content handling + external action capability. Specific concerns:

| Risk | Description |
|---|---|
| **Broad OAuth surface** | Simultaneous OAuth access to email, code repositories, calendar, chat history, and payment tooling — a misconfigured or compromised token can cascade across all connected services |
| **Piped install risk** | The `curl \| bash` / PowerShell install scripts grant execution privileges to remotely hosted code before inspection and lack separate cryptographic signatures. Native signed packages (Homebrew, signed APT repo, AUR, signed MSI) are safer |
| **Managed backend trust** | Default model routing and OAuth flows depend on TinyHumans servers — supply chain trust applies to the managed layer, not just the OSS client |
| **Prompt injection** | 118+ auto-fetched data sources are potential injection vectors; adversarial content in emails, calendar events, or Slack messages could influence agent behavior |

### Mitigations

- Use a native signed package (Homebrew, signed APT repo, AUR, signed MSI, or DMG) rather than `curl | bash` / PowerShell scripts
- Review OAuth scopes carefully; grant only integrations you actively need
- Inspect the Obsidian vault periodically to audit what the agent has retained
- Run on a dedicated machine or user account if handling sensitive credentials
- For high-security environments, disable managed backend services and configure fully local models

---

## Comparison with OpenClaw and Hermes Agent

| Dimension | OpenHuman | OpenClaw | Hermes Agent |
|---|---|---|---|
| **Primary use case** | Personal AI with persistent life-memory | Hyper-personal assistant | Hyper-personal assistant with learning loop |
| **Memory capacity** | 1B tokens, NeoCortex hierarchical tree | 3-tier Markdown (MEMORY.md, daily, DREAMS.md) | FTS5 + Honcho user modeling |
| **Self-improvement** | ❌ | ❌ | ✅ Automatic skill creation + refinement |
| **Integrations** | 118+ OAuth (Composio) | 23+ messaging platforms | MCP servers |
| **Messaging gateways** | ❌ (no chat app bridge) | ✅ WhatsApp, Telegram, Slack, iMessage, 20+ more | ✅ Telegram, Discord, Slack, WhatsApp, Signal, Email |
| **Voice** | ✅ STT + ElevenLabs TTS + mascot lip-sync | ✅ ElevenLabs; wake word (macOS/iOS); continuous (Android) | ✅ Voice memo transcription |
| **Video meeting** | ✅ Google Meet as live participant | ❌ | ❌ |
| **Model flexibility** | 200+ via managed router or own keys | Any provider + Ollama local | Any provider via OpenRouter |
| **Token compression** | ✅ TokenJuice (up to 80% reduction) | ❌ | ❌ |
| **Desktop app** | ✅ Native (Tauri) | ❌ (CLI + terminal UI) | ❌ (CLI + terminal UI) |
| **MCP support** | ❌ | ❌ | ✅ |
| **Language** | Rust + TypeScript | TypeScript / Node.js | Python |
| **Open source** | ✅ GPL-3.0 | ✅ MIT | ✅ |
| **GitHub stars (May 2026)** | ~27k (2 weeks post-launch) | 373k | ~153k |
| **Security profile** | Toxic flow trifecta; managed backend dependency | Toxic flow trifecta; active supply chain incidents | Toxic flow trifecta (inherited) |

---

## Suitable For

- Individuals wanting a persistent AI that knows their full personal and professional context across email, calendar, code, and documents
- Teams evaluating memory-centric personal agent architectures with a 1B-token horizon
- Developers who want a desktop-native agent with a polished GUI rather than a terminal-first experience
- Users interested in voice-first or video meeting AI integration without a separate service layer
- Builders who want an auditable, locally stored memory vault (Obsidian-compatible)

## Limitations

- No self-improvement or skill learning loop — the agent's behavior does not autonomously improve from past task outcomes (cf. Hermes Agent)
- No native messaging gateway — cannot be reached via WhatsApp, Telegram, Slack, etc. (cf. OpenClaw, Hermes)
- No native MCP support
- Default experience depends on the TinyHumans managed backend for model routing and OAuth — partial cloud trust required
- GPL-3.0 license is more restrictive than MIT (OpenClaw) for commercial embedding
- Very new project (May 2026 beta): production track record and long-term ecosystem maturity are unproven
- `curl | bash` / PowerShell install methods are a security risk; native signed packages (Homebrew, APT, AUR, MSI, DMG) are recommended

---

## See Also

- [Popular AI Agents](README.md)
- [OpenClaw](openclaw.md)
- [Hermes Agent (Nous Research)](hermes-agent.md)
- [Agent Memory Solutions](../AgentMemory/solutions.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Production Best Practices — State and Memory](../ProductionBestPractices/state-memory.md)
- [Agentic Tech Stack](../AgenticTechStack/README.md)

## References

- [OpenHuman — TinyHumans AI](https://tinyhumans.ai/openhuman) — official product page
- [tinyhumansai/openhuman — GitHub](https://github.com/tinyhumansai/openhuman) — source repository (32.5k+ stars, 3,060+ commits as of mid-June 2026)
- [OpenHuman Documentation — GitBook](https://tinyhumans.gitbook.io/openhuman) — official documentation
- [OpenHuman on Product Hunt](https://www.producthunt.com/products/openhuman) — launch listing
