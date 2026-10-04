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
| 2026-10-02 | Entorno Flutter/Android instalado (SDK 3.47.6, AVD, Chrome, toolchain Linux) | `flutter doctor` 6/6 |
| 2026-10-02 | App en web-server :4203 + analyze/test verdes | `flutter test` +1 |
| 2026-10-02 | Login real Flutter↔backend: AuthRepository Bearer, TokenStorage, CORS :4203, HomeScreen | curl 200+CORS+token; analyze/test verdes |
| 2026-10-02 | Feature pacientes: ApiClient core + lista/form/detalle en Flutter | API 201+?buscar; test 3/3; commit 8675d8b |
| 2026-10-02 | Feature agenda: vista de día + form cita + cambio de estado en Flutter | API 201+?desde&hasta; test 4/4; commit cc3b357 |
| 2026-10-03 | Calendario mensual en agenda Flutter (CalendarioMes sin deps, conteoDelMes por rango, layout responsivo lista+calendario) | analyze limpio; test 5/5; commit 6fec587 |
| 2026-10-03 | Evoluciones en app Flutter (historial+form con vínculo a cita) + tap cita→ficha + calendario colapsa al elegir día | API 201+GET; analyze/test 6/6 |
| 2026-10-03 | Análisis de mejoras: roadmap priorizado (solape+reagendar+archivos → n8n → plantillas especialidad) | verificado en código, no ejecutado |
| 2026-10-03 | Solape backend + fix lazy proxy + reagendar + archivos UI (MVP dominio completo) | API 409/200; mvn 7/7; flutter 7/7 |
| 2026-10-03 | Credenciales seed unificadas (rama chore, rol `titular`) | commit en rama |
