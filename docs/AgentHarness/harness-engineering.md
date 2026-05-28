# Harness Engineering

## Overview

Harness engineering is the practice of designing and maintaining the system of guides and sensors that wrap a coding agent to increase confidence in its output. While the [Agent Harness](./agent-harness.md) page covers what a harness *is* and its core components, this page focuses on *how to engineer one* — the mental models, control structures, regulation categories, and practical patterns for building an effective outer harness for a coding agent.

The goal of a well-built harness is twofold: increase the probability the agent gets it right the first time, and provide a self-correcting feedback loop that catches as many issues as possible before they reach human review. The result is less review toil, higher system quality, and fewer wasted tokens.

This framing is drawn from Birgitta Böckeler (Thoughtworks, April 2026), who applies cybernetics concepts to harness design.

## Bounded Contexts of "Harness"

The word "harness" means different things depending on context:

- **Model-level harness**: everything except the model itself (the broad LangChain definition — see [Agent Harness](./agent-harness.md))
- **Builder harness**: the harness built into the coding agent product by its creators (system prompt, code retrieval, orchestration)
- **User harness**: the outer harness built by the team *using* the coding agent, specific to their codebase and conventions

Harness engineering for coding agent users focuses on the **user harness** — the controls a team builds around the agent for their specific system.

## Feedforward and Feedback

A harness operates through two complementary control types:

| Control Type | Direction | Purpose | Examples |
|---|---|---|---|
| **Guides** (feedforward) | Before the agent acts | Anticipate unwanted outputs; steer behavior proactively | AGENTS.md, skills, reference docs, coding conventions, bootstrap scripts |
| **Sensors** (feedback) | After the agent acts | Observe outputs; enable self-correction | Linters, type checkers, test runners, AI code review agents, browser automation |

Using only feedback produces an agent that keeps repeating the same mistakes. Using only feedforward produces an agent that encodes rules but never verifies they worked. Both are required.

## Computational vs. Inferential Controls

Controls also differ by execution type:

| Type | Execution | Speed | Reliability | Best For |
|---|---|---|---|---|
| **Computational** | CPU — deterministic | Milliseconds to seconds | Reliable, consistent | Tests, linters, type checkers, structural analysis, dependency scanners |
| **Inferential** | GPU/NPU — LLM-based | Slower, more expensive | Non-deterministic | Semantic analysis, AI code review, LLM-as-judge, rich guidance |

Computational sensors are cheap enough to run on every change alongside the agent. Inferential sensors add semantic judgment but should be used selectively — on post-integration pipelines or for high-value checks where deterministic tools fall short.

A particularly powerful pattern: inferential sensors whose output is **optimized for LLM consumption** — custom linter messages that include remediation instructions, effectively a positive form of prompt injection that feeds directly into the agent's self-correction loop.

## The Steering Loop

The human's role is to steer the agent by iterating on the harness itself. When an issue recurs, the response is to improve the feedforward or feedback controls — not to supervise more closely.

Agents can assist in this loop: coding agents can write structural tests, generate draft rules from observed patterns, scaffold custom linters, and create how-to guides from codebase archaeology. This makes building custom controls progressively cheaper.

## Timing: Keep Quality Left

Harness controls should be distributed across the development lifecycle according to their cost, speed, and criticality — the same principle as shifting tests left in CI/CD.

**Before commit / during agent run:**
- Fast linters, type checkers, basic code review agent
- Feedforward guides (AGENTS.md, skills, LSP integration)

**Post-integration pipeline:**
- Repeat all fast controls
- Add more expensive sensors: mutation testing, broad architecture review, detailed inferential review

**Continuous / outside the change lifecycle:**
- Drift detection: dead code, test coverage quality, dependency scanning
- Runtime feedback: SLO monitoring, response quality sampling, log anomaly detection

## Regulation Categories

A harness regulates the codebase across three distinct dimensions. Harnessability and complexity vary significantly across them.

### Maintainability Harness

