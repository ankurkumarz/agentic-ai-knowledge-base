# Microsoft Agent Governance Toolkit

## Overview

The **Agent Governance Toolkit (AGT)** is an open-source, MIT-licensed runtime governance framework from Microsoft that enforces deterministic policy over autonomous AI agents. Unlike prompt-based safety approaches, AGT intercepts every tool call, resource access, and inter-agent message at the middleware layer and evaluates it against policy *before* execution. The project covers all 10 OWASP Agentic Top 10 risks and ships with 13,000+ tests across 10 formal RFC 2119-compliant specifications.

## Key Components

### Policy Engine

AGT's core is a deterministic allow/deny policy evaluator with sub-millisecond latency (0.012 ms p50 for single rules, 35,000 concurrent operations/second). Three policy languages are supported:

| Language | Best For |
|---|---|
| YAML | Simple allow/deny rules; human-readable |
| OPA/Rego | Complex logic, attribute-based access control |
| Cedar | Formal verification, regulatory compliance scenarios |

The engine is **fail-closed** by design: any evaluation error results in denial. Policy violations achieve 0.00% pass-through rates in reported benchmarks — a result prompt-based safety cannot match deterministically.

### Zero-Trust Identity (AgentMesh)

Every agent receives cryptographic credentials rather than relying on ambient trust:

- **Ed25519** signatures for standard deployments
- **ML-DSA-65** (post-quantum lattice-based) for quantum-safe environments
- **Behavioral trust score** (0–1000 scale) that decays when anomalous actions are detected
- **SPIFFE/SVID** compatibility for integration with existing service-mesh identity systems
- **Trust ceiling propagation**: a delegated agent cannot exceed the trust level of its parent, preventing privilege escalation through chains

### Execution Sandboxing (Agent Hypervisor)

Inspired by hardware privilege rings, AGT implements four isolation levels:

| Ring | Name | Description |
|---|---|---|
| 0 | Kernel | Governance infrastructure only |
| 1 | Supervisor | Orchestration layer |
| 2 | User | Standard agent workloads |
| 3 | Untrusted | External/third-party agent code |

Multi-step workflows use **Saga orchestration** with automatic compensation — if a workflow step fails or is denied, preceding steps are rolled back. A **kill switch** capability enables immediate agent termination across the fleet.

### MCP Security Gateway

Purpose-built protection for Model Context Protocol tool integrations:

- **Tool poisoning detection**: flags tools with malicious instructions embedded in descriptions
- **Description drift monitoring**: alerts when a tool's description changes between invocations
- **Typosquatting checks**: catches tool names designed to impersonate trusted tools
- **Hidden instruction scanning**: detects invisible or obfuscated instructions in MCP tool metadata

### Agent SRE (Site Reliability Engineering)

AGT applies SRE practices to autonomous agent fleets:

- **SLOs and error budgets** per agent type
- **Circuit breakers** that halt runaway agents before cascading failures propagate
- **Replay debugging**: reconstruct the exact sequence of events that led to a failure
- **Chaos engineering** hooks for controlled fault injection during testing
- **OpenTelemetry-native** observability with governance events emitted as structured traces

### Audit and Compliance

| Capability | Detail |
|---|---|
| Tamper-evident logs | Merkle-chained audit trail; entries cannot be altered without detection |
| Decision BOM | Full "bill of materials" reconstruction for any governance decision |
| Regulatory mapping | Automated compliance evidence for EU AI Act, SOC 2, HIPAA, GDPR |
| SIEM export | CloudEvents format for ingestion by Splunk, Sentinel, Datadog, etc. |

## OWASP Agentic Top 10 Coverage

AGT explicitly maps its controls to all 10 OWASP Agentic risks:

| OWASP Risk | AGT Control |
|---|---|
| Agent Goal Hijacking | Policy engine blocks unauthorized goal modification |
| Excessive Capabilities | Least-privilege enforcement via per-agent tool allowlists |
| Identity & Privilege Abuse | Zero-trust credentials with behavioral trust scoring |
| Uncontrolled Code Execution | Execution ring isolation and sandboxed containers |
| Insecure Output Handling | Content validation policies on agent outputs |
| Memory Poisoning | Episodic memory integrity checks on write operations |
| Unsafe Inter-Agent Communications | Encrypted channels with trust-gated message routing |
| Cascading Failures | Circuit breakers and SLO enforcement across the fleet |
| Human-Agent Trust Deficit | Merkle-chained audit trails and flight recorder capability |
| Rogue Agents | Kill switch, ring 3 isolation, and anomaly-triggered quarantine |

## Framework Integration

AGT ships adapters for 20+ frameworks, enabling governance without rewriting agent code:

- LangChain / LangGraph
- AutoGen
- CrewAI
- OpenAI Agents SDK
- Semantic Kernel
- Google ADK
- LlamaIndex
- Dify

Multi-language SDKs are available for Python, TypeScript, .NET, Rust, and Go.

## Conformance Testing

AGT's 992 conformance tests map to 10 formal specifications:

| Specification | Tests |
|---|---|
| Agent OS Policy Engine | 68 |
| AgentMesh Identity/Trust | 135 |
| Agent Hypervisor Execution | 80 |
| MCP Security Gateway | 127 |
| Audit/Compliance | 157 |
| Framework Adapter Contract | 152 |

Security tooling includes CodeQL (Python/TypeScript SAST), Gitleaks (secret scanning), ClusterFuzzLite (7 fuzz targets), and Dependabot across 13 package ecosystems.

## Honest Design Boundaries

AGT enforces governance at the Python middleware layer, not the OS kernel level. The project documentation explicitly recommends running agents in separate containers for OS-level isolation. The toolkit is production-quality (v3.7.0, Microsoft-signed releases) but is in **public preview** as of 2026.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Policy language selection | Teams new to policy-as-code may find Rego complex | Start with YAML rules for simple cases; migrate to Cedar when formal verification is needed |
| Fail-closed vs. fail-open | Errors in policy evaluation can halt agents unexpectedly | Accept fail-closed behavior; build robust policy rule sets and test with conformance suite before production |
| Trust score decay | Anomaly detection penalizes trust score but does not explain *why* | Instrument trust score changes via OpenTelemetry traces; set SLO alerts on trust score thresholds |
| Saga compensation | Automatic rollback may leave partial state in external systems | Test compensation paths with chaos engineering hooks; design external operations to be idempotent |
| MCP tool drift | Description drift monitoring may flag legitimate tool updates | Pin tool versions in policy; use staging environment to validate MCP tool updates before promoting |
| Quantum-safe migration | ML-DSA-65 is more CPU-intensive than Ed25519 | Enable quantum-safe mode selectively for high-assurance agents; benchmark overhead before fleet-wide rollout |

## See Also

- [Security Frameworks Overview](./Readme.md)
- [NIST AI RMF](./nist-ai-rmf.md)
- [Google SAIF](./google-saif.md)
- [Agent Security (Production Best Practices)](../ProductionBestPractices/security.md)
- [MCP Standard](../Standards/mcp.md)
- [Microsoft — Agentic AI Overview](../AllThingsMicrosoft/README.md)
- [AI Governance Solutions](../AIGovernance/governance-solutions.md)
- [Multi-Agent System Architecture](../Architecture/multi-agent-system.md)
- [Agent Observability](../Observability/Readme.md)

## References

- [agent-governance-toolkit (GitHub)](https://github.com/microsoft/agent-governance-toolkit) — MIT-licensed runtime governance framework from Microsoft; public preview as of 2026
