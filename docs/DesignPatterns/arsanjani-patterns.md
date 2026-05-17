# Agentic Architectural Patterns — Arsanjani & Bustos

## Overview

This page synthesizes the pattern catalog from *Agentic Architectural Patterns for Building Multi-Agent Systems* (Arsanjani & Bustos, Packt, 2026, ISBN 978-1-80602-957-0). The book presents a structured pattern language organized into five groups: **Multi-Agent Coordination**, **Explainability & Compliance**, **Robustness & Fault Tolerance**, **Human-Agent Interaction**, and **Agent-Level** patterns. Each pattern follows a Context–Problem–Solution structure, includes implementation guidance, and is mapped to a GenAI Maturity Level (see [Arsanjani GenAI Maturity Model](../MaturityModels/arsanjani-genai-maturity.md)).

The book uses Python and Google Gemini/ADK for code examples but notes the patterns are LLM-agnostic.

---

## Part 1: Multi-Agent Coordination Patterns

### Agent Router (Intent-Based Routing)

**Context:** A system has multiple specialized agents. Users submit natural-language requests that must be dispatched to the correct specialist.

**Problem:** Hard-coded conditional routing breaks as the agent count grows. Keyword matching is fragile and cannot distinguish capability boundaries safely.

**Solution:** Two-step routing: (1) an LLM with a strict schema performs *semantic intent extraction*, translating the raw query into a structured `RoutingIntent` object containing a verb (action) and noun (resource); (2) a *capability graph* maps `(action, resource)` tuples to agent names. If no match exists the request is rejected rather than misdirected.

**Consequences:**
- Pros: Decoupling, scalability (new agents register in the graph without touching routing logic), safety (the graph acts as a whitelist).
- Cons: LLM extraction adds latency; over-granular schema makes the graph brittle.

**Implementation guidance:** Aim for 10–20 canonical action/resource pairs. Use function-calling mode for structured intent extraction (not free-text prompts). Add a semantic cache layer to bypass LLM extraction for repeat queries.

---

### Task Delegation Frameworks

#### Supervisor Architecture (Centralized Orchestration)

**Context:** A complex task requires multiple sequential or conditional steps, each handled by a specialist.

**Problem:** How can the system reliably control flow, track state, and prevent dropped tasks without constant human intervention?

**Solution:** A central orchestrator agent receives the top-level goal, formulates a plan (static or LLM-generated), and delegates sub-tasks to worker agents via structured messages. It collects results and drives conditional branching.

| Feature | Detail |
|---|---|
| Control flow | Hierarchical; orchestrator delegates to workers |
| Key benefit | Predictability, clear audit trail, easy to govern |
| Key drawback | Orchestrator is a single point of failure and potential bottleneck |
| Best for | Regulated workflows (finance, healthcare), processes with clear sequential logic |

**Implementation guidance:** Strict separation of concerns — orchestrator handles routing and state only, workers execute domain tasks. Enforce JSON-schema outputs at every handoff. Implement checkpointing (e.g., LangGraph persisters) so the workflow survives orchestrator restarts.

#### Swarm Architecture (Emergent Decentralized Coordination)

**Context:** The task is dynamic, the solution path is not predefined, or high resilience against component failure is required.

**Problem:** How can a group of autonomous agents collaborate without a central controller that can become a bottleneck or failure point?

**Solution:** A shared *task board* holds task objects with lifecycle statuses. Agents poll the board and self-select tasks that match their capability. On completion, they update the task status, allowing the next capable agent to continue.

| Feature | Detail |
|---|---|
| Control flow | Peer-to-peer; agents self-select from shared board |
| Key benefit | Resilience (no single point of failure), horizontal scalability |
| Key drawback | Hard to debug; behavior is emergent and less predictable; governance is difficult |
| Best for | Creative tasks, content generation pipelines, dynamic environments |

**Implementation guidance:** Start with Supervisor Architecture in enterprise contexts. Introduce Swarm for sub-teams where autonomy is required. Many production systems use a hybrid: Supervisor oversees the business process but delegates blocks to self-organizing crews.

---

### Agent Composition Topologies

#### Blackboard Knowledge Hub

**Context:** Multiple specialists must contribute partial facts to a shared solution. The order of contributions cannot be predetermined.

**Problem:** How can agents collaborate on an ill-defined problem without tight coupling or race conditions?

**Solution:** A central *Blackboard* stores typed, versioned facts and hypotheses. A *Controller* arbitrates contribution cycles (post → evaluate → integrate). Agents do not communicate directly; they post to and read from the Blackboard.

