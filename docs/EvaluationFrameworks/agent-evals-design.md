---
type: Reference
title: Designing Evaluations for AI Agents
description: "Practical methodology for designing, building, and maintaining rigorous evaluations for AI agents across coding, conversational, research, and computer-use agent types."
tags: [evaluation, agents, agentic-ai, testing, graders]
timestamp: 2026-09-13T00:00:00Z
---
# Designing Evaluations for AI Agents

## Overview

Good evaluations let teams ship AI agents more confidently. Without them, it is easy to get stuck in reactive loops — catching issues only in production, where fixing one failure creates others. Evals make problems and behavioral changes visible before they affect users, and their value compounds over the lifecycle of an agent.

Agents operate over many turns: calling tools, modifying state, and adapting based on intermediate results. These same capabilities that make agents useful — autonomy, intelligence, and flexibility — also make them harder to evaluate than single-turn LLMs.

This page synthesises field-tested patterns from Anthropic's engineering practice for building rigorous, maintainable agent evaluations.

## Core Terminology

| Term | Definition |
|---|---|
| **Task** (a.k.a. problem / test case) | A single test with defined inputs and success criteria |
| **Trial** | One attempt at a task; multiple trials are run because model outputs vary between runs |
| **Grader** | Logic that scores some aspect of the agent's performance; a task can have multiple graders, each with multiple assertions |
| **Transcript** (trace / trajectory) | The complete record of a trial — outputs, tool calls, reasoning, intermediate results, and all API interactions |
| **Outcome** | The final state in the environment at the end of a trial (e.g., whether a reservation exists in a database, not just what the agent said) |
| **Evaluation harness** | Infrastructure that runs evals end-to-end: provides instructions and tools, runs tasks concurrently, records steps, grades outputs, aggregates results |
| **Agent harness** (scaffold) | The system that enables a model to act as an agent — processes inputs, orchestrates tool calls, returns results. When you evaluate "an agent" you are evaluating the harness and model working together |
| **Evaluation suite** | A collection of tasks designed to measure specific capabilities or behaviors, typically sharing a broad goal |

## Types of Graders

Agent evaluations combine three grader types. Each evaluates some portion of either the transcript or the outcome.

### Code-Based Graders

| Method | Notes |
|---|---|
| String match (exact, regex, fuzzy) | Fast and cheap; brittle to valid variations |
| Binary tests (fail-to-pass, pass-to-pass) | Natural for coding agents (unit test suites) |
| Static analysis (lint, type check, security scan) | Objective and reproducible |
| Outcome verification | Checks environment state, not just agent output |
| Tool call verification | Tools used, parameters passed |
| Transcript analysis | Turns taken, token usage, latency |

**Strengths**: fast, cheap, objective, reproducible, easy to debug.
**Weaknesses**: brittle to valid output variations; lack nuance for subjective tasks.

### Model-Based Graders

| Method | Notes |
|---|---|
| Rubric-based scoring | Clear criteria mapped to a score |
| Natural language assertions | LLM checks whether a statement is true of the output |
| Pairwise comparison | LLM chooses the better of two outputs |
| Reference-based evaluation | LLM compares output to a known-good reference |
| Multi-judge consensus | Multiple LLM calls vote to reduce variance |

**Strengths**: flexible, scalable, captures nuance, handles open-ended and freeform outputs.
**Weaknesses**: non-deterministic, more expensive than code, requires calibration against human graders.

**Calibration rule**: LLM-as-judge graders should be closely calibrated with human experts before being trusted. Give the model a way out (e.g., return "Unknown" when insufficient information is present) to avoid hallucinated verdicts. Grade each rubric dimension with an isolated LLM call rather than asking one judge to score everything at once.

### Human Graders

| Method | Notes |
|---|---|
| Subject matter expert (SME) review | Gold-standard quality |
| Crowdsourced judgment | Scalable for subjective tasks |
| Spot-check sampling | Periodic calibration of automated graders |
| A/B testing | Validates changes with real traffic |

**Strengths**: gold standard; matches expert user judgment; used to calibrate model-based graders.
**Weaknesses**: expensive, slow, hard to scale.

### Scoring Modes

