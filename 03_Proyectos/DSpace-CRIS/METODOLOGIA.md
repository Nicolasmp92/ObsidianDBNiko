# METODOLOGÍA — Instalación rápida de DSpace-CRIS (producto de arranque)

Método de trabajo repetible para vender "instalación + puesta en marcha de
DSpace-CRIS" a instituciones chilenas. Objetivo: de encargo firmado a
instancia operativa y conforme-ANID en el menor tiempo posible, sin
depender de memoria — cada fase tiene checklist, entregable y gate.

Referencias: `INSTALACION.md` (receta técnica), `ESTANDARES-CL.md`
(cumplimiento chileno). Fuente de lecciones: bitácora lab UOH.

## Fase 0 — Levantamiento (antes de cotizar)

Recoger del cliente, en una sola reunión + formulario:

- [ ] Servidor destino: propio Linux / VPS / nube — specs (≥8 GB RAM, disco, OS)
- [ ] Dominio + HTTPS (quién administra DNS)
- [ ] Alcance: ¿solo instalar? ¿+ datos iniciales? ¿+ tema/marca? ¿+ capacitación?
- [ ] Volumen y fuente de datos iniciales (xlsx/CSV de WoS/Scopus/ANID/SIS)
- [ ] ¿Metadata-only o depósito de fulltext (PDFs)?
- [ ] ¿ORCID de investigadores disponibles?
- [ ] Responsable institucional y canal de aprobaciones

**Entregable:** acta de alcance + presupuesto por fases. **Gate:** alcance
firmado — sin esto no se cotiza (lección: los gaps de cumplimiento nacen de
la fuente de datos, hay que verla antes de prometer).

## Fase 1 — Infraestructura

- [ ] Server Linux aprovisionado (SSH por llave, UFW, Docker + compose)
- [ ] DNS apuntado, Traefik/nginx + Let's Encrypt
- [ ] Backups desde día 1: `pg_dump` cron + volumen assetstore fuera del host
- [ ] Monitor (Uptime Kuma o equivalente) contra `/server/api` y front

**Entregable:** server endurecido + runbook de acceso. **Gate:** `docker compose version` OK y DNS resuelve.

## Fase 2 — Instalación base (la receta, ~1-2 h)

Seguir `INSTALACION.md` tal cual:

- [ ] Clon tag `dspace-cris-2025.02.00` + `.env`
- [ ] `docker compose up -d` → migración automática → los 4 servicios Up
- [ ] `create-administrator`
- [ ] `initialize-entities` **ambos XML** (relationship-types +
  correction-relationship-types — la trampa documentada)
- [ ] `restart: unless-stopped` en todos los servicios

**Entregable:** instancia vacía operativa. **Gate:** 3 endpoints OAI
responden `Identify` + login admin.

## Fase 3 — Configuración estándar chileno

- [ ] Esquema de metadatos: campos ANID registrados (`oaire.*`,
  `oairecerif.*`, citation.*, `oaire.licenseCondition`, `dc.type` curado en español si el cliente lo pide)
- [ ] `mapConverter-coarTypes.properties` con el mapeo `dc.type`→URI COAR
- [ ] Taxonomías OCDE área/subárea + CNED + SIES como campos de subject
- [ ] `metadata-security.cfg`: qué campos se ven en "todos los metadatos"
- [ ] Marca: logo, colores, nombre institucional, correo de contacto
- [ ] Comunidades/colecciones iniciales según estructura del cliente
- [ ] Registro en LA Referencia / Nodo ANID (trámite del cliente, asistir)

**Entregable:** config-cris versionado del cliente. **Gate:** record de
prueba emite OAI correcto en `openaire4` y `openairecris`.

## Fase 4 — Datos (si está en alcance)

- [ ] Plantilla CSV del cliente → transform a campos DSpace (patrón probado:
  transform script versionado + canario de N registros primero)
- [ ] Cargas: `metadata-import -v -w` por paquetes pequeños con log
- [ ] Entidades derivadas: Persons/OrgUnits/Journal-Volumes desde metadatos
  (lección: se construyen post-carga, no se importan sueltas)
- [ ] Enriquecimiento opcional: Unpaywall por DOI → licencia CC real +
  `url_for_pdf` (919/1634 DOIs resueltos en el lab)
- [ ] `oai import -c` + purge de caché OAI tras cada paquete grande

**Entregable:** ítems cargados + informe de brechas de la fuente.
**Gate:** matriz ANID medida — 6/6 M, MA aplicables, R reportados.

## Fase 5 — Verificación y entrega

- [ ] Checklist `ESTANDARES-CL.md` §5 completo (3 OAI + M al 100% + COAR)
- [ ] Prueba de cosecha por LA Referencia/Nodo (coordinar con el cliente)
- [ ] Runbook de operación entregado (arranque, backup, restore, CLI común)
- [ ] Capacitación admin (si está en alcance): cargas, entidades, correcciones
- [ ] Cierre: bitácora del proyecto + handoff documentado

**Gate final:** institución cosechable por la cadena ANID y operación
transferida.

## Reuso acumulado (cada encargo engorda el kit)

| Artefacto | De dónde sale | Estado |
|---|---|---|
| Receta instalación | `INSTALACION.md` (lab UOH) | ✅ lista |
| Baseline ANID | `ESTANDARES-CL.md` (auditoría verificada) | ✅ lista |
| Transform CSV genérico | `scripts/transform_v2_curado.py` (repo UOH) — reescribir sin campos uoh.* | ⏳ adaptar por encargo |
| Config systemd prod | `docs/servidor/propuesta-systemd-cris.md` | ⏳ adaptar |
| Enriquecedor Unpaywall | `scripts/r_enriquecer_unpaywall.py` | ✅ reusable tal cual (sin datos UOH) |
| Monitor watchdog | `docs/servidor/monitoreo-watchdog.md` | ⏳ adaptar |

> **Regla de oro del producto:** lo que se aprenda en un encargo vuelve a
> esta carpeta (bitácora + doc nuevo o actualizado) — el kit mejora solo.
