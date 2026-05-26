"""
Genera Mapa_General_Carreras.html
Vista panoramica INTERACTIVA: 50 roles en una grilla (categorias x niveles)
Cards clickeables que abren el detalle del rol en la version interactiva.
"""

import json

LEVEL_ORDER = ['junior', 'mid', 'senior', 'manager', 'executive']
LEVEL_COLORS = {
    'junior': '#10B981',
    'mid': '#06B6D4',
    'senior': '#F59E0B',
    'manager': '#EC4899',
    'executive': '#C084FC',
}


def hex_to_rgba(h, a):
    h = h.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{a})'


CSS = """
:root{
  --bg-deep:#0A0E1A;--bg-alt:#0E1322;--bg-card:#1A2236;--bg-elevated:#222B42;
  --border:#2A3149;--border-bright:#3A4566;
  --text-primary:#F8FAFC;--text-secondary:#CBD5E1;--text-muted:#94A3B8;--text-dim:#64748B;
  --gold:#F59E0B;--mint:#10B981;--cyan:#06B6D4;--magenta:#EC4899;--violet:#C084FC;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg-deep);color:var(--text-primary);font-family:'Sora',sans-serif;min-height:100vh}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 1400px 900px at 70% 0%,rgba(245,158,11,0.05),transparent 60%),radial-gradient(ellipse 1200px 800px at 30% 100%,rgba(236,72,153,0.04),transparent 60%);pointer-events:none;z-index:0}

.app{position:relative;z-index:1;max-width:2000px;margin:0 auto;padding:32px 36px 60px}

/* === TOP BAR === */
.top{display:flex;justify-content:space-between;align-items:center;padding-bottom:20px;margin-bottom:24px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:16px}
.brand{display:flex;align-items:center;gap:14px;font-family:'Bricolage Grotesque',serif;font-weight:700;font-size:22px;letter-spacing:-0.02em}
.brand-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--gold),var(--magenta));border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:800;font-size:18px;color:var(--bg-deep)}
.brand em{font-style:italic;color:var(--gold)}
.brand-meta{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase;margin-top:2px}
.nav-links{display:flex;gap:10px;flex-wrap:wrap}
.nav-link{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);text-decoration:none;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s}
.nav-link:hover{background:var(--bg-elevated);color:var(--gold);border-color:var(--gold)}

/* === HERO === */
.hero{margin-bottom:28px}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:12px}
.eyebrow::before{content:'';width:28px;height:1px;background:var(--gold)}
.title{font-family:'Bricolage Grotesque',serif;font-size:clamp(36px,4vw,52px);font-weight:700;line-height:1;letter-spacing:-0.035em;margin-bottom:10px}
.title em{font-style:italic;color:var(--gold);font-weight:500}
.subtitle{color:var(--text-secondary);font-size:14px;max-width:900px;line-height:1.55;display:flex;gap:24px;flex-wrap:wrap;font-family:'JetBrains Mono',monospace}
.subtitle span{display:flex;align-items:center;gap:8px}
.subtitle .arrow{color:var(--gold);font-size:16px}

/* === FILTROS === */
.filters{display:flex;gap:24px;padding:18px 22px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;margin-bottom:24px;flex-wrap:wrap;align-items:center}
.filter-group{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.filter-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.2em;text-transform:uppercase;padding-right:8px;border-right:1px solid var(--border);margin-right:4px}
.filter-chip{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);padding:5px 11px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:100px;cursor:pointer;transition:all 0.2s;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:0.05em}
.filter-chip:hover{background:rgba(255,255,255,0.08);color:var(--text-primary)}
.filter-chip.active{background:var(--chip-color,var(--gold));color:var(--bg-deep);border-color:var(--chip-color,var(--gold));font-weight:600}
.filter-chip .dot{width:8px;height:8px;border-radius:50%;background:var(--chip-color)}
.filter-chip.active .dot{background:var(--bg-deep)}
.reset-btn{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);background:none;border:none;cursor:pointer;text-decoration:underline;letter-spacing:0.1em;text-transform:uppercase}
.reset-btn:hover{color:var(--gold)}

/* === GRID === */
.grid-wrapper{overflow-x:auto;padding-bottom:8px}
.grid{display:grid;gap:0;border:1px solid var(--border);border-radius:14px;overflow:hidden;background:var(--bg-card);min-width:1800px}

/* Header de categorias */
.col-header{padding:14px 10px 12px;background:var(--bg-card);border-bottom:2px solid var(--border);position:sticky;top:0;z-index:5;display:flex;flex-direction:column;align-items:center;gap:4px}
.col-header.label-cell{background:var(--bg-deep)}
.col-header-bar{width:32px;height:4px;border-radius:2px;background:var(--cat-color);margin-bottom:6px}
.col-header-name{font-size:12px;font-weight:700;color:var(--text-primary);text-align:center;line-height:1.2;letter-spacing:-0.01em}
.col-header-sub{font-size:10px;color:var(--text-secondary);text-align:center}
.col-header-count{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--cat-color);margin-top:3px;font-weight:600}

/* Filas (niveles) */
.row-label{padding:18px 14px;background:var(--bg-deep);border-right:2px solid var(--lvl-color);border-bottom:1px solid var(--border);display:flex;flex-direction:column;justify-content:center;gap:4px;min-width:170px}
.row-label.alt{background:#0F1422}
.row-label-num{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--lvl-color);font-weight:700;letter-spacing:0.2em}
.row-label-name{font-family:'Bricolage Grotesque',serif;font-size:17px;font-weight:700;letter-spacing:-0.02em;line-height:1.1}
.row-label-years{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-secondary)}
.row-label-count{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--lvl-color);font-weight:600;margin-top:4px;display:flex;align-items:center;gap:5px}
.row-label-count::before{content:'';width:6px;height:6px;background:var(--lvl-color);border-radius:50%}

/* Celda de la grilla */
.cell{padding:8px 6px;border-bottom:1px solid var(--border);border-right:1px solid var(--border);display:flex;flex-direction:column;gap:6px;align-items:stretch;min-height:80px}
.cell.alt{background:rgba(255,255,255,0.012)}
.cell:last-child{border-right:none}

/* Card de rol */
.card{background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:9px 11px;cursor:pointer;transition:all 0.18s;position:relative;border-left:3px solid var(--card-color);display:flex;flex-direction:column;gap:3px;overflow:hidden}
.card::before{content:'';position:absolute;top:0;right:0;width:45%;height:100%;background:linear-gradient(135deg,transparent 50%,var(--card-glow));pointer-events:none;opacity:0.5;border-radius:0 8px 8px 0;transition:opacity 0.2s}
.card:hover{background:var(--bg-elevated);transform:translateY(-2px);box-shadow:0 6px 14px rgba(0,0,0,0.4),0 0 0 1px var(--card-color);z-index:2;border-color:var(--card-color)}
.card:hover::before{opacity:1}
.card-top{display:flex;justify-content:space-between;align-items:flex-start;gap:6px;position:relative;z-index:1}
.card-name{font-family:'Bricolage Grotesque',serif;font-size:13px;font-weight:700;color:var(--text-primary);line-height:1.15;letter-spacing:-0.015em;flex:1}
.card-id{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--text-dim);font-weight:600;flex-shrink:0}
.card-name-es{font-size:10px;color:var(--text-muted);font-style:italic;line-height:1.2;position:relative;z-index:1}
.card-bottom{display:flex;justify-content:space-between;align-items:center;margin-top:auto;padding-top:4px;position:relative;z-index:1}
.card-salary{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--gold);font-weight:700}
.card-demand{font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;padding:2px 6px;background:rgba(255,255,255,0.05);border-radius:4px}
.card-demand.very-high{color:var(--mint);background:rgba(16,185,129,0.1)}
.card-demand.explosive{color:var(--magenta);background:rgba(236,72,153,0.12);font-weight:700}

/* Card cuando esta atenuada por filtro */
.card.dim{opacity:0.18;filter:saturate(0.3)}
.card.dim:hover{opacity:1;filter:none}

/* Cell vacia */
.cell-empty{display:flex;align-items:center;justify-content:center;color:var(--text-dim);font-family:'JetBrains Mono',monospace;font-size:10px;padding:10px 4px;opacity:0.4}

/* === FOOTER === */
.footer{margin-top:32px;padding-top:28px;border-top:1px solid var(--border);display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.foot h4{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:0.15em;text-transform:uppercase;margin-bottom:10px}
.foot p{font-size:13px;color:var(--text-secondary);line-height:1.6}
.foot p strong{color:var(--text-primary);font-weight:600}

@media (max-width:1100px){
  .grid{min-width:1500px}
  .footer{grid-template-columns:1fr}
}
@media (max-width:640px){
  .app{padding:20px 16px}
  .grid{min-width:1300px}
}
"""


