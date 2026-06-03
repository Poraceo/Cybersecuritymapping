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

/* === FILTRO POR SKILLS === */
.skill-filter{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px 22px;margin-bottom:24px;position:relative}
.skill-filter-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:12px}
.skill-filter-title{display:flex;align-items:center;gap:10px}
.skill-filter-title h3{font-family:'Bricolage Grotesque',serif;font-size:18px;font-weight:700;letter-spacing:-0.02em;color:var(--text-primary)}
.skill-filter-title small{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.15em;padding-left:8px;border-left:1px solid var(--border)}
.skill-filter-controls{display:flex;align-items:center;gap:14px;flex-wrap:wrap}

/* Toggle AND/OR */
.mode-toggle{display:flex;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px;padding:3px;font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:0.1em;text-transform:uppercase}
.mode-toggle button{background:none;border:none;padding:6px 12px;border-radius:100px;cursor:pointer;color:var(--text-muted);transition:all 0.2s;font-family:inherit;font-size:inherit;letter-spacing:inherit;text-transform:inherit;font-weight:600}
.mode-toggle button.active{background:var(--gold);color:var(--bg-deep)}
.mode-toggle button:not(.active):hover{color:var(--text-primary)}

.mode-explainer{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.05em}
.mode-explainer strong{color:var(--gold);font-weight:600}

/* Buscador de skills */
.skill-search{flex:1;min-width:200px;max-width:320px;display:flex;align-items:center;gap:8px;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px;padding:6px 14px;transition:border 0.2s}
.skill-search:focus-within{border-color:var(--gold)}
.skill-search input{flex:1;background:none;border:none;color:var(--text-primary);font-family:'JetBrains Mono',monospace;font-size:12px;outline:none}
.skill-search input::placeholder{color:var(--text-dim)}
.skill-search-icon{color:var(--text-muted);font-size:14px}

/* Counter */
.match-counter{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);padding:6px 12px;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px}
.match-counter strong{color:var(--gold);font-size:13px;font-weight:700}

/* Grilla de columnas de skills */
.skill-columns{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:6px}
.skill-col{display:flex;flex-direction:column;gap:8px;background:var(--bg-deep);border:1px solid var(--border);border-radius:10px;padding:14px 14px 12px;min-height:60px}
.skill-col-title{display:flex;align-items:center;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid var(--border);margin-bottom:6px}
.skill-col-title h4{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--col-color);letter-spacing:0.15em;text-transform:uppercase;font-weight:700;display:flex;align-items:center;gap:6px}
.skill-col-title h4::before{content:'';width:8px;height:8px;background:var(--col-color);border-radius:50%}
.skill-col-count{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-dim);font-weight:600}
.skill-col[data-col="hard"]{--col-color:var(--cyan)}
.skill-col[data-col="soft"]{--col-color:var(--mint)}
.skill-col[data-col="certs"]{--col-color:var(--gold)}

.skill-chips-wrap{display:flex;flex-wrap:wrap;gap:5px;max-height:200px;overflow-y:auto;padding-right:4px;align-content:flex-start}
.skill-chips-wrap::-webkit-scrollbar{width:6px}
.skill-chips-wrap::-webkit-scrollbar-track{background:transparent}
.skill-chips-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}

.skill-chip-small{font-size:11px;padding:3px 9px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:100px;color:var(--text-secondary);cursor:pointer;transition:all 0.15s;display:inline-flex;align-items:center;gap:4px;white-space:nowrap;line-height:1.4}
.skill-chip-small:hover{background:rgba(255,255,255,0.08);color:var(--text-primary);border-color:var(--col-color)}
.skill-chip-small.active{background:var(--col-color);color:var(--bg-deep);border-color:var(--col-color);font-weight:600}
.skill-chip-small .x{opacity:0.6;font-size:10px}
.skill-chip-small.active .x{opacity:1}
.skill-chip-small.hidden{display:none}
.skill-chip-small .count-mini{opacity:0.5;font-size:9px;margin-left:2px}

