# Governance Best Practices

## Overview

Governance best practices translate high-level policy into repeatable engineering and operational controls. For agentic AI systems, the most critical controls address the unique risks introduced by autonomous action: multi-step tool use, non-deterministic decision-making, access to sensitive data, and the difficulty of attributing outcomes to specific model decisions.

## Human-in-the-Loop (HITL) Controls

Human oversight is the primary safeguard for high-impact agentic actions. Effective HITL implementation requires explicit design, not ad-hoc intervention:

| Pattern | When to Apply | Implementation Notes |
|---|---|---|
| **Approval gate** | Before irreversible or high-value actions (financial transactions, data deletion, external communications) | Agent pauses, presents proposed action and rationale, waits for explicit human approval before proceeding |
| **Shadow mode** | During initial production rollout or after capability changes | Agent generates recommendations; human executes; diff between agent and human decision is logged for drift detection |
| **Confidence threshold** | When agent confidence in a decision falls below a defined level | Low-confidence states route to human review queue; agent does not proceed until resolved |
| **Periodic checkpoint** | For long-running autonomous workflows | Agent pauses at defined intervals (e.g., every N actions or T minutes) to summarize progress and request continuation approval |
| **Anomaly escalation** | When agent detects an unexpected state or out-of-distribution input | Agent surfaces the anomaly and halts rather than proceeding with a potentially incorrect action |

## Audit Trail Requirements

A complete audit trail for an agentic system must capture:

- **Inputs**: raw user prompt, retrieved context, tool outputs fed back to the model
- **Model decisions**: which action was selected and the reasoning trace (chain-of-thought or structured rationale)
- **Tool calls**: each external call (API, database, filesystem), arguments passed, response received, and timestamp
- **Human interactions**: approval/rejection decisions, override events, and the identity of the reviewer
- **Outputs**: final response delivered to the user or downstream system
- **System state**: agent version, model version, configuration snapshot at time of execution

Audit logs must be:
- **Tamper-evident**: stored in append-only systems with cryptographic integrity checks
- **Queryable**: structured (JSON or columnar) to support forensic investigation and regulatory reporting
- **Retained** per applicable regulatory requirements (typically 3–7 years for high-risk domains)
- **Access-controlled**: restricted to authorized reviewers with a logged access trail

## Bias and Fairness Monitoring

Agentic systems that make or influence decisions affecting people require ongoing bias monitoring:

| Area | Challenge | Practice |
|---|---|---|
| Training data bias | LLMs inherit biases from pre-training data | Document known limitations; test against demographic subgroups before deployment |
| Retrieval bias | RAG systems may preferentially surface documents that reflect historical patterns | Audit retrieval results across demographic dimensions; apply diversity-aware reranking |
| Decision disparity | Agent recommendations may differ systematically across protected groups | Define fairness metrics (demographic parity, equalized odds) and run regular disparity audits |
| Feedback loop amplification | Agent actions influence future data, which retrains future models | Monitor for distributional drift; include adversarial and edge-case data in eval suites |

## Data Governance

Agents that retrieve and process data from enterprise systems must enforce data governance at the agent layer:

- **Data classification labels** propagate into the agent's context window — agents must not route classified data to tools or services that lack the appropriate clearance
- **PII minimization**: scrub or pseudonymize personal data before sending to external LLM providers unless contractual data processing agreements are in place
- **Purpose limitation**: agents are scoped to specific data domains; access to out-of-scope data sources requires explicit authorization
- **Retention policies**: ephemeral agent context (conversation history, working memory) must be purged on schedule; long-term memory stores are subject to the same retention rules as the underlying data

## Model and Prompt Versioning

| Practice | Description |
|---|---|
| Version every prompt | Store system prompts in version control alongside the application code; tag releases |
| Canary prompt deployments | Roll out prompt changes to a small traffic slice before full deployment; compare evaluation metrics |
| Prompt regression tests | Maintain a curated set of golden inputs and expected outputs; run on every prompt change in CI |
| Model pinning | Pin to a specific model version in production; test against new model versions in staging before promoting |
| Change attribution | Link every production incident back to the specific prompt version, model version, or configuration change that was active |

## Incident Response

Every production agent deployment requires a documented incident response plan:

1. **Detection**: monitoring alerts fire on anomalous action rates, error spikes, or HITL escalation volume
2. **Containment**: kill switches and feature flags allow instant disabling of specific agent capabilities without full rollback
3. **Investigation**: structured audit logs support root-cause analysis; queries identify the specific decision chain that produced the incident
4. **Remediation**: fix prompt, tool, or configuration; deploy via canary with regression tests
5. **Post-mortem**: document root cause, contributing factors, timeline, and preventive controls; share findings with governance stakeholders
6. **Regulatory notification**: for high-risk AI systems under the EU AI Act or sector-specific regulations, serious incidents may trigger mandatory reporting obligations

## Red-Teaming and Adversarial Testing

Before production deployment of high-autonomy agents, conduct structured adversarial testing:

- **Prompt injection**: attempt to override system prompt instructions via user input or retrieved documents
- **Scope creep**: craft inputs that attempt to lead the agent outside its authorized domain
- **Privilege escalation**: test whether the agent can be manipulated into using tools or data sources it should not access
- **Hallucination under pressure**: verify that the agent declines rather than fabricates when asked for information outside its knowledge
- **Multi-agent collusion**: in multi-agent systems, test whether a compromised sub-agent can manipulate orchestrator behavior

Document test cases, results, and residual risks in the system's risk register. Re-run adversarial tests after any significant model, prompt, or tool change.

## Governance Metrics

Track these metrics as leading indicators of governance health:

| Metric | What It Signals |
|---|---|
| HITL escalation rate | Percentage of agent runs that triggered a human review; sharp increases indicate unexpected agent behavior |
| Action reversal rate | Percentage of agent actions reversed by humans post-execution; high rates indicate autonomy is miscalibrated |
| Policy violation incidents | Count of attempts (blocked or successful) to breach access control or data handling policies |
| Audit log completeness | Percentage of agent runs with complete, parseable audit logs; gaps indicate instrumentation failures |
| Fairness disparity score | Difference in agent recommendation rates across demographic subgroups; monitored on a rolling basis |
| Model/prompt change frequency | How often configuration changes are deployed; high frequency without corresponding test coverage is a risk signal |

## See Also

- [Governance Strategy](governance-strategy.md)
- [Governance Solutions](governance-solutions.md)
- [ProductionBestPractices — Security](../ProductionBestPractices/security.md)
- [ProductionBestPractices — Testing & Evaluations](../ProductionBestPractices/testing-evaluations.md)
- [ProductionBestPractices — Observability](../ProductionBestPractices/observability.md)
- [Security Frameworks](../SecurityFrameworks/README.md)

## References

- [NIST AI Risk Management Framework 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — Map, Measure, Manage functions inform control design
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — Article 9 (risk management), Article 12 (record-keeping), Article 14 (human oversight)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — prompt injection, insecure output handling, and other agent-specific risks
