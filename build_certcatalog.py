"""
Genera Catalogo_Certificaciones.html
Vista dedicada de TODAS las certificaciones con info oficial.
Filtros por vendor, búsqueda por texto, ordenamiento por precio/dificultad.
"""

import json


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

.app{position:relative;z-index:1;max-width:1600px;margin:0 auto;padding:32px 36px 60px}

.top{display:flex;justify-content:space-between;align-items:center;padding-bottom:20px;margin-bottom:24px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:16px}
.brand{display:flex;align-items:center;gap:14px;font-family:'Bricolage Grotesque',serif;font-weight:700;font-size:22px;letter-spacing:-0.02em}
.brand-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--gold),var(--magenta));border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:800;font-size:18px;color:var(--bg-deep)}
.brand em{font-style:italic;color:var(--gold)}
.brand-meta{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase;margin-top:2px}
.nav-links{display:flex;gap:10px;flex-wrap:wrap}
.nav-link{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);text-decoration:none;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s}
.nav-link:hover{background:var(--bg-elevated);color:var(--gold);border-color:var(--gold)}

.hero{margin-bottom:28px}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--gold);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:12px;display:flex;align-items:center;gap:12px}
.eyebrow::before{content:'';width:28px;height:1px;background:var(--gold)}
.title{font-family:'Bricolage Grotesque',serif;font-size:clamp(36px,4vw,52px);font-weight:700;line-height:1;letter-spacing:-0.035em;margin-bottom:10px}
.title em{font-style:italic;color:var(--gold);font-weight:500}
.subtitle{color:var(--text-secondary);font-size:14px;max-width:800px;line-height:1.55}

/* Stats */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:24px}
.stat{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}
.stat-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase}
.stat-value{font-family:'Bricolage Grotesque',serif;font-size:28px;font-weight:700;color:var(--gold);letter-spacing:-0.02em}
.stat-sub{font-size:11px;color:var(--text-secondary)}

/* Controls */
.controls{display:flex;gap:14px;padding:16px 20px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;margin-bottom:20px;flex-wrap:wrap;align-items:center}
.control-search{flex:1;min-width:240px;display:flex;align-items:center;gap:10px;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px;padding:8px 16px;transition:border 0.2s}
.control-search:focus-within{border-color:var(--gold)}
.control-search input{flex:1;background:none;border:none;color:var(--text-primary);font-family:'Sora',sans-serif;font-size:13px;outline:none}
.control-search input::placeholder{color:var(--text-dim)}
.control-search-icon{color:var(--text-muted);font-size:14px}
.sort-select{background:var(--bg-deep);border:1px solid var(--border);border-radius:100px;padding:8px 14px;color:var(--text-primary);font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.1em;text-transform:uppercase;cursor:pointer;outline:none}
.sort-select:focus{border-color:var(--gold)}
.match-counter{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);padding:6px 14px;background:var(--bg-deep);border:1px solid var(--border);border-radius:100px}
.match-counter strong{color:var(--gold);font-size:13px;font-weight:700}

/* Vendor chips */
.vendor-filters{display:flex;gap:8px;padding:14px 20px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;margin-bottom:24px;flex-wrap:wrap;align-items:center}
.vendor-filters-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:0.2em;text-transform:uppercase;padding-right:8px;border-right:1px solid var(--border);margin-right:4px}
.vendor-chip{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);padding:5px 12px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:100px;cursor:pointer;transition:all 0.15s;display:inline-flex;align-items:center;gap:5px}
.vendor-chip:hover{background:rgba(255,255,255,0.08);color:var(--text-primary)}
.vendor-chip.active{background:var(--gold);color:var(--bg-deep);border-color:var(--gold);font-weight:600}
.vendor-chip .count{opacity:0.6;font-size:10px}
.vendor-chip.active .count{opacity:0.9}
.reset-btn{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);background:none;border:none;cursor:pointer;text-decoration:underline;letter-spacing:0.1em;text-transform:uppercase;padding:5px 8px}
.reset-btn:hover{color:var(--gold)}

