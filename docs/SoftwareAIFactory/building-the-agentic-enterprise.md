---
type: Playbook
title: Building the Agentic Enterprise
description: A practical field guide to designing, deploying, and operating agentic AI systems on Google Cloud, covering architecture patterns, context engineering, AgentOps, platform engineering, and organizational transformation.
tags: [software-ai-factory, agentops, architecture, google-cloud, adk, agentic-ai]
timestamp: 2026-10-27T00:00:00Z
---

# Building the Agentic Enterprise

## Overview

*Building the Agentic Enterprise* by Jaroslav Pantsjoha (Packt, 2026) is a field guide to closing the production gap in agentic AI: the distance between a compelling demo and a system that runs reliably in production, is governable, and delivers repeatable business outcomes. The book uses Google Cloud and the Agent Development Kit (ADK) as its primary technical lens, and grounds every pattern in a continuous case study — the Macro Research & Education Platform (MREP) built by a fictional market intelligence firm, ACME Research.

The central thesis is that the model is only one part of the challenge. Failures that prevent agentic systems from reaching production are structural, not technical — they arise when autonomous capability meets an organization that lacks the governance, skills, and operating culture to run it. Three foundations must be strengthened in parallel: **skills**, **context**, and **culture** — the Three Pillars of Agentic Engineering.

## The Three Pillars of Agentic Engineering

| Pillar | Problem It Solves | Core Claim |
|---|---|---|
| **Skills** | The skills gap nobody has named | Organizations lack the hybrid skills — architecture, operations, product, and AI — needed to take agentic systems from pilot to production |
| **Context** | Context as strategic moat | The durable competitive advantage is not the model (which commoditizes) but the proprietary context an organization can engineer around it |
| **Culture** | AI as organizational culture | Transformation requires reinventing business processes around agentic players, not just making existing processes incrementally faster |

## The PoC Trap and the Day 2 Problem

A consistent theme is the **proof-of-concept trap**: teams produce impressive demos, generate executive attention, then stall between demonstration and production. The failure is structural — it is not a model quality problem:

- AI systems require enterprise wrapping (security review, compliance, data residency, budget ceilings, ownership) that was never designed for autonomous systems
- Most teams treat deployment as the finish line; the harder problem is **Day 2** — operating a live agentic system sustainably over time
- "Vibe coding" (deploying untested prototypes) and "prototype is production" are the two anti-patterns that most reliably produce expensive post-launch failures

Closing the gap requires strengthening technical capability, organizational context, and operating culture in parallel — improvements to the model or prompt alone are insufficient.

The organizational maturity progression the book maps is: **Discovery → Crawl → Walk → Run**:

- **Discovery**: AI on the roadmap; no measurable impact yet
- **Crawl**: Less than 25% business impact; AI SaaS used by some teams; proof exists but is siloed
- **Walk**: Less than 50% impact; human-plus-AI enablement across multiple teams
- **Run**: AI as a structural part of the operating model; agentic systems in production

## LLM Applications vs Agentic Systems

The book draws a sharp architectural boundary between two categories that the industry often conflates:

| Dimension | LLM Application | Agentic System |
|---|---|---|
| Control flow | Predetermined by the developer | Determined at runtime by the model's observations |
| Plan revision | None — executes regardless of outcome | Revises plan based on what it observes |
| Tool use | Invoked according to predefined workflow | Invoked as needed based on reasoning |
| The tell | "Can it change its plan based on what it learns?" — No | Yes |

Prompt chaining is **orchestration without autonomous adaptation**. The distinction is not whether a workflow is complex — it is who controls the next move.

## The Reason-Act-Observe (RAO) Loop

The foundational execution primitive for any agentic system:

1. **Reason** — the model evaluates current context and determines the next action
2. **Act** — the model invokes a tool, delegates to a sub-agent, or produces output
3. **Observe** — the model receives the result and updates its reasoning accordingly

