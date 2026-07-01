# Claude Managed Agents

## Overview

Claude Managed Agents is Anthropic's hosted agent execution platform — a pre-built, configurable agent harness that runs in managed infrastructure. Rather than building a custom agent loop, tool execution layer, and runtime, developers get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. The platform includes built-in prompt caching, context compaction, and other performance optimizations.

Announced through April–May 2026, three capabilities were added: **Memory** (public beta, April 23), **Dreaming** (research preview, May 6), and **Outcomes + Multiagent Orchestration** (public beta, May 6).

**Base requirement**: All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets this automatically.

## Core Concepts

| Concept | Description |
|---|---|
| **Agent** | Model, system prompt, tools, MCP servers, and skills — defined once, reused by ID |
| **Environment** | Where sessions run: Anthropic-managed cloud container or self-hosted sandbox |
| **Session** | A running agent instance performing a specific task, generating an event stream |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status) |

## Feature 1 — Memory (Public Beta)

### What It Is

Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context. Each session starts fresh by default; without memory, all state is lost when a session ends.

A **memory store** is a workspace-scoped collection of text documents. When attached to a session, it is **mounted as a directory** inside the container at `/mnt/memory/`. The agent reads and writes it with the same file tools it uses for the rest of the filesystem (bash, grep, etc.). A note describing each mount (path, access mode, description, instructions) is automatically added to the system prompt.

Every mutation creates an immutable **memory version** (`memver_...`), giving a full audit trail and point-in-time recovery. Versions are retained for 30 days (recent versions always kept regardless of age).

### Key Constraints

| Limit | Value |
|---|---|
| Max memory stores per session | 8 |
| Max individual memory file size | 100 kB (~25k tokens) |
| Max per-store instructions length | 4,096 characters |
| Memory version retention | 30 days (recent always kept) |

### API

**Create a store** — `POST /v1/memory_stores`

```python
store = client.beta.memory_stores.create(
    name="User Preferences",
    description="Per-user preferences and project context.",
)
# store.id = "memstore_01Hx..."
```

**Seed before first session** (optional):

```python
client.beta.memory_stores.memories.create(
    store.id,
    path="/formatting_standards.md",
    content="All reports use GAAP formatting. Dates are ISO-8601...",
)
```

**Attach to a session** — specify `access` and per-store `instructions`:

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[{
        "type": "memory_store",
        "memory_store_id": store.id,
        "access": "read_write",  # or "read_only"
        "instructions": "User preferences and project context. Check before starting any task.",
    }],
)
```

**Safe content edits** — use optimistic concurrency via `content_sha256` to avoid clobbering concurrent writes:

```python
client.beta.memory_stores.memories.update(
    memory_id=mem.id,
    memory_store_id=store.id,
    content="CORRECTED: Always use 2-space indentation.",
    precondition={"type": "content_sha256", "content_sha256": mem.content_sha256},
)
```

**Redact a version** (compliance — remove PII/secrets from history):

```python
client.beta.memory_stores.memory_versions.redact(version_id, memory_store_id=store.id)
```

### Memory Structure Best Practice

Structure memory as many small focused files, not a few large ones (100 kB cap per file). Use directory paths to organize by topic:

```
/preferences/formatting.md
/preferences/communication-style.md
/project/architecture-decisions.md
/project/known-issues.md
```

### Security Warning

Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user prompts, fetched web content, third-party tool output), a prompt injection could write malicious content into the store — which later sessions then read as trusted memory. **Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.**

---

## Feature 2 — Dreaming (Research Preview)

### What It Is

Dreaming is an asynchronous memory-curation job that runs **between** sessions, not during active task execution. It takes a memory store plus past session transcripts as input, and produces a **new, reorganized memory store** as output — the input is never modified (non-destructive by design).

The analogy is hippocampal memory consolidation: instead of storing raw interactions indefinitely, dreaming reviews what was accumulated, deduplicates, removes contradictions and outdated facts, and promotes recurring patterns (repeated mistakes, team preferences) into clean structured memories.

**Additional beta header required**: `dreaming-2026-04-21`

### What Dreaming Does

- Merges duplicate information into existing topic files (not new near-duplicates)
- Removes or replaces stale and contradicted entries with the latest value
- Surfaces new insights and recurring patterns: preferred workflows, repeated mistakes, team conventions
- Converts relative dates to absolute dates for temporal durability
- Produces a clean indexed topic-file structure

### API

**Create a dream** — `POST /v1/dreams`

```python
dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-4-7",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
# dream.id = "drm_01..."
# dream.status = "pending"
```

**Track progress** (poll):

```python
while dream.status in ("pending", "running"):
    time.sleep(10)
    dream = client.beta.dreams.retrieve(dream.id)