Regulates internal code quality: duplication, complexity, test coverage, style, architectural drift. This is the most mature category — pre-existing tooling (linters, coverage tools, ArchUnit) maps directly onto it.

**What computational sensors catch reliably:** duplicate code, cyclomatic complexity, missing test coverage, architectural drift, style violations.

**What inferential sensors can partially address:** semantically duplicate code, redundant tests, brute-force fixes, over-engineered solutions — but expensively and probabilistically, not on every commit.

**What neither catches reliably:** misdiagnosis of issues, overengineering, misunderstood instructions. These require human judgment.

### Architecture Fitness Harness

Regulates architectural characteristics via [Fitness Functions](https://www.thoughtworks.com/en-de/radar/techniques/architectural-fitness-function):

- Skills that feed forward performance requirements + performance tests that feed back on regressions
- Skills describing observability conventions (logging standards) + debugging instructions that ask the agent to reflect on log quality
- Custom linters enforcing module boundary rules + structural tests that run as pre-commit hooks

The OpenAI Codex team's approach is a concrete example: layered domain architecture enforced by custom linters and structural tests, with recurring "garbage collection" agents that scan for drift and open targeted refactoring PRs.

### Behaviour Harness

The hardest category — regulating whether the application functionally behaves as intended.

Current common approach:
- **Feedforward**: functional specification (short prompt to multi-file descriptions)
- **Feedback**: AI-generated test suite + coverage checks + manual testing

This approach places significant trust in AI-generated tests, which is not yet sufficient for high-confidence autonomous delivery. The [approved fixtures](https://lexler.github.io/augmented-coding-patterns/patterns/approved-fixtures/) pattern shows promise in specific areas but is not a wholesale solution. The behaviour harness remains an open problem.

## Harnessability

Not every codebase is equally amenable to harnessing. Properties that increase harnessability:

- **Strong typing**: type checkers become available as sensors automatically
- **Clearly definable module boundaries**: enable architectural constraint rules
- **Opinionated frameworks**: abstract away details the agent doesn't need to reason about
- **"Boring" technology choices**: stable APIs, high training data representation, composable abstractions

Ned Letcher (Thoughtworks) uses the term **ambient affordances** for these structural properties of the environment that make it legible, navigable, and tractable to agents.

**Greenfield vs. legacy tradeoff**: Greenfield teams can bake harnessability in from day one — technology and architecture choices determine how governable the codebase will be. Legacy teams face the harder problem: the harness is most needed where it is hardest to build.

## Harness Templates

Enterprise teams typically have a small number of common service topologies (e.g., CRUD business service on JVM, event processor in Go, data dashboard in Node) that cover ~80% of their needs. These may evolve into **harness templates**: bundles of guides and sensors pre-configured for a topology's structure, conventions, and tech stack.

Teams may increasingly choose tech stacks and architectures partly based on what harnesses are already available. This is also an application of **Ashby's Law of Requisite Variety**: a regulator must have at least as much variety as the system it governs. Committing to a topology narrows the agent's output space, making a comprehensive harness more achievable.

## The Role of the Human

Human developers bring an implicit harness to every codebase: absorbed conventions, aesthetic judgment, organizational memory, and social accountability. A coding agent has none of this — no intuition that "we don't do it that way here," no awareness of which technical debt is tolerated for business reasons, no sense that a 300-line function is a problem.

Harnesses are an attempt to externalize and make explicit what human developer experience provides. But this can only go so far. The goal of a good harness is not to fully eliminate human input — it is to **direct human attention to where it matters most**.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Feedforward-only harness | Rules encoded but never verified | Always pair guides with sensors; both are required |
| Feedback-only harness | Agent repeats same mistakes | Add feedforward guides to prevent known failure modes proactively |
| Expensive sensors on every commit | Inferential sensors slow down the loop | Run computational sensors on every change; reserve inferential for post-integration or high-value checks |
| Sensor messages not LLM-optimized | Generic error messages don't help the agent self-correct | Write custom linter messages with remediation instructions embedded |
| Behaviour harness gap | AI-generated tests trusted uncritically | Supplement with approved fixtures pattern where applicable; maintain manual testing for critical paths |
| Harness coherence drift | Guides and sensors contradict each other as the harness grows | Treat harness as a system; periodically audit for conflicts; use agents to help maintain it |
| Legacy codebase harnessability | Harness most needed where hardest to build | Prioritize highest-risk areas; introduce harnessability improvements incrementally |

## Automated Harness Optimization

Manual harness engineering covers the user harness for a specific codebase, but the **design space is too large to explore by hand** — the combination of retrieval logic, context budgets, routing predicates, tool definitions, and completion conditions is combinatorially large.

Meta-Harness (Lee et al., 2026) demonstrates a complementary approach: an agentic outer loop that searches over harness code, using a coding agent with filesystem access to prior candidates' source code, scores, and raw execution traces. This addresses the exploration problem while still benefiting from a human-built starting harness. Key findings relevant to harness engineers:

- **Execution traces matter more than scores**: giving the proposer raw traces (not compressed summaries) enables it to diagnose specific failure modes and make targeted edits
- **Discovered harnesses generalize**: a harness found by searching on one model transfers to held-out models — harness quality is partially model-independent
- **All harness dimensions are searchable**: the outer loop can jointly optimize system prompts, retrieval logic, context management, and tool definitions in a single search

This shifts the harness engineer's role toward: (1) building a working scaffold that defines the search space, (2) ensuring clean logging of execution traces, and (3) setting up evaluation tasks that represent the target distribution. See [Harness Optimization](./harness-optimization.md) for the full architecture and results.

## Open Questions

- How do we evaluate harness coverage and quality? (Analogous to code coverage and mutation testing for tests)
- How do we keep guides and sensors in sync as the harness grows, preventing contradictions?
- If sensors never fire, is that high quality or inadequate detection?
- How far can agents make sensible trade-offs when instructions and feedback signals conflict?
- What tooling can help configure, sync, and reason about feedforward and feedback controls as a unified system?
- Can automated harness search (e.g., Meta-Harness) be extended to optimize the feedforward/feedback control structure itself, not just retrieval and context management?

## See Also

- [Agent Harness](./agent-harness.md)
- [Harness Optimization](./harness-optimization.md) — automated harness search with Meta-Harness; complements manual harness engineering
- [Code as Agent Harness](./code-as-agent-harness.md) — research survey formalizing code as the executable, inspectable, stateful substrate of agent harnesses
- [The 8 Levels of Agentic Engineering](../MaturityModels/agentic-engineering-levels.md) — harness engineering corresponds to Level 6 in the practitioner progression framework
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Context Engineering Challenges](../ContextEngineering/challenges.md)
- [Agent Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Observability](../ProductionBestPractices/observability.md)
- [Agentic Design Patterns](../DesignPatterns/openai-patterns.md)

## References

- [Meta-Harness: End-to-End Optimization of Model Harnesses — Lee, Nair, Zhang, Lee, Khattab, Finn; arXiv:2603.28052 (March 2026)](https://arxiv.org/abs/2603.28052) — automated harness search via agentic proposer with filesystem access to execution traces; empirical evidence that harness optimization is model-independent
- [Harness Engineering for Coding Agent Users — Birgitta Böckeler, martinfowler.com (April 2, 2026)](https://martinfowler.com/articles/harness-engineering.html) — feedforward/feedback framework, regulation categories, harnessability, and cybernetics framing
- [The Anatomy of an Agent Harness — Vivek Trivedy, LangChain (March 10, 2026)](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) — foundational definition of Agent = Model + Harness
- [Harness Engineering: Leveraging Codex in an Agent-First World — Ryan Lopopolo, OpenAI (February 11, 2026)](https://openai.com/index/harness-engineering) — real-world harness engineering at scale
- [Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems — Ning et al., arXiv:2605.18747 (May 2026)](https://arxiv.org/abs/2605.18747) — research survey formalizing harness mechanisms (planning, memory, tool use, iterative debugging, feedback-driven control) and multi-agent scaling via shared code artifacts