Tools are what give agents their agency — the ability to interact with external systems rather than just producing text. Without tools a model can only generate; with them it can take actions in the world. A tool is any callable interface the agent can use to reach external systems: API calls, database queries, code execution, sub-agent delegation, or human escalation.

## Google ADK Core Primitives

The Agent Development Kit (ADK) is Google's code-first framework for building single and multi-agent systems. Key primitives:

| Primitive | Role |
|---|---|
| **Agent** | The reasoning unit — wraps a model with instructions, tools, and sub-agents |
| **Tool** | A callable function with a schema the model uses to understand and invoke it |
| **Runner** | Executes the agent loop; manages the interaction between agent and session |
| **Session** | Short-term conversational state — the task thread that persists across turns |
| **SessionService** | Manages Tier 2 (session) state; backed by in-memory, Firestore, or AlloyDB |
| **MemoryService** | Manages Tier 3 (long-term) episodic recall |

ADK orchestration primitives:
- **SequentialAgent** — runs sub-agents in order; each step's output is the next step's input
- **ParallelAgent** — fans out to all sub-agents simultaneously; aggregates results
- **LoopAgent** — iterates until a termination condition is met
- **ADK Skills** — the compositional layer between tools and sub-agents; reusable capability units

## Core Architectural Patterns

The book names eight production patterns, each suited to a distinct workload shape:

| Pattern | Structure | Best For | Characteristic Failure |
|---|---|---|---|
| **Planner-Executor** | Planner produces a structured plan; Executor carries it out | Complex multi-step tasks requiring upfront sequencing | Planner invents non-existent data sources |
| **Controller-Worker** | Controller assigns tasks; Workers report results | Parallelizable work with a coordination layer | Controller bottleneck under load |
| **Reactive** | Agent responds to events as they arrive | Low-latency, event-triggered automation | State management complexity |
| **Deliberative** | Agent reasons ahead before acting | High-stakes decisions requiring planning | Latency; over-planning |
| **Event-Driven** | Agents triggered by events in a message bus | Loose coupling; async workloads | Debugging causal chains |
| **Workflow-Driven** | Explicit DAG orchestration | Compliance-sensitive, auditable pipelines | Rigidity; hard to adapt mid-run |
| **Reflection (Trifecta)** | Agent critiques its own output and revises | Quality-critical output where self-correction adds value | Infinite loops; cost |
| **Routing** | Router classifies intent and delegates to specialist agents | High-volume, multi-domain request handling | Tool-selection accuracy degradation above ~50 tools |

### The Harness Layer

A pattern the book introduces explicitly: **separation of control and execution**. The harness is everything outside the model that makes it useful:

- **Control** — the harness decides what happens: routing, guardrails, tool authorization, loop termination
- **Execution** — the model decides what to do within the bounds set by the harness

The anti-pattern "smart tools" collapses this boundary by embedding business logic inside tool implementations, making the system untestable and ungovernable. Tools should be thin I/O contracts; logic belongs in the harness or the model's instructions, not inside tools.

## Multi-Agent Orchestration

### When Multi-Agent Becomes Necessary

The single-agent decision heuristic:
1. Start with a single agent. Can it coherently handle the problem?
2. If yes, stay single-agent with MCP tool empowerment. Add complexity only when needed.
3. If no, identify the natural decomposition: what are the genuinely distinct roles?
4. Design role boundaries with clear responsibilities and explicit handoffs.
5. Choose the simplest context-sharing mechanism that fits.

Signals that multi-agent is warranted: the context window fills with unrelated domains; one agent's output is another's required input; the task has genuinely parallel sub-tasks; different parts of the workflow have different latency, cost, or governance requirements.

**The tool-sprawl threshold**: a single agent with ~50 tools in a real municipal-sector deployment fell below 60% tool-selection accuracy — effectively a coin flip. Decomposing into specialist agents each with a focused tool surface resolved the accuracy problem.

