# Agent Client Protocol (ACP)

## Overview

The **Agent Client Protocol (ACP)** is an open standard, originally published by Zed Industries in August 2025, that standardizes communication between *code editors* (interactive programs for viewing and editing source code) and *coding agents* (programs that use generative AI to autonomously modify code). Before ACP, each editor needed a bespoke integration for every agent it wanted to support, forcing the ecosystem to repeatedly reinvent the same plumbing. ACP replaces those one-off integrations with a single interface: any ACP-compliant agent can run inside any ACP-compliant editor without custom glue code.

*Source: [Agent Client Protocol](https://agentclientprotocol.com/), [agentclientprotocol/agent-client-protocol on GitHub](https://github.com/zed-industries/agent-client-protocol)*

## Key Concepts / Architecture

### Transport and Message Format

- **Transport**: JSON-RPC 2.0 messages exchanged over `stdin`/`stdout` (line-delimited JSON), typically with the editor spawning the agent as a subprocess.
- **Message types**: requests, responses, and notifications, following standard JSON-RPC semantics.
- **Roles**: the **Client** (the code editor/IDE) and the **Agent** (the coding-agent process). The Client is always the one that launches and drives the connection; either side can subsequently send requests and notifications once a session is established.
- **Versioning**: wire compatibility is governed by a negotiated `protocolVersion` exchanged during initialization, not by SDK or crate release numbers. The current stable wire protocol is version 1, with schema artifacts published per version (`schema/v1`, `schema/v2`, etc.) and as JSON Schema files attached to GitHub releases.

### Session Lifecycle

1. **`initialize`** — sent by the Client on startup to negotiate the `protocolVersion` and exchange capability declarations (e.g., the Client's `fileSystem` and `terminal` support; the Agent's `modelSelector` and `loadSession` support).
2. **`session/new`** — creates a new session for an interaction (a single editing/conversation context).
3. **`session/load`** — resumes a previously created session, if the Agent supports it; the Agent replays the full conversation history back to the Client as a sequence of `session/update` notifications.
4. **`session/prompt`** — the Client forwards a user turn (prompt) to the Agent within a session.
5. **`session/update`** — notifications the Agent streams back to the Client during processing, carrying incremental output, tool-call status, and reasoning/"thought" content for real-time display.

### Content and Tool Calls

- **Content Blocks**: Markdown-first rich text, with support for images, audio, and resource references.
- **Tool calls** are reported to the Client via `session/update` notifications so the editor can render real-time progress. Tool calls are categorized as: `read`, `edit`, `delete`, `move`, `search`, `execute`, `think`, and `fetch`.
- **Permission requests**: an Agent that wants to perform a sensitive operation (e.g., editing a file, running a command) can request authorization from the user through the Client via `session/request_permission`, rather than auto-approving itself — keeping the human in the loop for risky actions.
- **Client-provided capabilities**: Clients can expose primitives the Agent calls into, including filesystem access (`fs/read_text_file`, `fs/write_text_file`) and terminal control (`terminal/create`, `terminal/output`, `terminal/wait_for_exit`, `terminal/kill`, `terminal/release`). This keeps file and command execution inside the user's editor-controlled environment rather than requiring the Agent to manage its own sandbox, with the editor acting as the gatekeeper for permissions.

## Relationship to MCP

ACP and the [Model Context Protocol (MCP)](./mcp.md) address different layers of the agentic stack and are complementary rather than competing:

| Aspect | ACP | MCP |
|---|---|---|
| **Primary relationship** | Editor (Client) ↔ Coding agent | LLM application (Host) ↔ Tool/data server |
| **What it standardizes** | How an editor launches, drives, and renders a coding agent's session (prompts, streaming updates, tool-call display, permissions, file/terminal access) | How an LLM application discovers and calls external tools/resources |
| **Direction of control** | Client (editor) is the integration surface; Agent plugs into it | Agent/Host is the client; MCP servers expose capabilities to it |
| **Typical use** | Make a coding agent (Claude Code, Gemini CLI, Goose, etc.) usable inside any IDE without per-editor glue code | Give an agent access to external tools and data regardless of which editor or runtime hosts it |

In practice, a single coding agent can speak ACP to its host editor while separately using MCP to call out to external tools — the two protocols operate at different points in the same pipeline.

## Ecosystem and Adoption

- **License / governance**: Apache License 2.0, no CLA required (contributions are automatically licensed under Apache 2.0); governance and contribution process documented in the project's `GOVERNANCE.md` and `CONTRIBUTING.md`.
- **Official SDKs**: TypeScript (`@agentclientprotocol/sdk` on npm), Python (`agent-client-protocol` on PyPI, Pydantic models, asyncio-based), Rust (`agent-client-protocol` / `agent-client-protocol-schema` crates on crates.io), Kotlin (`acp-kotlin`, JVM), and Java.
- **Native agent implementations** (speak ACP directly): Gemini CLI (Google), GitHub Copilot CLI (public preview), Goose, Cline, OpenHands, Mistral's Vibe, Auggie, and Blackbox AI.
- **Adapter-based implementations**: Claude Code and OpenAI's Codex CLI are exposed to ACP-compatible editors via adapters rather than native support.
- **Editor adoption**: Originated in [Zed](https://zed.dev/acp). In October 2025, JetBrains announced a partnership with Zed to co-develop ACP and bring native support to IntelliJ IDEA, PyCharm, and WebStorm; JetBrains and Zed subsequently launched a shared **ACP Agent Registry** — a directory for discovering and connecting ACP-compatible coding agents from within a supporting IDE.
- Google built an ACP-compatible Gemini CLI as the first external integration used to validate the protocol design.

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Per-editor agent integrations | Each new editor/agent pairing traditionally required custom glue code | Implement against the ACP wire protocol once; reuse across any ACP-compliant editor or agent |
| Trusting agent-initiated file/command actions | Agents executing edits or commands without user awareness is a security risk | Require Agents to route sensitive operations (file writes, command execution) through `session/request_permission` and Client-exposed `fs/*` / `terminal/*` capabilities so the editor remains the gatekeeper |
| Version drift between SDKs and wire protocol | Crate/package release numbers do not map 1:1 to protocol compatibility | Negotiate and check the `protocolVersion` returned from `initialize` rather than relying on SDK version numbers to determine compatibility |
| Supporting agents without native ACP support | Some popular coding agents (e.g., Claude Code, Codex CLI) predate ACP | Use or build an adapter that translates the agent's native CLI/API surface into ACP `session/*` calls |

## See Also

- [Model Context Protocol (MCP)](./mcp.md) — complementary protocol for tool/resource access by LLM applications
- [Agent2Agent (A2A) Protocol](./agent2agent.md) — peer-to-peer agent coordination, a different layer than ACP's editor-agent integration
- [Agentic AI Foundation](./agentic-ai-foundation.md) — open-standards governance context for the broader agentic protocol ecosystem
- [AgenticFrameworks/ai-coding-agents.md](../AgenticFrameworks/ai-coding-agents.md) — coding agents such as Claude Code and Gemini CLI that integrate with ACP
- [AllThingsAnthropic/README.md](../AllThingsAnthropic/README.md) — Claude Code's ACP adapter integration
- [AllThingsGoogle/README.md](../AllThingsGoogle/README.md) — Gemini CLI's native ACP support

## References

- [Agent Client Protocol — official site](https://agentclientprotocol.com/) — protocol overview, specification pages (Session Setup, Tool Calls, etc.)
- [agentclientprotocol/agent-client-protocol on GitHub](https://github.com/zed-industries/agent-client-protocol) — reference schema, Rust crates, SDK links, AGENTS.md/contribution process
- [Zed — Agent Client Protocol](https://zed.dev/acp) — protocol announcement and rationale from the originating editor
- [Zed — External Agents documentation](https://zed.dev/docs/ai/external-agents) — list of supported agents and setup instructions
