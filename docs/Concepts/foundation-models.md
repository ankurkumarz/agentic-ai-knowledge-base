---
type: Concept
title: Foundation Models
description: "Foundation models are large-scale AI models trained on broad data that can be adapted to a wide range of downstream tasks"
tags: [concepts, agentic-ai]
timestamp: 2026-07-17T00:00:00Z
---
# Foundation Models

## Overview

Foundation models are large-scale AI models trained on broad data that can be adapted to a wide range of downstream tasks. They represent a shift from task-specific models (one model per task) to general-purpose models that can perform many tasks without being retrained from scratch. The term *foundation* signals both their importance as building blocks for AI applications and their ability to be fine-tuned for specific needs.

GPT-4, Claude, Gemini, and Llama are all foundation models. They are also called large language models (LLMs) when text-only, or large multimodal models (LMMs) when they process multiple modalities (text, images, audio, video).

## From Language Models to Foundation Models

**Language models** encode statistical information about language — how likely a word (or token) is to appear in a given context. The basic unit is a *token*, which can be a character, word, or sub-word. GPT-4 uses ~¾ words per token on average.

Two types of language models:

| Type | How It Works | Primary Use Case |
|---|---|---|
| **Masked LM** (e.g., BERT) | Predicts missing tokens anywhere in a sequence (fill-in-the-blank) | Classification, sentiment analysis, code debugging |
| **Autoregressive LM** (e.g., GPT) | Predicts the next token based on preceding tokens | Text generation, chat, coding, reasoning |

Autoregressive models dominate modern AI applications because they generate open-ended outputs.

**Self-supervision** is the key enabler of scale. Instead of requiring manually labeled data, language models learn from the text itself: each sentence provides both the input context and the prediction target. This enables training on internet-scale data (books, Wikipedia, code, web pages) without labeling cost, allowing models to grow to billions of parameters.

**Foundation models** extend language models to multiple data modalities. CLIP (OpenAI, 2021) used 400M image-text pairs from the internet without manual labels. GPT-4V and Claude 3 process both text and images. Some models also handle video, audio, 3D assets, and protein structures.

## Model Architecture

Modern foundation models predominantly use the **transformer** architecture, which excels at processing sequences of tokens in parallel using attention mechanisms. Key design dimensions:

- **Model size (parameters)**: GPT-1 (2018) had 117M parameters; current large models exceed 100B. More parameters generally means more capacity to learn, requiring more training data.
- **Context length**: How many tokens the model can process at once. Longer contexts allow more complex tasks but increase compute cost quadratically (or linearly with optimized attention).
- **Vocabulary size**: GPT-4 has 100,256 tokens; Mixtral 8x7B has 32,000 tokens.

### Training Phases

| Phase | Description | Who Does It |
|---|---|---|
| **Pre-training** | Train from random weights on massive datasets. Autoregressive: predict next token. Most compute-intensive step (~98% of resources for InstructGPT). | Model developers only |
| **Post-training / Supervised Finetuning (SFT)** | Continue training on curated instruction-following examples. Teaches the model to respond appropriately to user requests. | Model developers; sometimes application teams |
| **Preference Finetuning (RLHF/DPO)** | Align the model to human preferences using comparison data (preferred vs. rejected responses). | Model developers |

Pre-training and post-training differ in goal, not process — both update model weights. Application developers who adapt models are typically doing *finetuning*, not post-training.

## Sampling and Generation

Foundation models are probabilistic: given a prompt, they generate a probability distribution over the next token, sample from it, append the token, and repeat. This probabilistic nature explains both the creativity and the inconsistency of AI outputs.

Key sampling parameters:

| Parameter | What It Controls | Effect |
|---|---|---|
| **Temperature** | Sharpness of probability distribution | Low (≤0.3): focused, deterministic; High (>1): creative, diverse |
| **Top-p (nucleus sampling)** | Cumulative probability threshold for candidate tokens | Limits sampling to the most likely tokens summing to p |
| **Top-k** | Number of top tokens to sample from | Hard limit on candidate set |

**Test-time compute (TTC)**: Allocating more compute at inference time (e.g., chain-of-thought, majority voting, best-of-N sampling) can significantly improve output quality without retraining. OpenAI's o1/o3 series explicitly trades tokens for reasoning quality.

**Structured outputs**: Models can be constrained to produce valid JSON, XML, or code by modifying the sampling process to only generate tokens consistent with the expected format (constrained decoding). This is critical for production systems that parse model outputs programmatically.

## Probabilistic Nature and Hallucinations

Because outputs are sampled from a probability distribution, models can generate plausible-sounding but factually incorrect information — called *hallucinations*. Key implications:

- Two identical prompts with non-zero temperature will produce different outputs
- Models may confidently state incorrect facts they've never seen in training
- Mitigation: RAG (ground responses in retrieved facts), lower temperature, verification steps, output guardrails

## Key Distinctions

**Foundation model vs. task-specific model**: A foundation model is general-purpose; a task-specific model is optimized for one task. Foundation models can be adapted to specific tasks via prompting, RAG, or finetuning, often with far less data than training from scratch.

**Generative vs. embedding models**: Generative models produce open-ended outputs (text, images). Embedding models produce fixed-size vector representations of inputs. CLIP is an embedding model; GPT-4 is generative. Embedding models are critical for RAG retrieval.

**Open vs. closed models**: Closed-weight models (GPT-4, Claude) are accessible only via API. Open-weight models (Llama, Mistral, Falcon) allow local deployment, finetuning, and inspection — at the cost of operational complexity.

## Choosing Between Models

Model selection involves trade-offs across multiple dimensions:

| Dimension | Considerations |
|---|---|
| **Quality** | Benchmark performance, domain-specific capabilities, instruction following |
| **Latency** | TTFT (time to first token), TPOT (time per output token), total latency |
| **Cost** | Input and output token pricing; self-hosting vs. API costs |
| **Context length** | Maximum supported input; relevance to your use case |
| **Modalities** | Text-only vs. multimodal; required for vision/audio tasks |
| **Deployment** | API (managed) vs. self-hosted (open-weight) |
| **Data privacy** | Whether data can leave your organization |

**Build vs. buy**: Using an existing foundation model is almost always faster and cheaper than pre-training from scratch. Pre-training requires rare expertise, massive compute, and months of work. The build-vs-buy question more often arises at the finetuning level.

## See Also

- [AI Engineering](ai-engineering.md)
- [Prompt Engineering](../PromptEngineering/README.md)
- [RAG Reference Architecture](../ReferenceArchitecture/rag-architecture.md)
- [Finetuning](../Architecture/finetuning.md)
- [Inference Optimization](../Architecture/inference-optimization.md)
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md)
- [Context Engineering: Key Challenges](../ContextEngineering/challenges.md)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — Chip Huyen, O'Reilly, 2025. Chapters 1–2.
- [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) — OpenAI, 2023.
- [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) — Radford et al., OpenAI, 2021.