### Orchestration vs Choreography

| Dimension | Orchestration | Choreography |
|---|---|---|
| Control | Centralized supervisor | Distributed; agents react to shared state/events |
| Observability | High — one place to trace decisions | Lower — causal chains cross agent boundaries |
| Failure isolation | Clear; supervisor handles escalation | Complex; emergent failures are harder to attribute |
| Enterprise fit | Preferred for regulated, auditable workloads | Better for loosely coupled, high-throughput pipelines |

### Preventing Runaway Autonomy

Five multi-agent failure modes and their mitigations:

| Failure Mode | Description | Mitigation |
|---|---|---|
| **Infinite loop** | Agent cycles through the same plan without terminating | Loop detection; max-turn circuit breakers |
| **Context starvation** | Agent loses task context across handoffs | Explicit context handoff schemas; the Three Cs (Coherent, Consistent, Complete) |
| **Conflicting actions** | Two agents write to the same resource simultaneously | Shared state locking; supervisor arbitration |
| **Runaway autonomy** | Agent acquires or exercises authority beyond its scope | Scope enforcement; Least Agency principle |
| **Blame diffusion** | No agent can be held accountable for a wrong outcome | Named owner per supervisor output; accountability logged |

**Circuit breakers** — the system-level pattern for runaway control: each agent has a maximum budget (turns, tokens, time) and a hardcoded escalation path when limits are hit. The supervisor does not trust agents to self-terminate.

## Context Engineering

### Context as Strategic Moat

The book's central thesis: as models commoditize, the durable competitive advantage shifts to **proprietary context**. Foundation models are broadly accessible; what differentiates organizations is the quality, freshness, and governance of the context they can assemble around those models.

Context quality is measured on four dimensions:
- **Currency** — is it fresh enough for the decision?
- **Accuracy** — does it reflect ground truth?
- **Relevance** — is it actually useful for the current task?
- **Authority** — is it from the right source for this decision?

### Prompting vs Context Engineering

| Dimension | Prompt Engineering | Context Engineering |
|---|---|---|
| Focus | Static instruction layer — how to phrase the model's task | Dynamic assembly of runtime information the model reasons over |
| Cadence | Changes when behavior needs to change | Changes on every request |
| Owner | Model/agent developer | Platform/data engineering |
| Failure mode | Model ignores or misinterprets instructions | Model reasons correctly on wrong or stale data |

### Context Sources Hierarchy

1. **RAG pipelines** — large, relatively static knowledge; semantic retrieval; latency tradeoff
2. **Tool-based context (APIs)** — real-time, authoritative, transactional; latency per call
3. **Session state** — conversation continuity; fast; size-limited
4. **Long-term memory** — episodic recall across sessions; extraction required
5. **Domain and policy context** — always-on rules and constraints; injected at agent start

### RAG vs Tools Decision Matrix

| Condition | Use RAG | Use Tools |
|---|---|---|
| Data freshness | Data is relatively static | Data changes frequently |
| Precision | Approximate match acceptable | Authoritative source required |
| Query type | Semantic understanding needed | Transactional accuracy required |
| Data structure | Unstructured text | Structured data |

Default guidance: use RAG for knowledge (documents, policies); use tools for real-time data (prices, user state); use session state for conversation continuity. Layer all three with priority ranking.

### Context Window Management

- **Context budget**: allocate token regions explicitly — system prompt, working memory, tool results, history
- **Context drift**: the gradual divergence of context from task relevance; detected via retrieval quality metrics and semantic similarity to the current goal
- **Prioritization and compression**: summarize older turns; evict low-relevance tool results; keep the current task frame always visible

Anti-patterns: "Kitchen sink retrieval" (fetching everything and letting the model sort it out), "Stale by schedule" (refreshing on a timer rather than on detected drift), "Context privilege escalation" (one agent's context scope creeping into another's domain).

## Security, Identity, and Guardrails

