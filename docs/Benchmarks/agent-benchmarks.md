---
type: Benchmark
title: Agent Evaluation Benchmarks
description: "Agent benchmarks evaluate AI systems on complex, multi-step tasks that require planning, tool use, and autonomous decision-making"
tags: [benchmarks, evaluation, agentic-ai]
timestamp: 2026-09-13T00:00:00Z
---
# Agent Evaluation Benchmarks

## Overview

Agent benchmarks evaluate AI systems on complex, multi-step tasks that require planning, tool use, and autonomous decision-making. Unlike LLM benchmarks that test knowledge and reasoning in isolation, agent benchmarks assess end-to-end task completion in realistic environments.

## General-Purpose Agent Benchmarks

### GAIA
**Resource**: [GAIA: HF Benchmarking General AI Agents](https://huggingface.co/gaia-benchmark)

GAIA (General AI Assistants) is a benchmark for evaluating general-purpose AI agents across diverse tasks requiring multi-step reasoning, tool use, and real-world knowledge. Tasks are designed to be simple for humans but challenging for AI systems, requiring web browsing, file processing, and multi-modal reasoning.

**Key Characteristics**:
- Three difficulty levels (Level 1, 2, 3)
- Tasks require tool use (web search, code execution, file reading)
- Human baseline: ~92% accuracy; top AI systems: ~50-70%
- Hosted on Hugging Face with public leaderboard

### Terminal Bench
**Resource**: [Terminal Bench](https://www.tbench.ai/)

A comprehensive benchmark specifically designed for AI agents operating in terminal/command-line environments. Tests agents on system administration tasks, file manipulation, process management, and shell scripting.

**Key Characteristics**:
- Real terminal environment execution
- Tasks range from basic file operations to complex system administration
- Evaluates both correctness and efficiency of solutions
- Relevant for coding agents and DevOps automation

### TerminalBench-2

An expanded version of Terminal Bench used to evaluate harness-level improvements in agentic coding. Includes 89 Dockerized tasks spanning diverse technical domains. Terminal-Bench 2.0 tasks are implemented in the [Harbor](../EvaluationFrameworks/platforms.md#harbor) task format and executed via the Harbor harness — Harbor reworked the original Terminal-Bench harness to support cloud-deployed containers and a provider-agnostic agent interface.

**Key Characteristics**:
- 89 Dockerized tasks covering code translation, distributed ML setup, systems programming, bioinformatics, and cryptanalysis
- Tests entire agent harness (system prompts, tools, completion-checking logic, context management) — not just model capability
- Used in the Meta-Harness paper to show that automatically discovered harnesses surpass hand-engineered baselines (Terminus 2, Terminus-KIRA)
- Relevant for evaluating harness optimization approaches, not just model selection
- Strong baselines: Terminus 2 and Terminus-KIRA provide hand-engineered orchestration paradigms
- Official harness: [Harbor](../EvaluationFrameworks/platforms.md#harbor) — supports running agents like Claude Code, OpenHands, and Codex CLI against the task set across distributed cloud sandbox providers

### Terminal-Bench 2.1
**Resource**: [Terminal Bench](https://www.tbench.ai/)

An incremental update to TerminalBench-2 with an expanded task set, improved Dockerized environments, and refined evaluation methodology. Maintains backward compatibility with TerminalBench-2 baselines while adding coverage for newer technical domains.

**Key Characteristics**:
- Expanded task count beyond the 89 tasks in TerminalBench-2, with new domains added
- Improved Docker environment stability and reproducibility for more reliable automated scoring
- Refined completion-checking logic to reduce ambiguous pass/fail edge cases
- Continues to evaluate the full agent harness rather than isolated model capability
- Backward-comparable with TerminalBench-2 results for longitudinal tracking of agent progress
- Runs on the same [Harbor](../EvaluationFrameworks/platforms.md#harbor) harness as TerminalBench-2

### METR (Model Evaluation & Threat Research)
**Resource**: [METR](https://metr.org/)

METR is a research organization that develops and runs evaluations of frontier AI systems' ability to complete complex tasks without human input. Focuses on autonomous capability assessment for safety research, particularly evaluating whether AI systems can perform tasks that could pose risks if misused.

**Key Characteristics**:
- Focus on long-horizon autonomous tasks
- Safety-oriented evaluation methodology
- Used by major AI labs for pre-deployment assessment
- Evaluates tasks requiring sustained autonomy over hours

## Web and Computer Interaction Benchmarks

### VisualWebArena
**Resource**: [VisualWebArena](https://github.com/web-arena-x/visualwebarena)

A benchmark for multimodal agents that interact with web interfaces using both visual and textual information. Extends WebArena with visual understanding requirements, testing agents on realistic web tasks that require interpreting screenshots and UI elements.

**Key Characteristics**:
- Multimodal (vision + text) agent evaluation
- Realistic web application environments (shopping, forums, classifieds)
- Tasks require understanding visual UI elements
- Measures task completion rate and efficiency

### OSWorld
**Resource**: [OSWorld Benchmark for Multimodal Agents](https://os-world.github.io/)

Benchmarks multimodal agents for open-ended tasks in real computer environments. Agents interact with actual operating systems (Windows, macOS, Ubuntu) through screenshots and keyboard/mouse actions, testing real-world computer use capabilities.

**Key Characteristics**:
- Real OS environments (not simulated)
- Tasks span web browsing, office applications, coding, file management
- Evaluates agents that control computers like humans
- Relevant for computer-use agents (e.g., Claude Computer Use, Operator)

### OSWorld-Verified

A curated subset of OSWorld tasks where human annotators have verified that each task is unambiguously solvable and the automated evaluation function produces accurate results. Designed to provide a higher-quality, lower-noise evaluation signal than the full OSWorld set.

**Key Characteristics**:
- Human-verified task solvability — reduces false negatives from unanswerable or ambiguously specified tasks
- Accurate evaluation functions validated by annotators — reduces false positives from flawed graders
- Preferred over the full OSWorld set when benchmark reliability matters more than breadth
- Analogous in philosophy to SWE-bench Verified: curated correctness over raw volume
- Useful as a calibration reference when comparing agent systems across papers

## Software Development Benchmarks

### SWE-Bench
**Resource**: [SWE-Bench](https://www.swebench.com/)

A dataset that tests AI systems' ability to solve real GitHub issues automatically. Agents must understand codebases, reproduce bugs, and implement fixes that pass existing test suites. SWE-Bench Verified is a curated subset with human-verified solvability.

**Key Characteristics**:
- 2,294 real GitHub issues from popular Python repositories
- Requires understanding large codebases
- Evaluation via automated test suite execution
- Industry standard for coding agent evaluation

### SWE-bench Pro

A significantly harder extension of SWE-bench targeting production-grade software engineering challenges. Issues are drawn from more complex, real-world scenarios that require multi-file edits, deeper codebase understanding, and reasoning across larger contexts than the original benchmark.

**Key Characteristics**:
- Harder task selection: issues require more reasoning steps, broader codebase context, and multi-file changes compared to standard SWE-bench
- Longer effective context requirements — agents must navigate large, unfamiliar codebases
- Designed to differentiate top-tier coding agents where standard SWE-bench scores are converging
- Maintains the same automated test-suite evaluation methodology as the original
- Relevant for teams building or selecting agents for production software engineering workflows

### DeepSWE

**Resource**: [deepswe.datacurve.ai](https://deepswe.datacurve.ai/) | [Paper (arXiv 2607.07946)](https://arxiv.org/abs/2607.07946) | [GitHub](https://github.com/datacurve-ai/deep-swe)

DeepSWE, by Datacurve, is a contamination-free benchmark of 113 original long-horizon software engineering tasks designed to differentiate frontier coding agents where saturating benchmarks like SWE-bench Pro can no longer separate them. Tasks are written from scratch — not adapted from existing commits or PRs — ensuring no model has seen solutions during pretraining.

**Key Characteristics**:
- **113 tasks** across **91 repositories** and **5 languages**: TypeScript, Go, Python, JavaScript, and Rust
- **Contamination-free**: all tasks are original, not drawn from existing GitHub issues or PRs
- **High complexity**: prompts are roughly half the length of SWE-bench Pro's, yet solutions require ~5.5× more code and ~2× more output tokens than SWE-bench Pro tasks
- **Behavior-based verification**: hand-written verifiers test software behavior rather than implementation details, avoiding the high false-positive/false-negative rates found in automated test-suite graders
- **Consistent scaffolding**: all models run on mini-swe-agent for apples-to-apples comparison
- **Live leaderboard** updated continuously (last updated September 3, 2026; 28 models evaluated)

**Current leaderboard leaders** (Pass@1, as of September 2026):
- gpt-6-astra: 74% ±3% ($6.52/task, 29 steps)
- gemini-3.8-flash: 74% ±1% ($2.36/task, 166 steps)
- claude-opus-5: 74% ±4% ($11.84/task, 99 steps)

**Why it matters**: Addresses three key gaps in existing coding benchmarks — (1) SWE-bench Pro's verifier misgrading rates (~8% false positives, ~24% false negatives flagged in the DeepSWE audit), (2) benchmark contamination from tasks derived from public GitHub history, and (3) task complexity ceilings where top models cluster within overlapping confidence intervals. DeepSWE's real-world task diversity (91 repos, 5 languages, complex multi-file changes) provides a more reliable signal for selecting or comparing frontier coding agents.

### ALE-Bench
**Resource**: [ALE-Bench Leaderboard](https://sakanaai.github.io/ALE-Bench-Leaderboard/) | [Paper (NeurIPS 2025)](https://arxiv.org/abs/2506.09050) | [GitHub](https://github.com/SakanaAI/ALE-Bench)

A benchmark for long-horizon, objective-driven algorithm engineering, developed by Sakana AI and accepted to NeurIPS 2025 (Datasets & Benchmarks track). Draws problems from the AtCoder Heuristic Contest (AHC) — real competitive programming contests focused on NP-hard optimization problems that have no known exact solution. Unlike pass/fail coding benchmarks, ALE-Bench rewards iterative improvement toward a numeric score, mirroring how human contestants spend days or weeks refining algorithms.

**Key Characteristics**:
- **40 problems** sourced from AHC contests held through April 2025; a lite subset of 10 representative problems is also provided
- **Score-based evaluation** (not pass/fail): agents are scored on solution quality against a continuous numeric objective, enabling fine-grained comparison
- **Long time horizon**: encourages iterative refinement across many iterations — agents submit code, observe test-run feedback and visualizations, and improve their solutions in a loop
- **Domains**: routing, planning, multi-agent control, puzzle-solving, Bayesian inference, and other NP-hard combinatorial optimization problems
- **Scoring metrics**: per-problem raw score, contest rank among ~1,000 human competitors, and an Elo-like performance rating; aggregated as mean/median across the suite
- **ALE-Agent** (Sakana AI's reference agent): achieved a top-21 finish out of ~1,000 participants in a live AtCoder Heuristic Competition, validating benchmark-to-real-competition transferability
- Complements SWE-bench (bug-fixing, pass/fail) with a fundamentally different evaluation axis: continuous optimization under a time budget rather than binary correctness

## Multi-Agent and Collaboration Benchmarks

### AgentBench
A comprehensive benchmark evaluating LLMs as agents across 8 distinct environments including operating systems, databases, knowledge graphs, digital card games, lateral thinking puzzles, house-holding tasks, web shopping, and web browsing.

### τ-bench (Tau-bench)
Evaluates agents on realistic customer service scenarios requiring multi-turn conversations, policy adherence, and tool use. Tests agents' ability to follow complex business rules while serving customers effectively. One model plays a user persona while the agent navigates scenarios in domains like retail support and airline booking.

### τ2-bench (Tau2-bench)
The successor to τ-bench, extending multi-turn evaluation to more complex and adversarial scenarios. Simulates extended, realistic conversations where agents must navigate policy edge cases, handle frustrated users, and maintain consistent behavior across many turns. Used by Anthropic internally to stress-test models through adversarial conversations, including in alignment auditing workflows.

**Key Characteristics**:
- Multi-turn interaction simulation across retail and airline booking domains
- One model plays a user persona; the agent must navigate realistic policy constraints
- Tests both task completion and interaction quality as separate dimensions
- Extended conversation length exposes consistency failures not visible in shorter evals
- Adversarial variants used for alignment auditing — stress-testing model behavior under sustained pressure

## Agent Memory Benchmarks

### LongMemEval
**Resource**: [Paper (ICLR 2025)](https://arxiv.org/abs/2410.10813) | [GitHub](https://github.com/xiaowu0162/LongMemEval) | [Website](https://xiaowu0162.github.io/long-mem-eval/)

LongMemEval (Wu et al., UCLA NLP) benchmarks chat assistants on long-term interactive memory across extended multi-session histories. It formalizes a three-stage memory architecture — Indexing, Retrieval, Reading — and evaluates five core memory abilities against 500 hand-curated questions paired with timestamped chat histories.

**Five Core Memory Abilities**:
- **Information Extraction**: Retrieve specific facts stated in past sessions
- **Multi-Session Reasoning**: Synthesize information spread across multiple conversations
- **Temporal Reasoning**: Understand and reason about when events occurred relative to the query
- **Knowledge Updates**: Handle cases where information changes or is contradicted over time
- **Abstention**: Recognize when the answer is not present in memory (correct refusal)

**Key Characteristics**:
- 500 questions across 7 task categories: single-session-user, single-session-assistant, single-session-preference, temporal-reasoning, knowledge-update, multi-session, and abstention variants
- Three difficulty variants: LongMemEval_S (~115k tokens, ~40 sessions), LongMemEval_M (~500 sessions per history), LongMemEval_Oracle (oracle retrieval upper bound)
- Attribute-controlled pipeline generates coherent, extensible, timestamped chat histories inspired by "needle-in-a-haystack" methodology
- GPT-4o automatic QA evaluation; supports both turn-level and session-level memory recall metrics
- Systems evaluated include BM25, Contriever, Stella, and GTE embeddings; RAG with key expansion strategies (summarization, keyphrase extraction, user facts extraction)
- Accepted at ICLR 2025

### LongMemEval-V2
**Resource**: [Paper (arXiv 2605.12493, May 2026)](https://arxiv.org/abs/2605.12493) | [Website](https://xiaowu0162.github.io/long-mem-eval/)

LongMemEval-V2 (Wu et al., UCLA NLP) extends the benchmark to the agentic context, evaluating whether memory systems help web agents accumulate environment-specific experience — framing the goal as developing "knowledgeable colleagues" rather than accurate chat assistants. V2 shifts from conversational history to action trajectories in specialized web environments.

**Five Agentic Memory Abilities**:
- **Static State Recall**: Remember fixed facts about an environment (UI layout, available fields, configuration)
- **Dynamic State Tracking**: Track how environment state changes across agent trajectories
- **Workflow Knowledge**: Recall multi-step procedures for accomplishing recurring tasks
- **Environment Gotchas**: Remember known failure modes, edge cases, and workarounds
- **Premise Awareness**: Recognize when preconditions for a task are not satisfied

**Key Characteristics**:
- 451 manually curated questions
- Up to 500 trajectories per history; up to 115M tokens total — substantially larger context than V1
- Environments drawn from WebArena and WorkArena: Magento shopping, shopping admin, Postmill forum, ServiceNow
- Targets procedural and environmental memory gaps not addressed by V1's focus on user preference recall
- Authors: Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang (UCLA NLP)

## Research and Retrieval Benchmarks

### BrowseComp

A benchmark for testing whether AI agents can find specific, hard-to-locate facts across the open web — "needles in haystacks" that are easy to verify once found but difficult to locate. Designed to test research agent capability rather than general knowledge: questions are answerable by a determined human researcher but require navigating multiple pages and sources.

**Key Characteristics**:
- Questions are designed to be easy to verify but hard to solve — correct answers can be confirmed immediately, eliminating ambiguity in grading
- Targets retrieval and navigation skill rather than memorised knowledge
- Graded with exact-match or verifiable-fact checks, making it deterministic despite open-web scope
- Relevant for teams building research agents, deep-research pipelines, or web-browsing agents
- Used by Anthropic as a reference point for evaluating research-oriented agent capability

### DeepResearch Bench

**Resource**: [Project Page](https://deepresearch-bench.github.io/) | [Paper (arXiv 2506.11763)](https://arxiv.org/abs/2506.11763) | [GitHub](https://github.com/Ayanami0730/deep_research_bench) | [Dataset](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset) | [Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)

DeepResearch Bench (DRB), from researchers at the University of Science and Technology of China (USTC), is a benchmark for systematically evaluating **Deep Research Agents (DRAs)** — LLM-based agents that autonomously orchestrate multi-step web exploration, targeted retrieval, and higher-order synthesis to produce analyst-grade, citation-rich research reports.

**Key Characteristics**:
- 100 PhD-level research tasks (50 Chinese, 50 English) spanning 22 topic domains: Science & Technology (physics, chemistry, biology, environmental science, engineering), Finance & Business (investments, personal finance, marketing, HR), Software, and others (Art & Design, Entertainment, History, Industrial, Transportation, Travel)
- Domain distribution derived from analysis of 96,147 anonymized real user queries from web-search-enabled LLM interactions, classified via the WebOrganizer taxonomy to reflect authentic research demand
- Tasks authored and screened by PhD-level domain experts and senior practitioners (5+ years' experience) for quality, clarity, authenticity, and challenge level

**Evaluation Frameworks**:
- **RACE (Reference-based Adaptive Criteria-driven Evaluation)**: scores generated reports against reference reports across four dimensions — comprehensiveness, insight/depth, instruction-following, and readability — using dynamically generated, task-specific weighted criteria
- **FACT (Framework for Factual Abundance and Citation Trustworthiness)**: extracts statement-URL pairs (factual claims and cited sources) from a report, deduplicates them, and uses web scraping plus LLM judgment to verify whether each source supports its claim, yielding citation accuracy and effective-citations-per-task metrics

**Evaluation Infrastructure**:
- Initial evaluator setup (July 2025): Gemini-2.5-Pro for RACE, Gemini-2.5-Flash for FACT; evaluated DRAs included Kimi-Researcher, Doubao-DeepResearch, and Claude-Researcher, with raw articles and scores published on the Hugging Face leaderboard
- *(Updated: as of May 2026, the official evaluator transitioned to GPT-5.5 for RACE and GPT-5.4-mini for FACT, following Google's announced deprecation of Gemini-2.5-Pro. Against a human inter-annotator agreement baseline of 68.78%, candidate evaluators scored — GPT-5.5: 71.82% overall (PAR 73.00, OPC 89.70, FAP 65.35, FAS 59.23); Gemini-3.1-Pro: 70.58%; Claude-Opus-4-7: 70.11%. A dual-acceptance window through 31 May 2026 accepted submissions under both the legacy (Gemini-2.5-Pro) and new (GPT-5.5) evaluators on separate leaderboards; legacy code is preserved on the `Gemini-2.5` branch)*

**Licensing**: Benchmark code under MIT license; dataset and leaderboard hosted on Hugging Face

**Related**: **DeepResearch Bench II (DRB II)** (Feb 2026, [paper](https://arxiv.org/abs/2601.08536)) is a follow-up benchmark from the same lab that evaluates DRA reports against 9,430 fine-grained binary rubrics (information recall, analysis, presentation) derived from expert-written articles — a different evaluation focus from DRB. DRB continues to be maintained independently alongside DRB II.

### WANDR

WANDR (Wide And Nuanced Deep Research) evaluates agents on "wide research" tasks that require careful orchestration of search, compute, and model reasoning. It is inspired by the knowledge-intensive professional tasks that Perplexity Computer handles for users and iterates on WideSearch and similar benchmarks with emphasis on more complex task structures and multi-source synthesis requirements.

**Key Characteristics**:
- Tasks require multi-step, multi-source research workflows rather than single-query retrieval
- Evaluates orchestration quality — the agent must decide which retrieval strategies to use, in what order, and how to aggregate results
- Graded on accuracy, citation correctness, and structured output completeness
- Designed to expose the limits of fixed RAG pipelines versus adaptive retrieval strategies
- Perplexity's Search as Code (SaC) architecture achieves a 2.5× advantage over the next-best system on WANDR
- Relevant for teams building research agents, knowledge synthesis pipelines, or competitive intelligence systems

**Reference**: [Rethinking Search as Code Generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation), Perplexity AI Research, September 2025.

## Domain-Specific Agent Benchmarks

### Finance Agent v2

A domain-specific benchmark evaluating AI agents on complex financial tasks requiring multi-step reasoning, tool use, and domain expertise. Version 2 extends the original with harder tasks and broader financial domain coverage.

**Key Characteristics**:
- Tasks span market analysis, portfolio construction, financial document interpretation, earnings call analysis, and regulatory compliance reasoning
- Requires integration of external data sources (market feeds, SEC filings, financial statements) via tool use
- Multi-step reasoning chains: agents must chain retrieval, calculation, and interpretation steps to produce final answers
- Graded against expert-annotated ground truth rather than automated test suites
- Relevant for teams building financial AI assistants, trading agents, or compliance automation systems
- Version 2 adds more complex portfolio optimization scenarios and cross-document reasoning tasks compared to v1

## Benchmark Selection Guide

| Use Case | Recommended Benchmark |
|----------|----------------------|
| General agent capability | GAIA |
| Web automation | VisualWebArena |
| Computer use (broad) | OSWorld |
| Computer use (reliable signal) | OSWorld-Verified |
| Software development (standard) | SWE-Bench |
| Software development (hard/production) | SWE-bench Pro |
| Software development (contamination-free, frontier) | DeepSWE |
| Algorithm engineering / optimization | ALE-Bench |
| Terminal/CLI tasks | Terminal-Bench 2.1 |
| Safety evaluation | METR |
| Customer service agents | τ-bench / τ2-bench |
| Financial domain agents | Finance Agent v2 |
| Wide/deep research orchestration | WANDR |
| Open-web needle-in-haystack research | BrowseComp |
| Deep research report quality & citation accuracy | DeepResearch Bench |
| Long-term memory (chat assistants) | LongMemEval |
| Long-term memory (web agents) | LongMemEval-V2 |

## Evaluation Considerations

### Reproducibility
Agent benchmarks are harder to reproduce than static LLM benchmarks due to:
- Non-deterministic LLM outputs
- Dynamic web environments that change over time
- Dependency on external APIs and services

### Cost
Running agent benchmarks is expensive — each task may require dozens of LLM calls and tool executions. Budget accordingly and use smaller evaluation subsets for rapid iteration.

### Leaderboard Contamination
As benchmarks become public, training data contamination becomes a concern. Prefer benchmarks with held-out test sets or those that regularly refresh their task sets.

## See Also

- [LLM Benchmarks](llm-benchmarks.md)
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md)
- [Designing Evaluations for AI Agents](../EvaluationFrameworks/agent-evals-design.md) — grader types, pass@k/pass^k metrics, and per-agent-type eval design patterns
- [Agent Evaluation Platforms — Harbor](../EvaluationFrameworks/platforms.md#harbor) — the open-source harness that executes Terminal-Bench 2.0/2.1 at scale
- [Observability](../Observability/Readme.md)
- [Harness Optimization](../AgentHarness/harness-optimization.md) — TerminalBench-2 as a harness-level evaluation environment
- [Search as Code](../RAG/search-as-code.md) — Perplexity's SaC architecture; introduces the WANDR benchmark
- [Agent Memory Research Papers](../AgentMemory/research-papers.md) — LongMemEval foundational papers and memory architecture research
- [Long-Term Memory Strategies](../AgentMemory/ltm-strategies.md) — retrieval and consolidation patterns evaluated by LongMemEval
