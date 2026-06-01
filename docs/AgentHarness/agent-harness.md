# Agent Harness

## Overview

An agent harness is everything that wraps a model to make it useful — every piece of code, configuration, and execution logic that is not the model itself. The core equation is:

> **Agent = Model + Harness**

A raw model takes in data (text, images, audio, video) and outputs text. It cannot maintain durable state, execute code, access real-time knowledge, or set up environments. The harness provides all of these capabilities. If you are not the model, you are the harness.

This framing, articulated by LangChain (Vivek Trivedy, March 2026), forces a clean separation of concerns: the model contains the intelligence; the harness makes that intelligence useful.

## Core Components

A harness concretely includes:

| Component | Description |
|---|---|
| **System Prompts** | Instructions injected at agent start that shape behavior, persona, and constraints |
| **Tools, Skills, MCPs** | Callable functions and their descriptions; the action space available to the model |
| **Bundled Infrastructure** | Filesystem, sandbox, browser — the execution environment |
| **Orchestration Logic** | Subagent spawning, handoffs, model routing, loop control |
| **Hooks / Middleware** | Deterministic execution wrappers: compaction triggers, continuation logic, lint checks |

## Why Harnesses Exist: Working Backwards from Model Limitations

Each harness component exists to close a gap between what a model can do natively and what an agent needs to do in practice.

### Filesystems — Durable Storage and Context Management

Models can only operate on knowledge within their context window. Filesystems solve this by giving agents a workspace to read data, code, and documentation; a place to store intermediate outputs that outlast a single session; and a natural collaboration surface for multiple agents and humans.

Git adds versioning to the filesystem so agents can track work, roll back errors, and branch experiments. The filesystem is arguably the most foundational harness primitive because it unlocks every other capability.

### Bash + Code Execution — General-Purpose Tool

