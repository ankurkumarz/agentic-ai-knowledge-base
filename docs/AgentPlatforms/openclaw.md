# OpenClaw

## Overview

OpenClaw is a free, MIT-licensed, open-source personal AI agent that runs locally on your own devices and connects to messaging platforms you already use. It is local-first by design: all conversations, memory, and skills are stored as plain Markdown and YAML files on your machine — no data leaves to a vendor-hosted SaaS. A single **Gateway** process runs on your machine (or a server) and acts as the bridge between your messaging apps and an always-available AI assistant.

OpenClaw launched in late January 2026 and became one of the fastest-growing open-source repositories in GitHub history (373k stars as of May 2026). It is the predecessor project to **[Hermes Agent](hermes-agent.md)** (Nous Research), which adds a closed-loop self-improvement layer and GOAP-based reasoning on top of a similar hyper-personal assistant pattern.

**Official docs:** https://docs.openclaw.ai/

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

### Local-First Memory System

OpenClaw memory is a three-tier structure stored as plain files under `~/.openclaw/workspace`:

| File | Role | Loaded automatically |
|---|---|---|
| `MEMORY.md` | Long-term: durable facts, preferences, decisions | Every DM session |
| `memory/YYYY-MM-DD.md` | Daily working notes, running context, observations | Today + yesterday |
| `DREAMS.md` *(optional)* | Consolidation summaries from background dreaming passes | On demand |

Material moves from daily notes into `MEMORY.md` as the agent discerns what is durable. An **Automatic Memory Flush** runs a silent pass before conversation compaction, prompting the agent to save important context before the window closes.

**Memory search tools:**
- `memory_search` — hybrid vector + BM25 keyword search when an embedding provider is configured
- `memory_get` — direct file read or line-range access

**Storage backends (configurable):**

| Backend | Details |
|---|---|
| **Builtin** (default) | SQLite, no extra dependencies |
| **QMD** | Local-first sidecar with reranking and query expansion |
| **Honcho** | Cloud-backed cross-session user modeling |
| **LanceDB** | Bundled plugin with Ollama-compatible embeddings |

**Dreaming (optional):** A background consolidation pass scores and promotes high-signal items into long-term memory via grounded backfill and live promotion pathways.

**Memory Wiki Plugin:** Adds a provenance-rich knowledge layer with structured claims, contradiction tracking, and wiki-native tools alongside core recall.

Auto-detection picks an embedding provider from available API keys (OpenAI, Gemini, Voyage, Mistral) without manual configuration.

### Multi-Platform Messaging

A single Gateway process handles inbound messages from all connected channels, routing them to the same agent context:

| Category | Platforms |
|---|---|
| Mainstream | WhatsApp, Telegram, Slack, Discord, Signal, iMessage |
| Enterprise | Microsoft Teams, Google Chat, Mattermost, Matrix, Nextcloud Talk |
| Regional / niche | Feishu, LINE, WeChat, QQ, Zalo, Nostr, Synapse Chat, Tlon, Twitch, IRC |
| Built-in | WebChat (browser UI) |

Voice notes on WhatsApp and text messages on Slack route to the same agent session.

**Voice:** Wake-word voice mode on macOS/iOS; continuous voice mode on Android. Voice synthesis via ElevenLabs, with system TTS as fallback.

### Built-in Tools

Tools are organised into named groups. Access is controlled globally via `tools.allow` / `tools.deny` in `openclaw.json` (deny wins), and per-agent via allowlists.

| Group | Tools |
|---|---|
| `group:sessions` | `sessions_list`, `sessions_history`, `sessions_send`, `sessions_spawn`, `session_status` |
| `group:ui` | `browser`, `canvas` |
| `group:automation` | `cron`, `gateway` |
| `group:nodes` | `nodes` |
| `group:memory` | `memory_search`, `memory_get` |
| `group:web` | `web_search`, `web_fetch` |
| `group:messaging` | `message` |
| `group:openclaw` | All built-in tools (excludes plugins) |

**Tool profiles** provide preset allowlists: `minimal` (session_status only) and `coding` (file system, runtime, sessions, memory, image).

### Skills and ClawHub

Skills are discrete, portable capability packages. Each skill is a directory containing a `SKILL.md` with YAML frontmatter and instruction text.

**SKILL.md frontmatter fields:**

