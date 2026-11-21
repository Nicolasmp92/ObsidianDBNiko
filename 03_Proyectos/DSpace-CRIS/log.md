# Log — DSpace-CRIS (instalación para cliente externo)

Bitácora append-only. Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO / PENDIENTE.

Repo/código: `C:\Users\Niko\dspace-cris-lab` (clon `4Science/DSpace` @ `dspace-cris-2025.02.00`).
Stack: DSpace-CRIS 2025.02.00 + Docker Compose (backend, Angular, Postgres 15, Solr, Matomo opc.).
Fuente de conocimiento: `repositorios-digitales-uoh/DSPACE-CRIS/` (bitácora UOH).

## 2026-11-20 — Nace el proyecto

- **DECISIÓN** — Se crea el proyecto por encargo de un **contacto externo**:
  instalación y puesta en marcha de DSpace-CRIS. Es trabajo independiente de
  la línea UOH (donde el usuario es contraparte técnica del CRIS institucional,
  implementación a cargo de Francisco/UChile).
- **HECHO** — Pull del repo UOH: 226 commits nuevos (`b0f32f1`). La bitácora
  CRIS cubre 3 meses de lab: stack Docker verificado, cargas CSV, entidades,
  metadatos ANID, licencias Unpaywall, docs de servidor y tutoriales.
- **HECHO** — Lab local ya existe en este PC: `C:\Users\Niko\dspace-cris-lab`,
  clon oficial `4Science/DSpace` @ `dspace-cris-2025.02.00` (misma versión que
  el servidor UOH y que se documenta como estable), `.env` listo
  (`COMPOSE_PROJECT_NAME=dcris25`), Docker Desktop 28.5.1 + Compose v2.40.2
  operativos.
- **HECHO** — Receta de instalación destilada en `INSTALACION.md` desde la
  bitácora UOH (pasos + trampas reales encontradas allá).
- **RIESGO (frontera)** — El conocimiento técnico del lab UOH es reutilizable;
  los **datos y la configuración UOH no** (metadatos `uoh.*`, cargas
  institucionales, tema, credenciales). Para el cliente: seed propio o vacío.
- **RIESGO (operativo)** — Aprendido en la U: Docker Desktop en Windows cae
  (exit 255 → `wsl -t docker-desktop`) y los contenedores del compose oficial
  no traen restart policy. Para producción del cliente conviene servidor Linux
  + `restart: unless-stopped` o systemd (ver `propuesta-systemd-cris.md` en el
  repo UOH).
- **PENDIENTE** — Definir con el cliente: alcance real (¿solo instalar o
  también cargar datos/tema/capacitar?), servidor destino, dominio+HTTPS,
  plazos y precio. Sin eso el proyecto queda en `pipeline`.
- **PENDIENTE** — Ensayar levantamiento limpio end-to-end para cronometrar y
  documentar la instalación de cero (sirve como evidencia para el presupuesto).

## 2026-11-20 — Conocimiento reusable identificado (mapa)

Del repo UOH, lo que aplica directo a una instalación nueva:

- **Versionado**: `dspace-cris-2025.02.00` = esquema `9.0.2025.02.13`. Las 4
  imágenes son `4science/dspace-cris{,-cli,-solr,-angular}` en Docker Hub.
- **Receta base** (`INSTALACION.md`): compose up → migración automática →
  `create-administrator` → `initialize-entities` (2 XML).
- **Trampa crítica documentada**: sin `correction-relationship-types.xml`
  las cargas con workflow fallan (la primera carga UOH del 9-sep murió por
  eso) — el servicio de correcciones exige las 12 relaciones
  `isCorrectionOfItem`.
- **Operación**: `metadata-import -v -w` para CSV; volúmenes persisten
  (`pgdata`, `assetstore`, solr); admin por `docker-compose-cli.yml`.
- **Producción**: `docs/servidor/` del repo UOH tiene runbook de arranque,
  propuesta systemd, modelo de entornos git y monitoreo/watchdog — portables
  al servidor del cliente.
- **Metadatos**: `metadata-security.cfg` controla qué campos se ven en la
  vista completa de metadatos (mecanismo D8, lección aprendida el 19-nov).

## 2026-11-20 (2) — El encargo se convierte en producto

- **DECISIÓN (usuario)** — El objetivo no es solo cumplir este encargo: es
  un **producto de arranque rápido** alineado a estándares chilenos, para
  que encargos similares futuros tengan metodología de trabajo veloz.
- **HECHO** — `METODOLOGIA.md` escrita: 6 fases con checklist + entregable +
  gate (F0 levantamiento → F1 infra → F2 instalación → F3 config estándar
  CL → F4 datos → F5 verificación/entrega) + tabla de reuso acumulado
  (artefactos transferibles del lab UOH: transform CSV, Unpaywall, systemd,
  watchdog).
- **HECHO** — `ESTANDARES-CL.md` escrito desde la auditoría ANID verificada:
  el estándar chileno = OpenAIRE v4 + DC + OAI-PMH + COAR con 32 metadatos
  (6M/8MA/15R/3O); los 3 endpoints OAI que deben responder; matriz
  ANID→campo DSpace verificada; taxonomías chilenas OCDE/CNED/SIES;
  checklist de verificación por entrega.
- **HECHO** — MOC renombrado conceptualmente a «producto de arranque rápido».
- **HIPÓTESIS** — Si el próximo encargo trae fuente de datos similar
  (xlsx WoS/Scopus), el transform de la UOH se adapta en horas; el cuello
  real será siempre F0 (ver la fuente antes de prometer cumplimiento).
