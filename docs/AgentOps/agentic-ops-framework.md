# Agentic Ops Framework (AOF)

## Overview

The Agentic Ops Framework (AOF) is an open source, Rust-based framework that lets DevOps, SRE, and platform engineers build and orchestrate AI agents using Kubernetes-style YAML specifications and a `kubectl`-style CLI (`aofctl`). It is positioned as "n8n for Agentic Ops" — a way to define and run operational AI agents without writing Python, by reusing the declarative mental model operators already have from Kubernetes.

## Key Concepts / Architecture

AOF defines three core resource abstractions, each expressed as a Kubernetes-style manifest (`apiVersion: aof.dev/v1`, `kind: ...`):

- **Agent** — a single AI instance configured with instructions, tools, and a model
- **AgentFleet** — a coordinated team of multiple agents working together on a task
- **AgentFlow** — a DAG-based, multi-step workflow with conditional branches and human-approval gates

The CLI mirrors `kubectl` semantics (e.g., `aofctl apply`, `aofctl run agent`), so operators familiar with Kubernetes tooling can apply the same workflow to agent definitions.

## Key Features

- **LLM providers**: OpenAI (GPT-4), Anthropic Claude, Google Gemini, Ollama (local models), and Groq, switchable without code changes
- **Integrations**: `kubectl`, shell/bash execution, HTTP requests, Slack, Discord, Telegram, GitHub, PagerDuty (incident webhooks), and custom MCP tool servers
- **Human-in-the-loop**: approval gates implemented as conditional workflow branches — e.g., routing high-severity findings to Slack for manual sign-off before remediation runs
- **Safety controls**: allowed command lists and audit logging to constrain what agents can execute against live infrastructure
- **Memory**: persistent memory and RAG integration intended to let agents retain context and learn across interactions

## Suitable For (Pros)

- Teams that want operational/DevOps automation agents (incident response, ChatOps bots, remediation workflows) defined declaratively, alongside existing Kubernetes manifests
- Organizations standardizing on a single CLI/YAML mental model across infrastructure and agent definitions
- Use cases requiring tight integration with ops tooling (PagerDuty, Slack, GitHub) out of the box

## Status

- Apache 2.0 licensed, written in Rust (~90% of codebase)
- Beta maturity (latest release v0.4.0-beta at time of writing); installable via Cargo, pre-built binaries, or GitHub Releases (`curl -sSL https://aof.dev/install.sh | bash`)
- Maintained under the `agenticdevops` organization on GitHub; documentation at docs.aof.sh

## See Also

- [kagent](kagent.md) — CNCF Sandbox project for running agents as native Kubernetes CRDs (Go/Python stack vs. AOF's Rust CLI-first approach)
- [KAOS (K8s Agent Orchestration System)](kaos.md) — another Kubernetes-native multi-agent orchestration project
- [Kubernetes Agent Sandbox (SIG Apps)](../Standards/k8s-agent-sandbox.md)
- [Standards/MCP](../Standards/mcp.md) — protocol AOF uses for custom tool integration
- [AgentOps Overview](README.md)
- [ProductionBestPractices: Deployment](../ProductionBestPractices/deployment.md) — GitOps and human-in-the-loop deployment gating patterns

## References

- [aof.sh](https://aof.sh/) — official project site
- [docs.aof.sh](https://docs.aof.sh/) — documentation index
- [GitHub - agenticdevops/aof](https://github.com/agenticdevops/aof) — source repository