/* Cert cards */
.certs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px}
.cert-card{background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--gold);border-radius:12px;padding:18px 20px;text-decoration:none;color:inherit;transition:all 0.2s;display:flex;flex-direction:column;gap:10px;position:relative;cursor:pointer}
.cert-card:hover{background:var(--bg-elevated);border-color:var(--gold);transform:translateY(-2px);box-shadow:0 8px 24px rgba(245,158,11,0.15)}
.cert-card.hidden{display:none}
.cert-card-header{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.cert-card-acronym{font-family:'Bricolage Grotesque',serif;font-size:22px;font-weight:700;color:var(--gold);letter-spacing:-0.025em;line-height:1.1}
.cert-card-arrow{color:var(--gold);font-size:14px;flex-shrink:0;opacity:0.7;transition:transform 0.2s}
.cert-card:hover .cert-card-arrow{transform:translate(3px,-3px);opacity:1}
.cert-card-fullname{font-size:13px;color:var(--text-secondary);line-height:1.4;font-style:italic;min-height:36px}
.cert-card-meta{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;font-size:11px;font-family:'JetBrains Mono',monospace;padding-top:10px;border-top:1px solid var(--border)}
.cert-card-label{color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;font-size:10px;padding-top:1px}
.cert-card-value{color:var(--text-primary);font-weight:500}
.cert-card-value.price{color:var(--gold);font-weight:700;font-size:12px}
.cert-card-notes{font-size:11px;color:var(--text-muted);font-style:italic;line-height:1.4;padding:8px 10px;background:rgba(255,255,255,0.03);border-radius:6px;border-left:2px solid rgba(245,158,11,0.4)}
.cert-card-cta{font-size:11px;color:var(--gold);font-family:'JetBrains Mono',monospace;letter-spacing:0.05em;display:flex;align-items:center;gap:5px;margin-top:auto;padding-top:6px}
.cert-card-cta::before{content:'→'}
.cert-card.basic{border-left-color:var(--text-dim);opacity:0.7;cursor:default}
.cert-card.basic:hover{transform:none;background:var(--bg-card);box-shadow:none}

/* Difficulty badge */
.cert-card-diff{position:absolute;top:18px;right:42px;font-family:'JetBrains Mono',monospace;font-size:8px;font-weight:700;padding:2px 7px;border-radius:100px;letter-spacing:0.1em;text-transform:uppercase}
.cert-card-diff.beginner{background:rgba(16,185,129,0.2);color:var(--mint)}
.cert-card-diff.intermediate{background:rgba(6,182,212,0.2);color:var(--cyan)}
.cert-card-diff.advanced{background:rgba(245,158,11,0.2);color:var(--gold)}
.cert-card-diff.expert{background:rgba(236,72,153,0.2);color:var(--magenta)}

/* Empty state */
.empty-state{padding:60px 20px;text-align:center;color:var(--text-muted);font-family:'JetBrains Mono',monospace;display:none}
.empty-state.visible{display:block}
.empty-state h4{font-family:'Bricolage Grotesque',serif;font-size:24px;color:var(--text-primary);margin-bottom:8px}

@media (max-width:640px){
  .app{padding:20px 16px}
  .certs-grid{grid-template-columns:1fr}
}
"""


def build_catalog(data, output_path):
    certs_lookup = data.get('certsLookup', {})
    # Deduplicar (los aliases apuntan al mismo cert) usando shortName como llave
    seen = set()
    certs = []
    for cert in certs_lookup.values():
        sn = cert.get('shortName', '')
        if sn and sn not in seen:
            seen.add(sn)
            certs.append(cert)
    # Ordenar alfabéticamente por shortName
    certs.sort(key=lambda c: c.get('shortName', '').lower())

    # Recolectar vendors únicos
    vendor_count = {}
    for c in certs:
        v = c.get('vendor', 'Otros') or 'Otros'
        vendor_count[v] = vendor_count.get(v, 0) + 1
    vendors_sorted = sorted(vendor_count.items(), key=lambda x: (-x[1], x[0]))

    # Stats
    n_total = len(certs)
    n_free = sum(1 for c in certs if c.get('priceUSD') == 0)
    n_paid = sum(1 for c in certs if c.get('priceUSD') and c.get('priceUSD') > 0)
    avg_price = 0
    if n_paid > 0:
        avg_price = int(sum(c.get('priceUSD', 0) for c in certs if c.get('priceUSD') and c.get('priceUSD') > 0) / n_paid)
    n_vendors = len(vendor_count)

    # Generar cards HTML
    cards_html = []
    for c in certs:
        acronym = c.get('shortName', '')
        fullname = c.get('fullName', '')
        vendor = c.get('vendor', '—') or '—'
        price = c.get('priceUSD')
        if price == 0:
            price_str = 'Gratis'
        elif price is None:
            price_str = 'No publicado'
        else:
            price_str = f'${price:,} USD'
        prep = c.get('prepTime', '—') or '—'
        diff = c.get('difficulty', '—') or '—'
        validity = c.get('validity', '—') or '—'
        url = c.get('officialUrl', '')
        notes = c.get('notes', '')
        # Data attrs for filtering
        data_vendor = vendor.replace('"', '&quot;')
        diff_class = diff.lower() if diff else ''
        # Para búsqueda: incluir acronym, fullname, vendor
        searchable = f"{acronym} {fullname} {vendor}".lower().replace('"', '&quot;')

        if url:
            cards_html.append(f'''<a class="cert-card" href="{url}" target="_blank" rel="noopener" data-vendor="{data_vendor}" data-search="{searchable}" data-price="{price if price is not None else -1}" data-diff="{diff}">
                <div class="cert-card-header">
                    <span class="cert-card-acronym">{acronym}</span>
                    <span class="cert-card-arrow">↗</span>
                </div>
                {f'<span class="cert-card-diff {diff_class}">{diff}</span>' if diff and diff != '—' else ''}
                <div class="cert-card-fullname">{fullname}</div>
                <div class="cert-card-meta">
                    <span class="cert-card-label">Vendor</span><span class="cert-card-value">{vendor}</span>
                    <span class="cert-card-label">Precio</span><span class="cert-card-value price">{price_str}</span>
                    <span class="cert-card-label">Prep</span><span class="cert-card-value">{prep}</span>
                    <span class="cert-card-label">Vigencia</span><span class="cert-card-value">{validity}</span>
                </div>
                {f'<div class="cert-card-notes">⚠️ {notes}</div>' if notes else ''}
                <div class="cert-card-cta">Ir al sitio oficial</div>
            </a>''')
        else:
            cards_html.append(f'''<div class="cert-card basic" data-vendor="{data_vendor}" data-search="{searchable}" data-price="-1" data-diff="">
                <div class="cert-card-header">
                    <span class="cert-card-acronym">{acronym}</span>
                </div>
                <div class="cert-card-fullname">{fullname}</div>
                {f'<div class="cert-card-notes">⚠️ {notes}</div>' if notes else ''}
            </div>''')

    # Vendor chips
    vendor_chips = []
    for v, count in vendors_sorted:
        v_attr = v.replace('"', '&quot;')
        vendor_chips.append(f'<button class="vendor-chip" data-vendor-filter="{v_attr}">{v}<span class="count">{count}</span></button>')

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Catálogo de Certificaciones · Cyber.map</title>
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
        <div>Cyber<em>.map</em> <span style="font-size:13px;color:var(--text-muted);font-weight:400;margin-left:6px">/ Catálogo de certificaciones</span></div>
        <div class="brand-meta">{n_total} CERTIFICACIONES · {n_vendors} VENDORS · INFO OFICIAL</div>
      </div>
    </div>
    <div class="nav-links">
      <a class="nav-link" href="Mapa_General_Carreras.html">← Mapa general</a>
      <a class="nav-link" href="Mapa_Carreras_Ciberseguridad.html">← Detalle por rol</a>
    </div>
  </div>

  <div class="hero">
    <div class="eyebrow">CATÁLOGO COMPLETO · INFO VERIFICADA EN SITIOS OFICIALES</div>
    <h1 class="title">Todas las <em>certificaciones</em> que importan.</h1>
    <p class="subtitle">Cada certificación con su nombre completo, vendor oficial, precio en USD, tiempo de preparación, dificultad y vigencia. Haz click en cualquier tarjeta para ir directamente al sitio oficial del proveedor.</p>
  </div>

  <!-- Stats -->
  <div class="stats">
    <div class="stat">
      <div class="stat-label">Total certificaciones</div>
      <div class="stat-value">{n_total}</div>
      <div class="stat-sub">Investigadas en fuentes oficiales</div>
    </div>
    <div class="stat">
      <div class="stat-label">Vendors/Emisores</div>
      <div class="stat-value">{n_vendors}</div>
      <div class="stat-sub">ISC2, CompTIA, GIAC, etc.</div>
    </div>
    <div class="stat">
      <div class="stat-label">Precio promedio</div>
      <div class="stat-value">${avg_price:,}</div>
      <div class="stat-sub">USD · examen estándar</div>
    </div>
    <div class="stat">
      <div class="stat-label">Certs gratis</div>
      <div class="stat-value">{n_free}</div>
      <div class="stat-sub">Costo $0 USD</div>
    </div>
  </div>

  <!-- Search + Sort -->
  <div class="controls">
    <div class="control-search">
      <span class="control-search-icon">🔍</span>
      <input type="text" id="searchInput" placeholder="Buscar por nombre, acrónimo, vendor (ej: CISSP, ISC2, cloud...)">
    </div>
    <select class="sort-select" id="sortSelect">
      <option value="name">A → Z</option>
      <option value="price-asc">Precio: bajo a alto</option>
      <option value="price-desc">Precio: alto a bajo</option>
      <option value="difficulty">Por dificultad</option>
    </select>
    <span class="match-counter" id="matchCounter"><strong>{n_total}</strong> visibles</span>
  </div>

  <!-- Filtros por vendor -->
  <div class="vendor-filters">
    <span class="vendor-filters-label">Vendor</span>
    {''.join(vendor_chips)}
    <button class="reset-btn" id="resetBtn">× Limpiar</button>
  </div>

  <!-- Grid de certs -->
  <div class="certs-grid" id="certsGrid">
    {''.join(cards_html)}
  </div>

  <div class="empty-state" id="emptyState">
    <h4>Ninguna certificación coincide</h4>
    <p>Prueba con otros términos o quita filtros</p>
  </div>
</div>

<script>
  const activeVendors = new Set();
  let currentSort = 'name';
  let currentSearch = '';

  function applyFilters() {{
    const cards = document.querySelectorAll('.cert-card');
    let visible = 0;
    cards.forEach(card => {{
      const v = card.dataset.vendor;
      const s = card.dataset.search || '';
      const matchVendor = activeVendors.size === 0 || activeVendors.has(v);
      const matchSearch = !currentSearch || s.includes(currentSearch);
      if (matchVendor && matchSearch) {{
        card.classList.remove('hidden');
        visible++;
      }} else {{
        card.classList.add('hidden');
      }}
    }});
    document.getElementById('matchCounter').innerHTML = `<strong>${{visible}}</strong> visibles`;
    document.getElementById('emptyState').classList.toggle('visible', visible === 0);
  }}

  function applySort() {{
    const grid = document.getElementById('certsGrid');
    const cards = Array.from(grid.querySelectorAll('.cert-card'));
    const diffOrder = {{'Beginner': 1, 'Intermediate': 2, 'Advanced': 3, 'Expert': 4, '': 5, '—': 5}};
    cards.sort((a, b) => {{
      if (currentSort === 'name') {{
        return a.querySelector('.cert-card-acronym').textContent.localeCompare(b.querySelector('.cert-card-acronym').textContent);
      }} else if (currentSort === 'price-asc') {{
        const pa = parseInt(a.dataset.price);
        const pb = parseInt(b.dataset.price);
        if (pa === -1) return 1;
        if (pb === -1) return -1;
        return pa - pb;
      }} else if (currentSort === 'price-desc') {{
        const pa = parseInt(a.dataset.price);
        const pb = parseInt(b.dataset.price);
        if (pa === -1) return 1;
        if (pb === -1) return -1;
        return pb - pa;
      }} else if (currentSort === 'difficulty') {{
        return (diffOrder[a.dataset.diff] || 5) - (diffOrder[b.dataset.diff] || 5);
      }}
      return 0;
    }});
    cards.forEach(c => grid.appendChild(c));
  }}

  // Vendor filter chips
  document.querySelectorAll('[data-vendor-filter]').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const v = btn.dataset.vendorFilter;
      if (activeVendors.has(v)) {{
        activeVendors.delete(v);
        btn.classList.remove('active');
      }} else {{
        activeVendors.add(v);
        btn.classList.add('active');
      }}
      applyFilters();
    }});
  }});

  // Search
  document.getElementById('searchInput').addEventListener('input', e => {{
    currentSearch = e.target.value.trim().toLowerCase();
    applyFilters();
  }});

  // Sort
  document.getElementById('sortSelect').addEventListener('change', e => {{
    currentSort = e.target.value;
    applySort();
  }});

  // Reset
  document.getElementById('resetBtn').addEventListener('click', () => {{
    activeVendors.clear();
    document.querySelectorAll('.vendor-chip.active').forEach(c => c.classList.remove('active'));
    document.getElementById('searchInput').value = '';
    currentSearch = '';
    applyFilters();
  }});
</script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
