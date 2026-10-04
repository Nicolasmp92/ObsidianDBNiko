---
tipo: registro
proyecto: startercustomekit
---
# Registro de actividades — StarterCustomeKit

Tabla estructurada **append-only**. Una fila por actividad verificable; las filas nuevas van al final. El registro completo por-commit vive en `StarterCustomeKit/registro_actividades.md` (repo).

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-10-02 | Inventario v1 (Laravel) + Frunexis; alcance v2 documentado | nota `SCK - Alcance v2` |
| 2026-10-02 | Reemplazo del contenido por stack Angular+Spring (rama `feat/stack-v2-angular-spring`) | ~300 archivos D/M/??; v1 en git |
| 2026-10-02 | Backend Spring Boot: JWT dual, usuarios, items, health, seed | `mvn test`+`package` OK; smoke curls OK |
| 2026-10-02 | Frontend Angular 22 SSR + Tailwind + proxy `/api` | build/test/lint OK; login→me→logout E2E |
| 2026-10-02 | Fix proxy Express `/api` + `allowedHosts` localhost | curl /api/health → 200 vía proxy |
| 2026-10-02 | Paquete `.devin` copiado + inyector + bitácoras + README | repo |
| 2026-10-02 | Sidebar v1 recreada: 3 estados, overlay móvil <1024px, tooltips CDK, antiflash, sticky | commits `30f6964`/`9c76988`/`5dc5209` |
| 2026-10-02 | Puertos propios 8081/4201/4001 commiteados como defaults | PR #23 mergeado |
| 2026-10-02 | BD PostgreSQL `sck`/`sck_user`; backend migrado de H2 a PG | `psql` conecta, seed persistido |
| 2026-10-02 | Stack v2 promovido a `main` | PR #22 mergeado; tag `v1-laravel` creado |
