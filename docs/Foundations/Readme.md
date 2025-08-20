
## Definition

- [AI Agents by Berkley Book](https://aima.cs.berkeley.edu/). [N8N Blog](https://blog.n8n.io/ai-agents/) on AI Agent Flows.
![AI Agent Internal Arch](https://i.postimg.cc/ydGV1c3Q/ai-agents-arch.png)

```mermaid
flowchart TD
  %% --- Styles (safe) ---
  classDef env fill:#f7e8f0,stroke:#c2185b,stroke-width:2px,rx:12,ry:12,color:#111;
  classDef agent fill:#e8f7f0,stroke:#0f9d58,stroke-width:2px,rx:12,ry:12,color:#111;
  classDef comp fill:#e6f0fb,stroke:#1a73e8,stroke-width:1.5px,rx:8,ry:8,color:#111;
  classDef action fill:#fff5cc,stroke:#eab308,stroke-width:1.5px,rx:8,ry:8,color:#111;

  %% --- Environment ---
  subgraph ENV["Environment"]
    PERCEPTS["Percepts"]
    ACTIONS["Actions"]
  end
  class ENV env

  %% --- Agent ---
  subgraph AG["AI Agent"]
    S["Sensors<br/>(inputs, APIs, webhooks)"]
    PERCEPTION["Perception Layer<br/>(preprocess, embed)"]
    KB["Knowledge Base / Memory<br/>(facts, vectors, state)"]
    REASON["Reasoning Engine<br/>(LLM+prompts, rules, RL)"]
    PLAN["Planning & Goals<br/>(decompose, schedule)"]
    LEARN["Learning Module<br/>(feedback, fine-tune, RL)"]
    ACT["Actuators<br/>(APIs, commands, outputs)"]
  end
  class AG agent
  class S,PERCEPTION,KB,REASON,PLAN,LEARN,ACT comp

  %% --- Flow ---
  PERCEPTS --> S --> PERCEPTION --> KB
  PERCEPTION --> REASON
  KB --> REASON
  REASON --> PLAN --> ACT
  LEARN --> KB
  LEARN --> REASON
  ACT --> ACTIONS

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
