# Knowledge Graph

Explore connections across the knowledge base. Nodes are colour-coded by section; size reflects the number of **See Also** links. Click any node to navigate to that page.

<style>
#kg-wrap {
  position: relative;
  background: #0d0d1a;
  border-radius: 8px;
  border: 1px solid #2a2a4a;
  overflow: hidden;
  margin: 1rem 0 2rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
#kg-bar {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  padding: 10px 14px;
  background: #12122a;
  border-bottom: 1px solid #1e1e3f;
  font-size: 12px;
}
#kg-search {
  background: #1e1e3f;
  border: 1px solid #3a3a6a;
  border-radius: 5px;
  padding: 4px 10px;
  color: #ddd;
  font-size: 12px;
  width: 160px;
  outline: none;
}
#kg-search:focus { border-color: #5b6af0; }
#kg-chips { display: flex; flex-wrap: wrap; gap: 5px; }
.kg-chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #1a1a3a;
  border: 1px solid #3a3a6a;
  border-radius: 12px;
  padding: 2px 8px;
  cursor: pointer;
  color: #777;
  font-size: 10px;
  user-select: none;
  transition: border-color 0.15s, color 0.15s, background 0.15s;
}
.kg-chip.on {
  border-color: #5b6af0;
  color: #c0c8ff;
  background: rgba(91, 106, 240, 0.12);
}
.kg-chip .dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
#kg-stats { color: #444; font-size: 11px; margin-left: auto; white-space: nowrap; }
#cy { width: 100%; height: 70vh; min-height: 520px; display: block; }
#kg-legend {
  position: absolute;
  bottom: 12px;
  left: 12px;
  background: rgba(10, 10, 24, 0.93);
  border: 1px solid #2a2a4a;
  border-radius: 6px;
  padding: 10px 14px;
  font-size: 11px;
  color: #aaa;
  max-height: 260px;
  overflow-y: auto;
  line-height: 1.7;
  z-index: 10;
}
#kg-legend h4 {
  margin: 0 0 5px;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #555;
}
.kg-leg-row { display: flex; align-items: center; gap: 6px; }
.kg-leg-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
#kg-tip {
  position: absolute;
  pointer-events: none;
  background: rgba(14, 14, 38, 0.97);
  border: 1px solid #4a4a8a;
  border-radius: 7px;
  padding: 9px 13px;
  font-size: 12px;
  max-width: 230px;
  display: none;
  z-index: 30;
  line-height: 1.5;
}
#kg-tip b { display: block; font-size: 13px; color: #e0e0ff; margin-bottom: 2px; }
#kg-tip .tt-sec { color: #5b6af0; font-size: 11px; }
#kg-tip .tt-deg { color: #555; font-size: 11px; margin-top: 2px; }
#kg-zoom {
  position: absolute;
  top: 12px;
  right: 12px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  z-index: 10;
}
.kg-zb {
  width: 26px; height: 26px;
  background: rgba(10, 10, 24, 0.9);
  border: 1px solid #2a2a4a;
  border-radius: 4px;
  color: #777;
  font-size: 15px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  user-select: none;
}
.kg-zb:hover { background: rgba(91, 106, 240, 0.2); color: #c0c8ff; }
/* Fullscreen / expanded state */
#kg-wrap.kg-expanded {
  position: fixed !important;
  inset: 0 !important;
  z-index: 9999 !important;
  border-radius: 0 !important;
  margin: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
}
#kg-wrap.kg-expanded #cy,
#kg-wrap:fullscreen #cy {
  height: calc(100vh - 48px) !important;
  min-height: unset !important;
}
#kg-wrap:fullscreen {
  border-radius: 0;
  border: none;
  width: 100vw;
  height: 100vh;
}
#kg-loading {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #444;
  font-size: 13px;
  background: #0d0d1a;
  z-index: 5;
}
</style>

