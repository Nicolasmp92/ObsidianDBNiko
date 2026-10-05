---
tipo: registro
proyecto: beanflow
---
# Registro de actividades — BeanFlow

Tabla estructurada **append-only**. Una fila por actividad verificable; las filas nuevas van al final. El registro completo por-commit vive en `BeanFlow/registro_actividades.md` (repo).

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2025-10-24 | Reemplazo Laravel→Angular+Spring: v1 eliminada, v2 untracked | `d2be7a5` |
| 2026-10-05 | Fix `etiquetaRol()` en UsuariosPage + modo dev H2 (`db/migration-h2`) | backend :8085 up, login 200 |
| 2026-10-05 | Stack v2 consolidado y pusheado; bitácoras repo+vault creadas | push `refactor/stack-angular-spring` |
| 2026-10-05 | Fix 500 salón/carta/cocina: `@EntityGraph` en 5 repos (lazy + open-in-view=false) | `d590e17`; 10 GET 200 + abrir comanda 201 |