/* Bar de skills activas */
.active-skills-bar{display:none;margin-top:14px;padding:10px 14px;background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.2);border-radius:10px;align-items:center;gap:10px;flex-wrap:wrap}
.active-skills-bar.visible{display:flex}
.active-skills-bar-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--gold);letter-spacing:0.15em;text-transform:uppercase;font-weight:700}
.active-skills-list{display:flex;flex-wrap:wrap;gap:5px;flex:1}
.active-skill-tag{font-size:11px;padding:3px 9px;background:var(--gold);color:var(--bg-deep);border-radius:100px;font-weight:600;display:inline-flex;align-items:center;gap:5px;cursor:pointer}
.active-skill-tag:hover{background:#FBBF24}
.active-skill-tag .x{font-size:13px;line-height:1}
.clear-skills-btn{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);background:none;border:none;cursor:pointer;text-decoration:underline;letter-spacing:0.1em;text-transform:uppercase}
.clear-skills-btn:hover{color:var(--gold)}

/* Badge de match en cards */
.match-badge{position:absolute;top:8px;right:8px;font-family:'JetBrains Mono',monospace;font-size:9px;font-weight:700;padding:2px 7px;border-radius:100px;background:var(--mint);color:var(--bg-deep);z-index:5;letter-spacing:0.05em;display:none}
.match-badge.visible{display:block}
.match-badge.partial{background:var(--gold)}
.match-badge.low{background:var(--text-dim);color:var(--text-primary)}

/* Cuando hay filtro de skills activo, cards sin match se atenúan */
.card.no-match{opacity:0.15;filter:saturate(0.2)}
.card.no-match:hover{opacity:0.6}

