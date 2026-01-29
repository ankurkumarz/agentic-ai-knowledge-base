# OpenAI Agent Design Patterns

## Overview

Agents design patterns in this guide focus on how to structure reasoning, tools, orchestration, and safety guardrails for reliable, production-grade systems. These patterns are derived from OpenAI's practical guide to building agents and provide a comprehensive framework for developing robust agentic AI systems.

![OpenAI Agentic Design Patterns](../assets/images/architecture-openai-agentic-patterns.jpeg)
*OpenAI's comprehensive agentic design patterns overview*

## Core Agent Structure

### Three-Part Foundation
Every agent system is built on three minimal building blocks:

- **Model (Reasoning)**: The core AI model that processes information and makes decisions
- **Tools (Actions/Data)**: The capabilities that allow the agent to interact with external systems and data
- **Instructions (Behavior/Guardrails)**: The rules and guidelines that govern agent behavior and ensure safety

### Single Orchestration Loop
Implement a single orchestration loop ("run") with clear exit conditions:
- Final tool output completion
- Direct user response requirement
- Error state handling
- Maximum turns reached

## Model and Tool Patterns

### Progressive Model Selection
- **Start with capability**: Begin with the most capable models for all steps
- **Optimize progressively**: Swap in smaller models for simpler sub-tasks to balance cost, latency, and accuracy
- **Maintain quality**: Ensure accuracy is preserved when optimizing for performance

### Standardized Tool Definitions
Organize tools into three categories with reusable, well-documented interfaces:

- **Data Tools**: Information retrieval and processing capabilities
- **Action Tools**: External system interactions and modifications
- **Orchestration Tools**: Workflow management and coordination

**Best Practice**: Use more tools in one agent before splitting into multiple agents to maintain simplicity and coherence.

## Instruction and Prompt Patterns

### SOP-Derived Routines
- **Source from existing processes**: Derive routines from existing Standard Operating Procedures (SOPs) and policies
- **Convert to instructions**: Transform policies into numbered, unambiguous instructions for the agent
- **Maintain clarity**: Ensure instructions are specific and actionable

### Template-Based Prompts
- **Use variables**: Implement prompt templates with variables (e.g., user profile, policies) instead of many separate prompts
- **Define explicitly**: Clearly specify actions, edge cases, and conditional branches
- **Maintain consistency**: Ensure uniform behavior across different scenarios

## Orchestration Patterns

### Single-Agent Pattern
**Recommended starting point** for most workflows:
- One agent with many tools handling workflows via a loop
- Preferred for simplicity and easier evaluations
- Suitable for most use cases before considering multi-agent approaches

### Multi-Agent Patterns

#### Manager Pattern
- **Central coordination**: One "manager" agent orchestrates specialized agents as tools
- **Unified interface**: Maintains a single user interface for consistency
- **Result synthesis**: Combines outputs from multiple specialized agents

#### Decentralized Pattern
- **Peer coordination**: Agents hand off control via "handoff tools"
- **Domain specialization**: Useful for triage and domain-specialized flows
- **No central controller**: Eliminates single points of failure

## Agent Splitting Patterns

### When to Split Agents
Split into multiple agents when:
- Prompts become too complex with many conditionals
- Tools overlap or confuse selection
- A single agent cannot reliably follow instructions
- Domain expertise requires specialized knowledge

### Domain-Based Agent Architecture
- **Functional domains**: Create agents for specific functions (e.g., refund, research, writing)
- **Business domains**: Organize by business areas (e.g., sales, technical support, order management)
- **Triage coordination**: Use a triage or manager agent to route traffic appropriately

## Guardrail and Safety Patterns

### Layered Guardrails
Implement multiple layers of protection:

1. **Relevance Classifier**: Ensures responses stay on-topic
2. **Safety Classifier**: Identifies potentially harmful content
3. **PII Filtering**: Removes personally identifiable information
4. **Moderation**: Content appropriateness checking
5. **Rules-Based Protections**: Regex patterns, blocklists, length limits
6. **Output Validation**: Ensures response quality and format

### First-Class Guardrail Components
- **Optimistic execution**: Run guardrails concurrently with main processing
- **Exception handling**: Raise exceptions (tripwires) for policy violations
- **Escalation triggers**: Activate alternate flows when guardrails are triggered
- **Performance optimization**: Minimize latency impact while maintaining safety

## Human-in-the-Loop Patterns

### Intervention Triggers
Implement human intervention for:
- **Repeated failures**: Beyond defined thresholds
- **High-risk actions**: Refunds, cancellations, payments requiring approval
- **Low confidence**: When agent uncertainty exceeds acceptable levels
- **Policy violations**: When guardrails detect potential issues

### Escalation Paths
- **Graceful handoff**: Enable smooth transitions to human operators
- **Context preservation**: Maintain conversation history and state
- **Return mechanisms**: Allow agents to resume after human intervention
- **User notification**: Keep users informed of escalation status

## Implementation Best Practices

### Development Approach
1. **Start simple**: Begin with single-agent patterns
2. **Iterate based on needs**: Add complexity only when necessary
3. **Measure performance**: Use clear metrics for evaluation
4. **Test thoroughly**: Validate all patterns and edge cases

### Production Considerations
- **Monitoring**: Implement comprehensive logging and metrics
- **Scalability**: Design for growth and increased load
- **Reliability**: Build in redundancy and error recovery
- **Security**: Apply defense-in-depth principles

### Evaluation Framework
- **Functional testing**: Verify core capabilities work as expected
- **Safety testing**: Validate guardrails and safety measures
- **Performance testing**: Measure latency, throughput, and resource usage
- **User experience**: Assess interaction quality and satisfaction

## Resources

- **Source**: [A Practical Guide to Building Agents (OpenAI)](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/1524861/79a8a29e-badc-4d70-b2e2-c12369e0241f/a-practical-guide-to-building-agents.pdf)
- **OpenAI Documentation**: Official agent development resources
- **Community Examples**: Real-world implementations and case studies
- **Best Practices**: Ongoing updates and refinements to patterns
