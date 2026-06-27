# Agent Sandboxing

## Overview

Sandboxing is the practice of running agent-invoked code or tools in an isolated execution environment that constrains what resources the process can access. As agents increasingly execute arbitrary code, invoke third-party MCP servers, and operate multi-step tool chains, sandboxing becomes a foundational security control — limiting the blast radius of a compromised tool, a malicious prompt injection payload, or an unintended side effect.

The core guarantee a sandbox provides: **a process running inside it cannot access filesystem paths, network endpoints, or system calls that the sandbox policy does not explicitly allow**, regardless of what instructions it receives at runtime.

## Isolation Taxonomy

Agent sandboxes exist across four tiers, trading isolation strength against startup speed and operational complexity:

| Tier | Mechanism | Isolation Strength | Startup Speed | Examples |
|---|---|---|---|---|
| **OS-level policy** | Kernel syscall filters, seccomp, Seatbelt, namespace jails | Medium | <10 ms | srt, nsjail, bubblewrap |
| **Container** | Linux namespaces + cgroups; shared host kernel | Medium | <100 ms | Docker, gVisor (userspace kernel overlay) |
| **MicroVM** | Hardware virtualization (KVM); minimal guest kernel | High | 100–500 ms | Firecracker, Kata Containers |
| **Cloud-hosted sandbox** | Managed sandbox-as-a-service; isolation handled by provider | High (opaque) | <1 s (warm) | E2B, Daytona, Modal |

Choosing a tier is primarily a tradeoff between the **trust level** of the code being executed and the **latency budget** of the agent workflow.

## Solution Landscape

### Cloud-Hosted Sandboxes

Managed services that provide on-demand isolated execution environments via API. The provider owns the isolation layer; teams consume sandboxes as a primitive.

#### E2B