### The Agent Identity Stack

Every agent in a production system needs a verifiable identity:

| Layer | What It Provides |
|---|---|
| **Workload Identity Federation** | Cryptographic identity for the agent process; eliminates long-lived service account keys |
| **Service Account per Role** | Not per agent instance — per functional role, least-privilege |
| **Tool-level RBAC** | Authorization checked at the tool boundary, not in the agent's instructions |
| **Audit Trail** | Every action traced to an agent identity, a session, and a human owner |

The design principle: models can be manipulated through prompt injection. Infrastructure controls sit outside the reasoning loop and cannot be bypassed by the model.

### The Concentric Security Model

Six progressively tighter layers surrounding the agent and its data:
1. Edge WAF (network perimeter)
2. VPC Service Controls (data exfiltration prevention)
3. Identity and access controls (Workload Identity Federation)
4. Tool-level RBAC (authorization at the action boundary)
5. Agent guardrails (input, action, output rails)
6. Data controls (PII detection, field-level encryption)

### Guardrail Architecture (Three-Layer)

| Layer | When It Fires | What It Enforces |
|---|---|---|
| **Input guardrail** | Before the model processes a request | Topic scope, PII detection, prompt injection detection, rate limits |
| **Action guardrail** | Before a tool call executes | Permission check; write-back authorization; scope enforcement |
| **Output guardrail** | Before the response is returned | Hallucination check; content policy; data residency |

### MCP Security Considerations

MCP exposes a significant attack surface in multi-agent systems:
- **Tool response injection**: malicious content in tool responses re-enters the agent's reasoning as context
- **Shadow tools**: rogue MCP servers masquerading as legitimate tool endpoints
- **Prompt injection via data sources**: RAG knowledge base entries crafted to redirect agent behavior

Mitigations: signed MCP manifests, centralized MCP proxy pattern, Model Armor sanitization on all tool responses, private-network MCP via tunnels.

**Least Agency principle**: every agent should have the minimum capability set required to complete its task. Authority is not granted speculatively.

### Google's SAIF 2.0

Google's Secure AI Framework (SAIF 2.0) provides six core security principles applicable to agentic deployments: secure by design, secure by default, secure in deployment, secure operations, security transparency, and responsible AI. The framework maps to the five NIST CSF functions (Identify, Protect, Detect, Respond, Recover) for agentic workloads.

## State, Memory, and Decision Persistence

### The Four-Tier Memory Hierarchy

| Tier | Name | Persistence | Backing Store | Use Case |
|---|---|---|---|---|
| **Tier 1** | Working memory (context window) | Turn-scoped | In-process | Active reasoning; immediate tool results |
| **Tier 2** | Session memory | Session-scoped | Firestore / Redis | Conversation continuity; task state |
| **Tier 3** | Long-term / episodic memory | Persistent | AlloyDB / Vector store | Cross-session recall; user preferences |
| **Tier 4** | Audit trail (immutable) | Permanent | Cloud Spanner / BigQuery | Compliance; decision replay; dispute resolution |

### Decision Audit Trails

A compliance-grade system must be able to answer: "Why did the agent decide what it decided?" This requires capturing not just the outcome but the **reasoning trace** — the chain of observations, tool calls, and intermediate conclusions that led to the decision. Near-miss events (decisions that were almost wrong) carry equal weight to actual errors in a well-designed audit trail.

The **session-rewind** capability in recent ADK releases allows operators to roll a session back to the state before a specified invocation, enabling compliance review, debugging, and re-execution with different inputs.

### The Day 2 Survival Pattern

Schema migration is the most common Day 2 outage pattern for stateful agents: a session schema change incompatible with sessions in-flight causes a runtime failure. Mitigations:
- Lazy migration chains (agents re-hydrate old session schemas on first access)
- Graceful amnesia (if hydration fails, load only the session summary and ask the user to re-establish context)
- Schema versions tracked in session metadata; migration scripts version-controlled alongside the agent code

