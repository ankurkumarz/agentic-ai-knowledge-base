# Agent Security

Agentic AI systems introduce security risks that don't exist in traditional software. Agents can take real-world actions, access sensitive data, and be manipulated through their inputs. Security must be designed in from the start, not bolted on.

## Overview

![Google AI agent security risks and principles](../assets/images/security-google-agent-risks-principles.png)

The two primary risk categories for agentic systems:

- **Rogue actions**: Agents taking unauthorized, harmful, or unintended actions in external systems
- **Sensitive data disclosure**: Agents inadvertently exposing confidential information through outputs or tool calls

Google's three-layer defense model addresses both:

1. **Policy Definition** — System instructions define the agent's constitution: what it can and cannot do
2. **Guardrails & Filtering** — Input classifiers block malicious prompts; output filters catch PII and policy violations; HITL escalation for high-risk actions
3. **Monitoring & Response** — Continuous behavioral monitoring with automated anomaly response

## Best Practices

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Prompt injection | Malicious content in retrieved documents or user inputs hijacks agent behavior | Trusted all inputs equally; agents executed injected instructions | Treat user input and retrieved content as untrusted; use input classifiers (e.g., Perspective API) before passing to agent |
| Overprivileged agents | Agents granted broad tool access use capabilities beyond their intended scope | Gave agents all tools for flexibility; scope creep led to unintended actions | Apply principle of least privilege — grant only the tools and permissions required for the specific task; in multi-agent systems, use AWS STS to generate time-limited, scoped credentials per task |
| Prompt injection propagation in multi-agent systems | Malicious content processed by one agent is forwarded to the next, compounding the attack | Trusted content that had already passed through one agent; downstream agents executed injected instructions | Treat all externally-originated content as untrusted regardless of how many agents have processed it; apply Amazon Bedrock Guardrails at every agent boundary, not just the entry point |
| Credential exposure in agent payloads | Raw credentials passed in task objects between agents get logged or leaked | Included API keys in handoff payloads for convenience; appeared in traces and DynamoDB records | Never pass raw credentials in task objects; use IAM role-based delegation; AWS IAM Roles Anywhere for non-AWS workloads |
| Unauthorized agent discovery | Agents in an A2A network can be discovered and invoked by unauthorized callers | Relied on obscurity for agent endpoints; no authentication on agent card endpoints | Implement agent card registry with authentication requirements; apply Amazon Bedrock Guardrails at every A2A boundary |
| Sensitive data in tool outputs | Tool responses containing PII or secrets get included in agent context and logs | Logged all tool outputs for debugging; exposed sensitive data in observability store | Implement output filtering on tool responses; mask PII before writing to traces or memory |
| Uncontrolled autonomous actions | Agents take irreversible real-world actions (send email, delete records) without confirmation | Allowed full autonomy for efficiency; caused accidental data loss and unwanted communications | Require human-in-the-loop confirmation for irreversible or high-impact actions; implement action dry-run mode |
| Tool risk not rated | All agent tools treated equally regardless of reversibility, access level, or financial impact | High-risk write tools called without extra scrutiny; caused unintended transactions | Assign each tool a risk rating (low/medium/high) based on read-only vs. write access, reversibility, account permissions, and financial impact; trigger guardrail checks or HITL before high-risk tool calls (OpenAI Agents SDK tool safeguards pattern) |
| Lack of audit trail | No record of what actions an agent took and why | Relied on application logs; couldn't reconstruct agent decision paths for compliance | Log every tool call with inputs, outputs, agent reasoning, and user context; maintain immutable audit trail |
| Model poisoning via RAG | Adversarial documents in the knowledge base manipulate agent behavior | Ingested all documents without validation; poisoned knowledge base affected all users | Validate and sanitize documents before ingestion; implement content moderation on knowledge base updates |
| Credential exposure | API keys and secrets passed through agent context get logged or leaked | Stored credentials in system prompts for convenience; appeared in traces | Use secrets management (AWS Secrets Manager, Vault); inject credentials at runtime via secure environment, never in prompts |
| Cross-tenant data leakage | In multi-tenant deployments, one user's context bleeds into another's | Shared memory and tool caches across users; namespace collisions occurred | Enforce strict tenant isolation in all memory stores, caches, and tool configurations; audit access patterns regularly |
| Compromised agent in a multi-agent mesh | A compromised agent sends malicious payloads to peers, spreading the attack laterally | Trusted all inter-agent messages as internal; one compromised node propagated injected content to others | **Agent Mesh Defense** pattern: route all inter-agent communication through a firewall agent that validates message schemas and enforces policy before forwarding; treat every agent boundary as a trust boundary |
| Adversarial instruction injection | Malicious inputs in retrieved content redirect an agent to ignore its own constraints — a silent override | No self-monitoring; agent executed injected instructions silently alongside legitimate ones | **Agent Self-Defense** pattern: maintain an internal anomaly-detection layer that flags instruction patterns attempting to override system constraints; agent refuses and alerts rather than executing |
| Uncontrolled code execution side effects | An agent executing code or calling external APIs causes unintended side effects on shared infrastructure | Ran agent tasks in shared process with full I/O access; one runaway agent corrupted shared state | **Execution Envelope Isolation (Sandboxing)**: isolate agent code execution in a container or VM with enforced resource limits and restricted I/O; use ephemeral execution contexts destroyed after task completion |
| No deterministic policy enforcement | Prompt-based safety instructions can be bypassed; cannot guarantee 0% violation rate | Relied on system prompt rules; adversarial inputs circumvented them | Use a middleware policy engine (e.g., Microsoft AGT) that evaluates YAML/OPA/Cedar rules before execution; fail-closed design ensures errors result in denial rather than pass-through |
| Privilege escalation through agent delegation | A lower-trust delegated agent inherits excessive permissions from its orchestrator | Forwarded full credentials to sub-agents for convenience; compromised sub-agent gained orchestrator-level access | Apply trust ceiling propagation: delegated agents cannot exceed parent trust level; use scoped, time-limited credentials per task |
| MCP tool tampering | Tool descriptions in Model Context Protocol integrations are modified to inject hidden instructions | Trusted MCP tool metadata without verification; agent executed poisoned tool logic | Deploy an MCP Security Gateway layer that monitors for description drift, typosquatting, and hidden instruction patterns on every tool invocation |
| MCP server over-privilege | MCP servers run as host OS processes with invoking user's permissions; a compromised server can read arbitrary files or phone home | Relied on trust in third-party MCP server code; no OS-level restriction | Wrap each MCP server process with [Anthropic Sandbox Runtime (`srt`)](../SecurityFrameworks/anthropic-sandbox-runtime.md) to enforce an explicit filesystem + network allowlist at OS level (macOS Seatbelt / Linux bubblewrap) |
| Malicious skills in the supply chain | Agent skills fetched from external sources may embed prompt injection, data exfiltration, or malicious code patterns; research shows 26.1% of skills contain vulnerabilities | Installed third-party skills without vetting; trusted source repo as sufficient guarantee | Scan all externally-sourced skills before installation using [Cisco Skill Scanner](../SecurityFrameworks/skill-scanners.md) or [NVIDIA SkillSpector](../SecurityFrameworks/skill-scanners.md); integrate SARIF output into GitHub Code Scanning to block unsafe skills at PR time |
| Sensitive data exposure in event-driven agent pipelines | Agents consuming/producing events across a shared data streaming platform can expose regulated or confidential fields to unauthorized consumers of the same topic | Relied on topic-level access control only; any consumer with topic access could read all fields | Enforce field-level encryption and access control on event payloads; apply Stream Governance (data lineage and quality policies) across the pipeline; set fine-grained, regulation-aligned (e.g., GDPR) retention policies per topic rather than a single global retention setting (Confluent, 2025) |

