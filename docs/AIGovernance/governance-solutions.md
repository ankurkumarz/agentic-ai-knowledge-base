# Governance Solutions

## Overview

Governance solutions are the platforms, tools, and services that operationalize AI governance policy at scale. They span commercial enterprise platforms, open-source toolkits, and native offerings from the major cloud providers. The right combination depends on the organization's deployment model (cloud-native, on-premises, hybrid), the regulatory environment, and the maturity of existing MLOps infrastructure.

## Commercial Governance Platforms

### IBM OpenScale / Watson OpenScale (AI Fairness 360 + Watson)

IBM's AI Fairness 360 is an open-source toolkit (backed by IBM Research) for detecting and mitigating bias in ML models, while Watson OpenScale (now IBM OpenPages with Watson) provides an enterprise governance platform for:

- Model inventory and risk classification
- Automated fairness and drift monitoring
- Explainability dashboards
- Regulatory compliance reporting (EU AI Act, SR 11-7)

### Arthur AI

Arthur AI is a model monitoring and observability platform focused on production ML and LLM systems. Key capabilities:

- **Real-time drift detection** for model inputs, outputs, and performance metrics
- **LLM-specific monitoring**: hallucination detection, toxicity scoring, PII detection in completions
- **Explainability**: feature importance and counterfactual explanations for tabular models
- **Alerting and workflow integrations**: Slack, PagerDuty, Jira

### Fiddler AI

Fiddler provides explainable AI monitoring with a focus on enterprise auditability:

- Model performance monitoring with slice-and-dice analysis across demographic segments
- Natural language explanation of model decisions (NLP-based explanation summaries)
- Compliance-ready reporting exports
- Integration with major ML platforms (SageMaker, Vertex AI, Azure ML)

### Holistic AI

Holistic AI offers an AI audit and governance platform specifically designed for regulatory compliance:

- EU AI Act risk classification and conformity assessment support
- Bias and fairness audits with standardized reporting
- Third-party audit-ready documentation packages
- Ongoing monitoring with compliance posture dashboards

### Credo AI

Credo AI is a governance platform that connects policy to technical controls:

- Policy-as-code framework: define governance requirements; platform validates AI systems against them
- Integration with popular ML frameworks (scikit-learn, TensorFlow, PyTorch, Hugging Face)
- Evidence collection for internal audits and regulatory submissions
- Risk register and remediation tracking

## Open-Source Tools

| Tool | Primary Function | Key Features |
|---|---|---|
| **AI Fairness 360 (AIF360)** | Bias detection and mitigation | 70+ fairness metrics, 10+ bias mitigation algorithms, Python/R |
| **Fairlearn** | Fairness assessment and mitigation (Microsoft) | Constraint-based mitigation, interactive dashboard, scikit-learn compatible |
| **SHAP** | Model explainability | Shapley value-based feature importance, works with any ML model |
| **LIME** | Local interpretable model-agnostic explanations | Local surrogate models for per-instance explanation |
| **Alibi Detect** | Outlier, drift, and adversarial detection | Statistical tests for covariate shift, data drift, adversarial inputs |
| **Giskard** | LLM and ML testing for reliability and ethics | Automated vulnerability scanning, bias detection, RLHF-compatible |
| **TruLens** | LLM evaluation and observability | RAG triad evaluation (groundedness, relevance, coherence), feedback functions |
| **Guardrails AI** | Input/output validation for LLMs | Schema validation, fact-checking, toxicity filtering, custom validators |
| **NeMo Guardrails** (NVIDIA) | Conversational guardrails for LLM applications | Colang scripting language, topical and safety rails, multi-turn support |

## Vendor-Native Governance Offerings

### AWS

| Service / Feature | Governance Function |
|---|---|
| **Amazon SageMaker Clarify** | Bias detection in training data and model outputs; feature importance (SHAP) |
| **Amazon SageMaker Model Monitor** | Data quality, model quality, bias drift, and feature attribution drift monitoring |
| **AWS AI Service Cards** | Documentation of responsible AI design for AWS AI services |
| **Amazon Bedrock Guardrails** | Content filtering, PII redaction, topic denial, grounding checks for LLM-based agents |
| **AWS Config + CloudTrail** | Audit trails for AWS resource changes and API calls made by agents |

### Google Cloud

| Service / Feature | Governance Function |
|---|---|
| **Vertex AI Model Monitoring** | Training-serving skew and prediction drift detection |
| **Vertex AI Explainable AI** | Feature attributions (Integrated Gradients, XRAI, SHAP) for structured and image models |
| **Model Cards (Vertex AI)** | Standardized model documentation for transparency and auditability |
| **Google SAIF (Secure AI Framework)** | Six-component framework for AI security and governance (see Security Frameworks) |
| **Vertex AI Gemini Safety Filters** | Input/output content classification and blocking for LLM deployments |
| **Google Cloud Audit Logs** | Complete activity logs for Vertex AI API calls and agent tool use |