## AgentOps and EvalOps

### Why Traditional Ops Breaks for Agentic Systems

Traditional DevOps assumed deterministic software: the same input always produces the same output, and correctness is binary. Agentic systems are **statistically correct** — correctness is a distribution, not a value. Traditional monitoring, alerting thresholds, and test suites do not map.

### The Five-Layer Agent Governance Stack

1. **Safety layer** — three rails: input (sanity check), action (permission check), output (hallucination check)
2. **Evaluation layer (EvalOps)** — continuous, statistical evaluation in production; the Evaluation Pyramid
3. **Observability layer** — cognitive observability: not just "did it respond?" but "did it reason correctly?"
4. **Runtime controls** — retries, circuit breakers, HITL escalation, global kill switch
5. **Lifecycle layer** — birth-to-retirement governance: Agent Registry, lifecycle phases, saturation ceiling

### The Evaluation Pyramid

Mirrors the traditional Test Pyramid with one critical change: upper layers are statistical rather than binary.

| Layer | Type | What It Checks | Cost |
|---|---|---|---|
| **Component tests** | Deterministic | Tool contracts, schema validation, output format | Low |
| **Integration tests** | Semi-deterministic | Agent-tool interactions, handoff schemas | Medium |
| **Trajectory evaluation** | Statistical | Did the agent take the right sequence of steps? | High |
| **LLM-as-judge** | Statistical | End-to-end quality against golden outputs | Highest |

Key trajectory metrics: tool-call accuracy, step completion rate, context utilization, goal achievement rate.

**Implementing LLM-as-judge**: the judge model (ideally a different model from the one being evaluated) scores outputs against a rubric. "Judge drift" — where the judge's rubric drifts from the intended standard over time — is a named anti-pattern that requires periodic rubric re-calibration against human ratings.

### Human-in-the-Loop (HITL) as Architectural Decision

The key design question for any HITL proposal is: **what decision is the human actually being asked to make?**

Reviewing every agent output for correctness creates a bottleneck that doesn't scale — reviewers disengage quickly when approving routine outputs. Placing humans at **goal-setting, constraint-definition, and approval boundaries** — rather than at every output — scales with business change rather than with traffic volume. Agents execute within those human-defined bounds.

### The Three Trust Tiers

| Tier | Agent Behavior | Human Role |
|---|---|---|
| **Tier 1** | Agent reads and summarizes; no writes | Review outputs |
| **Tier 2** | Agent drafts; human approves before any external action | Approval gate |
| **Tier 3** | Agent acts autonomously within defined scope; humans set scope and review anomalies | Scope governance |

### CI/CD for Non-Deterministic Systems

Agent CI/CD differs from software CI/CD in one critical dimension: the test suite cannot assert exact output equality. Quality gates must be statistical:

- Pass rate against an eval suite of real representative tasks
- Trajectory evaluation metrics above configured thresholds
- Domain-specific compliance gates (for MREP: source verification rate, compliance agent rejection rate)
- A failed domain gate blocks promotion — eval is the deployment authority

The **adversarial gate**: before a new agent revision reaches production, it runs against an adversarial eval suite designed to trigger its known failure modes. Passing the adversarial suite is a prerequisite for canary promotion.

**Canary and shadow deployment** for agents: shadow deployment runs the new revision on live traffic without routing its outputs to users; canary promotes a small traffic slice to the new revision and compares statistical quality metrics against the control.

## Platform Engineering for Agentic Systems

### The Internal Developer Platform (Paved Road)

At scale, individual teams building their own RAG stacks, eval pipelines, and deployment infrastructure create the "three stacks in a trenchcoat" anti-pattern — duplicated, inconsistent, ungovernable. The alternative is a **centralized Agent Platform with self-service APIs**:

