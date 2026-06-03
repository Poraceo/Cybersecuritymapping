"""
Genera Mapa_Mental_Carreras.html
Mapa mental visual: eje Y = nivel de seniority, eje X = categorías
Todos los 50 roles en una sola vista panorámica.
"""

LEVEL_ORDER = ['junior', 'mid', 'senior', 'manager', 'executive']

CSS = """
:root{
  --bg-deep:#0A0E1A;--bg-card:#131826;--bg-elevated:#1A2030;
  --border:#2A3149;--border-bright:#3A4566;
  --text-primary:#F8FAFC;--text-secondary:#CBD5E1;--text-muted:#94A3B8;--text-dim:#64748B;
  --accent-gold:#F59E0B;--accent-mint:#10B981;--accent-magenta:#EC4899;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg-deep);color:var(--text-primary);font-family:'Sora',sans-serif;min-height:100vh}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 1400px 900px at 70% 0%,rgba(245,158,11,0.05),transparent 60%),radial-gradient(ellipse 1200px 800px at 30% 100%,rgba(236,72,153,0.04),transparent 60%);pointer-events:none;z-index:0}
body::after{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.012) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.012) 1px,transparent 1px);background-size:80px 80px;pointer-events:none;z-index:0}
.mm-app{position:relative;z-index:1;max-width:1900px;margin:0 auto;padding:36px 48px 80px}

.mm-top{display:flex;justify-content:space-between;align-items:center;padding-bottom:24px;margin-bottom:32px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:16px}
.mm-brand{display:flex;align-items:center;gap:14px;font-family:'Bricolage Grotesque',serif;font-weight:700;font-size:22px;letter-spacing:-0.02em}
.mm-brand-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--accent-gold),var(--accent-magenta));border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:800;font-size:18px;color:var(--bg-deep)}
.mm-brand em{font-style:italic;color:var(--accent-gold)}
.mm-brand-meta{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase;margin-top:2px}
.mm-link{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);text-decoration:none;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s}
.mm-link:hover{background:var(--bg-elevated);color:var(--accent-gold);border-color:var(--accent-gold)}

.mm-hero{margin-bottom:32px}
.mm-hero-eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent-gold);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:12px}
.mm-hero-eyebrow::before{content:'';width:28px;height:1px;background:var(--accent-gold)}
.mm-hero-title{font-family:'Bricolage Grotesque',serif;font-size:clamp(40px,4.5vw,60px);font-weight:700;line-height:1;letter-spacing:-0.035em;margin-bottom:14px;background:linear-gradient(180deg,#FFFFFF,#94A3B8 130%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mm-hero-title em{font-style:italic;color:var(--accent-gold);-webkit-text-fill-color:var(--accent-gold);font-weight:500}
.mm-hero-sub{color:var(--text-secondary);font-size:16px;max-width:800px;line-height:1.55}

.mm-legend{display:flex;flex-wrap:wrap;gap:8px 14px;padding:18px 22px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;margin-bottom:40px;align-items:center}
.mm-legend::before{content:'CATEGORÍAS';font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.2em;padding-right:8px;border-right:1px solid var(--border);margin-right:4px}
.mm-legend-item{display:flex;align-items:center;gap:7px;font-size:12px;color:var(--text-secondary)}
.mm-legend-dot{width:10px;height:10px;border-radius:3px}
.mm-legend-label{font-weight:500}
.mm-legend-count{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);padding:1px 6px;background:rgba(255,255,255,0.05);border-radius:4px}

.mm-map{display:flex;flex-direction:column;gap:24px;position:relative}
.mm-map::before{
  content:'';position:absolute;left:88px;top:30px;bottom:30px;width:2px;
  background:linear-gradient(180deg,var(--accent-mint) 0%,var(--accent-mint) 25%,var(--accent-gold) 50%,var(--accent-magenta) 75%,var(--accent-magenta) 100%);
  opacity:0.4;z-index:0;border-radius:2px;
}

.mm-band{display:grid;grid-template-columns:200px 1fr;gap:36px;align-items:stretch;position:relative;z-index:1}

.mm-band-label{
  background:var(--bg-card);border:1px solid var(--border);border-radius:14px;
  padding:20px;display:flex;flex-direction:column;gap:4px;position:relative;
  border-left:4px solid var(--band-color);
}
.mm-band-label::after{
  content:'';position:absolute;right:-26px;top:50%;width:22px;height:2px;
  background:var(--band-color);transform:translateY(-1px);z-index:2;
}
.mm-band-label::before{
  content:'';position:absolute;right:-32px;top:50%;width:10px;height:10px;
  background:var(--band-color);border-radius:50%;transform:translate(0,-50%);
  box-shadow:0 0 12px var(--band-color);z-index:3;
}
.mm-band-num{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--band-color);letter-spacing:0.2em}
.mm-band-name{font-family:'Bricolage Grotesque',serif;font-size:22px;font-weight:700;letter-spacing:-0.025em;line-height:1.1;margin-top:4px}
.mm-band-years{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-muted);margin-top:4px}
.mm-band-count{margin-top:10px;padding-top:10px;border-top:1px solid var(--border);font-size:11px;color:var(--text-secondary);font-family:'JetBrains Mono',monospace;letter-spacing:0.1em}

.mm-band-cards{
  display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start;padding:4px 0;
  border-left:1px dashed var(--border);padding-left:24px;
}

.mm-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:10px;
  padding:10px 13px;min-width:175px;max-width:215px;position:relative;
  transition:all 0.2s;cursor:default;border-left:3px solid var(--card-color);
}
.mm-card:hover{
  background:var(--bg-elevated);transform:translateY(-2px);
  box-shadow:0 6px 16px rgba(0,0,0,0.4);border-color:var(--card-color);z-index:2;
}
.mm-card::before{
  content:'';position:absolute;top:0;right:0;width:50%;height:100%;
  background:linear-gradient(135deg,transparent 50%,var(--card-glow));
  pointer-events:none;border-radius:0 10px 10px 0;opacity:0.6;
}
.mm-card-num{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--text-dim);letter-spacing:0.15em;margin-bottom:3px;position:relative}
.mm-card-name{font-family:'Bricolage Grotesque',serif;font-size:14px;font-weight:600;letter-spacing:-0.015em;line-height:1.2;margin-bottom:5px;position:relative}
.mm-card-salary{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--accent-gold);font-weight:600;position:relative}

.mm-footer{margin-top:56px;padding-top:32px;border-top:1px solid var(--border);display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.mm-foot-block h4{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent-gold);letter-spacing:0.15em;text-transform:uppercase;margin-bottom:12px}
.mm-foot-block p{font-size:13px;color:var(--text-secondary);line-height:1.6}

@media print{
  body::before,body::after{display:none}
  .mm-app{padding:20px}
  .mm-link{display:none}
}

@media (max-width:1100px){
  .mm-band{grid-template-columns:1fr;gap:12px}
  .mm-band-label::after,.mm-band-label::before{display:none}
  .mm-map::before{display:none}
  .mm-band-cards{border-left:none;padding-left:0}
  .mm-footer{grid-template-columns:1fr}
}
@media (max-width:640px){
  .mm-app{padding:20px}
  .mm-card{min-width:140px}
}
"""