## Layered Guardrail Taxonomy

Defense-in-depth for agentic systems requires guardrails at every stage of the loop, not only at input:

| Layer | Where Applied | What It Checks |
|---|---|---|
| Input guardrails | Before the agent receives a request | Reject or route unsafe user requests |
| Context guardrails | During context assembly | Label untrusted content; redact secrets before they enter the model |
| Schema guardrails | On tool arguments | Force structured inputs and outputs; reject malformed calls |
| Tool guardrails | Around execution | Validate args and results; bound result size; redact sensitive data |
| Permission guardrails | Before side effects | Approve, deny, or pause based on risk class |
| Output guardrails | Before user-visible response | Check final answer for PII, unsafe content, false claims |
| Trace guardrails | After the run | Grade tool calls and decisions; detect anomalies retrospectively |

Each guardrail should be fast, specific, and independently testable.

## Approval Record Format

High-risk actions must pause the loop and emit a structured approval record stored outside the model context. The model must never approve its own actions.

**Approval request:**
```json
{
  "approval_type": "external_send",
  "action": "send_email",
  "target": "customer@example.com",
  "risk": "external_communication",
  "preview_ref": "artifact://drafts/email_123",
  "expected_result": "Customer receives renewal reminder.",
  "rollback": "Cannot unsend; follow-up correction possible.",
  "scope": "single_send_only"
}
```

