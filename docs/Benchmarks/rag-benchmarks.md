---
type: Benchmark
title: RAG Evaluation Benchmarks
description: "Seven benchmarks for evaluating the retrieval quality, hallucination, long-context capability, and reasoning accuracy of RAG-powered applications."
tags: [benchmarks, rag, retrieval, evaluation, agentic-ai]
timestamp: 2026-09-13T00:00:00Z
---

# RAG Evaluation Benchmarks

## Overview

Evaluating a RAG system requires more than generic LLM benchmarks. Retrieval quality, hallucination under context, long-context needle retrieval, and multi-hop reasoning each demand dedicated measurement. The seven benchmarks below cover the core failure modes of production RAG pipelines and are the recommended starting set for tracking Agentic RAG retrieval quality.

## Benchmarks

### 1. NeedleInAHaystack (NIAH)

**What it tests**: In-context retrieval from long documents — whether the model can locate a single planted fact ("needle") inside a large irrelevant corpus ("haystack").

**How it works**: A short, specific statement is embedded at a configurable depth inside a large text corpus (originally Paul Graham essays). The model is asked a question answerable only from that statement. Tests are repeated across different context lengths and needle depths to build a 2D performance heatmap.

**Why it matters for RAG**: Directly measures whether the model loses or ignores retrieved context as context length grows. A model that drops accuracy at depth 50% of a 64K context window will silently mis-answer RAG queries where the relevant chunk is not at the top of the context.

