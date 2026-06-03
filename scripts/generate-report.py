#!/usr/bin/env python3
"""
CRISP Report Generator
Converts docs/ markdown files into a single beautiful self-contained HTML file.

Usage:
    python3 generate-report.py [docs_dir] [output_file]

Defaults:
    docs_dir    = ./docs
    output_file = ./crisp-report.html

Requirements:
    pip install markdown pygments
"""

import sys
import os
import re
import json
from pathlib import Path
from datetime import datetime

try:
    import markdown
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.toc import TocExtension
    from pygments.formatters import HtmlFormatter
except ImportError:
    print("Missing dependencies. Run: pip install markdown pygments")
    sys.exit(1)


# ─── Config ───────────────────────────────────────────────────────────────────

DOCS_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs")
OUTPUT_FILE = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("crisp-report.html")

# Doc display metadata: filename stem → (icon, display title, category)
DOC_META = {
    "problem-statement":     ("🎯", "Problem Statement",       "Discovery"),
    "success-metrics":       ("📊", "Success Metrics",         "Discovery"),
    "market-research":       ("🔍", "Market Research",         "Discovery"),
    "swot":                  ("⚖️",  "SWOT Analysis",           "Discovery"),
    "buy-vs-build-matrix":   ("🛒", "Buy vs Build",            "Discovery"),
    "value-proposition-canvas": ("💎", "Value Proposition",    "Discovery"),
    "stakeholder-register":  ("👥", "Stakeholder Register",    "Discovery"),
    "user-journey-map":      ("🗺️",  "User Journey Map",        "Discovery"),
    "ux-discovery":          ("🎨", "UX Discovery",            "Discovery"),
    "process-flow":          ("⚙️",  "Process Flow",            "Discovery"),
    "project-goals":         ("🏆", "Project Goals",           "Discovery"),
    "integration-map":       ("🔗", "Integration Map",         "Discovery"),
    "data-flow":             ("🌊", "Data Flow",               "Discovery"),
    "design-system":         ("🎨", "Design System",           "Spec"),
    "ux-spec":               ("📐", "UX Spec",                 "Spec"),
    "initial-backlog":       ("📋", "Initial Backlog",         "Spec"),
    "assumptions-log":       ("💭", "Assumptions Log",         "Spec"),
    "risk-assessment":       ("⚠️",  "Risk Assessment",         "Spec"),
    "mvp-prioritization":    ("🎯", "MVP Prioritization",      "Spec"),
    "sprint-plan":           ("🗓️",  "Sprint Plan",             "Spec"),
    "logging-spec":          ("📝", "Logging Spec",            "Spec"),
    "data-mapping":          ("🗄️",  "Data Mapping",            "Spec"),
    "analytics-spec":        ("📈", "Analytics Spec",          "Spec"),
    "landing-page-brief":    ("🚀", "Landing Page Brief",      "Spec"),
    "agent-security":        ("🔐", "Agent Security",          "Spec"),
    "decisions":             ("🧭", "Decisions Log",           "Spec"),
    "assumptions-log":       ("💭", "Assumptions Log",         "Spec"),
    # Archaeology docs
    "system-overview":       ("🏗️",  "System Overview",         "Archaeology"),
    "architecture-map":      ("🗺️",  "Architecture Map",        "Archaeology"),
    "tech-stack":            ("⚙️",  "Tech Stack",              "Archaeology"),
    "domain-glossary":       ("📖", "Domain Glossary",         "Archaeology"),
    "business-context":      ("💼", "Business Context",        "Archaeology"),
    "risk-register":         ("⚠️",  "Risk Register",           "Archaeology"),
    "feature-inventory":     ("🗂️",  "Feature Inventory",       "Archaeology"),
    "open-questions":        ("❓", "Open Questions",          "Archaeology"),
    "runbook-skeleton":      ("📟", "Runbook Skeleton",        "Archaeology"),
    # Execute docs
    "test-log":              ("🧪", "Test Log",                "Execute"),
}

