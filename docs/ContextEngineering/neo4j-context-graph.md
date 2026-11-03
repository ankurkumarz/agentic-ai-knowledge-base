---
type: Playbook
title: "Building Context Graphs with Neo4j"
description: "Neo4j Labs tools for building graph-native agent memory: the create-context-graph scaffolding CLI and the Neo4j Agent Memory Service (NAMS)."
tags: [context-engineering, neo4j, agentic-ai, knowledge-graph]
timestamp: 2026-11-03T00:00:00Z
---

# Building Context Graphs with Neo4j

## Overview

Neo4j Labs provides two complementary tools for building context graphs in agentic AI systems: **`create-context-graph`**, a CLI scaffolding tool that generates a complete full-stack context graph application in minutes, and the **Neo4j Agent Memory Service (NAMS)**, a managed cloud memory backend that stores, extracts, and compresses agent memory as a structured knowledge graph. Together they implement a three-memory-type architecture (short-term, long-term, reasoning) that distinguishes graph-native agent memory from plain RAG.

---

## `create-context-graph` — CLI Scaffolding Tool

### What It Is

`create-context-graph` is an interactive CLI from Neo4j Labs that generates a domain-specific context graph application (FastAPI backend + Next.js frontend + Neo4j graph) paired with the `neo4j-agent-memory` library and eight agent framework options.

```bash
# Hosted memory (NAMS) — no Neo4j to operate
uvx create-context-graph my-app --domain healthcare --framework strands --nams-api-key sk-nams-...

# Self-hosted Neo4j with full demo fixtures (~85 entities, 180 relationships)
uvx create-context-graph my-app --domain healthcare --framework pydanticai --self-hosted --demo

# Interactive wizard
npx create-context-graph
```

### Three-Memory-Type Architecture

Every generated app implements the same memory model:

| Memory Type | Storage | What It Captures |
|---|---|---|
| Short-term | Conversation messages | Chat history and raw document content |
| Long-term | Neo4j entity graph (POLE+O model) | Persons, Organizations, Locations, Events, Objects — auto-extracted from conversation |
| Reasoning | Decision traces | Full provenance: thought chains, tool calls, causal relationships, approvals |

This is the key distinction from plain RAG: the agent reasons over a structured knowledge graph with full decision traceability, not just retrieved text chunks.

### Memory Backends