- **Agent Blueprint** — IaC template for a new agent: IAM bindings, Secret Manager wiring, Cloud Run / Agent Runtime config, logging setup
- **Paved road** — the platform team owns RAG, eval, deploy, and observability infrastructure; product teams consume it, don't rebuild it
- **Agent Gateway** — the enforcement point: all agent traffic passes through; enforces security policy, Model Armor, rate limits, cost attribution
- **Agent Registry** — central catalog of approved agents, tools, and skills; the single source of truth for governed assets

### Operating Model Roles

| Role | Responsibility |
|---|---|
| **Platform team (AICCoE)** | Builds and maintains the paved road; governs the Agent Gateway and Registry; sets standards |
| **Product / agent team** | Consumes the platform; builds agent business logic and domain-specific tools |
| **Applied AI Engineer** | Hybrid role spanning architecture, operations, product, and AI; the "Mini-CEO" of the agent system |
| **Agent Owner** | Named human accountable for a running agent system; the person who "signs off" before go-live |

### AI Center of Excellence (AICCoE)

The AICCoE mandate: prevent the "pervasive AI problem" — hundreds of agents built independently with no shared standards, no shared infrastructure, and no shared governance. The AICCoE:

- Publishes versioned platform modules (RAG pipeline, eval harness, deploy templates)
- Operates the Agent Gateway as the enforcement point
- Maintains the API Hub as the agent tool registry
- Governs the Agent Registry (which agents are approved, by whom, for what scope)
- Runs the InnerSource model — teams contribute improvements back to the platform

### DORA Archetypes and Organizational Readiness

The book maps organizational readiness to DORA research archetypes:

- **"Constrained by Process" teams (Cluster 3)**: ideal agent candidates — disciplined enough to govern autonomous systems
- **"Legacy Bottleneck" teams (Cluster 2)**: danger zone — technical debt and manual process gates will block agent delivery
- **"Harmonious High-Achievers" (Cluster 7)**: platform pioneers — high deployment frequency and recovery time make them ideal AICCoE anchors

## Operating Models and Business Transformation

### The Service-as-Software Shift

Traditional B2B commerce: a company buys a service performed by humans. The emerging model: **Business-to-Agent (B2A)** — a company's agents interact directly with another company's agents. The transaction surface, the contracting model, and the trust model all change.

Implications:
- APIs become agent interfaces (structured, machine-readable, with capability declarations)
- SLAs are negotiated between orchestrators, not account managers
- Trust is established via cryptographic agent identity, not human relationships

### The AI Squad Model

The operating unit for hybrid human-agent work. Composition:

- **Human orchestrator** — sets goals, constraints, and approval boundaries; reviews anomalies; escalates blockers
- **Specialist agents** — domain-specific actors with focused tool surfaces
- **Coordinator agent (optional)** — manages inter-agent communication and context handoffs

The squad replaces the team-of-humans model for defined, repeatable workflows. Humans remain the orchestration layer; agents fill the execution layer.

### The Agentic Maturity Triangle

Three audience faces on the maturity axis: **#AIReady** (has assistants, incremental gains) → **#AIFirst** (processes redesigned around AI) → **#AINative** (agentic players in the operating model; humans govern, agents execute). The Vibe Engineering tax — the cost of maintaining prototype-quality systems that were never properly operationalized — is what stalls most organizations between AIReady and AIFirst.

### Applied AI Engineering as Emerging Discipline

The book argues for a new discipline synthesizing:
- Solutions architecture (system design, cloud deployment)
- Platform engineering (CI/CD, IaC, observability)
- Product ownership (business value alignment, stakeholder management)
- AI/ML operations (model selection, eval, cost management)
- Security and compliance (identity, guardrails, audit)

The "Multi-vantage posture" — single-hat hiring fails because no one of these disciplines alone is sufficient. Applied AI Engineers must hold multiple vantage points simultaneously.

### Culture as Code

