# Thoughtworks Technology Radar Vol. 34 — Agentic AI Digest

## Overview

The Thoughtworks Technology Radar Volume 34 (April 2026) was assembled at the TAB meeting in Bengaluru, March 2026. It contains 118 blips across four quadrants (Techniques, Platforms, Tools, Languages & Frameworks) and four rings (Adopt, Trial, Assess, Caution). This page extracts and synthesises every entry relevant to **agentic AI, LLM systems, coding agents, context engineering, evaluation, observability, and agent security**.

> **Editorial note — opinionated source.** The Thoughtworks Technology Radar represents the perspective of Thoughtworks' Technology Advisory Board (TAB), a group of 22 senior technologists at a single consultancy. It is one credible signal in the industry, not an authoritative standard. Radar placements reflect Thoughtworks' project experience and technology strategy at a specific point in time and may not align with your organisation's context. Where this page touches existing wiki assessments (e.g., LangGraph, Langfuse), the changes are clearly attributed to this source. Cross-reference with the [Agentic Framework Solutions Radar](../AgenticFrameworks/solutions.md), [Observability Tech Radar](../Observability/tech-radar.md), and vendor-specific documentation for a fuller picture.

---

## Key Themes

### 1. Evaluating technology in an agentic world
The pace of change and semantic diffusion (terms like "agents" and "harness engineering" used inconsistently) make evaluation harder. Many tools are under a month old, maintained by a single contributor using a coding agent. The risk: **codebase cognitive debt** — AI-generated code adopted without the mental models to understand it, making systems harder to debug and evolve.

### 2. Retaining principles, relinquishing patterns
AI forces a return to foundations: pair programming, zero trust architecture, mutation testing, DORA metrics, clean code, and deliberate design. Teams must preserve good engineering principles while discarding patterns that no longer hold in an agentic world.

### 3. Securing permission-hungry agents
The agents worth building need access to everything. Simon Willison's "lethal trifecta" — private data + untrusted content + external action — now describes most useful agents by default. Zero trust, least-privilege, model improvements, and defense in depth are table stakes, but there is no silver bullet. Safe agent systems are composed of pipelines of constrained agents with strong monitoring.

### 4. Putting coding agents on a leash (harness engineering)
Teams invest in **coding agent harnesses**: feedforward controls (Agent Skills, spec-driven development) and feedback controls (compilers, linters, mutation testing, code review integrated into workflows). The goal is self-correction before human review.

---

## Techniques

### Adopt

| Entry | Status | Description |
|---|---|---|
| **Context engineering** | Moved in | Treats the context window as a design surface, not a text box. Techniques mature: prompt caching for static instructions, dynamic retrieval (selective MCP server loading), context graphs for institutional reasoning, and stateful compression via sub-agents. Essential for building resilient enterprise agents. |
| **Curated shared instructions for software teams** | No change | Anchor AI guidance directly into service templates (CLAUDE.md, AGENTS.md, .cursorrules) rather than relying on individual developers to write prompts from scratch. Separates general prompt libraries from repository-specific AI configuration. |
| **Structured output from LLMs** | Moved in | Constraining models to predefined formats (JSON, typed classes) is now a sensible default for programmatic consumption. Use **Instructor** or **Pydantic AI** for stable abstraction and automatic retries across providers. |
| **Zero trust architecture** | No change | Apply "never trust, always verify," identity-based security, and least-privilege access as foundational defaults for any agent deployment. Use SPIFFE for agent identity, OIDC impersonation in place of long-lived static keys. Non-negotiable regardless of the system being built. |
| **DORA metrics** | No change | More important than ever in AI-assisted development. Measuring productivity by lines of code generated is misleading. Rework rate specifically signals blind spots in AI-assisted delivery. |

### Trial

