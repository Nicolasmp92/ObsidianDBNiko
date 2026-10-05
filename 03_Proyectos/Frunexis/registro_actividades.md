---
tipo: registro
proyecto: frunexis
---
# Registro de actividades — Frunexis

Tabla estructurada **append-only**. Una fila por actividad verificable; las filas nuevas van al final. El registro completo por-commit vive en `Frunexis/registro_actividades.md` (repo).

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-10-02 | Triage: reemplazar Laravel por stack SCK, alcance catálogo + personal (agenda → sconect) | migraciones v1 leídas; decisión del usuario |
| 2026-10-02 | Reemplazo por kit en `feat/stack-v2-sck` + renombrado sck→frunexis + items eliminado | `git archive` + renombrado global |
| 2026-10-02 | Backend: 5 entidades + 5 repos + 5 controllers + seed catálogo | `mvn test` verde |
| 2026-10-02 | Frontend: 5 páginas CRUD + rutas + iconos sidebar | build/lint/test verdes |
| 2026-10-02 | BD `frunexis`/`frunexis_user` + `include-message=always` | smoke: 200/201/409/401 |
| 2026-10-02 | Promovido a main (PR #10, `b969b80`); tag `v1-laravel` | git log remoto |
| 2026-10-02 | Puertos propios 8082/4202/4002 commiteados | PR #11; grep sin restos |
| 2026-10-02 | RBAC granular: roles/permisos/joins + @PreAuthorize + seeder matriz v1 | smoke: 403/200 por permiso, grant sin re-login |
| 2026-10-02 | Estructura v1: hoja de vida 8 tabs, contratos drill-down, temporada vigente única, modal permisos | build/lint/test verdes |
| 2026-10-02 | README documenta RBAC + bitácoras cerradas | PRs #12 (`ebbcd27`) y #13 (`1103032`) |
| 2026-10-03 | Credenciales seed unificadas `nikolasmp92@gmail.com`/`niko9214` (en vivo + defaults) | login 200 vs API |
| 2026-10-04 | Paletas+preferencias+login portados de SCK; fix prerender | `cb65de1`,`96c734c` 9/9 tests |
| 2026-10-04 | Fix sesión SSR portado de KaiPetPoint (cookie SSR + auth) | `9d76aa1` 11/11 tests |
| 2026-10-04 | Fix tooltip DomPortal (parentNode) portado de KaiPetPoint | `4b3105f` + spec |
| 2026-10-04 | Sistema de dialogos modales portado de KaiPetPoint (6 paginas a modal, 6 confirms reemplazados; alerts de error pendientes) | `4a3cd6d` en `feat/paletas-tema` 12/12 |
