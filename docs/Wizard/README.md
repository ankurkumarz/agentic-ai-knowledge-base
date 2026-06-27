# Recommendation Wizard

A guided, client-side wizard that helps you find the right starting point in this knowledge base. Answer two short questions and it recommends the most relevant pages — no data leaves your browser.

<style>
#wz-wrap {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  margin: 1rem 0 2rem;
  background: var(--md-code-bg-color);
}
#wz-step-label {
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--md-default-fg-color--light);
  margin-bottom: 0.5rem;
}
#wz-question {
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 1rem;
}
#wz-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.6rem;
  margin-bottom: 1rem;
}
.wz-opt {
  display: block;
  text-align: left;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px;
  padding: 0.65rem 0.9rem;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  cursor: pointer;
  font-size: 0.85rem;
  line-height: 1.3;
  transition: border-color 0.15s, background 0.15s;
}
.wz-opt:hover {
  border-color: var(--md-accent-fg-color);
  background: var(--md-accent-fg-color--transparent);
}
.wz-opt .wz-opt-title { font-weight: 600; display: block; margin-bottom: 0.15rem; }
.wz-opt .wz-opt-desc { color: var(--md-default-fg-color--light); font-size: 0.78rem; }
#wz-results { display: grid; gap: 0.6rem; margin-bottom: 1rem; }
.wz-card {
  display: block;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 6px;
  padding: 0.7rem 0.9rem;
  text-decoration: none;
  color: var(--md-default-fg-color);
  background: var(--md-default-bg-color);
}
.wz-card:hover { border-color: var(--md-primary-fg-color); }
.wz-card .wz-card-title { font-weight: 600; color: var(--md-primary-fg-color); }
.wz-card .wz-card-desc { font-size: 0.82rem; color: var(--md-default-fg-color--light); margin-top: 0.2rem; }
#wz-actions { display: flex; gap: 0.6rem; }
.wz-btn {
  border: 1px solid var(--md-default-fg-color--lightest);
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  border-radius: 5px;
  padding: 0.4rem 0.9rem;
  font-size: 0.82rem;
  cursor: pointer;
}
.wz-btn:hover { border-color: var(--md-primary-fg-color); }
#wz-trail { font-size: 0.78rem; color: var(--md-default-fg-color--light); margin-bottom: 0.75rem; }
#wz-trail span.wz-crumb-active { color: var(--md-primary-fg-color); font-weight: 600; }
</style>

<div id="wz-wrap" markdown="0">
  <div id="wz-trail"></div>
  <div id="wz-step-label"></div>
  <div id="wz-question"></div>
  <div id="wz-options"></div>
  <div id="wz-results"></div>
  <div id="wz-actions"></div>
</div>