| Entry | Status | Description |
|---|---|---|
| **Agent Skills** | New | Open standard for modularising context: package instructions, scripts, and resources that agents load on demand based on descriptions. Reduces token consumption and mitigates instruction bloat. Backed by plugin marketplaces for versioned distribution. Caution: unreviewed third-party skills introduce supply chain security risks. |
| **Feedback sensors for coding agents** | New | Wire deterministic quality gates — compilers, linters, type checkers, test suites — directly into agentic workflows so failures trigger self-correction before human review. Implement as a reviewer agent or a companion process agents can query. Run during the coding session, before commit. |
| **Mapping code smells to refactoring techniques** | New | Instruct agents to handle specific code issues with defined approaches. Map unique smells to techniques via Agent Skills, slash commands, or AGENTS.md. Especially effective for legacy stacks (.NET Framework 2.0, Java 8) where generic training data falls short. |
| **Mutation testing** | New | Introduces deliberate bugs into source code to verify tests fail when behavior breaks. Critical in AI-assisted development where high coverage percentages can mask logically hollow tests. Tools: **Stryker**, **Pitest**, **cargo-mutants**. |
| **Progressive context disclosure** | New | Give agents a lightweight discovery phase to select what they need rather than front-loading all instructions. Avoids context rot from bloated "DO/DO NOT" rule lists. Works for RAG scenarios and Agent Skill selection. |
| **Sandboxed execution for coding agents** | New | Run agents in isolated environments with restricted file system access, controlled network, and bounded resources. Treat as a sensible default, not optional. Options: Dev Containers (ephemeral), Sprites (stateful+checkpoint), Bubblewrap (Linux-native), sandbox-exec (macOS). |

### Assess

| Entry | Status | Description |
|---|---|---|
| **Agentic reinforcement learning environments** | New | Combine context, tools, and verifiable feedback to train LLM agents on multi-step tasks. See **Agent Lightning** framework. |
| **Architecture drift reduction with LLMs** | New | Combine deterministic structural analysis tools (ArchUnit, Spectral) with LLM evaluation to detect and fix architectural violations as code evolves. |
| **Code intelligence as agentic tooling** | New | Give agents AST-aware tools via Language Server Protocol for accurate symbol-aware refactoring and navigation. Tools: **Serena** (MCP), **OpenCode**, **Claude Code**. |
| **Context graph** | New | Model decisions, policies, and precedents as connected nodes enabling agents to reason across causal chains. Related to **GraphRAG**. |
| **Feedback flywheel** | New | Continuously improve agent harnesses by capturing successes and failures to refine future interactions. Feeds into spec-driven development and curated shared instructions. |
| **LLM evaluation using semantic entropy** | New | Focus on meaning variation rather than surface-level text differences to detect confabulations in QA systems. More robust than string-matching metrics. |
| **Measuring collaboration quality with coding agents** | New | Track metrics like first-pass acceptance rate and iteration cycles rather than purely throughput-focused measures. Part of a broader redefinition of what it means to be a software developer. |
| **MITRE ATLAS** | New | Adversarial Tactics, Techniques, and Common Knowledge for AI/ML systems. Use for threat modeling AI systems. Complements Google SAIF and NIST AI RMF. |
| **Ralph loop** | New | Feed fixed prompts through loops with fresh contexts, letting agents converge toward specifications. Related to team-of-coding-agents patterns. |
| **Role-based contextual isolation in RAG** | New | Tag data chunks with permissions at indexing time to implement zero trust at the retrieval layer. Prevents unauthorized data access through the RAG path. |
| **Skills as executable onboarding documentation** | New | Use skills to combine scripting with LLM semantics for dynamic, context-aware onboarding. Executable specs replace static documentation. |
| **Small language models** | No change | SLMs offer better intelligence per dollar for summarization, coding, and edge deployment. Consider model distillation for specific tasks. |
| **Team of coding agents** | No change | Orchestrate small, role-specific agent teams collaborating on tasks. Tooling support has improved since last Radar. |
| **Temporal fakes** | New | Build stateful simulators maintaining internal state machines to test against realistic system behavior in complex distributed systems. |
| **Toxic flow analysis for AI** | No change | Examine agentic systems to identify the "lethal trifecta" data paths (private data + untrusted input + external action) before exploitation. Tools: **OpenClaw**, **Agent Scan**. |
| **Vision language models for end-to-end document parsing** | New | Use unified VLM approaches to replace multi-stage OCR pipelines. Manage hallucination risks. Compare with **Docling** (structured output approach). |

