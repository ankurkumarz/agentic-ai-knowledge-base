# State & Memory Management

Effective memory management determines whether an agent feels like a persistent, intelligent system or a stateless chatbot. The core challenge is deciding what to keep in the expensive context window versus what to offload to external storage.

## Overview

![Memory Architecture](../assets/images/agent-memory-architecture.png)

Agent memory operates across three functional tiers:

| Tier | Purpose | Storage | Analogy |
|---|---|---|---|
| Short-term (Working Memory) | Current task context and conversation flow | In-memory / checkpointer | RAM |
| Episodic Memory | Searchable log of past events and outcomes | Vector DB / structured logs | Journal |
| Long-term (Semantic Memory) | Persistent facts, preferences, and learned rules | Knowledge graph / SQL | Hard drive |

## Best Practices

| Key Challenge | Description | Lessons Learned & Alternatives Considered | Solution Applied |
|---|---|---|---|
| Context window overflow | Long sessions exceed model token limits, causing truncation or errors | Tried increasing context window size; costs scaled quadratically | Implement sliding window or recursive summarization to compress old history |
| State loss between sessions | Agents forget user preferences and prior decisions across sessions | Stored full conversation history; retrieval became slow and noisy | Extract and persist key facts (entity extraction) to a structured store; retrieve on demand |
| Conflicting memory updates | Multiple agents writing to shared memory create inconsistencies | Used a single shared vector DB; concurrent writes caused stale reads | Implement optimistic locking or event-sourced memory with a temporal knowledge graph (Zep/Graphiti) |
| Memory retrieval relevance | Fetching too much irrelevant context degrades response quality | Retrieved top-K by embedding similarity alone; pulled in unrelated facts | Combine semantic search with metadata filters (recency, entity type, session ID) |
| Memory privacy and isolation | User A's memory leaking into User B's context | Shared embedding space across users; namespace collisions occurred | Enforce strict tenant/user namespacing in all memory stores; audit access patterns |
| Implicit vs explicit memory | Agents miss important facts not explicitly stated by users | Relied on users to say "remember this"; most didn't | Run a background extraction LLM to monitor conversations and auto-save key facts |
| Memory staleness | Stored facts become outdated as user context changes | Kept all facts indefinitely; agents acted on stale preferences | Attach TTLs to volatile facts; use temporal graphs to track how facts evolve over time. For managed platforms, use scheduled dreaming (Anthropic) to auto-purge contradicted facts between sessions |
| Working memory for tool-heavy tasks | Complex multi-step tool chains lose intermediate state | Passed all state through the context window; hit token limits | Use a scratchpad / AgentFS for intermediate tool outputs; reference by pointer in context |
| Self-improvement without retraining | Agent makes same mistakes across sessions without model fine-tuning | Manual rule updates in system prompt; engineers couldn't keep up | Use scheduled memory consolidation (dreaming) to extract recurring patterns from episodic logs and promote them to procedural memory automatically |
| Self-evaluation of agent output quality | Hard to know if agent succeeded without human review | Spot-checking a sample; missed regressions | Add an isolated grader agent (Outcomes pattern) that scores output against a plain-language rubric in a separate context window; loop until grader approves or max iterations reached |
| Scheduled/automated loops losing continuity between runs | A recurring automation (cron, `/loop`, `/goal`) has no memory of what a prior run already tried or resolved | Re-ran the same triage prompt from scratch each morning; duplicated work and re-surfaced resolved findings | Externalize loop state to a markdown file or tracker board (e.g., Linear via MCP) that records what's done and what's next — the agent forgets between runs, the repo/tracker doesn't; see [Loop Engineering](../AgentHarness/loop-engineering.md) |

## Memory Solutions Reference

