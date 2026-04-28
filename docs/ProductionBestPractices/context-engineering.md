# Context Engineering

Context engineering is the discipline of deciding what information goes into an agent's context window, when, and in what form. Poor context management is one of the most common causes of agent quality degradation in production.

## Overview

The context window is the agent's working memory — expensive, limited, and critical. The five core strategies for managing it:

| Strategy | Use When | Example |
|---|---|---|
| Offload | Long-term notes, tool logs, TODO lists | Write intermediate results to AgentFS; reference by pointer |
| Reduce (Compaction) | Conversation history grows too long | Summarize old turns; prune irrelevant tool call results |
| Retrieve | Need external knowledge on demand | RAG over knowledge base; fetch only relevant chunks |
| Isolate | Multi-agent systems with specialized roles | Each sub-agent gets only its relevant context slice |
| Cache | Stable, repeated prefixes (system prompts, tool definitions) | Use Anthropic/Gemini prompt caching for static prefixes |

## Best Practices

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Context rot | Context quality degrades over long sessions as irrelevant information accumulates | Kept full conversation history; later turns were confused by early irrelevant content | Implement periodic compaction — summarize and prune history at defined intervals or token thresholds |
| Context poisoning | Malicious or misleading content in retrieved documents corrupts agent reasoning | Trusted all retrieved content equally; agents acted on injected instructions | Validate and sanitize retrieved content; use separate trust levels for user input vs. retrieved data |
| Context distraction | Too much context causes the agent to focus on the wrong information | Added more context hoping for better answers; quality dropped | Apply context minimalism — include only information directly relevant to the current task |
| Context window exhaustion | Complex multi-step tasks exceed token limits mid-execution | Increased model context window; costs scaled with no quality improvement | Offload intermediate state to filesystem/scratchpad; keep only active task context in window |
| Multi-agent context conflicts | Sub-agents with overlapping context make contradictory decisions | Shared full context across all agents; conflicting decisions emerged | Isolate context per agent role; use a coordinator agent to resolve conflicts at handoff boundaries |
| Retrieval noise | RAG retrieval pulls in semantically similar but contextually irrelevant chunks | Used top-K similarity only; retrieved off-topic content regularly | Combine semantic search with metadata filters (recency, document type, entity); re-rank with a cross-encoder |
| System prompt bloat | System prompts grow over time with accumulated instructions | Added instructions incrementally; prompt became contradictory and expensive | Audit system prompts regularly; remove redundant instructions; use prompt caching for stable prefixes |
| Context across sessions | Agents lose context between sessions requiring users to repeat themselves | Stored raw conversation history; retrieval was slow and noisy | Extract key facts and preferences to structured memory at session end; inject as compact summary at session start |

## Implementation References

| Source | Key Insight |
|---|---|
| [Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) | Heavy use of filesystem offloading + prompt caching for performance |
| [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context isolation in multi-agent research systems; preventing cross-agent contamination |
| [LangGraph](https://rlancemartin.github.io/2025/06/23/context_engineering/) | Summarization as middleware in agent pipelines; built into DeepAgent |
| [Devin / Cognition](https://cognition.ai/blog/dont-build-multi-agents) | Caution on multi-agent context distribution — sub-agents should avoid decisions to reduce conflict risk |
| [ACE Framework](https://github.com/ace-agent/ace) | 3-role framework: Generator (creates context), Reflector (evaluates quality), Curator (organizes for retrieval) |

## Context Caching

Prompt caching reduces costs significantly for agents with large, stable system prompts or document contexts:

| Provider | Cache Discount | Notes |
|---|---|---|
| Anthropic Claude | ~90% on cached tokens | Cache static prefixes: system prompt, tool definitions, documents |
| Google Gemini | Significant reduction | [Context Caching on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) |

## See Also
- [State & Memory Management](./state-memory.md)
- [Cost Management](./cost-management.md)
- [Agent Security](./security.md)
