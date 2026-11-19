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
| 2026-10-13 | Perfil del clínico: `/api/perfil` + foto + `duracionCitaMin` alimenta agenda; usuarios +6 cols | suites verdes, smoke OK |
| 2026-10-13 | Preferencias: dias laborales, bloqueos y logo separados del perfil; agenda enforcea 400/409 en crear y reagendar | suites verdes, smoke API OK, `bb7ab97` |
| 2026-10-13 | Excepciones de calendario: dias_especiales (bloqueado\|extra) con rangos; extra abre dia no laboral, bloqueado cierra laboral | suites verdes, smoke 201/400/409, `a6bdcd7` |
| 2026-10-13 | Navegacion inferior M3: tabs Agenda/Pacientes/Cuenta, IndexedStack conserva estado, fix heroTag de FABs | analyze+test 7/7, `61586a5` |
| 2026-10-13 | Solicitudes de cita (estado solicitada, webhook), puntos ambar en calendario, banner + confirmar/rechazar 1-toque, pacientes M3; fix check constraint del enum | suites verdes, smoke webhook→solicitada→confirmada, `aa9137b` |
| 2026-10-13 | Atender=Evolucionar (cita queda atendida al crear evolucion), swipe der=atender/izq=reagendar, atendidos al final del listado | suites verdes, smoke evolucion->atendida, `e3eea6f` |
| 2026-10-13 | Agenda por etapas: 3 secciones colapsables (Por confirmar/Agendados/Atendidos), acciones coherentes por estado, toggle calendario en la vista | analyze+test 7/7, `95854c7` |
| 2026-11-05 | Repo clonado en PC casa (HEAD 2086608, sin divergencia); gap toolchain detectado: falta mvn+flutter | git clone + log repo |
| 2026-11-05 | Contrato webhook n8n completado (preferencias + código portal + sobrecupo opt-in) + spec recepcionista | commit `ead323d`, [[SCN - n8n Recepcionista WhatsApp]] |

| 2026-11-05 | Dev local E2E (backend :8083 + web :4203); toolchain Maven/Flutter portable; fix CORS patterns; paciente al vuelo en cita | `mvn test` 7/7 · analyze 0 issues · login local 200 |
| 2026-11-05 | Demo pública en VPS: stack /opt/sconect-demo (pg+jar+nginx) tras Traefik → sslip.io con HTTPS | login demo 200 · api/clinica 200 via HTTPS público |
| 2026-11-16 | Tercer PC dev Windows: sconect clonado + toolchain portable (JDK 17, Maven 3.9.9, Flutter 3.50) | `mvn test` 20/20 · build web OK |
| 2026-11-16 | Diagnóstico bot con WAHA mockeado: "hola"→menú @c.us/@lid, token 401 — código sano | log mock con sendText correcto |
| 2026-11-16 | Fix PUT /api/preferencias (merge tri-estado) + recordatorios 24h + hardening @lid + ojito login | 4 commits pusheados `9c1c506` · tests 20/20 |
| 2026-11-16 | E2E bot WhatsApp en prod: "hola"→menú→agendar→solicitada id=7; confirmar notifica al paciente (lids/pn→sendText 201, mensaje recibido) | logs WAHA/backend + WhatsApp real |
| 2026-11-16 | Fix CORS: PATCH no estaba en allowedMethods → 403 pre-auth en app (causa del "sin permiso"); fix lazy-proxy en cambiarEstado; pull-to-refresh en agenda | PATCH+OPTIONS con Origin→200, `96e0865` `7d30b3f` |
| 2026-11-16 | UX bot: atajos m/s/n, numeración plana, año en fechas; anticipación mínima configurable (120min) | `b73c850` `d6facf1` `86a2b3a` |
| 2026-11-16 | Lock pesimista por profesional (carrera app↔bot) + 409 informativo; AppToast componente único (17 showSnackBar→1 API, overlay superior) + aviso "notificamos a tu paciente" | tests 20/20, `1d78736` `212a25a` |
| 2026-11-19 | `front/SCN - front-widgets.md` — inventario de widgets compartidos + API AppButton (primera spec docs-first) | doc en vault |
| 2026-11-19 | `back/SCN - back-arquitectura.md` — mapa de módulos + API + invariantes (spec docs-first del back) | doc en vault |