### Caution

| Entry | Status | Description |
|---|---|---|
| **Agent instruction bloat** | New | Instructions accumulate organically and conflict; prioritize minimal, coherent sets surfaced progressively via Agent Skills. Handwritten specifications outperform LLM-generated ones for precision. |
| **AI-accelerated shadow IT** | No change | Non-engineers increasingly deploy ungoverned code via Claude Code and similar tools. Govern AI-assisted workflow creation through controlled environments and shared catalogs. |
| **Codebase cognitive debt** | New | The gap between implementation and team understanding grows with AI-accelerated change. Track cognitive load intentionally. Related to "intent debt" — misalignment between human project intentions and LLM understanding. |
| **Coding agent swarms** | New | Large swarms amplify individual model biases and face maturity, cost, and coordination challenges. Use only for well-specified tasks. Use only when warranted; balanced composition counteracts predictable model preferences. |
| **Coding throughput as a measure of productivity** | New | Measuring output speed alone encourages poor behavior. Focus on first-pass acceptance rates and delivery outcomes (DORA metrics) instead. |
| **Ignoring durability in agent workflows** | New | Expect failures and recover gracefully. Integrate durable execution into agent frameworks — **LangGraph**, **Temporal**, **Restate**, **Golem**. Design for failure from the start. |
| **MCP by default** | New | Avoid MCP unless governance and multi-tenant benefits justify the protocol complexity. Many use cases can be addressed with simpler CLIs or scripts. Agent Skills are often sufficient. |

---

## Platforms

### Trial

| Entry | Status | Description |
|---|---|---|
| **AG-UI Protocol** | Moved in | Open standard for agentic UI communication. However, the landscape is shifting: newer MCP-based applications package HTML/UI widgets directly within MCP servers. AG-UI remains valid for decoupling front-end UX from orchestration, but assess its role given the consolidation toward MCP. |
| **AWS Bedrock AgentCore** | New | Managed agentic platform (similar to GCP Vertex AI Agent Builder, Azure AI Foundry Agent Service). Recommended approach: decouple orchestration logic into external frameworks like **LangGraph**; use AgentCore runtime for production concerns (session isolation, security, observability). |
| **Graphiti** | Moved in | Temporal knowledge graph engine from Zep. Ingests data as discrete episodes and maintains bi-temporal validity windows, so outdated facts are invalidated rather than overwritten. Benchmarks: 18.5% accuracy improvements, 90% latency reductions vs flat vector stores. Ships a first-class MCP server. Primary backend: Neo4j; lighter alternative: FalkorDB. |
| **Langfuse** | No change | OSS LLM engineering platform: observability, prompt management, evaluations, dataset management. v3 architecture uses ClickHouse + Redis + S3. Both SDKs now built natively on OpenTelemetry. New experiment runner SDK moves it beyond tracing into systematic evaluation workflows. Self-hostable. |
| **SigNoz** | New | OSS, OpenTelemetry-native observability platform with unified logs, metrics, and traces. ClickHouse backend. Reduces observability costs vs Datadog. Supports PromQL and ClickHouse SQL. Strong self-hosted alternative. |
| **Replit** | New | Cloud-native IDE combining editor, runtime, AI assistance, and deployment. Reduces onboarding friction. Effective for prototyping, training, and knowledge-sharing sessions. |

### Assess

