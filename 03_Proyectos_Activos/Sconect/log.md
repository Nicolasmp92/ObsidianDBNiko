---
tipo: log
proyecto: sconect
---
# 📓 Log — Sconect

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

La bitácora técnica autoritativa vive en el repo (`log.md` + `registro_actividades.md`); esta nota resume hitos y decisiones para consulta desde el vault.

---

## 2026-10-02 — Nacimiento del proyecto v2

- **HECHO** — Análisis de los repos previos: `SConect-Laravel` era scaffold vacío (2 reinicios previos en su historial); `sconect-app` aportó skeleton Flutter BLoC + paleta esmeralda + assets de marca. El dominio real venía del PRD en el vault.
- **DECISIÓN** — Stack: Spring Boot (backend del kit, con el RBAC de Frunexis) + Flutter BLoC. El Go del PRD queda superado.
- **DECISIÓN** — Modelo de cuenta: **titular + administrativo** (delegación de permisos sin compartir claves, como pide el PRD). Multi-profesional fuera del MVP.
- **DECISIÓN** — Evoluciones **inmutables**; paciente con historial → soft-delete; cita con evoluciones → 409, se cancela.
- **DECISIÓN** — El `administrativo` **no ve evoluciones** por defecto: privacidad clínica delegable explícitamente por el titular.
- **DECISIÓN** — WhatsApp/n8n en el MVP como **endpoint webhook** (no solo seam): `POST /api/webhooks/citas` (busca/crea paciente por teléfono) + `GET /api/webhooks/agenda` (horas ocupadas), auth por `X-Api-Key`.
- **HECHO** — Monorepo creado y verificado end-to-end: 9 tablas en PostgreSQL `sconect`, login titular (26 permisos), administrativo 403 en evoluciones, webhook crea paciente+cita `origen:whatsapp`, `mvn test`+`package` verdes. Commit inicial `41e14a9`.

## Pendientes

- Conectar app Flutter al backend (datasource HTTP, secure storage, pantallas de dominio).
- Montar flujo n8n/WhatsApp real sobre el contrato ya servido.
- AuditLog + reportes (fase 2 del PRD).
- Token de GitHub expuesto en chat: revocación manual pendiente (tarea global del usuario).

## 2026-10-02 — Entorno de desarrollo Flutter operativo

- **HECHO** — Toolchain completo instalado y verificado: Flutter 3.47.6 (`~/flutter`), Android SDK 36 (`~/Android/Sdk`), AVD `sconect_dev`, Chrome 154, toolchain escritorio Linux. `flutter doctor` 6/6 verde; KVM activo para emulador acelerado.
- **HECHO** — App corriendo en `web-server` puerto **4203** (mapa de puertos); `flutter analyze` limpio y `flutter test` verde (smoke splash→login reemplazó la plantilla del contador).
- **PENDIENTE** — Conectar login real al backend :8083 (Bearer para móvil; verificar CORS para web).

## 2026-10-02 — Login real conectado (Flutter ↔ backend)

- **HECHO** — AuthRepository (http + Bearer) reemplaza el mock; splash restaura sesión vía `GET /api/auth/me`; HomeScreen placeholder con logout. CORS habilitado solo para `localhost:4203` (sin credenciales).
- **HECHO** — TokenStorage: secure storage en nativo, SharedPreferences en web/fallback. Verificado con curl cross-origin: 200 + token Bearer (26 permisos titular). `flutter analyze`/`test` verdes.
- **PENDIENTE** — Pantallas de dominio (agenda/pacientes/evoluciones/archivos). Modo offline (restaurar con backend caído → login): fase 2.

## 2026-10-02 — Feature pacientes (primer dominio en la app)

- **HECHO** — `ApiClient` en `core/` (Bearer automático + errores con message del backend). Feature `pacientes/`: modelo, repository, bloc, lista con búsqueda debounce, formulario crear/editar (10 campos), detalle con eliminar (soft-delete lo decide el backend). Home → Pacientes navegable.
- **VERIFICADO** — API viva: POST 201, `?buscar=` OK; `flutter analyze` limpio, `flutter test` 3/3. Commit `8675d8b` en GitHub.
- **PENDIENTE** — Agenda/citas, evoluciones y archivos en la app (placeholders honestos en detalle).

