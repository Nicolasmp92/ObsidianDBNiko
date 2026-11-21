# DATOS-CLIENTE — Qué debe entregar la institución para su CRIS

> **Documento para enviar al cliente.** Define exactamente qué datos
> necesitamos, en qué formato y con qué calidad, para instalar y poblar un
> DSpace-CRIS conforme a los estándares chilenos (ANID/OpenAIRE/COAR).
> Basado en una instalación real verificada — cada requisito existe porque
> sin él algo se rompe o no emite.

**Nivel de exigencia:** ⬛ obligatorio para partir · ⬜ recomendado (mejora
cumplimiento ANID) · ◻ opcional (desbloquea funciones extra).

---

## 1 · Universos de datos (un archivo por universo)

| Universo | Exigencia | Sin esto |
|---|---|---|
| **Publicaciones** | ⬛ | No hay repositorio. Es el núcleo del encargo |
| **Personas** (investigadores) | ⬜ | Sin ella los autores quedan como texto, sin ficha ni perfil |
| **Unidades** (facultades, institutos, departamentos) | ⬜ | Sin ella no hay navegación por estructura ni afiliación |
| **Proyectos/Financiamiento** | ◻ | El metadato de financiamiento ANID solo se emite con entidades reales (el texto suelto NO cosecha) |
| **Revistas** | ◻ | Se pueden derivar del campo `revista`+`ISSN` de las publicaciones — entregar solo si tienen fuente curada |
| **Fulltext (PDFs)** | ◻ | El repositorio funciona metadata-only; los PDFs se depositan después si se decide |

## 2 · Formato del contenedor (aplica a todos los archivos)

| Regla | Especificación |
|---|---|
| Formato | **CSV** (o XLSX — lo convertimos). Un archivo por universo |
| Codificación | **UTF-8** |
| Separador | `;` punto y coma (o `,` — declarar cuál usan) |
| Multivalor | `\|\|` (doble pipe) — ej: `Autor Uno\|\|Autor Dos` |
| Fechas | `AAAA` o `AAAA-MM-DD` — **nunca** `2016.0` ni `05-03-2019` ambiguo |
| Encabezados | Primera fila = nombres de columna (los de las tablas §3 o los propios — el mapeo lo hacemos nosotros) |
| Unicidad | Una fila = un registro; **sin duplicados por DOI** ni por ID |
| Vacíos | Celda vacía, no `N/A`, `-`, `sin dato` |

## 3 · Especificación por entidad

### 3.1 · Publicaciones ⬛

Columnas **mínimas** (los 6 mandatorios ANID):

| Columna | Campo DSpace | Formato | Ejemplo |
|---|---|---|---|
| `id` | identificador local | único, correlativo | `PUB_0001` |
| `titulo` | `dc.title` | texto | `Efectos del cambio climático…` |
| `autores` | `dc.contributor.author` | `Apellidos, Nombres\|\|` | `Soto, Ana\|\|Pérez, Juan` |
| `anio` | `dc.date.issued` | `AAAA` | `2024` |
| `tipo` | `dc.type` | vocabulario del cliente (lo mapeamos a COAR) | `Artículo` |
| `acceso` | `dc.rights`/`oairecerif.access` | `open access` / `metadata only access` / `embargoed access` / `restricted access` | `open access` |

Columnas **recomendadas** (suben el cumplimiento MA/R):

| Columna | Campo DSpace | Formato | Nota |
|---|---|---|---|
| `doi` | `dc.identifier.doi` | `10.xxxx/...` **sin** `https://doi.org/` | clave de dedup y de enriquecimiento |
| `resumen` | `dc.description.abstract` | texto | |
| `idioma` | `dc.language.iso` | `spa`/`eng`/`por` | |
| `editorial` | `dc.publisher` | texto | |
| `palabras_clave` | `dc.subject` | `\|\|` | |
| `revista` | `dc.relation.journal` / `dc.source` | nombre canónico | alimenta entidad Journal |
| `issn` | `dc.identifier.issn` | `1234-5678` (print y/o eISSN, `\|\|`) | |
| `volumen` / `numero` / `pagina_inicio` / `pagina_fin` | `oaire.citation.*` | texto/número | la cita completa |
| `financiamiento` | `dc.relation.funding` | texto libre | ej: `FONDECYT 1123456` |
| `autor_correspondiente` | `dc.contributor.corresponding` | `Apellidos, Nombres` | |
| `unidad` | `dc.relation.orgunit` | nombre exacto de la unidad (debe existir en el archivo de unidades) | ruteo a colección |
| `isi` / `scopus` | `dc.identifier.isi` / `dc.identifier.scopus` | IDs | identificadores alternos |
| `area_ocde` / `subarea_ocde` / `cned` / `sies` | `dc.subject.ocde*` | taxonomías chilenas | ⬜ si no las traen, **las derivamos** desde WoS/Scopus o ISSN (~80% cobertura probada) |
| `orcid_autores` | identificador de autor | `0000-0000-0000-0000` o URL | permite enlazar Persons |
| `url_oa` | `dc.identifier.uri` | URL del fulltext externo | diagnóstico de acceso |
| `version` | `oaire.version` | `publishedVersion`/`acceptedVersion`… | vocabulario COAR |
| `embargo_fin` | `oairecerif.access.embargoEnd` | `AAAA-MM-DD` | solo si hay ítems embargados |