Codifying organizational purpose so it can be injected into agent context:
1. Inventory the implicit — values, priorities, and constraints that are currently in people's heads
2. Structure the strategic — encode them as machine-readable policy files, not prose memos
3. Govern like infrastructure — version-controlled, reviewed, tested against agent behavior

This closes the loop between the "context as moat" thesis and organizational design: the organization's proprietary context includes its purpose, constraints, and decision principles, not just its data.

## The MREP Reference Architecture

The book consolidates patterns into a single worked architecture — the Macro Research & Education Platform — with a **Decision Register** capturing every load-bearing design decision. Key decisions documented:

| Decision Area | Question | Default Answer |
|---|---|---|
| Single vs multi-agent | Can one agent handle the full task coherently? | Start single; decompose when context fills or roles diverge |
| Orchestration vs choreography | Is compliance/auditability required? | Orchestration for regulated workloads |
| RAG vs tools | Is the data static or dynamic? | RAG for static knowledge; tools for real-time data |
| Centralized vs federated platform | Is there shared data or compliance? | Centralized platform with self-service APIs |
| HITL placement | What question does the human answer? | Goal/constraint setting and approval boundaries, not output review |
| Agent Runtime vs Cloud Run | Is long-running state required? | Agent Runtime for stateful; Cloud Run for stateless |

## Common Anti-Patterns

| Anti-Pattern | Description | Consequence |
|---|---|---|
| **Vibe coding** | Deploying untested prototypes directly to production | No baseline; no rollback; no owner |
| **Agent in name only** | LLM application labeled as an agent | Mis-governed; wrong operational model applied |
| **Prototype is production** | PoC code running live after the demo succeeded | Technical debt compounds; no governance |
| **The omnipotent agent** | Single agent accumulates all tools and responsibilities | Tool-selection accuracy collapses above ~50 tools |
| **The self-evaluating agent** | Agent judges its own output quality | Systematic blind spots; evaluation always passes |
| **MCP tool sprawl** | Registering every available MCP server without governance | Attack surface expansion; context pollution |
| **The silent fail** | Agent returns a graceful response on internal error | Production issues invisible until they cause visible business damage |
| **The eval-free zone** | CI/CD pipeline without evaluation gates | Regressions in agent behavior deploy silently |
| **Agent sprawl** | Agents proliferate without a registry or lifecycle governance | Ungovernable fleet; no named owners |
| **The efficiency trap** | AI investment optimized for cost reduction rather than capability expansion | Competitive differentiation erodes as everyone achieves the same incremental gains |
| **Context Amnesia** | Agent loses task context across sessions or handoffs | Recurring errors; user frustration; audit gaps |
| **Vibe Scaling** | Scaling prototype patterns to enterprise load without re-architecture | Fragility, compliance exposure, operational chaos |

## See Also

- [Gemini Enterprise Agent Platform](../AgentPlatforms/gemini-enterprise-agent-platform.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Agent Harness](../AgentHarness/agent-harness.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [AgentOps Overview](../AgentOps/README.md)
- [GenOps](../AgentOps/genops.md)
- [LLM Evaluation Frameworks](../EvaluationFrameworks/llm-frameworks.md)
- [AI-as-Judge](../EvaluationFrameworks/ai-as-judge.md)
- [Agent Identity](../SecurityFrameworks/agent-identity.md)
- [SAIF Framework](../SecurityFrameworks/google-saif.md)
- [State & Memory Management](../ProductionBestPractices/state-memory.md)
- [Deployment Best Practices](../ProductionBestPractices/deployment.md)
- [Agent Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [AI Governance Strategy](../AIGovernance/governance-strategy.md)
- [Google Vendor Hub](../AllThingsGoogle/README.md)

## References

- Jaroslav Pantsjoha, *Building the Agentic Enterprise: A Practical Field Guide to Designing, Deploying, and Operating Agentic AI Systems on Google Cloud*, Packt Publishing, 2026. ISBN 9781807604455