CATEGORY_ORDER = ["Discovery", "Archaeology", "Spec", "Execute", "Other"]
CATEGORY_COLORS = {
    "Discovery":  "#6366f1",
    "Archaeology":"#f59e0b",
    "Spec":       "#10b981",
    "Execute":    "#3b82f6",
    "Other":      "#8b5cf6",
}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def extract_summary(md_text, max_chars=160):
    """Extract first meaningful paragraph as summary."""
    lines = md_text.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('|') and not line.startswith('-') and not line.startswith('_') and not line.startswith('>') and len(line) > 20:
            clean = re.sub(r'\*+|`|_+|\[([^\]]+)\]\([^)]+\)', r'\1', line)
            return clean[:max_chars] + ('…' if len(clean) > max_chars else '')
    return "No summary available."

def extract_title(md_text, fallback):
    """Extract h1 title from markdown."""
    for line in md_text.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    return fallback

def convert_md(md_text):
    """Convert markdown to HTML with syntax highlighting."""
    md = markdown.Markdown(extensions=[
        FencedCodeExtension(),
        CodeHiliteExtension(css_class='highlight', guess_lang=False),
        TableExtension(),
        TocExtension(baselevel=1),
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
    ])
    return md.convert(md_text)

def get_meta(stem):
    key = stem.lower()
    # try ai-spec- prefix
    if key.startswith('ai-spec-'):
        label = key.replace('ai-spec-', '').replace('-', ' ').title()
        return ("🤖", f"AI Spec: {label}", "Spec")
    if key.startswith('sprint-') and 'delta' in key:
        n = key.replace('sprint-', '').replace('-delta', '')
        return ("📊", f"Sprint {n} Delta", "Execute")
    if key.startswith('sprint-') and 'report' in key:
        n = key.replace('sprint-', '').replace('-report', '')
        return ("📄", f"Sprint {n} Report", "Execute")
    return DOC_META.get(key, ("📄", stem.replace('-', ' ').title(), "Other"))

def get_pygments_css():
    return HtmlFormatter(style='github-dark').get_style_defs('.highlight')


# ─── Read docs ────────────────────────────────────────────────────────────────

def load_docs(docs_dir):
    docs = []
    if not docs_dir.exists():
        print(f"Warning: {docs_dir} not found — generating empty report.")
        return docs
    for f in sorted(docs_dir.glob("*.md")):
        text = f.read_text(encoding='utf-8')
        stem = f.stem
        icon, display_title, category = get_meta(stem)
        title = extract_title(text, display_title)
        summary = extract_summary(text)
        html_body = convert_md(text)
        docs.append({
            "id": slugify(stem),
            "stem": stem,
            "title": title,
            "display_title": display_title,
            "icon": icon,
            "category": category,
            "summary": summary,
            "html_body": html_body,
        })
    return docs

def read_project_name(docs_dir):
    """Try to extract project name from crisp-state.json or problem-statement."""
    state = docs_dir.parent / "docs" / "crisp-state.json"
    if state.exists():
        try:
            data = json.loads(state.read_text())
            name = data.get("project", {})
            if isinstance(name, dict):
                name = name.get("name", "")
            if name:
                return name
        except Exception:
            pass
    ps = docs_dir / "problem-statement.md"
    if ps.exists():
        text = ps.read_text()
        title = extract_title(text, "")
        if title:
            return title
    return "CRISP Project"


# ─── HTML Template ────────────────────────────────────────────────────────────

