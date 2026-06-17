# Multi-Agent Systems

## Overview

Multi-agent systems (MAS) consist of multiple autonomous agents that interact and collaborate to solve complex problems that are beyond the capabilities of individual agents.

![Multi-Agent Architecture](../assets/images/multi-agent-architecture.png)
(Source: [LangChain](https://blog.langchain.com/how-and-when-to-build-multi-agent-systems/))

## Key Characteristics

### Distributed Intelligence
- **Decentralized Decision Making**: Each agent makes autonomous decisions
- **Specialized Capabilities**: Agents have specific roles and expertise
- **Collaborative Problem Solving**: Agents work together toward common goals
- **Emergent Behavior**: System-level intelligence emerges from agent interactions

### Communication and Coordination
- **Message Passing**: Agents exchange information and requests
- **Negotiation Protocols**: Agents negotiate resource allocation and task assignment
- **Consensus Mechanisms**: Agents reach agreement on shared decisions
- **Coordination Strategies**: Agents synchronize their actions

## Architecture Patterns

### Hierarchical Organization
```
Manager Agent
├── Specialist Agent A
├── Specialist Agent B
└── Coordinator Agent
    ├── Worker Agent 1
    └── Worker Agent 2
```

**Benefits**:
- Clear command structure
- Efficient task delegation
- Scalable organization

### Peer-to-Peer Network
```
Agent A ←→ Agent B
    ↕       ↕
Agent C ←→ Agent D
```

**Benefits**:
- Fault tolerance
- Distributed processing
- No single point of failure

### Blackboard Architecture
```
Shared Knowledge Space (Blackboard)
    ↑           ↑           ↑
Agent A    Agent B    Agent C
```

**Benefits**:
- Shared information access
- Asynchronous collaboration
- Flexible agent participation

## Implementation Frameworks

### AutoGen (Microsoft)
- **Conversational Agents**: Multi-agent chat systems
- **Role-based Design**: Specialized agent roles
- **Human-in-the-loop**: Interactive agent collaboration

```python
import autogen

# Define agents with specific roles
user_proxy = autogen.UserProxyAgent("user_proxy")
assistant = autogen.AssistantAgent("assistant")
critic = autogen.AssistantAgent("critic")

# Create group chat
groupchat = autogen.GroupChat(
    agents=[user_proxy, assistant, critic],
    messages=[],
    max_round=10
)
```

### CrewAI
- **Role-based Agents**: Defined roles and responsibilities
- **Task Management**: Structured task assignment and execution
- **Process Orchestration**: Workflow management

```python
from crewai import Agent, Task, Crew

# Define specialized agents
researcher = Agent(
    role='Researcher',
    goal='Gather comprehensive information',
    backstory='Expert in information gathering'
)

writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Skilled content creator'
)

# Create crew with agents and tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task]
)
```

### LangGraph
- **Graph-based Workflows**: Visual workflow representation
- **State Management**: Shared state across agents
- **Conditional Logic**: Dynamic workflow paths

## Communication Protocols

### Message Types
- **Inform**: Share information without expecting response
- **Request**: Ask for action or information
- **Propose**: Suggest a course of action
- **Accept/Reject**: Respond to proposals
- **Query**: Ask questions about agent state or capabilities

### Coordination Mechanisms
- **Contract Net Protocol**: Bidding for task assignment
- **Consensus Algorithms**: Distributed agreement
- **Market Mechanisms**: Economic-based coordination
- **Voting Systems**: Democratic decision making

## Use Cases and Applications

### Software Development
- **Code Review Teams**: Multiple agents reviewing different aspects
- **Testing Automation**: Specialized testing agents
- **Documentation Generation**: Collaborative content creation

### Business Process Automation
- **Customer Service**: Routing and specialized handling
- **Supply Chain Management**: Distributed optimization
- **Financial Analysis**: Multi-perspective evaluation

### Research and Analysis
- **Literature Review**: Parallel information gathering
- **Data Analysis**: Specialized analytical agents
- **Report Generation**: Collaborative synthesis

## Design Considerations

### Agent Specialization
- **Domain Expertise**: Agents focused on specific areas
- **Capability Complementarity**: Agents with different strengths
- **Role Clarity**: Well-defined responsibilities and boundaries

### Scalability
- **Dynamic Agent Creation**: Adding agents as needed
- **Load Distribution**: Balancing work across agents
- **Resource Management**: Efficient resource utilization

### Fault Tolerance
- **Redundancy**: Multiple agents for critical functions
- **Graceful Degradation**: System continues with reduced capability
- **Recovery Mechanisms**: Automatic error recovery

## Best Practices

### System Design
1. **Clear Role Definition**: Each agent should have well-defined responsibilities
2. **Minimal Coupling**: Reduce dependencies between agents
3. **Standard Interfaces**: Use consistent communication protocols
4. **Monitoring and Logging**: Track agent interactions and performance

### Implementation
1. **Start Simple**: Begin with basic multi-agent interactions
2. **Iterative Development**: Gradually add complexity and agents
3. **Testing Strategy**: Test individual agents and system interactions
4. **Performance Optimization**: Monitor and optimize system performance

## Challenges and Solutions

### Common Challenges
- **Coordination Overhead**: Managing agent interactions
- **Conflict Resolution**: Handling disagreements between agents
- **Scalability Limits**: Performance degradation with many agents
- **Debugging Complexity**: Tracing issues in distributed systems

### Solutions
- **Efficient Protocols**: Use lightweight communication mechanisms
- **Conflict Resolution Strategies**: Implement negotiation and arbitration
- **Hierarchical Organization**: Structure agents to reduce complexity
- **Comprehensive Logging**: Detailed tracking of agent activities

## The Four Planes of a Multi-Agent System (AWS)

AWS frames multi-agent systems around four distinct planes, each with a clear responsibility:

| Plane | Responsibility | AWS Services |
|---|---|---|
| Control plane | Orchestrator decomposes tasks, delegates to subagents, monitors progress, synthesizes results. Directs — does not execute. | Amazon Bedrock Multi-Agent Collaboration (supervisor mode), AWS Step Functions |
| Execution plane | Independent specialized agents with scoped system prompts, curated tools, and purpose-built retrieval corpora. Independently deployable, evaluatable, and scalable. | Amazon Bedrock AgentCore, AWS Lambda |
| State plane | Shared information layer: task state (durable), session context (low latency), domain knowledge (retrieval). Agents coordinate through state, not direct coupling. | Amazon DynamoDB, Amazon ElastiCache, Amazon Bedrock Knowledge Bases |
| Capability plane | Tools exposed through MCP servers — standardized, discoverable, governed. Shared across agents with per-agent access controls at the server level. | Amazon MCP Servers, Amazon Bedrock AgentCore, AWS Lambda |

## When to Move to Multi-Agent

Four triggers that signal a single-agent workflow is breaking down:

| Trigger | Description |
|---|---|
| Context saturation | Complex long-horizon tasks overflow a single context window. The agent forgets earlier work but does not know it has. |
| Task specialization | One agent trying to excel at multiple domains simultaneously produces mediocrity across the board rather than excellence in any domain. |
| Latency and parallelism | Sequential execution is unnecessarily slow. Independent subtasks should run in parallel. |
| Fault isolation | A single-agent failure derails the entire workflow. Multi-agent systems localize failures — one agent down does not stop the rest. |

Rule of thumb: move to multi-agent when your single-agent workflow shows any two of these four triggers simultaneously.

## Orchestration Patterns

Four patterns, each suited to a different task structure:

| Pattern | When to Use | AWS Implementation | Watch Out |
|---|---|---|---|
| Centralized orchestration | Complex, open-ended tasks requiring dynamic planning and real-time adaptation | Amazon Bedrock Multi-Agent (supervisor mode) | Orchestrator is a single point of failure — invest heavily here |
| Skill-based dispatch | Fixed set of well-defined, parameterized operations invoked by a reasoning agent | AWS Lambda functions behind MCP server interfaces | Less flexible for open-ended tasks; best for known, stable operations |
| Handoff chains | Linear sequential pipelines where each step depends on the previous output | Step Functions state machines with Choice states | Rigidity — branching logic can become unwieldy without proper Choice state design |
| Parallel fan-out and synthesis | Multi-domain tasks where independent specialist analysis can be parallelized | Amazon EventBridge + Amazon SQS + Lambda specialists | Synthesis step is routinely underbuilt — handle conflicting results explicitly |

## Non-Determinism at Scale

Non-determinism compounds across agent boundaries. With 90% per-agent accuracy:

| Pipeline depth | Compound accuracy |
|---|---|
| 1 agent | 90% |
| 2-agent pipeline | 81% |
| 4-agent pipeline | 66% |

With 99% per-agent accuracy, a 4-agent pipeline reaches 96%. Individual agent quality must be substantially higher than the acceptable overall error rate.

Three defenses against propagation:
- **Structured schema at every boundary** — require JSON-schema-validated outputs at every handoff. Free-form inter-agent prose is a bug.
- **Abstention as a feature** — agents uncertain about a task should return a structured abstention response, not a low-confidence guess. Build and evaluate abstention behavior explicitly in golden datasets.
- **End-to-end evaluation (non-optional)** — per-agent evaluations are necessary but not sufficient. Run complete workflow evaluations. `Builtin.GoalSuccessRate` measures system-level success, not per-agent output quality.

## Shared State and Handoff Design

What to store where:

| Store | Latency | Use For | AWS Service |
|---|---|---|---|
| Task state | Single-digit ms reads, survives agent failures, audit trail | Durable workflow execution state | Amazon DynamoDB |
| Session context | Sub-ms access, TTL-managed | Conversation turns + recently accessed payloads | Amazon ElastiCache |
| Domain knowledge | Vector retrieval, governance-controlled | Shared across all agents with no duplication | Amazon Bedrock Knowledge Bases |
| Intermediate results | Cost-effective, durable | Referenced by task state record in DynamoDB, not forwarded in payloads | Amazon S3 |

**Handoff payload principle**: include what the next agent needs — nothing more. Verbose payloads bloat context windows and degrade reasoning quality.

## MCP vs. A2A in Multi-Agent Systems

| Protocol | Interface | Pattern | Rule |
|---|---|---|---|
| MCP | Agent → Tool | Client-server; agent is always the client, tool server is always the responder | Per-agent access controls must be implemented at the server level — not in system prompts |
| A2A | Agent → Agent | Peer protocol; any agent can initiate or receive | Do not use MCP for agent-to-agent delegation — it is the wrong abstraction |

A2A task objects carry: description, context, authorized resources, expected output schema, and constraints. Agent cards enable dynamic discoverability without pre-built integration.

## Failure Modes Unique to Multi-Agent Systems

| Failure Mode | Description | Mitigation |
|---|---|---|
| Cascading failures | One failing agent takes down the entire chain | Circuit breakers in Step Functions catch repeated failures and route to fallback paths |
| Orchestration loops | Orchestrators that repeatedly delegate tasks in a cycle run up unbounded costs | Explicit step counters, loop detection, and forced termination conditions; Step Functions enforces maximum execution time and step limits natively |
| Conflicting parallel outputs | Parallel agents evaluate the same configuration and reach opposite conclusions | Synthesis step must resolve conflicts explicitly — not with a generic summarize prompt; in safety-critical domains, the conservative result always wins |
| Context corruption at handoffs | Malformed, truncated, or semantically inconsistent payloads cause silent failures | Schema-validate every incoming handoff payload before acting; return a structured error to the orchestrator on validation failure |

## Security at Agent Boundaries

Zero trust: treat every agent boundary as a trust boundary. Apply security controls redundantly at MCP server, agent boundary, and orchestration layer.

| Risk | Mitigation |
|---|---|
| Overprivileged subagents | Least-privilege scoped credentials per task; AWS STS generates time-limited credentials |
| Prompt injection propagation | Content filtering at every agent boundary via Amazon Bedrock Guardrails; treat all externally-originated content as untrusted regardless of how many agents have processed it |
| Credential exposure in payloads | Never pass raw credentials in task objects; use IAM role-based delegation; AWS IAM Roles Anywhere for non-AWS workloads |
| Unauthorized agent discovery | Agent card registry with authentication requirements |

## Distributed Observability

A consistent trace ID — propagated through every agent and tool call — is the only way to correlate logs into a single execution graph. Without distributed tracing, root-cause analysis is guesswork.

Layered evaluation strategy: per-agent (isolated datasets) + full workflow (`Builtin.GoalSuccessRate`) + differential analysis correlating per-agent scores against system-level outcomes.

## Seven Benefits of Multi-Agent Systems

From *Mastering Multi-Agent Systems* (Galileo, 2026), the seven primary advantages over single-agent approaches:

| Benefit | Single-Agent Limitation | Multi-Agent Solution |
|---|---|---|
| Specialization | One model handles all tasks, losing context as it switches domains | Specialized agents each maintain focused context, reducing hallucinations |
| Validation (orthogonal checking) | No self-correction mechanism; confident when wrong | Peer-review layers: Generation → Logic → Fact → Safety agents catch errors the initial model misses |
| Parallel processing | Sequential processing hits time and context limits | Dispatcher + parallel Analysis agents + Aggregator; 20 min → 3 min on 100-review workloads |
| Fault tolerance | Single point of failure stops everything | Graceful degradation: failed agent spawns backup or flags for human review; partial work is preserved |
| Dynamic routing | Same model for simple FAQs and complex reasoning | Route by confidence: >0.9 = fully automated; 0.7–0.9 = human review option; <0.7 = specialist or human |
| Context preservation | Forgets early messages as context window fills | Separate Memory Agent + Consistency Checker maintains coherence across 50+ message sessions |
| Observability | Black box — hard to know why something went wrong | Per-agent metrics, A/B testing of individual agents, token cost attribution per component |

**Gartner prediction**: 40% of agentic AI projects will be canceled by 2027 due to reliability issues. The successful 60% will match architecture to actual needs.

## When Multi-Agent Systems Actually Work

Three patterns that successful implementations share (from Galileo research):

1. **Problems that can be parallelized** — subtasks require zero communication during processing. Each agent works independently; results are aggregated at the end.
2. **Read-heavy, write-light workloads** — agents primarily consume information rather than modify shared state. Coordination complexity drops dramatically.
3. **Explicit coordination rules** — deterministic orchestration with clear handoff points, defined data formats, interaction protocols, and fallback behaviors.

**Checklist before building**:
- Can you break down the work into completely independent tasks?
- Do agents primarily read and analyze rather than write and modify?
- Can results be combined mechanically (concatenation, voting, averaging)?
- Is parallel processing speed worth a 2–5× cost increase?
- Can one agent failing be isolated from others?

## When Multi-Agent Systems Fail

### Coordination Cost Economics

Two agents need one communication channel. Three need three. Four need six. Coordination overhead grows quadratically. Three high-impact failure scenarios:

1. **Memory fragments across agents** — Agent B needs Agent A's output but gets either too much (expensive) or too little (broken functionality). No clean way to share only relevant details.
2. **Operational costs multiply** — A task costing $0.10 for a single agent may cost $1.00 in a multi-agent system due to context sharing, handoffs, and verification.
3. **Write conflicts cascade** — Agent A creates a user profile structure. Agent B creates a different one. Agent C reconciles both and creates a third. Three incompatible representations of the same data.

### Concrete Cost Comparison (Customer Support)

| Approach | Time | Cost | Failure Points |
|---|---|---|---|
| Single agent (reads ticket, searches docs, checks account, crafts reply) | 2s | $0.05 | 1 |
| Multi-agent (Triage + Research + Account + Response + Orchestrator) | 3.8s | $0.40 | 5 agents, 10 potential interaction bugs |

The multi-agent system costs 8× more, takes nearly twice as long, and creates exponentially more ways to fail.

### The Model Evolution Challenge

Rich Sutton's Bitter Lesson: general methods using more computation ultimately win over specialized structures. Multi-agent complexity often compensates for current model limitations that will disappear:

- Context windows too small → distribute the load (but windows are growing)
- Tool calling unreliable → create dedicated tool-use agents (but models are improving)
- Complex reasoning fails in one pass → split into specialist agents (but newer models handle this natively)

Teams that built complex orchestration layers for GPT-4 found them unnecessary with GPT-5. **Design for removal**: write orchestration code in a separate module that can be deleted when a better model arrives. Make agent boundaries collapsible so Agent A (research) and Agent B (summarize) can merge into one "research and summarize" agent later.

### The Decision Framework (5 Questions)

Before building a multi-agent system, answer in order:

1. **Can better prompt engineering solve this?** In 80% of cases, a well-crafted single agent with good context management beats multi-agent.
2. **Are your subtasks genuinely independent?** Real independence = zero shared state during processing. Sequential tasks with dependencies are not parallel work.
3. **Can you afford the cost increase?** Expect 2–5× more than single agents due to coordination overhead, duplicate context, and retry logic.
4. **Is your latency tolerance measured in seconds?** Each agent handoff adds 100–500ms. Five agents can add 2+ seconds.
5. **Do you have debugging infrastructure?** Multi-agent failures require tracing through multiple execution paths, shared state changes, and inter-agent communication logs.

## The Four Primary Architectures

### 1. Centralized: The Orchestrator Pattern

A single powerful agent serves as the central coordinator, allocating tasks, monitoring progress, and synthesizing results. All data flows through one hub.

**Performance characteristics**:
- Token efficiency: high (no duplicate work)
- Latency: higher (sequential coordination)
- Throughput: ceiling based on orchestrator capacity
- Context: concentrated on the central agent

**Best for**: Simple workflows requiring strong consistency; complex queries needing dynamic planning (e.g., Anthropic's Research agent spawning specialized subagents).

**Watch out**: Orchestrator is a single point of failure. Becomes a choke point at 10–20 agents.

**Map-reduce pattern**: Orchestrator maps work to parallel agents, then reduces their results into a single answer.

### 2. Decentralized: Peer-to-Peer Coordination

Agents communicate directly with neighbors, making local decisions without central coordination. Intelligence emerges from local interactions.

**Performance characteristics**:
- Token efficiency: lower (potential duplicate work)
- Latency: lower for local decisions
- Throughput: scales linearly with agents
- Context: distributes evenly across the system

**Best for**: Systems requiring resilience and local optimization; enterprise HR systems where benefits, payroll, retirement, and time-off agents coordinate directly.

**Watch out**: Coordinating global behavior is challenging; maintaining consistency without central authority is difficult.

### 3. Hierarchical: Multi-Level Management

Multiple layers of supervision create a tree structure. Supervisor agents perform task planning, break down work, assign sub-tasks, and facilitate communication between specialists.

**Performance characteristics**:
- Token efficiency: moderate (some redundancy between levels)
- Latency: moderate (multi-hop coordination)
- Throughput: high (parallel teams)
- Context: segments by level and team

**Best for**: Complex multi-domain problems that naturally decompose into sub-problems; news aggregation platforms with content, fact-checking, and publishing teams. Google ADK exemplifies this pattern.

**Watch out**: Coordination overhead between levels adds complexity. Each level should add meaningful abstraction, not bureaucracy.

### 4. Hybrid: Strategic Center, Tactical Edges

Combines centralized control with decentralized flexibility. Global decisions flow from central coordinators; local optimizations happen through peer interactions.

**Performance characteristics**:
- Token efficiency: varies based on task distribution
- Latency: optimizes for both global and local operations
- Throughput: combines benefits of both approaches
- Context: strategic at center, tactical at edges

**Best for**: Enterprise-scale systems with mixed requirements (e.g., food delivery: central orchestrator handles payments and order integrity; regional agent clusters handle routing and timing).

**Watch out**: Highest complexity; requires careful definition of the boundary between centralized and decentralized zones.

### Architecture Selection Matrix

| Primary Need | Best Architecture |
|---|---|
| Simple workflows, strong consistency | Centralized |
| Resilience, local optimization | Decentralized |
| Complex domains with team structures | Hierarchical |
| Enterprise systems with mixed requirements | Hybrid |

### Architecture Decision Factors

- **Consistency requirements**: Perfect sync across all agents → centralized. Agents can work with slightly stale data → decentralized.
- **Scale trajectory**: 3–5 agents → centralized. Dozens to hundreds within months → hierarchical or hybrid.
- **Team structure**: Clear reporting lines → hierarchical. Flat organization → peer-to-peer.
- **Problem decomposition**: Completely independent chunks → decentralized. Tasks that build on each other → centralized or hierarchical.

## Framework Comparison for Multi-Agent Architectures

| Framework | Key Strengths | Best For |
|---|---|---|
| LangGraph | Directed graph modeling, persistent memory across turns, full state tracking, handles conditional flows | Complex workflows with state management; hierarchical and hybrid patterns |
| Agno | ~2μs agent creation, ~3.75 KiB per agent, multi-modal support, minimal resource footprint | High-performance, high-volume operations (e.g., 500 simultaneous stock analysis agents) |
| Mastra | Native TypeScript, works with existing REST APIs, graph-based workflows, no separate AI infrastructure | Web applications and TypeScript projects |
| CrewAI | Predefined agent personas, minimal configuration, centralized orchestration, consistent role behaviors | Role-based collaboration and rapid prototyping |
| Google ADK | Flexible orchestration (Sequential/Parallel/Loop), hierarchical composition, built-in evaluation framework, Vertex AI integration | Multi-agent systems on GCP; news aggregation, content pipelines |
| AWS Strands | Model-driven approach, native MCP support, A2A protocol for agent discovery | Production-ready agents on AWS; code modernization systems |

**Framework choice implies architectural decisions**: LangGraph suits hierarchical and hybrid patterns; CrewAI suits centralized; Agno suits decentralized high-throughput; Mastra suits hybrid web-integrated systems.

## Supervisor vs. Swarm: A Direct Comparison

Arsanjani & Bustos (2026) formalize the two primary task-delegation frameworks as a design choice axis:

| Feature | Supervisor Architecture (Centralized) | Swarm Architecture (Decentralized) |
|---|---|---|
| Control flow | Hierarchical; single orchestrator delegates to workers | Peer-to-peer; agents self-select tasks from a shared board |
| Coordination | Explicit and top-down; supervisor manages workflow | Emergent and bottom-up; arises from local agent interactions |
| Modularity | High; specialist agents added or replaced under supervisor | High; agents added or removed from the swarm |
| Key benefit | Predictability, clear oversight, easy to govern and debug | Resilience, no single point of failure, horizontal scalability |
| Key drawback | Supervisor is a single point of failure and potential bottleneck | Hard to debug; governance and compliance enforcement is difficult |
| Best for | Regulated workflows (finance, healthcare) with clear sequential logic | Creative tasks, content pipelines, dynamic environments |

**Implementation guidance:** Start with Supervisor Architecture in enterprise contexts. Introduce Swarm for sub-teams where resilience matters more than predictability. Many production systems use a hybrid: a Supervisor manages the business process but delegates blocks to self-organizing crews.

## Agent Router Pattern

The Agent Router is the foundational building block for Supervisor Architecture. Rather than hard-coded conditional routing, it uses:

1. **Semantic intent extraction** — an LLM with a strict schema translates a user query into a structured `RoutingIntent` object with an action (verb) and resource (noun)
2. **Capability graph lookup** — a graph maps `(action, resource)` tuples to agent names; if no match exists the request is rejected

This decouples the extraction layer from agent names, allows new agents to register without touching routing logic, and uses the graph as a safety whitelist preventing routing to incapable agents.

## Event-Driven Realizations of Multi-Agent Patterns (Confluent)

Confluent's *A Guide to Event-Driven Design for Agents and Multi-Agent Systems* (2025) reframes agents as functioning much like microservices — and argues that the same shift from tightly coupled, request/response microservices to event-driven architecture (EDA) should apply to multi-agent coordination. Applied to the patterns above:

- **Centralized / Orchestrator-Worker**: instead of the orchestrator holding direct connections to every worker, it publishes keyed command messages to a Kafka topic. Worker agents form a **consumer group**, pulling from assigned partitions; the same key is reused across a stateful sequence so it lands on the same worker. The **Kafka Consumer Rebalance Protocol** automatically rebalances load as workers are added or removed, and a failed worker recovers by **replaying the log from its last saved offset** — removing the need for the orchestrator's bespoke failure-handling logic.
- **Hierarchical**: the orchestrator-worker decomposition is applied recursively, with every non-leaf node acting as orchestrator for its own subtree. Agents publish/subscribe to event streams across tiers rather than relying on direct supervision references, so hierarchy levels can be added or removed without touching core logic.
- **Blackboard**: the shared knowledge base is implemented as a Kafka topic; agents publish updates as events and other agents subscribe to only the updates relevant to them, avoiding the synchronization bottleneck of a directly-queried shared database.
- **Market-Based** *(not covered by the four architectures above — a fifth coordination mode)*: agents publish bids/offers as events; a market-making service matches them and executes transactions asynchronously. This replaces O(n²) direct peer-to-peer negotiation with interaction through a single central event log — the pattern underlying high-throughput use cases like real-time financial trading agents.

Full pattern-by-pattern treatment (Traditional vs. Event-Driven, plus worked SDR and Agentic RAG examples) is in [Event-Driven Design Patterns for Multi-Agent Systems (Confluent)](../DesignPatterns/event-driven-patterns.md).

## See Also
- [Event-Driven Design Patterns for Multi-Agent Systems (Confluent)](../DesignPatterns/event-driven-patterns.md)
- [Agent Development Frameworks](../AgenticFrameworks/README.md)
- [Architecture Components Selection](components-selection.md)
- [12-Factor Agents](12-factor-agents.md)
- [Context Engineering](../ContextEngineering/README.md)
- [AWS AgentCore](../AgentPlatforms/aws-agentcore.md)
- [A2A Protocol](../Standards/agent2agent.md)
- [MCP Protocol](../Standards/mcp.md)
- [ProductionBestPractices/deployment.md](../ProductionBestPractices/deployment.md)
- [ProductionBestPractices/security.md](../ProductionBestPractices/security.md)
- [ProductionBestPractices/observability.md](../ProductionBestPractices/observability.md)

## References

- [AWS Marketplace — Building Agentic Systems: Multi-Agent Architectures (Module 4)](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/multi-agent-architectures) — Workshop slide deck covering the four planes, orchestration patterns, non-determinism math, shared state design, MCP/A2A distinction, security at agent boundaries, and distributed observability
- [Mastering Multi-Agent Systems eBook](https://galileo.ai) — Galileo, 2026. Author: Pratik Bhavsar. Seven benefits, failure modes, decision framework, four architectures, context engineering, LangGraph production example with Galileo observability.
- Arsanjani, A., & Bustos, J.P. (2026). *Agentic Architectural Patterns for Building Multi-Agent Systems*. Packt Publishing. ISBN 978-1-80602-957-0. — Source for Supervisor vs. Swarm comparison and Agent Router pattern.