Rather than forcing users to pre-build tools for every possible action, giving agents a bash tool lets them design their own tools on the fly via code. The standard agent execution pattern is a [ReAct loop](https://docs.langchain.com/oss/python/langchain/agents) — reason, act via tool call, observe result, repeat. Bash + code execution makes this loop general-purpose.

### Sandboxes — Safe, Scalable Execution Environments

Running agent-generated code locally is risky and does not scale. Sandboxes provide:
- Secure, isolated code execution
- Allow-listed commands and network isolation for security
- On-demand environment creation and teardown for scale
- Pre-installed runtimes, CLIs, and browsers for useful defaults

Browsers, logs, screenshots, and test runners give agents self-verification loops: write code → run tests → inspect logs → fix errors.

### Memory and Search — Continual Learning

Models have no knowledge beyond their weights and current context. Harnesses extend this via:
- **Memory file standards** (e.g., AGENTS.md) injected into context on agent start; as agents edit these files, updated knowledge persists across sessions — a form of continual learning
- **Web search and MCP tools** (e.g., Context7) for up-to-date knowledge beyond the training cutoff

### Hooks and Middleware — Deterministic Execution Control

Hooks intercept model behavior at defined points to enforce deterministic outcomes:
- **Compaction hooks**: triggered when context approaches the window limit; intelligently summarize and offload context so the agent can continue
- **Tool call offloading**: keeps head and tail tokens of large tool outputs; offloads full output to filesystem
- **Skills / progressive disclosure**: loads only relevant tool descriptions into context on demand, preventing context rot from too many tools at startup
- **The Ralph Loop**: a hook pattern that intercepts the model's exit attempt and reinjects the original prompt in a clean context window, forcing the agent to continue toward a completion goal

## Orchestration for Long-Horizon Work

Long-horizon autonomous execution requires all harness primitives to compound:

- **Filesystems + git** track work across sessions; new agents can quickly get up to speed on project history
- **Planning tools** let agents decompose tasks, track progress, and adapt as they learn
- **Subagent spawning** delegates independent subtasks in parallel, each with isolated context
- **Self-verification loops** (test runners, lint checks, browser validation) ground solutions in observable outcomes

## The Model–Harness Co-Evolution Loop

Modern agent products (Claude Code, Codex) are post-trained with models and harnesses in the loop. This creates a feedback cycle:

1. Useful harness primitives are discovered and added
2. Models are trained with those primitives in the loop
3. Models become more capable within that harness
4. New primitives are discovered

A side effect is overfitting: changing tool logic can degrade model performance because the model was trained expecting specific harness behavior. This also means the best harness for a given task is not necessarily the one a model was post-trained with — harness optimization for a specific task can yield significant performance gains independent of model capability.

## Automated Harness Optimization

Because harnesses are code, the space of possible harness implementations is too large to explore by hand. Recent work demonstrates that harnesses can be **automatically searched** using an agentic outer loop, yielding harnesses that outperform hand-designed alternatives.

Meta-Harness (Lee et al., 2026) treats harness optimization as a code search problem: an agentic proposer (a coding agent with full filesystem access to prior candidates' source code, scores, and execution traces) iteratively proposes improved harness implementations. Key results:

- **+7.7 accuracy points** on text classification over a state-of-the-art context management baseline, using **4x fewer tokens**
- **+4.7 accuracy points** on 200 IMO-level math problems, averaging across five held-out models not seen during search
- Surpasses all hand-engineered baselines on TerminalBench-2 agentic coding tasks

A discovered harness generalizes across model families — the search can be run on one model and the resulting harness deployed on others. This makes harness optimization a **model-independent performance lever**, complementary to model selection and prompt engineering.

The critical design choice is giving the proposer access to raw execution traces (not compressed summaries), so it can diagnose specific failure modes before proposing targeted edits. See [Harness Optimization](./harness-optimization.md) for the full system architecture and best practices.

## Harness vs. Model Responsibility Over Time

As models become more capable, some harness responsibilities will be absorbed natively (planning, self-verification, long-horizon coherence). However, harnesses will remain valuable because:
- A well-configured environment, the right tools, durable state, and verification loops make any model more efficient regardless of base intelligence
- Harnesses engineer systems *around* model intelligence, not just patch over deficiencies

## Code as the Harness Substrate

A 2026 survey (Ning et al., arXiv:2605.18747) formalizes a complementary view: rather than code being one harness component among many, code increasingly serves as the **unifying substrate** of the entire harness — the medium through which agents reason, act, model environments, receive feedback, and coordinate.

Code has three structural properties unavailable to text-based harnesses:
- **Executability**: model outputs become verifiable operations, not just text
- **Inspectability**: intermediate computation is exposed as structured traces
- **Statefulness**: task progress is represented persistently across context windows

The survey organizes this into three layers: (1) harness interface — code connecting agents to reasoning, action, and environment modeling; (2) harness mechanisms — planning, memory, tool use, and iterative debugging; (3) harness scaling — multi-agent coordination over shared code artifacts. See [Code as Agent Harness](./code-as-agent-harness.md) for the full taxonomy.

## Formal Taxonomy: ETCLOVG

A 2026 survey (submitted to TMLR) proposes the **ETCLOVG seven-layer taxonomy** as a formal classification for harness systems, separating structural pillars from control-plane layers:

- **Structural pillars**: Execution (E), Tooling (T), Context (C), Lifecycle (L) — what an agent can do
- **Control plane**: Observability (O), Verification (V), Governance (G) — how safely and reliably it operates

A companion survey (Meng et al., arXiv:2605.29682) formalizes a six-component architectural tuple **H=(E,T,C,S,L,V)** — Execution Loop, Tool Registry, Context Manager, State Store, Lifecycle Hooks, Evaluation Interface — using labeled-transition-system semantics that distinguish safety invariants from liveness guarantees. Evaluating 23 systems against this model, the survey finds that only Claude Code, PRISM/OpenClaw, AIOS, OpenHands, and SWE-agent implement all six components. See [LLM Harness Survey](./llm-harness-survey.md) for the full taxonomy, completeness matrix, and empirical benchmarks.

## Harness Maturity Levels

A provider-neutral progression for building up harness capability. Move up levels only when evals show the simpler level is insufficient.

| Level | Name | Capabilities | When to Use |
|---|---|---|---|
| 0 | Answer-only assistant | No tool execution | Short Q&A, drafting, summarization over provided content |
| 1 | Retrieval agent | Search and read trusted resources; no side effects | Lookup, research, read-only workflows |
| 2 | Drafting agent | Propose actions, draft messages, produce plans; cannot commit | Pre-approval content creation, planning |
| 3 | Approval-gated actor | Prepare and execute actions after explicit user or policy approval | CRM updates, emails, database writes |
| 4 | Policy-bounded autonomous actor | Execute low-risk actions autonomously within strict scopes, budgets, and audit controls | Scoped automation with guardrails |
| 5 | Long-running goal worker | Continue across turns or sessions toward a measurable objective; requires durable state, compaction, checkpoints | Multi-session research, large-scale automation |

Most agent failures are caused by starting too high — broad tools, missing approval gates, and no evals before reaching Level 3+.

## Authority Hierarchy

The harness should maintain an explicit authority hierarchy and label content by authority level. Retrieved content may contain instructions, but those instructions are data, not policy.

```
provider/system policy
  → organization policy
  → product/developer policy
  → workspace/project policy
  → domain or directory policy
  → user task
  → model-visible runtime reminders
  → tool observations
  → untrusted retrieved content
```

The trusted control plane (user identity, credentials, approval records, audit logs, billing, authorization) must stay outside model-directed compute. Secrets, approval logic, and authorization decisions must never live inside the model prompt.

## See Also

- [Harness Engineering](./harness-engineering.md)
- [Pi (pi.dev)](./pi-dev.md) — minimal open-source terminal coding agent harness; four-tool core (read, write, edit, bash), sub-1K-token system prompt, 15+ providers, fully extensible via TypeScript packages
- [Flue](../AgenticFrameworks/flue.md) — open-source TypeScript agent harness framework; implements the Agent = Model + Harness pattern with built-in sandbox, sessions, and skills
- [Harness Optimization](./harness-optimization.md) — automated harness search with Meta-Harness (Lee et al., 2026)
- [Code as Agent Harness](./code-as-agent-harness.md) — survey taxonomy of code as the agent substrate (Ning et al., 2026)
- [LLM Harness Survey](./llm-harness-survey.md) — ETCLOVG taxonomy, harness completeness matrix, nine technical challenges, empirical benchmarks
- [Agentic Engineering Levels](../MaturityModels/agentic-engineering-levels.md) — harness engineering is Level 6 in the 8-level practitioner progression
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [Agent Memory Management](../AgentMemory/functional-tiers.md)
- [Agentic Design Patterns](../DesignPatterns/openai-patterns.md)
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [Context Engineering: Key Challenges](../ContextEngineering/challenges.md)

## References

- [agents-best-practices — DenisSergeevitch (2025)](https://github.com/DenisSergeevitch/agents-best-practices) — provider-neutral agent harness skill; covers loop invariants, maturity levels, permission model, planning mode, context compaction, and launch gates
- [Agent Harness for Large Language Model Agents: A Survey — Meng et al., arXiv:2605.29682 (2026)](https://arxiv.org/pdf/2605.29682) — H=(E,T,C,S,L,V) formal model with LTS semantics; Harness Completeness Matrix for 23 systems; eight future directions; 110+ papers annotated
- [Agent Harness Engineering: A Survey — picrew et al., OpenReview / TMLR submission (2026)](https://openreview.net/forum?id=3hXEPbG0dh) — proposes ETCLOVG seven-layer taxonomy; evaluates 23+ systems; establishes harness design as the binding performance constraint (tool format optimization: 6.7% → 68.3% on SWE-bench)
- [Meta-Harness: End-to-End Optimization of Model Harnesses — Lee, Nair, Zhang, Lee, Khattab, Finn; arXiv:2603.28052 (March 2026)](https://arxiv.org/abs/2603.28052) — automated harness search; agentic proposer with filesystem-based history; +7.7 points on text classification, +4.7 points on IMO math reasoning, surpasses hand-engineered baselines on TerminalBench-2
- [The Anatomy of an Agent Harness — Vivek Trivedy, LangChain (March 10, 2026)](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) — defines the harness concept and derives core components from model limitations
- [Harness Engineering: Leveraging Codex in an Agent-First World — Ryan Lopopolo, OpenAI (February 11, 2026)](https://openai.com/index/harness-engineering) — real-world harness engineering lessons from building a million-line codebase with zero manually-written code
- [Harness Engineering for Coding Agent Users — Birgitta Böckeler, martinfowler.com (April 2, 2026)](https://martinfowler.com/articles/harness-engineering.html) — feedforward/feedback framework, regulation categories, and harnessability concepts
- [Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems — Ning et al., arXiv:2605.18747 (May 2026)](https://arxiv.org/abs/2605.18747) — 197-paper survey establishing executability, inspectability, and statefulness as structural harness properties; three-layer taxonomy (interface, mechanisms, scaling)
