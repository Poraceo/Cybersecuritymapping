# 📖 LEEME — Sistema editable de Cyber.map

¡Hola! Este sistema te permite editar el contenido de los HTMLs de carreras
de ciberseguridad sin tocar código HTML.

---

## 🎯 Resumen rápido

1. Abrís `roles.md` en cualquier editor de texto.
2. Cambiás lo que quieras (salarios, descripciones, skills, proyecciones, lo que sea).
3. Corrés `python actualizar.py` en la terminal.
4. Los 4 archivos finales se regeneran solos.

---

## 📁 Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| **`roles.md`** | ⭐ El archivo que editás. Contiene los 50 roles y configuración. |
| **`actualizar.py`** | ⭐ El script que corrés para regenerar los archivos. |
| `LEEME.md` | Este archivo. |
| `parser.py`, `build_*.py` | Motor del sistema. **No los edites.** |
| `Mapa_General_Carreras.html` | 🆕 Vista panorámica INTERACTIVA con filtros. |
| `Mapa_Carreras_Ciberseguridad.html` | App con navegación completa por niveles/categorías. |
| `Mapa_Mental_Carreras.html` | Vista por niveles (orientación más vertical). |
| `Mapa_General_Carreras.png` | Imagen estática para compartir/imprimir. |

### 🆕 Las 4 vistas — cuándo usar cada una

| Vista | Cuándo usarla |
|---|---|
| **Mapa General** (HTML) | En lives de TikTok como vista principal. Tiene filtros por categoría/nivel y permite hacer click en cualquier rol para ver detalle. |
| **App con detalle** (HTML) | Cuando alguien pregunta por un rol específico, navegás por categorías o niveles, ves descripción completa, skills, certificaciones. |
| **Vista por niveles** (HTML) | Para mostrar la progresión de carrera visualmente desde Junior hasta C-Level. |
| **Imagen PNG** | Para compartir por WhatsApp, subir a redes, imprimir. |

---

## ✅ Requisitos (una sola vez)

### Python 3.6+

```
python --version
```

Si te dice "command not found", probá con `python3 --version`. Si no lo tenés:
- **Mac:** ya viene, probá con `python3`.
- **Windows:** descargá de https://www.python.org/downloads/ y marcá "Add Python to PATH".

### Matplotlib (solo para la imagen PNG)

Si querés que se genere la imagen PNG, instalá matplotlib una sola vez:

```
pip install matplotlib
```

> Si no lo instalás, igual funciona: solo no se genera el PNG, los HTMLs sí.

---

## 🖊 Cómo editar `roles.md`

Abrilo con cualquier editor:
- **Bloc de Notas** (Windows) / **TextEdit** (Mac) — funcionan
- **VS Code**, **Sublime Text**, **Notepad++** — mejores si editás mucho

### Estructura de un rol

```
## Rol #01: SOC Analyst Tier 1
@rolES: Analista SOC Nivel 1
@cat: defensive
@nivel: junior
@anos: 0-2 años
@sinonimos: Security Operations Analyst · Junior SecOps
@salario_mes: $700 - $6,700
@salario_ano: $8,400 - $80,000
@demanda: MUY ALTA
@remoto: Híbrido (turnos 24/7)
@relacionados: 2, 3, 4, 38

# OPCIONALES — campos de proyección (puedes agregarlos a cualquier rol):
@proyeccion: +18% en 2 años (entry-level más demandado en LATAM)
@tendencia: AI augmenting alert triage pero NO reemplazando analistas
@salto_salarial: De $8K (Junior LATAM) a $80K (Senior USA)
@dificultad: Baja (con Security+ y ganas, 6 meses de prep)

### Descripción
Texto libre describiendo qué hace el rol.

### Hard Skills
- Cosa 1
- Cosa 2

(... etc ...)
```

### 📌 Campos OBLIGATORIOS (no los borres)

| Campo | Qué pone |
|---|---|
| `@rolES` | Nombre en español |
| `@cat` | Una de: `defensive`, `offensive`, `architecture`, `specialized`, `grc`, `legal`, `leadership`, `sales`, `awareness`, `operations`, `ecosystem` |
| `@nivel` | Una de: `junior`, `mid`, `senior`, `manager`, `executive` |
| `@anos` | Rango años de experiencia |
| `@sinonimos` | Otros nombres del rol (separados por · ) |
| `@salario_mes` | Rango mensual USD: `$X,XXX - $X,XXX` |
| `@salario_ano` | Rango anual USD |
| `@demanda` | `MUY ALTA`, `ALTA`, `MEDIA`, `EXPLOSIVA` |
| `@remoto` | Tipo de trabajo |
| `@relacionados` | IDs de roles relacionados, separados por coma |

### 🆕 Campos OPCIONALES de proyección

