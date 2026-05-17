# Deployment

Deploying agentic AI systems requires practices that go beyond standard software deployment. Agents are non-deterministic, stateful, and can take real-world actions — which means deployment failures have higher blast radius than typical services.

## Overview

![GenOps Team Structure](../assets/images/agentops-genops-team-diagram.jpeg)

GenOps (Generative Operations) is the evolution of MLOps for agentic systems. Key differences from traditional MLOps:

| Dimension | Traditional MLOps | GenOps |
|---|---|---|
| Output type | Deterministic predictions | Non-deterministic, generative responses |
| Evaluation | Accuracy, F1, AUC | Relevance, coherence, safety, alignment |
| Versioning | Model weights + data | Model + prompt + context + tools |
| Rollback trigger | Accuracy regression | Quality regression, safety violation, cost spike |
| Scaling unit | Inference replicas | Agent instances + tool capacity + memory stores |

## Best Practices

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Big-bang deployments | Releasing agent changes to all users at once risks widespread quality regressions | Tried feature flags only; still exposed too many users to broken prompts | Use canary deployments — route 5% of traffic to new version, monitor quality metrics before full rollout |
| Prompt versioning | Prompt changes are as impactful as code changes but often untracked | Stored prompts in code comments; no history or rollback | Treat prompts as versioned artifacts in source control; tie prompt version to deployment version |
| Environment parity | Agents behave differently in dev vs prod due to different tool configs or model versions | Used different model versions per environment; bugs only appeared in prod | Pin model versions and tool configurations per environment; use infrastructure-as-code for agent config |
| Stateful agent restarts | Restarting an agent mid-task loses in-progress state | Relied on client retry; users lost work | Implement checkpointing (LangGraph checkpointers, durable execution via Restate) so agents resume from last known state |
| Runaway agent loops | Agents can enter infinite tool-call loops consuming unbounded tokens and time | Set only a global timeout; agents still burned budget before stopping | Enforce per-invocation step limits and token budgets; implement circuit breakers on tool call frequency |
| Multi-agent coordination failures | In multi-agent systems, one agent's failure cascades silently | Assumed agents would self-correct; they compounded errors instead | Define explicit handoff contracts between agents; validate outputs at each handoff boundary |
| Orchestration loops | Orchestrators that repeatedly delegate tasks in a cycle run up unbounded costs | Set only a global timeout; agents still burned budget before stopping | Implement explicit step counters, loop detection, and forced termination conditions; AWS Step Functions enforces maximum execution time and step limits natively — set these from day one |
| Schema-free handoffs | Free-form inter-agent prose at handoff boundaries causes silent failures and context corruption | Passed natural language summaries between agents for flexibility; downstream agents misinterpreted them | Require JSON-schema-validated outputs at every handoff; return a structured error to the orchestrator on validation failure — never proceed with a potentially corrupt payload |
| Handoff payload bloat | Verbose payloads forwarded between agents bloat context windows and degrade reasoning quality | Forwarded full intermediate results in task objects for completeness | Include only what the next agent needs; store intermediate results in S3 and reference them by pointer in DynamoDB task state |
| Scaling tool dependencies | Agent scale-out is bottlenecked by downstream tool API rate limits | Scaled agent replicas without scaling tool capacity; hit rate limits immediately | Model tool capacity as a first-class constraint; implement queuing and backpressure for tool calls |
| Deployment rollback | Rolling back an agent deployment is complex when memory stores have been mutated | Rolled back code but not memory; agents behaved inconsistently | Implement memory versioning or append-only memory with rollback markers; test rollback procedures regularly |

## Operational Maturity Levels

| Level | Characteristics |
|---|---|
| 1 – Basic | Manual deployment, basic logging, manual scaling |
| 2 – Automated | CI/CD pipelines, comprehensive monitoring, auto-scaling |
| 3 – Intelligent | Self-healing, predictive analytics, multi-agent coordination |
| 4 – Autonomous | Fully autonomous operational decisions, self-optimizing ecosystems |

## Core Infrastructure Stack

**Container Orchestration**: Kubernetes for agent deployment, Docker for containerization, service mesh for inter-agent communication

**CI/CD**: GitHub Actions / GitLab CI for pipelines, ArgoCD for GitOps-based deployment, Helm for Kubernetes management