| Entry | Status | Description |
|---|---|---|
| **Agent Trace** | New | Open specification (proposed by Cursor) for standardizing AI code attribution. Defines contributor types: human, AI, mixed, unknown. Compatible with Git, Mercurial, Jujutsu. Implementations: **Git AI**, **Cline**, **OpenCode**. Teams adopting coding agents should assess tools implementing this spec. |
| **Databricks Agent Bricks** | New | Prebuilt, auto-optimizing components for common AI patterns (knowledge assistants, data analysts) within Databricks. Declarative approach: define goal + data, framework handles execution. Reduces LLMOps and data curation effort. Suitable if already in the Databricks ecosystem. |
| **MCP Apps** | New | First official MCP extension, co-developed by Anthropic and OpenAI. Lets MCP servers return interactive HTML interfaces (dashboards, forms, visualizations) rendered in sandboxed iframes. Graceful degradation to text. Bidirectional: models observe user actions. Already supported in Claude, ChatGPT, VS Code, Goose. |
| **Neutree** | New | OSS platform for managing and serving LLMs on private infrastructure (model-as-a-service). Unified control plane for model lifecycle, inference serving, compute scheduling across NVIDIA/AMD/Intel. Enterprise capabilities: multi-tenancy, access control, usage accounting. Still relatively new — ecosystem and operational maturity evolving. |
| **Rhesis** | New | OSS testing platform for LLM and agentic applications. Define expected behavior in natural language, generate adversarial test scenarios, evaluate via UI, SDK, or API. Conversation simulator, adversarial testing, OpenTelemetry-based tracing, Docker self-hosting. Pre-production validation for non-deterministic systems. |
| **Sprites** | New | Stateful sandbox environment (from Fly.io) for coding agents. Provides persistent Linux environments with unlimited checkpoint and restore. Goes beyond Git: captures system state including installed dependencies and runtime configuration. Trade-off: non-ephemeral vs. ephemeral (Dev Containers). |

---

## Tools

### Adopt

| Entry | Status | Description |
|---|---|---|
| **Claude Code** | Moved in | Anthropic's agentic coding tool, widely treated as the benchmark for agentic coding capability. Now extends beyond code authoring into specifications, stories, configuration, infrastructure, and markdown-defined business processes. Continues to introduce patterns others follow: skills, subagents, remote control, team workflows. Pair with disciplined harness engineering. |
| **Cursor** | Moved in | Most widely adopted coding agent alongside Claude Code. Features: plan mode, hooks, subagents. Supports Agent Skills for standardizing interactions with complex codebases. Agent Client Protocol enables JetBrains users. Individual agent step inspection and rollback available. |

### Trial

| Entry | Status | Description |
|---|---|---|
| **cargo-mutants** | New | Mutation testing for Rust. Zero-configuration; no changes to source tree required. Injects intentional bugs to verify tests actually catch regressions. Useful feedback loop for teams new to Rust. Manage cost by targeting specific modules in local dev, full suites in CI. |
| **Claude Code plugin marketplace** | New | Git-based distribution for shared commands, prompts, and skills. Enables organizations to host internal team marketplaces on GitHub, delivering AI-driven workflows consistently via CLI. Addresses version drift from manual copy-paste sharing. |
| **Dev Containers** | New | Container-based isolation for coding agents. Restricts agents from host file system and credentials. Ephemeral-by-default. Supported natively by VS Code and Cursor; **DevPod** extends to any editor via SSH. Supply chain security benefit: declarative toolchain reduces exposure to compromised packages. |
| **OpenAI Codex** | New | Standalone agentic coding tool (dedicated macOS app and CLI). Effective for high-velocity drafting and repetitive implementation. Risk: suggests logically sound but functionally outdated library patterns — automated testing and human review are essential. |

### Assess

