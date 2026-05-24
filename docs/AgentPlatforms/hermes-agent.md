# Hermes Agent (Nous Research)

## Overview

Hermes Agent is an open-source, self-improving personal AI agent developed by Nous Research, launched in February 2026. It is the direct successor to OpenClaw and positions itself as the only agent with a built-in learning loop — creating skills from experience, improving them during use, and building a persistent model of the user across sessions. Unlike stateless coding agents, Hermes is designed as a long-lived personal assistant that runs unattended, operates across messaging platforms, and accumulates knowledge over time.

The Hermes project is built on the broader **Nous Hermes model family** — a series of open-source, fine-tuned LLMs (Hermes-2-Pro, Hermes-3) specifically optimized for function calling, structured output, and agentic tool use.

---

## Key Capabilities

### Self-Improvement and Learning Loop

Hermes is differentiated by autonomous, closed-loop learning:

- **Skill creation**: After completing complex tasks, the agent automatically creates reusable skills from the interaction
- **Skill improvement**: Skills are refined during future use, not just stored statically
- **Cross-session memory**: FTS5 full-text session search with LLM summarization allows recall of past conversations
- **User modeling**: Integrates [Honcho](https://www.honcho.dev/) for dialectic user modeling — building a persistent model of user preferences and working style across sessions

### Tool Use and MCP Integration

- **40+ built-in tools** covering file operations, web search, code execution, scheduling, and data retrieval
- **MCP (Model Context Protocol)** server integration for extended tool capabilities
- Compatible with the [agentskills.io](https://agentskills.io/) open standard for skill sharing
- Modular toolset system — add custom tools via the `@tool` decorator pattern

### Multi-Platform Access

| Interface | Details |
|---|---|
| Terminal UI | Multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, streaming tool output |
| Messaging gateways | Telegram, Discord, Slack, WhatsApp, Signal, Email |
| Voice | Voice memo transcription capabilities |
| Seven sandbox backends | Local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox |

### Scheduling and Automation

Built-in cron scheduler for unattended tasks defined in natural language: daily reports, nightly backups, weekly audits. Tasks deploy to any connected platform via the messaging gateway.

### Parallel Execution

Spawn isolated subagents for concurrent workstreams. RPC scripting collapses multi-step pipelines into zero-context-cost turns via Python scripts calling tools over RPC.

---

## Hermes Model Family (Nous Research)

The agent is built on a series of OSS models fine-tuned for agentic use cases:

| Model | Base | Key Capability |
|---|---|---|
| **Hermes-2-Pro-Llama-3-8B** | Llama 3 8B | Function calling via `<tool_call>` / `<tool_response>` XML tags; JSON structured output; ChatML format |
| **Hermes-3** | Llama 3.1 (8B, 70B, 405B) | Goal Oriented Action Planning (GOAP) via `<scratch_pad>` tags; enhanced multi-turn tool use |

### Function Calling Architecture (Hermes-2-Pro / Hermes-3)

The Hermes models use a structured ChatML prompt format with a distinctive XML-tag tool-call protocol:

```
<tool_call>
{"name": "function_name", "arguments": {"param": "value"}}
</tool_call>
```

The Hermes-3 GOAP template adds a reasoning scratch pad:

```
<scratch_pad>
Goal: [restated user intent]
Actions: [planned function calls]
Observation: [summarized tool results]
Reflection: [evaluating relevance and task progress]
</scratch_pad>
```

Models support:
- Recursive function calling (configurable depth, default 5)
- JSON mode / structured outputs via Pydantic schema enforcement
- 4-bit quantization for memory-efficient deployment
- Few-shot example injection for domain specialisation

---

## Architecture

| Component | Details |
|---|---|
| **Primary language** | Python (88%), TypeScript (8.8%) |
| **Installation** | Single-command scripts for Linux, macOS, WSL2, Windows (Windows in early beta) |
| **Deployment** | $5 VPS up to enterprise GPU clusters |
| **Model providers** | Nous Portal, OpenRouter (200+ models), NovitaAI, NVIDIA NIM, OpenAI, Anthropic, custom endpoints |
| **Memory backend** | Persistent storage + FTS5 full-text search + Honcho user modeling |
| **Skill storage** | Git-compatible, versioned skill library |

---

## Comparison with Related Agents

| Dimension | Hermes Agent | OpenClaw | Claude Code | OpenCode |
|---|---|---|---|---|
| **Primary use case** | Hyper-personal assistant with learning loop | Hyper-personal assistant | Coding agent | Coding agent |
| **Self-improvement** | ✅ Automatic skill creation + refinement | ❌ | ❌ | ❌ |
| **Cross-session memory** | ✅ Persistent + user modeling | ✅ Persistent | ❌ | ❌ |
| **MCP support** | ✅ | ❌ | ✅ | ✅ |
| **Messaging gateways** | ✅ (Telegram, Discord, Slack, WhatsApp) | ✅ (WhatsApp, iMessage) | ❌ | ❌ |
| **Model flexibility** | Any provider via OpenRouter etc. | Limited | Anthropic only | Any provider |
| **Open source** | ✅ | ✅ | ❌ | ✅ |
| **Security profile** | Permission-hungry (same trifecta risk as OpenClaw) | Permission-hungry | Sandboxed | Sandboxed |

---

## Security Considerations

Hermes Agent inherits the same **toxic flow trifecta** risk as OpenClaw: private data access + untrusted content handling + external action capability. The more tools and integrations enabled, the more useful — and the more concentrated the permission surface. Key mitigations:

- Run in a sandboxed Docker or Daytona environment to restrict file system and network access
- Apply least-privilege tool selection — enable only the tools needed
- Use the messaging gateway with a dedicated account rather than personal accounts
- Review skills before enabling — supply chain risk from third-party skill imports
- Migrate from OpenClaw using the built-in migration tooling (preserves settings, memories, skills)

See [Toxic flow analysis for AI](../AgenticTechStack/thoughtworks-radar-vol34.md) and [Production Best Practices — Security](../ProductionBestPractices/security.md) for broader guidance.

---

## Community and Ecosystem

The **Hermes Atlas** ([hermesatlas.com](https://hermesatlas.com)) community directory catalogs 80+ quality-filtered repositories across 12 categories: skills, plugins, integrations, deployment templates, and forks. The ecosystem expanded rapidly after launch in February 2026.

**Hermes Function Calling** reference repository: [NousResearch/hermes-function-calling](https://github.com/NousResearch/hermes-function-calling) — 1.4K stars, 187 forks (illustrates model adoption independent of the agent itself).

---

## Suitable For

- Teams building personal AI assistants that need persistent cross-session context and self-improvement
- Engineers who want an OSS personal assistant on self-hosted or low-cost infrastructure
- Developers experimenting with the GOAP reasoning pattern or Hermes model fine-tuning for tool use
- Researchers evaluating hyper-personal assistant architectures (with careful security scoping)

## Limitations

- Hyper-personal assistant pattern requires broad permissions — inherent security tension
- Windows support is still in early beta
- Ecosystem is rapidly evolving; skill quality and supply chain risk require active curation
- GOAP reasoning (Hermes-3) and skill self-improvement are newer features with limited long-term production case studies

---

## See Also

- [Popular AI Agents](README.md)
- [OpenClaw](openclaw.md)
- [OpenHuman (TinyHumans AI)](openhuman.md)
- [Agentic Tech Stack](../AgenticTechStack/README.md)
- [Thoughtworks Radar Vol. 34 — OpenClaw (Caution)](../AgenticTechStack/thoughtworks-radar-vol34.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Agent Memory Solutions](../AgentMemory/solutions.md)
- [MCP Standard](../Standards/mcp.md)

## References

- [Hermes Agent — Nous Research](https://hermes-agent.nousresearch.com/) — official product page
- [NousResearch/hermes-agent — GitHub](https://github.com/NousResearch/hermes-agent) — source repository
- [NousResearch/hermes-function-calling — GitHub](https://github.com/NousResearch/hermes-function-calling) — Hermes-2-Pro function calling reference implementation
- [Hermes Atlas](https://hermesatlas.com) — community ecosystem directory
- [agentskills.io](https://agentskills.io/) — open skills standard Hermes integrates with
