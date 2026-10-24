---
type: Reference
title: OpenShell (NVIDIA)
description: "OpenShell is an Apache-2.0 open-source runtime from NVIDIA that runs autonomous AI agents in sandboxes whose filesystem, network, and process access is governed by declared policies, with credentials injected only at approved endpoints"
tags: [security, sandboxing, agentic-ai]
timestamp: 2026-10-24T00:00:00Z
---
# OpenShell (NVIDIA)

## Overview

OpenShell describes itself as "the safe, private runtime for fleets of autonomous AI agents." Operators declare in a policy what each agent may access, and OpenShell enforces that policy around the agent's sandbox. It sits in the **sandboxing and execution-governance** layer of the agent stack: it is neither an agent framework nor a model provider, and it does not decide what an agent should do. Its role is to bound what the agent can touch and to keep credentials out of the agent's reach.

The project is relevant to the wider [agent sandboxing](agent-sandboxing.md) discussion because it combines three controls that are often treated separately: kernel-level enforcement, a declarative policy model, and credential brokering.

## Key Concepts / Architecture

The README names five parts. The page points to NVIDIA's architecture documentation for how they fit together, and does not describe the supervisor component in detail.

| Component | Role |
|---|---|
| **Gateway** | Control plane for sandboxes, policy, and access |
| **Supervisor** | Named in the README; its function is not described on the project page |
| **Sandboxes** | Isolated environments for agents, covering images, runtimes, GPU access, and lifecycle |
| **Policies** | Filesystem, network, and process rules, reviewed with an advisor and a prover before they take effect |
| **Providers** | Credentials that are applied only to requests bound for approved endpoints, including inference endpoints |

Extensibility is described through middleware, interceptors, and compute drivers.

## Enforcement and Policy Model

- **Kernel-level enforcement.** The README says OpenShell "instruments the kernel to enforce policy on every file access, system call, and network connection at runtime."
- **Credential isolation.** The README states that agents never see real credentials, and that OpenShell adds them only to requests bound for approved endpoints. This is the same pattern that [Agent Substrate](../Standards/k8s-agent-sandbox.md#agent-substrate-new-separate-open-source-project) describes for its egress gateway.
- **Verified policy changes.** Before a policy change is applied, the README says the project "uses formal verification to check what a policy change would allow," and risky changes wait for human review. The page does not describe the verification method, so treat this as the project's claim rather than an independently checked property.

## Platforms and Deployment

- **Host platforms.** Linux, macOS on Apple Silicon, and Windows through WSL 2 (experimental). Docker, Podman, or host virtualization is required.
- **Kubernetes.** Deployable with Helm. The cluster's CNI must enforce `NetworkPolicy`.
- **Agents.** The default sandbox image contains no agent. The quickstart runs OpenCode against a free OpenRouter model. The page gives no full list of supported agents.
- **SDKs.** Python, TypeScript, Go, and Rust. The OpenClaw platform lists OpenShell as one of its sandbox backends alongside Docker and SSH (see [OpenClaw](../AgentPlatforms/openclaw.md)).
- **Telemetry.** Anonymous operational telemetry is on by default. It can be disabled with `OPENSHELL_TELEMETRY_ENABLED=false` on the gateway, or with `server.telemetryEnabled=false` in the Helm values.

## Maturity and Licensing

- **License:** Apache License 2.0.
- **Version:** The documentation refers to OpenShell 0.1.x and includes a 0.1.0 upgrade guide. Treat the API surface as early.
- **Community:** At capture, the GitHub repository showed about 18.9k stars, 1.9k forks, 377 open issues, and 199 open pull requests.
- **Warranty:** The README states the software is provided "AS IS", without warranty of any kind.

## Considerations

- The security properties are the project's own claims. Evaluate the kernel enforcement, policy verification, and credential isolation against your threat model before relying on them.
- Telemetry is on by default. Teams with data-residency constraints should disable it explicitly.
- Experimental Windows support and a 0.1.x version line indicate that operational practice is still forming.

## See Also

- [Agent Sandboxing](agent-sandboxing.md) — isolation tiers and the general sandboxing guidance this runtime is one implementation of
- [Anthropic Sandbox Runtime (srt)](anthropic-sandbox-runtime.md) — OS-level process sandboxing for MCP servers, an alternative at a lighter isolation tier
- [Agent Governance Toolkit](agent-governance-toolkit.md) — policy-engine governance that operates at the agent-action layer
- [Kubernetes Agent Sandbox](../Standards/k8s-agent-sandbox.md) — Kubernetes-native sandbox API for agent tool-call execution
- [OpenClaw](../AgentPlatforms/openclaw.md) — a personal agent platform that lists OpenShell as a sandbox backend
- [Agent Harness](../AgentHarness/agent-harness.md) — where sandboxed execution fits in the harness

## References

- [NVIDIA/OpenShell — GitHub repository](https://github.com/NVIDIA/OpenShell) — README, license, and component overview
- [OpenShell documentation](https://docs.nvidia.com/openshell/latest/) — main documentation set
- [OpenShell architecture](https://docs.nvidia.com/openshell/latest/about/architecture) — how the gateway, sandboxes, policies, and providers fit together
- [OpenShell support matrix](https://docs.nvidia.com/openshell/latest/about/support-matrix) — supported platforms