**Consequences:** Pros — flexibility for ill-posed problems, full audit trail. Cons — central controller can become a throughput bottleneck; latency is higher than direct message passing.

#### Contract-Net Marketplace (Mediator + Bids)

**Context:** Multiple agents have overlapping capabilities. Tasks should go to the most suitable agent dynamically.

**Solution:** A mediator broadcasts task announcements. Agents submit bids (capability score, availability). The mediator awards the task to the best bidder.

#### Supervision Tree with Guarded Capabilities

**Context:** A system requires fault isolation — one failing agent must not corrupt the broader workflow.

**Solution:** Agents are organized in a supervision tree. Parent agents monitor child health and restart or replace failed agents within their subtree, limiting blast radius.

---

### Coordination Patterns

#### Multi-Agent Planning

**Context:** A complex goal requires task decomposition, dependency tracking, and parallel execution.

**Solution:** A planner agent produces a directed acyclic graph of sub-tasks. A scheduler assigns sub-tasks to agents respecting dependencies. Results are aggregated by a synthesis agent.

#### Knowledge Sharing

**Context:** Agents need access to shared domain knowledge that evolves as the workflow progresses.

**Solution:** A shared knowledge store (e.g., vector database + key-value cache) lets agents publish and retrieve facts using semantic similarity.

#### Tool Routing in Multi-Agent Contexts

**Context:** Multiple agents share a common toolset. The system must prevent tool conflicts and route tool calls to the appropriate agent.

**Solution:** A Tool Registry mediates access, enforcing exclusive leases for stateful tools and broadcasting results to interested agents.

#### Consensus

**Context:** Agents produce conflicting assessments of the same data (e.g., two risk models disagree).

**Solution:** Agents engage in a structured iterative debate. Each shares its reasoning; others critique. Convergence is reached when all parties accept a shared conclusion or a tie-breaker (human or rule) is invoked.

**Example use case:** Financial forecasting where two analyst agents receive the same market data and produce different projections. Consensus forces them to surface assumptions and converge.

#### Agent Negotiation

**Context:** Agents have competing goals and must agree on resource allocation or action priority.

**Solution:** Agents exchange structured offers and counter-offers (inspired by Contract-Net). A negotiation protocol defines termination conditions.

#### Resource Allocation

**Context:** Shared resources (APIs, compute, databases) must be allocated across agents to avoid starvation or exhaustion.

**Solution:** A Resource Manager agent tracks availability and enforces quota-based or priority-based allocation. Agents request, hold, and release resources explicitly.

#### Conflict Resolution

**Context:** Agents produce incompatible actions or contradictory world-state updates.

**Solution (four strategies):**
1. *Hierarchical resolution* — higher-rank agent wins
2. *Policy-based resolution* — rule engine adjudicates
3. *Negotiation* — agents bargain to a mutually acceptable outcome
4. *Game-theoretic resolution* — payoff matrix determines optimal outcome

**Implementation guidance:** Always create an explainable resolution record (audit trail). Define escalation paths to human-in-the-loop for unresolvable conflicts. Test conflict resolution paths with simulation before production rollout.

#### Formation Control

**Context:** A group of physical or virtual agents (e.g., drones, parallel processing units) must self-organize into a coordinated structure.

**Solution:** Agents maintain relative position using local rules (nearest-neighbor communication). A formation controller broadcasts target configurations; agents adjust autonomously.

---

## Part 2: Explainability and Compliance Patterns

### Instruction Fidelity Auditing

**Context:** In hierarchical multi-agent systems, a worker agent can successfully complete its local sub-task while silently violating constraints in the original high-level instruction — "silent failures."

**Problem:** How can the system verify that a worker's output strictly complies with all constraints in the original instruction before the action is finalized?

**Solution:** A dedicated *Auditor Agent* receives both the original instruction and the worker's output. Its sole role is to compare them against the stated constraints and return a structured audit verdict (`PASS`/`FAIL` with reasons). The orchestrator only finalizes the action if the audit passes.

**Consequences:** Pros — explicit compliance checkpoint, auditable trail. Cons — adds latency and token cost at every audited handoff.

**Implementation guidance:** Apply auditing selectively at high-risk handoffs (financial transactions, compliance-sensitive outputs), not at every step. Balance audit coverage against latency tolerance.

---

### Fractal Chain-of-Thought Embedding (FCoT)

**Context:** Standard chain-of-thought reasoning is linear and static. In multi-agent environments, an agent's reasoning may become invalid as peers provide new or contradictory data.

