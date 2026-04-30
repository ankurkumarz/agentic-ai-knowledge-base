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

## See Also
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