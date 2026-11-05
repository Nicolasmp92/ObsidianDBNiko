---
tipo: log
carpeta: 00_Reglas_y_Estandares
---

# Log — 00_Reglas_y_Estandares

Registro append-only de esta carpeta. Entradas tipificadas: HECHO / DECISIÓN / PENDIENTE. Las nuevas van al final.

## Contenido

- `reglas/` — reglas de orden del vault ([[Convenciones del Vault]])
- `estandares/` — estándares de código, stacks y setups
- `skills/` — store de skills de agente reutilizables (formato `SKILL.md` estándar Agent Skills; para instalar: copiar la carpeta a `.devin/skills/` del repo destino o a `%APPDATA%\devin\skills\` para uso global)

## Entradas

- **DECISIÓN** — Reorden del vault: `02_Reglas_y_Estandares` → `00_` (pasa a ser la primera carpeta, refleja que las reglas mandan sobre el contenido) y `00_Assets` → `98_` (multimedia tiene poco peso, queda antes del archivo histórico) (2026-11-05).
- **HECHO** — Subcarpetas creadas siguiendo la convención: `reglas/`, `estandares/`, `skills/`; los 5 documentos de estándares movidos a `estandares/` y Convenciones a `reglas/` (2026-11-05).
- **HECHO** — Store de skills poblado con las 8 skills del paquete `.devin` de `repositorios-digitales-uoh` (incluye references/ y agents/ de cada una) (2026-11-05).
- **PENDIENTE** — Usuario decide qué skills instalar y dónde (por repo vs global). Candidatas evaluadas en [[Top - Skills para desarrollo]].
- **HECHO** — Instaladas globalmente en `%APPDATA%\devin\skills\` (disponibles en toda sesión de este PC): `continuidad-sesion`, `guarda-edicion-concurrente`, `diagnostico-fallas` (2026-11-05).
- **HECHO** — Agregadas al store desde `anthropics/skills` (Apache 2.0): `webapp-testing` (Playwright E2E) y `skill-creator` (2026-11-05).
- **HECHO** — Verificado paquete `.devin` de repositorios-digitales-uoh: 27/27 blobs coinciden con `MANIFEST.sha256` (verificación contra objetos git; el `sha256sum -c` directo falla por checkout CRLF en Windows, no por corrupción). `inyector-skill.md` ya existía en la raíz del repo UOH, vigente desde 2026-09-22 (2026-11-05).
- **PENDIENTE** — Instalación por repo (`desarrollo-aplicaciones`, `triage-entrada`, `webapp-testing`) queda en espera: `namp-ingenieria`, `kpp` y `editora` no están clonados en este PC. Agregar `webapp-testing` al paquete `.devin` de UOH requiere regenerar su `MANIFEST.sha256` — decisión pendiente del usuario.
- **HECHO** — `webapp-testing` y `skill-creator` incorporadas al paquete `.devin` de repositorios-digitales-uoh: copiadas a `.devin/skills/`, `MANIFEST.sha256` regenerado (52 archivos, hashes LF verificados — los 27 anteriores intactos), `inyector-skill.md` actualizado (tabla de activación con 2 filas nuevas, adaptaciones, verificación, nuevo `paquete_sha256`). Commit `96ba434` en `main` (2026-11-05).