## 2026-10-02 — Feature agenda (vista de día)

- **HECHO** — Agenda por día: flechas ‹ › + date picker, citas por hora con chip de estado, menú por cita (confirmar/atendida/no asistió/cancelar/eliminar), FAB nueva cita con selector de paciente + duración. `ApiClient.patch` agregado.
- **VERIFICADO** — POST cita 201 (`agendada`/`manual`), `?desde&hasta` del día OK; analyze limpio, test 4/4. Commit `cc3b357` en GitHub.
- **DECISIÓN** — Vista de día en vez de calendario mensual (adecuada al profesional particular); semanal/mensual queda para después si hace falta.
- **PENDIENTE** — Evoluciones y archivos por paciente; calendario semanal/mensual; recordatorios.

## 2026-10-03 — Calendario mensual en agenda

- **HECHO** — `CalendarioMes` (grid manual, sin dependencias): puntos en días con citas, día seleccionado destacado, hoy con tinte, ‹ › navega meses (carga día 1), tap en día → recarga la lista. `AgendaLoaded` lleva `citasDelMes` (conteo por día, canceladas no cuentan) vía `?desde&hasta` del mes visible.
- **DECISIÓN** — El calendario es navegación, no reemplaza la vista de día: ≥900px lista izquierda + calendario derecha (~320px); angosto → colapsable con botón. Sin `table_calendar` ni paquetes (~150 líneas propias, tema esmeralda intacto).
- **FIX** — `await bloc.close()` dentro de `testWidgets` cuelga la suite (fake-async); en widget tests no se cierra el bloc a mano.
- **VERIFICADO** — `flutter analyze` limpio, `flutter test` 5/5. App servida en :4203.
- **PENDIENTE** — Evoluciones y archivos por paciente; recordatorios; flujo n8n real.

## 2026-10-03 — Evoluciones clínicas en la app

- **HECHO** — Feature `evoluciones/` en Flutter: modelo + repo (solo crear/listar, inmutable) + pantalla de historial + formulario con vínculo opcional a cita. Ficha de paciente gana historial y botón "Evolucionar"; menú de cita gana "Evolucionar paciente" (vincula la nota a la atención); tap en cita abre la ficha del paciente.
- **DECISIÓN** — En pantalla angosta, elegir día en el calendario lo colapsa solo para mostrar el listado del día (feedback del usuario sobre el flujo móvil).
- **VERIFICADO** — POST evolución 201 + GET lista (API viva); `flutter analyze` limpio; `flutter test` 6/6.
- **PENDIENTE** — Archivos clínicos (multipart); recordatorios; flujo n8n real.

## 2026-10-03 — Análisis de mejoras (roadmap priorizado)

- **ANÁLISIS** — Verificado en código: solape de citas sin validación, reagendar sin UI (PUT ya existe), archivos servidos sin UI, `especialidad` dormida. Prioridad: 1) solape+reagendar+archivos cierra MVP, 2) n8n mínimo viable, 3) plantillas por especialidad + recordatorios.
- **NO adoptado** — multi-tenant, vista semanal, push nativas, audit/reportes (fase 2), stores.

## 2026-10-03 — Solape + reagendar + archivos (cierra MVP del dominio)

- **HECHO** — Solape de citas validado en crear/PUT/webhook (409, canceladas no bloquean, adyacentes sí). Bug latente encontrado y corregido: proxies lazy → 500 en PUT/PATCH al serializar. Reagendar en app (form modo edición + menú). Feature archivos completo (file_picker/file_saver, subir/listar/descargar/eliminar).
- **VERIFICADO** — API viva: solape 409, reagendar 200, PATCH 200, webhook 409; `mvn test` 7/7; `flutter test` 7/7, analyze limpio.
- **PENDIENTE** — n8n real; recordatorios; plantillas por especialidad; modo offline; fase 2 (audit/reportes).