| Backend | How to Use | Write Capabilities |
|---|---|---|
| NAMS (hosted) | `--nams-api-key sk-nams-...` from [memory.neo4jlabs.com](https://memory.neo4jlabs.com) | Entity name/type/description only; relationships encoded in description fields |
| Self-hosted Neo4j | `--self-hosted` with bolt URI | Full Cypher, GDS projections, arbitrary relationship types, native edges |

### Supported Agent Frameworks

| Framework | Description |
|---|---|
| Strands | Anthropic tool-use agents (default) |
| PydanticAI | Structured tool definitions with Pydantic models and RunContext |
| Claude Agent SDK | Anthropic agentic loop |
| OpenAI Agents SDK | `@function_tool` decorators with `Runner.run()` |
| LangGraph | Stateful graph-based workflow with `create_react_agent()` |
| CrewAI | Multi-agent crew with role-based tools |
| Google ADK | Gemini agents with `FunctionTool` calling |
| Anthropic Tools | Modular tool registry with Anthropic API agentic loop |

All frameworks share the same FastAPI HTTP layer, Neo4j client, and Next.js frontend — only the agent implementation differs.

### Domain Coverage

27 industry domains with purpose-built ontologies, sample data, agent tools, and demo scenarios:

| Domain | Key Entities | Domain | Key Entities |
|---|---|---|---|
| Healthcare | Patient, Provider, Diagnosis, Treatment | Financial Services | Account, Transaction, Decision, Policy |
| Software Engineering | Repository, Issue, PR, Deployment | GenAI / LLM Ops | Model, Experiment, Prompt, Evaluation |
| Agent Memory | Agent, Conversation, Memory, ToolCall | Cybersecurity | Asset, Vulnerability, Alert, Incident |
| Legal | Case, Matter, Contract, Filing | Education | Student, Instructor, Course, Assessment |

Custom domains can be generated from a plain-English description using `--custom-domain`.

### SaaS Data Connectors

The scaffolded project can import real data from existing tools instead of (or alongside) synthetic demo data:

| Connector | What's Imported |
|---|---|
| GitHub | Issues, PRs, commits, contributors |
| Slack | Channel messages, threads, users |
| Linear | Issues, sprints, decision traces from history |
| Google Workspace | Drive docs, comment threads as decision traces, Calendar events |
| Claude Code | Session history, tool calls, developer preferences (reads `~/.claude/projects/`) |
| Claude AI / ChatGPT | Conversation exports — no API keys required |
| Salesforce, Jira, Notion, Gmail | Records, pages, emails |

The Google Workspace and Linear connectors capture first-class decision traces: Google Docs comment threads (question → deliberation → resolution) and Linear issue history.

### Generated Project Structure

```
my-app/
├── backend/app/
│   ├── agent.py                # AI agent (framework-specific)
│   ├── context_graph_client.py # Neo4j CRUD
│   ├── memory.py               # MemoryIntegration (neo4j-agent-memory v0.4)
│   ├── gds_client.py           # Graph Data Science
│   └── vector_client.py        # Vector search
├── frontend/components/
│   ├── ChatInterface.tsx        # Streaming chat with real-time tool calls
│   ├── ContextGraphView.tsx     # Interactive graph (schema, expand, zoom)
│   └── DecisionTracePanel.tsx   # Reasoning trace viewer
├── cypher/
│   ├── schema.cypher            # Constraints & indexes
│   └── gds_projections.cypher   # GDS algorithm config
├── data/ontology.yaml           # Domain ontology — drives schema, models, tools
└── mcp/                         # Optional MCP server config for Claude Desktop
```

A single `ontology.yaml` drives the entire generated application — schema, Pydantic models, agent tools, and visualization — through the Jinja2 template engine.

### MCP Integration

With `--with-mcp`, the scaffolded project generates an MCP server configuration for Claude Desktop. This creates a dual-interface architecture: the web app and Claude Desktop share one context graph, so entities, conversations, and reasoning traces are accessible from either interface.

### LLM Provider Flexibility

The memory layer uses LiteLLM for provider injection. Defaults:
- **Entity extraction LLM**: `anthropic/claude-haiku-4-5` (or `openai/gpt-4o-mini` if only OpenAI key is set)
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (local, no API key required)

Override with `--memory-llm` and `--memory-embedding` for Bedrock, Vertex AI, Ollama, Groq, Together, and others.

### Quick Start

```bash
# Hosted memory — graph starts empty, agent populates via chat
uvx create-context-graph my-app \
  --domain software-engineering \
  --framework pydanticai \
  --nams-api-key sk-nams-...

cd my-app
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env
make install && make start

# Self-hosted — pre-populated demo data
uvx create-context-graph my-app \
  --domain software-engineering \
  --framework pydanticai \
  --self-hosted --demo

cd my-app
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env
make install && make docker-up && make seed && make start
```

Open `http://localhost:3000` for the chat + graph UI, `http://localhost:8000/docs` for the API.

---

## Neo4j Agent Memory Service (NAMS)

### What It Is

NAMS is the managed cloud memory backend that `create-context-graph` defaults to. It is also usable standalone via REST or MCP from any agent framework. Call the API with a message — NAMS handles entity extraction, embedding, deduplication, and conversation compression asynchronously. The agent's code never manages any of that pipeline.

```bash
# Connect as an MCP server (Claude Code / Claude Desktop)
claude mcp add --transport http --scope project nams \
  https://memory.neo4jlabs.com/mcp \
  --header "Authorization: Bearer ${NAMS_API_KEY}"

# REST API
# 1. Create a conversation
curl -X POST https://memory.neo4jlabs.com/v1/conversations \
  -H "Authorization: Bearer $NAMS_API_KEY" \
  -d '{"userId": "user-1"}'

# 2. Store a message — extraction & embedding fire automatically
curl -X POST https://memory.neo4jlabs.com/v1/conversations/{id}/messages \
  -H "Authorization: Bearer $NAMS_API_KEY" \
  -d '{"role": "user", "content": "John works at Acme Corp in Denver"}'
# → extracts: John (person), Acme Corp (organization), Denver (location)

# 3. Retrieve layered context for prompt injection
curl https://memory.neo4jlabs.com/v1/conversations/{id}/context \
  -H "Authorization: Bearer $NAMS_API_KEY"
# → active reflection + recent observations + recent raw messages
```

### Three Memory Types in One Graph

| Type | Nodes | Description |
|---|---|---|
| Short-term | Conversation, Message (green) | Raw conversation history |
| Long-term | Entities via POLE+O model (orange) | Persons, Organizations, Locations, Events, Objects — auto-extracted and deduplicated |
| Reasoning | Agent steps, tool calls (purple) | Full provenance: thought chains, tool calls, causal links |

All three types live in a single Neo4j graph, enabling cross-type traversal: from a tool call → the entity it touched → the message that first mentioned it. Vector stores give recall; the graph gives understanding.

### Background Compression Pipeline

A continuous worker rolls raw messages into *observations* (2–4 sentence summaries of a message window) and synthesizes those into an *active reflection* (best current summary of the entire conversation). The `/context` endpoint returns all three tiers ready to drop into a prompt — no manual orchestration required.

```
raw messages → observations → active reflection
     ↑                              ↓
  stored via API          returned by /context
```

### NAMS Console

| Tab | Purpose |
|---|---|
| Dashboard | Service health, entity count, queue lag across 7 async workers |
| Memory Browser | Force-directed interactive graph, colored by entity type |
| HITL Resolution | Human review queue for ambiguous entity deduplication |
| Entity Explorer | Searchable/sortable table; hybrid vector + keyword search |
| Observations | Timeline of compression artifacts (observations → active reflection) |
| Query Console | Read-only Cypher editor against the live workspace graph |
| Ontologies | Domain schema management; clone templates or import RDF/TTL |
| Database | Bolt credentials, Neo4j Browser, full Cypher export/import, bring-your-own-database |

### Entity Resolution (HITL)

Newly extracted entities run through a type-strict cascade:
1. Exact match on normalized names and aliases
2. Fuzzy matching (Levenshtein, Jaro-Winkler, token-sort)
3. Semantic match on embeddings

High-confidence matches auto-merge. Ambiguous pairs are flagged as `SAME_AS` edges with `pending` status and surfaced in the HITL review queue for human confirmation, rejection, or bulk approval.

### Ontology Management

Workspaces start with the default POLE+O ontology. Options:
- Clone a domain template (healthcare, legal, financial-services, cybersecurity, retail, software-engineering, etc.)
- Import an existing schema (RDF/TTL)

Three validation modes govern unknown entity types:

| Mode | Behaviour |
|---|---|
| Permissive (default) | Accept unknown types; queue for review |
| Review | Accept but flag for approval |
| Strict | Reject with HTTP 422; suggest nearest declared type |

Every ontology edit produces an immutable revision with an append-only audit trail.

### API Keys and Access Scopes

Keys are scoped (`memory:read`, `entities:write`, `reasoning:write`, `ontology:write`) — an agent can be granted exactly the permissions it needs. Agent keys and admin keys are separate; admin keys allow workspace creation and management, rotating on a 90-day expiry.

### Platform Integrations

NAMS is designed to plug into existing agent platforms:
- **Salesforce Agentforce** — live
- **GCP Gemini Enterprise, AWS AgentCore, Microsoft Foundry** — in progress

**Get started:** sign up at [memory.neo4jlabs.com](https://memory.neo4jlabs.com). Library docs: [neo4j.com/labs/agent-memory/](https://neo4j.com/labs/agent-memory/).

---

## See Also

- [Context Graph](./context-graph.md) — formal definition of Context Graphs, CGR³ reasoning paradigm, and business case for decision traces
- [Context Engineering Strategies](./strategies.md) — offload, reduce, retrieve, isolate, cache
- [Agent Memory Management](../AgentMemory/README.md) — memory tiers, LTM strategies, and solutions
- [Knowledge Graph Memory](../AgentMemory/knowledge-graph-memory.md) — graph-based memory patterns and GraphRAG
- [Production Best Practices: State & Memory](../ProductionBestPractices/state-memory.md) — durable state patterns in production
- [Multi-Agent Systems](../Architecture/multi-agent-system.md) — orchestration layers where decision traces are generated
- [MCP Standard](../Standards/mcp.md) — Model Context Protocol used by NAMS MCP server

## References

- [create-context-graph (GitHub)](https://github.com/neo4j-labs/create-context-graph) — Neo4j Labs CLI scaffolding tool for domain-specific context graph apps with 8 agent frameworks and 27 industry domains
- [A Tour of the Neo4j Agent Memory Service (NAMS)](https://neo4j.com/blog/genai/a-tour-of-the-neo4j-agent-memory-service-nams/) — Neo4j walkthrough of NAMS: three-memory-type architecture, console tabs, HITL resolution, ontology management, and platform integrations
- [Neo4j Agent Memory Docs](https://neo4j.com/labs/agent-memory/) — official library documentation
- [graph-memory-system-one-demo (GitHub)](https://github.com/zach-blumenfeld/graph-memory-system-one-demo) — Zach Blumenfeld: demo showing how to distill agent knowledge captured in graph memory into System One workflows; includes a product-marketing agent learning email-blast procedures from Notion SOPs, and a business-loan assessment demo with decision traces filed back into the graph
- [AIP — Agent Instruction Protocol (GitHub)](https://github.com/zach-blumenfeld/aip) — open protocol for governed agent workflows: distills domain know-how (runbooks, SOPs, decision logs, wiki pages) into schema-validated YAML execution graphs that any agent, model, or orchestration stack can run step-by-step with explicit control flow and server-side run recording
- [AIP: A Graph Representation for Learning and Governing Agent Skills (arXiv:2606.04781)](https://arxiv.org/abs/2606.04781) — Blumenfeld (2026): compiling free-form agent skills into AIP's directed execution graph raised Claude Sonnet's mean task reward from 0.60 to 0.71 and pass rate from 53% to 67% across 27 real tasks on SkillsBench (p = 0.011); graph structure also enables precise failure diagnosis, schema-validated skill governance, and a natural action space for RL over skills
