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

## Short-term Memory Techniques

| Technique | Logic | Primary Benefit |
|---|---|---|
| Sliding Window | Retains only a fixed number of the most recent messages, discarding the oldest once the limit is reached. | Prevents "out of memory" errors and maintains low latency. |
| Token Trimming | Dynamically calculates and removes the minimum number of tokens from the start of the history to fit the model's limit. | Maximizes the use of the available context window without crashing. |
| Recursive Summarization | Periodically condenses older parts of the conversation into a short paragraph while keeping the recent messages in full. | Preserves long-term narrative context while saving significant token space. |
| Message Selection | Uses a "supervisor" model to retrieve only the past messages that are relevant to the current user query. | Highly efficient for complex, non-linear tasks where only specific historical facts matter. |
| Scratchpad / Working Memory | Provides a dedicated space (like a file or hidden block) for the agent to store intermediate thoughts and calculations. | Offloads technical complexity from the main chat history to keep the conversation clean. |
| Context Pinning | Locks vital information (like system instructions or core user preferences) so they are never discarded by trimming. | Ensures the agent never forgets its primary persona or mission. |

## Long-Term Memory (LTM) Strategies for AI Agents

| Strategy | Mechanism | Best For | Storage Type |
|---|---|---|---|
| Vector RAG | Text is embedded into numerical vectors; retrieved based on mathematical "closeness" to a query. | Fuzzy matching, semantic search, and general knowledge retrieval. | Vector DB (Pinecone, Chroma) |
| Knowledge Graphs | Maps data as nodes (entities) and edges (relationships), e.g., "User" -> "owns" -> "Macbook." | Relational reasoning, factual rigor, and multi-hop questions (e.g., "Who approved X's budget?"). | Graph DB (Neo4j, FalkorDB) |
| Entity Extraction | LLM extracts specific facts (names, dates, preferences) into structured tables. | Personalization and fixed attributes (e.g., "The user is allergic to peanuts"). | SQL / NoSQL (Postgres, Redis) |
| Incremental Summary | Periodically condenses old interaction logs into a running "narrative" or profile. | Long-term context without keeping every message word-for-word. | Text / Markdown files |
| Reflection / Consolidation | A background loop where the agent reviews its own logs to extract "learnings" or success patterns. | Continuous improvement and self-correction (e.g., "Method A failed twice; use Method B next time"). | AgentFS / Specialized DB |
| Episodic Memory | Stores specific past events as discrete "episodes" with timestamps. | Temporal reasoning and recalling "What exactly happened last Tuesday?" | Structured Logs / Metadata |
