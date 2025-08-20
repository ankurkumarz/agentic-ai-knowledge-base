
## Definition

- [AI Agents by Berkley Book](https://aima.cs.berkeley.edu/). [N8N Blog](https://blog.n8n.io/ai-agents/) on AI Agent Flows.

```mermaid
flowchart TD
    %% Define Styles
    classDef env fill:#fdf2f8,stroke:#db2777,stroke-width:2px,color:#000,rx:15,ry:15
    classDef agent fill:#ecfdf5,stroke:#10b981,stroke-width:2px,color:#000,rx:15,ry:15
    classDef comp fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#000,rx:10,ry:10
    classDef action fill:#fef9c3,stroke:#eab308,stroke-width:1.5px,color:#000,rx:10,ry:10

    %% Environment
    subgraph ENV["🌍 Environment"]
        P[🔎 Percepts]
        A[🎯 Actions]
    end
    class ENV env

    %% Agent
    subgraph AG["🤖 AI Agent"]
        S[📡 Sensors\n(Inputs, APIs, Webhooks)]
        Perception[🧩 Perception Layer\nPreprocessing, Embeddings]
        KB[(📚 Knowledge Base / Memory\nFacts, Vectors, State History)]
        RE[🧠 Reasoning Engine\nLLM + Prompts, Rules, RL]
        Plan[📋 Planning & Goals\nTask Decomposition, Scheduling]
        L[📈 Learning Module\nRL, Fine-tuning, Feedback]
        Act[⚙️ Actuators\nAPIs, Commands, Outputs]
    end
    class AG agent
    class S,Perception,KB,RE,Plan,L,Act comp

    %% Connections
    ENV -- Percepts --> S --> Perception --> KB
    Perception --> RE
    KB --> RE
    RE --> Plan --> Act
    L --> KB
    L --> RE
    Act --> ENV -- Actions -->
```

- [Definition by Harrison, LangChain Founder](https://blog.langchain.dev/what-is-an-agent/)
- [Ambient Agents](https://blog.langchain.dev/introducing-ambient-agents/): Ambient agents listen to an event stream and act on it accordingly, potentially acting on multiple events at a time)
- [12-Factor Agents - Principles for building reliable LLM applications](https://github.com/humanlayer/12-factor-agents/)

## Agentic Architecture

- [Agents Intro - a Google Whitepaper](https://www.kaggle.com/whitepaper-agents)
- [Building Effective Agents - Anthropic](https://www.anthropic.com/research/building-effective-agents)
- [Cohere - How enterprises can start building Agentic AI](https://cohere.com/blog/how-enterprises-can-start-building-agentic-ai)
- [AI Agents vs. Agentic AI White paper](https://arxiv.org/abs/2505.10468)

![AI Agents vs. Agentic AI](https://i.postimg.cc/y6R91zcW/IMG-0956.jpg)


## Agentic Workflows

- [Intro to Agentic Workflows by N8N](https://blog.n8n.io/ai-agentic-workflows/)

## Retrieval Strategies for Agents

- [Generative Retrieval including traditional retrieval, hybrid retrieval, semantic retrieval, knowledge-based retrieval, and agentic contextual retrieval](https://arxiv.org/abs/2502.16866)

## LLM Foundation

- [Foundations of Large Language Models](https://arxiv.org/pdf/2501.09223)

## Architecture Layers

![Arch](https://i.postimg.cc/PfbMFPM0/IMG-0894.jpg)