| Entry | Status | Description |
|---|---|---|
| **Agent Scan** | New | Security scanner for agent ecosystems (by Snyk). Discovers local MCP servers and skills; flags prompt injection, tool poisoning, toxic flows, hardcoded secrets, unsafe credential handling. Caution: scans share component metadata with Snyk APIs — validate operational value before adding to mandatory delivery gates. |
| **Beads** | New | Git-backed (Dolt) issue tracker as persistent memory layer for coding agents. Provides structured task graphs with blocker relationships and branch-friendly coordination for long-horizon multi-session work. New category: agent-native project memory. |
| **Bloom** | New | Anthropic tool for AI safety researchers. Probes LLM behaviors (sycophancy, self-preservation) using dynamically generated test conversations. Companion to **Petri**. Teacher model evaluates student model — use multiple evaluators to reduce bias. |
| **CodeScene** | No change | Behavioral code analysis combining complexity metrics with git history to identify hotspots. Now provides guidance for AI-friendly code design. **CodeHealth** metric flags areas where code is too complex for LLMs to safely refactor without high hallucination risk. Assess as a guardrail for coding agent adoption. |
| **Entire CLI** | New | Captures coding agent sessions (transcripts, prompts, tool calls, files touched, token usage) as searchable metadata on a dedicated Git branch. Supports Claude Code, Gemini CLI, Cursor, OpenCode, GitHub Copilot CLI. Addresses audit gap: what actually happened during a coding session. Checkpoint system enables practical recovery. |
| **Git AI** | New | OSS Git extension tracking AI-generated code with Git Notes. Links every AI-written line to agent, model, and prompts. Checkpoint-based tracking more accurate than line-counting approaches. Implements Agent Trace open standard. |
| **Google Antigravity** | New | Standalone VS Code fork (technology licensed from Windsurf). Centers IDE around multi-agent orchestration via Agent Manager dashboard. Built-in Chromium browser for agent-UI interaction. MCP integration with Google Cloud/Firebase. Still in public preview — assess security posture and enterprise readiness before adopting. |
| **OpenCode** | No change | Prominent OSS terminal-first coding agent. Model flexibility: hosted frontier models, self-hosted endpoints, local models, air-gapped setups. Extension model supports plugins and MCP. **Oh My OpenCode** (community harness) provides batteries-included multi-agent orchestration. |
| **OpenSpec** | New | OSS spec-driven development framework. Workflow: propose → apply → archive. Focuses on spec deltas rather than complete upfront specification — well-suited for brownfield systems. Tool-agnostic and iterative vs heavier alternatives (BMAD, Kiro). |
| **PageIndex** | New | Vectorless, reasoning-based RAG using hierarchical document indexing. LLM traverses table-of-contents index step-by-step. Produces explicit reasoning trace. Best for documents where meaning depends on structure (financial reports, legal documents). Trade-off: LLM inference in retrieval path introduces latency and cost. |
| **Pi** | New | Minimalist OSS terminal coding agent (TypeScript). Bare-bones, highly customizable building block. Easier to adapt than full agents. Project is still early and primarily maintainer-led. |
| **SGLang** | New | High-performance LLM serving framework. RadixAttention reuses KV states across prompts with high prefix overlap. Substantial gains in latency/efficiency for agents using long system prompts or extensive few-shot prompting. Alternative to vLLM for shared-prefix workloads. |
| **Warp** | No change | AI-augmented terminal now supporting full agentic development workflows. Block-based output handles high-throughput text from coding agents better than traditional terminals. Added Oz orchestration platform for cloud agents. Consider **Ghostty** for minimalist approach. |
| **WuppieFuzz** | New | OSS fuzzer for REST APIs using OpenAPI definitions. Generates valid requests, mutates to explore edge cases, uses server-side coverage feedback. Uncovers unhandled exceptions, authorization gaps, sensitive data leaks. Complement to scripted tests. |

### Caution

| Entry | Status | Description |
|---|---|---|
| **OpenClaw** | No change | Hyper-personal AI assistant (self-hosted, persistent, connected to messaging channels). Model is compelling but permission-hungry. Concentrates access to calendar, email, files, and communications in exactly the toxic-flow trifecta pattern. Alternatives with smaller blast radius: NanoClaw, ZeroClaw. |

---

## Languages & Frameworks

