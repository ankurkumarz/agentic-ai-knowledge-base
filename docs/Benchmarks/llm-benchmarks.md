# LLM Evaluation Benchmarks

## Overview

LLM benchmarks measure the capabilities of large language models across dimensions including reasoning, knowledge, coding, mathematics, instruction following, and safety. This page covers both community-driven leaderboards and standardized academic benchmarks.

## Community-Driven Leaderboards

### LMSYS Chatbot Arena
**Resource**: [LMSYS Chatbot Arena](https://lmarena.ai?leaderboard)

The most widely cited community-driven evaluation platform for comparing LLMs. Uses an Elo rating system based on human preference votes from blind head-to-head comparisons. Over 1 million human votes collected across hundreds of models.

**Key Features**:
- Human preference-based ranking (not automated metrics)
- Blind evaluation — users don't know which model they're comparing
- Covers general conversation, coding, math, and creative tasks
- Updated continuously as new models are submitted
- Considered the gold standard for real-world user preference

### Vellum LLM Comparison Board
**Resource**: [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard)

Comprehensive leaderboard comparing LLM performance across multiple dimensions including quality, speed, and cost. Provides side-by-side comparisons to help teams select the right model for their use case.

### Berkeley Function/Tool Calling Leaderboard
**Resource**: [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)

Evaluates LLMs' ability to call functions (tools) accurately using real-world API data. Critical for agentic applications where models must select and invoke the correct tools with proper parameters.

**Key Features**:
- Real-world API data from 1,600+ APIs
- Tests simple, parallel, multiple, and nested function calls
- Evaluates both function selection accuracy and parameter correctness
- Regularly updated with new models and API categories
- Essential benchmark for evaluating models in agentic contexts

### Galileo Agent Leaderboard
**Resource**: [Galileo Agent Leaderboard](https://huggingface.co/spaces/galileo-ai/agent-leaderboard)

Specialized leaderboard for LLM performance in agentic scenarios. Evaluates models on multi-step reasoning, tool use, and task completion in agent-specific contexts. Version 2 provides enhanced evaluation metrics.

## Academic and Standardized Benchmarks

### Reasoning and Knowledge

**MMLU (Massive Multitask Language Understanding)**
Tests knowledge across 57 subjects including STEM, humanities, and social sciences. A standard benchmark for measuring broad knowledge and reasoning.

**HellaSwag**
Tests commonsense reasoning and natural language inference. Models must complete sentences in contextually appropriate ways.

**ARC (AI2 Reasoning Challenge)**
Tests grade-school science questions requiring reasoning beyond simple fact retrieval. Includes Easy and Challenge subsets.

**TruthfulQA**
Evaluates whether models generate truthful answers to questions that humans often answer incorrectly due to misconceptions. Measures tendency to hallucinate.

### Coding Benchmarks

**HumanEval**
OpenAI's benchmark of 164 Python programming problems. Models generate code that must pass unit tests. Standard for measuring code generation capability.

**MBPP (Mostly Basic Python Problems)**
500 crowd-sourced Python programming problems. Complements HumanEval with a broader range of difficulty levels.

**LiveCodeBench**
A contamination-free coding benchmark that continuously adds new problems from competitive programming platforms (LeetCode, Codeforces, AtCoder).

### Mathematics

**MATH**
12,500 competition mathematics problems across 7 difficulty levels. Tests advanced mathematical reasoning from algebra to calculus.

**GSM8K**
8,500 grade school math word problems requiring multi-step arithmetic reasoning. A standard benchmark for mathematical problem-solving.

**AIME**
American Invitational Mathematics Examination problems. Tests frontier mathematical reasoning capabilities.

### Long Context

**RULER**
Evaluates long-context understanding across tasks including retrieval, multi-hop reasoning, and aggregation at various context lengths (4K to 128K tokens).

**HELMET**
Holistic Evaluation of Long-context Language Models across diverse tasks requiring genuine long-context understanding.

## Inference Performance Benchmarks

### LLM-Inference-Bench
**Resource**: [Inference Benchmarking of LLMs on AI Accelerators](https://arxiv.org/html/2411.00136v1)

Comprehensive benchmarking suite evaluating inference performance of LLMs across AI accelerators. Measures Time to First Token (TTFT), tokens per second, and throughput across different hardware configurations.

### vLLM Benchmark
**Resource**: [vLLM Benchmark](https://hud.pytorch.org/benchmark/llms)

Benchmarks for hosting inference LLM models using vLLM, measuring throughput and latency for production serving scenarios.

## Benchmark Selection Guide

| Evaluation Goal | Recommended Benchmark |
|----------------|----------------------|
| General capability comparison | LMSYS Chatbot Arena |
| Tool/function calling | Berkeley Function Calling Leaderboard |
| Agentic performance | Galileo Agent Leaderboard |
| Coding ability | HumanEval, LiveCodeBench |
| Mathematical reasoning | MATH, GSM8K |
| Broad knowledge | MMLU |
| Truthfulness | TruthfulQA |
| Long context | RULER, HELMET |
| Inference performance | LLM-Inference-Bench |

## Limitations and Considerations

### Benchmark Saturation
Many popular benchmarks (MMLU, HumanEval) are approaching saturation as frontier models score near 90%+. New, harder benchmarks are needed to differentiate top models.

### Training Data Contamination
Models may have seen benchmark questions during training, inflating scores. Prefer benchmarks with held-out test sets or dynamic question generation.

### Task Coverage Gaps
No single benchmark covers all real-world use cases. Use multiple benchmarks and supplement with task-specific evaluations for your domain.

## See Also

- [Agent Benchmarks](agent-benchmarks.md)
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md)
- [LLM Evaluation Dashboards](Readme.md)
