# Context Engineering

- [Agentic Context Engineering (ACE)](https://github.com/ace-agent/ace): 3 Role Agentic Framework: Generator, Reflector, and Curator. [Research Paper](https://arxiv.org/abs/2510.04618)

## Key Challenges in Context Management

- [Context Rot](https://research.trychroma.com/context-rot)
- Context Poisoning
- Context Distraction
- Context Confusion
- Context Clash

### References

- [Fix Your Context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html)


## Common Strategies for Context Management

- **Offload context (file system)**
  - Usage: Long-term memory, Notes, TODO List, Tool-heavy context (to keep reference to the detailed tool calling on file)
  - [Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) and Anthropic heavily use offloading context to the file system, and so [others](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html).
 
- **Reduce Context (compaction)**
  - Usage: Summarization, Tool calls pruning, Summarize / prune at agent-agent handoffs, Prune irrelevant parts of message history, Be careful of information loss
  - Claude code applying it + allows user to compact, LangGraph built Deepagent with summarization as middleware
 
- **Retrieve context**
  - Usage: Retrieve contextual data (using RAG etc.), Populate Prompt with Retrieved Data

- **Isolate context**
  - Usage: Split context across multi-agents (see: Drew’s post, Anthropic).
  - Multi-agents make conflicting decisions (see: Cognition/Walden Yan).
  - Sub-agents lower risk if avoid decisions (see: open-deep-research).

- **Cache Context**
  - Usage: Cached input token, Cache agent instructions, tool descriptions to prefix.
  - Claude & [Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) shared applicability of it, Gemini has [Context Caching](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)

## Manus

- [Context Engineering in Manus](https://rlancemartin.github.io/2025/10/15/manus/)
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## Anthropic

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

## LangGraph

- [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/)
  - [Google Docs and Notes](https://docs.google.com/presentation/d/16aaXLu40GugY-kOpqDU4e-S0hD1FmHcNyF0rRRnb1OU/)
- [Video - Context Engineering for Agents - Lance Martin, LangChain](https://www.youtube.com/watch?v=_IlTcWciEC4&t=1s)


## Devin (Cognition)

- [Don’t Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents)

## Misc

- [Context Engineering by Human Layer](https://docs.google.com/presentation/d/16ykxEU78250wG3mPKNrF5IfxxD1fIVgdLQD9tlSZa6M/edit?slide=id.g3a5a4059e08_0_2750#slide=id.g3a5a4059e08_0_2750)
