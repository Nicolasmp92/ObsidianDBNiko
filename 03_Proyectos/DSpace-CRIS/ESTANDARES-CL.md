# ESTÁNDARES-CL — Baseline de cumplimiento chileno para DSpace-CRIS

Lo que una instalación chilena debe exponer para interoperar con la cadena
**repo institucional → Nodo Nacional ANID → LA Referencia → OpenAIRE**.
Fuente: *Metadatos para la Interoperabilidad de los Repositorios* (ANID,
Nodo Nacional de Acceso, ene-2024) + auditoría verificada del lab UOH
(`docs/referencias/cumplimiento-anid-2024.md`, mediciones reales).

## 0 · El estándar en una línea

OpenAIRE Guidelines v4.0 + Dublin Core + **OAI-PMH** + vocabulario **COAR**
→ 32 metadatos en 4 niveles: **M** 6 · **MA** 8 · **R** 15 · **O** 3.

## 1 · Endpoints OAI que deben responder (gate de interoperabilidad)

| Endpoint | Formato | Para qué |
|---|---|---|
| `/server/oai/request?verb=Identify` | `oai_dc`, mets, didl, qdc, mods | OAI-PMH clásico — LA Referencia |
| `/server/oai/openaire4?verb=Identify` | `oai_openaire` | **OpenAIRE Literature v4.0 — el que ANID nombra** |
| `/server/oai/openairecris?verb=Identify` | `oai_cerif_openaire` | Perfil CERIF-CRIS (persons, orgunits, projects) |

Tras cargas masivas: `oai import -c` **y borrar caché** en
`/dspace/var/oai/requests/` del contenedor backend (trampa: el `-c` solo
purga el volumen del CLI, no el del backend).

## 2 · Matriz ANID → campos DSpace-CRIS (verificada en lab real)

### Mandatorios (M) — gate mínimo de entrega

| Etiqueta ANID | Campo DSpace | Emisión OAI |
|---|---|---|
| Título | `dc.title` | `datacite:title` + CERIF `<Title>` |
| Creador | `dc.contributor.author` | `datacite:creator` + CERIF `<Author>` |
| Fecha publicación | `dc.date.issued` | `datacite:date` |
| Tipo de recurso | `oaire.resourceType` (URI COAR) | `oaire:resourceType uri=` + CERIF `<Type>` |
| Identificador | `dc.identifier.doi` + handle | `datacite:identifier` |
| Derechos de acceso | `dc.rights`/`dc.rights.uri`/`oairecerif.access` | `datacite:rights rightsURI=COAR` + `<Access>` |

**Lecciones medidas:** `dc.title` también en *Persons* (`Apellidos, Nombres`)
o el `<PersonName>` CERIF sale vacío; `oairecerif.access` con URI COAR
alimenta `<Access>`; el mapeo `dc.type` → URI COAR vive en
`mapConverter-coarTypes.properties` (sin él, `<Type>` cae al default
`c_1843`).

### Mandatorios si aplica (MA)

| Etiqueta | Campo DSpace | Nota |
|---|---|---|
| Colaborador | `dc.contributor.*` | `datacite:contributor` |
| Financiamiento | `oaire.fundingReference` + **entidad Funding** | ⚠ el texto no basta: `oaire:fundingReferences` solo emite si hay entidad `Funding`/`Project` relacionada (`isFundingOfPublication`) |
| Embargo | `oairecerif.access.embargoEnd` | atributo `endDate` de `<Access>` — sale solo si hay ítems embargados |
| Idioma | `dc.language.iso` | normalizar (eng/spa/por…) |
| Editorial | `dc.publisher` | |
| Descripción | `dc.description.abstract` | |
| Materia | `dc.subject` + taxonomías CL (§3) | `datacite:subject` |
| Ubicación del archivo | bitstream `ORIGINAL` → `oaire:file` | solo si hay fulltext; metadata-only no aplica |

### Recomendados (R) — los que más pesan

| Etiqueta | Campo |
|---|---|
| Identificadores alternativos/relacionados | `dc.relation.ispartof`, `dc.relation.issn`, ISI/Scopus → `relatedIdentifier` |
| Licencia | `oaire.licenseCondition` + `dc.rights.uri` (URI CC o COAR; Unpaywall por DOI es la vía probada) |
| Versión | `oaire.version` (COAR version vocabulary) |
| Cita | `oaire.citation.title/volume/issue/startPage/endPage` — copiar de `dc.source`/`dc.description.*` |
| Fuente | `dc.source` |

### Optativos (O)
`datacite.size`, `datacite.geoLocation`, `dcterms.audience` — poblar si la fuente los trae.

## 3 · Taxonomías chilenas de materia

Clasificación que reportan ANID/Mineduc — configurar como campos de subject:

| Taxonomía | Origen | Niveles | Uso |
|---|---|---|---|
| **OCDE (Frascati)** | internacional | 7 áreas + **39 subáreas** | área+subárea = la grana fina que pide Chile |
| **CNED** | Consejo Nacional de Educación | 11 | acreditación |
| **SIES** | Mineduc | 11 | información educ. superior |

Lección del lab: OCDE/CNED/SIES derivan por tabla de cruce desde WoS/Scopus
(cubre ~82-94%); el resto por fallback institucional. El doc fuente:
`docs/referencias/indices-y-taxonomias.md`.

## 4 · Otros identificadores del ecosistema chileno

- **ORCID**: emisión `oairecerif:personIdentifier` / authority ORCID en
  Persons — ORCID-Chile ofrece feed OAI-ORE para traer publicaciones.
- **Handle**: cada ítem trae URI handle — sirve de `datacite:identifier` de
  respaldo cuando no hay DOI.
- **Fechas**: normalizar `2016.0` → `2016` (las fuentes xlsx traen decimales).

## 5 · Checklist de verificación por entrega

- [ ] `Identify` responde en los 3 endpoints OAI
- [ ] Los 6 M poblados al 100% (o brecha documentada por ítem)
- [ ] `datacite:rights` con URI COAR en cada record de `openaire4`
- [ ] CERIF: `<PersonName>` con nombre real (→ `dc.title` en Persons)
- [ ] `dc.type` → URI COAR correcto (revisar `mapConverter-coarTypes`)
- [ ] Funding solo si hay entidades Funding/Project reales
- [ ] Caché OAI purgado tras cargas masivas
