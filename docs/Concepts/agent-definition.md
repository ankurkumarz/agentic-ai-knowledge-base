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

## See Also
- [Agent Types](agent-types.md)
- [Architecture and Design Patterns](../Architecture/components-selection.md)
- [OpenAI Design Patterns](../DesignPatterns/openai-patterns.md)