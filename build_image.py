#!/usr/bin/env python3
"""
Mapa General — UNA SOLA IMAGEN con todos los roles.
Layout limpio, jerarquía visual clara, incluye nombres en español.
"""

import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from parser import parse_md


LEVEL_ORDER = ['junior', 'mid', 'senior', 'manager', 'executive']
LEVEL_COLORS = {
    'junior':    '#10B981',
    'mid':       '#06B6D4',
    'senior':    '#F59E0B',
    'manager':   '#EC4899',
    'executive': '#C084FC',
}

BG = '#0A0E1A'
BG_BAND_ALT = '#0E1322'
CARD_BG = '#1A2236'
BORDER = '#2A3149'
TEXT_PRIMARY = '#F8FAFC'
TEXT_SECONDARY = '#CBD5E1'
TEXT_MUTED = '#94A3B8'
TEXT_DIM = '#64748B'
GOLD = '#F59E0B'


def shorten(name, max_len=24):
    if len(name) <= max_len:
        return name
    parts = name.split('/')
    if len(parts) > 1:
        first = parts[0].strip()
        if len(first) <= max_len:
            return first
    return name[:max_len - 1] + '…'


def salary_max(s):
    if not s:
        return ''
    if '-' in s:
        return s.split('-')[-1].strip()
    return s


