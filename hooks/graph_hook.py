import json
import re
from pathlib import Path

SECTION_COLORS = {
    'Concepts':                '#5b6af0',
    'Architecture':            '#5bbff0',
    'DesignPatterns':          '#7c5bf0',
    'AgenticFrameworks':       '#f0875b',
    'AgenticTechStack':        '#f0c05b',
    'AgentPlatforms':          '#e05bb8',
    'WorkflowBuilders':        '#40c8a0',
    'Standards':               '#5bf0a0',
    'ReferenceArchitecture':   '#a05bf0',
    'ContextEngineering':      '#e05b5b',
    'PromptEngineering':       '#f07a5b',
    'AgentMemory':             '#f05b8a',
    'EvaluationFrameworks':    '#5b8af0',
    'Benchmarks':              '#5baaf0',
    'Observability':           '#5bd080',
    'SecurityFrameworks':      '#e0c040',
    'AgentOps':                '#c05bf0',
    'MaturityModels':          '#40b8e0',
    'Marketplace':             '#f0a05b',
    'RAG':                     '#6b7af0',
    'ProductionBestPractices': '#e04060',
    'AllThingsAnthropic':      '#d05bf0',
    'AllThingsGoogle':         '#40c0f0',
    'AllThingsMicrosoft':      '#5b80f0',
    'AllThingsOpenAI':         '#40e0b0',
    'Introduction':            '#888888',
}

_SEE_ALSO_RE = re.compile(
    r'##\s+See\s+Also\s*\n(.*?)(?=\n##\s|\Z)', re.DOTALL | re.IGNORECASE
)
_LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


def _page_url(rel_path: Path) -> str:
    stem = rel_path.stem.lower()
    if stem in ('readme', 'index'):
        parent = str(rel_path.parent).replace('\\', '/')
        return (parent.rstrip('/') + '/') if parent != '.' else ''
    return str(rel_path.with_suffix('')).replace('\\', '/') + '/'


def on_pre_build(config):
    docs_dir = Path(config['docs_dir'])
    output_path = docs_dir / 'graph-data.json'

    nodes: dict = {}
    raw_edges: list = []

    for md_file in sorted(docs_dir.rglob('*.md')):
        rel_path = md_file.relative_to(docs_dir)
        if len(rel_path.parts) < 2:
            continue

        section = rel_path.parts[0]
        rel_str = str(rel_path).replace('\\', '/')

        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
        except OSError:
            continue

        title_m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else rel_path.stem.replace('-', ' ').title()

        nodes[rel_str] = {
            'id':      rel_str,
            'label':   title[:52],
            'section': section,
            'color':   SECTION_COLORS.get(section, '#888888'),
            'path':    _page_url(rel_path),
            'degree':  0,
        }

        m = _SEE_ALSO_RE.search(content)
        if not m:
            continue

        for link in _LINK_RE.findall(m.group(1)):
            link = link.split('#')[0].strip()
            if not link.endswith('.md') or link.startswith(('http://', 'https://')):
                continue
            try:
                target_abs = (md_file.parent / link).resolve()
                target_rel = str(
                    target_abs.relative_to(docs_dir.resolve())
                ).replace('\\', '/')
            except (ValueError, OSError):
                continue
            if target_rel != rel_str:
                raw_edges.append({'source': rel_str, 'target': target_rel})

    valid_ids = set(nodes)
    edges = [
        e for e in raw_edges
        if e['source'] in valid_ids and e['target'] in valid_ids
    ]

    for e in edges:
        nodes[e['source']]['degree'] += 1
        nodes[e['target']]['degree'] += 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps({'nodes': list(nodes.values()), 'edges': edges}, indent=2),
        encoding='utf-8',
    )
    print(
        f'[graph_hook] {len(nodes)} nodes, {len(edges)} edges'
        f' → {output_path.relative_to(docs_dir.parent)}'
    )
