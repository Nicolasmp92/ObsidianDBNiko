# OPS — Clonar repos restantes y documentar esquemas BD de las apps

**Tipo:** infraestructura/documentación · **Origen:** sesión KPP 2026-10-09

## Alcance

Todos los repos están clonados en `~/Escritorio/Desarrollo` (2026-10-13)
y cada uno tiene su regla de esquema siguiendo el modelo de
`.devin/rules/backend-bd-esquema.md` (KPP):

- [x] **BeanFlow** — clonado; `main` ahora es Angular+Spring (merge
      `ea07d99`, 2026-10-13 — Laravel eliminado). Regla de esquema creada
      (Flyway V1). Foto histórica del esquema Laravel en
      [[Proyectos/BeanFlow/esquema-laravel-historico]].
      **Pendiente**: aprovisionar PostgreSQL `beanflow`/`beanflow_user`
      (requiere clave sudo/postgres del usuario; hoy corre en H2 en
      memoria, `:8085`/`:4205`).
- [x] **Frunexis** — clonado y regla creada (usa `ddl-auto: update`,
      sin Flyway — la regla lo registra).
- [x] **Sconect** — clonado monorepo (`backend/` + `app/` Flutter) y
      regla creada.
- [x] **StarterCustomeKit** — clonado y regla creada.

## Criterio de cierre

Cada repo con regla `.devin/rules/backend-bd-esquema.md` propia que
incluya: tablas/columnas/constraints, invariantes de dominio, historial
de migraciones y el mandato de actualizarla en el mismo commit que toque
el modelo. **Cumplido** salvo el pendiente de PostgreSQL de BeanFlow.
Ver guía de arranque: [[Proyectos - Setup y arranque]].
