## Short-term Memory


## Long-term Memory

- [Mem0](https://mem0.ai/):  a universal, self-improving memory layer that semantically extracts and stores user preferences and past interaction facts across sessions to provide highly personalized AI experiences.
- [Zep](https://www.getzep.com/): a context engineering platform that uses a temporal knowledge graph to help AI agents remember, summarize, and retrieve relevant facts and conversation history across long-term user sessions.

## Working (Filesystem Memory)

- [AgentFS](https://github.com/tursodatabase/agentfs): is a portable, SQLite-backed virtual filesystem that acts as a persistent "hard drive" for AI agents, allowing them to manage files, key-value state, and tool logs in a structured way that complements orchestration frameworks

| Solution | Memory Philosophy | Storage Tech | Primary Use Case | Key Strength |
|---|---|---|---|---|
| AgentFS | The Hard Drive | SQLite / Turso | Technical tasks & tool output | Portability: Moves the entire agent "state" in one .db file. |
| Mem0 | The Assistant | Vector DB / Graph | User personalization | Self-Improving: Automatically extracts facts like "User prefers Python." |
| Zep | The Historian | Temporal Graph | Long-running projects | Time-Aware: Tracks how facts change over time (e.g. updated budgets). |
| Letta (MemGPT) | The OS | Hierarchical | Autonomous long-term agents | Self-Management: Agent moves data between "RAM" and "Disk" on its own. |
| LangMem | The Brain | Integrated SaaS | LangGraph workflows | Native Sync: Perfectly captures "learnings" from LangChain threads. |