```

**Use the output** — the output is an ordinary memory store; review, then attach to future sessions:

```python
output_store_id = next(
    o.memory_store_id for o in dream.outputs if o.type == "memory_store"
)
session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    resources=[{"type": "memory_store", "memory_store_id": output_store_id}],
)
```

**Cancel / archive** — standard lifecycle management available.

### Dream Lifecycle

| Status | Meaning |
|---|---|
| `pending` | Created and queued |
| `running` | Pipeline processing; `usage` updates in real time |
| `completed` | Output memory store ready |
| `failed` | Terminated with error; output store contains partial results |
| `canceled` | Manually canceled; output store contains partial results |

While running, `dream.session_id` points at the underlying session executing the pipeline — you can stream that session's events to watch the dream read and write in real time.

### Limits and Billing

| Limit | Value |
|---|---|
| Sessions per dream | 100 (max) |
| `instructions` length | 4,096 characters |
| Supported models | `claude-opus-4-7`, `claude-sonnet-4-6` |
| Typical runtime | Minutes to tens of minutes |
| Billing | Standard token rates; scales linearly with session count and length |

### Error Types

| `error.type` | When |
|---|---|
| `timeout` | Exceeded runtime budget |
| `internal_error` | Unclassified pipeline failure |
| `memory_store_org_limit_exceeded` | Org hit memory-store cap during provisioning |
| `input_memory_store_too_large` | Input store exceeds pipeline size limit |
| `input_memory_store_unavailable` | Input store archived/deleted after dream was created |
| `input_session_unavailable` | An input session was archived/deleted after dream was created |

---

## Feature 3 — Outcomes (Public Beta)

### What It Is

Outcomes elevates a session from a conversation to goal-directed work. You define what "done" looks like via a plain-language rubric. The harness automatically provisions a separate **grader** that evaluates the agent's output against the rubric, returns per-criterion feedback, and the agent iterates until the outcome is satisfied or `max_iterations` is reached.

The grader runs in a **separate context window**, isolated from the main agent's reasoning — preventing the agent's implementation choices from contaminating the evaluation (same principle as LLM-as-judge in evaluation frameworks).

### Rubric Design

A rubric is a markdown document with explicit, gradeable criteria. Each criterion is scored independently, so vague criteria produce noisy evaluations.

```markdown
# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward

## Discount Rate
- WACC is calculated with stated assumptions
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Output Quality
- All figures in a single .xlsx file with clearly labeled sheets
- Sensitivity analysis on WACC and terminal growth rate included
```

Tip from Anthropic: give Claude a known-good example artifact and ask it to analyze what makes it good, then turn that into a rubric — often produces better criteria than writing from scratch.

Rubrics can be passed inline as text or uploaded once via the Files API and reused across sessions by file ID.

### API

**Define an outcome** — send `user.define_outcome` event after session creation:

```python
session = client.beta.sessions.create(agent=agent.id, environment_id=environment.id)

