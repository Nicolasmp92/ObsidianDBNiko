---
tipo: documento
proyecto: rescuedatos
actualizado: 2026-11-21
tags: [script, referencia, pipeline]
---
# 📄 Script `consolidar_respaldos.py` — comportamiento

Consolida N carpetas de respaldo/volcado en **una carpeta destino** ordenada por tipo de archivo. Diseñado para el flujo "rescaté datos crudos de un equipo dañado → entrego carpeta ordenada al cliente". Python 3, stdlib only, sin dependencias.

**Fuente:** `scripts/consolidar_respaldos.py` (este proyecto).

## Contrato

| | |
|---|---|
| **Entrada** | `SRC_ROOTS`: lista de carpetas origen (volcados) |
| **Salida** | `DST`: carpeta única con subcarpetas por categoría + `_log_movimientos.csv` + `_log_duplicados.csv` |
| **Garantía** | Todo archivo del origen termina en el destino, en `_Programas/`, o eliminado **solo si es duplicado idéntico verificado por hash**. Nada se pierde en silencio. |
| **Invariante de verificación** | `archivos_origen_total = movidos + programas + duplicados_eliminados` y `leftover_files = 0` |

## Fases de ejecución (en orden)

### 1. Junk → `_Programas/` (wholesale)

Los directorios listados en `JUNK` se mueven **enteros** a `DST/_Programas/<nombre>` con un solo rename — sin clasificar archivo por archivo. Es la parte más rápida (mueve decenas de miles de archivos en un instante).

- **Qué va en `JUNK`:** installs de programas recuperadas (`AutoCAD 2024/`, `D5 Render/`, `Engine/`, `Binaries/`, perfiles de Adobe). Se identifican **explorando antes de correr**, no por extensión.
- Si el nombre destino ya existe → sufijo ` (2)`.
- Si la ruta `JUNK` no existe → `[skip]` y sigue (no aborta).

### 2. Clasificación por extensión

Recorre los orígenes con `os.walk` (incluye ocultos) y asigna cada archivo a una categoría:

| Categoría | Extensiones |
|---|---|
| `Documentos/` | pdf doc docx xls xlsx ppt pptx odt ods odp rtf txt csv xps epub md pub vsd vsdx one |
| `Imagenes/` | jpg jpeg png gif webp svg tif tiff bmp heic heif ico cr2 nef arw dng raw jfif avif jp2 exr hdr |
| `Videos/` | mp4 mov avi mkv webm m4v 3gp wmv mpg mpeg mts m2ts vob flv |
| `Audio/` | mp3 wav m4a aac flac ogg opus wma mid midi aif aiff |
| `Proyectos/` | ai psd psb indd idml eps xd fig sketch dwg dxf dwt rvt rfa rte skp skb d5a d5s prproj aep blend obj fbx 3ds max c4d stl step stp iges igs lsp dyn bak sv$ pln pla 3dm gh ghx |
| `Correos/` | msg eml pst ost mbox |
| `Comprimidos/` | zip rar 7z tar gz bz2 xz cab iso dmg tgz |
| `Instaladores/` | exe msi msix appx pkg deb rpm |
| `Otros/` | todo lo demás (tmp, lnk, aae, json, dll sueltos…) |

- Extensión evaluada en minúsculas (`.JPG` = `.jpg`). Archivos sin extensión → `Otros`.
- **Regla de edición:** una extensión vive en una sola categoría; al agregar una, borrarla de donde estaba.

### 3. Ruta destino (regla `STRIP`)

Destino = `DST/<Categoría>/<ruta relativa del archivo>` — la estructura interna del origen se **preserva** (no es volcado plano).

**Excepción:** si el primer nivel es carpeta de perfil de usuario, se omite:

```text
STRIP = {escritorio, documentos, descargas, imagenes, downloads,
         desktop, documents, pictures, videos, music}

escritorio/Arquitectura/casa.dwg   → Proyectos/Arquitectura/casa.dwg
imagenes/FOTOS/202505_b/x.jpg      → Imagenes/FOTOS/202505_b/x.jpg
Mobile Devices/IMG_1993.jpeg       → Imagenes/Mobile Devices/IMG_1993.jpeg
```

