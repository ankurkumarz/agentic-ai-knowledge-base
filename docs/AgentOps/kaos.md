# KAOS (K8s Agent Orchestration System)

## Overview

KAOS is an open source, Kubernetes-native framework for deploying and orchestrating distributed multi-agent AI systems at scale — tool access, multi-agent coordination, and LLM integration managed through Kubernetes Custom Resources. It targets the specific pain of taking multi-agent/multi-tool/multi-model systems from a handful of agents to hundreds or thousands of services.

**Naming note**: KAOS is an independent community project (`axsaucedo/kaos` on GitHub) and is unrelated to Google's "Agent Sandbox" Kubernetes SIG Apps subproject, even though both address Kubernetes-native agent execution and both have been informally referred to using similar "agent orchestration" language. See [Kubernetes Agent Sandbox](../Standards/k8s-agent-sandbox.md) for the latter.

## Key Concepts / Architecture

KAOS splits responsibilities across three planes:

- **Control plane (Go)**: a KAOS Operator running three controllers — Agent Controller, MCPServer Controller, and ModelAPI Controller — that reconcile the corresponding Kubernetes CRDs
- **Data plane (Python)**: Agent Pods running the agent runtime, MCP Server Pods for tool integration, and ModelAPI Pods for LLM access (via Ollama/LiteLLM)
- **UI (TypeScript/React)**: a visual dashboard for monitoring agents, testing chat, and debugging memory and tool calls

Agents are powered by **PAIS** (an enterprise server wrapper around Pydantic AI) which adds an OpenAI-compatible HTTP API (`/v1/chat/completions`), distributed memory, multi-agent delegation, Agent2Agent (A2A) discovery, health probes, and OpenTelemetry instrumentation on top of plain Pydantic AI agents.

## Key Features

- Agentic graphs expressed as Kubernetes resources
- MCP tool integration
- Hierarchical multi-agent systems with automatic delegation
- OpenAI-compatible chat completions endpoint per agent
- CLI and visual dashboard for management and debugging

## Suitable For (Pros)

- Teams needing to scale distributed multi-agent systems across hundreds/thousands of services on Kubernetes
- Use cases wanting an OpenAI-compatible API surface per agent for drop-in compatibility with existing client tooling
- Pydantic AI users wanting an enterprise server wrapper without building one from scratch

## Status

- Apache 2.0 licensed
- ~259 GitHub stars, 17 forks, 21 releases (v0.4.7 latest as of mid-2026), ~1,180 commits — active development by an independent maintainer (`axsaucedo`)

## See Also

- [kagent](kagent.md) — CNCF Sandbox project with a similar goal of running agents as native Kubernetes CRDs
- [Agentic Ops Framework (AOF)](agentic-ops-framework.md) — Rust/CLI-first alternative for ops-focused agent orchestration
- [Kubernetes Agent Sandbox (SIG Apps)](../Standards/k8s-agent-sandbox.md) — Google-driven Kubernetes SIG Apps subproject for isolated agent execution (distinct project, overlapping naming)
- [Standards/MCP](../Standards/mcp.md)
- [Standards/Agent2Agent (A2A)](../Standards/agent2agent.md) — protocol used for KAOS agent discovery
- [AgentOps Overview](README.md)

## References

- [GitHub - axsaucedo/kaos](https://github.com/axsaucedo/kaos) — source repository
