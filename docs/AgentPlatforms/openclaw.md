# OpenClaw

## Overview

OpenClaw is a free, MIT-licensed, open-source personal AI agent that runs locally on your own devices and connects to messaging platforms you already use. It is local-first by design: all conversations, memory, and skills are stored as plain Markdown and YAML files on your machine — no data leaves to a vendor-hosted SaaS. OpenClaw launched in late January 2026 and became one of the fastest-growing open-source repositories in GitHub history, reaching 373k stars within months of release.

OpenClaw is the predecessor project to **[Hermes Agent](hermes-agent.md)** (Nous Research), which adds a closed-loop self-improvement layer and GOAP-based reasoning on top of a similar hyper-personal assistant pattern.

---

## History

OpenClaw has passed through three names reflecting major architectural rewrites:

| Phase | Name | Architecture | Config | Skill Format |
|---|---|---|---|---|
| 1 | **Clawdbot** | Single-file agent | Flat JSON | Loose scripts |
| 2 | **Moltbot** | Plugin system + HTTP gateway | TOML | Modules |
| 3 | **OpenClaw** | Local Gateway + multi-agent routing | YAML | `SKILL.md` standard |

The rename from Clawdbot was requested by Anthropic (too close to "Claude"). The skills format standardised at SKILL.md and the ClawHub marketplace launched alongside the OpenClaw rebrand.

---

## Key Capabilities

### Local-First Memory

OpenClaw stores all state as human-readable files:

- Conversations and session transcripts in `~/.openclaw/`
- Long-term memory in `MEMORY.md` and `memory/*.md` workspace files
- Skills as `SKILL.md` + supporting files

Files can be inspected in any text editor, versioned with Git, searched with `grep`, or deleted without ceremony. An indexing layer (SQLite or QMD) enables semantic search via embeddings, with optional BM25 hybrid search for improved recall.

### Multi-Platform Messaging

A single Gateway process handles inbound messages from all connected channels, routing them to the same agent context:

| Category | Platforms |
|---|---|
| Mainstream | WhatsApp, Telegram, Slack, Discord, Signal, iMessage |
| Enterprise | Microsoft Teams, Google Chat, Mattermost, Matrix, Nextcloud Talk |
| Regional / niche | Feishu, LINE, WeChat, QQ, Zalo, Nostr, Synapse Chat, Tlon, Twitch |
| Built-in | WebChat (browser UI) |

Voice notes on WhatsApp and text messages on Slack route to the same agent session. Voice wake and talk mode are supported on macOS, iOS, and Android.

### Skills and ClawHub

Skills are discrete, portable capability packages (`SKILL.md` + supporting files). The agent does not inject full skill text into every prompt — it injects a compact index (name, description, file path) and loads the full `SKILL.md` on demand when it judges a skill relevant.