def build_html(docs, project_name, generated_at):
    pygments_css = get_pygments_css()

    # Group by category
    by_category = {}
    for doc in docs:
        cat = doc["category"]
        by_category.setdefault(cat, []).append(doc)

    # Build cards HTML
    cards_html = ""
    for cat in CATEGORY_ORDER:
        if cat not in by_category:
            continue
        color = CATEGORY_COLORS.get(cat, "#8b5cf6")
        cards_html += f'<div class="category-section"><div class="category-label" style="--cat-color:{color}">{cat}</div><div class="card-grid">'
        for doc in by_category[cat]:
            cards_html += f'''
            <div class="card" onclick="showDoc('{doc["id"]}')" tabindex="0" onkeydown="if(event.key==='Enter')showDoc('{doc["id"]}')">
                <div class="card-icon">{doc["icon"]}</div>
                <div class="card-content">
                    <div class="card-title">{doc["display_title"]}</div>
                    <div class="card-summary">{doc["summary"]}</div>
                </div>
                <div class="card-arrow">→</div>
            </div>'''
        cards_html += '</div></div>'

    # Build doc pages HTML
    docs_html = ""
    for doc in docs:
        docs_html += f'''
        <div class="doc-page" id="doc-{doc["id"]}">
            <div class="doc-header">
                <button class="back-btn" onclick="showIndex()">← Back to overview</button>
                <div class="doc-meta">
                    <span class="doc-icon">{doc["icon"]}</span>
                    <span class="doc-category" style="--cat-color:{CATEGORY_COLORS.get(doc["category"], "#8b5cf6")}">{doc["category"]}</span>
                </div>
            </div>
            <article class="doc-body">
                {doc["html_body"]}
            </article>
        </div>'''

    doc_count = len(docs)
    categories_count = len(by_category)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project_name} — CRISP Docs</title>
<style>
/* ─── Reset & Base ─────────────────────────────────────────── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg: #0f0f13;
  --bg-surface: #16161d;
  --bg-card: #1c1c26;
  --bg-card-hover: #22222f;
  --border: #2a2a38;
  --border-subtle: #1f1f2b;
  --text-primary: #e8e8f0;
  --text-secondary: #9090a8;
  --text-muted: #5a5a72;
  --accent: #6366f1;
  --accent-glow: rgba(99,102,241,0.15);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
  --radius: 12px;
  --radius-sm: 8px;
  --shadow: 0 4px 24px rgba(0,0,0,0.4);
  --transition: 0.18s cubic-bezier(0.4, 0, 0.2, 1);
}}

html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font);
  background: var(--bg);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}}

/* ─── Layout ────────────────────────────────────────────────── */
#index-view, #doc-view {{ min-height: 100vh; }}
#doc-view {{ display: none; }}

.container {{
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}}

/* ─── Header ────────────────────────────────────────────────── */
.site-header {{
  border-bottom: 1px solid var(--border-subtle);
  padding: 32px 0 28px;
  margin-bottom: 48px;
  background: linear-gradient(180deg, rgba(99,102,241,0.04) 0%, transparent 100%);
}}
.header-inner {{
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}}
.header-brand {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.crisp-badge {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-glow);
  border: 1px solid rgba(99,102,241,0.3);
  padding: 4px 10px;
  border-radius: 100px;
}}
.project-name {{
  font-size: 28px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}}
.header-meta {{
  font-size: 13px;
  color: var(--text-muted);
  text-align: right;
}}
.header-stats {{
  display: flex;
  gap: 20px;
  margin-top: 4px;
}}
.stat {{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}}
.stat-value {{
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1;
}}
.stat-label {{
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}}

/* ─── Category sections ─────────────────────────────────────── */
.category-section {{ margin-bottom: 48px; }}
.category-label {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cat-color, var(--accent));
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.category-label::after {{
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border-subtle);
}}