client.beta.sessions.events.send(
    session_id=session.id,
    events=[{
        "type": "user.define_outcome",
        "description": "Build a DCF model for Costco in .xlsx",
        "rubric": {"type": "text", "content": RUBRIC},
        # or: "rubric": {"type": "file", "file_id": rubric.id},
        "max_iterations": 5,  # optional; default 3, max 20
    }],
)
```

Agent starts working immediately on receipt; no additional message required.

### Outcome Events

| Event | Description |
|---|---|
| `span.outcome_evaluation_start` | Grader starts evaluating an iteration. `iteration` field is 0-indexed. |
| `span.outcome_evaluation_ongoing` | Heartbeat while grader runs; internal reasoning is opaque |
| `span.outcome_evaluation_end` | Grader finished; `result` indicates next step |

**`span.outcome_evaluation_end` results:**

| `result` | What Happens |
|---|---|
| `satisfied` | Session transitions to `idle` |
| `needs_revision` | Agent starts a new iteration cycle |
| `max_iterations_reached` | Agent may do one final revision; session transitions to `idle` |
| `failed` | Rubric fundamentally doesn't match the task (e.g., contradictory description and rubric); session goes `idle` |
| `interrupted` | `user.interrupt` received after evaluation started |

**Example evaluation end event:**

```json
{
  "type": "span.outcome_evaluation_end",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated...",
  "iteration": 0,
  "usage": {"input_tokens": 2400, "output_tokens": 350}
}
```

### Retrieving Deliverables

The agent writes output files to `/mnt/session/outputs/` inside the container. Retrieve via the Files API scoped to the session:

```python
files = client.beta.files.list(scope_id=session.id)
content = client.beta.files.download(files.data[0].id)
content.write_to_file("/tmp/output.xlsx")
```

### Chaining Outcomes

Only one outcome is active at a time. After the terminal event of one outcome, send a new `user.define_outcome` to chain another. Session retains history of prior outcomes.

---

## Feature 4 — Multiagent Orchestration (Public Beta)

### What It Is

Multiagent orchestration lets one **coordinator** agent break complex work into pieces and delegate each piece to **specialist agents**, which run in parallel with their own isolated context. The coordinator synthesizes results when specialists complete.

### Architecture

- All agents share the same **container, filesystem, and vault credentials** (shared state)
- Each agent runs in its own **session thread** — a context-isolated event stream with its own conversation history
- Threads are **persistent**: the coordinator can send follow-ups to agents it called earlier
- Each agent uses its own configuration (model, system prompt, tools, MCP servers, skills) — context is NOT shared across agents
- MCP servers are **agent-scoped**; vault credentials are **session-scoped** (apply across all threads)

### Configuration

Set `multiagent.type = "coordinator"` on the coordinator agent with a roster of specialists:

```python
coordinator = client.beta.agents.create(
    name="Engineering Lead",
    model="claude-opus-4-7",
    system="Coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.",
    tools=[{"type": "agent_toolset_20260401"}],
    multiagent={
        "type": "coordinator",
        "agents": [
            {"type": "agent", "id": reviewer_agent.id},
            {"type": "agent", "id": test_writer_agent.id},
            {"type": "self"},  # coordinator can also spawn copies of itself
        ],
    },
)
```

Roster entries:
- `{"type": "agent", "id": agent_id}` — reference by ID (pins latest version)
- `{"type": "agent", "id": agent_id, "version": v}` — pin specific version
- `{"type": "self"}` — coordinator spawns copies of itself

### Limits

| Limit | Value |
|---|---|
| Max concurrent threads | 25 |
| Max unique agents in roster | 20 |
| Max delegation depth | 1 level (coordinator → specialists; specialists cannot sub-delegate) |

The coordinator can call **multiple copies** of the same agent in its roster (each creates a new thread).

### Delegation Patterns

| Pattern | Description |
|---|---|
| **Parallelization** | Fan out independent subtasks simultaneously (search multiple sources, analyze separate files), then synthesize |
| **Specialization** | Route to agents with domain-focused prompts and tools (security agent, documentation agent) |
| **Escalation** | Consult a more capable model for specific complex subtasks |

### Thread Events (Primary Stream)

| Event | Description |
|---|---|
| `session.thread_created` | Thread spawned; includes `session_thread_id` and `agent_name` |
| `session.thread_status_running` | Thread started activity |
| `session.thread_status_idle` | Agent awaiting input; includes `stop_reason` |
| `session.thread_status_terminated` | Thread archived or terminal error |
| `agent.thread_message_received` | Specialist delivered result to coordinator |
| `agent.thread_message_sent` | Coordinator sent follow-up to specialist |

Tool permission requests (`requires_action`) from subagents are cross-posted to the primary thread. Respond with `user.tool_confirmation` (with `tool_use_id`) — the server routes to the correct thread automatically.

---

## Self-Improvement Loop (Combined)

The combination of Memory + Dreaming + Outcomes creates a compound self-improvement loop:

```
Session executes task
  ↓
Outcomes grader evaluates against rubric (separate context)
  → needs_revision? Agent iterates
  → satisfied? Session completes
  ↓