**ClawHub** ([clawhub](https://github.com/openclaw/clawhub)) is the official public skills registry with 3,000+ community-built skills across automation, productivity, developer tooling, and domain-specific workflows.

### Live Canvas (A2UI)

An agent-driven visual workspace (A2UI) lets the agent render structured outputs, interact with UI elements, and maintain a persistent canvas alongside the conversation stream.

### Multi-Agent Routing

Inbound channels, accounts, and peers can route to isolated agent workspaces. Sandboxing is available per session (Docker default; SSH and OpenShell backends also supported).

### Automation

Built-in support for cron jobs, webhooks, and Gmail Pub/Sub enables unattended background workflows defined in natural language.

---

## Architecture

| Component | Details |
|---|---|
| **Primary language** | TypeScript / Node.js (requires Node 24+) |
| **Installation** | `npm install -g openclaw@latest` then `openclaw onboard --install-daemon` |
| **Gateway** | Local single control plane for sessions, channels, tools, events |
| **Memory backend** | Markdown + YAML files; SQLite or QMD index for semantic search |
| **Skill storage** | `~/.openclaw/workspace/skills/` (local) + ClawHub (remote registry) |
| **Sandboxing** | Docker (default), SSH, OpenShell |
| **Companion apps** | macOS menu bar app; iOS and Android nodes via WebSocket |
| **OS support** | macOS, Linux, Windows (WSL2), iOS, Android |

---

## Model Support

| Provider | Models |
|---|---|
| Anthropic | Claude (all current flagship models) |
| OpenAI | GPT-4o and successors |
| xAI | Grok |
| DeepSeek | DeepSeek V4 Flash, DeepSeek V4 Pro |
| Local | Any GGUF-compatible model via Ollama |

---

## Community and Ecosystem

| Metric | Value (as of May 2026) |
|---|---|
| GitHub stars | 373k |
| Forks | 77.3k |
| Contributors | 600+ |
| ClawHub skills | 3,000+ |
| Open issues | ~3.5k |

Sponsors include OpenAI, GitHub, NVIDIA, Vercel, Blacksmith, and Convex.

An independent community curation project, [awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw), tracks skills, plugins, memory systems, MCP tools, deployment stacks, and developer tooling.

---

## Security Considerations

OpenClaw is the primary case study for the **toxic flow trifecta** (also called the "lethal trifecta"): an agent that combines **private data access + untrusted content handling + external action capability**. Each element alone is manageable; the combination means a single misconfiguration can cascade into full credential and data exposure.

### ClawHavoc — Skills Supply Chain Incident (Feb 2026)

A coordinated campaign (ClawHavoc) planted malicious skills into ClawHub. Findings from multiple security researchers:

| Metric | Finding |
|---|---|
| Malicious skills confirmed | 341–1,184 (sources vary by audit date) |
| Prompt injection rate across all skills audited | 36% |
| Malware delivery vectors | Crypto wallets, trading bots, YouTube utilities, auto-updaters, Workspace integrations |
| Primary payloads | Atomic macOS Stealer, Windows credential harvesters |
| ClawHub ranking manipulation | Attackers exploited ranking to place malicious skill at #1 |

### Exposed Instances

| Metric | Finding |
|---|---|
| Exposed instances identified (SecurityScorecard, Feb 2026) | 135,000+ |
| Instances running without authentication | 63% |
| Later estimates (Censys mapping) | 220,000+ |
| CVE | CVE-2026-33579 |

### Thoughtworks Assessment

Thoughtworks Technology Radar Vol. 34 (April 2026) places OpenClaw at **Caution**, describing it as "permission-hungry by nature." Their blog post ("So, you want to run OpenClaw?") recommends treating secrets as toxic waste, using short-lived tokens with tight scopes, and applying a secret injection pattern so the agent never holds the actual credential string. Thoughtworks restricted OpenClaw on their own managed systems.

### Mitigations

- **Never expose OpenClaw to the public internet.** Use a VPN or SSH tunnel if remote access is needed.
- Run inside a Docker sandbox; restrict file system and network mounts.
- Use a dedicated low-privilege system account — not your personal user.
- Apply least-privilege model credentials: scoped API keys, not admin tokens.
- Audit ClawHub skills before installing. Prefer skills from verified publishers; pin to a specific commit hash.
- Enable DM pairing (`openclaw pairing approve`) — unknown senders receive a pairing code by default.
- Set up authentication on the WebChat interface.

---

## Comparison with Hermes Agent

| Dimension | OpenClaw | Hermes Agent |
|---|---|---|
| **Primary use case** | Hyper-personal assistant | Hyper-personal assistant with learning loop |
| **Self-improvement** | ❌ | ✅ Automatic skill creation + refinement |
| **Cross-session memory** | ✅ Markdown/YAML files + semantic search | ✅ FTS5 + Honcho user modeling |
| **Model flexibility** | Any provider + Ollama local | Any provider via OpenRouter |
| **Messaging platforms** | 20+ (broadest coverage) | 6 (Telegram, Discord, Slack, WhatsApp, Signal, Email) |
| **Voice support** | ✅ (macOS, iOS, Android native) | ✅ (voice memo transcription) |
| **Skills ecosystem** | ClawHub (3,000+) | agentskills.io standard |
| **MCP support** | ❌ (not native) | ✅ |
| **Language** | TypeScript / Node.js | Python |
| **Open source** | ✅ MIT | ✅ |
| **Security profile** | Permission-hungry; active supply chain incidents | Permission-hungry (inherited pattern) |
| **Community size** | 373k GitHub stars | Newer; smaller |
| **Status** | Active; predecessor project | Active; designed as OpenClaw successor |

---

## Suitable For

- Developers wanting a local-first, fully inspectable personal agent with broad messaging platform coverage
- Teams evaluating hyper-personal assistant architectures before choosing between OpenClaw and its successor Hermes
- Engineers who need 20+ messaging integrations in a single runtime
- Researchers studying agentic supply chain security and the toxic flow trifecta pattern

## Limitations

- No built-in self-improvement or skill-learning loop (see Hermes Agent for this)
- No native MCP support
- Active supply chain risk: ClawHub skill vetting is community-driven, not curated
- High exposure footprint: tens of thousands of misconfigured public instances create a noisy threat landscape
- Windows support requires WSL2
- Rapid growth means documentation and security hardening lag behind adoption

---

## See Also

- [Popular AI Agents](README.md)
- [Hermes Agent (Nous Research)](hermes-agent.md)
- [Agentic Tech Stack](../AgenticTechStack/README.md)
- [Thoughtworks Radar Vol. 34 — OpenClaw at Caution](../AgenticTechStack/thoughtworks-radar-vol34.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Agent Memory Solutions](../AgentMemory/solutions.md)
- [MCP Standard](../Standards/mcp.md)

## References

- [OpenClaw — Official site](https://openclaw.ai/) — product home page
- [openclaw/openclaw — GitHub](https://github.com/openclaw/openclaw) — source repository (373k stars)
- [openclaw/clawhub — GitHub](https://github.com/openclaw/clawhub) — official skills registry
- [awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw) — community curation of skills, plugins, and tooling
- [Thoughtworks Radar Vol. 34 — OpenClaw](https://www.thoughtworks.com/en-sg/radar/tools/openclaw) — Caution placement with rationale
- [So, you want to run OpenClaw? — Thoughtworks](https://www.thoughtworks.com/insights/blog/security/want-run-openclaw) — security guidance from Thoughtworks
- [Researchers Find 341 Malicious ClawHub Skills — The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) — ClawHavoc incident report
- [OpenClaw in the Wild — Censys](https://censys.com/blog/openclaw-in-the-wild-mapping-the-public-exposure-of-a-viral-ai-assistant/) — exposure mapping analysis
- [OpenClaw CVE-2026-33579](https://blink.new/blog/openclaw-cve-33579-am-i-compromised-2026) — vulnerability details
- [Clawdbot → Moltbot → OpenClaw name history](https://www.openclawexperts.io/clawdbot-moltbot-openclaw-name-history) — project lineage
