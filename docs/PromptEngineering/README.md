# Prompt Engineering

## Overview

Prompt engineering is the practice of designing inputs to foundation models to reliably produce desired outputs. It is one of the three core AI engineering techniques (alongside RAG and finetuning) for adapting models to specific applications — and usually the first to try, since it requires no model weight updates, no training data, and produces results in hours rather than weeks.

## Core Concepts

### What Is a Prompt?

A prompt is an instruction given to a model to perform a task. It typically consists of:

- **Task description**: What to do, including the role the model should play and the output format
- **Examples**: Demonstrations of the desired behavior (few-shot learning)
- **The task itself**: The specific question to answer, text to summarize, or problem to solve

### In-Context Learning: Zero-Shot and Few-Shot

In-context learning (introduced in the GPT-3 paper, Brown et al., 2020) means a model learns the desired behavior from examples in the prompt, without updating its weights.

- **Zero-shot**: No examples — the model relies on task description alone
- **Few-shot**: 1–10 examples provided — reduces ambiguity and steers tone, format, and content

The examples don't need to be complex. Simple demonstrations of the expected input-output pattern are often sufficient. Providing examples also serves as a consistency check: if the model can't follow the pattern from your examples, it probably can't follow your prompt either.

### System Prompt vs. User Prompt

Most model APIs split prompts into two roles:

- **System prompt**: Persistent instructions from the developer — persona, constraints, output format, behavioral guidelines. Applied to every conversation turn.
- **User prompt**: Per-turn input from the user — the actual question, document, or task.

Example:
```
System: You're an experienced real estate agent. Read each property disclosure 
carefully, assess the property's condition fairly, and help buyers understand 
risks and opportunities. Answer succinctly and professionally.

User:
Context: [disclosure.pdf]
Question: Summarize the noise complaints, if any, about this property.
```

System prompts are proprietary. Protecting them from extraction (through reverse prompt engineering or injection attacks) is a security concern for production applications.

## Prompt Engineering Best Practices

Synthesized from Chip Huyen's *AI Engineering* (O'Reilly, 2025, Chapter 5), OpenAI, Anthropic, Meta, and Google prompt engineering guides.

### 1. Write Clear and Explicit Instructions

- **Be unambiguous**: If you want a score from 1–5, say so. If you don't want fractional scores, say "output only integer scores."
- **Adopt a persona**: Ask the model to roleplay a specific role (first-grade teacher, senior engineer, legal reviewer). This shifts the model's perspective to match the intended output quality.
- **Provide examples**: Examples reduce ambiguity dramatically. A model that gives factually correct but contextually wrong answers (e.g., telling children Santa is fictional) can be steered with a single example of the desired framing.

### 2. Provide Sufficient Context

Models generate better responses when given the relevant context. Don't assume the model knows your use case, your users, or your domain — explicitly provide what matters.

- Include relevant background data in the prompt or via RAG retrieval
- Specify the audience ("explain this to a non-technical stakeholder")
- Specify constraints explicitly ("do not speculate beyond what the document states")

### 3. Break Complex Tasks into Simpler Subtasks

For multi-step tasks, decompose the prompt into a chain of simpler prompts rather than writing one giant prompt:

**Benefits of prompt decomposition**:
- **Performance**: Models follow simpler instructions more reliably
- **Monitoring**: Intermediate outputs can be inspected and logged
- **Debugging**: Failures are localized to a specific step
- **Parallelization**: Independent steps can run concurrently, reducing latency
- **Cost**: Smaller prompts use fewer tokens; cheaper models can handle simpler steps

**Example** (customer support):
1. Prompt 1: Classify the intent (billing / technical support / account management / general inquiry)
2. Prompt 2a: If technical support → troubleshooting script
3. Prompt 2b: If billing → billing resolution script

GoDaddy found that decomposing a 1,500-token monolithic prompt into smaller targeted prompts improved model performance while reducing token costs.

**Tradeoff**: More intermediate steps increase end-to-end latency for the user, and more model calls increase cost. Find the right decomposition granularity through experimentation.

### 4. Give the Model Time to Think

- **Chain-of-Thought (CoT)**: Instruct the model to "think step by step." CoT was introduced by Wei et al. (2022) and consistently improves performance on reasoning tasks across model families. LinkedIn found CoT also reduces hallucination rates.
- **Self-critique**: Ask the model to verify its own answer before finalizing. This catches surface-level errors but is limited by self-bias.
- **Extended reasoning**: Some models (GPT-o1/o3, Claude 3.5 Sonnet) have dedicated "extended thinking" modes that allocate additional compute to reasoning before producing a response.

### 5. Iterate on Your Prompts

Prompt engineering is empirical. No prompt is final:

