---
tipo: registro
proyecto: sconect
---
# Registro de actividades — Sconect

Tabla estructurada **append-only**. Una fila por actividad verificable; las filas nuevas van al final. El registro completo por-commit vive en `sconect/registro_actividades.md` (repo).

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-10-02 | Análisis repos previos + PRD del vault (dominio real) | git logs, pubspec, PRD |
| 2026-10-02 | Decisiones scope: titular+administrativo, monorepo, archivos+webhook en MVP | respuestas usuario |
| 2026-10-02 | Monorepo `sconect/` creado (backend desde Frunexis + app Flutter + .devin) | commit `41e14a9` |
| 2026-10-02 | Dominio clínica + RBAC (26 permisos) + webhooks n8n + `especialidad` | `mvn test`/`package` OK |
| 2026-10-02 | Smoke PostgreSQL: RBAC 403 evoluciones, webhook 201/401, reglas 409/soft-delete | curls verificados |
