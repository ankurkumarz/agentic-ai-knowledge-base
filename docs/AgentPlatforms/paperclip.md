---
type: Platform
title: Paperclip
description: "Paperclip is a self-hosted, MIT-licensed agent orchestration platform that organises AI agents into a company structure with org charts, goals, budgets, governance, and a full audit trail."
tags: [platforms, agentic-ai, orchestration, agent-management]
timestamp: 2026-09-14T00:00:00Z
---
# Paperclip

## Overview

Paperclip is a self-hosted, open-source (MIT) agent orchestration platform that treats AI agents as a workforce rather than individual tools. Users define a company mission, hire agents into roles (CEO, CTO, CMO, engineers, etc.), set per-agent budgets, and approve or override strategy from a governance dashboard. The key mental model shift is from "I am prompting an AI" to "I am managing a team" — every piece of work traces back to the company mission through a goal → project → task hierarchy.

Paperclip is model-agnostic and agent-agnostic: it orchestrates existing agents (Claude Code, Codex, Cursor, Gemini, Hermes, OpenClaw, Pi, OpenCode) rather than replacing them. If an agent can receive a heartbeat signal, Paperclip can hire it.

**Install**: `npx paperclipai onboard --yes`  
**Official site**: https://paperclip.ing/  
**LLM context file**: https://paperclip.ing/llms.txt

---

## Key Concepts

### Org Chart Model

Agents are assigned hierarchical roles with a boss, title, and job description. Delegation flows automatically up and down the reporting tree — a CEO agent can delegate to a CTO, who delegates to engineers. Cross-team requests route to the best available agent for the job.

### Goal Alignment

Every task traces back to the company mission through a four-level hierarchy:

| Level | Example |
|---|---|
| Mission | "Build the #1 AI note-taking app to $1mm ARR" |
| Project Goal | "Ship collaboration features" |
| Agent Goal | "Implement real-time sync" |
| Task | "Write WebSocket handler for document updates" |

Agents know what to do and why — context travels with the work.

### Heartbeat Scheduling

Agents run on scheduled heartbeats rather than continuously by default. A heartbeat wakes an agent to check its work queue and act. Agents can also be triggered by ticket assignment or @-mention. Continuous agents (e.g., OpenClaw) can be hooked in directly.

Example heartbeat cadences from the product:
- Copywriter: every 4 hours
- SEO Analyst: every 8 hours
- Social Manager: every 12 hours

### Ticket System

All agent communication happens through structured tickets. Every instruction, response, tool call, and decision is recorded with full tracing:

| Feature | Detail |
|---|---|
| Ticket ownership | Clear owner, status, and thread per task |
| Full trace | Every tool call, API request, and decision point logged |
| Audit log | Append-only; no edits or deletions; full accountability |

### Budget Controls

Monthly spend limits are set per agent. At 80% utilisation a soft warning fires; at 100% the agent auto-pauses and new tasks are blocked. The board (user) can override the limit and resume at any time. Cost tracking is available per agent, per task, per project, and per goal.

### Governance Model

The user operates as the board of directors:
- Agents cannot hire new agents without board approval
- The CEO cannot execute a strategy the user has not reviewed
- Any agent can be paused, reassigned, or terminated at any time
- Autonomy is a privilege granted by the user, not a default

---

## Four Pillars

Paperclip's product is organized around four operational pillars:

| Pillar | Primary users | Key capabilities |
|---|---|---|
| **Agentic Task Manager** | Everyone, daily | Tasks, approvals & review gates; proactive agent coworkers; auditable routines & workflows; verify from diffs, screenshots & tests |
| **Org Chart for Agents** | Managers | Mixed human + agent org chart; responsibilities, delegation, specialization; governance: who can do what; scoped secrets & company boundaries; connection permissions & responsible-user identities |
| **Agent Employee Training** | Enablers | Skill Studio & shared org-wide skills; evals & saved test runs; active learning loops & quality metrics; performance reviews for agents; saved test inputs; skill version history & restore; reusable team templates |
| **Agentic OS** | IT & platform | Cross-provider runtime: any model, any agent; sandboxing, integrations & MCP servers; SSO, GRC, RBAC & cost controls; data privacy, internal trace collection, compounding data value; personal & shared app connections; run history & opt-in tracing |

---

## Architecture