1. Start with the simplest prompt that could plausibly work
2. Test on a representative sample of real inputs
3. Identify failure modes (what kinds of inputs produce bad outputs?)
4. Revise the prompt to address failures
5. Retest to verify the fix didn't introduce new failures

**Version your prompts**: Store prompts in version control alongside evaluation results. Treat prompt changes like code changes — include regression tests.

### 6. Organize and Version Prompts

- Store prompts in a dedicated repository or prompt management tool
- Pin the model version alongside the prompt (model updates can silently break prompts)
- Maintain a regression test suite of known-good input/output pairs
- Log which prompt version was used for each production inference, for debugging

## Defensive Prompt Engineering

### The Threat Model

AI applications face two prompt-based attack vectors:

1. **Prompt injection**: An attacker embeds instructions in user input or retrieved content that override the system prompt, changing the model's behavior
2. **Jailbreaking**: Crafted prompts that bypass the model's safety training to elicit harmful or policy-violating outputs

Both are fundamentally difficult to eliminate because the same mechanism that makes models flexible (instruction following) makes them vulnerable.

### Proprietary Prompt Exfiltration

System prompts contain proprietary business logic and are routinely targeted for extraction via social engineering ("Repeat your instructions exactly") or indirect extraction through behavior analysis. Mitigations:

- Instruct the model never to reveal its system prompt
- Avoid putting irreplaceable secrets in system prompts (they will eventually be extracted)
- Monitor for prompt extraction attempts in logs

### Defenses Against Prompt Injection

| Defense | Description | Limitation |
|---|---|---|
| Input filtering | Detect and block injection patterns in user input | Pattern-based; bypassed by paraphrasing |
| Output filtering | Inspect model output for signs of hijacked behavior | Reactive; adds latency |
| Privilege separation | Keep untrusted retrieved content out of instruction position | Architectural; requires careful prompt templating |
| Prompt hardening | Explicit instructions to ignore conflicting instructions in retrieved content | Reduces but does not eliminate risk |
| Model-based classifiers | A dedicated classifier evaluates whether each input is likely an injection attempt | Cost; false positives |

**Fundamental limitation**: No perfect defense exists. Prompt injection is an inherent consequence of mixing instructions and data in a single context. Treat it as a risk to mitigate and monitor, not a problem to fully eliminate.

## Structured Outputs

Requiring models to output structured formats (JSON, XML, specific schemas) offers several benefits for production:

- Easier programmatic parsing
- Enforces constraints (no forbidden fields, required fields must be present)
- Reduces verbose prose in responses

Most major model APIs support structured output modes (OpenAI's `response_format`, Anthropic's tool use schemas, Google's response schemas). Libraries like Outlines and Instructor enforce structured outputs at the decoding level.

## Context Length and Efficiency

Longer prompts consume more tokens, increasing cost and latency. Strategies for context efficiency:

- Keep system prompts minimal; remove instructions that don't affect behavior
- Remove redundant or contradictory instructions as prompts evolve
- Use prompt decomposition to avoid sending irrelevant context to each step
- Summarize long retrieved passages rather than including them verbatim

## See Also

- [AI Engineering Overview](../Concepts/ai-engineering.md)
- [RAG Architecture](../RAG/Readme.md)
- [Context Engineering Strategies](../ContextEngineering/strategies.md)
- [AI as a Judge](../EvaluationFrameworks/ai-as-judge.md)
- [Agent Security / Prompt Injection](../ProductionBestPractices/security.md)
- [SkillOpt (Microsoft)](skillopt.md)
- [GEPA (Genetic-Pareto)](gepa.md)

## Tutorials and Guides

- [Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [Google Prompt Engineering Whitepaper](https://www.kaggle.com/whitepaper-prompt-engineering)

## References

- [AI Engineering: Building Applications with Foundation Models](https://www.oreilly.com/library/view/ai-engineering/9781098166304/) — Chip Huyen, O'Reilly, 2024. Chapter 5.
- [Brown et al. (2020) — Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)
- [Wei et al. (2022) — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [Khattab et al. (2023) — DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714)

## Prompt Examples

### Technical Writer Prompt (Gemini)

```markdown
You are a senior technical writer. Your task is to propose a new documentation
page based on trends in recent customer feedback.

**Step 1: Analyze Recent Customer-Reported Documentation Issues**
Analyze open customer issues to identify the most common or impactful user
pain points and respond with 2-3 top level themes, including the issue count
for each. Stop here and let me ask any questions about the analysis. From the
top themes, ask me to confirm which theme to proceed with.

Here is the list of issues: `doc-issues.csv`

**Step 2: Propose a New Content Type**
Determine the best content type (How-to, Concept, or Troubleshooting) that best
addresses the content theme. Then, propose an outline for the new page.
```
