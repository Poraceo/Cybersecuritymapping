"""
Genera Mapa_Carreras_Ciberseguridad.html (la app interactiva navegable)
"""
import json

CSS = """
:root {
  --bg-deep: #0A0E1A; --bg-card: #131826; --bg-card-hover: #1A2030; --bg-elevated: #1E2538;
  --border: #2A3149; --border-bright: #3A4566;
  --text-primary: #F8FAFC; --text-secondary: #CBD5E1; --text-muted: #94A3B8; --text-dim: #64748B;
  --accent-gold: #F59E0B; --accent-gold-glow: rgba(245,158,11,0.15);
  --accent-mint: #10B981; --accent-cyan: #06B6D4; --accent-magenta: #EC4899;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg-deep);color:var(--text-primary);font-family:'Sora',sans-serif;font-size:16px;line-height:1.5;min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 1200px 800px at 80% -10%,rgba(245,158,11,0.06),transparent 60%),radial-gradient(ellipse 1000px 700px at -10% 100%,rgba(16,185,129,0.05),transparent 60%);pointer-events:none;z-index:0}
body::after{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;z-index:0;mask-image:radial-gradient(ellipse at center,black 30%,transparent 80%)}
.app{position:relative;z-index:1;max-width:1600px;margin:0 auto;padding:32px 48px 80px}
.top-bar{display:flex;justify-content:space-between;align-items:center;margin-bottom:48px;padding-bottom:24px;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:16px}
.brand{display:flex;align-items:center;gap:14px;font-family:'Bricolage Grotesque',serif;font-weight:700;font-size:22px;letter-spacing:-0.02em;cursor:pointer}
.brand-mark{width:38px;height:38px;background:linear-gradient(135deg,var(--accent-gold),var(--accent-magenta));border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:800;font-size:20px;color:var(--bg-deep)}
.brand-text{display:flex;flex-direction:column;line-height:1.05}
.brand-text span:last-child{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);font-weight:500;letter-spacing:0.15em;text-transform:uppercase}
.brand em{font-style:italic;color:var(--accent-gold)}
.top-right{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.view-link{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);text-decoration:none;padding:8px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;letter-spacing:0.1em;text-transform:uppercase;transition:all 0.2s}
.view-link:hover{background:var(--bg-elevated);color:var(--accent-gold);border-color:var(--accent-gold)}
.breadcrumb{display:flex;align-items:center;gap:10px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-muted);flex-wrap:wrap}
.breadcrumb a{color:var(--text-secondary);text-decoration:none;cursor:pointer;padding:4px 10px;border-radius:6px;background:rgba(255,255,255,0.04);transition:all 0.2s}
.breadcrumb a:hover{background:rgba(255,255,255,0.08);color:var(--text-primary)}
.breadcrumb-sep{color:var(--text-dim)}
.breadcrumb-current{color:var(--accent-gold);font-weight:500;padding:4px 10px}
.home{animation:fadeIn 0.5s ease}
.hero{margin-bottom:64px}
.hero-eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent-gold);text-transform:uppercase;letter-spacing:0.2em;margin-bottom:16px;display:flex;align-items:center;gap:12px}
.hero-eyebrow::before{content:'';width:24px;height:1px;background:var(--accent-gold)}
.hero-title{font-family:'Bricolage Grotesque',serif;font-size:clamp(48px,6vw,88px);font-weight:700;line-height:0.98;letter-spacing:-0.04em;margin-bottom:24px;background:linear-gradient(180deg,#FFFFFF 30%,#94A3B8 130%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-title em{font-style:italic;color:var(--accent-gold);-webkit-text-fill-color:var(--accent-gold);font-weight:500}
.hero-sub{font-size:19px;color:var(--text-secondary);max-width:720px;line-height:1.55}
.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin:48px 0 64px}
.stat{padding:24px 28px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;position:relative;overflow:hidden}
.stat::after{content:'';position:absolute;top:0;left:0;width:3px;height:24px;background:var(--accent);border-radius:0 3px 3px 0}
.stat[data-c="gold"]{--accent:var(--accent-gold)}.stat[data-c="mint"]{--accent:var(--accent-mint)}.stat[data-c="cyan"]{--accent:var(--accent-cyan)}.stat[data-c="magenta"]{--accent:var(--accent-magenta)}
.stat-label{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-muted);margin-bottom:8px}
.stat-value{font-family:'Bricolage Grotesque',serif;font-size:36px;font-weight:700;letter-spacing:-0.03em;line-height:1}
.stat-value small{font-size:14px;color:var(--text-muted);font-weight:400;margin-left:4px}
.choice-section{margin-top:64px}
.section-header{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:32px}
.section-title{font-family:'Bricolage Grotesque',serif;font-size:32px;font-weight:600;letter-spacing:-0.02em}
.section-num{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-muted)}
.choice-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.choice-card{background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:32px;cursor:pointer;transition:all 0.3s;position:relative;overflow:hidden;min-height:260px;display:flex;flex-direction:column;justify-content:space-between}
.choice-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--c-glow),transparent 60%);opacity:0;transition:opacity 0.3s}
.choice-card:hover{transform:translateY(-4px);border-color:var(--c-color)}
.choice-card:hover::before{opacity:1}
.choice-card[data-c="gold"]{--c-color:var(--accent-gold);--c-glow:rgba(245,158,11,0.10)}
.choice-card[data-c="mint"]{--c-color:var(--accent-mint);--c-glow:rgba(16,185,129,0.10)}
.choice-card[data-c="magenta"]{--c-color:var(--accent-magenta);--c-glow:rgba(236,72,153,0.10)}
.choice-num{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--c-color);letter-spacing:0.15em;position:relative;z-index:1}
.choice-icon{width:56px;height:56px;background:var(--c-glow);border:1px solid var(--c-color);border-radius:14px;display:flex;align-items:center;justify-content:center;color:var(--c-color);position:relative;z-index:1}
.choice-title{font-family:'Bricolage Grotesque',serif;font-size:28px;font-weight:700;letter-spacing:-0.025em;line-height:1.05;position:relative;z-index:1}
.choice-desc{color:var(--text-secondary);font-size:15px;line-height:1.55;position:relative;z-index:1}
.choice-cta{display:flex;align-items:center;gap:8px;font-family:'JetBrains Mono',monospace;font-size:12px;text-transform:uppercase;letter-spacing:0.15em;color:var(--c-color);position:relative;z-index:1}
.list-view{animation:fadeIn 0.4s ease}
.list-header{margin-bottom:48px}
.list-eyebrow{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--accent-gold);text-transform:uppercase;letter-spacing:0.2em;margin-bottom:14px}
.list-title{font-family:'Bricolage Grotesque',serif;font-size:clamp(40px,5vw,64px);font-weight:700;letter-spacing:-0.03em;line-height:1;margin-bottom:18px}
.list-sub{font-size:17px;color:var(--text-secondary);max-width:700px}
.level-grid,.category-grid{display:grid;gap:18px}
.level-grid{grid-template-columns:repeat(5,1fr)}
.category-grid{grid-template-columns:repeat(4,1fr)}
.tile{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;cursor:pointer;transition:all 0.25s;position:relative;overflow:hidden;min-height:180px;display:flex;flex-direction:column;justify-content:space-between}
.tile:hover{transform:translateY(-3px);border-color:var(--tile-color)}
.tile::after{content:'';position:absolute;top:0;left:0;width:100%;height:4px;background:var(--tile-color)}
.tile-count{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-muted);letter-spacing:0.15em;text-transform:uppercase}
.tile-label{font-family:'Bricolage Grotesque',serif;font-size:24px;font-weight:700;letter-spacing:-0.02em;line-height:1.1}
.tile-meta{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-muted)}
.tile-desc{font-size:13px;color:var(--text-secondary);line-height:1.4}
.roles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:8px}
.role-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:22px;cursor:pointer;transition:all 0.25s;position:relative;display:flex;flex-direction:column;gap:12px}
.role-card:hover{transform:translateY(-3px);border-color:var(--role-color);background:var(--bg-card-hover)}
.role-card::before{content:'';position:absolute;top:0;left:0;width:3px;height:60%;background:var(--role-color);border-radius:0 3px 3px 0}
.role-card-top{display:flex;justify-content:space-between;align-items:flex-start}
.role-cat-badge{font-family:'JetBrains Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:0.15em;padding:4px 10px;border-radius:4px;background:var(--role-glow);color:var(--role-color);border:1px solid var(--role-color)}
.role-id{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-dim)}
.role-name{font-family:'Bricolage Grotesque',serif;font-size:20px;font-weight:700;letter-spacing:-0.02em;line-height:1.15}
.role-name-es{font-size:13px;color:var(--text-muted);margin-top:2px}
.role-salary{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--accent-gold);font-weight:600;display:flex;align-items:center;gap:6px}
.role-salary::before{content:'$';width:20px;height:20px;background:var(--accent-gold-glow);border:1px solid var(--accent-gold);border-radius:4px;display:inline-flex;align-items:center;justify-content:center;font-weight:800}
.role-meta-row{display:flex;gap:8px;flex-wrap:wrap;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em}
.role-meta-row span{padding:3px 8px;background:rgba(255,255,255,0.04);border-radius:4px}
.demand-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}
.demand-very-high{background:var(--accent-mint);box-shadow:0 0 8px var(--accent-mint)}
.demand-high{background:var(--accent-cyan)}
.demand-medium{background:var(--accent-gold)}
.common-skills{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:32px;margin-bottom:40px;position:relative;overflow:hidden}
.common-skills::before{content:'';position:absolute;top:0;right:0;width:300px;height:100%;background:radial-gradient(circle at top right,var(--accent-gold-glow),transparent 70%);pointer-events:none}
.common-skills h3{font-family:'Bricolage Grotesque',serif;font-size:20px;font-weight:600;margin-bottom:6px;letter-spacing:-0.02em;position:relative}
.common-skills h3 small{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-muted);font-weight:400;margin-left:10px;letter-spacing:0.1em;text-transform:uppercase}
.common-skills-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:18px;position:relative}
.common-skills-col h4{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--accent-gold);letter-spacing:0.15em;text-transform:uppercase;margin-bottom:12px}
.skill-chips{display:flex;flex-wrap:wrap;gap:6px}
.skill-chip{font-size:13px;padding:5px 12px;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:100px;color:var(--text-secondary)}
.detail{animation:fadeIn 0.4s ease}
.detail-hero{background:var(--bg-card);border:1px solid var(--border);border-radius:24px;padding:48px;margin-bottom:32px;position:relative;overflow:hidden}
.detail-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 600px 400px at 100% 0%,var(--detail-glow),transparent 60%);pointer-events:none}
.detail-hero-top{display:flex;gap:14px;margin-bottom:24px;position:relative;flex-wrap:wrap}
.detail-badge{font-family:'JetBrains Mono',monospace;font-size:11px;padding:6px 14px;border-radius:6px;text-transform:uppercase;letter-spacing:0.15em;font-weight:500}
.detail-cat-badge{background:var(--detail-glow);color:var(--detail-color);border:1px solid var(--detail-color)}
.detail-level-badge{background:rgba(255,255,255,0.06);color:var(--text-secondary);border:1px solid var(--border)}
.detail-id{margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-muted);letter-spacing:0.15em}
.detail-title{font-family:'Bricolage Grotesque',serif;font-size:clamp(40px,5.5vw,72px);font-weight:700;letter-spacing:-0.035em;line-height:1;margin-bottom:12px;position:relative;background:linear-gradient(180deg,#FFFFFF,#94A3B8 130%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.detail-subtitle{font-size:20px;color:var(--text-secondary);margin-bottom:6px;position:relative}
.detail-synonyms{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text-muted);position:relative}
.detail-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:36px;position:relative}
.detail-stat{border-left:2px solid var(--detail-color);padding-left:18px}
.detail-stat-label{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:0.15em;color:var(--text-muted);margin-bottom:6px}
.detail-stat-value{font-family:'Bricolage Grotesque',serif;font-size:22px;font-weight:700;letter-spacing:-0.02em;line-height:1.1}
.detail-stat-value.money{color:var(--accent-gold);font-family:'JetBrains Mono',monospace;font-size:18px;font-weight:600}
.detail-body{display:grid;grid-template-columns:1.5fr 1fr;gap:32px;margin-bottom:32px}
.detail-section{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:28px}
.detail-section h3{font-family:'Bricolage Grotesque',serif;font-size:19px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;display:flex;align-items:center;gap:10px}
.detail-section h3::before{content:'';width:4px;height:18px;background:var(--detail-color);border-radius:2px}
.detail-text{color:var(--text-secondary);font-size:15px;line-height:1.65}
.skill-group-title{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--detail-color);letter-spacing:0.15em;text-transform:uppercase;margin-bottom:12px;margin-top:18px}
.skill-group-title:first-child{margin-top:0}
.chips-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.chip{font-size:13px;padding:6px 13px;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:100px;color:var(--text-secondary)}
.chip-tool{color:var(--accent-cyan);border-color:rgba(6,182,212,0.3)}
.chip-cert{color:var(--accent-gold);border-color:rgba(245,158,11,0.3)}

/* === CERT CARDS visibles (info completa de cada cert) === */
.cert-cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;margin-top:14px}
.cert-card{background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--accent-gold);border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit;transition:all 0.2s;display:flex;flex-direction:column;gap:8px;position:relative;cursor:pointer}
.cert-card:hover{background:var(--bg-elevated);border-color:var(--accent-gold);transform:translateY(-2px);box-shadow:0 6px 18px rgba(245,158,11,0.15)}
.cert-card-basic{border-left-color:var(--text-dim);opacity:0.6;cursor:default}
.cert-card-basic:hover{transform:none;background:var(--bg-card);box-shadow:none}
.cert-card-header{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.cert-card-acronym{font-family:'Bricolage Grotesque',serif;font-size:18px;font-weight:700;color:var(--accent-gold);letter-spacing:-0.02em;line-height:1.1}
.cert-card-arrow{color:var(--accent-gold);font-size:13px;flex-shrink:0;opacity:0.7;transition:transform 0.2s}
.cert-card:hover .cert-card-arrow{transform:translate(2px,-2px);opacity:1}
.cert-card-fullname{font-size:13px;color:var(--text-secondary);line-height:1.4;font-style:italic}
.cert-card-meta{display:grid;grid-template-columns:auto 1fr;gap:5px 14px;font-size:11px;font-family:'JetBrains Mono',monospace;padding-top:8px;border-top:1px solid var(--border)}
.cert-card-label{color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;font-size:10px;padding-top:1px}
.cert-card-value{color:var(--text-primary);font-weight:500}
.cert-card-value.price{color:var(--accent-gold);font-weight:700;font-size:12px}
.cert-card-notes{margin-top:6px;font-size:11px;color:var(--text-muted);font-style:italic;line-height:1.4;padding:6px 10px;background:rgba(255,255,255,0.03);border-radius:6px;border-left:2px solid rgba(245,158,11,0.4)}
.cert-card-cta{margin-top:4px;font-size:11px;color:var(--accent-gold);font-family:'JetBrains Mono',monospace;letter-spacing:0.05em;display:flex;align-items:center;gap:5px}
.cert-card-cta::before{content:'→'}
.chip-cert.linked{cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:5px;position:relative;transition:all 0.2s}
.chip-cert.linked:hover{background:rgba(245,158,11,0.15);border-color:var(--accent-gold);transform:translateY(-1px)}
.chip-cert.linked::after{content:'↗';font-size:10px;opacity:0.7}
.chip-cert .cert-tooltip{position:absolute;bottom:calc(100% + 8px);left:0;background:#1A2030;border:1px solid var(--border-bright);border-radius:10px;padding:14px 16px;width:300px;max-width:90vw;opacity:0;visibility:hidden;transition:all 0.2s;z-index:100;pointer-events:none;box-shadow:0 10px 30px rgba(0,0,0,0.5);text-align:left;white-space:normal;font-family:'Sora',sans-serif}
.chip-cert.linked:hover .cert-tooltip{opacity:1;visibility:visible;bottom:calc(100% + 12px)}
.cert-tooltip::after{content:'';position:absolute;top:100%;left:20px;border:6px solid transparent;border-top-color:#1A2030}
.cert-tooltip-name{font-family:'Bricolage Grotesque',serif;font-size:15px;font-weight:700;color:var(--text-primary);letter-spacing:-0.01em;line-height:1.2;margin-bottom:8px}
.cert-tooltip-full{font-size:12px;color:var(--text-secondary);margin-bottom:10px;line-height:1.4}
.cert-tooltip-meta{display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:11px;font-family:'JetBrains Mono',monospace}
.cert-tooltip-label{color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;font-size:9px;padding-top:1px}
.cert-tooltip-value{color:var(--text-primary)}
.cert-tooltip-value.price{color:var(--accent-gold);font-weight:600}
.cert-tooltip-cta{margin-top:10px;padding-top:10px;border-top:1px solid var(--border);font-size:11px;color:var(--accent-gold);font-family:'JetBrains Mono',monospace;letter-spacing:0.05em}
.cert-tooltip-notes{margin-top:8px;font-size:11px;color:var(--text-muted);font-style:italic;line-height:1.4;padding:6px 8px;background:rgba(255,255,255,0.03);border-radius:6px}
.chip-soft{color:var(--accent-mint);border-color:rgba(16,185,129,0.3)}
.related-roles{display:flex;flex-direction:column;gap:10px;margin-top:14px}
.proj-row{display:flex;flex-direction:column;gap:4px;padding:12px 14px;background:rgba(245,158,11,0.05);border-left:2px solid var(--accent-gold);border-radius:6px;margin-bottom:10px}
.proj-row:last-child{margin-bottom:0}
.proj-label{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--accent-gold);text-transform:uppercase;letter-spacing:0.15em;font-weight:600}
.proj-value{font-size:14px;color:var(--text-primary);line-height:1.5}
.related-role-link{display:flex;align-items:center;gap:12px;padding:12px 14px;background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:10px;cursor:pointer;transition:all 0.2s;text-decoration:none}
.related-role-link:hover{background:rgba(255,255,255,0.06);border-color:var(--border-bright);transform:translateX(4px)}
.related-role-link-id{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-muted);min-width:30px}
.related-role-link-name{font-size:14px;color:var(--text-primary);flex:1;font-weight:500}
.related-role-link-arrow{color:var(--text-muted);font-family:'JetBrains Mono',monospace;font-size:14px}
.back-btn{display:inline-flex;align-items:center;gap:10px;padding:10px 18px;background:var(--bg-card);border:1px solid var(--border);border-radius:100px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-secondary);margin-bottom:32px;transition:all 0.2s}
.back-btn:hover{color:var(--text-primary);transform:translateX(-3px)}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@media (max-width:1100px){.stats-row{grid-template-columns:repeat(2,1fr)}.choice-grid,.roles-grid,.category-grid{grid-template-columns:repeat(2,1fr)}.level-grid{grid-template-columns:repeat(2,1fr)}.detail-body{grid-template-columns:1fr}.detail-stats{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){.app{padding:20px}.stats-row,.choice-grid,.roles-grid,.category-grid,.level-grid{grid-template-columns:1fr}.detail-stats{grid-template-columns:1fr}}
"""

