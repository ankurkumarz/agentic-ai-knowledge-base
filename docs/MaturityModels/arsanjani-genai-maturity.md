# Arsanjani GenAI Maturity Model

## Overview

The **GenAI Maturity Model** from *Agentic Architectural Patterns for Building Multi-Agent Systems* (Arsanjani & Bustos, Packt, 2026) defines seven levels (0–6) as a strategic roadmap for enterprise AI adoption — from raw data preparation to sophisticated multi-agent collaboration. It is notable for explicitly mapping maturity levels to architectural patterns: an organization's maturity is a direct result of the specific patterns it implements, not just its stated intent.

Security, Privacy, and Compliance are treated as cross-cutting concerns at every level.

## Maturity Levels

| Level | Title | Key Activities | Example |
|---|---|---|---|
| 0 | Prepare data (data foundation) | Acquire, generate (including synthetic), clean, curate, and govern data; address quality, relevance, licensing, and accessibility | Building a governed data lake; establishing data lineage |
| 1 | Select model and prompt/serve | Select pretrained foundation models; design prompts (prompt engineering); deploy and serve via APIs for content generation, Q&A, and basic function calling | A chatbot that answers HR questions using model knowledge |
| 2 | Contextual enhancement (RAG) | Use RAG to dynamically fetch external knowledge (documents, databases) and augment prompts; improves accuracy and reduces hallucination | An internal knowledge bot that retrieves live policy documents before answering |
| 3 | Tuning for specificity | Fine-tune models using PEFT/LoRA adaptor tuning or full fine-tuning with domain-specific data; specializes terminology, style, and behavior for agent roles | Tuning a model on enterprise sales data to understand sales-specific jargon |
| 4 | Grounding and evaluation | Implement output grounding (citations, source linking) and robust evaluation frameworks covering accuracy, bias, fairness, and safety | A financial analysis agent that provides summaries with explicit references to source reports |
| 5 | Single-agent systems | Architect systems around one autonomous AI agent performing multi-step reasoning, planning, and tool use (via function calling or MCP); requires LLMOps/AgentOps for lifecycle management | A travel planning agent that autonomously books flights and hotels via real APIs |
| 6 | Multi-agent systems | Deploy multiple specialized agents that collaborate, coordinate (via A2A protocol), and negotiate to solve problems exceeding a single agent's capacity | A supply chain system where inventory, logistics, and forecasting agents collaborate to respond to disruptions |

## Agentic AI Maturity Spectrum (Expanded Levels 5–6)

Within the agentic portion (Levels 5–6), the book defines six finer-grained sub-levels that map directly to the coordination pattern catalog:

| Sub-level | Description | Key Patterns |
|---|---|---|
| 1 – Basic agentic | Single agents, fixed workflows, predefined tool calls | Single-Agent Baseline, Static Function Calling, Watchdog Timeout, Agent Calls Human |
| 2 – Dynamic single-agent | Single agent dynamically selects from pre-approved tools | Agent Router, Dynamic Tool Selection, Simple RAG, Simple Retry |
| 3 – Introspective (ReAct/Reflexion) | Self-reflection and self-correction feedback loops | ReAct, Reflexion, Instruction Fidelity Auditing, Adaptive Retry with Prompt Mutation |
| 4 – Multi-agent systems | Multiple specialized agents; structured top-down coordination | Supervisor Architecture, Multi-Agent Planning, Shared Epistemic Memory, Event-Driven Reactivity, Tool/Agent Registry |
| 5 – Advanced with meta-agents | A meta-agent oversees and dynamically reassigns work | Meta-agents, Blackboard Topology, Resource Allocation, Contract-Net Marketplace, Supervision Trees |
| 6 – Self-correcting agents | Multi-turn feedback loops; agents critique and refine each other iteratively | Consensus, Agent Negotiation, Conflict Resolution, FCoT Embedding, Coevolved Agent Training, Trust Decay |

