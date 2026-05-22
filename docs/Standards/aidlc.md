# AI-Driven Development Life Cycle (AIDLC)

## Overview

**AIDLC** (AI-Driven Development Life Cycle) is an open-source, methodology-first framework from AWS Labs that guides AI coding agents through structured, human-approved phases of software development. Rather than treating AI assistance as a free-form chat interaction, AIDLC embeds requirements, design, and implementation as file-based artifacts — keeping context persistent and auditable across the full development lifecycle. The framework is agent-agnostic, IDE-agnostic, and model-agnostic, working through rule files that are loaded into whichever AI assistant the developer uses. As of April 2026 the project is at v0.1.8 with 2.4k GitHub stars, released under the MIT-0 license (permissive, no attribution required).

## Design Tenets

| Tenet | Description |
|---|---|
| No duplication | Single source of truth; platform-specific rule files are generated, not maintained as parallel copies |
| Methodology first | Works without tool installation; the framework is a methodology expressed in markdown files |
| Reproducible | Structured prompts and explicit stage gates minimize model variance |
| Agnostic | Platform-, IDE-, and vendor-neutral |
| Human in the loop | Critical decisions require explicit user confirmation before each stage executes |

## Three-Phase Adaptive Workflow

AIDLC decomposes development into three sequential phases. The framework adapts execution scope to request complexity — simple changes skip unnecessary stages while complex changes receive comprehensive treatment.

### Phase 1 — Inception (What to Build)

Determines requirements and approach before any code is written:

- **Requirements Analysis**: Structured questions to the developer; opt-in extensions surface additional constraints
- **User Story Creation**: Formalizes acceptance criteria from requirements
- **Design and Risk Assessment**: Identifies architectural decisions and risks upfront

### Phase 2 — Construction (How to Build)

Implements the agreed design under continuous quality control:

- **Component Design**: Breaks work into discrete, testable components
- **Code Generation**: AI generates code against the agreed specification
- **Testing Strategies and Quality Assurance**: Validates generated code against specs and quality criteria

### Phase 3 — Operations (Future)

Planned capability covering deployment automation, monitoring, and production readiness (not yet released as of v0.1.8).

## Artifact Structure

All generated outputs land in a structured directory inside the project:

```
<project-root>/
├── <platform-specific-rules-folder>/     # Agent instruction files (location varies by tool)
├── .aidlc-rule-details/                  # Shared rule detail files
│   ├── common/
│   ├── inception/
│   ├── construction/
│   ├── extensions/
│   └── operations/
└── aidlc-docs/                           # Generated artifacts (proposals, designs, tasks)
```

Rule files use a structured markdown format with `## Rule <PREFIX-NN>: <Title>` headers, a **Rule** section defining the requirement, and a **Verification** section with concrete evaluation criteria, enabling automated auditing.

## Platform Integration

AIDLC is activated by prefixing a request with `"Using AI-DLC, ..."` in any supported agent. Rule files are installed in tool-specific locations:

| AI Tool / IDE | Rules Location |
|---|---|
| Amazon Q Developer | `.amazonq/rules/` |
| Kiro | `.kiro/steering/` |
| Cursor | `.cursor/rules/` |
| Cline | `.clinerules/` |
| Claude Code | `CLAUDE.md` or `.claude/` |
| GitHub Copilot | `.github/copilot-instructions.md` |

## Extensions System

Extensions layer additional constraints (security baselines, compliance, testing policies) on top of the core workflow. Each extension includes:

- A rules file with blocking verification criteria and unique rule IDs (e.g., `SECURITY-01`) for audit trails
- An optional `<name>.opt-in.md` file that presents multiple-choice prompts during Requirements Analysis, letting developers selectively enable rules per change

Built-in extensions cover security baselines and property-based testing. Teams can author custom extensions for organizational policies.

## Supporting Tools

### AIDLC Evaluator

An automated testing framework (`scripts/aidlc-evaluator/`) that provides:

