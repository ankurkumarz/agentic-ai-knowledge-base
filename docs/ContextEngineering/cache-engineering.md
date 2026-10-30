---
type: Playbook
title: Cache Engineering for Agents
description: "Cache engineering lets agents directly control their active KV cache without modifying the text trajectory or re-prefilling retained context, overcoming the re-prefill dilemma of conventional context engineering."
tags: [context-engineering, kv-cache, agentic-ai, cost-optimization]
timestamp: 2026-10-30T00:00:00Z
---

# Cache Engineering for Agents

## Overview

Cache engineering is a new scheme for LLM agents to control their active key-value (KV) cache directly — without rewriting the text trajectory or triggering costly re-prefill. As agent trajectories grow longer, KV cache I/O and storage become the dominant cost driver. Conventional **context engineering** tackles this by trimming or summarizing history, but editing the trajectory prefix invalidates all downstream cached states, forcing an expensive re-prefill of retained context. Cache engineering sidesteps this dilemma entirely by operating on the cache layer rather than the token layer.

**Source**: [Cache Engineering for Agents — Fu et al., arXiv:2610.28577, Tsinghua University (October 2026)](https://arxiv.org/abs/2610.28577)

**Code**: [https://github.com/thu-nics/AKV](https://github.com/thu-nics/AKV)

## The Context Engineering Dilemma

Standard context engineering (summarization/trimming) faces a fundamental cost-accuracy tradeoff:

- **Editing earlier context** (e.g., summarizing turn 3 of 50) invalidates the KV cache for all tokens after the edit point. The longer the retained suffix, the more expensive the re-prefill.
- **Aggressive reduction** (keeping only recent rounds) avoids heavy re-prefill but discards intermediate tool results that may be essential for task accuracy.
- Empirically, summary-based context engineering at a 48K-token threshold reduces cost by ~7% but **lowers accuracy by 5 percentage points** on the BrowseComp-Plus benchmark (BCP).
- Trim-based context engineering (retaining only the latest 12 rounds) costs **1.85× more** than full-context inference due to re-prefill overhead.

KV cache reads account for **82.4% of total API cost** in long-horizon agent workloads.

## Cache Engineering Concepts

### What Changes

| | Context Engineering | Cache Engineering |
|---|---|---|
| **Operates on** | Text trajectory (token sequence) | Active KV cache |
| **Modifies history** | Yes — summarizes or trims tokens | No — trajectory is preserved |
| **Re-prefill needed** | Yes — editing prefix invalidates cache | No — retained states are reused |
| **Information loss** | Explicit (tokens removed) | Selective (only attention scope reduced) |
| **Retained cache** | Carries forward as-is | May implicitly contain info from dropped tokens |

### Core Cache Operations

Three primitive operations expose direct cache control:

**1. `append`** (standard)
Processes a new token and appends its KV state to the active cache. This is the normal LLM inference step, included here for completeness in the formalism.

**2. `drop`**
Removes selected KV entries from future attention. The dropped token's *text* stays in the trajectory; only its cached state is excluded from attention in subsequent steps. Crucially, the retained cache may still carry implicit information from the dropped entry if it attended to it before the drop — enabling information preservation even after eviction.

**3. `repos` (reposition)**
Adjusts the position encoding indices of retained KV keys using RoPE rotations, without re-prefill. This is necessary because standard position indices grow with the logical trajectory length. As entries are dropped, the remaining indices can approach the model's position limit even with a small active cache. `repos` decouples position encoding from logical index, allowing agents to continue indefinitely beyond what position limits would otherwise allow.

### History Dependence: The Serving Challenge

Cache states are **history-dependent**: the same retained token prefix can produce different KV states under different sequences of cache operations. For example, if token C attends to token A in one trajectory but A was already dropped before C was appended in another, C's KV state differs — even though both trajectories retain B and C with the same position encodings.

This means **prefix matching alone is insufficient** for correct cache reuse. Standard LLM serving systems (which assume token prefix → cache state) cannot handle cache engineering without modification.

## The AKV Serving Engine

AKV is co-designed with cache engineering to solve the history-dependence challenge through a **stateless interface / stateful serving** architecture.

### Serving Interface

AKV extends the standard LLM API minimally. The existing `messages` field carries the full logical token sequence; an optional `cache` field specifies `drop` and `repos` operations using an operate-after grammar:

```json
{
  "model": "gpt-oss-120b",
  "messages": [
    {"role": "user", "content": "Search ICLR"},
    {"role": "assistant", "content": "Searching"},
    {"role": "tool", "content": "ICLR is…"}
  ],
  "cache": {
    "drop": {"1": [0], "2": [1]},
    "reposition": [2]
  }
}
```

Each request fully describes its cache operation history, allowing the server to restore any evicted states without relying on physical cache persisting between turns.

### Internal Mechanisms

AKV addresses three serving challenges:

| Challenge | Mechanism | How it Works |
|---|---|---|
| Token prefixes no longer determine cache states | **Extended radix tree** | Adds `drop` nodes at operation trigger points; prefix matching walks both token and operation histories to distinguish states |
| Dropped cache may still be needed by concurrent requests | **Drop-aware eviction** | A KV entry becomes evictable only when all ongoing requests have dropped it; freed as a physical allocation but preserved as a tree placeholder |
| Restoring evicted states requires multiple forward passes | **Segment-batch attention** | Reconstructs missing states in a single prefill pass by batching segments that need recomputation |

### Stateless Interface Design

Each request includes its full cache operation history, making the server stateless from the client's perspective. If memory pressure causes eviction between turns, AKV can fully restore the required state. This is compatible with existing serving APIs.

## Cache Policy Design

### Tool-Response Rolling Drop

The primary example policy: **retain all reasoning and recent tool-response cache; drop older tool-response cache**. Motivation from empirical analysis:

- Tool responses receive less attention than assistant messages at comparable relative positions.
- Older tokens receive less attention than recent ones.
- Dropping older tool-response KV can **simultaneously reduce cost and improve accuracy** by eliminating low-value KV entries from attention.

The `repos` operation is applied after drops to prevent the position index from reaching the model's context limit — without it, BCP pass rate drops from 62% to 55% because agents halt when the position limit is exceeded.

### Ablation Findings

| Drop Target | `repos` | BCP Pass Rate | SWE Pass Rate |
|---|---|---|---|
| None (Standard) | — | Baseline | Baseline |
| Tool responses | No | +lower | +lower |
| Tool responses | **Yes** | **Best** | **Best** |
| Reasoning | Yes | Lower than tool-response only | Lower |
| Tool + Reasoning | Yes | Lower than tool-response only | Lower |

Dropping reasoning cache (alone or combined with tool responses) yields lower pass rates than dropping tool responses alone, confirming that reasoning chains should be retained.

### Recursive Self-Improvement (RSI) of Cache Policies

Cache engineering's programmable interface enables agents to **search, evaluate, and refine cache policies autonomously**:

1. Use the LLM to propose alternative cache policies (e.g., different drop targets, rolling window sizes).
2. Evaluate each policy on a held-out task set.
3. Refine toward lower cost and higher accuracy.

Results: RSI-designed policies reduce cost by **7.1% over expert-designed** tool-response rolling-drop (K=12) while maintaining full-context accuracy. Evaluated using MiniMax-M2.7 on 20 BCP tasks, then tested on 100 held-out tasks.

## Benchmark Results

Evaluated across three LLMs (MiniMax-M2.7, GPT-OSS-120B, a third model) and four agent benchmarks:
- **BCP** (BrowseComp-Plus) — deep research
- **xbench-DS** (xbench-DeepSearch-2510) — deep search
- **GAIA-Text** — 103-task general AI assistants validation subset
- **SWE-Verified** — software engineering

### Accuracy and Cost (vs. Threshold-Triggered Summarization)

| Method | Avg Score Δ | Avg Cost Δ |
|---|---|---|
| Cache Engineering (tool-response rolling drop) | **+1.7 points** | **−27.7%** |
| RSI-based cache policy | +comparable | −27.7% − 7.1% additional |

Cache engineering improves accuracy *and* reduces cost simultaneously — the first approach to break the accuracy-cost tradeoff of conventional context engineering.

### Serving Performance (AKV vs. Standard, GPT-OSS-120B on SWE-Verified)

| Metric | AKV vs Standard |
|---|---|
| Output throughput | Up to **1.2×** |
| P95 request latency | **1.5× speedup** |
| Concurrency scaling | AKV advantage widens at C≥14 as KV-cache pressure grows |

At high concurrency, standard serving must re-prefill evicted context, increasing latency and reducing throughput. AKV's retained-state reuse avoids this, yielding compounding advantages under load.

### Highest Pass Rates (BCP 100-task subset)

| Model | Best Method | Pass Rate |
|---|---|---|
| GPT-OSS-120B | RSI-based cache policy | 61.0% |
| MiniMax-M2.7 | RSI-based cache policy | 64.0% |

## Relationship to Existing Context Management Strategies

Cache engineering is **complementary to, not a replacement for** the standard context management strategies (see [strategies.md](./strategies.md)):

| Strategy | Relationship |
|---|---|
| **Reduce (Compaction/Summarization)** | Cache engineering replaces the re-prefill-heavy version for cost-sensitive workloads. When summaries are needed for external persistence (e.g., memory tool), context engineering is still appropriate. |
| **Cache (Prompt caching)** | Cache engineering extends prompt caching into the trajectory layer. The AKV extended radix tree handles history-dependent states that standard prefix caching cannot. |
| **Offload (Write)** | Orthogonal. Cache engineering manages in-flight KV state; offloading manages long-term persistence across sessions. |
| **Retrieve (RAG)** | Orthogonal. Cache engineering does not affect retrieval strategy. |
| **Isolate (Multi-agent)** | Each agent can apply its own cache policy. AKV's stateless interface supports multi-tenant isolation. |

### Positioning vs. Context Engineering

```
Context Engineering (text layer):
  trajectory → trim/summarize → shorter trajectory → re-prefill → inference

Cache Engineering (KV layer):
  trajectory → drop/repos on KV cache → smaller active cache → NO re-prefill → inference
```

The key insight: the text trajectory and the active KV cache are decoupled. Agents can reduce attention scope without altering the tokens they've generated.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Re-prefill dominates inference cost | Editing trajectory prefix forces expensive re-computation of all downstream KV states | Switch from summarization to cache engineering: use `drop` to exclude old tool-response KV from attention; no re-prefill required |
| Position index exhaustion | Long trajectories exhaust the model's position limit even with a small active cache | Apply `repos` after each `drop` cycle; this resets position encodings without re-prefill |
| Which entries to drop | Dropping reasoning cache degrades performance | Drop tool-response cache only (especially older rounds); retain all reasoning/assistant messages |
| Policy design overhead | Manual cache policy design is suboptimal | Use RSI: let the LLM propose, evaluate, and refine cache policies on held-out tasks; gains ~7% additional cost reduction |
| History-dependent serving | Naïve prefix caching returns wrong cache states under different `drop` orderings | Deploy AKV (or an equivalent extended radix tree implementation) rather than standard prefix caching |
| High-concurrency throughput | At C≥14 requests, re-prefill in standard serving compounds latency | AKV's cache reuse avoids re-prefill entirely; throughput advantage widens with concurrency |
| Combining with memory tools | Context window cleared; agent loses track of saved memory | Set `exclude_tools: ["memory"]` in any parallel clearing config; cache engineering does not interact with memory tool clearing |

## See Also

- [Common Strategies for Context Management](./strategies.md)
- [Key Challenges in Context Management](./challenges.md)
- [Anthropic Context Engineering](./anthropic.md)
- [Efficiency Frontier: Cost-Performance Optimization](./efficiency-frontier.md)
- [Production Best Practices: Context Engineering](../ProductionBestPractices/context-engineering.md)
- [Agent Memory — Short-Term](../AgentMemory/short-term.md)
- [Harness Optimization](../AgentHarness/harness-optimization.md)
- [Harness Engineering](../AgentHarness/harness-engineering.md)

## References

- [Cache Engineering for Agents — Fu et al., arXiv:2610.28577, Tsinghua University (October 2026)](https://arxiv.org/abs/2610.28577)
- [AKV Serving Engine — GitHub (thu-nics/AKV)](https://github.com/thu-nics/AKV)