def build_interactive(data, output_path):
    cfg = data['config']
    titulo = cfg.get('titulo', 'Mapa de Carreras')
    subtitulo = cfg.get('subtitulo', '50 ROLES · AMÉRICA 2026')
    salario_max = cfg.get('stat_salario_max', '$470K')
    crecimiento = cfg.get('stat_crecimiento', '+29%')

    total_roles = len(data['roles'])
    total_cats = len(data['categories'])

    roles_json = json.dumps(data['roles'], ensure_ascii=False)
    cats_json = json.dumps(data['categories'], ensure_ascii=False)
    levels_json = json.dumps(data['levels'], ensure_ascii=False)
    trending_json = json.dumps(data['trending'])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo} · LATAM 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=Sora:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="app">
  <div class="top-bar">
    <div class="brand" onclick="goHome()">
      <div class="brand-mark">⌘</div>
      <div class="brand-text"><span>Cyber<em>.map</em></span><span>{subtitulo}</span></div>
    </div>
    <div class="top-right">
      <a class="view-link" href="Mapa_General_Carreras.html">→ Mapa general</a>
      <a class="view-link" href="Mapa_Mental_Carreras.html">→ Vista panorámica</a>
      <a class="view-link" href="Comparar_Roles.html" style="color:var(--accent-cyan);border-color:var(--accent-cyan)">⚖ Comparar roles</a>
      <a class="view-link" href="Catalogo_Certificaciones.html" style="color:var(--accent-gold);border-color:var(--accent-gold)">📜 Catálogo de certs</a>
      <div class="breadcrumb" id="breadcrumb"></div>
    </div>
  </div>
  <div id="root"></div>