/* ─── Cards ─────────────────────────────────────────────────── */
.card-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 12px;
}}
.card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  cursor: pointer;
  display: flex;
  align-items: flex-start;
  gap: 14px;
  transition: background var(--transition), border-color var(--transition), transform var(--transition), box-shadow var(--transition);
  outline: none;
  position: relative;
  overflow: hidden;
}}
.card::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, var(--accent-glow) 0%, transparent 60%);
  opacity: 0;
  transition: opacity var(--transition);
}}
.card:hover, .card:focus {{
  background: var(--bg-card-hover);
  border-color: rgba(99,102,241,0.4);
  transform: translateY(-2px);
  box-shadow: var(--shadow);
}}
.card:hover::before, .card:focus::before {{ opacity: 1; }}
.card-icon {{
  font-size: 24px;
  line-height: 1;
  flex-shrink: 0;
  margin-top: 2px;
}}
.card-content {{ flex: 1; min-width: 0; }}
.card-title {{
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 6px;
  line-height: 1.3;
}}
.card-summary {{
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}
.card-arrow {{
  color: var(--text-muted);
  font-size: 16px;
  flex-shrink: 0;
  transition: color var(--transition), transform var(--transition);
  margin-top: 2px;
}}
.card:hover .card-arrow, .card:focus .card-arrow {{
  color: var(--accent);
  transform: translateX(3px);
}}

/* ─── Footer ────────────────────────────────────────────────── */
.site-footer {{
  border-top: 1px solid var(--border-subtle);
  padding: 24px 0;
  margin-top: 64px;
  text-align: center;
  font-size: 12px;
  color: var(--text-muted);
}}

/* ─── Doc view ──────────────────────────────────────────────── */
.doc-page {{
  max-width: 820px;
  margin: 0 auto;
  padding: 40px 24px 80px;
}}
.doc-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 40px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-subtle);
  flex-wrap: wrap;
  gap: 12px;
}}
.back-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  font-size: 14px;
  font-family: var(--font);
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition);
}}
.back-btn:hover {{
  background: var(--bg-card-hover);
  color: var(--text-primary);
  border-color: rgba(99,102,241,0.4);
}}
.doc-meta {{
  display: flex;
  align-items: center;
  gap: 10px;
}}
.doc-icon {{ font-size: 20px; }}
.doc-category {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cat-color, var(--accent));
  background: rgba(99,102,241,0.1);
  padding: 4px 10px;
  border-radius: 100px;
}}

/* ─── Doc body (typography) ──────────────────────────────────── */
.doc-body {{
  font-size: 16px;
  line-height: 1.75;
  color: var(--text-primary);
}}
.doc-body h1 {{
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  margin-bottom: 8px;
  line-height: 1.2;
}}
.doc-body h2 {{
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  margin: 40px 0 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border-subtle);
}}
.doc-body h3 {{
  font-size: 17px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 28px 0 12px;
}}
.doc-body h4 {{
  font-size: 15px;
  font-weight: 600;
  color: var(--text-secondary);
  margin: 20px 0 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}}