### Adopt

| Entry | Status | Description |
|---|---|---|
| **Instructor** | Moved in | Library for structured output from LLMs. Stable abstraction across providers with validation and automatic retries. Pairs with Pydantic AI for production-grade pipelines. |
| **Pydantic AI** | Moved in | Framework for structured output with built-in validation. Architecture favors simple agents communicating through code execution rather than rigid graphs. Built-in Logfire integration for full-stack observability. |

### Trial

| Entry | Status | Description |
|---|---|---|
| **Agent Development Kit (ADK)** | Trial (from Assess) | Google's framework for building and operating AI agents. Ecosystem and operational capabilities have matured since Assess. Stronger observability and runtime features. Still pre-GA in parts, with upgrade friction. Best for teams already in Google's platform. |
| **DeepEval** | Trial | OSS Python framework for LLM/RAG evaluation. Metrics: hallucination detection, answer relevance, faithfulness, contextual precision/recall. Custom metrics support. Now supports complex agentic workflows, multi-turn conversations, tool correctness, step efficiency, MCP server interaction evaluation, and conversation simulation. |
| **Docling** | Trial | OSS Python/TypeScript library for document conversion (PDFs, scanned docs) to JSON/Markdown. Computer vision–based layout understanding. Self-hostable alternative to Azure Document Intelligence, Amazon Textract, Google Document AI. Strong quality-to-cost balance for downstream agentic RAG workflows. Integrates with LangGraph. |
| **LangGraph** | Trial (from Adopt) | *(Moved out of Adopt)* The graph+global-shared-state approach is not always the best for agentic systems. An alternative pattern (used in Pydantic AI) — simple agents communicating through code execution, graph structures added when needed — often produces leaner, more debuggable systems. LangGraph remains powerful but is no longer the default for every agentic system. Still strong for stateful workflows and integrated durable execution. |
| **LangExtract** | Trial | OSS Python library for LLM-based structured extraction from unstructured text with precise source grounding. Key strength: source traceability linking each extracted entity to its location. Better for long-form, unstructured source material than Pydantic AI (which excels at shorter, predictable inputs). |
| **LiteLLM** | Trial | Evolved from LLM provider abstraction into a full AI gateway. Handles retries/failover, load balancing, cost tracking with budget controls, request tracing, access control, API key management, and content filtering. Risk: `drop_params` mode silently discards unsupported parameters — provider-specific capabilities reintroduce coupling. |

### Assess

| Entry | Status | Description |
|---|---|---|
| **Agent Lightning** | New | Agent optimization and training framework. Enables automatic prompt optimization, supervised fine-tuning, and agentic reinforcement learning without changing the underlying agent implementation. Training-Agent Disaggregation: Lightning Server manages training; Lightning Client collects traces for training feedback. Supports AutoGen, CrewAI. |
| **GitHub Spec Kit** | New | Spec-driven development framework for brownfield and greenfield environments. Core concept: the *constitution* (foundational rulebook: project scope, domain context, tech versions, coding standards, repo structure). Lifecycle: spec → plan → tasks → coding → review. Challenge: instruction bloat — extract reusable guidance into skills to keep instructions lean. |
| **Mastra** | No change | TypeScript-native framework for AI applications and agents. Graph-based workflow engine, unified LLM provider access, human-in-the-loop suspension/resumption, RAG and memory primitives, MCP server authoring, built-in evaluation and observability. Alternative to Python-heavy stacks for teams in Node.js/Next.js ecosystems. |
| **Pipecat** | New | OSS framework for real-time voice and multimodal agents. Modular pipeline: STT → LLM → TTS → transport orchestration. Strong engineering foundation, but significant platform engineering work needed for business-critical production. Compare with LiveKit Agents for more integrated production path. |
| **Superpowers** | New | Composable skills workflow for coding agents. Encourages brainstorming before coding, detailed planning before implementation, test-driven development, systematic root-cause debugging, post-implementation code review. Distributed via Claude Code and Cursor plugin marketplaces. |
| **TOON** | New | Token-Oriented Object Notation: human-readable encoding for JSON that reduces token usage when structured data is passed to LLMs. Last-mile optimization for prompt inputs with large, regular datasets. Not a replacement for JSON in APIs/databases. Benchmark against JSON/CSV for your model stack. |
| **Unsloth** | New | OSS framework for LLM fine-tuning and reinforcement learning. Optimizes GPU operations via custom NVIDIA kernels, making fine-tuning possible on consumer GPUs (T4 and above). Supports LoRA, full fine-tuning, multi-GPU, long-context (up to 500K tokens). Models: Llama, Mistral, DeepSeek-R1, Qwen, Gemma. |

