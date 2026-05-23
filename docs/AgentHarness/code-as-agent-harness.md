# Code as Agent Harness

## Overview

"Code as Agent Harness" is a survey framework that reframes the role of code in agentic AI systems. Rather than treating code merely as a generated artifact (a target output), the survey posits that code increasingly serves as an **executable, inspectable, and stateful harness** through which agents reason, act, model environments, receive feedback, and coordinate.

The key insight: code has three properties that make it uniquely suited as an agent substrate:

| Property | What It Means |
|---|---|
| **Executability** | Model outputs become verifiable operations — not just text |
| **Inspectability** | Intermediate computation is exposed as structured traces, enabling debugging and audit |
| **Statefulness** | Task progress is represented persistently, enabling long-horizon execution |

This framing, established in the 2026 survey by Ning et al. (UIUC, Meta, Stanford), synthesizes 197 papers across 40+ subcategories to offer a unified view of code as the foundational infrastructure layer for modern agent systems.

## Three-Layer Framework

The survey organizes the code-as-harness concept into three connected layers.

### Layer 1: Harness Interface

The harness interface is where code connects the agent to reasoning, action, and environment modeling — the three fundamental agent functions.

| Interface | Role of Code | Mechanism |
|---|---|---|
| **Reasoning** | Externalizes internal logic into verifiable computation | Interpreters, symbolic solvers, execution traces, and process rewards check and refine intermediate reasoning steps |
| **Acting** | Generated programs function as policies, tool calls, and reusable skills | Code-as-action works across embodied environments, GUI/OS contexts, and software systems |
| **Environment Modeling** | Represents state, dynamics, and feedback | Repositories, simulators, and test suites serve as the environment model the agent reasons over |

### Layer 2: Harness Mechanisms

The harness mechanisms are the internal control systems that manage how code-based agents operate over long horizons.

| Mechanism | Description |
|---|---|
| **Planning** | Structuring how agents decompose intent into executable steps; code provides a natural representation for plans as programs |
| **Memory** | Managing which information remains active in context versus externally stored; code artifacts (files, diffs, test results) serve as persistent memory |
| **Tool Usage** | Exposing typed schemas, sandboxes, and verification mechanisms as callable interfaces |
| **Iterative Debugging** | Converting execution failures into diagnostic and corrective actions through compilation feedback, runtime errors, and test signals |
| **Feedback-Driven Control** | Using execution results to adaptively optimize agent behavior, making the harness reliable and self-improving |

### Layer 3: Harness Scaling

Harness scaling addresses multi-agent coordination over shared code artifacts. Code becomes a common workspace that enables structured autonomy at scale.

| Dimension | Approaches |
|---|---|
| **Role specialization** | Agents specialize as synthesizers, code understanders, or verifiers |
| **Interaction modes** | Collaboration, critique, and debate between agents via shared code artifacts |
| **Workflow topologies** | Hierarchical, adaptive, and execution-driven multi-agent workflows |
| **State convergence** | Test-gated and consensus-based mechanisms for reaching shared agreement on correctness |

Multi-agent systems using code as a shared harness: repositories, tests, traces, and structured artifacts provide the common workspace through which agents coordinate, inspect, and improve each other's behavior.

## Application Domains

The survey identifies seven primary application contexts where the code-as-harness pattern is realized:

| Domain | Code Harness Role |
|---|---|
| **Code Assistants** | Repositories as persistent program worlds; repository-scale memory management; test suites as feedback mechanisms |
| **GUI / OS Agents** | Screen state rendered as structured code; action schemas unified through programmatic interfaces |
| **Scientific Discovery** | Hypotheses encoded as equations; experimental protocols as executable scripts; results as computational notebooks |
| **Embodied Robotics** | Reusable skill modules accumulated as code libraries; real-world deployment via auditable code harnesses |
| **Personalization & Recommendation** | User state and preference models represented as inspectable data structures |
| **DevOps** | Infrastructure-as-code enabling agents to reason over and modify deployment state |
| **Enterprise Workflows** | Business process logic encoded in verifiable, auditable code artifacts |

## Relationship to Agent Harness Concepts

The "code as harness" perspective extends and complements the practitioner-facing harness frameworks:

- The **LangChain harness anatomy** (Agent = Model + Harness) treats code execution as one harness component. The Ning et al. survey elevates code to a *unifying substrate* rather than a single component.
- The **feedforward/feedback harness engineering** model (Böckeler, Thoughtworks) maps directly to the survey's harness mechanisms: guides correspond to planning/memory mechanisms; sensors correspond to the feedback-driven control and iterative debugging mechanisms.
- The survey's **harness interface** layer formally describes what the LangChain harness calls "bundled infrastructure" — but grounds it in verifiable computation rather than tool access.

The three-layer taxonomy gives practitioners a theoretical scaffold for understanding *why* code-centric agent systems outperform purely natural-language orchestration: executability, inspectability, and statefulness are structural advantages unavailable to text-based harnesses.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Reasoning verification | Natural language reasoning is unverifiable | Route reasoning through code execution or symbolic solvers to get verifiable intermediate steps |
| Long-horizon memory | Context windows bound what agents can retain | Use code artifacts (files, diffs, test states) as persistent memory that outlasts any single context window |
| Multi-agent coordination | Prose handoffs between agents cause silent failures | Use shared code artifacts (tests, schemas, structured outputs) as the coordination surface |
| Feedback loop design | Agents repeat mistakes when feedback is sparse | Build iterative debugging loops: compile → run → test → observe → fix |
| Environment opacity | Agents cannot verify environment state | Represent environment state in code (simulations, test suites) so agents can inspect it directly |
| Tool interface fragility | Untyped tool interfaces cause silent failures | Expose tools via typed schemas with sandboxed execution and built-in verification |

## See Also

- [Agent Harness](./agent-harness.md)
- [Harness Engineering](./harness-engineering.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Agent Memory Functional Tiers](../AgentMemory/functional-tiers.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Agentic Design Patterns (OpenAI)](../DesignPatterns/openai-patterns.md)
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Production Best Practices: Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)

## References

- [Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems — Ning et al., arXiv:2605.18747 (May 2026)](https://arxiv.org/abs/2605.18747) — comprehensive 197-paper survey establishing code as the foundational substrate for agentic AI systems; introduces the three-layer harness taxonomy (interface, mechanisms, scaling)
- [Awesome-Code-as-Agent-Harness-Papers — GitHub](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) — companion repository with curated paper list organized by survey taxonomy
