# AI Agent Skill Security Scanners

## Overview

AI agent skill security scanners are dedicated tools for vetting the safety of agent skills — markdown-defined workflow definitions used by Claude Code, OpenAI Codex CLI, Cursor, and similar agent harnesses — before they are installed or executed. Research indicates that 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent, making automated scanning an essential layer in the skill supply chain. Two open-source tools address this gap: **Cisco AI Defense Skill Scanner** and **NVIDIA SkillSpector**.

Both tools combine static pattern matching, AST-based behavioral analysis, and optional LLM-powered semantic evaluation. They output structured reports in formats compatible with CI/CD pipelines and GitHub Code Scanning (SARIF).

## Tools at a Glance

| Attribute | Cisco Skill Scanner | NVIDIA SkillSpector |
|---|---|---|
| Vendor | Cisco AI Defense | NVIDIA |
| License | Open source | Apache 2.0 |
| Language | Python | Python 3.12+ |
| Install | `pip install cisco-ai-skill-scanner` | `make install` |
| Input formats | Skill directories, OpenAI Codex, Cursor | Git repos, URLs, ZIP files, directories, individual files |
| Detection patterns | YAML + YARA + AST + LLM | 64 patterns across 16 categories |
| Vulnerability CVE lookup | VirusTotal hash scanning | Live OSV.dev API with offline fallback |
| Output formats | Summary, JSON, Markdown, Table, SARIF, interactive HTML | Terminal, JSON, Markdown, SARIF |
| LLM providers | Bedrock, Google AI, Vertex, Azure OpenAI | OpenAI, Anthropic, NVIDIA build.nvidia.com |
| Workflow engine | N/A | LangGraph |
| CI/CD integration | GitHub Actions, pre-commit hooks, REST API | SARIF output for GitHub Code Scanning |

## Cisco AI Defense Skill Scanner

**Repository**: [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)

### Architecture

Skill Scanner uses a layered, multi-engine approach to reduce false positives through consensus:

1. **Static Analysis** — YAML and YARA pattern matching across all skill files
2. **Bytecode Integrity** — verifies that code artifacts have not been tampered with
3. **Pipeline Command Taint Analysis** — traces untrusted data flows through shell command pipelines
4. **Behavioral Analysis (AST)** — AST dataflow analysis for Python files, tracking tainted inputs to sensitive sinks
5. **LLM-Based Semantic Analysis** — AI-powered detection using configurable providers (Bedrock, Google AI, Vertex, Azure OpenAI); supports majority-vote consensus across configurable iteration counts
6. **Meta-Analyzer** — aggregates findings across all engines; applies consensus filtering to reduce noise
7. **Cloud Integration** — optional VirusTotal hash scanning and Cisco AI Defense cloud analysis

### CLI Commands

```bash
skill-scanner scan ./my-skill/           # single skill directory
skill-scanner scan-all ./skills/         # recursive multi-skill scan
skill-scanner interactive                # guided wizard
skill-scanner generate-policy            # create a custom scan policy
skill-scanner list-analyzers             # show available detection engines
```

### Non-Standard Format Support

The `--lenient` flag enables scanning of formats that do not conform to the OpenAI Codex or Cursor specification — specifically Claude Code `.claude/commands/*.md` skill files.

### Output and Integration

- **SARIF** output integrates directly with GitHub Code Scanning for PR-level security gating
- **Interactive HTML** reports group findings by attack correlation
- **Exit codes** based on severity thresholds allow build pipeline blocking
- **REST API** mode supports embedding Skill Scanner in a service mesh

### Key Limitation

> "No findings ≠ no risk. A scan returning 'No findings' indicates no known threat patterns were detected — it does not guarantee security or freedom from vulnerabilities."

## NVIDIA SkillSpector

