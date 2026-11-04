---
tipo: log
proyecto: taskflow
---
# 📓 Log — TaskFlow

Bitácora narrativa **append-only**: entradas nuevas al final. Tipos: **HECHO** / **DECISIÓN** / **HIPÓTESIS** / **RIESGO**. La bitácora técnica autoritativa vive en el repo.

---

## 2026-10-20 — Génesis desde SCK + dominio tareas

- **HECHO** — Generado desde `StarterCustomeKit`@main (git archive + rebrand con el script adaptado de `rebrand.py`): paquete `nicolasmp92.taskflow`, BD `taskflow`, cookie `taskflow_token`, env `TASKFLOW_*`, puertos 8085/4205/4005. Commit base `33dcd2d`.
- **HECHO** — Dominio `items` reemplazado por `tareas` (`35f203d`): kanban pendiente/en_progreso/hecha con flechas rápidas, prioridad, asignación a usuarios activos, `vence_en`, comentarios por tarea (agregan, no se editan). Dashboard con resumen del equipo. Campana real en topbar.
- **HECHO** — Smoke E2E verde sobre H2: login admin+colaborador, CRUD, comentar, resumen, asignables, **403** al borrar tarea ajena, **401** sin sesión, SSR sirve login 200 y redirige / y /tareas a login sin cookie.
- **HECHO** — Suite verde: `mvn test`, `npm test` 28/28, `ng lint`, `build` SSR.
- **DECISIÓN** — `SesionResponse` ganó `id`: el filtro "mías" no debe comparar nombres. Campo `eliminable` por petición evita exponer correos del creador.
- **RIESGO** — BD PostgreSQL `taskflow`/`taskflow_user` aún no creada (requiere superusuario local): hoy corre en modo H2 (`TASKFLOW_DB_URL=jdbc:h2:mem:…`). Comandos en README del repo.
- **HECHO** — Repo publicado en `github.com/Nicolasmp92/taskflow` (privado), `main` pusheada.

## 2026-10-24 — Demo en vivo + lección H2

- **HECHO** — App levantada para uso real: backend :8085 + `ng serve` :4205, login verificado.
- **RIESGO→LECCIÓN** — Tras suspensión del PC, H2 `jdbc:h2:mem:` sin `DB_CLOSE_DELAY=-1` se vació (Hikari cerró conexiones idle) y login tiró 500. Con el flag del README la BD sobrevive. En modo H2 siempre usar el comando completo; para trabajo real, PostgreSQL.
- **CIERRE** — Sesión terminada con app verificada. Siguiente gate: **[[Ideas|ISO Manager]]** (ya documentado en `Empresa/Ideas.md` — gestión de cumplimiento ISO 9001/14001/45001/27001; la nota original lo agenda post-F3, se adelanta por decisión).
