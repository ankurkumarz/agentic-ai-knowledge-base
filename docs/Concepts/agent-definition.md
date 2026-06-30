# Agent Definition

## What is an AI Agent?

An AI agent is an autonomous software entity that can perceive its environment, make decisions, and take actions to achieve specific goals. Unlike traditional software programs that follow predetermined instructions, AI agents exhibit intelligent behavior by:

- **Autonomy**: Operating independently without constant human intervention
- **Reactivity**: Responding to changes in their environment
- **Proactivity**: Taking initiative to achieve goals
- **Social Ability**: Interacting with other agents and humans

## Key Characteristics

### 1. Goal-Oriented Behavior
AI agents are designed with specific objectives and work towards achieving them through a series of actions and decisions.

### 2. Environmental Awareness
Agents can perceive and understand their operating environment, whether it's digital data, physical sensors, or user interactions.

### 3. Decision-Making Capabilities
Using various AI techniques (LLMs, machine learning, rule-based systems), agents can make informed decisions about their next actions.

### 4. Learning and Adaptation
Modern AI agents can learn from experience and adapt their behavior to improve performance over time.

## Agent Architecture Components

![Agent Definition Diagram](../assets/images/agent-definition-diagram.png)

The typical AI agent architecture includes:
- **Perception Module**: Processes environmental inputs
- **Decision Engine**: Determines appropriate actions
- **Action Module**: Executes decisions in the environment
- **Memory System**: Stores experiences and knowledge
- **Learning Component**: Improves performance over time

## OpenAI Definition (Practical Guide, 2024)

> "Agents are systems that independently accomplish tasks on your behalf."

OpenAI's production-oriented definition adds two concrete characteristics that distinguish a true agent from an LLM-powered app:

1. **Workflow control via LLM**: The agent uses an LLM to manage execution and make decisions. It recognises when a workflow is complete, can proactively correct its actions, and can halt execution and transfer control back to the user on failure.
2. **Dynamic tool selection within guardrails**: The agent has access to tools for interacting with external systems (data retrieval and action-taking) and selects the appropriate tools dynamically based on workflow state, always within defined guardrails.

Applications that integrate LLMs without using them to control workflow execution — simple chatbots, single-turn LLMs, sentiment classifiers — are **not** agents under this definition.

## Chat-Engine vs. Do-Engine (You.com, 2026)

You.com's 2026 AI Predictions whitepaper introduces a practical framing that sharpens the distinction between conversational AI and agentic AI:

- **Chat-Engine**: A system you converse with — it provides answers, summaries, or suggestions, but the human remains the executor of all actions.
- **Do-Engine**: A system that autonomously completes tasks end-to-end — it plans, selects tools, executes steps, and delivers outcomes without requiring the human to orchestrate each step.

This framing predicts a wholesale shift in how AI systems are built and valued: the utility of a Chat-Engine is bounded by human bandwidth; the utility of a Do-Engine scales with task complexity. Applications that integrate LLMs without delegating execution control remain Chat-Engines under this definition — and are expected to be superseded in enterprise value by Do-Engine architectures over 2026.

## AI Engineering Definition (Huyen, 2025)

Chip Huyen's *AI Engineering* (O'Reilly, 2025) provides a foundational definition from first principles:

> "An agent is anything that can perceive its environment and act upon that environment."

An agent is characterized by two dimensions:
1. **Environment**: The space the agent operates in — a game, the internet, a codebase, a kitchen, the road system
2. **Set of actions**: What the agent can do — augmented by the tools it has access to

The environment determines the *possible* actions. The agent's tool inventory restricts the *actual* environment it can operate in. A coding agent whose only tool is file editing is confined to the filesystem environment.

An AI agent specifically uses a foundation model as its "brain" — processing the task, reasoning about what to do, planning a sequence of actions, and determining when the task is complete. The key distinction from a simple LLM-powered app is that the model *controls the execution flow*, not just the generation of individual responses.

**Agent components in practice** (from Chapter 6):
- **Planning**: Breaking the goal into achievable sub-steps; deciding which tool to invoke next
- **Tools**: Read actions (search, retrieval, SQL query) and write actions (email, database write, API call)
- **Memory**: Short-term (in-context), episodic (session history), semantic (vector retrieval), procedural (system prompt / learned behavior)

The three main agent failure modes are: taking too long (infinite loops), making too many mistakes (compounding errors), and incurring too much cost (uncontrolled tool usage).

## See Also
- [Agent Types](agent-types.md)
- [Architecture and Design Patterns](../Architecture/components-selection.md)
- [OpenAI Design Patterns](../DesignPatterns/openai-patterns.md)
- [AI Engineering Overview](ai-engineering.md)
- [2026 AI Predictions (You.com)](ai-predictions-2026.md)