def build_general(data, output_path):
    cats = data['categories']
    levels = data['levels']
    roles = data['roles']
    cat_keys = list(cats.keys())
    n_cats = len(cat_keys)

    # Grid: (nivel, cat) -> [roles]
    grid = {}
    for lk in LEVEL_ORDER:
        for ck in cat_keys:
            grid[(lk, ck)] = [r for r in roles
                              if r.get('level') == lk and r.get('cat') == ck]

    # Generar grid-template-columns
    grid_cols = f"170px repeat({n_cats}, minmax(150px, 1fr))"

    # === Header de categorias ===
    headers_html = ['<div class="col-header label-cell"></div>']
    for ck in cat_keys:
        cat = cats[ck]
        count = sum(1 for r in roles if r.get('cat') == ck)
        label = cat['label']
        if '/' in label:
            parts = [p.strip() for p in label.split('/')]
            name_html = f'<div class="col-header-name">{parts[0]}</div><div class="col-header-sub">{parts[1]}</div>'
        else:
            name_html = f'<div class="col-header-name">{label}</div>'
        headers_html.append(f'''<div class="col-header" style="--cat-color:{cat['color']}">
            <div class="col-header-bar"></div>
            {name_html}
            <div class="col-header-count">{count} roles</div>
        </div>''')

    # === Filas: por cada nivel, label + celdas ===
    rows_html = []
    for row_idx, lk in enumerate(LEVEL_ORDER):
        lvl = levels[lk]
        lvl_color = LEVEL_COLORS[lk]
        n_in = sum(1 for r in roles if r.get('level') == lk)
        alt_class = 'alt' if row_idx % 2 == 0 else ''

        # Label del nivel
        rows_html.append(f'''<div class="row-label {alt_class}" style="--lvl-color:{lvl_color}">
            <div class="row-label-num">NIVEL {row_idx + 1:02d}</div>
            <div class="row-label-name">{lvl['label']}</div>
            <div class="row-label-years">{lvl['yearsRange']}</div>
            <div class="row-label-count">{n_in} roles</div>
        </div>''')

        # Celdas
        for ck in cat_keys:
            cell_roles = grid[(lk, ck)]
            cat = cats[ck]
            color = cat['color']
            cards_html = []
            for role in cell_roles:
                role_en = role['roleEN']
                if len(role_en) > 30:
                    role_en_short = role_en.split('/')[0].strip() if '/' in role_en else role_en[:28] + '…'
                else:
                    role_en_short = role_en

                role_es = role.get('roleES', '')
                if len(role_es) > 32:
                    role_es = role_es[:30] + '…'

                # Salario tope
                sal = role.get('salaryMonth', '')
                salary_max = sal.split('-')[-1].strip() if '-' in sal else sal

                # Demanda
                demand_raw = role.get('demand', '').upper()
                if 'EXPLOSIVA' in demand_raw:
                    demand_cls = 'explosive'
                    demand_lbl = 'EXPLOSIVA'
                elif 'MUY ALTA' in demand_raw:
                    demand_cls = 'very-high'
                    demand_lbl = 'MUY ALTA'
                elif 'ALTA' in demand_raw:
                    demand_cls = ''
                    demand_lbl = 'ALTA'
                else:
                    demand_cls = ''
                    demand_lbl = demand_raw.split('(')[0].strip()[:10]

                cards_html.append(f'''<div class="card" data-cat="{ck}" data-level="{lk}" data-role-id="{role['id']}" style="--card-color:{color};--card-glow:{hex_to_rgba(color, 0.12)}">
                    <div class="card-top">
                        <div class="card-name">{role_en_short}</div>
                        <div class="card-id">#{role['id']:02d}</div>
                    </div>
                    <div class="card-name-es">{role_es}</div>
                    <div class="card-bottom">
                        <div class="card-salary">${salary_max[1:] if salary_max.startswith('$') else salary_max}/mes</div>
                        <div class="card-demand {demand_cls}">{demand_lbl}</div>
                    </div>
                </div>''')

            content = '\n'.join(cards_html) if cards_html else '<div class="cell-empty">—</div>'
            rows_html.append(f'<div class="cell {alt_class}">{content}</div>')

    # === Filtros: chips de categorias + niveles ===
    cat_chips = []
    for ck in cat_keys:
        cat = cats[ck]
        label_short = cat['label'].split('/')[0].strip()
        cat_chips.append(f'<button class="filter-chip" data-filter-cat="{ck}" style="--chip-color:{cat["color"]}"><span class="dot"></span>{label_short}</button>')

    lvl_chips = []
    for lk in LEVEL_ORDER:
        lvl = levels[lk]
        lvl_color = LEVEL_COLORS[lk]
        lvl_short = lvl['label'].split('/')[0].split('-')[0].strip()
        lvl_chips.append(f'<button class="filter-chip" data-filter-level="{lk}" style="--chip-color:{lvl_color}"><span class="dot"></span>{lvl_short}</button>')

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mapa General · Carreras Ciberseguridad</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Sora:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="app">
  <div class="top">
    <div class="brand">
      <div class="brand-mark">⌘</div>
      <div>
        <div>Cyber<em>.map</em> <span style="font-size:13px;color:var(--text-muted);font-weight:400;margin-left:6px">/ Mapa general interactivo</span></div>
        <div class="brand-meta">{len(roles)} ROLES · {n_cats} CATEGORÍAS · {len(LEVEL_ORDER)} NIVELES</div>
      </div>
    </div>
    <div class="nav-links">
      <a class="nav-link" href="Mapa_Carreras_Ciberseguridad.html">→ Versión interactiva detalle</a>
      <a class="nav-link" href="Mapa_Mental_Carreras.html">→ Vista por niveles</a>
    </div>
  </div>

  <div class="hero">
    <div class="eyebrow">VISTA PANORÁMICA INTERACTIVA · TODO EN UNA PANTALLA</div>
    <h1 class="title">El universo completo de <em>ciberseguridad</em>.</h1>
    <p class="subtitle">
      <span><span class="arrow">↓</span> Niveles de seniority</span>
      <span><span class="arrow">→</span> Categorías</span>
      <span style="color:var(--text-muted)">· Toca cualquier tarjeta para ver el rol en detalle</span>
    </p>
  </div>

  <!-- Filtros -->
  <div class="filters">
    <div class="filter-group">
      <span class="filter-label">Categoría</span>
      {''.join(cat_chips)}
    </div>
    <div class="filter-group">
      <span class="filter-label">Nivel</span>
      {''.join(lvl_chips)}
    </div>
    <button class="reset-btn" id="resetBtn">× Limpiar filtros</button>
  </div>

  <!-- Grid principal -->
  <div class="grid-wrapper">
    <div class="grid" style="grid-template-columns:{grid_cols}">
      {''.join(headers_html)}
      {''.join(rows_html)}
    </div>
  </div>

  <!-- Footer informativo -->
  <div class="footer">
    <div class="foot">
      <h4>Cómo leer el mapa</h4>
      <p>Cada fila es un <strong>nivel de seniority</strong> (Junior arriba → C-Level abajo). Cada columna es una <strong>categoría</strong> o área de especialización. Las tarjetas muestran el nombre del rol, su salario máximo mensual y la demanda actual del mercado.</p>
    </div>
    <div class="foot">
      <h4>Filtros y navegación</h4>
      <p>Usa los chips de arriba para resaltar roles por <strong>categoría</strong> o <strong>nivel</strong>. Toca cualquier tarjeta para abrirla en la versión interactiva con descripción completa, skills, herramientas, certs y mercados que más contratan.</p>
    </div>
    <div class="foot">
      <h4>Sobre los salarios</h4>
      <p>El monto mostrado es el <strong>tope mensual</strong> del rango (Senior trabajando para mercado USA). El piso del rango — Junior trabajando en LATAM — está en la versión interactiva. Los rangos se basan en datos 2025-2026.</p>
    </div>
  </div>
