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

An expanded version of Terminal Bench used to evaluate harness-level improvements in agentic coding. Includes 89 Dockerized tasks spanning diverse technical domains.

**Key Characteristics**:
- 89 Dockerized tasks covering code translation, distributed ML setup, systems programming, bioinformatics, and cryptanalysis
- Tests entire agent harness (system prompts, tools, completion-checking logic, context management) — not just model capability
- Used in the Meta-Harness paper to show that automatically discovered harnesses surpass hand-engineered baselines (Terminus 2, Terminus-KIRA)
- Relevant for evaluating harness optimization approaches, not just model selection
- Strong baselines: Terminus 2 and Terminus-KIRA provide hand-engineered orchestration paradigms

### Terminal-Bench 2.1
**Resource**: [Terminal Bench](https://www.tbench.ai/)

An incremental update to TerminalBench-2 with an expanded task set, improved Dockerized environments, and refined evaluation methodology. Maintains backward compatibility with TerminalBench-2 baselines while adding coverage for newer technical domains.

**Key Characteristics**:
- Expanded task count beyond the 89 tasks in TerminalBench-2, with new domains added
- Improved Docker environment stability and reproducibility for more reliable automated scoring
- Refined completion-checking logic to reduce ambiguous pass/fail edge cases
- Continues to evaluate the full agent harness rather than isolated model capability
- Backward-comparable with TerminalBench-2 results for longitudinal tracking of agent progress

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
Evaluates agents on realistic customer service scenarios requiring multi-turn conversations, policy adherence, and tool use. Tests agents' ability to follow complex business rules while serving customers effectively.

## Research and Retrieval Benchmarks

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
| Algorithm engineering / optimization | ALE-Bench |
| Terminal/CLI tasks | Terminal-Bench 2.1 |
| Safety evaluation | METR |
| Customer service agents | τ-bench |
| Financial domain agents | Finance Agent v2 |
| Wide/deep research orchestration | WANDR |

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
- [Observability](../Observability/Readme.md)
- [Harness Optimization](../AgentHarness/harness-optimization.md) — TerminalBench-2 as a harness-level evaluation environment
- [Search as Code](../RAG/search-as-code.md) — Perplexity's SaC architecture; introduces the WANDR benchmark
