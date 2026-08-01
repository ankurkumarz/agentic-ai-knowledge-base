---
type: Architecture
title: Finetuning
description: "Finetuning is the process of adapting a pre-trained foundation model to a specific task or style by continuing to train on targeted data"
tags: [architecture, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
# Finetuning

## Overview

Finetuning is the process of adapting a pre-trained foundation model to a specific task or style by continuing to train on targeted data. Unlike prompt engineering and RAG — which influence a model through its inputs without touching its weights — finetuning directly modifies the model. This makes it more powerful but also more resource-intensive and complex.

Finetuning is most often used to improve instruction-following behavior, enforce a specific output style or format, boost domain-specific capabilities, or reduce latency and cost by enabling smaller models to perform at the level of larger ones.

## When to Finetune

### Reasons to Finetune

- **Style and format compliance**: Prompt engineering cannot reliably enforce strict output structure (e.g., always return valid JSON with specific fields). Finetuning can bake this in.
- **Domain-specific knowledge**: A base model may lack medical, legal, or proprietary knowledge. Finetuning on domain corpora improves coverage.
- **Task specialization**: For narrow tasks, a finetuned small model can match or outperform a much larger general model, at lower latency and cost.
- **Safety and alignment**: Suppress undesirable behaviors, enforce brand voice, or tune refusal patterns.
- **Reducing prompt length**: If many examples are needed in-context (few-shot) to get good results, finetuning those examples into the model weights reduces per-request cost.

### Reasons NOT to Finetune

- **Insufficient data**: Finetuning typically requires hundreds to thousands of high-quality examples. With fewer examples, prompt engineering or RAG often performs better.
- **Task is solvable with prompts**: Many tasks, including complex reasoning, can be solved with well-crafted prompts. Finetuning adds cost and complexity without guaranteed gains.
- **Base model is changing**: If the underlying model is frequently updated, finetuning efforts become stale.
- **RAG can handle it**: If the need is to inject up-to-date or private knowledge, RAG is usually cheaper and more flexible than finetuning.

### Finetuning vs. RAG Decision Framework

| Scenario | Preferred Approach |
|---|---|
| Need up-to-date or frequently changing data | RAG |
| Need to enforce strict output format or style | Finetuning |
| Limited labeled data | RAG + prompt engineering |
| Need to reduce inference cost with a smaller model | Finetuning (distillation or direct) |
| Need to inject factual knowledge with citations | RAG |
| Task requires a behavior the base model wasn't trained for | Finetuning |
| Combination of above | RAG + finetuning (orthogonal, can be combined) |

## Memory Bottlenecks

Foundation model finetuning is memory-intensive. During training, the GPU must hold:
- **Model weights**: FP32 ≈ 4 bytes/param; FP16 ≈ 2 bytes/param
- **Gradients**: Same size as weights
- **Optimizer states**: Adam uses 8 bytes/param (momentum + variance)
- **Activations**: Proportional to batch size × sequence length

For a 7B-parameter model in FP32 with Adam: ~(4 + 4 + 8) × 7B = ~112GB — far exceeding most single GPUs. This is why most practical finetuning uses reduced-precision training and parameter-efficient methods.

### Numerical Representations

| Format | Bits | Range | Use Case |
|---|---|---|---|
| FP32 | 32 | ~±3.4×10³⁸ | Full-precision training |
| FP16 / BF16 | 16 | Smaller range; BF16 more stable | Mixed-precision training; inference |
| INT8 | 8 | -128 to 127 | Inference (weight quantization) |
| INT4 | 4 | -8 to 7 | Aggressive compression (QLoRA) |

**BF16** (brain floating point) is preferred over FP16 for training: it has the same dynamic range as FP32 but uses half the memory, avoiding the overflow issues common with FP16.

**Quantization** reduces precision of stored weights to lower memory footprint. See [Inference Optimization](./inference-optimization.md) for details.

## Parameter-Efficient Finetuning (PEFT)

PEFT methods update only a small fraction of model parameters, dramatically reducing memory and compute requirements. The core insight: models over-parameterize for any specific task, and most of the original knowledge can be preserved by adapting only a small subspace.

### LoRA (Low-Rank Adaptation)

The dominant PEFT approach. Instead of updating the full weight matrix W (size d×k), LoRA adds a low-rank decomposition:

```
W' = W + BA  (where B is d×r, A is r×k, r << min(d,k))
```

Only A and B are trained; W is frozen. Key parameters:
- **Rank r**: Smaller r = fewer trainable params = more memory-efficient, but lower expressiveness. Typical values: 4–64.
- **Alpha (α)**: Scaling factor for the LoRA update; often set to r or 2r.
- **Target modules**: Which weight matrices to apply LoRA to. Attention matrices (Q, K, V, O) are the most common; some practitioners also target MLP layers.

**Benefits**: 
- 10–10,000× fewer trainable parameters than full finetuning
- Only the small adapter needs to be saved and loaded; base model can be shared across tasks
- At inference, adapter weights are merged into base weights with no additional latency

### QLoRA

Combines quantization with LoRA:
1. Quantize the base model weights to 4-bit (NF4 format — a 4-bit float format designed for normally distributed weights)
2. Train LoRA adapters in 16-bit precision on top of the frozen quantized base

Practical impact: a 65B-parameter model that would require ~130GB for FP16 finetuning can be finetuned on a single 48GB GPU with QLoRA. Makes large model finetuning accessible on consumer hardware.

### Other PEFT Methods

| Method | Description | Key Characteristic |
|---|---|---|
| **Prompt tuning** | Learns soft "virtual tokens" prepended to input; only token embeddings are trained | Extremely few parameters; requires large base model to work well |
| **Prefix tuning** | Adds learned key/value pairs to each attention layer | More expressive than prompt tuning |
| **Adapter layers** | Inserts small trainable modules between transformer layers | Slightly more parameters than LoRA; original architecture preserved |
| **IA³** | Scales activation values; 100× fewer parameters than LoRA | Best for very low-data scenarios |

## Model Merging

A newer, experimental approach: combine multiple finetuned models by averaging or interpolating their weight matrices, without any additional training.

**SLERP** (Spherical Linear Interpolation): Interpolates between two model weight vectors on the hypersphere. Produces models that blend capabilities of both parent models more smoothly than simple averaging.

**TIES** (Trim, Elect Sign, Merge): Handles conflicting parameter updates from multiple models by: (1) trimming low-magnitude changes, (2) resolving sign conflicts via majority vote, (3) merging only elected parameters.

**DARE** (Drop and Rescale): Randomly drops a fraction of delta weights (finetuned minus base), then rescales the remainder. Reduces interference between different finetuning objectives.

Model merging is useful for combining task specializations or language capabilities without retraining, but results are less predictable than direct finetuning.

## Finetuning Tactics

**Data quality over quantity**: 1,000 high-quality, diverse examples typically outperform 10,000 noisy ones. Garbage in, garbage out applies more severely to finetuning than to base training.

**Start small**: Begin with a few hundred examples to verify the approach works before scaling. Evaluate on a held-out set after each training run.

**Baseline first**: Evaluate the base model before finetuning. Sometimes prompt engineering alone achieves the target quality.

**Watch for overfitting**: With small datasets, models can memorize training examples. Monitor validation loss and use early stopping.

**Choose the right base**: Finetuning a strong 7B model often outperforms finetuning a weak 13B model. Base model quality matters.

**LoRA rank selection**: Start with r=16 or r=32. Increase rank if the adapter doesn't converge; decrease if you need to reduce GPU memory.

## See Also

- [Foundation Models](../Concepts/foundation-models.md)
- [Dataset Engineering](./dataset-engineering.md)
- [Inference Optimization](./inference-optimization.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [AI Engineering](../Concepts/ai-engineering.md)
- [Context Engineering](../ProductionBestPractices/context-engineering.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — Chip Huyen, O'Reilly, 2025. Chapter 7.
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — Hu et al., 2021.
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — Dettmers et al., 2023.
- [TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708) — Yadav et al., 2023.