</div>

<script>
  // Estado de filtros
  let activeCats = new Set();
  let activeLevels = new Set();

  function applyFilters() {{
    const cards = document.querySelectorAll('.card');
    const hasCatFilter = activeCats.size > 0;
    const hasLvlFilter = activeLevels.size > 0;
    const noFilters = !hasCatFilter && !hasLvlFilter;

    cards.forEach(card => {{
      if (noFilters) {{
        card.classList.remove('dim');
        return;
      }}
      const cat = card.dataset.cat;
      const lvl = card.dataset.level;
      const matchCat = !hasCatFilter || activeCats.has(cat);
      const matchLvl = !hasLvlFilter || activeLevels.has(lvl);
      if (matchCat && matchLvl) {{
        card.classList.remove('dim');
      }} else {{
        card.classList.add('dim');
      }}
    }});
  }}

  // Click en chip de categoria
  document.querySelectorAll('[data-filter-cat]').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const c = btn.dataset.filterCat;
      if (activeCats.has(c)) {{
        activeCats.delete(c);
        btn.classList.remove('active');
      }} else {{
        activeCats.add(c);
        btn.classList.add('active');
      }}
      applyFilters();
    }});
  }});

  // Click en chip de nivel
  document.querySelectorAll('[data-filter-level]').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const l = btn.dataset.filterLevel;
      if (activeLevels.has(l)) {{
        activeLevels.delete(l);
        btn.classList.remove('active');
      }} else {{
        activeLevels.add(l);
        btn.classList.add('active');
      }}
      applyFilters();
    }});
  }});

  // Reset
  document.getElementById('resetBtn').addEventListener('click', () => {{
    activeCats.clear();
    activeLevels.clear();
    document.querySelectorAll('.filter-chip.active').forEach(c => c.classList.remove('active'));
    applyFilters();
  }});

  // Click en card -> navegar a la version interactiva con el rol
  document.querySelectorAll('.card').forEach(card => {{
    card.addEventListener('click', () => {{
      const roleId = card.dataset.roleId;
      // Abrir la version interactiva en el rol especifico
      window.location.href = `Mapa_Carreras_Ciberseguridad.html#role-${{roleId}}`;
    }});
  }});
</script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