**Approval result:**
```json
{
  "status": "approved",
  "approved_by": "user_id",
  "timestamp": "...",
  "scope": "single_send_only",
  "expires_at": "..."
}
```

Approval must be scoped to the exact action and plan version. Vague consent is not blanket authorization. Approval records must survive context compaction — store them in durable state, not only in the prompt.

## Security Frameworks Reference

| Framework | Provider | Key Focus |
|---|---|---|
| [NIST AI RMF](https://doi.org/10.6028/NIST.AI.100-1) | NIST | Risk-based governance across the full AI lifecycle (Govern, Map, Measure, Manage) |
| [SAIF](https://safety.google/safety/saif/) | Google | Secure foundation, development, deployment, and operations for AI systems |
| [Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/security/generative-ai-scoping-matrix/) | AWS | Security controls mapped to FM application types across the AI lifecycle |
| [Agent Governance Toolkit](../SecurityFrameworks/agent-governance-toolkit.md) | Microsoft | Runtime governance: deterministic policy engine (YAML/OPA/Cedar), zero-trust identity, execution rings, MCP security gateway; covers all 10 OWASP Agentic risks |
| [Skill Scanner](../SecurityFrameworks/skill-scanners.md) | Cisco AI Defense | Multi-engine skill security scanner: YAML + YARA + AST taint analysis + LLM consensus; SARIF/GitHub Actions integration |
| [SkillSpector](../SecurityFrameworks/skill-scanners.md) | NVIDIA | Two-stage skill scanner: 64 vulnerability patterns across 16 categories including MCP risks; live OSV.dev CVE lookup; LangGraph pipeline |

## Security Controls by Risk Level

| Risk Level | Example Use Cases | Key Controls |
|---|---|---|
| High | Financial transactions, healthcare, critical infrastructure | Enhanced HITL, strict access controls, real-time monitoring, comprehensive audit trails |
| Medium | Customer service, content generation, business automation | Regular security assessments, standard access controls, monitoring and logging |
| Low | Internal productivity, R&D, educational tools | Basic access controls, standard monitoring, user training |

## Emerging Threats

| Threat | Description | Mitigation |
|---|---|---|
| Prompt injection | Malicious inputs manipulate agent behavior | Input validation, content classifiers, sandboxed execution |
| Model poisoning | Attacks on training data or knowledge base | Secure ingestion pipelines, content moderation, provenance tracking |
| Data extraction | Attempts to extract sensitive training data via crafted prompts | Output filtering, rate limiting, anomaly detection on output patterns |
| Adversarial examples | Inputs designed to cause misclassification or unexpected behavior | Adversarial testing (red teaming), input sanitization, behavioral monitoring |

## Three-Layer Security Defense (Google SAIF Model)

Unlike traditional software on predetermined paths, agents make decisions, interpret ambiguous requests, access multiple tools, and maintain memory across sessions. Google's approach addresses this through three defense layers:

**1. Policy Definition and System Instructions (The Agent's Constitution)**
Define policies for desired and undesired agent behavior. Engineer these into System Instructions (SIs) that act as the agent's core constitution — the first line of defense.

**2. Guardrails, Safeguards, and Filtering (The Enforcement Layer)**
- **Input Filtering**: Use classifiers and services like the Perspective API to analyze and block malicious inputs before they reach the agent
- **Output Filtering**: Pass every agent response through safety filters (e.g., Vertex AI safety filters) to block PII, toxic language, or policy violations before sending to the user
- **HITL Escalation**: For high-risk or ambiguous actions, the system must pause and escalate to human review

**3. Continuous Assurance and Testing (The Adaptive Layer)**
Safety is not a one-time setup. Requires:
- **Rigorous Evaluation**: Any change to the model or safety systems triggers a full re-run of the evaluation pipeline
- **RAI Testing**: NPOV (Neutral Point of View) evaluations, parity evaluations across demographic groups
- **Proactive Red Teaming**: Manually and via AI-driven persona-based simulation

## Security Response Playbook

When a threat is detected in production, the response follows: **contain → triage → resolve**.

1. **Immediate Containment**: Stop the harm using a "circuit breaker" — typically a feature flag to instantly disable the affected tool or capability
2. **Triage**: Route suspicious requests to a HITL review queue to investigate the exploit's scope and impact
3. **Permanent Resolution**: Develop a patch (updated input filter or system prompt), deploy it through the automated CI/CD pipeline — ensuring the fix is validated before blocking the exploit for good

## Additional Agent-Specific Threats

| Threat | Description | Mitigation |
|---|---|---|
| Memory poisoning | False information stored in an agent's memory corrupts all future interactions | Validate and sanitize inputs to memory stores; implement content moderation on memory writes |
| Dynamic tool orchestration abuse | Agent's trajectory assembled on-the-fly can be manipulated to invoke unintended tools | Robust tool versioning, access control per tool, and behavior monitoring |
| Scalable state management exploits | Memory stored across interactions can be exploited for cross-session attacks | Strict tenant isolation in all memory stores; audit access patterns regularly |

## See Also
- [Observability](./observability.md) — Security monitoring as part of observability; Evolving Security section
- [Deployment](./deployment.md) — Secure deployment practices
- [Context Engineering](./context-engineering.md) — Context isolation and sanitization
- [SecurityFrameworks](../SecurityFrameworks/Readme.md) — NIST AI RMF, Google SAIF, AWS coverage
- [AI Agent Skill Security Scanners](../SecurityFrameworks/skill-scanners.md) — Cisco Skill Scanner and NVIDIA SkillSpector for skill supply-chain security
- [Agent Skills / SKILLS.md Standard](../Standards/skills.md) — Skill authoring, scoping, and security best practices
- [Event-Driven Design Patterns for Multi-Agent Systems (Confluent)](../DesignPatterns/event-driven-patterns.md) — Stream Governance, field-level encryption, and retention policies for event-driven agent pipelines

## References
- [agents-best-practices — DenisSergeevitch (2025)](https://github.com/DenisSergeevitch/agents-best-practices) — source for layered guardrail taxonomy, approval record format, and threat category model
- Falconer, S. (2025). *A Guide to Event-Driven Design for Agents and Multi-Agent Systems*. Confluent, Inc. — source for Stream Governance, field-level encryption, and GDPR-aligned retention guidance
