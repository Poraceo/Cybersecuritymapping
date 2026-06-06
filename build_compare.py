"""
Genera Comparar_Roles.html
Vista dedicada para comparar 2 roles lado a lado (como comparador de carros).
Muestra TODOS los parametros: salario, demanda, remoto, skills, certs, etc.
Highlights:
- Items comunes en ambos roles (verde)
- Items unicos a cada rol
- URL hash support: #1,7 preselecciona los roles
"""

import json


LEVEL_LABELS = {
    'junior': 'Junior · 0-2 años',
    'mid': 'Mid-Level · 3-7 años',
    'senior': 'Senior · 5-12 años',
    'manager': 'Manager · 7-12 años',
    'executive': 'Director / C-Level · 10+ años',
}

LEVEL_COLORS = {
    'junior': '#10B981',
    'mid': '#06B6D4',
    'senior': '#F59E0B',
    'manager': '#EC4899',
    'executive': '#C084FC',
}


CSS = """
:root{
  --bg-deep:#0A0E1A;--bg-alt:#0E1322;--bg-card:#1A2236;--bg-elevated:#222B42;
  --border:#2A3149;--border-bright:#3A4566;
  --text-primary:#F8FAFC;--text-secondary:#CBD5E1;--text-muted:#94A3B8;--text-dim:#64748B;
  --gold:#F59E0B;--mint:#10B981;--cyan:#06B6D4;--magenta:#EC4899;--violet:#C084FC;
  --col-a:#06B6D4;--col-b:#EC4899;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg-deep);color:var(--text-primary);font-family:'Sora',sans-serif;min-height:100vh}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 1200px 800px at 20% 0%,rgba(6,182,212,0.06),transparent 60%),radial-gradient(ellipse 1200px 800px at 80% 100%,rgba(236,72,153,0.05),transparent 60%);pointer-events:none;z-index:0}

.app{position:relative;z-index:1;max-width:1600px;margin:0 auto;padding:32px 36px 60px}

/* === TOP NAV === */
.top{display:flex;justify-content:space-between;align-items:center;padding-bottom:20px;margin-bottom:24px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:16px}
.brand{display:flex;align-items:center;gap:14px;font-family:'Bricolage Grotesque',serif;font-weight:700;font-size:22px;letter-spacing:-0.02em}
.brand-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--col-a),var(--col-b));border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:800;font-size:18px;color:var(--bg-deep)}
.brand em{font-style:italic;color:var(--gold)}
.brand-meta{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase;margin-top:2px}
.nav-links{display:flex;gap:10px;flex-wrap:wrap}
.nav-link{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);text-decoration:none;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s}
.nav-link:hover{background:var(--bg-elevated);color:var(--gold);border-color:var(--gold)}

/* === HERO === */
.hero{margin-bottom:24px}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:12px}
.eyebrow::before{content:'';width:28px;height:1px;background:var(--gold)}
.title{font-family:'Bricolage Grotesque',serif;font-size:clamp(32px,4vw,48px);font-weight:700;line-height:1;letter-spacing:-0.035em;margin-bottom:10px}
.title em{font-style:italic;color:var(--gold);font-weight:500}
.subtitle{color:var(--text-secondary);font-size:14px;max-width:800px;line-height:1.55}

/* === SELECTORES === */
.selectors{display:grid;grid-template-columns:1fr auto 1fr;gap:14px;margin-bottom:28px;align-items:stretch}
.selector{background:var(--bg-card);border:2px solid var(--border);border-radius:14px;padding:14px 16px;position:relative;transition:border 0.2s}
.selector.col-a{border-left:4px solid var(--col-a)}
.selector.col-b{border-left:4px solid var(--col-b)}
.selector-label{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.selector.col-a .selector-label{color:var(--col-a)}
.selector.col-b .selector-label{color:var(--col-b)}
.selector-label::before{content:'';width:8px;height:8px;border-radius:50%;background:currentColor}
.selector select{width:100%;background:var(--bg-deep);border:1px solid var(--border);border-radius:8px;padding:10px 14px;color:var(--text-primary);font-family:'Sora',sans-serif;font-size:14px;font-weight:600;outline:none;cursor:pointer;transition:border 0.2s}
.selector select:hover,.selector select:focus{border-color:var(--gold)}
.selector-info{margin-top:10px;display:flex;gap:10px;flex-wrap:wrap;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted)}
.selector-info span{padding:3px 8px;background:var(--bg-deep);border-radius:100px;text-transform:uppercase;letter-spacing:0.05em}
.vs-mark{display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque',serif;font-size:24px;font-weight:700;color:var(--gold);font-style:italic;letter-spacing:-0.05em;padding:0 8px}

/* === SWAP BUTTON === */
.swap-bar{display:flex;justify-content:center;margin-bottom:18px}
.swap-btn{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);background:var(--bg-card);border:1px solid var(--border);border-radius:100px;padding:8px 18px;cursor:pointer;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s;display:flex;align-items:center;gap:8px}
.swap-btn:hover{background:var(--bg-elevated);color:var(--gold);border-color:var(--gold)}

/* === EMPTY STATE === */
.empty-state{padding:80px 20px;text-align:center;color:var(--text-muted);background:var(--bg-card);border:1px dashed var(--border);border-radius:14px}
.empty-state h3{font-family:'Bricolage Grotesque',serif;font-size:24px;color:var(--text-primary);margin-bottom:8px;letter-spacing:-0.02em}
.empty-state p{font-size:14px;line-height:1.5}

/* === COMPARISON ROWS === */
.compare-body{display:flex;flex-direction:column;gap:20px}
.compare-row{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;overflow:hidden}
.compare-row-header{padding:12px 20px;background:rgba(245,158,11,0.06);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}
.compare-row-title{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);font-weight:700;display:flex;align-items:center;gap:10px}
.compare-row-title .icon{font-size:14px}
.compare-row-body{display:grid;grid-template-columns:1fr 1fr;gap:0}
.cell{padding:18px 22px;display:flex;flex-direction:column;gap:10px;position:relative}
.cell-a{border-right:1px solid var(--border);border-left:3px solid var(--col-a)}
.cell-b{border-left:3px solid var(--col-b)}

/* Tipos de contenido en las celdas */
.cell-text{font-size:14px;color:var(--text-primary);line-height:1.55}
.cell-text.big{font-family:'Bricolage Grotesque',serif;font-size:22px;font-weight:700;letter-spacing:-0.02em;line-height:1.15}
.cell-text.salary{font-family:'JetBrains Mono',monospace;font-size:18px;font-weight:700;color:var(--gold);letter-spacing:-0.01em}
.cell-text.demand{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:700;letter-spacing:0.05em;text-transform:uppercase}
.cell-text.demand.high{color:var(--mint)}
.cell-text.demand.veryhigh{color:var(--mint)}
.cell-text.demand.explosive{color:var(--magenta)}
.cell-text.demand.medium{color:var(--cyan)}
.cell-empty{color:var(--text-dim);font-style:italic;font-size:13px}

/* Lists con highlighting */
.cell-chips{display:flex;flex-wrap:wrap;gap:6px}
.chip-c{font-family:'Sora',sans-serif;font-size:12px;padding:5px 11px;border-radius:100px;background:rgba(255,255,255,0.04);border:1px solid var(--border);color:var(--text-secondary);display:inline-flex;align-items:center;gap:5px;line-height:1.3}
.chip-c.shared{background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.4);color:var(--mint);font-weight:600}
.chip-c.shared::before{content:'✓';font-size:9px;font-weight:700}
.chip-c.unique-a{border-color:rgba(6,182,212,0.3);color:var(--col-a)}
.chip-c.unique-b{border-color:rgba(236,72,153,0.3);color:var(--col-b)}

/* Header de columna dentro de filas */
.cell-col-label{position:absolute;top:6px;right:8px;font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--text-dim);font-weight:700}
.cell-a .cell-col-label{color:rgba(6,182,212,0.5)}
.cell-b .cell-col-label{color:rgba(236,72,153,0.5)}

/* Compare summary */
.summary-row{background:linear-gradient(135deg,rgba(6,182,212,0.06),rgba(236,72,153,0.06));border:1px solid var(--border-bright);border-radius:14px;padding:18px 22px;margin-bottom:8px;display:grid;grid-template-columns:auto 1fr auto 1fr auto;gap:14px;align-items:center}
.summary-num{font-family:'Bricolage Grotesque',serif;font-size:32px;font-weight:700;color:var(--gold);letter-spacing:-0.03em;line-height:1}
.summary-label{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:0.15em;text-transform:uppercase;color:var(--text-muted);margin-top:3px}
.summary-divider{width:1px;height:40px;background:var(--border)}

/* Roles relacionados */
.related-chips{display:flex;flex-wrap:wrap;gap:6px}
.related-chip{font-family:'JetBrains Mono',monospace;font-size:11px;padding:5px 11px;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px;color:var(--text-secondary);cursor:pointer;text-decoration:none;transition:all 0.15s}
.related-chip:hover{border-color:var(--gold);color:var(--gold)}

/* Mobile */
@media (max-width:900px){
  .selectors{grid-template-columns:1fr;gap:10px}
  .vs-mark{padding:8px 0}
  .compare-row-body{grid-template-columns:1fr}
  .cell-a{border-right:none;border-bottom:1px solid var(--border)}
  .summary-row{grid-template-columns:1fr 1fr;gap:10px;text-align:center}
  .summary-divider{display:none}
}

/* CTA box */
.cta-box{margin-top:20px;background:var(--bg-card);border:1px solid var(--border);border-left:4px solid var(--gold);border-radius:12px;padding:18px 22px;display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.cta-box-text{font-size:13px;color:var(--text-secondary);line-height:1.5}
.cta-box-text strong{color:var(--text-primary)}
.cta-box a{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);background:rgba(245,158,11,0.1);border:1px solid var(--gold);border-radius:8px;padding:8px 14px;text-decoration:none;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s;white-space:nowrap}
.cta-box a:hover{background:var(--gold);color:var(--bg-deep)}
"""