<div id="kg-wrap" markdown="0">
  <div id="kg-bar">
    <input id="kg-search" placeholder="🔍  Search pages…" type="text" autocomplete="off" />
    <div id="kg-chips"></div>
    <span id="kg-stats"></span>
  </div>
  <div id="cy"></div>
  <div id="kg-loading">Loading graph…</div>
  <div id="kg-legend"><h4>Sections</h4><div id="kg-leg-items"></div></div>
  <div id="kg-tip">
    <b id="tt-title"></b>
    <div class="tt-sec" id="tt-sec"></div>
    <div class="tt-deg" id="tt-deg"></div>
  </div>
  <div id="kg-zoom">
    <div class="kg-zb" id="kz-in" title="Zoom in">+</div>
    <div class="kg-zb" id="kz-out" title="Zoom out">−</div>
    <div class="kg-zb" id="kz-fit" title="Fit all">⊙</div>
    <div class="kg-zb" id="kz-fs" title="Full screen">⤢</div>
  </div>
</div>

{% raw %}
<script>
(function () {
  var cyEl = document.getElementById('cy');
  if (!cyEl) return;

  var COLORS = {
    Concepts: '#5b6af0', Architecture: '#5bbff0', DesignPatterns: '#7c5bf0',
    AgenticFrameworks: '#f0875b', AgenticTechStack: '#f0c05b',
    AgentPlatforms: '#e05bb8', WorkflowBuilders: '#40c8a0',
    Standards: '#5bf0a0', ReferenceArchitecture: '#a05bf0',
    ContextEngineering: '#e05b5b', PromptEngineering: '#f07a5b',
    AgentMemory: '#f05b8a', EvaluationFrameworks: '#5b8af0',
    Benchmarks: '#5baaf0', Observability: '#5bd080',
    SecurityFrameworks: '#e0c040', AgentOps: '#c05bf0',
    MaturityModels: '#40b8e0', Marketplace: '#f0a05b',
    RAG: '#6b7af0', ProductionBestPractices: '#e04060',
    AllThingsAnthropic: '#d05bf0', AllThingsGoogle: '#40c0f0',
    AllThingsMicrosoft: '#5b80f0', AllThingsOpenAI: '#40e0b0',
    Introduction: '#888888'
  };

  function colorFor(sec) { return COLORS[sec] || '#888'; }

  function loadCytoscape(cb) {
    if (window.cytoscape) { cb(); return; }
    var s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/cytoscape@3.29.2/dist/cytoscape.min.js';
    s.onload = cb;
    s.onerror = function () {
      document.getElementById('kg-loading').textContent = 'Failed to load Cytoscape.js. Check your network connection.';
    };
    document.head.appendChild(s);
  }

  function buildChips(sections, activeFilters, cy) {
    var chipsDiv = document.getElementById('kg-chips');
    sections.forEach(function (sec) {
      var chip = document.createElement('span');
      chip.className = 'kg-chip on';
      chip.dataset.section = sec;
      var dot = document.createElement('span');
      dot.className = 'dot';
      dot.style.background = colorFor(sec);
      chip.appendChild(dot);
      chip.appendChild(document.createTextNode(sec.replace('AllThings', '')));
      chip.addEventListener('click', function () {
        if (activeFilters[sec]) {
          delete activeFilters[sec];
          chip.classList.remove('on');
        } else {
          activeFilters[sec] = true;
          chip.classList.add('on');
        }
        applyFilter(cy, activeFilters);
      });
      chipsDiv.appendChild(chip);
    });
  }

  function buildLegend(sections) {
    var legDiv = document.getElementById('kg-leg-items');
    sections.forEach(function (sec) {
      var row = document.createElement('div');
      row.className = 'kg-leg-row';
      var dot = document.createElement('span');
      dot.className = 'kg-leg-dot';
      dot.style.background = colorFor(sec);
      row.appendChild(dot);
      row.appendChild(document.createTextNode(sec));
      legDiv.appendChild(row);
    });
  }

  function applyFilter(cy, activeFilters) {
    cy.batch(function () {
      cy.nodes().forEach(function (n) {
        n.style('display', activeFilters[n.data('section')] ? 'element' : 'none');
      });
      cy.edges().forEach(function (e) {
        var show = activeFilters[e.source().data('section')] &&
                   activeFilters[e.target().data('section')];
        e.style('display', show ? 'element' : 'none');
      });
    });
  }

  function attachSearch(cy) {
    document.getElementById('kg-search').addEventListener('input', function () {
      var q = this.value.toLowerCase().trim();
      cy.batch(function () {
        if (!q) {
          cy.elements().removeClass('kg-dimmed kg-hi');
          return;
        }
        cy.nodes().forEach(function (n) {
          var match = n.data('label').toLowerCase().indexOf(q) !== -1 ||
                      n.data('section').toLowerCase().indexOf(q) !== -1;
          n.removeClass('kg-dimmed kg-hi');
          n.addClass(match ? 'kg-hi' : 'kg-dimmed');
        });
        cy.edges().forEach(function (e) {
          var hasHi = e.source().hasClass('kg-hi') || e.target().hasClass('kg-hi');
          e.removeClass('kg-dimmed');
          if (!hasHi) e.addClass('kg-dimmed');
        });
      });
    });
  }

  function attachTooltip(cy) {
    var tip = document.getElementById('kg-tip');
    var wrap = document.getElementById('kg-wrap');
    cy.on('mouseover', 'node', function (evt) {
      var n = evt.target;
      document.getElementById('tt-title').textContent = n.data('label');
      document.getElementById('tt-sec').textContent = n.data('section');
      var deg = n.data('degree');
      document.getElementById('tt-deg').textContent =
        deg + ' connection' + (deg === 1 ? '' : 's');
      tip.style.display = 'block';
    });
    cy.on('mouseout', 'node', function () {
      tip.style.display = 'none';
    });
    cy.on('mousemove', 'node', function (evt) {
      var oe = evt.originalEvent;
      var rect = wrap.getBoundingClientRect();
      var x = oe.clientX - rect.left + 14;
      var y = oe.clientY - rect.top - 10;
      if (x + 240 > rect.width) x = oe.clientX - rect.left - 244;
      tip.style.left = x + 'px';
      tip.style.top = y + 'px';
    });
  }

  function attachNav(cy) {
    cy.on('tap', 'node', function (evt) {
      var path = evt.target.data('path');
      if (path) window.location.href = '../' + path;
    });
    cy.on('mouseover', 'node', function () { cyEl.style.cursor = 'pointer'; });
    cy.on('mouseout',  'node', function () { cyEl.style.cursor = 'default'; });
  }

  function attachZoom(cy) {
    document.getElementById('kz-in').addEventListener('click', function () {
      cy.animate({ zoom: cy.zoom() * 1.25, duration: 150 });
    });
    document.getElementById('kz-out').addEventListener('click', function () {
      cy.animate({ zoom: cy.zoom() * 0.8, duration: 150 });
    });
    document.getElementById('kz-fit').addEventListener('click', function () {
      cy.fit(undefined, 30);
    });
  }

  function attachFullscreen(cy) {
    var btn  = document.getElementById('kz-fs');
    var wrap = document.getElementById('kg-wrap');

    function onEnter() {
      btn.textContent = '⤡';
      btn.title = 'Exit full screen';
      setTimeout(function () { cy.resize(); cy.fit(undefined, 30); }, 80);
    }
    function onExit() {
      btn.textContent = '⤢';
      btn.title = 'Full screen';
      setTimeout(function () { cy.resize(); cy.fit(undefined, 30); }, 80);
    }

    btn.addEventListener('click', function () {
      if (document.fullscreenEnabled) {
        if (!document.fullscreenElement) {
          wrap.requestFullscreen().catch(function () {
            wrap.classList.add('kg-expanded');
            onEnter();
          });
        } else {
          document.exitFullscreen();
        }
      } else {
        wrap.classList.toggle('kg-expanded');
        wrap.classList.contains('kg-expanded') ? onEnter() : onExit();
      }
    });

    document.addEventListener('fullscreenchange', function () {
      document.fullscreenElement ? onEnter() : onExit();
    });
  }

  function initGraph(data) {
    var nodes = data.nodes;
    var edges = data.edges;
    var sections = [];
    var seen = {};
    nodes.forEach(function (n) {
      if (!seen[n.section]) { seen[n.section] = true; sections.push(n.section); }
    });
    sections.sort();

    var activeFilters = {};
    sections.forEach(function (s) { activeFilters[s] = true; });

    buildChips(sections, activeFilters, null);
    buildLegend(sections);
    document.getElementById('kg-stats').textContent =
      nodes.length + ' nodes · ' + edges.length + ' edges';

    var cy = window.cytoscape({
      container: cyEl,
      elements: {
        nodes: nodes.map(function (n) {
          return { data: {
            id: n.id, label: n.label, section: n.section,
            path: n.path, degree: n.degree, color: colorFor(n.section)
          }};
        }),
        edges: edges.map(function (e, i) {
          return { data: { id: 'e' + i, source: e.source, target: e.target }};
        })
      },
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'width':  'mapData(degree, 0, 10, 14, 40)',
            'height': 'mapData(degree, 0, 10, 14, 40)',
            'label': '',
            'font-size': '9px',
            'color': '#ccc',
            'text-valign': 'bottom',
            'text-margin-y': '3px',
            'text-outline-width': '2px',
            'text-outline-color': '#0d0d1a',
            'border-width': 0,
            'opacity': 0.9
          }
        },
        {
          selector: 'node[degree >= 3]',
          style: { 'label': 'data(label)' }
        },
        {
          selector: 'node:selected',
          style: { 'border-width': 2, 'border-color': '#fff', 'opacity': 1 }
        },
        {
          selector: 'node.kg-hi',
          style: { 'border-width': 2, 'border-color': '#fff', 'opacity': 1 }
        },
        {
          selector: 'node.kg-dimmed',
          style: { 'opacity': 0.1 }
        },
        {
          selector: 'edge',
          style: {
            'width': 1,
            'line-color': '#3a3a7a',
            'opacity': 0.45,
            'curve-style': 'bezier'
          }
        },
        {
          selector: 'edge.kg-dimmed',
          style: { 'opacity': 0.04 }
        }
      ],
      layout: {
        name: 'cose',
        animate: false,
        randomize: true,
        nodeRepulsion: function () { return 450000; },
        nodeOverlap: 12,
        idealEdgeLength: function () { return 70; },
        edgeElasticity: function () { return 200; },
        gravity: 60,
        numIter: 1500,
        initialTemp: 250,
        coolingFactor: 0.95,
        minTemp: 1,
        fit: true,
        padding: 24
      },
      userZoomingEnabled: true,
      userPanningEnabled: true,
      boxSelectionEnabled: false,
      minZoom: 0.08,
      maxZoom: 6
    });

    // Re-wire chips now that cy exists
    document.querySelectorAll('.kg-chip').forEach(function (chip) {
      chip.onclick = function () {
        var sec = chip.dataset.section;
        if (activeFilters[sec]) {
          delete activeFilters[sec];
          chip.classList.remove('on');
        } else {
          activeFilters[sec] = true;
          chip.classList.add('on');
        }
        applyFilter(cy, activeFilters);
      };
    });

    attachSearch(cy);
    attachTooltip(cy);
    attachNav(cy);
    attachZoom(cy);
    attachFullscreen(cy);

    document.getElementById('kg-loading').style.display = 'none';
  }

  loadCytoscape(function () {
    fetch('../graph-data.json')
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (data) { initGraph(data); })
      .catch(function (err) {
        document.getElementById('kg-loading').textContent =
          'Could not load graph data (' + err.message + '). Run mkdocs build first.';
      });
  });
})();
</script>
{% endraw %}