[E2B](https://github.com/e2b-dev/e2b) is an open-source infrastructure platform for running AI-generated code in secure, isolated cloud sandboxes. Agents start a sandbox, execute commands or code via SDK, and destroy it when done — the provider handles all isolation.

| Attribute | Detail |
|---|---|
| Deployment model | Cloud (AWS, GCP); self-hostable via Terraform |
| SDK languages | Python, TypeScript/JavaScript |
| Primary use case | AI code interpreter; executing untrusted LLM-generated code |
| GitHub stars | ~12.4k |
| License | Open-source (Apache-2.0 core) |

- **Strengths**: Simple API; no infrastructure knowledge required; purpose-built for AI agent code execution
- **Limitations**: Cloud dependency; limited control over the underlying isolation mechanism; potential cold-start latency

#### Daytona

[Daytona](https://github.com/daytonaio/daytona) provides "secure and elastic infrastructure runtime for AI-generated code execution and agent workflows." Each sandbox is a fully isolated computer with a dedicated kernel, filesystem, network stack, and allocated vCPU/RAM/disk.

| Attribute | Detail |
|---|---|
| Deployment model | Cloud; open-source self-hostable |
| SDK languages | Python, TypeScript, Ruby, Go, Java |
| Startup time | < 90 ms |
| Isolation | Dedicated kernel + filesystem per sandbox; stateful snapshots |
| Primary use case | Agent workflows requiring persistent state across steps |

- **Strengths**: True kernel isolation; stateful environment snapshots for multi-step agents; broad SDK coverage; OCI/Docker compatible
- **Limitations**: Heavier than OS-level sandboxes; self-hosting adds operational burden

#### Modal

[Modal](https://modal.com) is a cloud execution platform targeting ML/AI workloads. It runs Python functions in isolated containers with GPU access, and is commonly used to give agents access to compute-intensive tools (model inference, batch jobs) in a sandboxed environment.

| Attribute | Detail |
|---|---|
| Deployment model | Fully managed cloud |
| Primary language | Python |
| Isolation | Container-based; hardware-isolated per job |
| Key differentiator | GPU support; fast cold-start; pay-per-use |
| Primary use case | Compute-intensive agent tools; model inference sandboxing |

- **Strengths**: GPU access; low operational overhead; per-invocation billing
- **Limitations**: Python-centric; less control over network policy compared to lower-level tools

#### AWS Lambda MicroVMs

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) executes every function invocation inside a dedicated Firecracker microVM (see [Firecracker](#firecracker-aws) below), giving agent tool calls hardware-virtualization-level isolation without managing VMs directly. As a managed cloud sandbox it sits alongside E2B, Daytona, and Modal — the isolation mechanism is the same microVM tier as raw Firecracker, but consumed as a fully managed, pay-per-invocation service rather than self-operated infrastructure.

| Attribute | Detail |
|---|---|
| Deployment model | Fully managed cloud (AWS) |
| Isolation mechanism | Firecracker microVM per invocation |
| Max runtime | Up to 8 hours per invocation |
| Max memory | Up to 10 GB (aligned to standard Lambda limits) |
| Cold start overhead | ~100–200 ms added vs. standard Lambda cold start |
| Burst scaling | Up to 4x vertical burst scaling |
| Lifecycle control | Configurable auto-suspend and auto-resume |

- **Strengths**: No infrastructure to operate; integrates directly with the broader AWS agent stack (Bedrock AgentCore, Step Functions); auto-suspend/resume reduces idle cost for long-running agent sessions
- **Limitations**: AWS-only; the added cold-start overhead versus standard Lambda matters for latency-sensitive single-tool-call agent loops
- **Agent relevance**: Suitable for AWS-native agent platforms needing per-invocation hardware isolation for tool execution without standing up Firecracker themselves

---

### Infrastructure Primitives

Lower-level tools that implement isolation via OS or hypervisor mechanisms. These form the foundation that cloud-hosted services build on top of, and can be used directly when fine-grained policy control is needed.

#### Anthropic Sandbox Runtime (srt)

[srt](https://github.com/anthropic-experimental/sandbox-runtime) enforces filesystem and network restrictions at the OS level without a container. Its primary use case is wrapping individual MCP server processes in a least-privilege policy envelope.

| Attribute | Detail |
|---|---|
| Tier | OS-level policy |
| macOS mechanism | `sandbox-exec` with dynamically generated Seatbelt profiles |
| Linux mechanism | `bubblewrap` with network namespace isolation |
| Network filtering | HTTP and SOCKS5 proxies; allow-list only |
| Install | `npm install -g @anthropic-ai/sandbox-runtime` |
| License | Apache-2.0 |

See [Anthropic Sandbox Runtime](./anthropic-sandbox-runtime.md) for full detail.

#### Firecracker (AWS)

[Firecracker](https://github.com/firecracker-microvm/firecracker) is a virtual machine monitor (VMM) that uses KVM to create microVMs. It powers AWS Lambda and AWS Fargate. Each microVM boots in milliseconds, has a minimal attack surface (no unnecessary devices), and is isolated at the hardware virtualization boundary.

| Attribute | Detail |
|---|---|
| Tier | MicroVM |
| Isolation mechanism | KVM hardware virtualization + seccomp filters + Jailer (cgroup/namespace) |
| Startup time | ~125 ms (cold), < 5 ms (restored snapshots) |
| Default resources | 1 vCPU, 128 MiB RAM (configurable) |
| License | Apache-2.0 |
| Adoption | Powers AWS Lambda and AWS Fargate |

- **Strengths**: Near-VM isolation with near-container startup speed; used at massive scale; snapshot/restore support
- **Limitations**: Linux KVM host required; not a drop-in container replacement; operational complexity
- **Agent relevance**: Suitable for per-agent-run microVM isolation where strong multi-tenant security is required

#### gVisor (Google)

[gVisor](https://github.com/google/gvisor) is an application kernel written in Go that runs in userspace and intercepts system calls before they reach the host kernel. Its OCI runtime (`runsc`) integrates with Docker and Kubernetes as a drop-in replacement for `runc`.

| Attribute | Detail |
|---|---|
| Tier | Container (userspace kernel overlay) |
| Isolation mechanism | Syscall interception and re-implementation in Go (Sentry + Gofer processes) |
| Container integration | OCI-compatible; `runsc` runtime for Docker/Kubernetes |
| Performance overhead | 10–30% for syscall-heavy workloads |
| License | Apache-2.0 |
| Adoption | Used in Google Cloud Run, GKE Sandbox |

- **Strengths**: Strong reduction in host kernel attack surface vs. standard containers; OCI-compatible; no hardware virtualization required
- **Limitations**: Performance penalty from syscall interception; some Linux syscalls not yet implemented
- **Agent relevance**: Drop-in hardening for containerized agent tools in Kubernetes clusters; used in Cloud Run for agent deployments

#### Kata Containers

[Kata Containers](https://github.com/kata-containers/kata-containers) wraps each container in a lightweight VM using hardware virtualization (Intel VT-x, AMD SVM, ARM Hyp), combining VM-grade isolation with container-like operations. It implements the containerd shimv2 API, making it transparent to container orchestrators.

| Attribute | Detail |
|---|---|
| Tier | MicroVM (container-wrapped) |
| Isolation mechanism | Hypervisor-based (supports QEMU, Cloud Hypervisor, Firecracker as VMM) |
| Container integration | containerd shimv2; OCI-compatible |
| Multi-arch | x86_64, aarch64, ppc64le, s390x |
| License | Apache-2.0 |

- **Strengths**: VM-grade isolation with Kubernetes-native operation; supports Firecracker as the underlying VMM for ultra-fast boot
- **Limitations**: Requires hardware virtualization support; higher resource overhead than gVisor
- **Agent relevance**: Suitable for multi-tenant agent platforms where Kubernetes is the orchestration layer and strong workload separation is required

#### nsjail (Google)

[nsjail](https://github.com/google/nsjail) is a lightweight process isolation tool using Linux namespaces, cgroup, and seccomp-bpf. Used by Google's infrastructure to sandbox arbitrary processes with fine-grained policy control.

| Attribute | Detail |
|---|---|
| Tier | OS-level policy |
| Isolation mechanism | Linux namespaces (PID, network, mount, UTS, IPC) + cgroups + seccomp-bpf |
| Deployment | Linux only; binary or Docker-based |
| License | Apache-2.0 |

- **Strengths**: Very low overhead; fine-grained syscall policy; no daemon required
- **Limitations**: Linux only; requires familiarity with seccomp policy authoring; less MCP-specific tooling than `srt`
- **Agent relevance**: Appropriate for sandboxing agent-invoked shell scripts or CLI tools on Linux hosts where container overhead is unacceptable

---

## Comparison Summary

| Solution | Type | Startup | Isolation Level | Agent-Native | OS Support | License |
|---|---|---|---|---|---|---|
| **E2B** | Cloud SaaS | < 1 s (warm) | High (provider-managed) | Yes — code interpreter focus | Cloud | Apache-2.0 |
| **Daytona** | Cloud / OSS | < 90 ms | High (dedicated kernel) | Yes — agent workflow focus | Cloud | Apache-2.0 |
| **Modal** | Cloud SaaS | < 1 s (warm) | Medium–High (container) | Partial — compute focus | Cloud | Proprietary |
| **AWS Lambda MicroVMs** | Cloud (managed) | ~100–200 ms added cold start | Very High (Firecracker microVM) | Partial — general serverless, AWS-native agent stacks | Cloud (AWS) | Proprietary (managed service) |
| **Anthropic srt** | OS-level | < 10 ms | Medium (policy-based) | Yes — MCP server focus | macOS, Linux | Apache-2.0 |
| **Firecracker** | MicroVM | ~125 ms | Very High (KVM) | No — infrastructure primitive | Linux (KVM) | Apache-2.0 |
| **gVisor** | Container (userspace kernel) | < 100 ms | High (syscall interception) | No — infrastructure primitive | Linux | Apache-2.0 |
| **Kata Containers** | MicroVM + Container | ~200–500 ms | Very High (hypervisor) | No — infrastructure primitive | Linux | Apache-2.0 |
| **nsjail** | OS-level | < 10 ms | Medium (namespace+seccomp) | No — general-purpose | Linux | Apache-2.0 |
| **Docker (standard)** | Container | < 100 ms | Low–Medium (namespaces) | No — general-purpose | Linux, macOS, Windows | Apache-2.0 |

## Selection Guide

| Requirement | Recommended Approach |
|---|---|
| Sandbox individual MCP server processes on a developer machine | Anthropic srt (`npm install -g @anthropic-ai/sandbox-runtime`) |
| Execute AI-generated code in cloud with minimal setup | E2B (SDK-first, cloud-native) |
| Multi-step agent workflows with persistent state across steps | Daytona (stateful snapshots, dedicated kernel) |
| Compute-intensive agent tools (GPU, ML inference) | Modal |
| Multi-tenant Kubernetes agent platform needing VM-grade isolation | gVisor (drop-in) or Kata Containers (stronger) |
| Serverless agent invocations at scale (own AWS infrastructure) | Firecracker microVMs |
| Serverless agent invocations on AWS without operating Firecracker directly | AWS Lambda (managed microVM per invocation, configurable auto-suspend/resume) |
| Sandboxing CLI tools / shell commands on Linux with zero overhead | nsjail |
| Rapid prototype; already using Docker | Docker + resource limits (lowest bar; not sufficient for high-trust scenarios) |

## Best Practices

| Challenge | Description | Solution |
|---|---|---|
| Choosing isolation tier | Mismatch between threat model and sandbox strength | Map trust level of code to isolation tier: dev tooling → OS-level; untrusted user code → microVM or cloud-hosted |
| Sandbox escape via network | A sandboxed process phones home or exfiltrates data | Apply allow-list network policy at every tier; use proxy-based filtering (srt, Daytona) |
| Cold-start latency in agent loops | Spinning up a new sandbox per tool call adds hundreds of ms | Use warm sandbox pools (E2B, Daytona) or snapshot/restore (Firecracker) to amortize startup cost |
| State persistence across agent steps | Agent needs to write a file in step 1 and read it in step 2 | Use stateful sandbox sessions (Daytona snapshots, E2B persistent filesystems) rather than ephemeral per-call sandboxes |
| Observability gap | Sandbox violations and resource usage not visible in agent traces | Pipe sandbox violation logs and resource metrics into your observability stack alongside agent traces |
| Resource exhaustion (CPU/RAM) | Runaway sandbox process consumes host resources | Set hard cgroup limits (CPU, memory, disk I/O) at the sandbox layer; cloud-hosted services handle this automatically |
| Credential leakage into sandbox | Secrets injected into sandbox environment variables can be exfiltrated | Never inject long-lived credentials; use IAM role-based short-lived tokens; restrict sandbox network egress to prevent exfiltration |
| Over-trusting containers | Standard Docker containers share the host kernel; a kernel exploit breaks isolation | Upgrade to gVisor or Kata Containers for untrusted code; reserve plain Docker for fully-trusted internal tools only |

## Relationship to Other Security Controls

Sandboxing addresses **execution isolation** — it constrains what a running process can do. It is one layer in a defense-in-depth posture and does not replace:

- **Input filtering** — prompt injection defense before code reaches the sandbox
- **Output filtering** — screening tool responses for PII or exfiltrated content before returning to the agent
- **Identity and least-privilege access** — the agent's credentials should be scoped regardless of the sandbox
- **Policy engines** — deterministic pre-execution policy checks (e.g., Microsoft AGT) applied above the OS layer
- **Audit logging** — every sandbox invocation should be recorded alongside the agent trace

## See Also

- [Anthropic Sandbox Runtime](./anthropic-sandbox-runtime.md)
- [Agent Security — Production Best Practices](../ProductionBestPractices/security.md)
- [Agentic AI Security Overview](./Readme.md)
- [Agent Governance Toolkit (Microsoft)](./agent-governance-toolkit.md)
- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Architecture Components Selection](../Architecture/components-selection.md)
- [AgentOps — Deployment](../ProductionBestPractices/deployment.md)
- [AWS — Agentic AI Overview](../AllThingsAWS/README.md)

## References

- [E2B GitHub](https://github.com/e2b-dev/e2b) — Open-source cloud sandbox infrastructure for AI-generated code; ~12.4k stars; Apache-2.0
- [Daytona GitHub](https://github.com/daytonaio/daytona) — Secure, elastic sandbox runtime for agent workflows; dedicated kernel per sandbox; Apache-2.0
- [Anthropic Sandbox Runtime](https://github.com/anthropic-experimental/sandbox-runtime) — OS-level MCP server sandboxing via Seatbelt/bubblewrap; ~4.1k stars; Apache-2.0
- [Firecracker GitHub](https://github.com/firecracker-microvm/firecracker) — AWS microVM VMM using KVM; powers Lambda and Fargate; Apache-2.0
- [gVisor GitHub](https://github.com/google/gvisor) — Google userspace application kernel for container sandboxing; OCI-compatible; Apache-2.0
- [Kata Containers GitHub](https://github.com/kata-containers/kata-containers) — VM-wrapped containers using hardware virtualization; containerd shimv2; Apache-2.0
- [nsjail GitHub](https://github.com/google/nsjail) — Google lightweight Linux namespace+seccomp process isolation tool; Apache-2.0
- [AWS Lambda MicroVMs Guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) — AWS documentation on Firecracker microVM isolation per Lambda invocation, runtime/memory limits, and lifecycle controls