/* Empty state */
.empty-state{grid-column:1/-1;padding:40px;text-align:center;color:var(--text-muted);font-family:'JetBrains Mono',monospace;display:none}
.empty-state.visible{display:block}
.empty-state h4{font-family:'Bricolage Grotesque',serif;font-size:24px;color:var(--text-primary);margin-bottom:8px}

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
  .skill-columns{grid-template-columns:1fr;gap:14px}
  .skill-chips-wrap{max-height:160px}
  .skill-filter-controls{width:100%}
  .skill-search{max-width:none;width:100%}
}
@media (max-width:640px){
  .app{padding:20px 16px}
  .grid{min-width:1300px}
  .skill-filter-controls{flex-direction:column;align-items:stretch}
  .mode-toggle{align-self:flex-start}
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

    # === Recolectar skills unicas y contar frecuencias ===
    def clean_skill(s):
        # Normalizar: quitar estrellas, parentesis con notas, espacios extra
        s = s.replace('⭐', '').strip()
        # Mantener parentesis si son parte del nombre como (Microsoft Endpoint)
        return s

    hard_freq = {}
    soft_freq = {}
    cert_freq = {}
    # Mapeo de skill normalizada -> set de roleId
    skill_to_roles = {'hard': {}, 'soft': {}, 'certs': {}}

    for r in roles:
        for s in r.get('hardSkills', []):
            cs = clean_skill(s)
            if cs:
                hard_freq[cs] = hard_freq.get(cs, 0) + 1
                skill_to_roles['hard'].setdefault(cs, set()).add(r['id'])
        for s in r.get('softSkills', []):
            cs = clean_skill(s)
            if cs:
                soft_freq[cs] = soft_freq.get(cs, 0) + 1
                skill_to_roles['soft'].setdefault(cs, set()).add(r['id'])
        for s in r.get('certs', []):
            cs = clean_skill(s)
            if cs:
                cert_freq[cs] = cert_freq.get(cs, 0) + 1
                skill_to_roles['certs'].setdefault(cs, set()).add(r['id'])

    # Ordenar por frecuencia descendente (los mas usados arriba)
    hard_sorted = sorted(hard_freq.items(), key=lambda x: (-x[1], x[0].lower()))
    soft_sorted = sorted(soft_freq.items(), key=lambda x: (-x[1], x[0].lower()))
    cert_sorted = sorted(cert_freq.items(), key=lambda x: (-x[1], x[0].lower()))

    # Mapeo de roleId -> {hard:[], soft:[], certs:[]} para embeber en el HTML
    role_skills = {}
    for r in roles:
        role_skills[r['id']] = {
            'hard': [clean_skill(s) for s in r.get('hardSkills', []) if clean_skill(s)],
            'soft': [clean_skill(s) for s in r.get('softSkills', []) if clean_skill(s)],
            'certs': [clean_skill(s) for s in r.get('certs', []) if clean_skill(s)],
        }
    role_skills_json = json.dumps(role_skills, ensure_ascii=False)

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
                    <div class="match-badge" data-match-for="{role['id']}"></div>
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

    # === Chips de skills (3 columnas: Hard / Soft / Certs) ===
    def make_skill_chips(sorted_skills, col_type):
        chips = []
        for skill, count in sorted_skills:
            # Escape simple para atributos HTML
            skill_attr = skill.replace('"', '&quot;')
            chips.append(f'<button class="skill-chip-small" data-skill-type="{col_type}" data-skill-name="{skill_attr}">{skill}<span class="count-mini">·{count}</span></button>')
        return ''.join(chips)

    hard_chips = make_skill_chips(hard_sorted, 'hard')
    soft_chips = make_skill_chips(soft_sorted, 'soft')
    cert_chips = make_skill_chips(cert_sorted, 'certs')

    n_hard = len(hard_sorted)
    n_soft = len(soft_sorted)
    n_certs = len(cert_sorted)

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
      <a class="nav-link" href="Catalogo_Certificaciones.html" style="color:var(--gold);border-color:var(--gold)">📜 Catálogo de certs</a>
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

  <!-- Filtro POR SKILLS -->
  <div class="skill-filter">
    <div class="skill-filter-header">
      <div class="skill-filter-title">
        <h3>🎯 ¿Qué skills ya tienes?</h3>
        <small>FILTRA ROLES POR LO QUE SABES</small>
      </div>
      <div class="skill-filter-controls">
        <div class="skill-search">
          <span class="skill-search-icon">🔍</span>
          <input type="text" id="skillSearch" placeholder="Buscar skill o cert...">
        </div>
        <div class="mode-toggle">
          <button class="active" data-mode="OR">CUALQUIERA</button>
          <button data-mode="AND">TODAS</button>
        </div>
        <span class="match-counter" id="matchCounter"><strong>{len(roles)}</strong> roles visibles</span>
      </div>
    </div>

    <div class="skill-columns">
      <div class="skill-col" data-col="hard">
        <div class="skill-col-title">
          <h4>Hard Skills</h4>
          <span class="skill-col-count">{n_hard} totales</span>
        </div>
        <div class="skill-chips-wrap" data-col-chips="hard">{hard_chips}</div>
      </div>
      <div class="skill-col" data-col="soft">
        <div class="skill-col-title">
          <h4>Soft Skills</h4>
          <span class="skill-col-count">{n_soft} totales</span>
        </div>
        <div class="skill-chips-wrap" data-col-chips="soft">{soft_chips}</div>
      </div>
      <div class="skill-col" data-col="certs">
        <div class="skill-col-title">
          <h4>Certificaciones</h4>
          <span class="skill-col-count">{n_certs} totales</span>
        </div>
        <div class="skill-chips-wrap" data-col-chips="certs">{cert_chips}</div>
      </div>
    </div>

    <div class="active-skills-bar" id="activeSkillsBar">
      <span class="active-skills-bar-label">Tu perfil:</span>
      <div class="active-skills-list" id="activeSkillsList"></div>
      <button class="clear-skills-btn" id="clearSkillsBtn">× Limpiar skills</button>
    </div>
  </div>

  <!-- Grid principal -->
  <div class="grid-wrapper">
    <div class="grid" style="grid-template-columns:{grid_cols}">
      {''.join(headers_html)}
      {''.join(rows_html)}
    </div>
    <div class="empty-state" id="emptyState">
      <h4>Ningún rol coincide</h4>
      <p>Prueba quitando alguna skill o cambiando a modo CUALQUIERA</p>
    </div>
  </div>

  <!-- Footer informativo -->
  <div class="footer">
    <div class="foot">
      <h4>🎯 Filtro por skills</h4>
      <p>Selecciona las skills que <strong>ya tienes</strong> (hard, soft o certs). Usa el modo <strong>CUALQUIERA</strong> para descubrir roles donde tu skill aplica, o <strong>TODAS</strong> para encontrar roles que requieren exactamente lo que tienes. El badge en cada card muestra <strong>cuántas de tus skills matchean</strong>.</p>
    </div>
    <div class="foot">
      <h4>Filtros y navegación</h4>
      <p>Combina filtros de <strong>categoría</strong>, <strong>nivel</strong> y <strong>skills</strong> para refinar la búsqueda. Toca cualquier tarjeta para abrirla en la versión interactiva con descripción completa, herramientas y mercados que más contratan.</p>
    </div>
    <div class="foot">
      <h4>Sobre los salarios</h4>
      <p>El monto mostrado es el <strong>tope mensual</strong> del rango (Senior trabajando para mercado USA). El piso del rango — Junior trabajando en LATAM — está en la versión interactiva. Los rangos se basan en datos 2025-2026.</p>
    </div>
  </div>
</div>

<script>
  // Datos de skills por rol
  const ROLE_SKILLS = {role_skills_json};
  const TOTAL_ROLES = {len(roles)};

  // Estado de filtros
  let activeCats = new Set();
  let activeLevels = new Set();
  let activeSkills = {{ hard: new Set(), soft: new Set(), certs: new Set() }};
  let mode = 'OR'; // 'OR' o 'AND'

  function getTotalActiveSkills() {{
    return activeSkills.hard.size + activeSkills.soft.size + activeSkills.certs.size;
  }}

  // Calcula match (porcentaje) entre skills activas y skills del rol
  function calculateMatch(roleId) {{
    const total = getTotalActiveSkills();
    if (total === 0) return {{ matches: 0, total: 0, allMatch: true }};

    const roleData = ROLE_SKILLS[roleId];
    if (!roleData) return {{ matches: 0, total: total, allMatch: false }};

    let matches = 0;
    let allMatch = true;
    const types = ['hard', 'soft', 'certs'];
    for (const t of types) {{
      const roleSetLower = new Set((roleData[t] || []).map(s => s.toLowerCase()));
      for (const userSkill of activeSkills[t]) {{
        if (roleSetLower.has(userSkill.toLowerCase())) {{
          matches++;
        }} else {{
          allMatch = false;
        }}
      }}
    }}
    return {{ matches, total, allMatch }};
  }}

  function applyFilters() {{
    const cards = document.querySelectorAll('.card');
    const hasCatFilter = activeCats.size > 0;
    const hasLvlFilter = activeLevels.size > 0;
    const hasSkillFilter = getTotalActiveSkills() > 0;

    let visibleCount = 0;

    cards.forEach(card => {{
      const cat = card.dataset.cat;
      const lvl = card.dataset.level;
      const roleId = card.dataset.roleId;
      const badge = card.querySelector('.match-badge');

      // Filtro cat/level
      const matchCat = !hasCatFilter || activeCats.has(cat);
      const matchLvl = !hasLvlFilter || activeLevels.has(lvl);

      // Reset clases
      card.classList.remove('dim', 'no-match');
      badge.classList.remove('visible', 'partial', 'low');
      badge.textContent = '';

      // Filtro de skills
      let passesSkillFilter = true;
      if (hasSkillFilter) {{
        const matchInfo = calculateMatch(roleId);
        const pct = Math.round((matchInfo.matches / matchInfo.total) * 100);

        if (mode === 'AND') {{
          // Modo TODAS: solo pasa si tiene TODAS las skills
          passesSkillFilter = matchInfo.allMatch && matchInfo.matches === matchInfo.total;
        }} else {{
          // Modo CUALQUIERA: pasa si tiene al menos una
          passesSkillFilter = matchInfo.matches > 0;
        }}

        // Mostrar badge de match si hay alguna coincidencia
        if (matchInfo.matches > 0) {{
          badge.textContent = `${{matchInfo.matches}}/${{matchInfo.total}} · ${{pct}}%`;
          badge.classList.add('visible');
          if (pct === 100) {{
            // Verde (default)
          }} else if (pct >= 50) {{
            badge.classList.add('partial');
          }} else {{
            badge.classList.add('low');
          }}
        }}
      }}

      const fullMatch = matchCat && matchLvl && passesSkillFilter;

      if (fullMatch) {{
        visibleCount++;
      }} else {{
        // Si solo falla por skill, usa 'no-match' (mas atenuado)
        if (matchCat && matchLvl && !passesSkillFilter) {{
          card.classList.add('no-match');
        }} else {{
          card.classList.add('dim');
        }}
      }}
    }});

    // Actualizar contador
    const counter = document.getElementById('matchCounter');
    if (hasSkillFilter || hasCatFilter || hasLvlFilter) {{
      counter.innerHTML = `<strong>${{visibleCount}}</strong> de ${{TOTAL_ROLES}} roles ${{hasSkillFilter ? 'matchean' : 'visibles'}}`;
    }} else {{
      counter.innerHTML = `<strong>${{TOTAL_ROLES}}</strong> roles visibles`;
    }}

    // Empty state
    document.getElementById('emptyState').classList.toggle('visible', visibleCount === 0 && (hasSkillFilter || hasCatFilter || hasLvlFilter));
  }}

  function renderActiveSkillsBar() {{
    const total = getTotalActiveSkills();
    const bar = document.getElementById('activeSkillsBar');
    const list = document.getElementById('activeSkillsList');

    if (total === 0) {{
      bar.classList.remove('visible');
      list.innerHTML = '';
      return;
    }}

    bar.classList.add('visible');
    const tags = [];
    const types = ['hard', 'soft', 'certs'];
    for (const t of types) {{
      for (const skill of activeSkills[t]) {{
        const skillEsc = skill.replace(/"/g, '&quot;');
        tags.push(`<span class="active-skill-tag" data-tag-type="${{t}}" data-tag-name="${{skillEsc}}">${{skill}}<span class="x">×</span></span>`);
      }}
    }}
    list.innerHTML = tags.join('');

    // Click en tag de skill activa la quita
    list.querySelectorAll('.active-skill-tag').forEach(tag => {{
      tag.addEventListener('click', () => {{
        const t = tag.dataset.tagType;
        const n = tag.dataset.tagName;
        activeSkills[t].delete(n);
        // Actualizar el chip correspondiente
        document.querySelectorAll(`[data-skill-type="${{t}}"][data-skill-name="${{n.replace(/"/g, '&quot;')}}"]`).forEach(c => c.classList.remove('active'));
        renderActiveSkillsBar();
        applyFilters();
      }});
    }});
  }}

  // Click en chip de skill
  document.querySelectorAll('.skill-chip-small').forEach(chip => {{
    chip.addEventListener('click', () => {{
      const type = chip.dataset.skillType;
      const name = chip.dataset.skillName;
      if (activeSkills[type].has(name)) {{
        activeSkills[type].delete(name);
        chip.classList.remove('active');
      }} else {{
        activeSkills[type].add(name);
        chip.classList.add('active');
      }}
      renderActiveSkillsBar();
      applyFilters();
    }});
  }});

  // Toggle AND/OR
  document.querySelectorAll('.mode-toggle button').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.mode-toggle button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      mode = btn.dataset.mode;
      applyFilters();
    }});
  }});

  // Buscador de skills
  document.getElementById('skillSearch').addEventListener('input', (e) => {{
    const q = e.target.value.trim().toLowerCase();
    document.querySelectorAll('.skill-chip-small').forEach(chip => {{
      const name = chip.dataset.skillName.toLowerCase();
      if (!q || name.includes(q)) {{
        chip.classList.remove('hidden');
      }} else {{
        chip.classList.add('hidden');
      }}
    }});
  }});

  // Limpiar skills
  document.getElementById('clearSkillsBtn').addEventListener('click', () => {{
    activeSkills = {{ hard: new Set(), soft: new Set(), certs: new Set() }};
    document.querySelectorAll('.skill-chip-small.active').forEach(c => c.classList.remove('active'));
    renderActiveSkillsBar();
    applyFilters();
  }});

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

  // Reset total
  document.getElementById('resetBtn').addEventListener('click', () => {{
    activeCats.clear();
    activeLevels.clear();
    activeSkills = {{ hard: new Set(), soft: new Set(), certs: new Set() }};
    document.querySelectorAll('.filter-chip.active, .skill-chip-small.active').forEach(c => c.classList.remove('active'));
    document.getElementById('skillSearch').value = '';
    document.querySelectorAll('.skill-chip-small.hidden').forEach(c => c.classList.remove('hidden'));
    renderActiveSkillsBar();
    applyFilters();
  }});

  // Click en card -> navegar a la version interactiva con el rol
  document.querySelectorAll('.card').forEach(card => {{
    card.addEventListener('click', (e) => {{
      // Si el click fue en el badge, no navega
      if (e.target.classList.contains('match-badge')) return;
      const roleId = card.dataset.roleId;
      window.location.href = `Mapa_Carreras_Ciberseguridad.html#role-${{roleId}}`;
    }});
  }});

  // Inicializar
  applyFilters();
</script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