def build_compare(data, output_path):
    roles = data['roles']
    cats = data['categories']

    # Datos serializados para JS
    roles_data = []
    for r in roles:
        # Convertir certsEnriched para que JS lo pueda usar
        certs_simple = []
        for c in r.get('certsEnriched', []):
            if isinstance(c, dict):
                certs_simple.append({
                    'displayName': c.get('displayName', ''),
                    'info': c.get('info')
                })
            else:
                certs_simple.append({'displayName': str(c), 'info': None})

        roles_data.append({
            'id': r['id'],
            'roleEN': r.get('roleEN', ''),
            'roleES': r.get('roleES', ''),
            'cat': r.get('cat', ''),
            'level': r.get('level', ''),
            'years': r.get('years', ''),
            'synonyms': r.get('synonyms', ''),
            'salaryMonth': r.get('salaryMonth', ''),
            'salaryYear': r.get('salaryYear', ''),
            'demand': r.get('demand', ''),
            'remote': r.get('remote', ''),
            'description': r.get('description', ''),
            'hardSkills': r.get('hardSkills', []),
            'tools': r.get('tools', []),
            'softSkills': r.get('softSkills', []),
            'certs': r.get('certs', []),
            'certsEnriched': certs_simple,
            'howToStart': r.get('howToStart', ''),
            'growth': r.get('growth', ''),
            'markets': r.get('markets', ''),
            'related': r.get('related', []),
            'projection': r.get('projection', ''),
            'trend2026': r.get('trend2026', ''),
            'salaryJump': r.get('salaryJump', ''),
            'difficulty': r.get('difficulty', ''),
        })

    # Categorias para mostrar labels
    cats_data = {k: {'label': v.get('label', k), 'color': v.get('color', '#94A3B8')} for k, v in cats.items()}

    # Generar opciones del dropdown ordenadas por ID
    options_html = []
    for r in sorted(roles, key=lambda x: x['id']):
        cat_label = cats.get(r['cat'], {}).get('label', r['cat']).split('/')[0].strip()
        options_html.append(f'<option value="{r["id"]}">#{r["id"]:02d} · {r["roleEN"]} ({cat_label})</option>')
    options_str = '\n'.join(options_html)

    # Datos serializados
    roles_json = json.dumps(roles_data, ensure_ascii=False)
    cats_json = json.dumps(cats_data, ensure_ascii=False)
    level_labels_json = json.dumps(LEVEL_LABELS, ensure_ascii=False)
    level_colors_json = json.dumps(LEVEL_COLORS, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Comparar Roles · Cyber.map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Sora:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="app">
  <div class="top">
    <div class="brand">
      <div class="brand-mark">⚖</div>
      <div>
        <div>Cyber<em>.map</em> <span style="font-size:13px;color:var(--text-muted);font-weight:400;margin-left:6px">/ Comparar roles</span></div>
        <div class="brand-meta">COMPARADOR LADO A LADO · {len(roles)} ROLES DISPONIBLES</div>
      </div>
    </div>
    <div class="nav-links">
      <a class="nav-link" href="Mapa_General_Carreras.html">← Mapa general</a>
      <a class="nav-link" href="Mapa_Carreras_Ciberseguridad.html">← Detalle por rol</a>
      <a class="nav-link" href="Catalogo_Certificaciones.html">📜 Catálogo de certs</a>
    </div>
  </div>

  <div class="hero">
    <div class="eyebrow">COMPARADOR DE CARRERAS · LADO A LADO</div>
    <h1 class="title">¿Cuál te conviene <em>más</em>?</h1>
    <p class="subtitle">Elegí dos roles para verlos uno al lado del otro: salarios, demanda, skills, certs, trabajo remoto y todos los demás datos. Las skills que comparten ambos roles aparecen marcadas en verde <span style="color:var(--mint);font-weight:600">✓</span> — eso te dice qué transferís de un rol al otro.</p>
  </div>

  <!-- Selectores -->
  <div class="selectors">
    <div class="selector col-a">
      <div class="selector-label">Rol A</div>
      <select id="selectA">
        <option value="">— Seleccioná un rol —</option>
        {options_str}
      </select>
      <div class="selector-info" id="infoA"></div>
    </div>
    <div class="vs-mark">vs.</div>
    <div class="selector col-b">
      <div class="selector-label">Rol B</div>
      <select id="selectB">
        <option value="">— Seleccioná un rol —</option>
        {options_str}
      </select>
      <div class="selector-info" id="infoB"></div>
    </div>
  </div>

  <div class="swap-bar">
    <button class="swap-btn" id="swapBtn">⇄ Intercambiar lados</button>
  </div>

  <!-- Contenido dinamico -->
  <div id="comparisonContent">
    <div class="empty-state">
      <h3>Seleccioná dos roles para empezar</h3>
      <p>Elegí un rol en cada lado para ver la comparación completa: salarios, skills, certificaciones, mercados y más.</p>
    </div>
  </div>
</div>

<script>
  const ROLES = {roles_json};
  const CATS = {cats_json};
  const LEVELS = {level_labels_json};
  const LEVEL_COLORS = {level_colors_json};
  const ROLES_BY_ID = {{}};
  ROLES.forEach(r => ROLES_BY_ID[r.id] = r);

  // === Helpers ===
  function escHtml(s) {{
    if (s === null || s === undefined) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }}

  function normalize(s) {{
    return String(s||'').replace(/⭐/g,'').trim().toLowerCase();
  }}

  function demandClass(s) {{
    const u = (s||'').toUpperCase();
    if (u.includes('EXPLOSIVA')) return 'explosive';
    if (u.includes('MUY ALTA')) return 'veryhigh';
    if (u.includes('ALTA')) return 'high';
    if (u.includes('MEDIA')) return 'medium';
    return '';
  }}

  // Render de listas con highlight de items comunes
  function renderList(itemsA, itemsB, side) {{
    const items = side === 'a' ? itemsA : itemsB;
    if (!items || items.length === 0) {{
      return '<div class="cell-empty">No especificado</div>';
    }}
    const setA = new Set((itemsA||[]).map(normalize));
    const setB = new Set((itemsB||[]).map(normalize));
    const chips = items.map(it => {{
      const n = normalize(it);
      const inBoth = setA.has(n) && setB.has(n);
      const cls = inBoth ? 'shared' : (side === 'a' ? 'unique-a' : 'unique-b');
      return `<span class="chip-c ${{cls}}">${{escHtml(it)}}</span>`;
    }}).join('');
    return `<div class="cell-chips">${{chips}}</div>`;
  }}

  // Render row con dos celdas
  function renderRow(icon, title, contentA, contentB) {{
    return `<div class="compare-row">
      <div class="compare-row-header">
        <div class="compare-row-title"><span class="icon">${{icon}}</span> ${{title}}</div>
      </div>
      <div class="compare-row-body">
        <div class="cell cell-a"><div class="cell-col-label">A</div>${{contentA}}</div>
        <div class="cell cell-b"><div class="cell-col-label">B</div>${{contentB}}</div>
      </div>
    </div>`;
  }}

  // Render text simple
  function renderText(text, klass) {{
    if (!text) return '<div class="cell-empty">No especificado</div>';
    return `<div class="cell-text ${{klass||''}}">${{escHtml(text)}}</div>`;
  }}

  // Render demand con clase
  function renderDemand(text) {{
    if (!text) return '<div class="cell-empty">—</div>';
    return `<div class="cell-text demand ${{demandClass(text)}}">${{escHtml(text)}}</div>`;
  }}

  // Roles relacionados clicables
  function renderRelated(ids) {{
    if (!ids || ids.length === 0) return '<div class="cell-empty">Ninguno especificado</div>';
    const chips = ids.map(id => {{
      const r = ROLES_BY_ID[id];
      if (!r) return '';
      return `<a class="related-chip" href="Mapa_Carreras_Ciberseguridad.html#role-${{id}}">#${{String(id).padStart(2,'0')}} ${{escHtml(r.roleEN)}}</a>`;
    }}).join('');
    return `<div class="related-chips">${{chips}}</div>`;
  }}

  // Update selector info badges
  function updateInfo(role, infoEl) {{
    if (!role) {{ infoEl.innerHTML = ''; return; }}
    const cat = CATS[role.cat] || {{label: role.cat}};
    infoEl.innerHTML = `
      <span>${{escHtml(cat.label)}}</span>
      <span>${{escHtml(LEVELS[role.level] || role.level)}}</span>
    `;
  }}

  // Calcular skills comunes para summary
  function countShared(a, b, field) {{
    if (!a || !b) return 0;
    const setA = new Set((a[field]||[]).map(normalize));
    const setB = new Set((b[field]||[]).map(normalize));
    let count = 0;
    setA.forEach(x => {{ if (setB.has(x)) count++; }});
    return count;
  }}

  // Render principal de comparacion
  function render() {{
    const idA = parseInt(document.getElementById('selectA').value);
    const idB = parseInt(document.getElementById('selectB').value);
    const roleA = ROLES_BY_ID[idA];
    const roleB = ROLES_BY_ID[idB];

    updateInfo(roleA, document.getElementById('infoA'));
    updateInfo(roleB, document.getElementById('infoB'));

    // Actualizar URL hash
    if (roleA && roleB) {{
      window.history.replaceState(null, '', `#${{idA}},${{idB}}`);
    }} else if (roleA) {{
      window.history.replaceState(null, '', `#${{idA}}`);
    }}

    const out = document.getElementById('comparisonContent');

    if (!roleA || !roleB) {{
      out.innerHTML = `<div class="empty-state">
        <h3>${{roleA||roleB ? 'Elegí el segundo rol para comparar' : 'Seleccioná dos roles para empezar'}}</h3>
        <p>Elegí un rol en cada lado para ver la comparación completa: salarios, skills, certificaciones, mercados y más.</p>
      </div>`;
      return;
    }}

    // Calcular shared para el summary
    const sharedHard = countShared(roleA, roleB, 'hardSkills');
    const sharedSoft = countShared(roleA, roleB, 'softSkills');
    const sharedTools = countShared(roleA, roleB, 'tools');
    const sharedCerts = countShared(roleA, roleB, 'certs');
    const totalShared = sharedHard + sharedSoft + sharedTools + sharedCerts;

    // Row builders
    let html = '';

    // Summary
    html += `<div class="summary-row">
      <div><div class="summary-num">${{sharedHard}}</div><div class="summary-label">Hard skills compartidas</div></div>
      <div class="summary-divider"></div>
      <div><div class="summary-num">${{sharedSoft}}</div><div class="summary-label">Soft skills compartidas</div></div>
      <div class="summary-divider"></div>
      <div><div class="summary-num">${{sharedTools+sharedCerts}}</div><div class="summary-label">Tools + Certs compartidas</div></div>
    </div>`;

    // Nombre del rol
    html += renderRow('🎯', 'Nombre del rol',
      `${{renderText(roleA.roleEN, 'big')}}<div style="font-size:13px;color:var(--text-secondary);font-style:italic">${{escHtml(roleA.roleES||'')}}</div>`,
      `${{renderText(roleB.roleEN, 'big')}}<div style="font-size:13px;color:var(--text-secondary);font-style:italic">${{escHtml(roleB.roleES||'')}}</div>`
    );

    // Categoria + nivel
    const catA = CATS[roleA.cat] || {{label: roleA.cat, color: '#94A3B8'}};
    const catB = CATS[roleB.cat] || {{label: roleB.cat, color: '#94A3B8'}};
    const sameCat = roleA.cat === roleB.cat;
    const sameLvl = roleA.level === roleB.level;
    html += renderRow('🗂️', 'Categoría · Nivel',
      `<div class="cell-text" style="color:${{catA.color}};font-weight:700">${{escHtml(catA.label)}}${{sameCat?' <span style="color:var(--mint);font-size:11px;font-weight:600">✓ MISMA</span>':''}}</div><div style="font-size:13px;color:var(--text-secondary)">${{escHtml(LEVELS[roleA.level]||roleA.level)}}${{sameLvl?' <span style="color:var(--mint);font-size:11px;font-weight:600">✓ MISMO</span>':''}}</div>`,
      `<div class="cell-text" style="color:${{catB.color}};font-weight:700">${{escHtml(catB.label)}}${{sameCat?' <span style="color:var(--mint);font-size:11px;font-weight:600">✓ MISMA</span>':''}}</div><div style="font-size:13px;color:var(--text-secondary)">${{escHtml(LEVELS[roleB.level]||roleB.level)}}${{sameLvl?' <span style="color:var(--mint);font-size:11px;font-weight:600">✓ MISMO</span>':''}}</div>`
    );

    // Salario mensual
    html += renderRow('💰', 'Salario mensual (USD)',
      renderText(roleA.salaryMonth, 'salary'),
      renderText(roleB.salaryMonth, 'salary')
    );

    // Salario anual
    html += renderRow('📈', 'Salario anual (USD)',
      renderText(roleA.salaryYear, 'salary'),
      renderText(roleB.salaryYear, 'salary')
    );

    // Demanda
    html += renderRow('🔥', 'Demanda del mercado',
      renderDemand(roleA.demand),
      renderDemand(roleB.demand)
    );

    // Trabajo remoto
    html += renderRow('🏠', 'Trabajo remoto',
      renderText(roleA.remote),
      renderText(roleB.remote)
    );

    // Descripcion
    html += renderRow('📝', '¿Qué hace en su día a día?',
      renderText(roleA.description),
      renderText(roleB.description)
    );

    // Hard skills
    html += renderRow('🛠️', 'Hard Skills (técnicas)',
      renderList(roleA.hardSkills, roleB.hardSkills, 'a'),
      renderList(roleA.hardSkills, roleB.hardSkills, 'b')
    );

    // Tools
    html += renderRow('🧰', 'Herramientas',
      renderList(roleA.tools, roleB.tools, 'a'),
      renderList(roleA.tools, roleB.tools, 'b')
    );

    // Soft skills
    html += renderRow('💬', 'Soft Skills',
      renderList(roleA.softSkills, roleB.softSkills, 'a'),
      renderList(roleA.softSkills, roleB.softSkills, 'b')
    );

    // Certs
    html += renderRow('🎓', 'Certificaciones recomendadas',
      renderList(roleA.certs, roleB.certs, 'a'),
      renderList(roleA.certs, roleB.certs, 'b')
    );

    // Como empezar
    html += renderRow('🚀', 'Cómo empezar',
      renderText(roleA.howToStart),
      renderText(roleB.howToStart)
    );

    // Ruta de crecimiento
    html += renderRow('🪜', 'Ruta de crecimiento',
      renderText(roleA.growth),
      renderText(roleB.growth)
    );

    // Mercados
    html += renderRow('🌎', 'Mercados que más contratan',
      renderText(roleA.markets),
      renderText(roleB.markets)
    );

    // Proyecciones (si existen)
    if (roleA.projection || roleB.projection || roleA.trend2026 || roleB.trend2026) {{
      const projA = [roleA.projection, roleA.trend2026, roleA.salaryJump, roleA.difficulty].filter(x=>x).join(' · ');
      const projB = [roleB.projection, roleB.trend2026, roleB.salaryJump, roleB.difficulty].filter(x=>x).join(' · ');
      html += renderRow('🔮', 'Proyecciones 2026-2028',
        renderText(projA),
        renderText(projB)
      );
    }}

    // Sinonimos
    if (roleA.synonyms || roleB.synonyms) {{
      html += renderRow('🔤', 'También conocido como',
        renderText(roleA.synonyms),
        renderText(roleB.synonyms)
      );
    }}

    // Roles relacionados
    html += renderRow('🔗', 'Roles relacionados',
      renderRelated(roleA.related),
      renderRelated(roleB.related)
    );

    // CTA al final
    html += `<div class="cta-box">
      <div class="cta-box-text">💡 <strong>Ver el detalle completo de cada rol:</strong> con descripciones extendidas, todas las certificaciones con links oficiales, salarios actualizados y más.</div>
      <a href="Mapa_Carreras_Ciberseguridad.html#role-${{idA}}">Detalle rol A →</a>
      <a href="Mapa_Carreras_Ciberseguridad.html#role-${{idB}}">Detalle rol B →</a>
    </div>`;

    out.innerHTML = html;
  }}

  // === Eventos ===
  document.getElementById('selectA').addEventListener('change', render);
  document.getElementById('selectB').addEventListener('change', render);

  // Swap
  document.getElementById('swapBtn').addEventListener('click', () => {{
    const a = document.getElementById('selectA');
    const b = document.getElementById('selectB');
    const tmp = a.value;
    a.value = b.value;
    b.value = tmp;
    render();
  }});

  // URL hash support (#1,7 o #1 para preseleccionar)
  function loadFromHash() {{
    const hash = window.location.hash.replace('#', '');
    if (!hash) return;
    const parts = hash.split(',').map(x => x.trim());
    if (parts[0]) document.getElementById('selectA').value = parts[0];
    if (parts[1]) document.getElementById('selectB').value = parts[1];
    render();
  }}

  loadFromHash();
  // Si no se cargo nada, default a 2 roles comunes para demostrar (SOC T1 vs Pentester Jr)
  if (!document.getElementById('selectA').value && !document.getElementById('selectB').value) {{
    // No preseleccionar nada — dejar empty state
    render();
  }}
</script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
