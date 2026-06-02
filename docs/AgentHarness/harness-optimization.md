# Harness Optimization

## Overview

Harness optimization is the automated search over LLM harness code to discover high-performing configurations without manual design. While agent harnesses are typically designed by hand, empirical evidence shows that the choice of harness can affect task performance as much as (or more than) model selection. Automated harness search treats the harness as a learnable artifact subject to iterative optimization.

The Meta-Harness paper (Lee et al., arXiv:2603.28052, March 2026) demonstrates this concretely: an agentic outer-loop system searches over harness code — the code that determines what information to store, retrieve, and present to the model — and consistently discovers harnesses that outperform hand-engineered baselines.

## The Harness Optimization Problem

A harness is more than a system prompt. It is the full programmatic envelope around the model: retrieval logic, context construction, memory management, tool definitions, completion-checking conditions, and state tracking. Every design decision in this code — which chunks to fetch, how to rank and deduplicate them, when to drop or summarize context, how to format examples — affects task performance.

Existing optimization methods (DSPy, TextGrad, OPRO, ProTeGi) are **poorly matched** to harness optimization for two reasons:

1. **Text vs. code**: They optimize text instructions (prompts, few-shot examples), not the arbitrary code that implements retrieval, branching, and state management.
2. **Feedback compression**: They compress evaluation feedback into short summaries or scalar scores, discarding the detailed execution traces (tool calls, model outputs, intermediate state) that diagnose *why* a candidate failed.

Harness optimization requires a code-editing agent that can reason over raw execution traces — not a text rewriter working from compressed summaries.

## Meta-Harness System Architecture

Meta-Harness is an outer-loop system built around three components:

### Agentic Proposer

The proposer is a **coding agent** (the paper uses Claude Code with Opus 4.6) that reads prior harness candidates from a filesystem and proposes improved harness implementations. Unlike prior optimization methods that receive a condensed gradient or summary, the proposer accesses:

- Source code of all prior candidate harnesses
- Per-candidate evaluation scores
- Raw execution traces: prompts sent, tool calls made, model outputs, state updates

The proposer reads a **median of 82 files per search iteration**, referencing over 20 prior candidates per iteration — a non-Markovian access pattern that exploits the full search history rather than just the previous candidate.

### Filesystem-Based History

Each evaluated harness contributes a directory to the filesystem. The directory contains:

```
candidates/
  run_001/
    harness.py        # source code
    score.json        # evaluation metrics
    traces/           # per-task execution logs
      task_001.json
      task_002.json
      ...
```

This structure gives the proposer up to **10 million tokens of diagnostic context** per iteration — far more than any text optimizer summary can carry. The proposer can grep across prior candidates, compare implementations side by side, and pinpoint specific failure modes from raw traces.

### Search Loop

The outer loop proceeds as:

1. **Initialize** with a baseline harness (hand-engineered or empty scaffold)
2. **Evaluate** the current harness on a training task set; log source, scores, and traces to filesystem
3. **Propose** a new harness: the coding agent reads the filesystem, diagnoses issues, and edits the code
4. **Repeat** — a typical run evaluates approximately 60 harnesses over 20 iterations

The proposer can introduce entirely new logic — custom routing predicates, novel reranking heuristics, adaptive context budgets — rather than just tweaking existing parameters.

## Experimental Results

Meta-Harness was evaluated on three domains:

### Online Text Classification

Compared against a state-of-the-art context management system:
- **+7.7 accuracy points** on the classification task
- **4x fewer context tokens** consumed
- Outcome: discovered harness both outperforms and is more efficient than the hand-engineered baseline

### Retrieval-Augmented Math Reasoning (200 IMO-Level Problems)

Compared against no retrieval, BM25, and dense retrieval:
- **+4.7 accuracy points** on average across **five held-out models** not seen during search
- Discovered harness: a compact **4-route BM25 program** with automatically identified routing predicates for combinatorics, geometry, number theory, and a default route — policy structure that emerged through search rather than being specified manually
- All design choices (routing predicates, reranking terms, deduplication thresholds, per-route example counts) selected by the outer loop across 40 iterations
- Generalizes robustly to unseen tasks and model variants

### Agentic Coding (TerminalBench-2)

Compared against hand-engineered baselines (Terminus 2, Terminus-KIRA):
- Discovered harnesses **surpass all hand-engineered baselines** on task pass rate
- TerminalBench-2 spans 89 Dockerized tasks: code translation, distributed ML setup, systems programming, bioinformatics, cryptanalysis
- Meta-Harness evolves the full coding harness: system prompts, tool definitions, completion-checking logic, and context management jointly