**Problem:** How can an agent's reasoning be structured to allow dynamic self-correction and synchronization with peer agents?

**Solution:** FCoT structures reasoning as recursive, self-contained *thought units*. Each unit is checked against an objective function (insight + alignment). If the check fails, the unit triggers *temporal re-grounding*: earlier conclusions are formally revised, not just appended. This enables:
- *Recursive self-correction* — continuous realignment loop
- *Dynamic context aperture* — zoom in/out on detail level
- *Inter-agent reflectivity* — agents evaluate and revise peer reasoning
- *Temporal re-grounding* — past conclusions are rewritten, not just extended

**Consequences:** Pros — real-time self-correction, transparent audit trace showing not just *what* was decided but *why* it was revised. Cons — higher latency and token cost than standard CoT; requires orchestration infrastructure for reflective loops.

**Implementation guidance:** Define a clear objective function before implementing FCoT. Apply to complex, high-value tasks where correctness justifies extra cost. Avoid for simple, time-sensitive tasks.

---

### Persistent Instruction Anchoring

**Context:** In deep agent chains, the original high-level instruction is placed at the top of context. As subordinate agents add reasoning and data, the instruction is "lost in the middle" and LLMs give it less weight.

**Problem:** How can critical constraints survive the full depth of a hierarchical multi-agent pipeline without being diluted or forgotten?

**Solution:** The orchestrator embeds critical instructions within semantically distinctive anchor tags (e.g., `PERSISTENT_GOAL: [NO_FORWARD_LOOKING_STATEMENTS]` or `<CRITICAL_INSTRUCTION>...</CRITICAL_INSTRUCTION>`). These anchors are passed along with every handoff context and are designed to remain salient regardless of their position in the prompt.

**Consequences:** Pros — significantly reduces instruction drift; provides auditable constraint traceability. Cons — minor prompt overhead; requires a consistent templating discipline across all agents.

**Implementation guidance:** Standardize the anchor format across the entire system. Use structured tags (not prose) so anchors can be reliably parsed and re-inserted at each handoff.

---

### Shared Epistemic Memory

**Context:** In a multi-agent collective, each agent maintains its own private context window. If one agent discovers a critical state change, others remain unaware — a "Tower of Babel" effect.

**Problem:** How can all agents in a workflow maintain a synchronized, authoritative understanding of the shared world state?

**Solution:** A centralized *Shared Epistemic Memory* module (global scratchpad) serves as the single source of truth. All agents read from and write to it using typed tools. The memory stores timestamped, agent-attributed facts, enabling downstream agents to weigh the freshness and reliability of data.

**Consequences:** Pros — prevents semantic drift; more efficient than passing large state payloads in messages. Cons — central memory can become a bottleneck or single point of failure; concurrent writes require atomic operations.

**Implementation guidance:** Use low-latency, persistent key-value stores (Redis, Memcached) rather than in-memory dictionaries. Enforce a TTL (Time-to-Live) on every memory entry to prevent stale facts from persisting. Expose memory via typed tools (`update_order_status(id, status)`) not generic text writes.

---

### Pattern Composition for Systemic Reliability

For production-grade agentic systems, combining multiple explainability patterns creates layered defense:

1. **Shared Epistemic Memory** — foundational layer of truth; all agents share synchronized state
2. **Persistent Instruction Anchoring** — ensures the mission survives deep agent chains
3. **FCoT Embedding** — continuous internal self-governance during agent reasoning
4. **Instruction Fidelity Auditing** — final external quality gate before committing actions

---

## Part 3: Robustness and Fault Tolerance Patterns

### Robustness Maturity Spectrum (Five Levels)

| Level | Sophistication | Core Capabilities | Key Patterns |
|---|---|---|---|
| 1 | Basic orchestration | Hardcoded chains | None; any failure is catastrophic |
| 2 | Reactive recovery | Retries, timeouts, redundancy | Parallel Execution Consensus, Watchdog Timeout, Adaptive Retry |
| 3 | Adaptive fault tolerance | Self-healing, fallbacks, checkpoints | Auto-Healing Resuscitation, Fallback Model Invocation, Incremental Checkpointing, Rate-Limited Invocation, Delayed Escalation |
| 4 | Observable and auditable | Causality tracking, trust scoring, canary testing | Causal Dependency Graph, Trust Decay and Scoring, Canary Agent Testing |
| 5 | Self-governed and secure | Sandboxing, consensus, isolation, firewalls | Agent Mesh Defense, Execution Envelope Isolation, Majority Voting |