| Field | Default | Purpose |
|---|---|---|
| `name`, `description` | required | Identity and discovery |
| `homepage` | — | URL shown in macOS Skills UI |
| `user-invocable` | `true` | Expose skill as a slash command |
| `disable-model-invocation` | `false` | Keep skill installable but exclude from agent prompt |
| `command-dispatch: tool` | — | Bypass the model; invoke a tool directly |
| `requires.bins` / `requires.anyBins` | — | Required CLI binaries (load-time gating) |
| `requires.env` | — | Required environment variables (load-time gating) |
| `os` | — | OS restriction |

**Skill load precedence** (highest wins): workspace → project agent → personal agent → managed/local → bundled → extra configured directories.

The agent does not inject full skill text into every prompt. It injects a compact XML list of eligible skills (name, description, path) and loads the full `SKILL.md` on demand when the model judges a skill relevant.

**Agent allowlists:** Per-agent skill lists in `openclaw.json` override defaults. A non-empty list represents the agent's complete available set rather than merging with defaults.

> **Security note from the official docs:** *"Treat third-party skills as untrusted code. Read them before enabling."*

**ClawHub** ([github.com/openclaw/clawhub](https://github.com/openclaw/clawhub)) is the official public skills registry with 3,000+ community-built skills. Install with `openclaw skills install <skill-slug>`; update all with `openclaw skills update --all`.

### Automation and Cron

The built-in cron scheduler runs inside the Gateway process and persists job definitions at `~/.openclaw/cron/jobs.json`.

**Schedule types:**

| Type | Flag | Format |
|---|---|---|
| One-shot | `--at` | ISO 8601 or relative (e.g. `20m`) |
| Fixed interval | `--every` | Duration string |
| Standard cron | `--cron` | 5 or 6-field expression + optional timezone |

Recurring top-of-hour jobs receive automatic staggering (up to 5 minutes) to spread load; override with `--exact`.

**Execution styles:**

| Style | Session value | Behaviour |
|---|---|---|
| Main session | `main` | Enqueues system event at next heartbeat |
| Isolated | `isolated` | Fresh agent turn in new session |
| Current | `current` | Binds to creation-time session context |
| Custom | `session:id` | Persists across runs for workflow continuity |

**Delivery modes:** `announce` (fallback text to target), `webhook` (POST to external URL), `none`.

**External triggers:** Webhooks authenticate via `Authorization: Bearer <token>`. Gmail Pub/Sub integration is available via `openclaw webhooks gmail setup`.

### Live Canvas (A2UI)

An agent-driven visual workspace (A2UI) lets the agent render structured outputs, interact with UI elements, snapshot the canvas state, and maintain a persistent canvas alongside the conversation stream.

### Multi-Agent Routing

Inbound channels, accounts, and peers can route to isolated agent workspaces. Sandboxing is available per session (Docker default; SSH and OpenShell backends also supported). Sub-agents connect to the same Gateway and can be spawned via `sessions_spawn`.

---

## Gateway and Configuration

The Gateway is the single control plane. Key configuration lives in `~/.openclaw/openclaw.json`.

| Item | Detail |
|---|---|
| Default port | `18789` (WebSocket + Control UI) |
| Default bind | `127.0.0.1` (loopback only — do not bind `0.0.0.0` without a firewall) |
| Auth | Token-based; rotated via `openclaw gateway token rotate` |
| Environment variables | `OPENCLAW_HOME`, `OPENCLAW_STATE_DIR`, `OPENCLAW_CONFIG_PATH` |
| Start as daemon | `openclaw onboard --install-daemon` |
| Status check | `openclaw gateway status` |
| Dashboard | `openclaw dashboard` (opens Control UI in browser) |

---

## Architecture

| Component | Details |
|---|---|
| **Primary language** | TypeScript / Node.js |
| **Minimum Node version** | 22.16+ (24 recommended) |
| **Installation** | `npm install -g openclaw@latest` |
| **Gateway** | Local single control plane for sessions, channels, tools, events |
| **Memory backend** | Markdown + YAML files; SQLite / QMD / Honcho / LanceDB for search |
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
| Google | Gemini (via API key) |
| Local | Any GGUF-compatible model via Ollama |

---

## Community and Ecosystem

| Metric | Value (May 2026) |
|---|---|
| GitHub stars | 373k |
| Forks | 77.3k |
| Contributors | 600+ |
| ClawHub skills | 3,000+ |

Sponsors include OpenAI, GitHub, NVIDIA, Vercel, Blacksmith, and Convex.

[awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw) — community-curated list of skills, plugins, memory systems, MCP tools, deployment stacks, and developer tooling.

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
| Exposed instances (SecurityScorecard, Feb 2026) | 135,000+ |
| Instances running without authentication | 63% |
| Later estimates (Censys mapping) | 220,000+ |
| CVE | CVE-2026-33579 |

### Thoughtworks Assessment

Thoughtworks Technology Radar Vol. 34 (April 2026) places OpenClaw at **Caution**, describing it as "permission-hungry by nature." Their blog post ("So, you want to run OpenClaw?") recommends treating secrets as toxic waste, using short-lived tokens with tight scopes, and applying a secret injection pattern so the agent never holds the actual credential string. Thoughtworks restricted OpenClaw on their own managed systems.

### Mitigations

- **Never expose the Gateway to the public internet.** Bind to loopback (`127.0.0.1`); use Tailscale or an SSH tunnel for remote access.
- Rotate the gateway token periodically; isolate the state directory (`chmod 700`).
- Run inside a Docker sandbox; restrict file system and network mounts.
- Use a dedicated low-privilege OS account — not your personal user.
- Apply least-privilege model credentials: scoped API keys, not admin tokens.
- Audit ClawHub skills before installing. Pin to a specific commit hash; prefer verified publishers. Read third-party `SKILL.md` files before enabling.
- Enable DM pairing (`openclaw pairing approve`) — unknown senders receive a pairing code by default.
- For group/channel contexts, sandboxing is strongly recommended.

---

## Comparison with Hermes Agent

| Dimension | OpenClaw | Hermes Agent |
|---|---|---|
| **Primary use case** | Hyper-personal assistant | Hyper-personal assistant with learning loop |
| **Self-improvement** | ❌ | ✅ Automatic skill creation + refinement |
| **Memory tiers** | 3-tier Markdown (MEMORY.md, daily notes, DREAMS.md) + 4 backends | FTS5 + Honcho user modeling |
| **Model flexibility** | Any provider + Ollama local | Any provider via OpenRouter |
| **Messaging platforms** | 23+ (broadest coverage) | 6 (Telegram, Discord, Slack, WhatsApp, Signal, Email) |
| **Voice support** | ✅ ElevenLabs; wake word (macOS/iOS); continuous (Android) | ✅ Voice memo transcription |
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
- [OpenClaw Documentation](https://docs.openclaw.ai/) — official documentation
- [docs.openclaw.ai/start/getting-started](https://docs.openclaw.ai/start/getting-started) — installation and onboarding guide
- [docs.openclaw.ai/tools](https://docs.openclaw.ai/tools) — built-in tools reference
- [docs.openclaw.ai/automation](https://docs.openclaw.ai/automation) — cron and webhook automation
- [docs.openclaw.ai/concepts/memory](https://docs.openclaw.ai/concepts/memory) — memory system architecture
- [docs.openclaw.ai/tools/skills](https://docs.openclaw.ai/tools/skills) — SKILL.md format and skills system
- [docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security) — Gateway security configuration
- [docs.openclaw.ai/platforms](https://docs.openclaw.ai/platforms) — supported messaging platforms
- [openclaw/openclaw — GitHub](https://github.com/openclaw/openclaw) — source repository (373k stars)
- [openclaw/clawhub — GitHub](https://github.com/openclaw/clawhub) — official skills registry
- [awesome-openclaw](https://github.com/vincentkoc/awesome-openclaw) — community curation of skills, plugins, and tooling
- [Thoughtworks Radar Vol. 34 — OpenClaw](https://www.thoughtworks.com/en-sg/radar/tools/openclaw) — Caution placement with rationale
- [So, you want to run OpenClaw? — Thoughtworks](https://www.thoughtworks.com/insights/blog/security/want-run-openclaw) — security guidance from Thoughtworks
- [Researchers Find 341 Malicious ClawHub Skills — The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) — ClawHavoc incident report
- [OpenClaw in the Wild — Censys](https://censys.com/blog/openclaw-in-the-wild-mapping-the-public-exposure-of-a-viral-ai-assistant/) — exposure mapping analysis
- [CVE-2026-33579](https://blink.new/blog/openclaw-cve-33579-am-i-compromised-2026) — vulnerability details
- [Clawdbot → Moltbot → OpenClaw name history](https://www.openclawexperts.io/clawdbot-moltbot-openclaw-name-history) — project lineage
