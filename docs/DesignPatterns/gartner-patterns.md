# Gartner LLM-based AI Design Patterns

## Overview

 [Emerging Patterns for Building LLM-Based AI Agents](https://www.gartner.com/en/documents/6142159)

## Patterns for Building LLM-Based Agents

Gartner's diagram outlines patterns across three categories: Agent Architectures, Functional Patterns, and Operational Patterns for LLM-based AI agents.

### Agent Architectures
- **Solo Agent**: Atomic, monolithic agents for simple tasks.
- **Agent Roles**: Define personas to guide behavior and scope.
- **Agent-to-Agent Handoff**: Delegation in multi-agent systems.
- **Multi-Agent Modularity**: Decomposes tasks across specialized sub-agents.

### Functional Patterns
- **Prescribed Plan**: Fixed workflows for repeatable processes.
- **Dynamic Plan**: Runtime strategy generation for adaptability.
- **MHQA**: Multi-hop question answering with iterative retrieval.
- **Collaborating Agents**: Dynamic teamwork.
- **Orchestrated Agents**: Predefined graphs for controlled interactions.
- **LLM Interaction Patterns**: ReAct (reason-act loops), Reflexion (self-critique), Chain of Thought (step-by-step reasoning).

### Operational Patterns
- **Agent Evaluation**: User-in-the-loop oversight; LLM-as-judge (deterministic).
- **Agent Action Patterns**: Function calling, generated code, API tools.
- **Memory Patterns**: RAG (retrieval-augmented generation), memory longevity, memory scope.
- **Security Patterns**: LLM guardrails, identity tokens, logging.