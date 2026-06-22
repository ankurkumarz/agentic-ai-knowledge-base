# kagent

## Overview

kagent ("Cloud Native Agentic AI") is an open source framework for building, deploying, and managing AI agents as native Kubernetes resources. Originated by Solo.io and contributed to the Cloud Native Computing Foundation (CNCF) as a Sandbox project, it targets DevOps and platform engineers who want to run agents using the same GitOps, RBAC, and observability tooling they already use for the rest of their cluster — rather than standing up a separate agent runtime outside Kubernetes.

## Key Concepts / Architecture

kagent makes an agent a first-class Kubernetes workload: agents are defined as Custom Resources (CRDs), versioned in Git, reviewed in pull requests, and rolled out with standard Kubernetes tooling (Helm, ArgoCD, kubectl).

**Core components:**
- **Controller** — a Kubernetes operator that watches and reconciles agent-related custom resources
- **Engine** — runs agent logic; built on Google's Agent Development Kit (ADK), with earlier releases built on Microsoft's AutoGen framework
- **UI** — a web interface for managing agents, tools, and visualizing runs
- **CLI** — command-line tooling for agent lifecycle management

**Key CRDs:**
- `Agent` — defines an agent's system prompt, tool bindings, and LLM/model configuration
- `ModelConfig` — represents an LLM provider configuration (model, credentials, endpoint)
- `ToolServers` — Kubernetes resources that expose Model Context Protocol (MCP) tool servers to agents

## Key Features

- **Protocol composition** — built on the MCP and A2A protocols, allowing models, frameworks, and tools to be swapped without rewriting agents
- **MCP tool integration** — ships with MCP servers for common cloud-native tooling: Kubernetes, Istio, Helm, Argo, Prometheus, Grafana, and Cilium
- **Multi-provider LLM support** — OpenAI, Azure OpenAI, Anthropic, Google Vertex AI, Ollama, and custom models reachable via AI gateways
- **Observability** — every prompt, tool call, and token emits OpenTelemetry traces through the same pipeline used for the rest of the cluster's services
- **Declarative configuration** — agents, tools, and models are all expressed as YAML Kubernetes manifests

## Suitable For (Pros)

- Platforms already standardized on Kubernetes GitOps workflows that want agent definitions to follow the same review/rollout discipline as other workloads
- Cloud-native operations use cases: configuration management, troubleshooting, deployment automation, observability pipeline setup, and network security changes (mTLS, authN/authZ)
- Teams that want agent observability unified with existing OTel-based monitoring stacks

## Governance and Status

- CNCF Sandbox project (contributed by Solo.io)
- As of the project's "100 Days" milestone (August 2025): 100+ contributors (85%+ from outside Solo.io) and 1,000+ GitHub stars; later figures show 3,100+ stars and 620+ forks
- Active Discord community and regular community meetings

## See Also

- [Agentic Ops Framework (AOF)](agentic-ops-framework.md) — a Rust-based, kubectl-style alternative for DevOps/SRE agent orchestration
- [KAOS (K8s Agent Orchestration System)](kaos.md) — a separate community project pursuing similar Kubernetes-native multi-agent orchestration goals
- [Kubernetes Agent Sandbox (SIG Apps)](../Standards/k8s-agent-sandbox.md) — emerging Kubernetes-native standard for isolated agent execution environments
- [Standards/MCP](../Standards/mcp.md) — Model Context Protocol used for kagent's tool integration
- [Standards/Agent2Agent (A2A)](../Standards/agent2agent.md) — protocol kagent composes for agent interoperability
- [AgentOps Overview](README.md)
- [Google ADK](../AgenticFrameworks/google-adk.md) — engine kagent's runtime is built on

## References

- [kagent.dev](https://kagent.dev/) — official project site
- [GitHub - kagent-dev/kagent](https://github.com/kagent-dev/kagent) — source repository
- [Kagent: Bringing Agentic AI to Cloud Native (CNCF Blog, April 2025)](https://www.cncf.io/blog/2025/04/15/kagent-bringing-agentic-ai-to-cloud-native/)
- [Celebrating 100 Days of Kagent (CNCF Blog, August 2025)](https://www.cncf.io/blog/2025/08/19/celebrating-100-days-of-kagent/)
- [Bringing Agentic AI to Kubernetes: Contributing Kagent to CNCF (Solo.io Blog)](https://www.solo.io/blog/bringing-agentic-ai-to-kubernetes-contributing-kagent-to-cncf)
