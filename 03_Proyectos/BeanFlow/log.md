---
tipo: log
proyecto: beanflow
---
# Log — BeanFlow (resumen del vault)

La bitácora técnica autoritativa vive en el repo (`log.md` + `registro_actividades.md`); esta nota resume hitos y decisiones para consulta desde el vault.

- **HECHO** — Reemplazo completo Laravel→Angular+Spring (`d2be7a5`, 2025-10-24): borrado de la v1 commiteado; el stack v2 quedó **untracked ~1 año**.
- **HECHO** — Stack v2 desarrollado sin commits: POS restaurante completo (salón/mesas, comandas, cocina, carta+recetas, bodega, cuenta, usuarios con roles garzon/cocina/caja/admin), auth JWT+cookie, diálogos modales y toasts ya portados del kit.
- **HECHO** — Consolidación en git (2026-10-05): todo el working tree commiteado y pusheado a `origin/refactor/stack-angular-spring`. Fix `etiquetaRol()` incluido (la app no compilaba — el método se referenciaba en la plantilla pero no existía).
- **RIESGO** — PostgreSQL `beanflow`/`beanflow_user` nunca se aprovisionó: backend corre en H2 en memoria (`db/migration-h2` sin el índice parcial `uq_comanda_abierta_por_mesa`). Datos volátiles; pendiente `createdb`/`createuser` con clave postgres del usuario.
- **PENDIENTE** — Merge de `refactor/stack-angular-spring` a `main` vía PR.