</div>
<script>
const ROLES={roles_json};
const CATEGORIES={cats_json};
const LEVELS={levels_json};
const HOT_ROLES={trending_json};
const ICONS={{
  level:'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V7l8-4v18M19 21V11l-6-4"/></svg>',
  category:'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
  trending:'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
  back:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>',
  arrow:'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
}};
let state={{view:'home',selection:null,history:[]}};
const root=document.getElementById('root');
const breadcrumb=document.getElementById('breadcrumb');
function navigate(v,s){{state.history.push({{view:state.view,selection:state.selection}});state.view=v;state.selection=s;render()}}
function goHome(){{state.view='home';state.selection=null;state.history=[];render()}}
function goBack(){{if(state.history.length===0){{goHome();return}}const p=state.history.pop();state.view=p.view;state.selection=p.selection;render()}}
function renderBreadcrumb(){{
  const p=['<a onclick="goHome()">Inicio</a>'];
  if(state.view==='levels')p.push('<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">Por Nivel</span>');
  if(state.view==='categories')p.push('<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">Por Categoría</span>');
  if(state.view==='trending')p.push('<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">Emergentes 2026</span>');
  if(state.view==='level'){{p.push('<span class="breadcrumb-sep">›</span><a onclick="navigate(\\'levels\\')">Por Nivel</a>');p.push(`<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">${{LEVELS[state.selection].label}}</span>`)}}
  if(state.view==='category'){{p.push('<span class="breadcrumb-sep">›</span><a onclick="navigate(\\'categories\\')">Por Categoría</a>');p.push(`<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">${{CATEGORIES[state.selection].label}}</span>`)}}
  if(state.view==='role'){{const r=ROLES.find(x=>x.id===state.selection);p.push(`<span class="breadcrumb-sep">›</span><span class="breadcrumb-current">${{r.roleEN}}</span>`)}}
  breadcrumb.innerHTML=p.join('');
}}
function dC(d){{const dd=d.toUpperCase();if(dd.includes('MUY ALTA')||dd.includes('EXPLOSIVA'))return'demand-very-high';if(dd.includes('ALTA'))return'demand-high';return'demand-medium'}}
function hexToRgba(h,a){{const r=parseInt(h.slice(1,3),16),g=parseInt(h.slice(3,5),16),b=parseInt(h.slice(5,7),16);return`rgba(${{r}},${{g}},${{b}},${{a}})`}}
function roleCard(r){{
  const c=CATEGORIES[r.cat];
  return `<div class="role-card" onclick="navigate('role',${{r.id}})" style="--role-color:${{c.color}};--role-glow:${{hexToRgba(c.color,0.1)}};">
    <div class="role-card-top"><span class="role-cat-badge">${{c.label.split('/')[0].trim()}}</span><span class="role-id">#${{String(r.id).padStart(2,'0')}}</span></div>
    <div><div class="role-name">${{r.roleEN}}</div><div class="role-name-es">${{r.roleES}}</div></div>
    <div class="role-salary">${{r.salaryMonth}}<small style="color:var(--text-muted);margin-left:6px;font-weight:400">/ mes</small></div>
    <div class="role-meta-row"><span><span class="demand-dot ${{dC(r.demand)}}"></span>${{r.demand.split('(')[0].trim()}}</span><span>${{r.years}}</span></div>
  </div>`;
}}
function getCommon(rs,k,lim){{
  const c={{}};rs.forEach(r=>(r[k]||[]).forEach(s=>{{const cl=s.replace(/⭐/g,'').trim();c[cl]=(c[cl]||0)+1}}));
  return Object.entries(c).filter(([_,n])=>n>=2).sort((a,b)=>b[1]-a[1]).slice(0,lim).map(([s])=>s);
}}
function renderHome(){{
  return `<div class="home">
    <div class="hero">
      <div class="hero-eyebrow">GUÍA DE CARRERAS · ACTUALIZADA 2026</div>
      <h1 class="hero-title">Existen más de <em>${{ROLES.length}} roles</em><br>en ciberseguridad.</h1>
      <p class="hero-sub">No todo es ser hacker. Esta es la guía interactiva más completa de carreras en ciberseguridad para Latinoamérica — desde el primer rol Junior hasta el CISO. Salarios reales, skills, certificaciones y cómo empezar.</p>
    </div>
    <div class="stats-row">
      <div class="stat" data-c="gold"><div class="stat-label">Roles documentados</div><div class="stat-value">{total_roles}</div></div>
      <div class="stat" data-c="mint"><div class="stat-label">Categorías</div><div class="stat-value">{total_cats}</div></div>
      <div class="stat" data-c="cyan"><div class="stat-label">Salario máximo</div><div class="stat-value">{salario_max}<small>/año</small></div></div>
      <div class="stat" data-c="magenta"><div class="stat-label">Crecimiento BLS 2024-34</div><div class="stat-value">{crecimiento}</div></div>
    </div>
    <div class="choice-section">
      <div class="section-header"><div class="section-title">¿Por dónde empiezas?</div><div class="section-num">/ 03 caminos</div></div>
      <div class="choice-grid">
        <div class="choice-card" data-c="gold" onclick="navigate('levels')">
          <div><div class="choice-num">/ 01</div><div class="choice-icon" style="margin-top:16px">${{ICONS.level}}</div></div>
          <div><div class="choice-title">Por nivel<br>de experiencia</div><p class="choice-desc">¿Apenas empiezas? ¿Ya eres senior? Encuentra los roles para tu nivel — desde Junior hasta C-Level.</p></div>
          <div class="choice-cta">Explorar ${{Object.keys(LEVELS).length}} niveles ${{ICONS.arrow}}</div>
        </div>
        <div class="choice-card" data-c="mint" onclick="navigate('categories')">
          <div><div class="choice-num">/ 02</div><div class="choice-icon" style="margin-top:16px">${{ICONS.category}}</div></div>
          <div><div class="choice-title">Por área<br>o categoría</div><p class="choice-desc">Ofensivo, defensivo, GRC, cloud, IA... encuentra qué área te apasiona.</p></div>
          <div class="choice-cta">Explorar ${{Object.keys(CATEGORIES).length}} áreas ${{ICONS.arrow}}</div>
        </div>
        <div class="choice-card" data-c="magenta" onclick="navigate('trending')">
          <div><div class="choice-num">/ 03</div><div class="choice-icon" style="margin-top:16px">${{ICONS.trending}}</div></div>
          <div><div class="choice-title">Emergentes<br>y mejor pagados</div><p class="choice-desc">Los roles más calientes de 2025-2026: IA Security, Kubernetes, Zero Trust, DevSecOps.</p></div>
          <div class="choice-cta">Ver top ${{HOT_ROLES.length}} ${{ICONS.arrow}}</div>
        </div>
      </div>
    </div>
  </div>`;
}}
function renderLevels(){{
  const cm={{junior:'#10B981',mid:'#06B6D4',senior:'#F59E0B',manager:'#EC4899',executive:'#C084FC'}};
  const cards=Object.entries(LEVELS).map(([k,l])=>{{
    const n=ROLES.filter(r=>r.level===k).length;
    return `<div class="tile" style="--tile-color:${{cm[k]||'#F59E0B'}}" onclick="navigate('level','${{k}}')">
      <div><div class="tile-count">Nivel · ${{n}} roles</div><div class="tile-label" style="margin-top:10px">${{l.label}}</div><div class="tile-meta" style="margin-top:6px">${{l.yearsRange}}</div></div>
      <div class="tile-desc">${{l.shortDesc}}</div></div>`;
  }}).join('');
  return `<div class="list-view">
    <button class="back-btn" onclick="goHome()">${{ICONS.back}} Volver al inicio</button>
    <div class="list-header"><div class="list-eyebrow">RUTA 01 / NIVEL DE EXPERIENCIA</div><h2 class="list-title">¿En qué nivel estás?</h2><p class="list-sub">Cada nivel tiene sus propios roles, salarios y skills clave. Toca tu nivel para ver los roles disponibles.</p></div>
    <div class="level-grid">${{cards}}</div></div>`;
}}
function renderCategories(){{
  const cards=Object.entries(CATEGORIES).map(([k,c])=>{{
    const n=ROLES.filter(r=>r.cat===k).length;
    return `<div class="tile" style="--tile-color:${{c.color}}" onclick="navigate('category','${{k}}')">
      <div><div class="tile-count">Área · ${{n}} roles</div><div class="tile-label" style="margin-top:10px">${{c.label}}</div></div></div>`;
  }}).join('');
  return `<div class="list-view">
    <button class="back-btn" onclick="goHome()">${{ICONS.back}} Volver al inicio</button>
    <div class="list-header"><div class="list-eyebrow">RUTA 02 / ÁREAS Y CATEGORÍAS</div><h2 class="list-title">${{Object.keys(CATEGORIES).length}} áreas distintas.</h2><p class="list-sub">Ciberseguridad no es una sola cosa. Defensiva, ofensiva, arquitectura, GRC, legal, ventas, gerencia... cada área es un mundo.</p></div>
    <div class="category-grid">${{cards}}</div></div>`;
}}
function renderTrending(){{
  const hot=HOT_ROLES.map(id=>ROLES.find(r=>r.id===id)).filter(r=>r);
  return `<div class="list-view">
    <button class="back-btn" onclick="goHome()">${{ICONS.back}} Volver al inicio</button>
    <div class="list-header"><div class="list-eyebrow">RUTA 03 / EMERGENTES 2025-2026</div><h2 class="list-title">Los ${{hot.length}} más calientes.</h2><p class="list-sub">Estos son los roles con mayor crecimiento, mejor pago y más demanda en este momento. AI Security lidera con +24x demanda desde 2023.</p></div>
    <div class="roles-grid">${{hot.map(roleCard).join('')}}</div></div>`;
}}
function renderLevel(){{
  const l=LEVELS[state.selection];
  const lr=ROLES.filter(r=>r.level===state.selection);
  const cc=getCommon(lr,'certs',8);
  const sc=getCommon(lr,'softSkills',8);
  return `<div class="list-view">
    <button class="back-btn" onclick="navigate('levels')">${{ICONS.back}} Cambiar de nivel</button>
    <div class="list-header"><div class="list-eyebrow">NIVEL · ${{l.yearsRange.toUpperCase()}}</div><h2 class="list-title">${{l.label}}</h2><p class="list-sub">${{lr.length}} roles disponibles en este nivel. ${{l.shortDesc}}.</p></div>
    <div class="common-skills"><h3>Lo que tienen en común estos roles<small>habilidades transversales del nivel</small></h3>
      <div class="common-skills-grid">
        <div class="common-skills-col"><h4>Certificaciones más recurrentes</h4><div class="skill-chips">${{cc.map(s=>`<span class="skill-chip" style="color:var(--accent-gold);border-color:rgba(245,158,11,0.3)">${{s}}</span>`).join('')}}</div></div>
        <div class="common-skills-col"><h4>Soft skills clave</h4><div class="skill-chips">${{sc.map(s=>`<span class="skill-chip" style="color:var(--accent-mint);border-color:rgba(16,185,129,0.3)">${{s}}</span>`).join('')}}</div></div>
      </div></div>
    <div class="roles-grid">${{lr.map(roleCard).join('')}}</div></div>`;
}}
function renderCategory(){{
  const c=CATEGORIES[state.selection];
  const cr=ROLES.filter(r=>r.cat===state.selection);
  const hc=getCommon(cr,'hardSkills',10);
  const tc=getCommon(cr,'tools',10);
  return `<div class="list-view">
    <button class="back-btn" onclick="navigate('categories')">${{ICONS.back}} Cambiar de área</button>
    <div class="list-header"><div class="list-eyebrow">ÁREA · CATEGORÍA</div><h2 class="list-title" style="color:${{c.color}}">${{c.label}}</h2><p class="list-sub">${{cr.length}} roles en esta área. Cada uno con su nivel y especialización.</p></div>
    <div class="common-skills"><h3>Skills compartidos en esta área<small>común a varios roles de la categoría</small></h3>
      <div class="common-skills-grid">
        <div class="common-skills-col"><h4>Habilidades técnicas</h4><div class="skill-chips">${{hc.map(s=>`<span class="skill-chip">${{s}}</span>`).join('')}}</div></div>
        <div class="common-skills-col"><h4>Herramientas comunes</h4><div class="skill-chips">${{tc.map(s=>`<span class="skill-chip" style="color:var(--accent-cyan);border-color:rgba(6,182,212,0.3)">${{s}}</span>`).join('')}}</div></div>
      </div></div>
    <div class="roles-grid">${{cr.map(roleCard).join('')}}</div></div>`;
}}
function renderRole(){{
  const r=ROLES.find(x=>x.id===state.selection);
  const c=CATEGORIES[r.cat],l=LEVELS[r.level];
  const dc=c.color,dg=hexToRgba(dc,0.15);
  const rel=(r.related||[]).map(id=>{{
    const x=ROLES.find(y=>y.id===id);if(!x)return'';
    return `<a class="related-role-link" onclick="navigate('role',${{x.id}})"><span class="related-role-link-id">#${{String(x.id).padStart(2,'0')}}</span><span class="related-role-link-name">${{x.roleEN}}</span><span class="related-role-link-arrow">→</span></a>`;
  }}).join('');
  return `<div class="detail" style="--detail-color:${{dc}};--detail-glow:${{dg}};">
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:32px;align-items:center">
      <button class="back-btn" onclick="goBack()" style="margin-bottom:0">${{ICONS.back}} Volver</button>
      <a class="back-btn" href="Comparar_Roles.html#${{r.id}}" style="margin-bottom:0;color:#06B6D4;border-color:rgba(6,182,212,0.3);text-decoration:none">⚖ Comparar con otro rol</a>
    </div>
    <div class="detail-hero">
      <div class="detail-hero-top">
        <span class="detail-badge detail-cat-badge">${{c.label}}</span>
        <span class="detail-badge detail-level-badge">${{l.label}} · ${{r.years}}</span>
        <span class="detail-id">ROL #${{String(r.id).padStart(2,'0')}} / ${{ROLES.length}}</span>
      </div>
      <h1 class="detail-title">${{r.roleEN}}</h1>
      <p class="detail-subtitle">${{r.roleES}}</p>
      <p class="detail-synonyms">${{r.synonyms||''}}</p>
      <div class="detail-stats">
        <div class="detail-stat"><div class="detail-stat-label">Salario mensual</div><div class="detail-stat-value money">${{r.salaryMonth}}</div></div>
        <div class="detail-stat"><div class="detail-stat-label">Salario anual</div><div class="detail-stat-value money">${{r.salaryYear}}</div></div>
        <div class="detail-stat"><div class="detail-stat-label">Demanda</div><div class="detail-stat-value">${{r.demand.split('(')[0].trim()}}</div></div>
        <div class="detail-stat"><div class="detail-stat-label">Trabajo remoto</div><div class="detail-stat-value">${{r.remote}}</div></div>
      </div>
    </div>
    <div class="detail-body">
      <div>
        <div class="detail-section"><h3>¿Qué hace en su día a día?</h3><p class="detail-text">${{r.description||''}}</p></div>
        <div class="detail-section" style="margin-top:20px"><h3>Habilidades y herramientas</h3>
          <div class="skill-group-title">Habilidades técnicas (hard skills)</div><div class="chips-row">${{(r.hardSkills||[]).map(s=>`<span class="chip">${{s}}</span>`).join('')}}</div>
          <div class="skill-group-title">Herramientas principales</div><div class="chips-row">${{(r.tools||[]).map(s=>`<span class="chip chip-tool">${{s}}</span>`).join('')}}</div>
          <div class="skill-group-title">Habilidades blandas (soft skills)</div><div class="chips-row">${{(r.softSkills||[]).map(s=>`<span class="chip chip-soft">${{s}}</span>`).join('')}}</div>
          <div class="skill-group-title">Certificaciones recomendadas</div><div class="cert-cards-grid">${{(r.certsEnriched||r.certs||[]).map(c=>{{
            if(typeof c==='string'){{ return `<div class="cert-card cert-card-basic"><div class="cert-card-header"><span class="cert-card-acronym">${{c}}</span></div></div>`; }}
            const info=c.info;
            if(!info||!info.officialUrl){{ return `<div class="cert-card cert-card-basic"><div class="cert-card-header"><span class="cert-card-acronym">${{c.displayName}}</span></div></div>`; }}
            const priceStr=info.priceUSD===0?'Gratis':(info.priceUSD?`$${{info.priceUSD}} USD`:'Precio no público');
            const notesHtml=info.notes?`<div class="cert-card-notes">⚠️ ${{info.notes}}</div>`:'';
            const fullName=info.fullName?`<div class="cert-card-fullname">${{info.fullName}}</div>`:'';
            const vendor=info.vendor||'—';
            return `<a class="cert-card" href="${{info.officialUrl}}" target="_blank" rel="noopener" title="Click para ir al sitio oficial de ${{vendor}}">
              <div class="cert-card-header">
                <span class="cert-card-acronym">${{info.shortName||c.displayName}}</span>
                <span class="cert-card-arrow">↗</span>
              </div>
              ${{fullName}}
              <div class="cert-card-meta">
                <span class="cert-card-label">Vendor</span><span class="cert-card-value">${{vendor}}</span>
                <span class="cert-card-label">Precio</span><span class="cert-card-value price">${{priceStr}}</span>
                <span class="cert-card-label">Prep</span><span class="cert-card-value">${{info.prepTime||'—'}}</span>
                <span class="cert-card-label">Nivel</span><span class="cert-card-value">${{info.difficulty||'—'}}</span>
                <span class="cert-card-label">Vigencia</span><span class="cert-card-value">${{info.validity||'—'}}</span>
              </div>
              ${{notesHtml}}
              <div class="cert-card-cta">Ir al sitio oficial</div>
            </a>`;
          }}).join('')}}</div>
        </div>
      </div>
      <div>
        <div class="detail-section"><h3>Cómo empezar</h3><p class="detail-text">${{r.entry||''}}</p></div>
        <div class="detail-section" style="margin-top:20px"><h3>Ruta de crecimiento</h3><p class="detail-text">${{r.growth||''}}</p></div>
        <div class="detail-section" style="margin-top:20px"><h3>Mercados que más contratan</h3><p class="detail-text">${{r.markets||''}}</p></div>
        ${{(r.projection||r.trend2026||r.salaryJump||r.difficulty)?`<div class="detail-section" style="margin-top:20px"><h3>Proyecciones 2026-2028</h3>
          ${{r.projection?`<div class="proj-row"><div class="proj-label">📈 Crecimiento esperado</div><div class="proj-value">${{r.projection}}</div></div>`:''}}
          ${{r.trend2026?`<div class="proj-row"><div class="proj-label">🔥 Tendencia</div><div class="proj-value">${{r.trend2026}}</div></div>`:''}}
          ${{r.salaryJump?`<div class="proj-row"><div class="proj-label">💰 Salto salarial Junior→Senior</div><div class="proj-value">${{r.salaryJump}}</div></div>`:''}}
          ${{r.difficulty?`<div class="proj-row"><div class="proj-label">⚡ Dificultad de entrada</div><div class="proj-value">${{r.difficulty}}</div></div>`:''}}
        </div>`:''}}
        ${{rel?`<div class="detail-section" style="margin-top:20px"><h3>Roles relacionados</h3><div class="related-roles">${{rel}}</div></div>`:''}}
      </div>
    </div>
  </div>`;
}}
function render(){{
  renderBreadcrumb();
  let h='';
  switch(state.view){{
    case'home':h=renderHome();break;
    case'levels':h=renderLevels();break;
    case'categories':h=renderCategories();break;
    case'trending':h=renderTrending();break;
    case'level':h=renderLevel();break;
    case'category':h=renderCategory();break;
    case'role':h=renderRole();break;
  }}
  root.innerHTML=h;
  window.scrollTo({{top:0,behavior:'smooth'}});
}}
// Deep linking: si la URL tiene #role-XX, abrir ese rol directamente
const hashMatch = window.location.hash.match(/role-(\\d+)/);
if (hashMatch) {{
  const targetId = parseInt(hashMatch[1]);
  if (ROLES.find(r => r.id === targetId)) {{
    state.view = 'role';
    state.selection = targetId;
  }}
}}
render();
</script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return len(html)