Estos aparecen como una sección **"Proyecciones 2026-2028"** en el detalle del rol.
Solo agregalos donde tengas info. Si no los tenés, no pasa nada — el rol funciona igual.

| Campo | Qué pone |
|---|---|
| `@proyeccion` | Crecimiento esperado, ej: `+45% en 3 años` |
| `@tendencia` | Tendencia de mercado 2026-2028 (texto libre) |
| `@salto_salarial` | De cuánto a cuánto crece Junior→Senior |
| `@dificultad` | `Baja`, `Media`, `Alta`, `Muy alta` |

**Ya están agregados como ejemplo en los roles #01, #13 y #23** — mirá esos primero para ver cómo se ven y copiá el formato.

---

## ✏️ Ejemplos de ediciones comunes

### Cambiar un salario
```
@salario_mes: $1,000 - $7,000     ← antes
@salario_mes: $1,200 - $8,500     ← después
```

### Agregar proyecciones a un rol
Localizás el rol y debajo del último `@` (antes de `### Descripción`) agregás:
```
@proyeccion: +30% en 2 años
@tendencia: La banca digital LATAM está duplicando equipos AppSec
@dificultad: Media
```

### Agregar una herramienta
```
### Tools
- Splunk
- Sentinel
- TU NUEVA HERRAMIENTA   ← simplemente agrega una línea con guion
```

### Cambiar el color de una categoría
Arriba en el archivo:
```
@categoria defensive: Defensivo / Blue Team | #60A5FA    ← antes
@categoria defensive: Mi Nuevo Nombre | #00FF00          ← después
```

### Agregar un rol nuevo
Copiá un bloque desde `## Rol #XX` hasta antes del siguiente `## Rol`, y cambiale el ID:
```
## Rol #51: Tu Nuevo Rol
@rolES: Tu rol en español
@cat: defensive
@nivel: mid
@anos: 3-5 años
@sinonimos: Nombre alternativo
@salario_mes: $2,000 - $10,000
@salario_ano: $24,000 - $120,000
@demanda: ALTA
@remoto: Remoto disponible
@relacionados: 1, 3

### Descripción
Qué hace.

### Hard Skills
- Habilidad

(... etc, las otras secciones ...)
```

---

## ▶️ Cómo regenerar los HTMLs

Una vez que terminaste de editar `roles.md`:

### Mac:
1. Abrí la **Terminal** (Cmd + Espacio → escribe "Terminal").
2. Navegá hasta esta carpeta. Ejemplo:
   ```
   cd ~/Desktop/cyber-map
   ```
3. Corrés:
   ```
   python3 actualizar.py
   ```

### Windows:
1. Abrí la carpeta en el explorador.
2. Mantené `Shift` y hacé clic derecho → "Abrir ventana de PowerShell aquí".
3. Corrés:
   ```
   python actualizar.py
   ```

### ¿Funcionó?

Verás algo así:
```
📖  Leyendo roles.md...
   ✓ 50 roles encontrados
🛠   Generando versión interactiva...
🧠  Generando mapa mental por niveles...
🗺   Generando mapa general interactivo...
🎨  Generando imagen PNG del mapa general...
✅  ¡LISTO!
```

Luego abrí los HTMLs con doble clic. 🎉

---

## 🛠 Solución a problemas

| Error | Solución |
|---|---|
| `command not found: python` | Probá con `python3` |
| `No encuentro el archivo roles.md` | Hacé `cd` a la carpeta donde están los archivos |
| `ERROR al leer roles.md` | Borraste un `@campo:` obligatorio. Compará con otro rol |
| `Roles con categoría inválida` | Usá una categoría válida (lista arriba) |
| `No se pudo generar la imagen` | Instalá matplotlib: `pip install matplotlib` |
| Los cambios no aparecen | Refrescá con `Cmd+Shift+R` (Mac) o `Ctrl+Shift+R` (Win) |

---

## 💡 Tip: workflow para el live de TikTok

1. **Antes del live:** revisá si querés agregar info nueva (proyecciones, salarios actualizados, roles nuevos).
2. Editá `roles.md`, corré `python actualizar.py`.
3. Abrí **`Mapa_General_Carreras.html`** y empezá el live con la vista panorámica:
   *"Mira todo el universo de la ciberseguridad de un vistazo..."*
4. Usá los filtros de categoría/nivel para ir destacando áreas según las preguntas de tu audiencia.
5. Hacé click en cualquier rol para abrirlo en la versión detallada con todo: skills, certs, mercados, proyecciones.

---

## 🤝 Atajo: ¿no querés correr el script?

Si te resulta más fácil, **pasale a Claude el `roles.md` editado por chat** con los cambios
que querés. Él lo procesa y te devuelve los HTMLs listos para descargar, sin que tengas
que correr el script ni instalar matplotlib ni nada.

¡Disfrutá! 🚀