**Recommended rollout:** Start at Level 2 for baseline stability; progress to Level 3 as the system scales; introduce Levels 4–5 for enterprise governance requirements.

---

### Parallel Execution Consensus

**Context:** High-stakes decisions (credit scoring, medical triage) made by a single non-deterministic LLM carry unacceptable risk.

**Problem:** How can the system mitigate the single point of failure of a critical LLM decision?

**Solution:** Two or more independent agents perform the same task in parallel using different models or prompts. An orchestrator compares outputs. If they agree within a defined tolerance, the result is validated. If they disagree significantly, a resolver agent or human reviewer is engaged.

**Consequences:** Pros — validation layer for critical decisions, redundancy against model failures. Cons — higher cost and latency (duplicate LLM calls); requires a well-defined tolerance and escalation path.

**Implementation guidance:** Define "agreement" precisely for each use case (5% numeric tolerance, semantic similarity threshold, etc.). Establish a clear tie-breaker protocol for disagreements.

---

### Delayed Escalation Strategy

**Context:** Immediate human escalation for every agent failure creates alert fatigue and operational bottlenecks. Many failures are transient.

**Problem:** How can the system handle failures intelligently without overwhelming human operators?

**Solution:** A tiered recovery path: (1) automated retry; (2) backup agent or simplified scope; (3) human escalation only after automated paths are exhausted. Each escalation packages a full context packet for efficient human review.

**Consequences:** Pros — reduces unnecessary interruptions; builds resilience against transient failures. Cons — introduces delay before human notification; retry windows must be carefully tuned.

---

### Watchdog Timeout Supervisor

**Context:** Agents interacting with external APIs or performing complex reasoning can hang indefinitely, freezing entire workflows.

**Problem:** How can the system detect and recover from unresponsive agents without manual intervention?

**Solution:** The orchestrator wraps every agent call in a timed execution block. If the agent does not respond within the timeout, it is forcefully terminated and a fallback behavior is triggered (backup agent, simplified analysis, or escalation).

**Consequences:** Pros — prevents cascading stall failures; enforces execution time bounds. Cons — canceling tasks mid-execution may leave resources in inconsistent states; timeout values require careful calibration.

**Implementation guidance:** Use async non-blocking timers (Python `asyncio.wait_for`). Design fallback logic to handle not just timeout events but any cleanup from the cancelled task.

---

### Adaptive Retry with Prompt Mutation

**Context:** An agent fails deterministically because it consistently misinterprets the prompt. A simple retry (same prompt) will reproduce the same failure.

**Problem:** How can a system recover from a deterministic LLM failure loop?

**Solution:** On failure, a meta-agent or orchestrator *mutates* the prompt before retrying. Mutation strategies:
- *Rephrasing* — change wording
- *Adding examples* — provide few-shot demonstrations
- *Decomposition* — add explicit chain-of-thought instruction ("Think step by step…")
- *Constraint tightening* — add format enforcement ("Ensure your response is valid JSON")

**Consequences:** Pros — recovers from deterministic failures; mutated prompts often produce more accurate results than the original. Cons — increased cost and latency; generating meaningful mutations may itself require an LLM call.

---

### Auto-Healing Agent Resuscitation

**Context:** An agent process crashes completely and needs to be restarted without losing task context.

**Solution:** A health monitor detects the crash, retrieves the agent's last checkpointed state, and restarts the agent process with that state restored.

---

### Incremental Checkpointing

**Context:** Long-running multi-step pipelines lose all progress if interrupted mid-execution.

**Solution:** The orchestrator persists workflow state to durable storage after each completed step. On restart, execution resumes from the last checkpoint rather than from the beginning.

---

### Majority Voting Across Agents

**Context:** Three or more independent agents produce potentially conflicting outputs on a critical decision.

**Solution:** An orchestrator collects all outputs and applies a majority vote. If a clear majority exists, it is accepted. If not, the tie is escalated.

---

### Causal Dependency Graph

**Context:** In complex multi-agent workflows, it is difficult to trace which upstream decision caused a downstream failure.

**Solution:** Every agent records its reasoning trace and the inputs it consumed. A graph links each output to its causal predecessors, enabling post-hoc audit and root-cause analysis.

---

### Agent Self-Defense

**Context:** An agent can be compromised by adversarial inputs (prompt injection, data poisoning) that redirect its behavior.

**Solution:** An agent maintains an internal self-monitoring layer that detects anomalous instruction patterns (e.g., instructions to ignore previous constraints). On detection, the agent refuses the instruction and triggers an alert.

