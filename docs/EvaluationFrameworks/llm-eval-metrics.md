---
type: Reference
title: LLM App Evaluation Metrics
description: "A catalogue of metrics for evaluating LLM-powered applications, organized by evaluation scope: trace, chat, tool, session, and retriever."
tags: [evaluation, metrics, agentic-ai]
timestamp: 2026-09-13T00:00:00Z
---

# LLM App Evaluation Metrics

## Overview

This page catalogues metrics used to evaluate LLM-powered applications. Use it as a checklist when designing an evaluation pipeline. Metrics are grouped by evaluation scope (Tag) so you can quickly identify what to measure at each layer of your system — from individual tool calls up to multi-turn sessions.

The `Level` column indicates the measurement granularity:
- **LLM** — measured at the model/response level
- **Code** — measured by a code-based (deterministic) evaluator

## Trace-Level Metrics

Measure behavior across an entire request/response trace, typically applied to the full prompt-and-response pair.

| Metric | Level | Description |
|---|---|---|
| Output Toxicity (Vision) | LLM | Detects harmful or unsafe content in vision-enabled model outputs |
| Prompt Injection | LLM | Identifies attempts to override or hijack the model's instructions via the prompt |
| Prompt Injection (Audio) | LLM | Prompt injection detection for audio input modalities |
| Prompt Injection (Vision) | LLM | Prompt injection detection for vision input modalities |

## LLM & Chat Metrics

Measure response quality, coherence, safety, and SQL correctness for chat-style interactions.

| Metric | Level | Description |
|---|---|---|
| Reasoning Coherence | LLM | Assesses whether the model's reasoning steps are logically consistent |
| Reasoning Coherence (Audio) | LLM | Reasoning coherence evaluation for audio-input interactions |
| Reasoning Coherence (Vision) | LLM | Reasoning coherence evaluation for vision-input interactions |
| SQL Adherence | LLM | Checks whether generated SQL conforms to the provided schema or constraints |
| SQL Correctness | LLM | Validates that generated SQL produces correct results against expected output |
| SQL Efficiency | LLM | Evaluates whether generated SQL is optimized (avoids full scans, unnecessary joins, etc.) |
| SQL Injection | LLM | Detects SQL injection vulnerabilities in model-generated queries |
| Tool Selection Quality | LLM | Assesses whether the model selected the appropriate tool for a given task |
| Tool Selection Quality (Audio) | LLM | Tool selection quality for audio-input interactions |
| Tool Selection Quality (Vision) | LLM | Tool selection quality for vision-input interactions |
| Unsafe Output | LLM | Flags outputs that violate safety policies or contain harmful content |
| Visual Fidelity | LLM | Measures how accurately the model describes or reproduces visual content |
| Visual Quality | LLM | Assesses the overall quality and clarity of vision-related outputs |

## Tool Metrics

Measure correctness and reliability of tool/function-calling behavior.

| Metric | Level | Description |
|---|---|---|
| Tool Error Rate | LLM | Proportion of tool calls that result in errors or malformed invocations |

## Session Metrics

Measure consistency and coherence across a multi-turn session.

| Metric | Level | Description |
|---|---|---|
| User Intent Change | LLM | Detects whether the user's intent shifted significantly across turns in a session |
| User Intent Change (Audio) | LLM | Intent change detection for audio-input sessions |
| User Intent Change (Vision) | LLM | Intent change detection for vision-input sessions |

## Retriever Metrics

Measure retrieval quality in RAG and code-search pipelines.

| Metric | Level | Description |
|---|---|---|
| Precision@K | Code | Proportion of the top-K retrieved items that are relevant to the query |

## Choosing Metrics for Your Pipeline

| Application Type | Recommended Metrics |
|---|---|
| Text chatbot / assistant | Reasoning Coherence, Unsafe Output, Prompt Injection |
| Vision / multimodal app | All Vision variants, Visual Fidelity, Visual Quality |
| Voice / audio app | All Audio variants, Reasoning Coherence (Audio) |
| Text-to-SQL / NL2SQL | SQL Adherence, SQL Correctness, SQL Efficiency, SQL Injection |
| Tool-calling / function-calling | Tool Selection Quality, Tool Error Rate |
| Multi-turn conversation | User Intent Change, Reasoning Coherence |
| RAG / retrieval pipeline | Precision@K, plus retriever metrics from RAGAS / DeepEval |

## See Also

- [LLM Evaluation Frameworks](llm-frameworks.md)
- [AI as a Judge — Deep Dive](ai-as-judge.md)
- [Agent Evaluation Platforms](platforms.md)
- [Evaluation Tech Radar](tech-radar.md)
- [Benchmarks](../Benchmarks/Readme.md)
- [Observability Solutions](../Observability/solutions.md)
