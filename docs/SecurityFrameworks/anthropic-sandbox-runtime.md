# Anthropic Sandbox Runtime

## Overview

The **Anthropic Sandbox Runtime** (`srt`) is a lightweight, OS-level sandboxing tool that enforces filesystem and network restrictions on arbitrary processes without requiring a container. Released as a research preview by Anthropic, its primary use case is sandboxing **Model Context Protocol (MCP) servers** to limit their capabilities — restricting which files they can read or write and which network endpoints they can reach — without the overhead of a full container runtime.

Available as an npm package (`@anthropic-ai/sandbox-runtime`) with ~4.1k GitHub stars and Apache-2.0 licensing, it is designed for developers who want tighter control over the tools their agents invoke.

## Key Features

- **Filesystem isolation** — deny-then-allow patterns for reads; allow-only model for writes; configurable path-level granularity
- **Network isolation** — allow-only model with HTTP/SOCKS5 proxies that filter traffic through localhost ports (macOS) or Unix sockets (Linux); blocks all unlisted domains
- **Unix socket control** — restricts access to local IPC sockets used by processes
- **Violation monitoring** — real-time alerts for sandbox breaches (macOS); event log for breach forensics

## Architecture

The sandbox uses native OS primitives rather than containerization, resulting in lower overhead:

| Platform | Mechanism | Network Filtering |
|---|---|---|
| macOS | `sandbox-exec` with dynamically generated Seatbelt security profiles | HTTP and SOCKS5 proxies bound to localhost ports |
| Linux | `bubblewrap` with network namespace isolation | HTTP and SOCKS5 proxies bound to Unix sockets |
| Windows | Not yet supported | — |

Both platforms use a dual-layer approach: one layer enforces the OS-level restriction policy; a second layer applies proxy-based filtering for network traffic that passes the first layer.

The codebase ships as both a **CLI tool** and a **reusable library**, allowing integration into agent harnesses programmatically.

## Primary Use Case — Sandboxing MCP Servers

MCP servers are third-party processes that agents invoke for tools and resources. Without sandboxing, a compromised or misbehaving MCP server could:

- Exfiltrate files from the host filesystem
- Phone home to arbitrary network endpoints
- Escalate capabilities beyond what the agent intends to grant

Wrapping each MCP server in `srt` applies a least-privilege envelope at the OS level: the server process can only access the filesystem paths and network destinations explicitly allowed in its policy, regardless of what instructions the agent sends to it.

## Installation

```bash
npm install -g @anthropic-ai/sandbox-runtime
```

Linux requires `bubblewrap`, `socat`, and `ripgrep` as system dependencies.

## Best Practices

| Challenge | Description | Solution |
|---|---|---|
| MCP server over-privilege | MCP servers run as host OS processes with the invoking user's permissions | Wrap each MCP server process with `srt`; define an explicit allowlist of paths and domains |
| Lateral file access | A compromised MCP tool reads files outside its intended scope | Configure deny-then-allow filesystem policy scoped to the project directory only |
| Unintended exfiltration | An agent tool sends data to an unintended remote endpoint | Use network allow-only mode; list only the endpoints the tool is expected to reach |
| Violation blind spots | Sandbox breaches occur silently, making forensics difficult | Enable violation monitoring; pipe alerts to your observability stack |
| Container overhead avoidance | Full Docker/OCI containers are too heavy for per-tool isolation | `srt` uses OS-native primitives (Seatbelt / bubblewrap) for lightweight, per-process isolation |

## Relationship to Broader Security Architecture

`srt` addresses a specific layer: **execution envelope isolation for MCP-invoked processes**. It complements but does not replace:

- **Input/output filtering** — still needed at the agent boundary for prompt injection defense
- **Identity and credential management** — `srt` does not manage secrets or authentication
- **Policy engines** (e.g., Microsoft AGT) — deterministic pre-execution policy checks that operate above the OS layer
- **Observability** — trace your agent's tool calls alongside `srt` violation logs for complete audit coverage

## See Also

- [Model Context Protocol (MCP)](../Standards/mcp.md)
- [Agent Security — Production Best Practices](../ProductionBestPractices/security.md)
- [Agentic AI Security Overview](./Readme.md)
- [Agent Governance Toolkit (Microsoft)](./agent-governance-toolkit.md)
- [Anthropic — Agentic AI Overview](../AllThingsAnthropic/README.md)

## References

- [anthropic-experimental/sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) — GitHub repository; Apache-2.0; ~4.1k stars; research preview for OS-level process sandboxing aimed at MCP servers
