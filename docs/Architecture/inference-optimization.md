---
type: Architecture
title: Inference Optimization
description: Inference optimization makes AI models faster and cheaper to run in production
tags: [architecture, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
# Inference Optimization

## Overview

Inference optimization makes AI models faster and cheaper to run in production. With foundation models — especially autoregressive LLMs — inference is inherently expensive: generating each output token requires loading the full model weights into GPU memory, and tokens are produced sequentially. This creates latency and cost pressure that grows with model scale. Optimization techniques address these bottlenecks at both the model level and the inference service level.

If you use a managed API (OpenAI, Anthropic, Google), the provider handles most of this. If you self-host a model, inference optimization becomes your responsibility.

## Understanding the Bottlenecks

### Compute-Bound vs. Memory-Bandwidth-Bound

| Bottleneck | Cause | When It Occurs |
|---|---|---|
| **Compute-bound** | Time-to-complete is limited by arithmetic operations | Prefill step (processing input tokens in parallel); image generation |
| **Memory-bandwidth-bound** | Time-to-complete is limited by data transfer rate between memory and compute | Decode step (generating output tokens sequentially); most LLM inference |

For autoregressive LLMs, **decode is memory-bandwidth-bound**: each token generation loads the entire model's weight matrices from GPU memory, but uses them for only a tiny amount of computation (one token). This means GPUs are underutilized during decoding.

### Prefill vs. Decode

```
Prefill: process all input tokens simultaneously → compute-bound
Decode: generate output tokens one by one → memory-bandwidth-bound
```

In production, these two steps are often decoupled and run on separate machines (prefill machines have different optimization profiles than decode machines). Time to First Token (TTFT) depends mainly on prefill; Time per Output Token (TPOT) depends on decode.

## Inference Performance Metrics

| Metric | Definition | Target |
|---|---|---|
| **TTFT** (Time to First Token) | Time from query to first generated token | As low as possible for chat; users accept longer wait for long-doc summarization |
| **TPOT** (Time per Output Token) | Time to generate each subsequent token | ~120 ms/token (8 tokens/s) is sufficient for most reading speeds |
| **Total latency** | TTFT + TPOT × output token count | Application-dependent |
| **Throughput (TPS)** | Output tokens per second across all users | Higher is lower cost |
| **Goodput** | Requests per second that meet the SLO (latency targets) | The metric that matters for real applications |
| **MFU** (Model FLOP Utilization) | Observed throughput / theoretical peak throughput | Measures how efficiently you're using GPU compute |
| **MBU** (Model Bandwidth Utilization) | Memory bandwidth used / peak bandwidth | Measures memory efficiency |

**Latency is a distribution, not a number.** Use p50, p95, p99 rather than averages. Outliers indicate problems (network errors, very long prompts).

**Batch vs. online APIs**: Many providers offer 50% cost reduction for batch APIs with hours-long SLOs. Suitable for synthetic data generation, periodic reporting, reindexing. Online APIs are for customer-facing use cases.

## Model-Level Optimization

### Quantization

Reduces the numerical precision of model weights (e.g., from 32-bit float to 8-bit or 4-bit integer):

| Method | Description | Trade-off |
|---|---|---|
| **Weight-only quantization** (W8, W4) | Quantize weights; keep activations in higher precision | Most widely used; minimal quality loss at 8-bit; some loss at 4-bit |
| **Activation quantization** (W8A8) | Quantize both weights and activations | Harder to implement; faster arithmetic on compatible hardware |
| **KV cache quantization** | Quantize the KV cache to int8 or fp8 | Reduces memory pressure; enables longer sequences |
| **QLoRA** | Quantize base model then add LoRA adapters | Makes finetuning of large models feasible on consumer GPUs |

Weight-only quantization is the most common approach: reducing FP32→FP16 halves memory footprint; FP16→INT8 halves again. Below 4 bits, quality degrades significantly.

### Pruning

Removes unnecessary parameters (connections or entire nodes) from a trained model:
- **Unstructured pruning**: Sets individual weights to zero → sparse model; not all hardware benefits from sparsity
- **Structured pruning**: Removes entire neurons/layers → smaller model; hardware-friendly
- In practice as of 2024, pruning is less commonly used than quantization due to complexity and smaller gains

### Knowledge Distillation

Trains a smaller "student" model to mimic the outputs of a larger "teacher" model. The student can achieve comparable quality to the teacher on specific tasks with far fewer parameters. Used by providers (e.g., GPT-4-distilled models) and application teams for latency-sensitive deployments.

### Speculative Decoding

Overcomes the sequential bottleneck of autoregressive decoding:

1. A fast, smaller **draft model** generates K candidate tokens in parallel
2. The target model **verifies** all K tokens simultaneously (parallelizable, thus fast)
3. The longest accepted prefix is kept; target model generates one additional token
4. Repeat

**Why it works**: Verification is faster than generation (parallel vs. sequential), and draft tokens for "easy" positions (common words, repeated patterns) are accepted at a high rate. For code generation, acceptance rates are especially high. DeepMind achieved >2× latency reduction for Chinchilla-70B using a 4B draft model.

Speculative decoding is now available in vLLM, TensorRT-LLM, and llama.cpp.

## Attention Mechanism Optimization

The transformer's attention mechanism has O(n²) complexity in sequence length — it's the dominant bottleneck for long contexts.

### KV Cache

When generating token t+1, the model doesn't need to recompute key and value vectors for tokens 1 through t — they can be cached and reused. This is the **KV cache**:

- KV cache size grows linearly with sequence length and batch size
- For a model with 96 layers, 96 attention heads, 128 head dimension, and sequence length 2048: KV cache ≈ 3TB at FP16 for a batch of 512
- Managing KV cache is one of the central inference engineering challenges

**KV cache optimizations**:

| Technique | Description |
|---|---|
| **PagedAttention** (vLLM) | Manages KV cache in non-contiguous memory pages (like OS virtual memory); eliminates fragmentation; enables dynamic allocation |
| **Grouped Query Attention (GQA)** | Multiple query heads share key/value heads; reduces KV cache size 4–8× with minimal quality loss |
| **Multi-Query Attention (MQA)** | Extreme version: all queries share one key/value head |
| **Cross-layer Attention** | Some layers share key/value from adjacent layers; Llama 3.1 uses this to reduce KV cache 20× |
| **Sliding window attention** | Only attends to the last W tokens; reduces both KV cache and computation |
| **KV cache quantization** | Stores KV cache at lower precision (int8/fp8) |

### FlashAttention

A hardware-optimized kernel that fuses multiple attention operations to reduce memory reads/writes. FlashAttention-2 and FlashAttention-3 bring 2–3× speedups over standard attention on modern NVIDIA GPUs (A100, H100). Used by default in most modern inference frameworks.

### Prompt Caching

If many requests share the same system prompt or document prefix, the KV cache for that prefix can be stored and reused. Providers (Anthropic, Google) offer explicit prompt caching APIs with ~90% cost reduction on cached tokens. Particularly valuable for RAG systems with large fixed context.

## Inference Service Optimization

### Continuous Batching

Naive batching waits until a batch is full before starting. **Continuous batching** processes new requests as soon as a slot is available — similar to how a rideshare service picks up new passengers when a seat frees up. This:
- Maximizes GPU utilization
- Reduces queueing delay
- Supports variable-length sequences without padding waste

Used by vLLM, TGI, and most modern inference frameworks.

### Prefill-Decode Disaggregation

Separate dedicated machines handle prefill (compute-bound) and decode (bandwidth-bound) phases:
- Prefill machines are optimized for parallel computation
- Decode machines are optimized for memory bandwidth
- Reduces interference between phases; improves TTFT and throughput independently

### Parallelism

For models that don't fit on a single GPU:

| Strategy | Description | Use Case |
|---|---|---|
| **Tensor parallelism** | Splits individual weight matrices across GPUs; requires fast interconnect | Single-node multi-GPU |
| **Pipeline parallelism** | Assigns different layers to different GPUs; introduces pipeline bubbles | Multi-node deployment |
| **Data parallelism** | Runs multiple copies of the model; routes different requests to different copies | High throughput, inference serving |
| **Expert parallelism** | For MoE models: each GPU hosts a subset of experts | Mixture-of-experts inference |

## Key Inference Frameworks

| Framework | Strengths |
|---|---|
| **vLLM** | PagedAttention, continuous batching, speculative decoding; widely adopted |
| **TensorRT-LLM** | NVIDIA-optimized; kernel fusion, INT8/FP8 quantization; best throughput on H100 |
| **llama.cpp** | CPU and Apple Silicon inference; good for local/edge deployment |
| **Hugging Face TGI** | Easy deployment; integrates with Hugging Face model hub |
| **DeepSpeed** | Training and inference optimization; tensor parallelism; Microsoft |

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| High TTFT | Prefill takes too long for large inputs | Use prompt caching; consider longer-context-optimized models |
| High TPOT | Decode is slow | Speculative decoding; smaller model; batch decode requests |
| Memory OOM | Model doesn't fit in GPU memory | Quantize to W8 or W4; use tensor parallelism; switch to smaller model |
| Low GPU utilization | MFU is poor despite workload | Enable continuous batching; increase batch size; inspect fragmentation |
| Cost too high | Per-token cost unsustainable | Batch non-latency-sensitive workloads; use caching; try smaller models |
| Long sequences degrade | KV cache overflow | GQA/MQA models; sliding window; KV cache quantization |

## See Also

- [Foundation Models](../Concepts/foundation-models.md)
- [AI Engineering](../Concepts/ai-engineering.md)
- [Finetuning](./finetuning.md)
- [Cost Management](../ProductionBestPractices/cost-management.md)
- [Observability](../Observability/Readme.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — Chip Huyen, O'Reilly, 2025. Chapter 9.
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — Kwon et al. (vLLM), 2023.
- [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691) — Dao, 2023.
- [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192) — Leviathan et al., 2022.