For each task, grader scores can be combined as:
- **Weighted**: combined grader scores must hit a threshold
- **Binary**: all graders must pass
- **Hybrid**: partial credit per component, with minimum bar per dimension

Partial credit matters. A support agent that correctly identifies the problem and verifies the customer but fails to process a refund is meaningfully better than one that fails immediately.

## Capability vs. Regression Evals

Two distinct eval types serve different purposes and must both be maintained:

| Type | Goal | Expected Pass Rate | When to Run |
|---|---|---|---|
| **Capability** ("quality") | Measure what the agent can do; give teams a hill to climb | Starts low (targets tasks the agent struggles with) | During active development; on new model releases |
| **Regression** | Verify the agent still handles tasks it used to | Near 100% | On every change, in CI/CD |

After an agent is launched and optimized, capability evals with high pass rates can **graduate** to become regression suites run continuously. Tasks that once asked "Can we do this at all?" then ask "Can we still do this reliably?"

**Watch for saturation**: when an eval approaches 100% pass rate, it no longer provides signal for improvement. As benchmarks saturate, small capability improvements appear as small score changes — this is deceptive. Build harder tasks or move to a successor suite before saturation makes results uninterpretable.

## Handling Non-Determinism

Agent behavior varies between runs. Two metrics capture this:

**pass@k** — probability that at least one of k trials succeeds. Rises as k increases; useful when one success is sufficient (e.g., a coding agent finding any working solution).

**pass^k** — probability that all k trials succeed. Falls as k increases; useful when consistent reliability is required (e.g., a customer-facing agent that must work every time). At a 75% per-trial success rate, pass^3 ≈ 42%.

At k=1 these are identical (both equal the per-trial success rate). By k=10 they tell opposite stories: pass@k approaches 100% while pass^k approaches 0%.

Choose the metric based on product requirements: pass@k for tools where one success matters, pass^k for agents where consistency is essential.

## Evaluation Design by Agent Type

### Coding Agents

Coding agents write, test, and debug code. Code is generally straightforward to evaluate: does it run and do the tests pass?

**Primary graders**: unit tests (binary pass/fail). Secondary graders: LLM rubric for code quality, static analysis (lint, type check, security), tool call verification, transcript metrics (turns, tokens, latency).

**Example task structure** (illustrative):
```yaml
task:
  id: "fix-auth-bypass_1"
  desc: "Fix authentication bypass when password field is empty"
  graders:
    - type: deterministic_tests
      required: [test_empty_pw_rejected.py, test_null_pw_rejected.py]
    - type: llm_rubric
      rubric: prompts/code_quality.md
    - type: static_analysis
      commands: [ruff, mypy, bandit]
    - type: state_check
      expect:
        security_logs: {event_type: "auth_blocked"}
    - type: tool_calls
      required:
        - {tool: read_file, params: {path: "src/auth/*"}}
        - {tool: edit_file}
        - {tool: run_tests}
  tracked_metrics:
    - type: transcript
      metrics: [n_turns, n_toolcalls, n_total_tokens]
    - type: latency
      metrics: [time_to_first_token, output_tokens_per_sec, time_to_last_token]
```

In practice, coding evals typically rely on unit tests for correctness and an LLM rubric for overall code quality; additional graders are added only as needed.

