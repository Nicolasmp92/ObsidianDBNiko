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