- **Golden test cases**: Representative scenarios for regression detection
- **Semantic evaluation**: LLM-as-judge scoring of agent outputs
- **Code analysis**: Linting and security scanning of generated code
- **NFR testing**: Non-functional requirement validation (token budgets, execution time)
- **CI/CD integration**: Blocks deployment when quality metrics fall below threshold

### AIDLC Design Reviewer (Experimental)

An AI-powered design analysis tool (`scripts/aidlc-designreview/`) available as a CLI or Claude Code hook. Uses three specialized agents:

| Agent | Role |
|---|---|
| Critique | Identifies weaknesses and risks in the proposed design |
| Alternatives | Suggests alternative approaches and trade-offs |
| Gap Analysis | Finds missing requirements or incomplete coverage |

Uses Amazon Bedrock as its backing model runtime.

## Installation

```bash
# Download and extract the release zip
# Copy rules to agent-specific location, e.g. for Cursor:
mkdir -p .cursor/rules
cat aws-aidlc-rules/core-workflow.md >> .cursor/rules/ai-dlc-workflow.mdc
mkdir -p .aidlc-rule-details
cp -R aws-aidlc-rule-details/* .aidlc-rule-details/

# Activate by prefixing requests:
# "Using AI-DLC, add a user authentication feature..."
```

Update to the latest version: `openspec update` (if using the CLI wrapper) or re-download the release zip.

## Comparison with Similar Frameworks

| Dimension | AIDLC (AWS) | OpenSpec (Fission AI) | AWS Kiro |
|---|---|---|---|
| Approach | Lifecycle phases with approval gates | Artifact-guided propose/apply/archive | Spec-as-source-of-truth IDE |
| Phase gates | Explicit — agent waits for approval | None — fluid updates throughout | Structured within Kiro IDE |
| Brownfield support | Yes (`/opsx:onboard` equivalent) | Yes (explicit goal) | Primarily new projects |
| Tool agnosticism | High — 6+ tools via rule files | High — 25+ tools via slash commands | Low — Kiro-specific |
| Complexity model | Adaptive (skips stages for simple changes) | Flat (always propose/apply/archive) | Spec-driven per feature |
| Evaluator included | Yes — AIDLC Evaluator with CI/CD hooks | No native evaluator | Built-in steering validation |
| AWS integration | Native (Bedrock for Design Reviewer, Q Developer) | None | Deep AWS/Bedrock integration |
| License | MIT-0 | MIT | Proprietary |
| Maturity (Apr 2026) | v0.1.8, 2.4k stars | v1.3.1, 50.1k stars | GA (AWS managed) |

## Best Practices

| Challenge / Area | Description | Solution / Recommendation |
|---|---|---|
| Phase skipping | Complex changes need all phases; simple fixes do not | Let AIDLC's adaptive engine decide scope — avoid overriding phase gates manually |
| Extension sprawl | Too many extensions create cognitive overhead | Start with core workflow; add extensions incrementally based on real quality gaps |
| Artifact staleness | `aidlc-docs/` accumulates outdated artifacts | Archive completed change folders; reference past artifacts explicitly when re-opening related work |
| Design Reviewer cost | Three-agent design review consumes significant tokens | Use as a gate for architectural changes, not routine feature work |
| CI/CD integration | Evaluator needs access to golden test cases | Maintain golden test set in version control; update on each significant behavioral change |

## See Also

- [OpenSpec (Fission AI)](./openspec.md)
- [AGENTS.md Standard](./agents-md.md)
- [Agentic AI Foundation](./agentic-ai-foundation.md)
- [Model Context Protocol](./mcp.md)
- [AgentHarness Engineering](../AgentHarness/harness-engineering.md)
- [Production Best Practices: Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [Production Best Practices: Deployment](../ProductionBestPractices/deployment.md)
- [AWS — Agentic AI Overview](../AllThingsAWS/README.md)

## References

- [awslabs/aidlc-workflows GitHub Repository](https://github.com/awslabs/aidlc-workflows) — official source, MIT-0 license, v0.1.8
- [AI-Driven Development Life Cycle (AWS DevOps Blog)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — launch blog post and design rationale
