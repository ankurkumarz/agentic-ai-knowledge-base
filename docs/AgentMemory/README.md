## Short-term Memory

| Category | Solution / Technique | Memory Philosophy | Best For |
|---|---|---|---|
| Frameworks | LangGraph Checkpoints | Stateful Threads | Saving the exact "snapshot" of a multi-step workflow. |
| Frameworks | LangChain Window | Sliding Buffer | Keeping only the last N interactions to save tokens. |
| Frameworks | Letta (MemGPT) | Virtual Context | Dynamically swapping info in/out of the context window. |
| In-Memory | Redis / Upstash | Ephemeral Cache | Low-latency session storage for high-speed chat apps. |
| Managed | OpenAI Threads | Stateful API | Hands-off management of current conversation history. |
| Technique | Summarization | Recursive Compression | Condensing old messages into a brief "recap" to save space. |
| Technique | Scratchpad | Working Draft | Agent-written notes used only for the current task logic. |

## Long-term Memory

- [Mem0](https://mem0.ai/):  a universal, self-improving memory layer that semantically extracts and stores user preferences and past interaction facts across sessions to provide highly personalized AI experiences.
- [Zep](https://www.getzep.com/): a context engineering platform that uses a temporal knowledge graph to help AI agents remember, summarize, and retrieve relevant facts and conversation history across long-term user sessions.

## Working (Filesystem Memory)

- [AgentFS](https://github.com/tursodatabase/agentfs): is a portable, SQLite-backed virtual filesystem that acts as a persistent "hard drive" for AI agents, allowing them to manage files, key-value state, and tool logs in a structured way that complements orchestration frameworks

## Comparative View

| Solution | Provider | Memory Philosophy | Core Technology | Key Strength |
|---|---|---|---|---|
| AgentFS | Turso | The Hard Drive | Portable SQLite | Filesystem-like persistence in a single, movable .db file. |
| Mem0 | Independent | The Assistant | Vector / Graph | Automatically extracts and refines user facts/preferences. |
| Zep | Independent | The Historian | Temporal Graph | Tracks how facts and knowledge evolve over a timeline. |
| Letta | Independent | The OS | Virtual Memory | Self-managed "RAM" and "Disk" for autonomous context. |
| LangMem | LangChain | The Brain | Managed SaaS | Deeply integrated long-term learning for LangGraph nodes. |
| Bedrock Memory | AWS | Enterprise Store | Managed AWS | Seamless scaling and compliance for Bedrock agents. |
| Vertex Memory | Google | Managed Bank | Google Cloud | Native "evolving" memory for the Gemini ecosystem. |
| Foundry Memory | Azure | Managed State | Microsoft Cloud | Enterprise-grade state management within Azure OpenAI. |