**Resources**:
- [Test repo — Needle In A Haystack (GitHub)](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

---

### 2. BeIR

**What it tests**: Information retrieval across 18 diverse datasets and 9 task types in a zero-shot, domain-agnostic evaluation setting.

**How it works**: Covers task types including fact-checking, duplicate detection, question answering, argument retrieval, and forum retrieval. Domains range from generic (news, Wikipedia) to specialized (biomedical publications). Evaluates dense retrievers, sparse retrievers, hybrid models, and re-rankers on the same splits.

**Why it matters for RAG**: The retriever is the first failure point in a RAG pipeline. BeIR's cross-domain zero-shot setup reveals whether a retriever generalizes — critical for enterprise RAG systems that operate across multiple document corpora.

**Resources**:
- [Paper: BeIR — A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/abs/2104.08663)
- [Dataset: BeIR on HuggingFace](https://huggingface.co/datasets/BeIR/beir)

---

### 3. FRAMES

**What it tests**: End-to-end RAG performance across three dimensions: factuality, retrieval accuracy, and multi-hop reasoning.

**How it works**: 800+ test samples requiring integration of information from 2–15 Wikipedia articles. Questions exercise numerical, tabular, and temporal reasoning, multiple constraints, and post-processing. No single-hop lookups — every question requires the model to synthesize across sources.

**Why it matters for RAG**: Most RAG evals test single-document retrieval. FRAMES specifically targets multi-hop scenarios where the model must retrieve and combine evidence — the hardest and most common failure mode in production agentic RAG.

**Resources**:
- [Paper: Fact, Fetch, and Reason — A Unified Evaluation of Retrieval-Augmented Generation](https://arxiv.org/abs/2409.12941)
- [Dataset: FRAMES on HuggingFace](https://huggingface.co/datasets/google/frames-benchmark)

---

### 4. RAGTruth

**What it tests**: Word-level hallucination in RAG outputs — how often and how severely models fabricate content when generating from retrieved context.

**How it works**: 18,000 naturally generated responses from diverse LLMs using RAG pipelines, annotated for four hallucination types:
- **Evident conflict** — clear factual errors, misspelled names, wrong numbers
- **Subtle conflict** — diverges from provided context without obvious error
- **Evident baseless introduction** — hypothetical or fabricated details not in context
- **Subtle baseless introduction** — subjective assumptions or unverified sentiment

**Why it matters for RAG**: Retrieval does not eliminate hallucination — models still fabricate when context is ambiguous or insufficient. RAGTruth provides a fine-grained taxonomy to diagnose which hallucination type a system suffers from, enabling targeted mitigations.

**Resources**:
- [Paper: RAGTruth — A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models](https://arxiv.org/abs/2401.00396)
- [Dataset: RAGTruth on HuggingFace](https://huggingface.co/datasets/wandb/RAGTruth)

---

### 5. RULER

**What it tests**: Long-context understanding across four task categories — retrieval, multi-hop tracing, aggregation, and question answering — at configurable context lengths (4K to 128K tokens).

**How it works**: Extends NIAH by varying the number and types of needles and adding task categories beyond simple retrieval. Synthetically generates evaluation examples based on input configuration (sequence length × task complexity), enabling consistent comparison across context window sizes.

**Why it matters for RAG**: Reveals the real effective context length of a model — many models claim 128K context windows but degrade significantly at lower effective lengths. Helps right-size context windows and chunk counts for RAG pipelines.

**Resources**:
- [Paper: RULER — What's the Real Context Size of Your Long-Context Language Models?](https://arxiv.org/abs/2404.06654)
- [Dataset: RULER on HuggingFace](https://huggingface.co/datasets/rulerscore/ruler)

---

### 6. MMNeedle

**What it tests**: Long-context retrieval capability for Multimodal Large Language Models (MLLMs) — locating a target sub-image ("needle") within a large image set ("haystack") based on a text description.

**How it works**: 40,000 images, 560,000 captions, and 280,000 needle-haystack pairs. Tests both single-needle and multiple-needle settings across varying context lengths. Uses image stitching to extend context length further.

**Why it matters for RAG**: As RAG expands to multimodal pipelines (document images, charts, diagrams), standard text-only NIAH tests are insufficient. MMNeedle is the primary benchmark for evaluating visual context retrieval, directly relevant to multimodal agentic RAG.

**Resources**:
- [Paper: Multimodal Needle in a Haystack — Benchmarking Long-Context Capability of Multimodal Large Language Models](https://arxiv.org/abs/2406.11230)
- [Dataset: MMNeedle on HuggingFace](https://huggingface.co/datasets/Fawad01/MMNeedle)

---

### 7. FEVER

**What it tests**: Fact extraction and verification — whether a system can retrieve evidence and correctly label claims as Supported, Refuted, or Not Enough Info.

**How it works**: 185,000+ human-generated claims based on Wikipedia articles. A model receives a claim (e.g., "The Eiffel Tower is in Berlin"), must retrieve relevant Wikipedia sentences, and assign the correct label. Tests information retrieval, evidence selection, and binary/ternary reasoning jointly.

**Why it matters for RAG**: Directly exercises the full RAG pipeline: retrieve → ground → reason → decide. The explicit "Not Enough Info" class tests whether the model knows when not to answer — a critical safety property for production RAG.

**Resources**:
- [Paper: FEVER — a large-scale dataset for Fact Extraction and VERification](https://arxiv.org/abs/1803.05355)
- [Dataset: FEVER on HuggingFace](https://huggingface.co/datasets/fever/fever)

---

## Benchmark Selection Guide

| RAG Failure Mode | Best Benchmark(s) |
|---|---|
| Context retrieval / needle finding (text) | NIAH, RULER |
| Context retrieval / needle finding (multimodal) | MMNeedle |
| Retriever generalization across domains | BeIR |
| Multi-hop reasoning across sources | FRAMES |
| Hallucination in generated answers | RAGTruth |
| Fact verification and evidence grounding | FEVER |
| Effective context window sizing | RULER |

## See Also

- [LLM Evaluation Benchmarks](llm-benchmarks.md)
- [Agent Evaluation Benchmarks](agent-benchmarks.md)
- [LLM App Evaluation Metrics](../EvaluationFrameworks/llm-eval-metrics.md)
- [LLM Evaluation Frameworks](../EvaluationFrameworks/llm-frameworks.md)
- [RAG Overview](../RAG/Readme.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Search as Code](../RAG/search-as-code.md)

## References

- [7 RAG Benchmarks (Evidently AI Blog)](https://www.evidentlyai.com/blog/rag-benchmarks) — survey of NIAH, BeIR, FRAMES, RAGTruth, RULER, MMNeedle, and FEVER with task descriptions and example questions