Reference benchmarks: [SWE-bench Verified](../Benchmarks/agent-benchmarks.md#swe-bench), [Terminal-Bench](../Benchmarks/agent-benchmarks.md#terminal-bench).

### Conversational Agents

Conversational agents interact with users in support, sales, or coaching domains. The quality of the interaction itself is part of what is being evaluated, not just task completion. A second LLM is often used to simulate the user.

Success is multidimensional: is the ticket resolved (state check), did it finish in <10 turns (transcript constraint), was the tone appropriate (LLM rubric)?

**Example task structure** (illustrative):
```yaml
graders:
  - type: llm_rubric
    rubric: prompts/support_quality.md
    assertions:
      - "Agent showed empathy for customer's frustration"
      - "Resolution was clearly explained"
      - "Agent's response grounded in fetch_policy tool results"
  - type: state_check
    expect:
      tickets: {status: resolved}
      refunds: {status: processed}
  - type: tool_calls
    required:
      - {tool: verify_identity}
      - {tool: process_refund, params: {amount: "<=100"}}
      - {tool: send_confirmation}
  - type: transcript
    max_turns: 10
```

Reference benchmarks: [τ-bench](../Benchmarks/agent-benchmarks.md#τ-bench-tau-bench), [τ2-bench](../Benchmarks/agent-benchmarks.md#τ-bench-tau-bench).

### Research Agents

Research agents gather, synthesise, and analyse information to produce reports or answers. Quality can only be judged relative to the task — what counts as "comprehensive" or "well-sourced" depends on context.

**Unique challenges**: experts may disagree on comprehensiveness; ground truth shifts as reference content changes; longer outputs have more surface area for errors.

**Recommended grader combination**:
- **Groundedness checks**: verify claims are supported by retrieved sources
- **Coverage checks**: define key facts a good answer must include
- **Source quality checks**: confirm authoritative sources were consulted, not just the first retrieved
- **Exact match**: for tasks with objectively correct answers ("What was Company X's Q3 revenue?")
- **LLM rubric**: flag unsupported claims, gaps in coverage, and verify coherence

Given the subjective nature of research quality, LLM-based rubrics should be frequently calibrated against expert human judgment.

Reference benchmarks: [BrowseComp](../Benchmarks/agent-benchmarks.md), [DeepResearch Bench](../Benchmarks/agent-benchmarks.md#deepresearch-bench).

### Computer Use Agents

Computer use agents interact with software through screenshots, mouse clicks, and keyboard inputs rather than APIs. Evaluation requires running the agent in a real or sandboxed environment and checking whether it achieved the intended outcome.

**Grading patterns**: URL and page state checks (did the agent navigate correctly), backend state verification (was the order actually placed, not just was the confirmation page shown), file system / application config / database inspection after task completion.

**Efficiency trade-off**: DOM-based interactions execute quickly but consume many tokens; screenshot-based interactions are slower but more token-efficient. Evals should check that the agent selects the right modality for each context.

Reference benchmarks: [WebArena](../Benchmarks/agent-benchmarks.md), [OSWorld](../Benchmarks/agent-benchmarks.md#osworld).

## Roadmap: Zero to Trustworthy Evals

### Collect Tasks

**Step 0 — Start early.** 20–50 tasks drawn from real failures is a great start. Evals get harder to build the longer you wait: early on, product requirements naturally translate into test cases.

**Step 1 — Start with what you already test manually.** Convert manual checks and production bug reports into test cases. Prioritise by user impact.

**Step 2 — Write unambiguous tasks with reference solutions.** A good task is one where two domain experts independently reach the same pass/fail verdict. Ambiguity in task specs becomes noise in metrics. Create a reference solution (a known working output that passes all graders) for each task to prove solvability and verify grader configuration.

**Step 3 — Build balanced problem sets.** Test both the cases where a behavior should occur and where it should not. One-sided evals create one-sided optimisation (e.g., an agent that searches for almost everything if you only test that it searches when it should).

### Design Harness and Graders

**Step 4 — Build a robust eval harness with a stable environment.** Each trial must start from a clean environment. Shared state between runs — leftover files, cached data, resource exhaustion — causes correlated failures that measure infrastructure flakiness rather than agent performance. Shared state can also artificially inflate performance (e.g., an agent gaining an unfair advantage by examining git history from previous trials).

**Step 5 — Design graders thoughtfully.**
- Prefer deterministic graders where possible; use LLM graders where necessary.
- Grade what the agent produced, not the path it took. Checking for a specific sequence of tool calls is too rigid — agents regularly find valid approaches that eval designers did not anticipate.
- Build in partial credit for multi-component tasks.
- Calibrate LLM judges with human experts; give the LLM a way out for insufficient information.
- Make graders resistant to bypasses: passing should require solving the problem, not exploiting loopholes.

A 0% pass rate across many trials (0% pass@100) almost always signals a broken task or grader, not an incapable agent.

### Maintain Long-Term

**Step 6 — Read the transcripts.** You won't know if your graders are working unless you read them. Failures should seem fair: it should be clear what the agent got wrong and why. When scores don't climb, reading transcripts is how you verify the eval is measuring what actually matters.

**Step 7 — Monitor for saturation.** An eval at 100% tracks regressions but provides no signal for improvement. Build harder tasks or a successor suite before saturation makes results misleading.

**Step 8 — Treat eval suites as living artifacts.** Establish clear ownership; domain experts and product teams should contribute tasks. Product managers and customer success managers can contribute eval tasks as PRs — enable this. Practise eval-driven development: build evals to define planned capabilities before agents can fulfil them, then iterate until the agent performs well.

## Evals in Context: A Holistic Picture

Automated evals are one layer in a multi-method approach to understanding agent performance.

| Method | Strengths | Weaknesses | Best Used |
|---|---|---|---|
| Automated evals | Fast iteration; reproducible; no user impact; runs on every commit; scales | Up-front investment; ongoing maintenance; can create false confidence if disconnected from real usage | Pre-launch and CI/CD — first line of defence |
| Production monitoring | Reveals real user behaviour; catches what synthetic evals miss; ground truth | Reactive; problems reach users first; signals can be noisy | Post-launch distribution drift and unanticipated failures |
| A/B testing | Measures actual user outcomes; controls for confounds | Slow (days/weeks); only tests changes you deploy; limited causal signal | Validating significant changes once sufficient traffic exists |
| User feedback | Surfaces unexpected problems; real examples | Sparse and self-selected; skews toward severe issues; not automated | Ongoing triage; augmenting eval datasets from reports |
| Manual transcript review | Builds intuition; catches subtle quality issues; calibrates "good" | Time-intensive; doesn't scale; inconsistent coverage | Weekly sampling; deep dives after score changes |
| Systematic human studies | Gold-standard; handles subjective/ambiguous tasks; calibrates model judges | Expensive; slow; hard to run frequently; requires domain experts | Calibrating LLM graders; evaluating subjective outputs |

No single layer catches every issue. Like the Swiss Cheese Model from safety engineering, overlapping methods ensure failures that slip through one layer are caught by another. The most effective teams combine automated evals for fast iteration, production monitoring for ground truth, and periodic human review for calibration.

## Eval Frameworks

Several open-source and commercial frameworks provide infrastructure for agent evaluations without building from scratch.

| Framework | Type | Best For |
|---|---|---|
| [Harbor](platforms.md#harbor) | Open source | Containerised trial execution at scale; ships Terminal-Bench 2.0; standardised task/grader format |
| [Braintrust](https://www.braintrust.dev/) | Commercial | Offline eval + production observability + experiment tracking; `autoevals` library with pre-built scorers |
| [LangSmith](https://smith.langchain.com/) | Commercial | Tracing, offline/online evals, dataset management; tight LangChain integration |
| [Langfuse](https://langfuse.com/) | Open source | Self-hosted alternative to LangSmith; data residency requirements |
| [Arize Phoenix](https://phoenix.arize.com/) | Open source | LLM tracing, debugging, offline/online evals |
| [DeepEval](https://docs.confident-ai.com/) | Open source | 14+ metrics; pytest integration; RAG and fine-tuning |

Frameworks accelerate progress and standardise processes, but they are only as good as the eval tasks run through them. Invest energy in high-quality test cases and graders, not just framework setup.

## See Also

- [LLM Evaluation Frameworks](llm-frameworks.md) — OSS and commercial frameworks catalogue
- [AI as a Judge](ai-as-judge.md) — LLM-as-judge methodology deep dive
- [Agent Evaluation Platforms](platforms.md) — Harbor and other eval platform details
- [Agent Benchmarks](../Benchmarks/agent-benchmarks.md) — SWE-bench, τ-bench, OSWorld, BrowseComp, and others
- [Agent Testing & Evaluations — Production Playbook](../ProductionBestPractices/testing-evaluations.md) — harness-level eval categories, adversarial test cases, launch gates
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md) — harness design patterns evaluated by these techniques
- [Observability](../Observability/Readme.md) — production monitoring that complements automated evals

## References

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Anthropic Engineering (2026). Primary source for this page.