def build_map(data, out_path):
    cats = data['categories']
    levels = data['levels']
    roles = data['roles']
    cat_keys = list(cats.keys())
    n_cats = len(cat_keys)

    grid = {}
    for lk in LEVEL_ORDER:
        for ck in cat_keys:
            grid[(lk, ck)] = [r for r in roles
                              if r.get('level') == lk and r.get('cat') == ck]

    col_w = 2.6
    card_h = 0.7
    card_gap = 0.1
    row_pad = 0.35

    label_w = 2.6
    title_h = 3.2
    cat_header_h = 1.3
    footer_h = 1.6

    row_heights = []
    for lk in LEVEL_ORDER:
        max_cards = max(len(grid[(lk, ck)]) for ck in cat_keys)
        max_cards = max(max_cards, 1)
        h = max_cards * (card_h + card_gap) + row_pad * 2
        row_heights.append(h)

    body_h = sum(row_heights)
    total_h = title_h + cat_header_h + body_h + footer_h
    total_w = label_w + n_cats * col_w + 0.8

    fig = plt.figure(figsize=(total_w, total_h), facecolor=BG, dpi=130)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, total_w)
    ax.set_ylim(0, total_h)
    ax.set_facecolor(BG)
    ax.axis('off')

    # === HEADER ===
    title_top = total_h - 0.3

    ax.add_patch(Rectangle((0.5, title_top - 0.15), 0.6, 0.04,
                           facecolor=GOLD, edgecolor='none'))
    ax.text(1.2, title_top - 0.13,
            'GUÍA DE CARRERAS EN CIBERSEGURIDAD · AMÉRICA · 2026',
            color=GOLD, fontsize=11, weight='bold',
            family='monospace', va='center', ha='left')

    ax.text(0.5, title_top - 0.85,
            f'{len(roles)} roles',
            color=TEXT_PRIMARY, fontsize=58, weight='bold',
            va='top', ha='left')
    ax.text(0.5, title_top - 1.85,
            'en ciberseguridad, mapeados.',
            color=TEXT_MUTED, fontsize=24,
            va='top', ha='left', style='italic')

    ax.text(0.5, title_top - 2.6,
            '↓ Eje vertical: progresión de carrera (Junior → C-Level)     '
            '→ Eje horizontal: categorías / áreas de especialización',
            color=TEXT_SECONDARY, fontsize=11,
            va='top', ha='left', family='monospace')

    ax.text(total_w - 0.5, title_top - 0.13, 'CYBER.MAP',
            color=TEXT_PRIMARY, fontsize=14, weight='bold',
            family='monospace', va='center', ha='right')
    ax.text(total_w - 0.5, title_top - 0.55,
            f'{len(cats)} categorías · {len(LEVEL_ORDER)} niveles',
            color=TEXT_MUTED, fontsize=9, family='monospace',
            va='center', ha='right')

    sep1_y = total_h - title_h
    ax.plot([0.5, total_w - 0.5], [sep1_y, sep1_y],
            color=BORDER, linewidth=0.7)

    # === HEADERS DE CATEGORÍAS ===
    cat_y_center = sep1_y - cat_header_h * 0.55

    for i, ck in enumerate(cat_keys):
        cat = cats[ck]
        x_center = label_w + i * col_w + col_w / 2

        ax.add_patch(Rectangle((label_w + i * col_w + 0.15, sep1_y - 0.18),
                               col_w - 0.3, 0.06,
                               facecolor=cat['color'], edgecolor='none'))

        label = cat['label']
        if '/' in label:
            parts = [p.strip() for p in label.split('/')]
            line1, line2 = parts[0], parts[1]
        else:
            line1, line2 = label, ''
        ax.text(x_center, cat_y_center + 0.15, line1,
                color=TEXT_PRIMARY, fontsize=9.5, weight='bold',
                va='center', ha='center')
        if line2:
            ax.text(x_center, cat_y_center - 0.15, line2,
                    color=TEXT_SECONDARY, fontsize=8.5,
                    va='center', ha='center')

        count = sum(1 for r in roles if r.get('cat') == ck)
        ax.text(x_center, cat_y_center - 0.55,
                f'· {count} {"rol" if count == 1 else "roles"} ·',
                color=cat['color'], fontsize=8, weight='bold',
                family='monospace', va='center', ha='center')

    sep2_y = sep1_y - cat_header_h
    ax.plot([0.5, total_w - 0.5], [sep2_y, sep2_y],
            color=BORDER, linewidth=0.7)

    # === BANDAS ===
    current_y = sep2_y

    for row_idx, lk in enumerate(LEVEL_ORDER):
        lvl = levels[lk]
        bcolor = LEVEL_COLORS[lk]
        rh = row_heights[row_idx]
        band_top = current_y
        band_bot = current_y - rh

        if row_idx % 2 == 0:
            ax.add_patch(Rectangle((0.3, band_bot), total_w - 0.6, rh,
                                   facecolor=BG_BAND_ALT,
                                   edgecolor='none', zorder=0))

        lx = 0.55
        ax.add_patch(Rectangle((lx, band_bot + 0.3), 0.08, rh - 0.6,
                               facecolor=bcolor, edgecolor='none', zorder=2))

        text_x = lx + 0.25

        # Header del nivel: número + nombre + años + conteo (todo junto arriba)
        ax.text(text_x, band_top - 0.4,
                f'NIVEL {row_idx + 1:02d}',
                color=bcolor, fontsize=9, weight='bold',
                family='monospace', va='top', ha='left')

        ax.text(text_x, band_top - 0.85,
                lvl['label'],
                color=TEXT_PRIMARY, fontsize=18, weight='bold',
                va='top', ha='left')

        # Años + conteo en la misma línea
        n_in = sum(1 for r in roles if r.get('level') == lk)
        ax.text(text_x, band_top - 1.35,
                f'{lvl["yearsRange"]}',
                color=TEXT_SECONDARY, fontsize=10, family='monospace',
                va='top', ha='left')

        # Badge del conteo
        ax.text(text_x, band_top - 1.7,
                f'● {n_in} roles',
                color=bcolor, fontsize=10, weight='bold',
                family='monospace', va='top', ha='left')

        # Descripción solo si hay espacio (banda alta)
        if rh > 2.5:
            desc = lvl['shortDesc']
            if len(desc) > 24:
                words = desc.split()
                lines = []
                current = []
                for w in words:
                    test = ' '.join(current + [w])
                    if len(test) > 24 and current:
                        lines.append(' '.join(current))
                        current = [w]
                    else:
                        current.append(w)
                if current:
                    lines.append(' '.join(current))
                desc = '\n'.join(lines)

            ax.text(text_x, band_top - 2.15,
                    desc,
                    color=TEXT_MUTED, fontsize=8.5,
                    va='top', ha='left', linespacing=1.4, style='italic')

        for col_idx, ck in enumerate(cat_keys):
            cell_roles = grid[(lk, ck)]
            cat = cats[ck]
            x_left = label_w + col_idx * col_w + 0.15
            x_right = label_w + (col_idx + 1) * col_w - 0.15
            card_w = x_right - x_left

            card_y = band_top - row_pad - card_h
            for role in cell_roles:
                box = FancyBboxPatch(
                    (x_left, card_y), card_w, card_h,
                    boxstyle="round,pad=0.01,rounding_size=0.08",
                    facecolor=CARD_BG, edgecolor=BORDER, linewidth=0.7,
                    zorder=2
                )
                ax.add_patch(box)
                ax.add_patch(Rectangle((x_left, card_y + 0.06),
                                       0.06, card_h - 0.12,
                                       facecolor=cat['color'], edgecolor='none',
                                       zorder=3))

                ax.text(x_right - 0.08, card_y + card_h - 0.1,
                        f'#{role["id"]:02d}',
                        color=TEXT_DIM, fontsize=7, family='monospace',
                        weight='bold', va='top', ha='right', zorder=4)

                name = shorten(role['roleEN'], 23)
                ax.text(x_left + 0.16, card_y + card_h - 0.1,
                        name,
                        color=TEXT_PRIMARY, fontsize=8.5, weight='bold',
                        va='top', ha='left', zorder=4)

                name_es = shorten(role.get('roleES', ''), 26)
                ax.text(x_left + 0.16, card_y + card_h - 0.32,
                        name_es,
                        color=TEXT_MUTED, fontsize=6.8, style='italic',
                        va='top', ha='left', zorder=4)

                sal = salary_max(role.get('salaryMonth', ''))
                ax.text(x_left + 0.16, card_y + 0.1,
                        f'hasta {sal}/mes',
                        color=GOLD, fontsize=7, family='monospace',
                        weight='bold', va='bottom', ha='left', zorder=4)

                card_y -= (card_h + card_gap)

        current_y = band_bot

    # === FOOTER ===
    fy = current_y - 0.3
    ax.plot([0.5, total_w - 0.5], [fy, fy], color=BORDER, linewidth=0.7)

    fbx = 0.5
    ax.text(fbx, fy - 0.35, 'SOBRE LOS SALARIOS',
            color=GOLD, fontsize=9, weight='bold',
            family='monospace', va='top', ha='left')
    ax.text(fbx, fy - 0.65,
            'El monto mostrado es el TOPE del rango mensual\n'
            '(Senior trabajando para mercado USA).\n'
            'El piso del rango — Junior en LATAM — está\n'
            'en la versión interactiva y en la hoja de Excel.',
            color=TEXT_SECONDARY, fontsize=8.5,
            va='top', ha='left', linespacing=1.5)

    fbx2 = total_w * 0.4
    ax.text(fbx2, fy - 0.35, 'CÓMO LEER ESTE MAPA',
            color=GOLD, fontsize=9, weight='bold',
            family='monospace', va='top', ha='left')
    ax.text(fbx2, fy - 0.65,
            'Cada tarjeta es un rol. El borde IZQUIERDO de color\n'
            'indica su categoría (color en el header de arriba).\n'
            'La fila indica el nivel de seniority requerido.\n'
            'Hay caminos cruzados — no todo es lineal.',
            color=TEXT_SECONDARY, fontsize=8.5,
            va='top', ha='left', linespacing=1.5)

    fbx3 = total_w - 6.0
    ax.text(fbx3, fy - 0.35, 'PROGRESIÓN DE CARRERA',
            color=GOLD, fontsize=9, weight='bold',
            family='monospace', va='top', ha='left')
    tl_y = fy - 0.95
    tl_start = fbx3
    tl_end = total_w - 0.5
    ax.plot([tl_start + 0.1, tl_end - 0.1], [tl_y, tl_y],
            color=BORDER, linewidth=2, zorder=2)
    for i, lk in enumerate(LEVEL_ORDER):
        frac = i / (len(LEVEL_ORDER) - 1)
        px = tl_start + 0.1 + (tl_end - tl_start - 0.2) * frac
        ax.add_patch(Circle((px, tl_y), 0.12,
                            facecolor=LEVEL_COLORS[lk], edgecolor=BG,
                            linewidth=1.5, zorder=4))
        short = levels[lk]['label'].split(' ')[0].split('/')[0].strip()
        ax.text(px, tl_y - 0.32, short,
                color=TEXT_PRIMARY, fontsize=8.5, family='monospace',
                weight='bold', va='top', ha='center')

    plt.tight_layout()
    plt.savefig(out_path, facecolor=BG, dpi=140, bbox_inches='tight',
                pad_inches=0.4)
    plt.close()

    return os.path.getsize(out_path)


if __name__ == '__main__':
    md_path = os.path.join(SCRIPT_DIR, 'roles.md')
    out_path = os.path.join(SCRIPT_DIR, 'Mapa_General_Carreras.png')

    print("📖  Leyendo roles.md...")
    data = parse_md(md_path)
    print(f"   ✓ {len(data['roles'])} roles, {len(data['categories'])} categorías")

    print("🎨  Generando mapa visual general...")
    size = build_map(data, out_path)
    print(f"   ✓ {os.path.basename(out_path)} ({size / 1024:.1f} KB)")
    print(f"\n✅ Imagen lista: {out_path}")