| Solution | Provider | Core Technology | Key Strength |
|---|---|---|---|
| [Mem0](https://mem0.ai/) | Independent | Vector + Graph | Auto-extracts and refines user facts across sessions |
| [Zep](https://www.getzep.com/) | Independent | Temporal Knowledge Graph | Tracks how facts evolve over time |
| [AgentFS](https://github.com/tursodatabase/agentfs) | Turso | SQLite-backed virtual FS | Filesystem-like persistence in a single portable .db file |
| [Letta (MemGPT)](https://letta.com/) | Independent | Virtual Context | Self-managed RAM/disk for autonomous context swapping |
| [LangMem](https://blog.langchain.dev/langmem/) | LangChain | Managed SaaS | Deep integration with LangGraph nodes |
| Claude Managed Agents Memory + Dreaming | Anthropic | Filesystem + scheduled consolidation | First-party self-improving memory with dreaming (between-session consolidation) and outcomes (self-grading); Harvey reported 6× task completion gains |
| Bedrock Memory | AWS | Managed AWS | Enterprise scaling and compliance for Bedrock agents |

## LTM Strategy Selection

| Strategy | Best For | Storage |
|---|---|---|
| Vector RAG | Fuzzy/semantic search over large knowledge bases | Pinecone, Chroma, pgvector |
| Knowledge Graph | Relational reasoning, multi-hop questions | Neo4j, FalkorDB |
| Entity Extraction | Personalization, fixed attributes (allergies, preferences) | Postgres, Redis |
| Incremental Summary | Long-term narrative without storing every message | Markdown / text files |
| Reflection / Consolidation | Self-correction, learning from past failures | AgentFS / specialized DB |

## Stateless Agent Design for Horizontal Scaling

Since LLMs are themselves stateless, persisting memory externally is **non-negotiable** for production agents. The payoff: any agent instance can handle any request, enabling serverless horizontal scaling.

**Google Cloud pattern**: Design agent logic as a stateless, containerized service with external state — deployable on Cloud Run (auto-scaling) or Vertex AI Agent Engine.

**Key architectural choice**:
- **Vertex AI Agent Engine**: Provides a built-in, durable session and memory service. Managed, but less flexible.
- **Cloud Run + external DB**: More flexibility — integrate directly with AlloyDB or Cloud SQL. Requires managing the persistence layer yourself.

**Handling long-running tasks**: For complex jobs, use asynchronous/event-driven patterns. A service publishes a task to Pub/Sub, which triggers a Cloud Run worker for asynchronous processing. The agent stays responsive while the job runs in the background.

**Reliability for stateful tools**: When a tool call fails (network issue, transient error), agents must retry safely. This requires:
- **Idempotent tools**: Tools designed so calling them twice with the same inputs doesn't cause duplicate side effects (e.g., duplicate charges, duplicate messages). Critical for tools involving financial transactions or external writes.
- **Exponential backoff**: Automatically retry with increasing delays, giving the downstream service time to recover.

## Multi-Agent Shared State (AWS Pattern)

In multi-agent systems, agents coordinate through shared state rather than direct coupling. AWS recommends a three-tier shared state architecture:

| Tier | Store | Characteristics | Use For |
|---|---|---|---|
| Task state | Amazon DynamoDB | Single-digit ms reads, survives agent failures, full audit trail | Durable workflow execution state — every step recorded |
| Session context | Amazon ElastiCache | Sub-ms access, TTL-managed | Conversation turns + recently accessed payloads |
| Domain knowledge | Amazon Bedrock Knowledge Bases | Vector retrieval, governance-controlled, shared across all agents | No duplication of knowledge across agent instances |
| Intermediate results | Amazon S3 | Cost-effective, durable | Referenced by pointer in DynamoDB task state — never forwarded in payloads |

**Handoff payload principle**: include only what the next agent needs. Verbose payloads bloat context windows and degrade reasoning quality. Store large intermediate artifacts in S3 and pass a reference, not the content.

## Event Sourcing for Multi-Agent State Consistency (Confluent Pattern)

An alternative to a shared mutable state store: maintain state consistency across many agents through **immutable logs and event sourcing**, as described in Confluent's *A Guide to Event-Driven Design for Agents and Multi-Agent Systems* (2025). The model treats every agent interaction as input → processing → output over a durable event log rather than a database record:

- **Every event is recorded as an immutable, append-only entry** — no data loss, and a complete audit trail of how state evolved.
- **Replay-based recovery**: if an agent fails, it restores its state by replaying events from its last saved offset, rather than reconstructing state from a snapshot.
- **Parallel consumption without interference**: multiple agents can consume the same event stream independently, each tracking its own offset, enabling horizontal scaling without lock contention.

This complements the AWS three-tier shared-state model above: task state and intermediate results can be derived from (or backed by) an event log instead of, or in addition to, a row-oriented store like DynamoDB, particularly when the dominant access pattern is "what happened, in order" rather than "what is the current value."

## See Also

- [Context Engineering](./context-engineering.md)
- [Observability](./observability.md)
- [Deployment](./deployment.md)
- [Claude Managed Agents — Memory, Dreaming & Outcomes](../AgentPlatforms/claude-managed-agents.md)
- [Long-Term Memory Strategies](../AgentMemory/ltm-strategies.md)
- [Event-Driven Design Patterns for Multi-Agent Systems (Confluent)](../DesignPatterns/event-driven-patterns.md)
- [Workflow Orchestration — Temporal](../WorkflowBuilders/orchestration.md)
- [Loop Engineering](../AgentHarness/loop-engineering.md) — externalized state as the "spine" of a scheduled, self-feeding agent loop