**Durable Execution**: [Restate](https://restate.dev/) for retries, fault tolerance, timers, and scheduling — acts as a reverse-proxy handling durable async execution for agent workflows

**Cloud Platforms**: Google Vertex AI, AWS Bedrock / AgentCore, Azure AI Foundry — each provides managed agent runtimes with built-in scaling and observability

## Evaluation-Gated Deployment

The core pre-production principle from Google's AgentOps practice: **no agent version should reach users without first passing a comprehensive evaluation that proves its quality and safety**. This trades manual uncertainty for automated confidence.

Two implementation patterns:

| Approach | When to Use | Mechanics |
|---|---|---|
| Manual Pre-PR Gate | Teams beginning their evaluation journey | AI/Prompt Engineer runs eval locally before PR; performance report linked in PR; reviewer assesses behavioral changes and guardrail violations |
| Automated In-Pipeline Gate | Mature teams | Evaluation harness integrated into CI/CD; failing evaluation automatically blocks deployment; thresholds defined by ML Governance |

The evaluation harness must assess **behavioral quality** — not just functional correctness. An agent can pass 100 unit tests but still fail by choosing the wrong tool or hallucinating a response.

## Three-Phase CI/CD Pipeline (Google AgentOps)

A robust agent CI/CD pipeline is structured as a funnel — catching errors early and cheaply ("shifting left"):

**Phase 1 — Pre-Merge Integration (CI)**
Triggered on every pull request. Runs fast checks: unit tests, code linting, dependency scanning, and — critically — the **agent quality evaluation suite** against a golden dataset. Failures block the merge. Infrastructure: Google Cloud Build with PR checks configuration template.

**Phase 2 — Post-Merge Validation in Staging (CD)**
Once merged, the CD process packages the agent and deploys it to a staging environment (high-fidelity replica of production). Runs load testing, integration tests against remote services, and internal user testing ("dogfooding"). The staging environment validates the agent as an *integrated system* under production-like conditions.

**Phase 3 — Gated Deployment to Production**
Almost never fully automatic. Requires a **Product Owner sign-off** (human-in-the-loop). The exact artifact validated in staging is promoted — not rebuilt. Infrastructure: Terraform for IaC, production deployment configuration with appropriate safeguards.

**Infrastructure enablers**:
- **Infrastructure as Code (IaC)**: Terraform defines environments programmatically — identical, repeatable, version-controlled. Prevents environment drift.
- **Automated Testing Frameworks**: Pytest-based frameworks handle agent-specific artifacts: conversation histories, tool invocation logs, dynamic reasoning traces.
- **Secrets Management**: API keys injected at runtime via Secret Manager — never hardcoded in repository or prompts.

## GitOps for Agent Deployments

Treat the git repository as the single source of truth for deployment state:
- Every deployment = a git commit
- Every rollback = a git revert
- Platforms: Agent Engine or Cloud Run + Cloud Load Balancing for traffic management across versions

## Fault Tolerance and Robustness Patterns

Arsanjani & Bustos (2026) define a five-level robustness maturity spectrum. The following patterns extend existing deployment practices for production-grade agentic systems:

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Stalled/hanging agents | An agent interacting with a slow external API enters an infinite wait, freezing the entire workflow | Set only a global timeout; stalled agent consumed the full budget before terminating | **Watchdog Timeout Supervisor**: wrap every agent call in a timed execution block (Python `asyncio.wait_for`); if agent does not respond within deadline, forcefully cancel and trigger fallback (backup agent, simplified analysis, or escalation) |
| Deterministic LLM failure loops | An agent repeatedly returns malformed output on the same input; simple retry reproduces the same failure | Resent the same prompt on retry — same error every time, wasted tokens | **Adaptive Retry with Prompt Mutation**: on failure, mutate the prompt before retrying — rephrase, add few-shot examples, inject chain-of-thought instructions ("Think step by step"), or tighten format constraints; mutated prompts often recover accuracy while resolving the failure |
| Agent crash mid-task | An agent process crashes and all in-progress state is lost; full restart required | Relied on client retry to restart from scratch — users lost minutes of work | **Auto-Healing Agent Resuscitation**: health monitor detects crash, retrieves last checkpointed state from durable store, restarts agent process with that state restored |
| Long-running pipeline interruptions | Multi-step pipelines lose all progress when interrupted mid-execution | Stored state in memory only; any infrastructure event meant starting over | **Incremental Checkpointing**: persist workflow state to durable storage (e.g., LangGraph checkpointers, DynamoDB) after each completed step; on restart, resume from last checkpoint rather than the beginning |
| API rate limit exhaustion | Agents calling shared external APIs exhaust rate limits, causing cascading failures | No throttling; bursts from parallel agents triggered 429 errors across the system | **Rate-Limited Invocation**: wrap all external API calls in a rate limiter enforcing per-agent and per-API quotas; excess requests are queued or rejected with graceful degradation |
| Primary model unavailability | The primary LLM becomes unavailable or cost threshold is breached mid-workflow | No fallback; agent halted and returned an error | **Fallback Model Invocation**: maintain a fallback hierarchy; on primary model failure or cost trigger, route to a smaller, faster, or cheaper model for continuity |
| Human escalation fatigue | Immediate escalation for every agent failure overwhelms operators and creates alert noise | Escalated every low-confidence result to a human reviewer; reviewers became a bottleneck | **Delayed Escalation Strategy**: attempt automated recovery first (retry → backup agent → simplified scope); only escalate to a human operator after automated paths are exhausted, with a full context packet for efficient review |

## See Also
- [Observability](./observability.md)
- [Cost Management](./cost-management.md)
- [Agent Testing & Evaluations](./testing-evaluations.md)
- [A2A Protocol](../Standards/agent2agent.md) — registry architectures for multi-agent deployments
- [Agentic Architectural Patterns — Arsanjani & Bustos](../DesignPatterns/arsanjani-patterns.md) — full fault tolerance and robustness pattern catalog

## References
- Arsanjani, A., & Bustos, J.P. (2026). *Agentic Architectural Patterns for Building Multi-Agent Systems*. Packt Publishing. ISBN 978-1-80602-957-0. — Source for robustness patterns: Watchdog Timeout, Adaptive Retry with Prompt Mutation, Auto-Healing, Incremental Checkpointing, Rate-Limited Invocation, Fallback Model Invocation, Delayed Escalation.