### 3.2 · Personas ⬜

| Columna | Campo DSpace | Exigencia | Nota |
|---|---|---|---|
| `id_persona` o `rut` | `person.identifier` | ⬛ **identificador único estable** — RUT es ideal (`12.345.678-9`) | lección probada: el RUT resolvió 254/254 identidades sin ambigüedad |
| `nombre_completo` | `dc.title` | ⬛ `Apellidos, Nombres` | sin este campo la ficha sale **vacía** en la cosecha CERIF — es mandatorio aunque no lo parezca |
| `orcid` | `person.identifier.orcid` | ⬜ | `https://orcid.org/0000-…` o ID corto |
| `unidad` | `person.affiliation.name` | ⬜ | debe calzar con el archivo de unidades |
| `email` | `person.email` | ◻ | oculto por defecto en la UI |
| `genero` / `fecha_nacimiento` | `oairecerif.person.*` | ◻ | se pueden ocultar vía config |

### 3.3 · Unidades organizacionales ⬜

| Columna | Exigencia | Nota |
|---|---|---|
| `id_unidad` | ⬛ | |
| `nombre` | ⬛ | nombre oficial canónico |
| `unidad_padre` | ⬜ | para la jerarquía (Departamento → Facultad → Universidad) |
| `tipo` | ◻ | facultad/instituto/departamento/centro |

### 3.4 · Proyectos/Financiamiento ◻

Solo si el cliente quiere que el metadato `fundingReferences` coseche a
ANID (el texto suelto en publicaciones no basta):

| Columna | Nota |
|---|---|
| `id_proyecto` | código ANID/agencia: `FONDECYT 1123456`, `ANID ATE…` |
| `titulo_proyecto` | |
| `agencia` / `programa` | ANID, FIA, interno… |
| `investigador_responsable` | debe calzar con `id_persona`/`rut` |
| `publicaciones_vinculadas` | IDs de `id` del archivo de publicaciones |

### 3.5 · Archivos (fulltext) ◻

Si el alcance incluye depósito: carpeta de PDFs nombrada por `id` de la
publicación, o columna `archivo` con nombre/ruta. Se monta por SAF
(Simple Archive Format) — no hace falta que preparen estructura.

## 4 · Reglas de calidad que pedimos de la entrega

Estas son las condiciones de aceptación — las medimos al recibir:

1. **0 duplicados por DOI** (y por `id`) en cada archivo
2. **6 campos mandatorios al 100%** en publicaciones (o lista explícita de
   los ítems que no los cumplen)
3. **IDs estables**: el `id`/`rut` de una persona es el mismo en todas las
   cargas futuras — es la clave de actualización incremental
4. **Nombres de unidad canónicos**: `unidad` en publicaciones y personas
   debe ser *exactamente* el `nombre` del archivo de unidades
5. **Autores en formato `Apellidos, Nombres`**, uno por celda multivalor
6. Fechas e identificadores en los formatos de §2 (DOI sin URL, ORCID
   completo, ISSN con guion)

## 5 · Lo que NO necesitamos que preparen

Se lo decimos explícito para que no gasten esfuerzo:

- Las **entidades Journal** se derivan solas de `revista`+`issn`
- Las **áreas OCDE/CNED/SIES** se derivan desde WoS/Scopus/ISSN si no las
  traen (tabla de cruce propia, cobertura probada ~80-94%)
- La **licencia Creative Commons real** se enriquece por DOI vía
  Unpaywall (en el lab resolvió 919/1.634 DOIs)
- El **mapeo a vocabulario COAR** de tipos, accesos y versiones es nuestro
- **Duplicados de grafía** (mismo valor con distinto case) los normalizamos

## 6 · Mínimo viable vs entrega ideal

| Si traen… | Resultado |
|---|---|
| Solo §3.1 mínimo | CRIS funcionando, cumple M de ANID — sin entidades ni facetas |
| §3.1 completo | + cita, financiamiento-texto, taxonomías derivadas, niveles R |
| + personas + unidades | + fichas de investigador, navegación por estructura, CERIF con nombres reales |
| + proyectos | + `fundingReferences` cosechable por ANID (requisito completo MA) |
| + PDFs | repositorio con fulltext — depósito y `oaire:file` |

## 7 · Cómo se entrega

1. Archivos por universo en CSV/XLSX según §2
2. **Diccionario de datos propio** si usan columnas distintas a §3 (una
   línea por columna: nombre, qué es, formato)
3. Muestra previa de 20–50 filas (**canario**) antes de la carga total —
   la validamos primero
4. Canal único de consulta de curación (quien decide sobre ambigüedades:
   autores sin unidad, unidades ambiguas, excepciones de taxonomía)

> **Regla del proyecto:** *cero ambigüedad declarada = cero tolerancia a
> relleno*. Los casos ambiguos se devuelven listados para decisión del
> cliente — nunca se "adivinan".