### Microsoft Azure

| Service / Feature | Governance Function |
|---|---|
| **Azure AI Content Safety** | Harm detection (hate, violence, self-harm, sexual content) for LLM inputs and outputs |
| **Azure Responsible AI Dashboard** | Unified dashboard: error analysis, fairness assessment, explainability, causal insights |
| **Fairlearn (Azure ML integration)** | Fairness constraints and mitigation in Azure ML pipelines |
| **Azure Policy** | Automated policy enforcement for Azure AI resource configurations |
| **Microsoft Responsible AI Standard** | Internal framework published as guidance for external practitioners |
| **Prompt Shields (Azure AI Studio)** | Prompt injection and jailbreak detection for Azure OpenAI deployments |

### Anthropic

| Offering | Governance Function |
|---|---|
| **Constitutional AI (CAI)** | Alignment technique using AI-written critique and revision to reduce harmful outputs |
| **Claude's System Prompt Controls** | Operator-level restrictions on topics, tool use, and output formatting |
| **Usage Policy and AUP** | Defines prohibited use cases; API access is subject to compliance with AUP |
| **Model Cards** | Published capability and safety evaluation results for each Claude release |

## Integration Patterns

### Governance-as-Code

Encode governance requirements as machine-readable policies that can be evaluated automatically in CI/CD pipelines and at runtime:

```
Policy → Code (Guardrails / NeMo / OPA) → Runtime Enforcement
                                        → CI Gate (pre-deployment validation)
                                        → Audit Export (evidence for compliance)
```

### Layered Defense

Combine multiple controls at different layers rather than relying on a single mechanism:

1. **Data layer**: PII detection and masking before data enters the agent pipeline
2. **Prompt layer**: input validation and injection detection (Guardrails AI, Prompt Shields)
3. **Model layer**: safety filters and content classification at inference time
4. **Action layer**: HITL gates on high-impact tool calls; least-privilege permission model
5. **Output layer**: output validation, PII scrubbing, factual grounding checks
6. **Audit layer**: comprehensive logging of all layers for post-hoc analysis

### Continuous Compliance Monitoring

Integrate governance metrics into the same observability stack used for operational monitoring:

- Ship audit logs to the organization's SIEM (Splunk, Datadog, OpenSearch)
- Create governance dashboards alongside latency and error rate dashboards
- Trigger governance alerts through the same on-call workflow as production incidents
- Produce automated compliance reports from audit log queries (avoid manual evidence collection)

## Solution Selection Criteria

| Criterion | Questions to Ask |
|---|---|
| Regulatory alignment | Does the solution support the specific reporting artifacts required by your applicable regulations (EU AI Act, SOC 2, HIPAA)? |
| LLM/agent support | Does the solution handle LLM-specific risks (prompt injection, hallucination, PII in completions), not just classical ML? |
| Integration depth | Does it integrate with your existing ML platform, CI/CD pipeline, and observability stack? |
| Audit-readiness | Does it produce exportable, tamper-evident evidence packages that auditors will accept? |
| Scalability | Can it handle the volume of agent runs and log events your deployment will generate? |
| Vendor lock-in | Is the solution portable across cloud providers, or does it create dependency on a single vendor? |

## See Also

- [Governance Strategy](governance-strategy.md)
- [Governance Best Practices](governance-best-practices.md)
- [Security Frameworks](../SecurityFrameworks/README.md)
- [Observability Solutions](../Observability/README.md)
- [ProductionBestPractices — Security](../ProductionBestPractices/security.md)
- [AllThingsAWS](../AllThingsAWS/README.md)
- [AllThingsGoogle](../AllThingsGoogle/README.md)
- [AllThingsMicrosoft](../AllThingsMicrosoft/README.md)
- [AllThingsAnthropic](../AllThingsAnthropic/README.md)

## References

- [IBM AI Fairness 360](https://aif360.mybluemix.net/) — open-source bias detection and mitigation toolkit
- [Microsoft Fairlearn](https://fairlearn.org/) — fairness assessment and mitigation library
- [SHAP (Shapley Additive Explanations)](https://shap.readthedocs.io/) — model explainability via game-theoretic feature attribution
- [Guardrails AI](https://www.guardrailsai.com/) — input/output validation framework for LLMs
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — conversational safety rails for LLM applications
- [TruLens](https://www.trulens.org/) — LLM evaluation and observability with RAG triad metrics
- [Giskard](https://www.giskard.ai/) — automated vulnerability testing for LLM and ML models
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) — AWS-native content and topic controls for Bedrock agents
- [Azure Responsible AI Dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard) — Microsoft's unified responsible AI tooling