## The New Agentic Stack

Advancing toward Levels 5–6 requires mastering three complementary interoperability layers:

| Layer | Technology | Purpose |
|---|---|---|
| 1 – Function calling | Native LLM capability | Agent's LLM invokes local tools within a single application runtime |
| 2 – Model Context Protocol (MCP) | Anthropic's open standard | Standardizes how agents discover and invoke external tools as independent interoperable services (agent → tools) |
| 3 – Agent-to-Agent (A2A) | Google's open protocol | Universal standard for structured task delegation and collaboration between independent agents on any framework (agent → agent) |

Mental model: **MCP = agent connects to tools; A2A = agents connect to each other.** In a complete multi-agent workflow, an orchestrator uses A2A to delegate tasks → worker agents use MCP to access the tools they need → results flow back through A2A.

## Agent Anatomy

The book defines seven internal components that form the continuous operational loop of any AI agent:

| Component | Function | Implementation |
|---|---|---|
| Goals | Objectives the agent seeks to achieve | Configuration parameters or dynamic state |
| Sense (Perception) | Gathers data from environment (APIs, databases, sensors) | API listeners, data stream processors, MCP clients |
| Reason (Cognition) | Analyzes sensed information using LLM | The agent-ready LLM; interprets inputs against goals |
| Plan | Devises a sequence of actions | LLM-generated task sequence; can be static or dynamic |
| Act (Action) | Executes plan via tools | External API calls, code execution, response generation |
| Memory | Stores knowledge, state, and past experience | Short-term (in-context); long-term (vector databases, persistent stores) |
| Coordinate | Interacts with other agents (multi-agent systems only) | A2A protocol; tracks task lifecycle states (submitted, working, completed) |

**The agentic loop:** Sense → Reason → Plan → Act → (feedback) → Sense. Each iteration allows the agent to adapt based on outcomes.

## Practical Rollout Roadmap

Chapter 12 of the book maps patterns to three implementation stages:

| Stage | Core Principle | Patterns to Implement |
|---|---|---|
| 1 – Foundational system | Build one thing well; test every integration | Single-Agent Baseline, basic observability, static tool calling |
| 2 – Production-ready service | Reliability and scalability | Watchdog Timeout, Adaptive Retry, Canary Testing, checkpointing, evaluation pipelines |
| 3 – Self-improving ecosystem | Continuous learning and multi-agent coordination | Coevolved Agent Training, Trust Decay, Swarm Architecture, Consensus |

## Key Production Challenges

The book identifies four categories of challenges in transitioning from PoC to production:

| Category | Key Challenges |
|---|---|
| Strategic and organizational | Demonstrating ROI, achieving stakeholder alignment, operational integration, change management |
| Data-related | Data governance, data quality, data silos, privacy compliance (GDPR, HIPAA) |
| Model and technical | Model robustness, adversarial attacks, hallucination minimization, legacy system integration, LLMOps/AgentOps |
| Ethical and responsible AI | Bias mitigation, transparency, explainability, governance frameworks |

## See Also

- [Agentic Architectural Patterns — Arsanjani & Bustos](../DesignPatterns/arsanjani-patterns.md)
- [AWS GenAI Maturity Model](./aws-genai.md)
- [Gartner's Perspective](./gartner.md)
- [Google's Perspective](./google.md)
- [Agentic Engineering Levels](./agentic-engineering-levels.md)
- [Agentic Architecture Components](../Architecture/components-selection.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [Standards: MCP](../Standards/mcp.md)
- [Standards: A2A](../Standards/agent2agent.md)

## References

- Arsanjani, A., & Bustos, J.P. (2026). *Agentic Architectural Patterns for Building Multi-Agent Systems*. Packt Publishing. ISBN 978-1-80602-957-0. — Comprehensive pattern catalog and GenAI maturity model; code at https://github.com/PacktPublishing/Agentic-Architectural-Patterns-for-Building-Multi-Agent-Systems