.doc-body p {{ margin-bottom: 16px; }}
.doc-body ul, .doc-body ol {{
  margin: 12px 0 16px 24px;
}}
.doc-body li {{ margin-bottom: 6px; }}
.doc-body li > ul, .doc-body li > ol {{ margin-top: 6px; margin-bottom: 4px; }}
.doc-body strong {{ color: var(--text-primary); font-weight: 600; }}
.doc-body em {{ color: var(--text-secondary); }}
.doc-body a {{
  color: #818cf8;
  text-decoration: underline;
  text-decoration-color: rgba(129,140,248,0.4);
  text-underline-offset: 3px;
  transition: color var(--transition);
}}
.doc-body a:hover {{ color: #a5b4fc; }}

/* ─── Blockquote ────────────────────────────────────────────── */
.doc-body blockquote {{
  border-left: 3px solid var(--accent);
  background: rgba(99,102,241,0.06);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 14px 20px;
  margin: 20px 0;
  color: var(--text-secondary);
  font-style: italic;
}}
.doc-body blockquote p {{ margin: 0; }}

/* ─── Tables ────────────────────────────────────────────────── */
.doc-body table {{
  width: 100%;
  border-collapse: collapse;
  margin: 24px 0;
  font-size: 14px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1px solid var(--border);
}}
.doc-body thead {{
  background: var(--bg-surface);
}}
.doc-body th {{
  padding: 12px 16px;
  text-align: left;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
}}
.doc-body td {{
  padding: 11px 16px;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  vertical-align: top;
}}
.doc-body tr:last-child td {{ border-bottom: none; }}
.doc-body tr:hover td {{ background: var(--bg-surface); }}

/* ─── Code ──────────────────────────────────────────────────── */
.doc-body code {{
  font-family: var(--font-mono);
  font-size: 0.85em;
  background: rgba(255,255,255,0.07);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 6px;
  color: #a5b4fc;
}}
.doc-body pre {{
  background: #0d0d14;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 20px;
  overflow-x: auto;
  margin: 20px 0;
  font-size: 13px;
  line-height: 1.6;
}}
.doc-body pre code {{
  background: none;
  border: none;
  padding: 0;
  color: inherit;
  font-size: inherit;
}}
/* Checkboxes */
.doc-body ul li input[type="checkbox"] {{
  margin-right: 8px;
  accent-color: var(--accent);
}}

/* ─── Pygments syntax highlighting ──────────────────────────── */
{pygments_css}
.highlight {{ background: #0d0d14 !important; border-radius: var(--radius-sm); }}

/* ─── Animations ────────────────────────────────────────────── */
@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(8px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
.fade-in {{ animation: fadeIn 0.22s ease forwards; }}

/* ─── Scrollbar ─────────────────────────────────────────────── */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--text-muted); }}

/* ─── Responsive ────────────────────────────────────────────── */
@media (max-width: 600px) {{
  .card-grid {{ grid-template-columns: 1fr; }}
  .project-name {{ font-size: 22px; }}
  .header-stats {{ gap: 12px; }}
  .doc-body h1 {{ font-size: 24px; }}
  .doc-body h2 {{ font-size: 18px; }}
}}
</style>
</head>
<body>

<!-- ═══ INDEX VIEW ═══════════════════════════════════════════════════════════ -->
<div id="index-view">
  <div class="site-header">
    <div class="container">
      <div class="header-inner">
        <div class="header-brand">
          <span class="crisp-badge">CRISP</span>
          <h1 class="project-name">{project_name}</h1>
        </div>
        <div class="header-meta">
          <div>Generated {generated_at}</div>
          <div class="header-stats">
            <div class="stat">
              <span class="stat-value">{doc_count}</span>
              <span class="stat-label">Documents</span>
            </div>
            <div class="stat">
              <span class="stat-value">{categories_count}</span>
              <span class="stat-label">Sections</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    {cards_html}
  </div>

  <div class="container">
    <div class="site-footer">
      Generated by CRISP Report Generator · {generated_at}
    </div>
  </div>
</div>

<!-- ═══ DOC VIEW ════════════════════════════════════════════════════════════ -->
<div id="doc-view">
  {docs_html}
</div>

<script>
const indexView = document.getElementById('index-view');
const docView = document.getElementById('doc-view');
let currentDoc = null;

function showDoc(id) {{
  // Hide all doc pages
  document.querySelectorAll('.doc-page').forEach(p => p.style.display = 'none');
  // Show the target
  const page = document.getElementById('doc-' + id);
  if (!page) return;
  page.style.display = 'block';
  page.classList.remove('fade-in');
  void page.offsetWidth; // reflow
  page.classList.add('fade-in');
  // Switch views
  indexView.style.display = 'none';
  docView.style.display = 'block';
  window.scrollTo({{ top: 0, behavior: 'instant' }});
  currentDoc = id;
  // Update browser history
  history.pushState({{ doc: id }}, '', '#' + id);
}}

function showIndex() {{
  docView.style.display = 'none';
  indexView.style.display = 'block';
  window.scrollTo({{ top: 0, behavior: 'instant' }});
  currentDoc = null;
  history.pushState({{ doc: null }}, '', window.location.pathname);
}}

// Handle browser back/forward
window.addEventListener('popstate', (e) => {{
  if (e.state && e.state.doc) {{
    showDoc(e.state.doc);
  }} else {{
    showIndex();
  }}
}});

// Handle direct URL with hash
window.addEventListener('DOMContentLoaded', () => {{
  const hash = window.location.hash.slice(1);
  if (hash) {{
    showDoc(hash);
  }}
}});

// Keyboard shortcut: Escape → back to index
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape' && currentDoc) showIndex();
}});
</script>

</body>
</html>'''


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Reading docs from: {DOCS_DIR.resolve()}")
    docs = load_docs(DOCS_DIR)

    if not docs:
        print("No markdown files found in docs/. Nothing to generate.")
        sys.exit(0)

    project_name = read_project_name(DOCS_DIR)
    generated_at = datetime.now().strftime("%B %d, %Y at %H:%M")

    print(f"Found {len(docs)} documents across {len(set(d['category'] for d in docs))} categories.")
    print(f"Project: {project_name}")

    html = build_html(docs, project_name, generated_at)
    OUTPUT_FILE.write_text(html, encoding='utf-8')

    print(f"\n✅ Report generated: {OUTPUT_FILE.resolve()}")
    print(f"   Open in browser: open {OUTPUT_FILE}")