### 4. Colisiones y dedup

Cuando `destino` ya existe:

```text
mismo tamaño?  ──no──→  renombrar "nombre (2).ext" (acción: renombrado)
     │sí
  md5 iguales? ──no──→  renombrar "nombre (2).ext"
     │sí
  eliminar archivo origen (duplicado idéntico verificado)
  → _log_duplicados.csv registra origen + dónde quedó la copia + hash
```

- Solo se hashea cuando hay colisión de nombre **y** tamaño — eso mantiene la corrida rápida (mover = rename, no copia de bytes).
- ` (n)` incrementa hasta encontrar nombre libre.
- **Lo que NO deduplica:** mismo contenido con nombre distinto (conserva ambos — seguro).

### 5. Limpieza de orígenes

Recorrido bottom-up borrando directorios vacíos. Las carpetas origen que quedan 100% vacías desaparecen solas. Al final imprime `leftover_files` por origen — debe ser `0`; si no, quedó algo sin procesar (investigar, no ignorar).

## Salidas y trazabilidad

- `_log_movimientos.csv` — cada archivo: `origen, destino, accion` (`movido` / `renombrado` / `programa_directorio` / `duplicado_identico_eliminado` / `ERROR: …`).
- `_log_duplicados.csv` — duplicados eliminados: `origen_eliminado, conservado_en, md5`.
- Ambos UTF-8 con BOM (abren directo en Excel).
- Consola: progreso cada 500 archivos + resumen final `movidos / renombrados / duplicados / errores / dirs_vacios`.

## Qué NO hace (límites deliberados)

- **No copia bytes:** todo es `shutil.move` (rename). Solo sirve origen y destino **en el mismo volumen**; entre discos distintos `shutil.move` sí copia, pero lento y sin reanudación — para eso usar robocopy/rsync y adaptar.
- **No borra nada no verificado:** excepto duplicados idénticos por hash. El junk va a `_Programas`, no a la papelera.
- **No mira contenido:** clasifica por extensión, no por magic bytes. Un `.pdf` renombrado `.jpg` va a `Imagenes`.
- **No sigue symlinks** (los salta).
- **No reanuda:** si se interrumpe, re-correr es seguro (lo ya movido no está en origen; lo pendiente se procesa), pero los logs se sobrescriben.

## Parametrización por caso (antes de cada encargo)

```python
SRC_ROOTS = [...]   # carpetas del volcado del cliente
DST       = Path(r"D:\Respaldo <Cliente>")
JUNK      = [...]   # dirs de programas hallados EXPLORANDO, nunca adivinar
STRIP     = {...}   # agregar si el perfil usa otros nombres (ej. "Users/X/Desktop")
CATS      = {...}   # mover extensiones entre categorías si el cliente pide otra agrupación
```

## Evolución pendiente (backlog técnico)

- [ ] `--dry-run`: reportar categorías y volúmenes sin tocar nada (ideal para cotizar al cliente)
- [ ] Dedup global opcional (índice tamaño→hash de todo el set, no solo colisiones de nombre)
- [ ] Reporte final legible (markdown/html) para entregar junto a la carpeta
- [ ] Subcategoría `Proyectos/` por familia (CAD vs Adobe vs 3D) si el volumen lo amerita
- [ ] Detección automática de junk por heurística (alta densidad de dll/exe/pyc + nombres de install) — hoy es manual

## Lecciones del caso 1 (Alejandra, 2026-11-21)

- ~60% del volumen rescatado era **programa reinstalable**, no datos — explorar `JUNK` primero es lo que más tiempo ahorra.
- Los volcados de recovery mezclan perfiles (`escritorio/`, `documentos/`) con exports sueltos (`1x/`, `72ppi/`): `STRIP` + preservación de ruta lo resuelve sin intervención manual.
- 36.838 archivos / ~50 GB de datos de usuario en **28 s** porque todo fue rename en el mismo volumen — no subestimar el costo si el destino fuera otro disco o red.
