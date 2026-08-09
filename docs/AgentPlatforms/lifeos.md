---
type: Platform
title: LifeOS
description: LifeOS is an open-source, harness-agnostic personal AI operating system that layers persistent memory, intent routing, and a self-modifying skills library on top of an existing AI coding platform such as Claude Code.
tags: [platforms, agentic-ai, personal-ai-agent, memory]
timestamp: 2026-08-09T00:00:00Z
---

# LifeOS

## Overview

LifeOS (Daniel Miessler) is an AI-powered personal operating system designed to help a user move from a "Current State" to an "Ideal State" in both life and work. Rather than being a standalone agent, it functions as a "general-purpose hill-climbing harness" — a configurable layer that runs on top of an existing AI coding platform (primarily Claude Code, though designed to be harness-agnostic) and adds persistent memory, intent-driven task routing, and self-modifying capabilities so the underlying model's raw reasoning power becomes personalized to the user's specific goals, preferences, and decision history. It sits in the same "personal AI agent" category as [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), and [OpenHuman](openhuman.md), distinguished by being distributed as a single self-contained Claude Code skill rather than a standalone application.

## Key Concepts / Architecture

LifeOS bundles several subsystems into one unified skill:

- **Cortex** — memory architecture: knowledge graph, work history, and accumulated learnings.
- **Synapse** — input routing and task classification; dispatches incoming requests to the appropriate workflow.
- **Atlas** — live asset management and relationship tracking.
- **Ledger** — change tracking and audit logs.
- **The Algorithm** — a seven-phase operating loop: OBSERVE → THINK → PLAN → BUILD → EXECUTE → VERIFY → LEARN.
- **ISA System (Ideal State Artifact)** — a structured document capturing the user's goals across multiple identity lenses.
- **Pulse** — a unified daemon providing voice interfaces, scheduling, dashboards, and optional messaging bridges.
- **Skills Library** — 49+ specialized workflows spanning research, writing, security, and other domains.

Architecturally, LifeOS positions itself as the operational layer *above* raw AI capability: the underlying harness (e.g., Claude Code) supplies reasoning and tool execution, while LifeOS supplies continuity — context, preferences, decision history, and goal-state alignment — across sessions.

### Technology Stack

- Language: TypeScript and Bash
- Runtime: Bun
- Primary platform: Claude Code (designed to be harness-agnostic)
- Distribution: single self-contained skill, installable via a prompt or `curl | bash`
- Persistence: Git-backed version control and local file storage

## Notable Design Patterns

- **Constitution-as-code** — identity and behavioral principles load as system prompts.
- **Capability awareness** — the installer detects which optional features a user wants and provides specific remediation on failure.
- **Recovery-by-design** — every component can be rolled back; user customizations in a dedicated `USER` directory survive upgrades.
- **Community-integrated development** — public PRs are ported into a private source tree, preserving contributor credit while maintaining release stability.

## Licensing

MIT License — free and open source, with explicit commercial-use freedom.

## Suitable for (Pros)

- Individual power users of Claude Code (or another supported harness) who want persistent, cross-session memory and goal tracking without adopting a separate standalone agent platform
- Users who want a self-contained, auditable, git-backed personal knowledge/memory layer rather than a hosted SaaS memory service

## Limitations (Cons)

- Tied in practice to Claude Code as the primary supported harness, despite the harness-agnostic design goal
- Single-user, local-first design — not intended for team or multi-tenant deployment
- As a skill/harness layer rather than a hosted platform, it depends on the capabilities and availability of the underlying AI coding platform it runs on

## See Also

- [Hermes Agent (Nous Research)](hermes-agent.md) — comparable self-improving personal AI assistant with cross-session memory
- [OpenClaw](openclaw.md) and [OpenHuman](openhuman.md) — other personal AI agents with persistent-memory architectures
- [Claude Code](../AICodingAgents/claude-code.md) — the primary harness LifeOS layers on top of, including its plugin/skill ecosystem
- [Long-Term Memory Strategies](../AgentMemory/ltm-strategies.md) — memory consolidation and knowledge-graph strategies related to LifeOS's Cortex subsystem
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md) — related continual-improvement loop patterns (compare "The Algorithm" to the Dreaming Loop)

## References

- [GitHub — danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS)