{% raw %}
<script>
(function () {
  var root = document.getElementById('wz-wrap');
  if (!root) return;

  // ---- Utils: small recommendation-matching helpers (no backend, pure client-side) ----
  var WizardUtils = {
    page: function (title, path, desc) {
      return { title: title, path: path, desc: desc };
    },
    linkFor: function (path) {
      return '../' + path;
    }
  };

  // ---- Data: goal -> refinement step -> recommended pages ----
  var TREE = {
    title: 'What are you trying to do?',
    options: [
      {
        key: 'new',
        title: 'Learn the basics',
        desc: 'New to agentic AI and want core concepts first.',
        results: [
          WizardUtils.page('Agent Definition', 'Concepts/agent-definition.md', 'What an "agent" means in this context.'),
          WizardUtils.page('Agent Types', 'Concepts/agent-types.md', 'Taxonomy of agent types and capabilities.'),
          WizardUtils.page('Foundations', 'Concepts/agent-foundational.md', 'Foundational building blocks of agentic systems.')
        ]
      },
      {
        key: 'framework',
        title: 'Choose a framework',
        desc: 'Pick an agent development framework or SDK.',
        refine: {
          title: 'What matters most for your choice?',
          options: [
            {
              key: 'graph',
              title: 'Graph / stateful orchestration',
              desc: 'Explicit control flow, branching, long-running state.',
              results: [
                WizardUtils.page('LangGraph', 'AgenticFrameworks/langgraph.md', 'Graph-based orchestration on top of LangChain.'),
                WizardUtils.page('Microsoft Agent Framework', 'AgenticFrameworks/microsoft-framework.md', 'Workflow-oriented multi-agent framework.')
              ]
            },
            {
              key: 'multiagent',
              title: 'Multi-agent collaboration',
              desc: 'Multiple cooperating or role-based agents.',
              results: [
                WizardUtils.page('CrewAI', 'AgenticFrameworks/crewai.md', 'Role-based multi-agent orchestration.'),
                WizardUtils.page('Google ADK', 'AgenticFrameworks/google-adk.md', 'Google’s Agent Development Kit.')
              ]
            },
            {
              key: 'cloud',
              title: 'Cloud-native / managed',
              desc: 'Prefer a managed platform over a self-hosted library.',
              results: [
                WizardUtils.page('AWS Strands Agents', 'AgenticFrameworks/aws-strands.md', 'AWS’s code-first agent SDK.'),
                WizardUtils.page('Google ADK', 'AgenticFrameworks/google-adk.md', 'Google’s Agent Development Kit.'),
                WizardUtils.page('Microsoft Agent Framework', 'AgenticFrameworks/microsoft-framework.md', 'Workflow-oriented multi-agent framework with enterprise/Azure integration.')
              ]
            },
            {
              key: 'general',
              title: 'General purpose / widely adopted',
              desc: 'Looking for the most established, broadly-used option.',
              results: [
                WizardUtils.page('LangGraph', 'AgenticFrameworks/langgraph.md', 'Graph-based orchestration on top of LangChain.'),
                WizardUtils.page('CrewAI', 'AgenticFrameworks/crewai.md', 'Role-based multi-agent orchestration.')
              ]
            }
          ]
        }
      },
      {
        key: 'architecture',
        title: 'Design the architecture',
        desc: 'Choosing components, patterns, or multi-agent topology.',
        results: [
          WizardUtils.page('Architecture Components Selection', 'Architecture/components-selection.md', 'How to choose the building blocks of an agentic system.'),
          WizardUtils.page('Multi-Agent Systems', 'Architecture/multi-agent-system.md', 'Topologies and coordination patterns for multiple agents.'),
          WizardUtils.page('OpenAI Design Patterns', 'DesignPatterns/openai-patterns.md', 'Common agentic design patterns.'),
          WizardUtils.page('12-Factor Agents', 'Architecture/12-factor-agents.md', 'Principles for building reliable agent systems.')
        ]
      },
      {
        key: 'memory',
        title: 'Handle memory & context',
        desc: 'State, long-term memory, or context window management.',
        results: [
          WizardUtils.page('Memory Functional Tiers', 'AgentMemory/functional-tiers.md', 'The four memory types agents use.'),
          WizardUtils.page('LTM Strategies', 'AgentMemory/ltm-strategies.md', 'Long-term memory storage and retrieval strategies.'),
          WizardUtils.page('Context Management Challenges', 'ContextEngineering/challenges.md', 'Common context-window problems.'),
          WizardUtils.page('Context Management Strategies', 'ContextEngineering/strategies.md', 'Mitigations: compaction, retrieval, isolation.')
        ]
      },
      {
        key: 'production',
        title: 'Go to production',
        desc: 'Deployment, reliability, cost, and operations.',
        refine: {
          title: 'Which production concern is most pressing?',
          options: [
            {
              key: 'observability',
              title: 'Observability',
              desc: 'Tracing, logging, metrics, dashboards.',
              results: [
                WizardUtils.page('Observability Best Practices', 'ProductionBestPractices/observability.md', 'Cross-cutting observability guidance for production agents.'),
                WizardUtils.page('Observability Solutions', 'Observability/solutions.md', 'Tooling landscape for agent observability.')
              ]
            },
            {
              key: 'security',
              title: 'Security & governance',
              desc: 'Prompt injection, least privilege, compliance.',
              results: [
                WizardUtils.page('Agent Security', 'ProductionBestPractices/security.md', 'Production security guidance for agents.'),
                WizardUtils.page('NIST AI RMF', 'SecurityFrameworks/nist-ai-rmf.md', 'Risk management framework for AI systems.')
              ]
            },
            {
              key: 'cost',
              title: 'Cost management',
              desc: 'Model routing, token budgets, caching.',
              results: [
                WizardUtils.page('Cost Management', 'ProductionBestPractices/cost-management.md', 'Strategies to control inference and token cost.')
              ]
            },
            {
              key: 'testing',
              title: 'Testing & evaluation',
              desc: 'Evals, red-teaming, regression testing.',
              results: [
                WizardUtils.page('Testing & Evaluations', 'ProductionBestPractices/testing-evaluations.md', 'Production testing and eval guidance.'),
                WizardUtils.page('LLM Evaluation Frameworks', 'EvaluationFrameworks/llm-frameworks.md', 'Frameworks for evaluating LLM/agent quality.')
              ]
            }
          ]
        }
      }
    ]
  };

  // ---- State machine ----
  var state = { node: TREE, trail: [] };

  function render() {
    var trailEl = document.getElementById('wz-trail');
    trailEl.innerHTML = state.trail.map(function (t, i) {
      var active = i === state.trail.length - 1 ? ' wz-crumb-active' : '';
      return '<span class="' + active.trim() + '">' + t + '</span>';
    }).join(' &rsaquo; ') || '&nbsp;';

    document.getElementById('wz-step-label').textContent =
      'Step ' + (state.trail.length + 1);
    document.getElementById('wz-question').textContent = state.node.title;

    var optsEl = document.getElementById('wz-options');
    var resEl = document.getElementById('wz-results');
    var actEl = document.getElementById('wz-actions');
    optsEl.innerHTML = '';
    resEl.innerHTML = '';
    actEl.innerHTML = '';

    if (state.node.options) {
      state.node.options.forEach(function (opt) {
        var btn = document.createElement('button');
        btn.className = 'wz-opt';
        btn.innerHTML = '<span class="wz-opt-title">' + opt.title + '</span>' +
                         '<span class="wz-opt-desc">' + opt.desc + '</span>';
        btn.addEventListener('click', function () {
          state.trail.push(opt.title);
          if (opt.refine) {
            state.node = opt.refine;
          } else {
            state.node = { title: 'Recommended pages', results: opt.results };
          }
          render();
        });
        optsEl.appendChild(btn);
      });
    }

    if (state.node.results) {
      state.node.results.forEach(function (r) {
        var a = document.createElement('a');
        a.className = 'wz-card';
        a.href = WizardUtils.linkFor(r.path.replace(/\.md$/, '/').replace(/README\/$/, ''));
        a.innerHTML = '<span class="wz-card-title">' + r.title + '</span>' +
                       '<div class="wz-card-desc">' + r.desc + '</div>';
        resEl.appendChild(a);
      });
    }

    if (state.trail.length > 0) {
      var backBtn = document.createElement('button');
      backBtn.className = 'wz-btn';
      backBtn.textContent = 'Start over';
      backBtn.addEventListener('click', function () {
        state = { node: TREE, trail: [] };
        render();
      });
      actEl.appendChild(backBtn);
    }
  }

  render();
})();
</script>
{% endraw %}

## How It Works

The wizard is a small client-side state machine: each answer narrows a decision tree down to a curated set of pages already in this wiki. Nothing is sent to a server — the question tree and the recommendation logic both run in the browser.

## See Also

- [Knowledge Graph](../graph.md)
- [Agentic AI Foundation](../Standards/agentic-ai-foundation.md)
- [Architecture Components Selection](../Architecture/components-selection.md)
- [Production Best Practices Overview](../ProductionBestPractices/README.md)

## References

- Internal tool — no external source.
