---
tipo: log
proyecto: beanflow
---
# Log — BeanFlow (resumen del vault)

La bitácora técnica autoritativa vive en el repo (`log.md` + `registro_actividades.md`); esta nota resume hitos y decisiones para consulta desde el vault.

- **HECHO** — Reemplazo completo Laravel→Angular+Spring (`d2be7a5`, 2025-10-24): borrado de la v1 commiteado; el stack v2 quedó **untracked ~1 año**.
- **HECHO** — Stack v2 desarrollado sin commits: POS restaurante completo (salón/mesas, comandas, cocina, carta+recetas, bodega, cuenta, usuarios con roles garzon/cocina/caja/admin), auth JWT+cookie, diálogos modales y toasts ya portados del kit.
- **HECHO** — Consolidación en git (2026-10-05): todo el working tree commiteado y pusheado a `origin/refactor/stack-angular-spring`. Fix `etiquetaRol()` incluido (la app no compilaba — el método se referenciaba en la plantilla pero no existía).
- **RIESGO** — PostgreSQL `beanflow`/`beanflow_user` nunca se aprovisionó: backend corre en H2 en memoria (`db/migration-h2` sin índice parcial `uq_comanda_abierta_por_mesa`). Datos volátiles; pendiente `createdb`/`createuser` con clave postgres del usuario.
- **VERIFICADO** — Smoke e2e en vivo con H2 (2026-10-06, `ebe2520`): flujo completo comanda→cocina→descuento exacto de insumos→cobro→mesa liberada; auth por rol correcta (cocina: 403 en comandas/admin, 200 en cola); doble comanda → 409; proxy :4205→:8085 OK. Único bloqueo real: credencial superusuario PostgreSQL para `beanflow`/`beanflow_user`.
- **AUDITADO** — Auditoría de mejora post-smoke (2026-10-06, `88487f9`): 6 brechas verificadas en código — `entregado` inalcanzable para garzón (endpoint bajo `/api/cocina/**`), nota de ítem cableada sin UI, cocina sin auto-refresh, "para llevar" huérfano del salón, líneas duplicadas 1× por click, guard sin autorización por rol. Roadmap de ramas registrado en `log.md` del repo; orden sugerido: brechas 1–3 (impacto día uno) → fixes 5–6 → `feat/historial-ventas` + `feat/cierre-caja`.
- **HECHO** — Merge `refactor/stack-angular-spring` → `main` (`ea07d99`, 2026-10-13): Laravel eliminado de `main`, el POS Angular+Spring es el stack activo. Verificado: `mvn test` 12/12, `ng build` verde, backend :8085 (H2) con login + comanda 201 en vivo.
- **HECHO** — Foto del esquema nuevo: `.devin/rules/backend-bd-esquema.md` en el repo. Foto del esquema Laravel viejo en [[esquema-laravel-historico]] (solo registro — el proyecto ya no depende de él).
- **HECHO** — PostgreSQL `beanflow`/`beanflow_user` aprovisionado (2026-10-13): Flyway V1 aplicado a PG 17.11, índice parcial `uq_comanda_abierta_por_mesa` enforced en BD (doble comanda → 409). Migración cerrada.
- **FIX** — Sesión SSR rota por `RenderMode.Prerender` en `app.routes.server.ts` (2026-10-14): el redirect a `/login` quedaba horneado en el build — F5 o acceso directo con sesión válida devolvía 302. Es la mitad faltante del fix de KaiPetPoint (`b5cdfbe`); los interceptores ya estaban portados. `login` queda prerenderizada, el resto `RenderMode.Server`. Rama `fix/ssr-render-por-peticion` pusheada, pendiente merge. Misma corrección aplicada en SCK (`feat/login-recordar`, `163e972`).
- **HECHO** — Capturas autenticadas del stack para portafolio (2026-10-14): 22 screenshots reales de BeanFlow/KaiPetPoint/SCK/Frunexis vía puppeteer-core (`.shots/capture.js` en Desarrollo/). Portafolio poblado con los 4 proyectos (`Nicolasmp92.github.io`, `9f9378d`).