## Implications

### Harness Choice is a Model-Independent Performance Lever

A harness discovered via search on one model transfers to held-out models. This means harness optimization produces **portable improvements** that are not specific to the model used during search — a practical advantage for teams that upgrade models frequently.

### Execution Traces Are the Critical Ingredient

The key architectural decision in Meta-Harness is giving the proposer access to raw execution traces, not just scores. Compressed per-candidate summaries lose the detail needed to diagnose subtle harness failures (wrong retrieval route, context truncation at the wrong point, deduplication threshold too aggressive). Raw traces enable targeted edits.

### Automated Harness Optimization Complements Manual Harness Engineering

Meta-Harness does not replace manual harness engineering — an initial scaffold is still needed, and the proposer benefits from domain knowledge encoded in the baseline harness. However, it addresses the **exploration problem**: the space of possible harness implementations is too large to search by hand, and intuitions about what works often fail for specialized domains (e.g., IMO-level math routing).

## Relationship to Prior Optimization Work

| System | Optimizes | Feedback Signal | Proposer Type |
|---|---|---|---|
| OPRO | Prompts (text) | Scalar score | LLM (text edit) |
| ProTeGi | Prompts (text) | Textual gradient | LLM (text edit) |
| TextGrad | Prompts + parameters | Textual gradient | LLM (text edit) |
| DSPy | Prompts + few-shot demos | Module scores | LLM (text edit) |
| **Meta-Harness** | **Harness code** | **Raw execution traces via filesystem** | **Coding agent** |

The key differentiator is that Meta-Harness optimizes code (not text) and gives the proposer uncompressed diagnostic access through a structured filesystem, rather than compressing feedback into a gradient or summary.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Trace verbosity | Raw execution traces are large | Structure traces as files per task; let the proposer selectively read via grep/cat rather than injecting all traces into every turn |
| Proposer context budget | 10M-token history exceeds single context window | Use a coding agent with filesystem tools; the agent selectively reads relevant prior candidates rather than consuming all context at once |
| Generalization risk | Harness overfit to training task distribution | Evaluate on held-out task subsets and held-out models during search; early stopping if validation gap widens |
| Initialization quality | Poor baseline harness leads to slow convergence | Provide a working hand-engineered baseline as the starting point; include a brief README in the harness directory explaining the domain |
| Log quality | Noisy or incomplete traces impede diagnosis | Ensure all tool calls, model outputs, and state transitions are logged; clean logging of proposer interactions is a hard requirement |
| Search budget | 60 harnesses over 20 iterations is expensive | Run cheaper evaluations (fewer tasks, smaller model) for the first 10 iterations; switch to full evaluation for the top candidates |

## See Also

- [Agent Harness](./agent-harness.md) — what a harness is and its core components
- [Harness Engineering](./harness-engineering.md) — manual harness engineering: feedforward/feedback controls, regulation categories
- [Harness Self-Evolution](./harness-self-evolution.md) — disentangles harness update capability (HUC) from benefit capability (HBC); shows update quality alone does not predict agent improvement
- [Code as Agent Harness](./code-as-agent-harness.md) — code as the executable, inspectable substrate of agent harnesses
- [Context Engineering Strategies](../ContextEngineering/strategies.md) — retrieval, compaction, and isolation strategies that harness optimization configures
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md) — retrieval-augmented generation patterns relevant to harness search
- [Agent Benchmarks](../Benchmarks/agent-benchmarks.md) — TerminalBench-2 and other evaluation environments used in harness optimization
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md) — LLM-as-judge, eval harnesses, and scoring methodologies
- [Production Best Practices: Context Engineering](../ProductionBestPractices/context-engineering.md)

## References

- [Meta-Harness: End-to-End Optimization of Model Harnesses — Lee, Nair, Zhang, Lee, Khattab, Finn; arXiv:2603.28052 (March 2026)](https://arxiv.org/abs/2603.28052) — Stanford / MIT / KRAFTON; introduces the harness optimization problem, filesystem-based diagnostic history, agentic proposer, and empirical results across text classification, RAG math reasoning, and agentic coding
- [Meta-Harness Reference Code — stanford-iris-lab/meta-harness (GitHub)](https://github.com/stanford-iris-lab/meta-harness) — MIT-licensed reference implementation; includes text classification and TerminalBench-2 experiments; ONBOARDING.md for domain adaptation
