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
- **HECHO** — Merge `refactor/stack-angular-spring` → `main` (`ea07d99`, 2026-10-13): Laravel eliminado de `main`, el POS Angular+Spring es el stack activo. Verificado: `mvn test` 12/12, `ng build` verde, backend :8085 (H2) con login + comanda 201 en vivo.
- **HECHO** — Foto del esquema nuevo: `.devin/rules/backend-bd-esquema.md` en el repo. Foto del esquema Laravel viejo en [[esquema-laravel-historico]] (solo registro — el proyecto ya no depende de él).
- **HECHO** — PostgreSQL `beanflow`/`beanflow_user` aprovisionado (2026-10-13): Flyway V1 aplicado a PG 17.11, índice parcial `uq_comanda_abierta_por_mesa` enforced en BD (doble comanda → 409). Migración cerrada.