---

### Agent Mesh Defense (Firewall)

**Context:** A compromised agent in a multi-agent network can send malicious payloads to its peers.

**Solution:** Inter-agent communication passes through a firewall agent that validates message schemas and enforces policy before forwarding.

---

### Execution Envelope Isolation (Sandboxing)

**Context:** An agent that executes code or calls external APIs could have unintended side effects.

**Solution:** Agent execution is sandboxed in an isolated environment (container, VM, restricted process). The sandbox enforces resource limits and restricts unauthorized I/O.

---

### Rate-Limited Invocation

**Context:** Agents calling shared APIs can exhaust rate limits, causing cascading failures.

**Solution:** A rate limiter wraps all external API calls, enforcing per-agent and per-API quotas. Excess requests are queued or rejected with graceful degradation.

---

### Fallback Model Invocation

**Context:** The primary LLM is unavailable or too expensive for a given request tier.

**Solution:** The orchestrator maintains a fallback hierarchy. On primary model failure or cost threshold breach, it routes to a smaller, faster, or cheaper model.

---

### Trust Decay and Scoring

**Context:** Agent reliability changes over time. A model or tool that performed well last month may degrade.

**Solution:** Every agent accumulates a rolling trust score based on recent success/failure rates. The orchestrator uses trust scores to route tasks and apply additional validation for low-trust agents.

---

### Canary Agent Testing

**Context:** Deploying a new agent version to all users simultaneously risks widespread regressions.

**Solution:** A small fraction of traffic (e.g., 5%) is routed to the new agent version. Performance metrics are compared against the stable version. The rollout proceeds only if metrics remain within acceptable bounds.

---

### Optimizing for Translation Overhead

**Context:** Converting between agent output formats (e.g., prose to JSON) consumes extra tokens and introduces errors.

**Solution:** Design agent output schemas once at the system level, ensuring all handoff formats are compatible without translation steps.

---

## Pattern–Maturity Level Mapping

| Pattern | Maturity Level | Category |
|---|---|---|
| Agent Router | 2 – Dynamic single-agent | Coordination |
| Supervisor Architecture | 4 – Multi-agent systems | Task Delegation |
| Swarm Architecture | 6 – Self-correcting agents | Task Delegation |
| Blackboard Knowledge Hub | 5 – Advanced multi-agent | Composition |
| Contract-Net Marketplace | 5 – Advanced multi-agent | Composition |
| Supervision Tree | 5 – Advanced multi-agent | Composition |
| Consensus | 6 – Self-correcting agents | Coordination |
| Agent Negotiation | 6 – Self-correcting agents | Coordination |
| Instruction Fidelity Auditing | 4–5 | Explainability |
| FCoT Embedding | 4–5 | Explainability |
| Persistent Instruction Anchoring | 4–5 | Explainability |
| Shared Epistemic Memory | 4–5 | Explainability |
| Parallel Execution Consensus | 2–3 | Robustness |
| Watchdog Timeout Supervisor | 2–3 | Robustness |
| Adaptive Retry with Prompt Mutation | 2–3 | Robustness |
| Auto-Healing Resuscitation | 3 | Robustness |
| Incremental Checkpointing | 3 | Robustness |
| Causal Dependency Graph | 4 | Robustness |
| Trust Decay and Scoring | 4 | Robustness |
| Canary Agent Testing | 4 | Robustness |
| Agent Self-Defense | 5 | Security |
| Agent Mesh Defense | 5 | Security |
| Execution Envelope Isolation | 5 | Security |

---

## See Also

- [Arsanjani GenAI Maturity Model](../MaturityModels/arsanjani-genai-maturity.md)
- [Agentic Architecture Components](../Architecture/components-selection.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [OpenAI Agentic Design Patterns](./openai-patterns.md)
- [Gartner LLM Design Patterns](./gartner-patterns.md)
- [ProductionBestPractices: Security](../ProductionBestPractices/security.md)
- [ProductionBestPractices: Deployment](../ProductionBestPractices/deployment.md)
- [ProductionBestPractices: Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Standards: MCP](../Standards/mcp.md)
- [Standards: A2A](../Standards/a2a.md)

## References

- Arsanjani, A., & Bustos, J.P. (2026). *Agentic Architectural Patterns for Building Multi-Agent Systems*. Packt Publishing. ISBN 978-1-80602-957-0. Code: https://github.com/PacktPublishing/Agentic-Architectural-Patterns-for-Building-Multi-Agent-Systems
