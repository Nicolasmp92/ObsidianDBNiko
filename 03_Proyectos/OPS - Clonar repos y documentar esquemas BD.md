# OPS — Clonar repos restantes y documentar esquemas BD de las apps

**Tipo:** infraestructura/documentación · **Origen:** sesión KPP 2026-10-09

## Alcance

Solo `kaipetpoint` está clonado en `~/Escritorio/Desarrollo`. Cuando se
clonen los demás repos, cada uno debe recibir su propia regla de esquema
siguiendo el modelo de `.devin/rules/backend-bd-esquema.md` (KPP):

- [ ] **BeanFlow** — clonar a `~/Escritorio/Desarrollo` y crear regla con
      su esquema (hoy corre en H2 en memoria; documentar también el
      aprovisionamiento de su PostgreSQL `beanflow`/`:8085`/`:4205`).
- [ ] **Frunexis** — clonar y documentar esquema (ojo: usa
      `ddl-auto: update`, sin Flyway — la regla debe registrar ese modo).
- [ ] **Sconect** — clonar monorepo (`backend/` + `app/` Flutter) y
      documentar esquema.
- [ ] **StarterCustomeKit** — clonar y documentar esquema.

## Criterio de cierre

Cada repo con regla `.devin/rules/backend-bd-esquema.md` propia que
incluya: tablas/columnas/constraints, invariantes de dominio, historial
de migraciones y el mandato de actualizarla en el mismo commit que toque
el modelo. Ver guía de arranque: [[Proyectos - Setup y arranque]].
