# Context Engineering

Context engineering is the art and science of filling the context window with just the right information at each step of an agent's trajectory. As agents handle longer tasks and accumulate tool call feedback, managing what goes into the context window becomes the primary engineering challenge — not the model itself.

> "Context engineering is effectively the #1 job of engineers building AI agents." — Cognition

> "Agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies." — Anthropic

## Why It Matters

LLMs have a finite attention budget. The transformer architecture creates n² pairwise relationships for n tokens — as context grows, the model's ability to capture these relationships gets stretched thin. Context must be treated as a precious, finite resource with diminishing marginal returns.

The term "context engineering" emerged as the successor to "prompt engineering," driven by the shift from one-shot tasks to long-running agents. Andrej Karpathy's framing: the LLM is the CPU, the context window is RAM, and context engineering is the OS's job of curating what fits.

## Section Contents

### 1.1 Key Challenges in Context Management → [challenges.md](./challenges.md)

The five failure modes that degrade agent performance as context grows:

- **Context Rot** — general performance degradation as token count increases
- **Context Poisoning** — hallucinations or errors that enter context and compound
- **Context Distraction** — model over-focuses on accumulated history, neglects training
- **Context Confusion** — superfluous information (e.g., too many tools) degrades responses
- **Context Clash** — conflicting information or decisions across context sections

### 1.2 Common Strategies for Context Management → [strategies.md](./strategies.md)

Five strategies used across production agents:

| Strategy | Core Idea | Key Examples |
|---|---|---|
| Offload (Write) | Save to file system; retrieve on demand | Manus todo.md, Anthropic memory tool, Claude Code CLAUDE.md |
| Reduce (Compaction) | Summarize or prune accumulated context | Claude Code auto-compact, LangGraph DeepAgent, Cognition fine-tuned summarizer |
| Retrieve (RAG) | Pull relevant context just-in-time | Claude Code glob/grep, Tool RAG, Windsurf multi-method retrieval |
| Isolate (Multi-agent) | Split context across subagents | Anthropic researcher, open-deep-research |
| Cache | Stable prefix caching for cost/latency | Manus KV-cache, Gemini Context Caching |

### 1.3 Context Implementation References

#### [Manus](./manus.md)
Six production principles from building Manus: KV-cache as primary metric, mask-don't-remove for tools, file system as ultimate context, todo.md attention recitation, keeping errors in context, and preventing few-shot drift.

#### [Anthropic](./anthropic.md)
Two sources: the multi-agent research system (orchestrator-worker pattern, 90.2% improvement over single-agent, subagent output to filesystem) and the effective context engineering guide (attention budget framing, just-in-time retrieval, compaction, structured note-taking).

#### [LangGraph](./langgraph.md)
Lance Martin's four-strategy framework (write, select, compress, isolate), the open-deep-research reference implementation demonstrating all four strategies, and DeepAgent's summarization-as-middleware pattern.

#### [Devin / Cognition](./devin.md)
Two core principles: share full agent traces (not just messages), and actions carry implicit decisions. Argues against multi-agent parallelism for tasks with interdependencies. Recommends single-threaded agents with fine-tuned compression for long-horizon tasks.

## Additional Resources

- [Context Engineering by Human Layer](https://docs.google.com/presentation/d/16ykxEU78250wG3mPKNrF5IfxxD1fIVgdLQD9tlSZa6M/) — presentation on context engineering principles
- [How to Fix Your Context — Drew Breunig](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html) — six tactics for context management
- [how_to_fix_your_context — LangChain GitHub](https://github.com/langchain-ai/how_to_fix_your_context) — code examples

## See Also

- [Agent Memory Management](../AgentMemory/README.md) — persistent memory strategies
- [Multi-Agent Systems](../Architecture/multi-agent-system.md) — context coordination in multi-agent environments
- [RAG Architecture](../ReferenceArchitecture/rag-architecture.md) — retrieval-based context management
- [Production Best Practices: Context Engineering](../ProductionBestPractices/context-engineering.md) — production guidance
