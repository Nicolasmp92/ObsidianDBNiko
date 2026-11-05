---
tipo: decision
estado: pendiente
actualizado: 2026-11-05
---

# 🏆 Top — Skills para desarrollo de software

Skills evaluadas para instalar en los proyectos de NAMP/vault. Formato: `SKILL.md` (estándar Agent Skills — sirven para Devin, Claude Code y cualquier agente compatible).

**Dónde instalar:**
| Alcance | Ubicación | Va a git |
|---|---|---|
| Por proyecto | `.devin/skills/<nombre>/` en el repo | Sí (viaja con el código) |
| Global (este PC) | `%APPDATA%\devin\skills\<nombre>\` | No |

---

## Tier 1 — Ya en nuestro store (`skills/`), probadas en UOH

Ordenadas por impacto en tu flujo (bitácoras + multi-PC + varios repos):

| # | Skill | Qué hace | Por qué para ti |
|---|---|---|---|
| 1 | `continuidad-sesion` | Retoma trabajo desde el estado del disco (bitácora, logs), no desde la memoria | Es exactamente el defecto que detectamos con el clon obsoleto de NAMP |
| 2 | `desarrollo-aplicaciones` | Diseña/desarrolla/reestructura apps: primeros principios, OODA, 3 ramas ToT, consejo de 5 | Skill central para NAMP, KPP, Editora |
| 3 | `diagnostico-fallas` | Debugging sistemático: reproducir → minimizar → hipótesis → fix acotado | Evita parches a ciegas en producción |
| 4 | `guarda-edicion-concurrente` | Relee antes de escribir, ediciones puntuales, append en bitácoras | Trabajas desde 2 PCs + agentes — previene pisar cambios |
| 5 | `auditoria-evidencia` | Audita productos de agentes con controles mecánicos y contraste | QA de lo que generan los agentes |
| 6 | `triage-entrada` | Acota encargos vagos con presupuesto antes de ejecutar | Para sesiones grandes en repos desconocidos |
| 7 | `interrogatorio-adopcion` | Evalúa herramientas/dependencias antes de incorporarlas | Encaja con "cero dependencias extra" de NAMP |
| 8 | `exploracion-analisis` | Análisis profundo de decisiones (primeros principios + OODA + consejo) | Para decisiones de arquitectura grandes |

**Recomendación:** instalarlas todas — ya fueron batalla-probadas en el repo UOH y vienen con `references/` incluidos.

---

## Tier 2 — Externas del ecosistema (anthropics/skills, Apache 2.0)

| # | Skill | Qué hace | Recomendación |
|---|---|---|---|
| 9 | `webapp-testing` | Testing E2E de apps web con Playwright (screenshots, logs, acciones) | ⭐ Alta — complementa tus auditorías CDP de namp.cl |
| 10 | `skill-creator` | Guía para crear nuevas skills propias | ⭐ Alta — para empaquetar tus propios flujos (deploy Dokploy, capturas IG) |
| 11 | `frontend-design` | Guías de diseño UI de calidad para interfaces | Media — útil para los posts/webs de NAMP |
| 12 | `mcp-builder` | Crear servidores MCP (integraciones del agente) | Media — solo si quieres conectar Devin a tus servicios |
| 13 | `docx` / `xlsx` / `pptx` / `pdf` | Crear/editar documentos Office y PDF | Baja — solo si generas informes/cotizaciones |

Instalación desde repo: `devin plugins install anthropics/skills` o copiar la carpeta suelta a `.devin/skills/`.

---

## Tier 3 — Built-in de Devin (ya disponibles, no requieren instalar)

- `devin-cli` — docs de Devin CLI · `declarative-repo-setup` — genera `environment.yaml` · `upload-secrets` — sube secretos al gestor de Devin

---

## Mi sugerencia de arranque

1. **Global (todas las sesiones):** `continuidad-sesion`, `guarda-edicion-concurrente`, `diagnostico-fallas`
2. **Por repo (namp-ingenieria, kpp, editora):** `desarrollo-aplicaciones`, `triage-entrada` + `webapp-testing`
3. **Cuando haga falta:** `skill-creator` para empaquetar flujos propios (ej. "generar post IG", "deploy a Dokploy")
