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

## Software Development Benchmarks

### SWE-Bench
**Resource**: [SWE-Bench](https://www.swebench.com/)

A dataset that tests AI systems' ability to solve real GitHub issues automatically. Agents must understand codebases, reproduce bugs, and implement fixes that pass existing test suites. SWE-Bench Verified is a curated subset with human-verified solvability.

**Key Characteristics**:
- 2,294 real GitHub issues from popular Python repositories
- Requires understanding large codebases
- Evaluation via automated test suite execution
- Industry standard for coding agent evaluation
- Top systems (Devin, SWE-agent) achieve 40-50%+ on verified subset

## Multi-Agent and Collaboration Benchmarks

### AgentBench
A comprehensive benchmark evaluating LLMs as agents across 8 distinct environments including operating systems, databases, knowledge graphs, digital card games, lateral thinking puzzles, house-holding tasks, web shopping, and web browsing.

### τ-bench (Tau-bench)
Evaluates agents on realistic customer service scenarios requiring multi-turn conversations, policy adherence, and tool use. Tests agents' ability to follow complex business rules while serving customers effectively.

## Benchmark Selection Guide

| Use Case | Recommended Benchmark |
|----------|----------------------|
| General agent capability | GAIA |
| Web automation | VisualWebArena |
| Computer use | OSWorld |
| Software development | SWE-Bench |
| Terminal/CLI tasks | Terminal Bench |
| Safety evaluation | METR |
| Customer service agents | τ-bench |

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
