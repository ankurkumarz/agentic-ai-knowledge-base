# Kubernetes Agent Sandbox

## Overview

Agent Sandbox is a Kubernetes-native standard, proposed in Google's Open Source Blog (November 2025) and launched as a formal subproject of Kubernetes SIG Apps at KubeCon Atlanta (November 2025), for running autonomous AI agent workloads safely and at scale. The motivating argument: Kubernetes was designed for stateless microservices, but agentic workloads are stateful, long-running, and behave fundamentally differently — they make iterative, quick tool calls (reading a file, running a calculation, querying an API), and for security reasons each of those calls benefits from its own isolated execution sandbox rather than sharing a long-lived Pod. Agent Sandbox introduces a controller-based Sandbox API as a standardized alternative to ad hoc workarounds (e.g., repurposing Jobs or long-lived Pods) for these patterns.

**Naming note**: this Google/Kubernetes SIG Apps initiative is distinct from the independent community project [KAOS (K8s Agent Orchestration System)](../AgentOps/kaos.md), despite both addressing Kubernetes-native agent execution. The Google blog post does not use the name "KAOS"; it introduces the "Agent Sandbox" / "Sandbox" API family described below.

## Key Concepts / Architecture

The ecosystem shift driving this proposal: agentic systems are moving from short-lived tasks to multiple coordinated agents that run continuously, maintain context, use external tools, write and execute code, and communicate with each other over extended periods — requirements that plain Kubernetes Pods do not address natively (persistent memory, complex inter-agent communication, dynamic resource allocation).

**Core API resources:**

| Resource | Purpose |
|---|---|
| `Sandbox` | The core resource defining an agent sandbox workload — a persistent, isolated instance of the agent's environment for single-container, stateful, singleton workloads |
| `SandboxTemplate` | Defines the secure blueprint of a sandbox archetype: resource limits, base image, and initial security policies |
| `SandboxClaim` | A transactional resource allowing users or higher-level agent frameworks (e.g., Google ADK, LangChain) to request an execution environment, abstracting away provisioning logic |

**Performance feature — WarmPools**: an extension that maintains a pool of pre-warmed pods so the Sandbox Controller can hand out a ready instance on claim, reducing cold-start latency to under one second.

## Key Features

- Managed through familiar Kubernetes constructs (controllers, CRDs) rather than a bespoke agent runtime
- Designed to let higher-level agent frameworks request execution environments declaratively via `SandboxClaim`, decoupling agent framework code from sandbox provisioning details
- Targets the security requirement that individual tool calls/code execution should run in isolated environments, not a shared long-lived process

## Governance and Status

- Formal subproject of Kubernetes SIG Apps
- Officially launched at KubeCon Atlanta, November 2025
- Code and docs: `kubernetes-sigs/agent-sandbox` on GitHub; project site at agent-sandbox.sigs.k8s.io
- Related Google Cloud productization: "Agent Sandbox on GKE" and "Agent Substrate," announced alongside GKE Pod Snapshots at the same KubeCon

## See Also

- [KAOS (K8s Agent Orchestration System)](../AgentOps/kaos.md) — independent, similarly-named community project for Kubernetes-native multi-agent orchestration
- [kagent](../AgentOps/kagent.md) — CNCF Sandbox project for running agents as Kubernetes CRDs
- [Agentic Ops Framework (AOF)](../AgentOps/agentic-ops-framework.md)
- [SecurityFrameworks: Agent Sandboxing](../SecurityFrameworks/agent-sandboxing.md) — general agent sandboxing security practices
- [AgentOps Overview](../AgentOps/README.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)

## References

- [Unleashing autonomous AI agents: Why Kubernetes needs a new standard for agent execution (Google Open Source Blog, November 2025)](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html)
- [Bringing you Agent Sandbox on GKE and Agent Substrate (Google Cloud Blog)](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate)
- [Running Agents on Kubernetes with Agent Sandbox (Kubernetes Blog, March 2026)](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)