Agent writes observations, preferences, patterns to memory store during session
  ↓
[Between sessions] Dreaming job runs:
  - Ingests episodic logs from past sessions + current memory store
  - Deduplicates, removes stale facts, promotes recurring patterns
  - Produces new consolidated memory store
  ↓
Next session starts with enriched, curated memory
  → Agent has inherited behavioral improvements without model retraining
```

This is Anthropic's production implementation of the Reflection/Consolidation LTM strategy from the CoALA taxonomy. No model retraining or weight updates occur — improvement is entirely through memory curation.

**Production evidence**: Harvey (legal AI startup, pilot customer) reported approximately **6× jump in task completion rates** using this combined loop for legal-drafting workflows (May 2026).

---

## Availability

| Feature | Status | Beta Header |
|---|---|---|
| Memory | Public beta | `managed-agents-2026-04-01` |
| Outcomes | Public beta | `managed-agents-2026-04-01` |
| Multiagent Orchestration | Public beta | `managed-agents-2026-04-01` |
| Dreaming | Research preview (request required) | `managed-agents-2026-04-01,dreaming-2026-04-21` |

Note: Claude Managed Agents is stateful by design — not eligible for Zero Data Retention (ZDR) or HIPAA BAA coverage. Sessions, files, and memory stores can be deleted via API.

---

## Rate Limits

| Operation | Limit |
|---|---|
| Create endpoints (agents, sessions, environments, etc.) | 300 requests/minute |
| Read endpoints (retrieve, list, stream, etc.) | 600 requests/minute |

---

## Best Practices

| Challenge | Description | Recommendation |
|---|---|---|
| Rubric vagueness | Vague criteria produce noisy grading | Write explicit, measurable criteria: "The CSV contains a price column with numeric values" not "The data looks good." Use a known-good artifact to generate rubrics. |
| Memory file size | Large monolithic memory files hit 100 kB cap and reduce relevance | Structure memory as many small topic-focused files under `/mnt/memory/` with a directory hierarchy |
| Prompt injection via memory | `read_write` store processes untrusted input → malicious memory written | Use `read_only` for reference stores; isolate stores that process user-supplied content |
| Dreaming data quality | Poorly organized memory leads to poor consolidation output | Structure initial memory by topic before running dreams; provide `instructions` to focus dreaming scope |
| Multiagent token budget | Parallel specialists can inflate total cost | Set per-specialist model to the smallest model that fits the task (e.g., Haiku for research, Opus for reasoning); limit roster size |
| Grader context contamination | Grader seeing agent reasoning defeats isolation | Never pass agent scratchpad or chain-of-thought to the grader — this is enforced by the separate context window |
| Concurrent memory writes | Multiple agents with shared `read_write` store create race conditions | Use `content_sha256` preconditions on updates; consider one store per agent thread |
| Max iterations tuning | Too few = premature termination; too many = runaway cost | Start with default (3), increase only for tasks with known high revision cycles; monitor `iteration` in events |

---

## See Also

- [Agent Memory Management](../AgentMemory/README.md)
- [Memory Solutions & Technology Radar](../AgentMemory/solutions.md)
- [Long-Term Memory Strategies](../AgentMemory/ltm-strategies.md)
- [Self-Learning Agents Reference Architecture](../ReferenceArchitecture/self-learning-agents.md)
- [Production Best Practices — State & Memory](../ProductionBestPractices/state-memory.md)
- [Anthropic Overview](../AllThingsAnthropic/README.md)
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md)
- [Multi-Agent System Architecture](../Architecture/multi-agent-system.md)

## References

- [New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](https://claude.com/blog/new-in-claude-managed-agents) — Anthropic official blog, May 2026
- [Memory and dreaming for self-learning agents](https://youtu.be/RtywqDFBYnQ) — YouTube video, Anthropic, 2026
- [Using agent memory — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/memory) — Official Memory documentation
- [Dreams — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/dreams) — Official Dreaming documentation
- [Define outcomes — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/define-outcomes) — Official Outcomes documentation
- [Multiagent sessions — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/multi-agent) — Official Multiagent documentation
- [Claude Managed Agents overview — Claude API Docs](https://platform.claude.com/docs/en/managed-agents/overview) — Platform overview