---

## Radar Summary Table

### Agentic AI Entries at a Glance

| Entry | Ring | Quadrant | New? | Key Signal |
|---|---|---|---|---|
| Context engineering | **Adopt** | Techniques | No | Foundational architecture for AI systems |
| Structured output from LLMs | **Adopt** | Techniques | No | Sensible default for programmatic LLM consumption |
| Zero trust architecture | **Adopt** | Techniques | No | Non-negotiable for agent deployment |
| Curated shared instructions | **Adopt** | Techniques | No | Anchor AI guidance into service templates |
| Instructor | **Adopt** | Languages & Frameworks | No | Stable LLM output abstraction |
| Pydantic AI | **Adopt** | Languages & Frameworks | No | Simpler agent architecture alternative to LangGraph |
| Claude Code | **Adopt** | Tools | No | Benchmark agentic coding tool |
| Cursor | **Adopt** | Tools | No | Most widely adopted coding agent IDE |
| Agent Skills | **Trial** | Techniques | Yes | Modular context for agents |
| Feedback sensors for coding agents | **Trial** | Techniques | Yes | Self-correction via quality gates |
| Progressive context disclosure | **Trial** | Techniques | Yes | Dynamic context loading |
| Sandboxed execution for coding agents | **Trial** | Techniques | Yes | Default isolation for agent execution |
| Mutation testing | **Trial** | Techniques | Yes | Honest signal for AI-generated test quality |
| AWS Bedrock AgentCore | **Trial** | Platforms | Yes | Managed agentic runtime |
| Graphiti | **Trial** | Platforms | No | Temporal knowledge graph memory |
| Langfuse | **Trial** | Platforms | No | LLM observability + evaluation |
| SigNoz | **Trial** | Platforms | Yes | OSS OpenTelemetry observability |
| ADK | **Trial** | Languages & Frameworks | No (Assess→Trial) | Google agent framework maturing |
| LangGraph | **Trial** (Thoughtworks) | Languages & Frameworks | No | Thoughtworks signal; this wiki retains Adopt based on industry adoption — see [solutions.md](../AgenticFrameworks/solutions.md) |
| LiteLLM | **Trial** | Languages & Frameworks | No | Full AI gateway |
| DeepEval | **Trial** | Languages & Frameworks | No | LLM/agent evaluation framework |
| Docling | **Trial** | Languages & Frameworks | No | Document-to-structured-output |
| Context graph | **Assess** | Techniques | Yes | Reasoning over policies and precedents |
| MITRE ATLAS | **Assess** | Techniques | Yes | AI/ML adversarial threat modeling |
| Role-based contextual isolation in RAG | **Assess** | Techniques | Yes | Zero trust in retrieval |
| Team of coding agents | **Assess** | Techniques | No | Role-specific agent collaboration |
| Small language models | **Assess** | Techniques | No | Cost-efficiency for targeted tasks |
| Agent Trace | **Assess** | Platforms | Yes | AI code attribution standard |
| Rhesis | **Assess** | Platforms | Yes | LLM/agent testing platform |
| Databricks Agent Bricks | **Assess** | Platforms | Yes | Prebuilt agent components in Databricks |
| MCP Apps | **Assess** | Platforms | Yes | HTML UI within MCP servers |
| Neutree | **Assess** | Platforms | Yes | Private LLM hosting platform |
| Sprites | **Assess** | Platforms | Yes | Stateful sandbox for coding agents |
| Claude Code plugin marketplace | **Trial** | Tools | Yes | Governed skill distribution |
| Dev Containers | **Trial** | Tools | Yes | Ephemeral agent sandboxing |
| OpenAI Codex | **Trial** | Tools | Yes | Agentic CLI coding tool |
| Agent Scan | **Assess** | Tools | Yes | Security scanner for MCP/skills |
| Beads | **Assess** | Tools | Yes | Agent-native task memory |
| CodeScene | **Assess** | Tools | No | Code quality guardrail for agents |
| Agent Lightning | **Assess** | Languages & Frameworks | Yes | Agent optimization and fine-tuning |
| Mastra | **Assess** | Languages & Frameworks | No | TypeScript agent framework |
| GitHub Spec Kit | **Assess** | Languages & Frameworks | Yes | Spec-driven development |
| Superpowers | **Assess** | Languages & Frameworks | Yes | Structured coding agent workflow |
| Unsloth | **Assess** | Languages & Frameworks | Yes | Efficient LLM fine-tuning |
| Agent instruction bloat | **Caution** | Techniques | Yes | Instructions degrade with accumulation |
| Coding agent swarms | **Caution** | Techniques | Yes | Maturity, cost, bias amplification risks |
| Ignoring durability in agent workflows | **Caution** | Techniques | Yes | Design for failure from the start |
| MCP by default | **Caution** | Techniques | Yes | Don't default to MCP over simpler CLIs |
| Codebase cognitive debt | **Caution** | Techniques | Yes | AI-accelerated change without understanding |
| OpenClaw | **Caution** | Tools | No | Permission-hungry hyper-personal assistant |
| AG-UI Protocol | **Trial** | Platforms | No | Being supplanted by MCP-embedded UI |

