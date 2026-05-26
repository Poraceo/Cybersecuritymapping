"""
Parser del archivo roles.md
Devuelve un dict con: config, categorias, niveles, trending, roles
"""
import re
import sys
import os

def parse_md(md_path):
    if not os.path.exists(md_path):
        print(f"ERROR: No encuentro el archivo {md_path}")
        print("Asegurate de que roles.md este en la misma carpeta que actualizar.py")
        sys.exit(1)

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remover comentarios HTML <!-- ... -->
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    config = {}
    categories = {}
    levels = {}
    trending = []
    roles = []

    # Config global
    for key in ['titulo', 'subtitulo', 'stat_salario_max', 'stat_crecimiento']:
        m = re.search(rf'@{key}:\s*(.+)', content)
        if m:
            config[key] = m.group(1).strip()

    # Categorias: @categoria CLAVE: Nombre | #COLOR
    for m in re.finditer(r'@categoria\s+(\w+):\s*([^|]+)\|\s*(#[0-9A-Fa-f]{6})', content):
        key = m.group(1).strip()
        categories[key] = {
            'label': m.group(2).strip(),
            'color': m.group(3).strip()
        }

    # Niveles: @nivel CLAVE: Nombre | Rango | Descripcion
    for m in re.finditer(r'@nivel\s+(\w+):\s*([^|]+)\|([^|]+)\|(.+)', content):
        key = m.group(1).strip()
        levels[key] = {
            'label': m.group(2).strip(),
            'yearsRange': m.group(3).strip(),
            'shortDesc': m.group(4).strip()
        }

    # Trending
    m = re.search(r'@trending:\s*([\d,\s]+)', content)
    if m:
        trending = [int(x.strip()) for x in m.group(1).split(',') if x.strip().isdigit()]

    # Roles: separar por "## Rol #XX:"
    role_blocks = re.split(r'^## Rol #(\d+):\s*(.+?)$', content, flags=re.MULTILINE)
    # role_blocks[0] = preludio. Luego se alternan (id, nombre_en, body)
    for i in range(1, len(role_blocks), 3):
        try:
            role_id = int(role_blocks[i])
            role_en = role_blocks[i+1].strip()
            body = role_blocks[i+2]
        except (IndexError, ValueError):
            continue

        role = {'id': role_id, 'roleEN': role_en}

        # Campos simples con @
        field_map = {
            'roleES': r'@rolES:\s*(.+)',
            'cat': r'@cat:\s*(\w+)',
            'level': r'@nivel:\s*(\w+)',
            'years': r'@anos:\s*(.+)',
            'synonyms': r'@sinonimos:\s*(.+)',
            'salaryMonth': r'@salario_mes:\s*(.+)',
            'salaryYear': r'@salario_ano:\s*(.+)',
            'demand': r'@demanda:\s*(.+)',
            'remote': r'@remoto:\s*(.+)',
            # Campos opcionales de proyección (no obligatorios)
            'projection': r'@proyeccion:\s*(.+)',
            'trend2026': r'@tendencia:\s*(.+)',
            'salaryJump': r'@salto_salarial:\s*(.+)',
            'difficulty': r'@dificultad:\s*(.+)',
        }
        for field, regex in field_map.items():
            m = re.search(regex, body)
            if m:
                role[field] = m.group(1).strip()

        # Relacionados (lista de ints)
        m = re.search(r'@relacionados:\s*([\d,\s]+)', body)
        role['related'] = [int(x.strip()) for x in m.group(1).split(',') if x.strip().isdigit()] if m else []

        # Secciones ### con listas (Hard Skills, Tools, Soft Skills, Certs)
        for section, key in [('Hard Skills', 'hardSkills'),
                             ('Tools', 'tools'),
                             ('Soft Skills', 'softSkills'),
                             ('Certs', 'certs')]:
            pattern = rf'### {re.escape(section)}\s*\n(.+?)(?=\n###|\n##|\Z)'
            m = re.search(pattern, body, re.DOTALL)
            if m:
                items = [line.lstrip('- ').strip() for line in m.group(1).split('\n') if line.strip().startswith('-')]
                role[key] = items
            else:
                role[key] = []

        # Secciones ### con texto plano
        for section, key in [('Descripción', 'description'),
                             ('Descripcion', 'description'),
                             ('Cómo empezar', 'entry'),
                             ('Como empezar', 'entry'),
                             ('Crecimiento', 'growth'),
                             ('Mercados', 'markets')]:
            pattern = rf'### {re.escape(section)}\s*\n(.+?)(?=\n###|\n##|\Z)'
            m = re.search(pattern, body, re.DOTALL)
            if m and key not in role:
                role[key] = ' '.join(line.strip() for line in m.group(1).split('\n') if line.strip())

        # Defaults
        for k in ['description', 'entry', 'growth', 'markets', 'synonyms']:
            if k not in role:
                role[k] = ''
        roles.append(role)

    roles.sort(key=lambda r: r['id'])

    return {
        'config': config,
        'categories': categories,
        'levels': levels,
        'trending': trending,
        'roles': roles
    }


def hex_to_rgba(hex_str, alpha):
    h = hex_str.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{alpha})'