| Component | Detail |
|---|---|
| **Runtime** | Node.js; single process with embedded Postgres (local mode) |
| **Database** | Embedded Postgres (local) or external Postgres (cloud/remote) |
| **Deployment** | Local instance or remote deploy; multi-company isolation in a single deployment |
| **License** | MIT — self-hosted, no Paperclip account required |
| **Agent protocol** | Heartbeat signal; adapters connect Paperclip to any execution environment |
| **Extension model** | Drop-in extensions add capabilities without modifying core code |
| **Context standard** | `SKILL.md` — agents use Paperclip's SKILL.md to discover needed context |

### Bring Your Own Agent

Paperclip supports any agent that can receive a heartbeat. The full confirmed roster includes:

| Agent | Notes |
|---|---|
| Claude Code | Anthropic agentic coding agent |
| OpenClaw | Local-first personal agent |
| Codex | OpenAI cloud coding agent |
| Cursor + Cloud | IDE-embedded + cloud agent |
| Gemini CLI | Google terminal coding agent |
| OpenCode | Open-source terminal coding agent |
| Pi | earendil.works minimal CLI agent |
| Hermes + Gateway | Nous Research personal agent with gateway routing |
| Grok Build | xAI coding agent |
| Kimi Code | Moonshot AI coding agent |

Custom processes, HTTP endpoints, and external adapter packages extend the roster further.

Adapters connect Paperclip to whatever execution environment the agent uses (Claude Code sessions, OpenClaw bots, Python scripts, shell commands, HTTP webhooks).

---

## Deployment Modes

| Mode | Description |
|---|---|
| **Local** | Single Node.js process; auto-configures embedded Postgres and local file storage; fastest setup |
| **Remote / Cloud** | Standard Postgres backend; agents can assist the deployment using Paperclip's SKILL.md |
| **Multi-company** | Single deployment runs multiple companies with complete data isolation; useful for parallel ventures or org template reuse |

---

## Positioning

Paperclip sits one layer above individual agents — it is the company operating system that organises agents, not a replacement for them. A useful framing from early users: *"OpenClaw is an employee, Paperclip is the company."*

| Dimension | Individual Agent (e.g., OpenClaw) | Paperclip |
|---|---|---|
| Scope | One agent, one user | Many agents, one org |
| Memory / goals | Per-agent | Company-wide mission hierarchy |
| Cost tracking | Per-run | Per agent, task, project, goal |
| Governance | User prompts agent directly | Board approves strategy, hires, budgets |
| Audit | Conversation history | Immutable, append-only ticket + trace log |
| Self-hosting | ✅ | ✅ |
| Open source | ✅ (varies by agent) | ✅ MIT |

---

## Best Practices

| Area | Recommendation |
|---|---|
| Start small | Begin with 2–3 agents and a single project goal before expanding the org |
| Budget hygiene | Set conservative per-agent monthly budgets; treat the 80% warning as a review trigger |
| Governance defaults | Keep board-approval for agent hiring enabled; disable only after you trust the CEO agent's judgment |
| Continuous agents | Hook continuous agents (OpenClaw, custom loops) only for roles where real-time reaction is necessary — heartbeat scheduling reduces runaway cost |
| Audit usage | Use the immutable ticket log as the source of truth for debugging unexpected agent behaviour |
| Multi-company isolation | Use separate company configs for production vs. testing org structures to avoid cross-contamination |

---

## Limitations

- Early-stage product; bring-your-own-ticket-system integration (e.g., Asana, Trello) is on the roadmap but not yet available
- Governance controls scope what agents can do *to Paperclip* (e.g., hiring); securing the agents themselves (prompt injection, credential handling) remains the user's responsibility
- Continuous agent mode requires the user to configure the agent's own security boundaries independently
- Local embedded Postgres simplifies setup but limits horizontal scaling without migration to external Postgres
- **Paperclip Cloud** (always-on hosted mode) is on the roadmap — a waitlist is open but the hosted tier is not yet generally available as of October 2026

---

## See Also

- [Popular AI Agents](README.md)
- [OpenClaw](openclaw.md)
- [Hermes Agent (Nous Research)](hermes-agent.md)
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Production Best Practices — Cost Management](../ProductionBestPractices/cost-management.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Agent Memory Solutions](../AgentMemory/solutions.md)
- [SKILL.md Standard](../Standards/skill-md.md)

## References

- [Paperclip — Official site](https://paperclip.ing/) — product home page and feature overview
- [Paperclip LLM context](https://paperclip.ing/llms.txt) — machine-readable context file for agent onboarding