**Repository**: [nvidia/skillspector](https://github.com/nvidia/skillspector)

### Architecture

SkillSpector uses a two-stage pipeline:

**Stage 1 — Static Analysis (always runs)**
- Regex pattern matching against 64 vulnerability signatures
- AST-based behavioral analysis (taint tracking from sources to sinks)
- YARA malware signature matching
- Dependency vulnerability scanning via live OSV.dev API (offline fallback available)

**Stage 2 — LLM Analysis (optional)**
- Context evaluation using a configured LLM provider
- False-positive filtering: LLM reclassifies borderline static findings
- Supports OpenAI, Anthropic, NVIDIA build.nvidia.com, and local OpenAI-compatible servers (Ollama, vLLM)
- Built on a **LangGraph** processing pipeline

### Vulnerability Categories (16 Domains)

Prompt injection · Data exfiltration · Privilege escalation · Supply chain attacks · Excessive agency · Output handling vulnerabilities · System prompt leakage · Memory poisoning · Tool misuse · Rogue agent behavior · Trigger abuse · AST-based code analysis · Taint tracking · YARA malware signatures · MCP-specific risks · Dependency CVEs (OSV.dev)

### CLI Usage

```bash
skillspector scan ./my-skill/
skillspector scan https://github.com/user/my-skill
skillspector scan ./skill.zip --format json --output report.json
skillspector scan ./my-skill/ --format sarif --output results.sarif
```

### Risk Scoring

Produces a 0–100 severity score per skill with actionable recommendations per finding.

### Key Limitation

Static and LLM analysis cannot evaluate runtime behavior; encrypted or binary code cannot be assessed.

## Detection Threat Model Comparison

| Threat Category | Cisco Skill Scanner | NVIDIA SkillSpector |
|---|---|---|
| Prompt injection | Yes (YARA + LLM) | Yes (64 patterns + LLM) |
| Data exfiltration | Yes (taint analysis) | Yes (taint tracking) |
| Malicious code patterns | Yes (YAML + YARA + AST) | Yes (YARA + AST) |
| Supply chain attacks | Partial (VirusTotal hash) | Yes (OSV.dev CVE lookup) |
| Privilege escalation | Partial (pipeline taint) | Yes (dedicated category) |
| MCP-specific risks | No | Yes (dedicated category) |
| Memory poisoning | No | Yes (dedicated category) |
| Rogue agent behavior | No | Yes (dedicated category) |
| False-positive reduction | Meta-Analyzer consensus | LLM reclassification |

## Best Practices

| Area | Description | Recommendation |
|---|---|---|
| CI/CD gating | Block PRs that introduce unsafe skills | Use SARIF output with GitHub Code Scanning; set severity threshold exit codes to fail the pipeline |
| Pre-install vetting | Scan third-party skills before deployment | Run SkillSpector or Skill Scanner against any skill fetched from an external source; treat all external skills as untrusted |
| LLM analysis cost | LLM engine adds latency and API cost | Enable LLM analysis only for findings above a static severity threshold; use local models (Ollama) for high-volume scanning |
| Non-standard formats | Claude Code `.claude/commands/*.md` files | Use Skill Scanner with `--lenient` flag; SkillSpector accepts raw directories natively |
| CVE coverage | Dependency vulnerabilities in skill-authored code | SkillSpector's OSV.dev integration covers this; configure offline fallback for air-gapped environments |
| Layered scanning | No single engine catches all threats | Run both tools in complementary roles: SkillSpector for broad CVE + MCP coverage, Skill Scanner for consensus-filtered semantic analysis |
| Policy customization | Generic policies produce irrelevant findings | Use `skill-scanner generate-policy` to create context-specific rules for your skill inventory |

## See Also

- [Agent Skills / SKILLS.md Standard](../Standards/skills.md)
- [Agent Security Best Practices](../ProductionBestPractices/security.md)
- [Agentic AI Security Overview](./Readme.md)
- [Agent Governance Toolkit](./agent-governance-toolkit.md)
- [Anthropic Sandbox Runtime](./anthropic-sandbox-runtime.md)
- [Agent Sandboxing](./agent-sandboxing.md)
- [Model Context Protocol](../Standards/mcp.md)
- [EvaluationFrameworks](../EvaluationFrameworks/Readme.md)

## References

- [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) — Open-source multi-engine skill security scanner from Cisco AI Defense; detects prompt injection, data exfiltration, and malicious code patterns
- [nvidia/skillspector](https://github.com/nvidia/skillspector) — Open-source two-stage skill scanner from NVIDIA; 64 vulnerability patterns across 16 categories with live OSV.dev CVE lookup and LangGraph pipeline
