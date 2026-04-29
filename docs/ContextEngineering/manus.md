# Manus Context Engineering

## Overview

Manus is an autonomous AI agent built by a team led by Yichao 'Peak' Ji. The team made a foundational bet on context engineering over model fine-tuning — choosing to ship improvements in hours rather than weeks by shaping context rather than retraining models. They have rebuilt their agent framework four times, each time after discovering a better approach to context management.

> "If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed." — Yichao 'Peak' Ji

A typical Manus task requires around 50 tool calls, with an average input-to-output token ratio of ~100:1. This makes context engineering a first-order concern, not an optimization.

## Key Principles

### 1. Design Around the KV-Cache

Manus identifies KV-cache hit rate as the single most important metric for a production agent. With Claude Sonnet, cached input tokens cost $0.30/MTok vs. $3.00/MTok uncached — a 10x difference in cost and significant latency reduction.

Practices to maximize cache hit rate:
- **Keep the prompt prefix stable**: Even a single-token difference invalidates the cache from that point forward. A common mistake is including a timestamp (precise to the second) at the start of the system prompt.
- **Make context append-only**: Avoid modifying previous actions or observations. Ensure serialization is deterministic — many languages don't guarantee stable key ordering when serializing JSON, which silently breaks caching.
- **Mark cache breakpoints explicitly**: Some providers require manual insertion of cache breakpoints. At minimum, ensure the breakpoint covers the end of the system prompt.

### 2. Mask, Don't Remove (Tool Management)

As Manus's action space grew (especially with MCP integrations), the naive approach of dynamically adding/removing tools caused two problems:
1. Tool definitions live near the front of the context — any change invalidates the KV-cache for all subsequent content.
2. When prior actions reference tools no longer in the current context, the model gets confused and produces schema violations or hallucinated actions.

**Solution**: Manus uses a context-aware state machine to manage tool availability. Rather than removing tools, it masks token logits during decoding to prevent or enforce selection of certain actions based on current state. Tool definitions remain stable in the prefix; availability is controlled at the decoding layer.

Manus also designs action names with consistent prefixes (e.g., `browser_*` for browser tools, `shell_*` for command-line tools) to enable easy group-level constraints without stateful logit processors.

### 3. Use the File System as Context

Manus treats the file system as the "ultimate context": unlimited in size, persistent by nature, and directly operable by the agent.

Three pain points that motivate this:
1. Observations from web pages or PDFs can easily exceed context limits.
2. Model performance degrades beyond a certain context length even within the window.
3. Long inputs are expensive even with prefix caching.

**Key design principle**: All compression strategies are designed to be restorable. Web page content can be dropped from context as long as the URL is preserved. A document's contents can be omitted if its file path remains in the sandbox. This allows Manus to shrink context length without permanently losing information — avoiding the irreversible information loss risk of aggressive summarization.

### 4. Manipulate Attention Through Recitation

Manus agents create a `todo.md` file and update it step-by-step as a task progresses. This is not cosmetic — it's a deliberate mechanism to keep the agent's objectives in its recent attention span.

A typical Manus task spans ~50 tool calls. Without active attention management, agents drift off-topic or forget earlier goals in long contexts ("lost-in-the-middle" problem). By constantly rewriting the todo list, Manus recites its objectives into the end of the context, biasing the model's focus toward the current plan without architectural changes.

### 5. Keep the Wrong Stuff In

A common impulse when an agent makes an error is to clean up the trace — retry the action, reset state, hide the failure. Manus's experience is the opposite: **leave failed actions and their observations in context**.

When the model sees a failed action and its resulting error or stack trace, it implicitly updates its beliefs away from similar actions. Erasing failure removes evidence, preventing the model from adapting. Manus considers error recovery one of the clearest indicators of true agentic behavior.

### 6. Don't Get Few-Shotted

If the context is full of similar past action-observation pairs, the model will tend to follow that pattern even when it's no longer optimal. In batch tasks (e.g., reviewing 20 resumes), agents fall into a rhythm of repeating similar actions.

**Solution**: Manus introduces small amounts of structured variation in actions and observations — different serialization templates, alternate phrasing, minor noise in order or formatting. This controlled randomness breaks the pattern and prevents brittle, overgeneralized behavior.

## Summary of Strategies Used

| Strategy | Manus Implementation |
|---|---|
| Cache context | KV-cache optimization as primary metric; stable prefix, append-only context, deterministic serialization |
| Offload context | File system as primary external memory; restorable compression only |
| Reduce context | Drop content when reference (URL/path) is preserved; never irreversibly compress |
| Isolate context | Context-aware state machine for tool masking; not multi-agent parallelism |
| Attention management | todo.md recitation to prevent goal drift in long tasks |

## See Also

- [Common Strategies for Context Management](./strategies.md)
- [Key Challenges in Context Management](./challenges.md)
- [Anthropic Multi-Agent Research System](./anthropic.md)
- [LangGraph Context Engineering](./langgraph.md)
- [Agent Memory Management](../AgentMemory/README.md)

## References

- [Context Engineering for AI Agents: Lessons from Building Manus — Yichao 'Peak' Ji](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — primary source
- [Context Engineering for Agents — Lance Martin (references Manus)](https://rlancemartin.github.io/2025/06/23/context_engineering/)