---

## Notable Movement Since Last Radar

| Entry | Movement | Significance |
|---|---|---|
| **Claude Code** | Assess → **Adopt** | Now the industry benchmark for agentic coding |
| **Cursor** | Trial → **Adopt** | Most widely used coding agent IDE |
| **LangGraph** | Adopt → **Trial** (Thoughtworks only) | Graph+shared-state architecture not always best per Thoughtworks; this wiki retains Adopt based on broad industry production adoption |
| **Instructor** | Trial → **Adopt** | Stable abstraction for structured LLM output |
| **Pydantic AI** | Trial → **Adopt** | Simpler agent architecture gaining production trust |
| **Context engineering** | Trial → **Adopt** | Now foundational, not just optimization |
| **ADK** | Assess → **Trial** | Google's agent framework maturing |
| **Graphiti** | Assess → **Trial** | Peer-reviewed benchmarks demonstrate production viability |
| **Docling** | Assess → **Trial** | Strong production-scale extraction results |

---

## See Also

- [Agent Tech Stack References](README.md)
- [Semantic Data Layer Technology Radar](semantic-data-layer-radar.md)
- [Agentic Framework Solutions Tech Radar](../AgenticFrameworks/solutions.md)
- [Context Engineering](../ContextEngineering/README.md)
- [Agent Observability Tech Radar](../Observability/tech-radar.md)
- [Agent Memory Solutions](../AgentMemory/solutions.md)
- [Evaluation Frameworks](../EvaluationFrameworks/Readme.md)
- [Security Frameworks](../SecurityFrameworks/Readme.md)
- [Agent Harness Engineering](../AgentHarness/harness-engineering.md)
- [Production Best Practices — Security](../ProductionBestPractices/security.md)
- [Production Best Practices — Deployment](../ProductionBestPractices/deployment.md)

## References

- [Thoughtworks Technology Radar Vol. 34](https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf) — April 2026 edition (PDF). Primary source for all entries and descriptions on this page.
