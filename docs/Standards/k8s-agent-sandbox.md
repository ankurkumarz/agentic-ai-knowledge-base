---
type: Standard
title: Kubernetes Agent Sandbox
description: "Agent Sandbox is a Kubernetes-native standard, proposed in Google's Open Source Blog (November 2025) and launched as a formal subproject of Kubernetes SIG Apps at KubeCon Atlanta (November 2025), f..."
tags: [standards, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
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

## Core CRD API Reference

The official `kubernetes-sigs/agent-sandbox` release (as of April 2026) exposes the following CRDs:

| CRD | Purpose |
|---|---|
| `Sandbox` | Declarative API for a single, stateful pod with a stable hostname and optional persistent storage |
| `SandboxTemplate` | Reusable templates that codify runtime configuration for consistent sandbox provisioning |
| `SandboxClaim` | User-facing abstraction that provisions a sandbox from a template without exposing low-level details |
| `SandboxWarmPool` | Pre-warmed pod pools for near-instant sandbox allocation (sub-millisecond assignment vs. cold pod scheduling) |

## Key Features

- Managed through familiar Kubernetes constructs (controllers, CRDs) rather than a bespoke agent runtime
- Designed to let higher-level agent frameworks request execution environments declaratively via `SandboxClaim`, decoupling agent framework code from sandbox provisioning details
- Targets the security requirement that individual tool calls/code execution should run in isolated environments, not a shared long-lived process
- **Stable identity and persistent storage**: each Sandbox has a stable hostname and can be backed by a PVC that survives restarts, allowing agents to reconnect across sessions without application-level coordination
- **Hibernation & resume**: the controller can pause sandboxes to free compute resources and resume them automatically on incoming network connections — state is preserved during the sleep window, eliminating cold-state cost for bursty workloads
- **Scheduled deletion**: TTL-based automatic cleanup via the controller, removing the need for manual sandbox lifecycle management
- **Runtime-agnostic isolation**: pluggable backends — standard containers, gVisor (kernel-level), and Kata Containers (VM-grade) — are selected at deploy time, not baked into the API

## Client SDKs

Agent Sandbox ships first-class client libraries for programmatic sandbox management:

| SDK | Language | Capabilities |
|---|---|---|
| **Python Client** | Python | Create/query/manage sandboxes; filesystem read/write/transfer; designed for Python-based agent runtimes |
| **Go Client** | Go | Same API surface; designed for Go services, controllers, and platform tooling |

Both SDKs expose `Filesystem` operations (read, write, list, transfer files into/out of sandboxes) and `Volume` attachment for mounting persistent storage.

## Use Cases

The project documents several canonical deployment patterns:

| Pattern | Lifecycle | Description |
|---|---|---|
| **Code Execution** | Short-lived | Run untrusted LLM-generated code in fully isolated sandboxes; ideal for code interpreters, analytics tools, on-demand computation |
| **Coding Agents** | Medium-lived | Autonomous agents that write, debug, and refactor code inside secure sandboxes with full dev tooling |
| **Computer Use** | Medium-lived | AI agents that interact with graphical desktops, browsers, and GUI applications inside isolated sandboxes |
| **CI/CD Integration** | Short-to-medium | Isolated testing, validation, and automated workflows integrated into CI/CD pipelines |
| **Always-on Agent Environments (OpenClaw)** | Long-lived | Run [OpenClaw](../AgentPlatforms/openclaw.md) agent environments persistently inside Agent Sandbox for long-running workloads |
| **gVisor Isolation** | Any | Harden sandbox isolation with gVisor's userspace kernel — intercepts system calls to protect the host |
| **Kata Containers Isolation** | Any | Hardware virtualization with a dedicated kernel per sandbox via Kata Containers + QEMU |

## Governance and Status

- Formal subproject of Kubernetes SIG Apps
- Officially launched at KubeCon Atlanta, November 2025
- Code and docs: `kubernetes-sigs/agent-sandbox` on GitHub; project site at agent-sandbox.sigs.k8s.io
- **GKE Agent Sandbox reached General Availability** *(Updated: previously framed only as the KubeCon Atlanta launch; as of the Google Cloud Blog GA announcement, GKE Agent Sandbox is now generally available)*

## GKE Productization: GA and Agent Substrate

Google Cloud's GKE-specific productization of the Agent Sandbox standard reached GA with several concrete performance and cost claims:

| Capability | Detail |
|---|---|
| Pod Snapshots integration | Suspends idle agent workloads and resumes them in seconds — addresses the "short bursty cycles followed by longer idle periods" pattern typical of agent workloads, avoiding wasted compute on idle agents |
| Sandbox provisioning latency | The Agent Sandbox API's integrated warm pool allocates 300 sandboxes per second per cluster, with 90% of allocations completing within 200 milliseconds |
| Cold-pool cost efficiency | Standby capacity buffers (suspended VMs) replenish the warm pool at a fraction of the cost of keeping pools live |
| Security | Native gVisor support and default-deny Kubernetes network policy, with pluggable interfaces for Kata Containers |
| Price-performance | Up to 30% better price-performance on Axion processors than comparable hyperscaler offerings |
| Adoption | 16x growth in sandboxes on GKE in under 5 months since the preview announcement |

### Agent Substrate (new, separate open-source project)

Agent Substrate is a distinct Google open-source project — not a renamed or merged version of Agent Sandbox — aimed at the performance and density needs of ultra-scale agent fleets:

- Takes the core secure runtime and snapshotting capabilities of Agent Sandbox and pairs them with a **minimal control plane** designed to bypass certain Kubernetes control-plane limits without reinventing the rest of the Kubernetes stack
- Standard Kubernetes is optimized for thousands of long-running services; Agent Substrate is designed for the chatter of **millions of sub-second tool calls** that would overwhelm a standard control plane
- Intended as the foundation for agents, agent harnesses, and agent runtimes — including a newly announced "Agent Executor" project
- One active optimization direction: bringing data locality into the scheduler core, so agent state and scheduling decisions are co-located to reduce overhead

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
- [Agent Sandbox — Official Documentation](https://agent-sandbox.sigs.k8s.io/docs) — full CRD reference, SDK docs, use-case guides, runtime templates; CC BY 4.0
- [Agent Sandbox — GitHub (kubernetes-sigs)](https://github.com/kubernetes-sigs/agent-sandbox) — source repository; last updated April 2026
