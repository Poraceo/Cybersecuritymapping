#!/usr/bin/env python3
"""
ACTUALIZAR.PY
=============
Este es el script que corres en la terminal para regenerar los HTMLs.

USO:
    python actualizar.py

Lee roles.md (en esta misma carpeta) y regenera:
  - Mapa_Carreras_Ciberseguridad.html  (versión interactiva)
  - Mapa_Mental_Carreras.html          (vista panorámica)

Solo necesita Python 3.6 o superior. NO requiere instalar nada extra.
"""

import os
import sys

# Asegurarse de que el script encuentre los módulos locales
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

try:
    from parser import parse_md
    from build_interactive import build_interactive
    from build_mindmap import build_mindmap
    from build_general import build_general
    from build_certcatalog import build_catalog
    from build_image import build_map
except ImportError as e:
    print("=" * 60)
    print("❌ ERROR: No se pueden cargar los módulos del sistema.")
    print("=" * 60)
    print(f"   Detalle: {e}")
    print("")
    print("   Asegúrate de tener TODOS estos archivos en la misma carpeta:")
    print("     - actualizar.py")
    print("     - parser.py")
    print("     - build_interactive.py")
    print("     - build_mindmap.py")
    print("     - build_general.py")
    print("     - build_image.py")
    print("     - roles.md")
    print("")
    print("   Si el error menciona 'matplotlib', instálalo con:")
    print("     pip install matplotlib")
    sys.exit(1)


def main():
    print("")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   CYBER.MAP — ACTUALIZADOR DE HTMLs                      ║")
    print("║   Regenerando archivos desde roles.md...                 ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("")

    md_path = os.path.join(SCRIPT_DIR, "roles.md")
    certs_path = os.path.join(SCRIPT_DIR, "certs.json")
    out_interactive = os.path.join(SCRIPT_DIR, "Mapa_Carreras_Ciberseguridad.html")
    out_mindmap = os.path.join(SCRIPT_DIR, "Mapa_Mental_Carreras.html")
    out_general = os.path.join(SCRIPT_DIR, "Mapa_General_Carreras.html")
    out_catalog = os.path.join(SCRIPT_DIR, "Catalogo_Certificaciones.html")
    out_image = os.path.join(SCRIPT_DIR, "Mapa_General_Carreras.png")

    # Paso 1: Parsear roles.md
    print("📖  Leyendo roles.md...")
    try:
        data = parse_md(md_path, certs_path)
    except Exception as e:
        print(f"❌  ERROR al leer roles.md: {e}")
        print("    Revisa que el formato del archivo sea correcto.")
        print("    Tip: asegúrate de no haber borrado las líneas con @.")
        sys.exit(1)

    n_roles = len(data['roles'])
    n_cats = len(data['categories'])
    n_levels = len(data['levels'])
    n_trending = len(data['trending'])

    print(f"   ✓ {n_roles} roles encontrados")
    print(f"   ✓ {n_cats} categorías")
    print(f"   ✓ {n_levels} niveles")
    print(f"   ✓ {n_trending} roles trending")

    # Info de certs enriquecidas
    n_certs_lookup = len(data.get('certsLookup', {}))
    if n_certs_lookup > 0:
        total_enriched = sum(
            sum(1 for c in r.get('certsEnriched', []) if c.get('info'))
            for r in data['roles']
        )
        total_cert_mentions = sum(len(r.get('certsEnriched', [])) for r in data['roles'])
        print(f"   ✓ {n_certs_lookup} certs en base oficial · {total_enriched}/{total_cert_mentions} chips con datos oficiales")
    else:
        print(f"   ⚠️  certs.json no encontrado (los chips de cert no tendrán datos oficiales)")
    print("")

    # Validaciones básicas
    if n_roles == 0:
        print("⚠️  No se encontró ningún rol. Verifica el formato '## Rol #XX: Nombre'.")
        sys.exit(1)

    # Avisar de roles sin categoría o nivel
    sin_cat = [r['id'] for r in data['roles'] if not r.get('cat') or r.get('cat') not in data['categories']]
    sin_nivel = [r['id'] for r in data['roles'] if not r.get('level') or r.get('level') not in data['levels']]
    if sin_cat:
        print(f"⚠️  Roles con categoría inválida o faltante: {sin_cat}")
    if sin_nivel:
        print(f"⚠️  Roles con nivel inválido o faltante: {sin_nivel}")

    # Paso 2: Generar HTML interactivo
    print("🛠   Generando versión interactiva...")
    try:
        size1 = build_interactive(data, out_interactive)
        print(f"   ✓ {os.path.basename(out_interactive)} ({size1:,} chars)")
    except Exception as e:
        print(f"❌  ERROR al generar HTML interactivo: {e}")
        sys.exit(1)

    # Paso 3: Generar mapa mental
    print("🧠  Generando mapa mental por niveles...")
    try:
        size2 = build_mindmap(data, out_mindmap)
        print(f"   ✓ {os.path.basename(out_mindmap)} ({size2:,} chars)")
    except Exception as e:
        print(f"❌  ERROR al generar mapa mental: {e}")
        sys.exit(1)

    # Paso 4: Generar mapa general INTERACTIVO (HTML)
    print("🗺   Generando mapa general interactivo...")
    try:
        size_g = build_general(data, out_general)
        print(f"   ✓ {os.path.basename(out_general)} ({size_g:,} chars)")
    except Exception as e:
        print(f"❌  ERROR al generar mapa general: {e}")
        sys.exit(1)

    # Paso 4b: Catálogo de certificaciones
    print("📜  Generando catálogo de certificaciones...")
    try:
        size_c = build_catalog(data, out_catalog)
        print(f"   ✓ {os.path.basename(out_catalog)} ({size_c:,} chars)")
    except Exception as e:
        print(f"⚠️  No se pudo generar catálogo de certs: {e}")

    # Paso 5: Generar imagen estática del mapa general (PNG)
    print("🎨  Generando imagen PNG del mapa general...")
    try:
        size3 = build_map(data, out_image)
        print(f"   ✓ {os.path.basename(out_image)} ({size3 / 1024:.1f} KB)")
    except Exception as e:
        print(f"⚠️  No se pudo generar la imagen: {e}")
        print("    (necesitas matplotlib: pip install matplotlib)")
        print("    Continuando sin la imagen...")

    print("")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   ✅  ¡LISTO!                                            ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║   {n_roles} roles regenerados.                                  ║")
    print("║                                                          ║")
    print("║   Para verlos, abre con doble clic:                      ║")
    print("║   • Mapa_General_Carreras.html (panorámica interactiva)  ║")
    print("║   • Mapa_Carreras_Ciberseguridad.html (detalle)          ║")
    print("║   • Mapa_Mental_Carreras.html (por niveles)              ║")
    print("║   • Mapa_General_Carreras.png (imagen)                   ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Interrumpido por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌  Error inesperado: {e}")
        print("    Si esto persiste, revisa que roles.md siga el formato original.")
        sys.exit(1)