def hex_to_rgba(h, a):
    h = h.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{a})'


def build_mindmap(data, output_path):
    cfg = data['config']
    titulo = cfg.get('titulo', 'Mapa de Carreras')
    cats = data['categories']
    levels = data['levels']
    roles = data['roles']

    # Colores por nivel
    level_colors = {
        'junior': '#10B981',
        'mid': '#06B6D4',
        'senior': '#F59E0B',
        'manager': '#EC4899',
        'executive': '#C084FC'
    }

    # Construir bandas (una por nivel)
    bands_html = []
    for idx, level_key in enumerate(LEVEL_ORDER):
        if level_key not in levels:
            continue
        lvl = levels[level_key]
        level_roles = [r for r in roles if r.get('level') == level_key]
        band_color = level_colors.get(level_key, '#F59E0B')

        # Agrupar por categoría dentro del nivel, manteniendo orden de cats
        cards_html = []
        for cat_key in cats:
            cat_info = cats[cat_key]
            color = cat_info['color']
            for role in level_roles:
                if role.get('cat') != cat_key:
                    continue
                role_en = role['roleEN']
                # Acortar nombres largos
                if len(role_en) > 32:
                    parts = role_en.split('/')
                    if len(parts) > 1:
                        role_en_short = parts[0].strip()
                    else:
                        role_en_short = role_en[:30] + '…'
                else:
                    role_en_short = role_en

                # Sacar el tope del salario
                sal = role.get('salaryMonth', '')
                if '-' in sal:
                    salary_max = sal.split('-')[-1].strip()
                else:
                    salary_max = sal

                title_attr = f"{role['roleEN']} — {role.get('roleES', '')}"

                card = f'''<div class="mm-card" style="--card-color:{color};--card-glow:{hex_to_rgba(color, 0.12)};" title="{title_attr}">
                    <div class="mm-card-num">#{role['id']:02d} · {cat_info['label'].split('/')[0].strip()}</div>
                    <div class="mm-card-name">{role_en_short}</div>
                    <div class="mm-card-salary">hasta {salary_max}/mes</div>
                </div>'''
                cards_html.append(card)

        band = f'''<div class="mm-band">
            <div class="mm-band-label" style="--band-color:{band_color};">
                <div class="mm-band-num">/ NIVEL {idx + 1:02d}</div>
                <div class="mm-band-name">{lvl['label']}</div>
                <div class="mm-band-years">{lvl['yearsRange']}</div>
                <div class="mm-band-count">{len(level_roles)} roles</div>
            </div>
            <div class="mm-band-cards">{''.join(cards_html)}</div>
        </div>'''
        bands_html.append(band)

    # Leyenda de categorías
    legend_items = []
    for key, cat in cats.items():
        count = sum(1 for r in roles if r.get('cat') == key)
        legend_items.append(f'''<div class="mm-legend-item">
            <span class="mm-legend-dot" style="background:{cat['color']}"></span>
            <span class="mm-legend-label">{cat['label']}</span>
            <span class="mm-legend-count">{count}</span>
        </div>''')

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mapa Mental · {titulo}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Sora:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="mm-app">
  <div class="mm-top">
    <div class="mm-brand">
      <div class="mm-brand-mark">⌘</div>
      <div>
        <div>Cyber<em>.map</em> <span style="font-size:13px;color:var(--text-muted);font-weight:400;margin-left:6px">/ Vista panorámica</span></div>
        <div class="mm-brand-meta">MAPA MENTAL · {len(roles)} ROLES · {len(LEVEL_ORDER)} NIVELES</div>
      </div>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <a class="mm-link" href="Mapa_General_Carreras.html">→ Mapa general</a>
      <a class="mm-link" href="Mapa_Carreras_Ciberseguridad.html">→ Versión interactiva</a>
      <a class="mm-link" href="Catalogo_Certificaciones.html" style="color:var(--accent-gold);border-color:var(--accent-gold)">📜 Catálogo de certs</a>
    </div>
  </div>

  <div class="mm-hero">
    <div class="mm-hero-eyebrow">VISTA PANORÁMICA · TODOS LOS ROLES EN UNA PANTALLA</div>
    <h1 class="mm-hero-title">El universo de la <em>ciberseguridad</em>,<br>de un solo vistazo.</h1>
    <p class="mm-hero-sub">El eje vertical muestra la progresión de seniority — desde Junior hasta C-Level. Las tarjetas dentro de cada banda están agrupadas por categoría (color del borde izquierdo). Pasa el cursor sobre cualquier rol para ver su nombre completo.</p>
  </div>

  <div class="mm-legend">
    {''.join(legend_items)}
  </div>

  <div class="mm-map">
    {''.join(bands_html)}
  </div>

  <div class="mm-footer">
    <div class="mm-foot-block">
      <h4>Cómo leer este mapa</h4>
      <p>Verticalmente: la progresión de carrera. Cada nivel agrupa los roles típicos de ese rango de experiencia. Horizontalmente, dentro de cada banda, los roles están agrupados por categoría (color en el borde izquierdo de cada tarjeta).</p>
    </div>
    <div class="mm-foot-block">
      <h4>El salario que ves</h4>
      <p>Es el tope mensual del rango global — lo que ganaría un Senior trabajando para USA. El mínimo del rango (no mostrado aquí) corresponde a entry-level en mercados LATAM. Ver la versión interactiva para rango completo y detalles.</p>
    </div>
    <div class="mm-foot-block">
      <h4>Línea de tiempo</h4>
      <p>La línea de color a la izquierda conecta los niveles para visualizar el flujo de una carrera completa: del verde (Junior) al magenta/morado (C-Level). No todos los caminos son lineales — hay saltos laterales, pivotes y caminos paralelos.</p>
    </div>
  </div>
</div>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
