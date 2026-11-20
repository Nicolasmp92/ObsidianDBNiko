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

## 2026-10-13 — Perfil del clínico + "rendimiento" (duración por cita)

- **HECHO** — Módulo `/api/perfil`: el clínico configura nombre, título, especialidad, teléfono, dirección de consulta, bio, foto (multipart ≤5 MB) y `duracionCitaMin` (15–120). La duración alimenta el default del formulario de citas — la agenda respeta el ritmo de cada profesional.
- **BASE FUTURA** — `titulo`/`bio`/`direccion`/`foto` son los datos públicos del clínico para la app de pacientes (valoración, "cerca de mí").
- **VERIFICADO** — `mvn test` 7/7, `flutter test` 7/7, analyze limpio; smoke curl en vivo OK (PUT 200, duración 300 → 400, foto sin auth → 401).
- **PENDIENTE** — siguiente de la cola: webhook n8n mínimo viable (ya servido en `/api/webhooks/citas`); luego recordatorios y plantillas por especialidad.

## 2026-10-13 — Preferencias del clínico (separación de perfil)

- **HECHO** — Perfil = quién eres; preferencias = cómo trabajas. Nueva
  feature `preferencias`: duración habitual de cita (movida del perfil),
  días laborales con chips L-D, logo de la consulta (multipart ≤5 MB) y
  tabla `dias_bloqueados` (fecha + motivo, UQ por usuario).
- **ENFORCEMENT REAL** — La agenda rechaza en backend al crear y
  reagendar: día no laboral → 400, día bloqueado → 409 (sumado al solape
  409). No es configuración decorativa; ningún cliente/integración puede
  crear citas inválidas.
- **FIX DE DISEÑO** — PUT con los 7 días o null → "todos los días";
  antes un null era ignorado y la preferencia era irreversible.
- **VERIFICADO** — `mvn test` 7/7, `flutter test` 7/7, analyze limpio.
  Smoke en vivo: PUT 200, sin auth 401, cita domingo no laboral → 400,
  día bloqueado → 409, día libre → 201, POST/GET logo 200. `main`
  (`b709c86` → `bb7ab97`), pusheado.
- **PENDIENTE** — UI de agenda que atenúe días no laborales/bloqueados;
  horarios de apertura/cierre por día (hoy son días enteros); usar el
  logo en comprobantes. Cola intacta: n8n → recordatorios → plantillas.

## 2026-10-13 — Lluvia de ideas (pulido según modelo de negocio)

Sesión de ideación sobre qué pulir. Ordenado por retorno:

**Día a día del clínico**
- Vista "hoy" como home: próximas atenciones y próximo paciente al abrir.
- Acciones rápidas en cita: confirmar / atendida / no_asistió + deep
  links `tel:`/`wa.me` al paciente desde la ficha.
- Registrar inasistencias → métrica de no-shows por paciente (cobra por
  adelantado al reincidente).
- Horarios de apertura/cierre por día (preferencias por bloque horario,
  no solo día entero).

**Ya servido, falta conectar**
- n8n + WhatsApp sobre el webhook existente: recepcionista automático
  (consulta agenda → ofrece horas → agenda → confirma).
- Recordatorios 24h antes (campo `recordadoEn` ya existe en `citas`).
- Plantillas de evolución por `usuarios.especialidad` (campo dormido).

**Semilla de la app de pacientes**
- Valoración post-atención (tabla `valoraciones`) → marketplace futuro.
- Endpoint público del clínico (titulo/bio/direccion/foto/logo ya están).
- Sobreturnos / lista de espera: ofrecer hora liberada por cancelación.

**SaaS multi-empresa**
- Multi-profesional (consulta con N clínicos compartiendo pacientes) —
  hoy single-clinician por decisión, es el paso a arrendar a clínicas.
- Reportes (permiso `reportes.view` existe sin endpoints): ocupación,
  ingresos esperados, pacientes nuevos/mes.
- AuditLog del PRD (obligación real con datos clínicos).

**Prioridad sugerida**: 1) vista "hoy" + acciones rápidas, 2) horarios
apertura/cierre + calendario que atenúa días bloqueados, 3) n8n mínimo,
4) recordatorios.

## 2026-10-13 — Solicitudes de cita pendientes + navegación M3

- **HECHO** — Estado `solicitada` en citas: el webhook crea solicitudes
  pendientes; el clínico las confirma/rechaza con un toque en la agenda
  (tarjetas ámbar + banner). Calendario marca días con solicitudes con
  punto ámbar. Las solicitudes bloquean el horario hasta resolverlas.
- **HECHO** — Shell M3: barra inferior Agenda/Pacientes/Cuenta,
  IndexedStack conserva estado; pacientes rediseñado (SearchBar,
  iniciales, contador).
- **LECCIÓN** — `ddl-auto` no actualiza CHECK constraints de enums al
  agregar valores: hubo que hacer `DROP CONSTRAINT` manual. Otra razón
  para migrar a Flyway antes de producción.
- **VERIFICADO** — suites verdes ambos lados; webhook → solicitada →
  confirmada en vivo. `main` `aa9137b`.

## 2026-10-13 — Cupo diario de pacientes

- Preferencias + "Pacientes por día" (`usuarios.max_pacientes_dia`,
  null = sin límite, validado 1–100). Va de la mano con la duración
  habitual: rendimiento = cuántos por hora + cuántos por día.
- Enforcement en crear/reagendar (409 día lleno, la propia cita no se
  cuenta al moverla en el mismo día) **y en el webhook** — el bot de
  WhatsApp recibe "agenda completa" para ofrecer otra fecha.
- El webhook ahora también respeta días laborales/bloqueos/extras
  (hueco: antes solo chequeaba solape).
- Bug preexistente arreglado de paso: reagendar por API daba 500 por
  proxy lazy del profesional — `@Transactional` en `actualizar`.
- Commits: `b328f4b` → merge `3846ac4` en `main`. Smoke en vivo OK,
  datos de prueba limpiados. mvn 7/7 · flutter 7/7 · analyze limpio.

## 2026-10-13 — Sobrecupo

- `citas.sobrecupo`: el clínico fuerza una hora sobre el cupo diario o
  en horario solapado (switch "Sobrecupo" en el formulario de cita).
  Solo decisión manual — el webhook de WhatsApp nunca crea sobrecupos.
  Sigue exigiendo día laboral/no bloqueado (para día extra, preferencias).
- La tarjeta de agenda marca "· Sobrecupo" en el subtítulo.
- Aprendizaje: `ddl-auto` no puede agregar `NOT NULL` sin default en
  tabla con filas — la columna se agregó manual. Refuerza el pendiente
  Flyway.
- Commits: `16c5ea4` → merge `78cfc77` en `main`. Smoke OK (cupo 409 →
  sobrecupo 201; bloqueado sigue 409). mvn 7/7 · flutter 7/7.

## 2026-10-13 — Contador de cupos restantes

- Sección "Por confirmar" muestra "Quedan N de M cupos" (rojo: "Cupo
  completo") según `max_pacientes_dia` — misma regla que el backend
  (no canceladas cuentan, sobrecupos incluidos). Solo front, sin cambio
  de API. Prefs se recargan con cada carga del día.
- Commit `95dac2b` → merge `718d8a6` en `main`.

## 2026-10-13 — Nota n8n: solicitud de sobrecupo por WhatsApp

- Pendiente para el flujo n8n: cuando el día esté lleno (409 cupo), el
  bot podrá ofrecer al paciente **solicitar sobrecupo** — solo si el
  clínico lo habilita en preferencias (flag opt-in por implementar).
- Queda como `solicitada` + sobrecupo: el clínico confirma/rechaza
  desde la agenda. El bot nunca crea el sobrecupo por sí solo.

## 2026-10-13 — Portal del paciente (app del paciente en la misma app)

- Entrada "Soy paciente" desde el login clínico → teléfono + código
  de 6 dígitos (10 min, un solo uso). JWT propio
  (`sub=paciente:<id>`) que no sirve para la API clínica; el token
  vive en clave separada y convive con la sesión del profesional.
- El paciente ve el catálogo de clínicos, solicita hora (queda
  `solicitada`, origen `app`, mismas reglas de agenda), anula sus
  citas no resueltas, y lee sus evoluciones y exámenes.
- Nunca revela si un teléfono existe (respuesta genérica); en dev el
  código viaja en la respuesta (`sconect.portal.dev-code`), en
  producción lo mandará n8n por WhatsApp.
- Smoke 12 casos OK; fix preventivo @Transactional en lecturas lazy.
- Commit 4584034 en main. Pendiente: envío real del código por
  WhatsApp (n8n) + rate-limit del acceso.

## 2026-11-05 — Retomada en PC casa (segundo postulante a ingresos)

- **HECHO** — Repo clonado en `Desktop/Desarrollo/sconect`; HEAD `2086608` coincide con la bitácora (sin divergencia, el vault estaba al día).
- **RIESGO** — Toolchain incompleto en este PC: Java 17 OK pero `mvn` y `flutter` no instalados (viven en el PC pega) → instalar antes de tocar backend/app o trabajar en diseño/spec mientras.
- **PENDIENTE** — Cola priorizada vigente: (1) n8n + WhatsApp real — envío del código del portal por WhatsApp + rate-limit del acceso + flag opt-in sobrecupo para el bot; (2) recordatorios 24h (`recordadoEn` ya existe); (3) UI agenda: atenuar días no laborales/bloqueados + horarios apertura/cierre por día; (4) Flyway antes de producción; (5) ventana mínima de anulación en portal; logo en comprobantes. Fase 2: audit/reportes, multi-profesional, offline.

## 2026-11-05 — Contrato n8n completado + spec del recepcionista

- **HECHO** — Backend: `GET /webhooks/preferencias`, `POST /webhooks/portal/codigo` (idempotente), `solicitudSobrecupo` + flag `sobrecupoBot`. `mvn test` 7/7 + smoke 11 casos. Commit `ead323d` en `sconect/main`.
- **HECHO** — Spec del recepcionista: [[SCN - n8n Recepcionista WhatsApp]] — flujo conversacional, matriz de providers (Meta Cloud API / Evolution API / WAHA), plan de despliegue.
- **PENDIENTE** — Decisión del usuario: provider de WhatsApp. Prerrequisito descubierto: sconect aún no tiene deploy en VPS (el backend corre local) — el bot en producción lo exige.

## 2026-11-05 — Demo pública en el VPS + dev local completo

- **HECHO** — Dev local end-to-end en este PC: backend `:8083` (H2) + app web `:4203`. Toolchain completado: Maven 3.9.9 + Flutter 3.47.9/Dart 3.13.7 portables en `~/tools` (Dart viejo 3.9.2 no cumplía `^3.11.4`).
- **BUG+FIX** — CORS bloqueaba el front fuera de `localhost:4203` (preview/proxy `127.0.0.1` → "no se pudo conectar"). `SecurityConfig` ahora usa `allowedOriginPatterns` → comodín `http://localhost:*,http://127.0.0.1:*` en dev. Otra lección: `flutter.bat` solo corre vía `cmd /c` desde Git Bash.
- **HECHO** — Alta de paciente al vuelo desde Nueva cita (`PacienteFormScreen` devuelve el `Paciente` guardado y queda preseleccionado). `flutter analyze` 0 issues.
- **HECHO** — **Demo pública desplegada** en el VPS (`/opt/sconect-demo`, patrón kpp-demo): postgres 16 + backend jar + nginx sirviendo el build web de Flutter con proxy `/api` → backend (mismo origen). Traefik + Let's Encrypt. URL temporal: `https://sconect.200.141.25.56.sslip.io` — login demo `demo@sconect.cl`. `ApiConfig` usa mismo origen en puerto 80/443. Commits `666e98d`+`0d39950` en `sconect/main`.
- **PENDIENTE** — DNS `sconect.namp.cl` → `200.141.25.56` en NIC Chile (usuario); luego monitor Kuma. El registro A falta — Traefik ya tiene la regla, funcionará solo al propagarse.

## 2026-11-05 (cierre) — Punto de retomada

- **Dónde quedó**: demo pública viva en `https://sconect.200.141.25.56.sslip.io` (login `demo@sconect.cl`). Dev local operativo: backend `:8083` (H2 mem) + web `:4203`. Todo commiteado y pusheado (`sconect/main` = `0d39950`, vault incluido).
- **Siguiente paso concreto**: usuario crea A record `sconect.namp.cl` → `200.141.25.56` en NIC Chile; luego agregar monitor Kuma.
- **Abiertos**: provider WhatsApp (decisión), workflow n8n, recordatorios 24h, UI agenda días/horarios, Flyway pre-prod, bug `PUT /api/preferencias` (documentado), ventana anulación portal, logo comprobantes.
- **Notas de entorno (este PC)**: Maven 3.9.9 + Flutter 3.47.9 en `~/tools` (portables); `flutter.bat` solo vía `cmd /c` en Git Bash; H2 es en memoria → cada restart del backend borra datos locales.
- **Secretos**: `.env` del demo vive solo en el VPS (`/opt/sconect-demo/.env`, chmod 600) — no está en ningún repo.

## 2026-11-06 — Dominio real + acceso Kuma

- **HECHO** — `sconect.namp.cl` → `200.141.25.56` creado en **Cloudflare** (no en NIC Chile — la zona DNS del dominio vive ahí: `andy/cheryl.ns.cloudflare.com`; NIC solo tiene el registro). Proxy "DNS only" (nube gris) obligatorio para que Traefik emita Let's Encrypt. Propagación instantánea; cert válido + login demo verificado end-to-end. `sconect.200.141.25.56.sslip.io` sigue funcionando (SAN en el mismo cert).
- **HECHO** — Clave de Uptime Kuma reseteada por CLI: los scripts documentados vivían en otra cuenta; Kuma usa `@louislam/sqlite3` → update directo de hash bcrypt en la DB (`changes=1`). Usuario `nikolasmp92@gmail.com`, nueva clave entregada en conversación.
- **PENDIENTE** — Agregar monitor de `sconect.namp.cl` en Kuma (manual o vía Socket.IO).

## 2026-11-06 — Ronda de feedback de testers (demo) — ejecutada y redesplegada

Testers amigos probaron `https://sconect.namp.cl`. Bitácora ítem por ítem:

1. **Retorno entre vistas** — HECHO: las 21 `MaterialPageRoute` llevan `RouteSettings(name)` → el navegador sincroniza URL/historial (atrás/adelante reales en web). Las AppBar ya tenían flecha de vuelta.
2. **Instalar la app** — HECHO: Sconect es PWA. `manifest.json` con branding (nombre "Sconect", theme `#004D40`), `index.html` con hook `beforeinstallprompt` → `window.sconectInstalar()`; login muestra "Instalar la app en mi dispositivo" — prompt nativo en Chrome/Edge/Android, instrucciones en Safari/iOS (helper Dart `core/pwa/` con import condicional).
3. **Teléfono sin validación** — HECHO: solo dígitos y `+`, máx 15, mín 8 si se rellena ("Max" interpretado como máximo de dígitos). Formatter + validator.
4. **RUT sin validación** — HECHO: dígito verificador módulo 11 (`12.345.678-9` o `12345678-9`); validador independiente del de teléfono.
5. **Fecha de nacimiento** — HECHO: `TextFormField` readOnly que abre picker (ya no es un ListTile disfrazado), muestra `DD/MM/AAAA`, opcional y con botón para limpiar; el modelo sigue guardando ISO en backend.
6. **Bloqueo de agenda en calendario** — HECHO: `AgendaBloc` cachea `Preferencias`; el calendario atenúa y tacha días no laborales (gris) y bloqueados (tinte rojo + snackbar con motivo al tocar); `CitaFormScreen` usa `selectableDayPredicate` → esos días no se pueden elegir en el picker. Backend sigue validando como fuente de verdad.
7. **Preview de rendimiento + horas/día** — HECHO: backend `Usuario.horasTrabajoDia` (1–16, null=8) en `GET/PUT /api/preferencias`; form "Jornada diaria" + tarjeta preview en vivo "≈ N pacientes/día: horas × (60/duración)", acotado por el cupo si existe.
8. **Subida de archivos con error** — HECHO (causa real): Spring Boot limita multipart a **1 MB** por defecto; nginx ya permitía 25m pero `application.yml` no configuraba `spring.servlet.multipart` → `MaxUploadSizeExceededException` en cualquier archivo real. Fijado a 20MB/25MB. Verificado en la demo: subir PDF 2MB → 201, listar → OK, descargar → 2MB íntegro, borrar → 204.
9. **Redundancia en evoluciones** — HECHO: ficha tenía tarjeta "Evoluciones" + botón suelto "Evolucionar"; queda solo la tarjeta (el historial ya tiene FAB "Nueva evolución").
10. **Reagendar permite cambiar paciente** — HECHO: en modo edición el selector se reemplaza por un campo deshabilitado con el nombre del paciente (cambiarlo no es reagendar, es transferir la hora).
11. **Evoluciones sin editar/eliminar** — **FLAG, decisión del usuario pendiente**: hoy son inmutables por diseño clínico (el formulario ya lo advierte). Opciones: (a) mantener inmutables + corregir/agregar nueva evolución; (b) edición solo del autor con ventana (p.ej. 24h) y registro de modificación; (c) eliminar solo titular con soft-delete. No implementado a propósito — es una decisión médico-legal del producto, no un bug.

**Verificación**: `flutter analyze` 0 issues, `mvn test` 7/7, build web + jar, redeploy VPS (`up -d --build`, healthy), smoke en producción: front 200, login OK, preferencias con `horasTrabajoDia` persistido, upload/descarga/eliminación OK. Commit `2096780` en `sconect/main`.

**Pendiente tras la ronda**: decisión ítem 11; monitor Kuma; bug conocido `PUT /api/preferencias` (campos ausentes borran — confirmado de nuevo hoy al hacer PUT solo con `horasTrabajoDia`: dejó `diasLaborales` vacío; restaurado manualmente; front siempre envía todo así que no afecta al usuario).

## 2026-11-06 (segunda parte) — Ítem 11 resuelto: evoluciones editar/eliminar

- **DECISIÓN (usuario)** — Política "Editar 24h + historial": el autor corrige su evolución dentro de 24 h de creada (queda `modificadoEn`/`modificadoPor` y la UI marca "editada"); eliminar es **soft-delete** (`eliminada`/`eliminadaEn`/`eliminadaPor`) — el registro clínico se conserva para auditoría, nunca se borra físicamente. Pasada la ventana, las evoluciones son inmutables y el backend sugiere crear una nota aclaratoria (409).
- **HECHO** — `PUT/DELETE /api/clinica/evoluciones/{id}` (regla autor + ventana), `puedeEditar` calculado en backend por solicitante, acciones en la UI solo cuando aplica, listados clínica+portal excluyen eliminadas, `@Transactional` en mutaciones (autor lazy + `open-in-view:false` → el primer deploy dio 500 "no session", corregido).
- **INCIDENTE MENOR** — `ddl-auto` creó `eliminada_en/_por` y `modificado_*` pero NO la columna booleana `eliminada` en Postgres → `ALTER TABLE ... ADD COLUMN eliminada boolean NOT NULL DEFAULT false` manual en la DB del demo. Refuerza el pendiente de Flyway antes de producción real.
- **Verificado en producción**: crear → PUT edita (registra `modificadoEn`) → DELETE 204 → desaparece del listado, `eliminada=true` en DB. Commit `dee71f1` en `sconect/main`.
- **CIERRE DE RONDA**: los 11 ítems de testers quedaron resueltos y redesplegados en `https://sconect.namp.cl`. Pendientes originales vigentes: monitor Kuma, bug `PUT /api/preferencias` (semántica PATCH), n8n/WhatsApp, recordatorios 24h, Flyway.

## 2026-11-06 (cierre de ronda) — Punto de retomada hacia WhatsApp

- **Dónde quedó**: los 11 ítems de feedback de testers resueltos, verificados y desplegados en `https://sconect.namp.cl`. Todo pusheado: `sconect/main` = `dee71f1`, vault = `6f8fe74`.
- **Siguiente paso concreto**: integración WhatsApp — cabeza de cola original (provider aún sin decidir: spec en [[SCN - n8n Recepcionista WhatsApp]]; recomendación piloto = Evolution API en Dokploy). El backend ya expone el contrato completo: `GET /webhooks/preferencias`, `POST /webhooks/portal/codigo` (idempotente), `solicitudSobrecupo` + flag `sobrecupoBot`.
- **ADVERTENCIA del usuario**: encontró **errores importantes** al usar la app — se dejan registrados como cola de bugs para después de la integración WhatsApp (pendiente que el usuario los pase en detalle).
- **Nota deploy**: para redesplegar: `mvn -q -DskipTests package` → `scp jar` → `tar` de `app/build/web` → `docker compose -f docker-compose.demo.yml up -d --build` en `/opt/sconect-demo`. Columna `eliminada` requirió ALTER manual (ddl-auto la omitió).

## 2026-11-06 (tercera parte) — Recepcionista WhatsApp: backend + WAHA, sin n8n

- **DECISIÓN (usuario)** — Replanteo de n8n: el recepcionista es una máquina de ~6 estados, no necesita orquestador. Arquitectura elegida: lógica del bot **dentro del backend** (testeable, versionada) + **WAHA** como transporte (contenedor, gratis Apache-2.0, pairing sin re-escanear QR). n8n queda fuera del camino crítico (posible glue no crítico a futuro). Meta Cloud API pierde: service-messages pasaron a cobro (oct-2026) + setup de días.
- **HECHO** — Módulo `bot/` en backend: `BotController` (`POST /api/bot/whatsapp/{token}` — token en path porque WAHA no firma), `BotService` (máquina de estados persistida en `bot_conversaciones`, expira 30 min), `BotConversacion`+repo, `WahaClient` (`/api/sendText`). Flujo: menú → nombre (paciente nuevo) → días laborales libres → horas (jornada 09:00×`horasTrabajoDia`, slots de `duracionCitaMin`, ≥30 min anticipación, sin solapes) → confirmación → cita `solicitada` origen `whatsapp`. Sobrecupo opt-in cuando día lleno + flag. Opción 2: código portal idempotente. Reglas espejo de `WebhooksController`.
- **HECHO** — Deploy: servicio `waha` (devlikeapro/waha, engine GOWS) en el stack demo, red interna únicamente; dashboard/QR solo por túnel SSH. Webhook `WHATSAPP_HOOK_URL` → backend interno. Envs nuevas en `.env` del VPS (generadas server-side): `SCONECT_BOT_TOKEN`, `SCONECT_WAHA_API_KEY`, `SCONECT_WAHA_SESSION`. Volumen `waha-sessions`→`/app/.sessions` (corregido tras leer health real).
- **Verificación** — `mvn test` 11/11 (4 nuevos `BotServiceTest`: agendar completo, portal solo registrados, reset menu, input inválido). Producción: WAHA health ok, webhook 401/200 según token, app 200.
- **RIESGO declarado** — WAHA es no-oficial: posible ban del número, apto piloto. Migración a Meta Cloud API si escala (solo cambia el adaptador).
- **PENDIENTE (usuario)** — vincular el WhatsApp del consultorio: `ssh -L 3000:localhost:3000 niko@200.141.25.56` → `localhost:3000/dashboard` → sesión `default` → QR.
- **Spec** — [[SCN - Recepcionista WhatsApp (WAHA + backend)]]; la nota n8n quedó `superseded` (contrato webhooks sigue vivo).

## 2026-11-06 (continuación) — WAHA dashboard + monitor Kuma

- **FIX** — Dashboard WAHA pedía login con clave aleatoria regenerada por restart → persistidas `SCONECT_WAHA_DASH_USER/PASSWORD` en `.env` del VPS + envs en compose. Credenciales entregadas al usuario (guardar en Bitwarden). Volumen sesiones corregido: health real mostró `/app/.sessions`, no `/app/sessions`.
- **HECHO** — Monitor Kuma `Sconect Demo` (ID 4) → `https://sconect.namp.cl/api/health` cada 60s. Vía `uptime-kuma-api` en contenedor python efímero; workaround: Kuma 2.1 exige columna `conditions` NOT NULL que la librería aún no envía → dict del monitor construido a mano (`_build_monitor_data` + `conditions=[]` + `_call("add")`).
- **NOTA** — El túnel SSH del dashboard WAHA muere si el contenedor se recrea: re-abrir `ssh -L 3000:localhost:3000 niko@200.141.25.56` y recargar.
- **PENDIENTE (usuario)** — vincular sesión `default` de WAHA con el WhatsApp del consultorio (QR en dashboard).

## 2026-11-06 (cierre) — Vinculación WAHA pendiente, pairing code como vía

- **INTENTO** — Sesión `default` creada por API; primera vez arrancó con engine WEBJS (env errónea `WAHA_ENGINE`) → corregida a `WHATSAPP_DEFAULT_ENGINE=GOWS` en compose y redeploy. GOWS activo (`grpc READY`, `gows connected`).
- **BLOQUEO** — QR escaneo falló dos veces: el PNG rota cada ~60s y llega al usuario con demora (se muestra la imagen por chat, no es cámara en vivo). Sesión quedó `FAILED` por timeout. **Vía elegida para el retake**: pairing code (`POST /api/default/auth/request-code`, sin cámara) — falta que el usuario pase el número del consultorio.
- **HECHO** — Credenciales dashboard persistidas (`SCONECT_WAHA_DASH_*` en `.env`); monitor Kuma `Sconect Demo` (ID 4) vivo contra `/api/health`.
- **PUNTO DE RETOMADA** — todo lo demás listo: bot desplegado y testeado (11/11), WAHA sano, red interna verificada (401/200 según token). Solo falta: (1) `POST /api/sessions/default/restart`, (2) pairing code con el número, (3) mandar "hola" al WhatsApp del consultorio y verificar respuesta del bot.
- **Cola pendiente** — errores importantes que el usuario encontró en la app (pospuestos); bug `PUT /api/preferencias`; recordatorios 24h; Flyway.

## 2026-11-13 — WAHA vinculado: recepcionista conectado al WhatsApp real

- **HECHO** — Sesión `default` → `WORKING`, cuenta `56962308757@c.us` ("Niko"), GOWS conectado. Logrado por QR en dashboard con cámara pre-abierta. Timing real: el QR muere a ~2.5 min y WAHA no regenera (sesión → FAILED); pairing code expira aún antes. Dashboard nuevo requiere Connect del worker (API + `WAHA_API_KEY`, guarda server en localStorage) o Sessions lista vacío.
- **PENDIENTE (verificación e2e)** — "hola" al +56 9 6230 8757 → bot debe contestar menú 1/2/3. Después: flujo completo agendar → cita `solicitada` aparece en la agenda del clínico.
- **RIESGO (cuentas)** — PAT GitHub `Nicolasmp92` de este PC expiró/revocado (12→13-nov): push/pull de repos privados y del vault caído hasta renovar. Commits quedan locales.

## 2026-11-13 (cierre) — Bot no respondía: fix HTTP/1.1 deployado

- **HECHO** — Testers mandaron "hola" sin respuesta. Causa aislada: el webhook entrante funcionaba (WAHA→backend 200) pero `WahaClient` fallaba al **responder** — el `HttpClient` del JDK intenta upgrade h2c en cleartext y WAHA cierra la conexión (`header parser received no bytes`). Endpoint y auth verificados sanos por curl antes de tocar código.
- **FIX+DEPLOY** — `HttpClient` pinned a HTTP/1.1 (commit `f4df87f`), `mvn test` 11/11, jar subido por rsync (el scp lo dejó corrupto 258B — verificado por SHA-256) y backend recreado: `/api/health` 200.
- **PENDIENTE (e2e)** — repetir "hola" al +56 9 6230 8757 → menú 1/2/3. Si no responde, siguiente sospechoso: remitentes llegan `…@lid` (esquema nuevo de WhatsApp) y `BotController` pasa `payload.from` directo como `chatId` — verificar si WAHA acepta `@lid` en `sendText`.
- **CORRECCIÓN** — el PAT `Nicolasmp92` NO murió (falsa alarma por DNS transitorio); pushes funcionan.
- **PUNTO DE RETOMADA** — sesión WAHA `default` WORKING, fix en prod, solo falta el test e2e. Si responde: probar flujo agendar → cita `solicitada` en la agenda del clínico. Cola intacta: errores de la app que el usuario reportó, bug `PUT /api/preferencias`, recordatorios 24h, Flyway.

## 2026-11-16 — Tercer PC dev (Windows) + afinación local del backlog

- **HECHO** — Sconect clonado en este PC (Windows, `nicolas.munoz` — tercer equipo, distinto de PC pega/PC casa del MOC): `Desktop/Desarrollo/sconect`. Toolchain portable `~/tools`: JDK 17.0.21 + Maven 3.9.9 + Flutter 3.50.0. `mvn test` 20/20, `flutter build web` OK. Credencial GitHub reusada del remote de `cabid` (PAT embebido, convención de este PC).
- **HECHO (diagnóstico bot)** — pipeline del recepcionista verificado local E2E con WAHA mockeado: "hola" → menú 1/2/3 tanto para `@c.us` como `@lid`, token malo → 401. El código está sano; si prod sigue sin responder el fallo es WAHA/WhatsApp, no el bot. Ojo: bug conocido de GOWS — `sendText` a `@c.us` puede dar 500 "no LID found" (issue devlikeapro/waha#2214); enviar a `@lid` es la vía oficial según el maintainer.
- **HECHO** — 3 commits en `sconect/main` (`9c1c506`): `559e173` fix PUT /api/preferencias merge tri-estado (ausente≠null explícito — el bug que borraba campos con PUT parcial, resuelto de la cola); `f1a5413` recordatorios 24h por WhatsApp (`RecordatorioService` + `citas.recordadoEn`, solo agendada/confirmada) + hardening `@lid` (PN real vía `GET /api/{session}/lids/{lid}`; sin resolver → teléfono null + guard anti `endsWith("")` que matcheaba cualquier paciente); `010bde7` ojito para ver contraseña en login. + `559e173` tests: 20/20 total.
- **HECHO** — Seed dev por defecto `nikolasmp92@gmail.com`/`niko9214` en application.yml (pedido del usuario).
- **PENDIENTE (deploy)** — Los 4 commits están pusheados pero NO deployados: este PC aún no tiene SSH al VPS. Llave `id_ed25519.pub` entregada al usuario para `authorized_keys`. Al habilitarse: `mvn package` + `flutter build web` → sync a `/opt/sconect-demo` → `docker compose -f docker-compose.demo.yml up -d --build` → verificar columna `recordado_en` en Postgres (precedente `eliminada` requirió ALTER manual) → e2e "hola" al +56 9 6230 8757.
- **NOTA** — Flutter 3.50 depreca `package:flutter/material.dart` (→ `material_ui`): 23 infos en analyze, sin errores; los otros PCs corren 3.47.x. Migración queda como deuda.
- **Cola intacta** — errores de la app que el usuario reportó (sin detalle aún), Flyway, migración material_ui, monitor Kuma ya existe.

## 2026-11-16 (tarde) — Deploy a producción + SSH resuelto

- **HECHO** — SSH de este PC al VPS habilitado: llave autorizada vía consola web Hostinger (Opción A). **Causa raíz del fallo posterior**: `id_ed25519` tenía passphrase (`niko9214`) — el servidor aceptaba la llave pero el cliente no podía firmar no-interactivamente. **Esto explica el "quirk host-bound" de koha-prod** (misma llave, mismo síntoma). Resuelto: passphrase removida (decisión del usuario, convención llaves sin passphrase); alias `ssh vps` configurado.
- **HECHO (diagnóstico VPS)** — Sesión WAHA `default` WORKING (`56962308757@c.us`, lid propio `184378835615751@lid`); webhook env `WHATSAPP_HOOK_URL`→backend con token OK; sesión zombie `session_01m7…` FAILED genera ruido horario en logs (`websocket not connected`) — candidata a borrar. Sin hits al webhook en 48h (nadie testeó desde el fix).
- **HECHO (deploy)** — Commits `559e173`+`f1a5413`+`010bde7` deployados a `/opt/sconect-demo` (jar SHA-256 verificado + build web). Stack healthy, `sconect.namp.cl/api/health` 200, columna `recordado_en` creada por ddl-auto sin ALTER manual.
- **HECHO** — Titular del demo cambiado a `nikolasmp92@gmail.com`/`niko9214` (decisión usuario; demo@sconect.cl dejó de existir). Update por SQL con bcrypt generado local. **Ojo trampa**: el hash `$2b$…` se corrompió por doble expansión de shell (`$2b`→`b`) en el primer UPDATE — re-aplicado por psql stdin heredoc; login verificado 200 via `/api/auth/login`.
- **PENDIENTE (e2e)** — "hola" al +56 9 6230 8757 → menú. Usuario por enviar.

## 2026-11-16 (noche) — E2E bot exitoso + confirmación notifica + fixes UX/CORS/lock

- **HECHO (e2e bot)** — "hola" al +56 9 6230 8757 → menú → agendar → `solicitada` id=7 en prod. Webhook→backend 200, sendText 201, `lids/{lid}` resolviendo PN en vivo (hardening operando).
- **HECHO (notificación)** — `notificarRespuesta` en `cambiarEstado`: PATCH solicitada→confirmada → `lids/pn` 200 → sendText 201 → mensaje recibido en WhatsApp real. El 401 de `lids/pn` visto antes era sonda manual sin `X-Api-Key` — falsa alarma.
- **HECHO (causa raíz "No tienes permiso")** — el CorsFilter rechazaba **PATCH** (no estaba en `allowedMethods`) con 403 "Invalid CORS request" 31B ANTES de auth: los GET cargaban la agenda pero confirmar moría en app/navegador; mis curls sin `Origin` pasaban 200. Fix `96e0865`: agregar PATCH. Verificado OPTIONS+PATCH con Origin → 200.
- **HECHO (agenda)** — `RefreshIndicator` pull-to-refresh (solicitudes del bot llegan con la agenda ya abierta); fix lazy-proxy en `cambiarEstado` (re-fetch `findWithDetalleById` para response+notify; el proxy `Paciente#1` moría fuera de sesión → 500 → "reintentar").
- **HECHO (UX bot)** — atajos `m`/`s`/`n` (además de menu/si/no), numeración plana `1.` (keycaps no agrupan decenas), fechas con año, instrucción de hora y de menú en líneas separadas.
- **HECHO (reglas configurables)** — `anticipacionMinMin` en preferencias (default 120, 0=off) reemplaza el 30' hardcodeado; el bot no ofrece horas dentro de la ventana.
- **HECHO (carrera reservas)** — `findWithLockById` PESSIMISTIC_WRITE sobre la fila del profesional + `@Transactional` en crear/actualizar: el par validar-solape→insert es serializado app↔bot. Bot re-valida solape+cupo bajo lock en `crearSolicitud`. 409 informativo: "la acaba de pedir un paciente por WhatsApp — respóndela en 'Por confirmar'" vs "solapa con la cita de <nombre> (<hora>)". Commit `1d78736`.
- **HECHO (AppToast)** — componente único `lib/core/widgets/app_toast.dart` (Overlay superior, exito/error/info, auto-dismiss): reemplazados los 17 `showSnackBar` ad-hoc de 13 archivos; el SnackBar default tapaba la bottom-nav. `AgendaAviso` (estado one-shot del bloc) → toast "Hora confirmada — avisamos a <paciente> por WhatsApp". Commit `212a25a`.
- **Tests** 20/20 · `analyze` 0 errores (solo deprecations material_ui preexistentes) · stack healthy.
- **PENDIENTE cola** — Flyway, migración material_ui, sesión WAHA zombie `session_01m7…` (ruido horario), errores de la app aún sin detalle del usuario.
- **HECHO (directorio público)** — el catálogo de clínicos se ve sin cuenta: `DirectorioScreen` público + widget `DirectorioClinicos` compartido con la pestaña Explorar del portal. Búsqueda, chips por especialidad (taxonomía `especialidades.dart`: clínica / terapias complementarias / otros), "Cerca de mí" con geolocator+Haversine. "Solicitar hora" sin sesión → gate `PortalEntradaScreen(comoGate)` que devuelve éxito y continúa agendando — la cuenta se pide solo en el enganche, como se pidió.
- **HECHO (auto-registro paciente)** — `codigos_portal.paciente_id` nullable (código pendiente por teléfono); `ingresar` con teléfono nuevo pide nombre+apellido (409) y crea el `Paciente` al reintentar. Social mock Google/Apple en la entrada ("llega pronto"). `Usuario` +lat/lng; `PerfilController` los acepta por API (mapa UI pendiente).
- **RIESGO (schema)** — `ddl-auto` no bajó el NOT NULL viejo de `codigos_portal.paciente_id` en Postgres local: ALTER manual hecho en local, **pendiente el mismo ALTER en producción** antes de desplegar. Refuerza la urgencia de Flyway.
- **Tests** — mvn 23/23 (nuevo `PortalRegistroTest`), flutter analyze 0, flutter test 11/11; fix test preexistente `agenda_test` (inyecta `_PrefsFake`, venía roto de 86a2b3a). e2e API local verificado: número nuevo → 409 → registro → token.
- **PENDIENTE** — ALTER prod + redeploy, UI mapa lat/lng clínico, social auth real, e2e "hola"→menú WhatsApp, decisión teléfono-notificación vs número-bot (2026-11-17).
- **HECHO (card directorio)** — portada/cover del clínico (`Usuario.fondoRuta` + upload/ver `/api/perfil/fondo`) y burbujas intercambiables: grande=logo consulta, chica=foto profesional, botón swap las alterna (AnimatedPositioned). Imágenes públicas `/api/portal/servicios/{id}/{foto,logo,fondo}`. Seed demo flag `SCONECT_SEED_DEMO`: 9 clínicos variados + coords; en local se les generaron JPGs mock reales. Commit `8036c8b` (2026-11-17).
- **HECHO (iconografía + seed media)** — adoptado `material_symbols_icons` (set oficial Google, Apache-2.0, tree-shake en build): ícono por especialidad en chips/secciones/placeholder-logo y `flip_to_front` en el badge de intercambio. `DataSeeder` ahora genera foto/logo/fondo con Java2D (determinístico por nombre) solo cuando el flag demo está activo — idempotente, no pisa uploads reales. Verificado e2e: regeneró media borrada al reiniciar; 23/23 backend, 11/11 flutter (2026-11-17).
- **HECHO (card encabezado)** — nombre + prefijo profesional ("Kg.", "Dr."…) ahora van sobre la portada, al lado del cluster de burbujas, con velo para legibilidad; `titulo` se renderiza como prefijo en la misma línea (antes era subtítulo aparte). Mock títulos normalizados a abreviaturas chilenas. analyze 0, test 11/11 (2026-11-17).
- **HECHO (fix directorio)** — el título "Encuentra tu profesional" se cortaba en el AppBar (competía con "Ingresar"): AppBar queda con "Profesionales" y el gancho pasa a encabezado del cuerpo sobre el buscador, compartido con la pestaña Explorar (2026-11-17).
- **HECHO (deploy prod)** — sconect.namp.cl actualizado: directorio + card encabezado/iconografía + ALTER `codigos_portal.paciente_id` aplicado + `SCONECT_SEED_DEMO=true` (9 clínicos ilustrados, media generada por el seed en el contenedor). e2e prod verificado: registro nuevo → 409 → token. Jar con SHA-256 chequeado (2026-11-17).
- **HECHO (fix caché prod)** — el teléfono veía la app vieja: nginx cacheaba 30d el bootstrap de Flutter (`main.dart.js`, `flutter_service_worker.js` — nombres sin hash). Ahora bootstrap `no-cache` y solo assets/canvaskit/icons con 30d. Cliente con SW viejo debe recargar en incógnito o borrar datos del sitio una vez (2026-11-17).
- **HECHO (filtros)** — chips de especialidad → botón tune + bottom sheet (badge + chip borrable en el contador): libera el top del directorio en móvil. Deployado a prod (2026-11-17).
- **HECHO (perf directorio)** — tirones de scroll: lista por grupos era `ListView(children:)` eager + imágenes decodificando a resolución completa. Fix: `ListView.builder` lazy con headers como items + `cacheWidth/Height` a tamaño físico. Deployado a prod (2026-11-17).
- **HECHO (fix blanco Solicitar hora)** — causa: `MaterialApp` sin `localizationsDelegates` y el picker pedía 'es' → crash/pantalla blanca. Fix: flutter_localizations + delegates (datepicker en español en toda la app). + diálogo de carga en solicitarCita y loadingBuilder en imágenes de la card. Deployado (2026-11-17).
- **HECHO (cuenta)** — botón Cerrar sesión fijado al pie con su divisor, fuera del scroll. Deployado (2026-11-17).
- **HECHO (cuenta paciente + foto compartida)** — componente reutilizable `core/widgets/opcion_cuenta.dart` (`OpcionCuenta` + `PieCerrarSesion` anclado al pie) usado por ambos perfiles; NavigationBar del paciente con color primary; cuenta del paciente con foto de perfil (JPG/PNG/WebP ≤5MB) que el clínico ve en su lista (`Paciente.fotoRuta`, `/api/portal/perfil/foto` JWT paciente, `/api/clinica/pacientes/{id}/foto` Bearer clínico, `tieneFoto` en DTO). e2e: paciente sube → clínico la ve → sin token 401. mvn 23/23, flutter 11/11, deployado a prod (2026-11-17).
- **HECHO (header directorio)** — filtros movidos al AppBar (icono tune + badge activo) en pantalla pública y pestaña Explorar; eliminado el encabezado grande, queda solo una línea caption bajo el buscador. Patrón de directorios: acción arriba, resultados en primer viewport. Deployado (2026-11-17).
- **HECHO (refresh global)** — pull-to-refresh en todas las vistas con datos (lista pacientes, ficha, evoluciones, archivos, perfil, preferencias, cuenta paciente; ya estaba en agenda/directorio/citas) + auto-refresh al cambiar de pestaña vía bump de Key (recrea el subárbol → initState recarga). Deployado (2026-11-17).
- **HECHO (rediseño header directorio)** — OODA condensado: la búsqueda se integra en el AppBar (`CampoBusquedaDirectorio` compartido, controller externo en DirectorioClinicos); titular eliminado, el cuerpo abre en resultados (1 sola fila sobre la primera card). RIESGO recurrente: procesos/buffers del IDE revierten archivos editados por el agente — reaplicado (2026-11-17).
- **HECHO (directorio)** — eliminado el titular residual "Encuentra a tu profesional" (resto de la reversión del IDE que quedó commiteado). La vista abre directo en resultados bajo la barra de búsqueda. Deployado (2026-11-18).
- **HECHO (agenda)** — calendario con 3 modos ciclables: semana compacta (default) → mes → oculto. En semana las flechas navegan ±7 días y días de otros meses se atenúan. Celda compartida `_celda`. Deployado (2026-11-18).
- **HECHO (sello visual glass)** — nueva identidad "vidrio esmerilado": `core/widgets/fondo_app.dart` (degradado menta #D3EAE2→#F1F8F6→#DCEFE9 + 2 manchas esmeralda translúcidas) montado vía `MaterialApp.builder`; `AppColors.background` → transparente (los 22 Scaffold dejan ver el fondo) y `AppColors.surface` → blanco 88% (tarjetas tipo glass, contraste conservado). Un solo punto de cambio, sin tocar pantallas. analyze 0, test 11/11, deployado a prod (2026-11-18).
- **HECHO (fix glass)** — inputs de login/portal_entrada quedaron tintados al volverse `background` transparente: su `fillColor` pasó a `AppColors.surface` (blanco 88%). Únicos dos usos de `fillColor: AppColors.background` en el repo. Deployado (2026-11-18).
- **HECHO (directorio UX)** — botón de filtros bajó del AppBar a `trailing` del `CampoBusquedaDirectorio` (queda al lado del campo, badge intacto); fila del título queda solo con "Profesionales" + "Ingresar". Restaurada flecha `arrow_back` (Symbols) con `maybePop` — el push desde login perdía el botón de regreso. Iconos migrados a Material Symbols (search/close/tune/arrow_back). Portal Explorar: recuperada la integración de búsqueda en `_barraPortal` (param `busqueda`/bottom) que el IDE había revertido a una versión pre-d80a19b. analyze 0, test 11/11, deployado (2026-11-18).
- **HECHO (favoritos + rating mock)** — `FavoritosService` (ChangeNotifier + SharedPreferences, IDs en el dispositivo, sirve con y sin cuenta): corazón translúcido en la portada de cada card (Symbols.favorite/favorite_border), toggle "Ver mis favoritos" en la fila de resultados (el listado = directorio filtrado), estado vacío propio. Rating mock determinístico por id (`_ratingMock`, 4.2–4.9 + N reseñas) bajo la especialidad — placeholder hasta clasificación real. analyze 0, test 11/11, deployado (2026-11-18).
- **HECHO (logo de marca)** — nuevo sello Sconect: burbuja de chat + corazón + check (conexión · salud · agenda), degradado esmeralda sobre squircle. Iterado visualmente (6 versiones renderizadas con Chrome headless hasta legible a 96px). Assets: `web/icons/Icon-{192,512}` + maskable (glifo 72% zona segura) + `favicon.png` 64px + `assets/brand/logo.png|svg` (fuente SVG en repo). Splash y login usan el logo real en vez de `health_and_safety` genérico. analyze 0, test 11/11, deployado (2026-11-18).
- **HECHO (apartado favoritos)** — `DirectorioClinicos.soloFavoritos` (modo listado fijo, oculta el toggle); nueva `FavoritosScreen` reutiliza todo el directorio (cards, corazones, distancia, solicitar hora); entrada "Mis favoritos" en Cuenta del paciente con contador reactivo vía `OpcionCuenta`. Des-marcar corazón saca la card en vivo. analyze 0, test 11/11, deployado (2026-11-18).
- **HECHO (foto de perfil por cámara)** — plugin `camera` 0.12.2 (soporte web vía getUserMedia): `core/widgets/camara_perfil.dart` con vista previa frontal espejada, guía circular atenuada, captura y confirmación Usar/Repetir; `core/widgets/elegir_foto.dart` = selector compartido (Tomar foto / Elegir de la galería) que devuelve bytes+MIME. Integrado en los dos flujos de foto de perfil (paciente en Cuenta, clínico en Perfil) — solo fotos de perfil usan cámara; el resto sigue con FilePicker. Errores amigables si no hay cámara o el navegador la bloquea. analyze 0, test 11/11, deployado (2026-11-18).
- HECHO 2026-11-18: Bloqueo de pacientes por profesional (tabla paciente_bloqueos paciente×profesional; PUT /api/clinica/pacientes/{id}/bloqueo; portal rechaza agendar con 403; UI listado con diálogo claro + reversible). E2E verificado local y tabla creada en prod (ddl-auto update). Pendiente: aplicar la misma tabla al futuro endpoint real de evaluación/clasificación. Deploy prod OK.
- DECISIÓN 2026-11-18: Sconect prohíbe bottom sheets — toda opción en ventana (AlertDialog). Migrados filtro de especialidades y selector de foto de perfil; showModalBottomSheet = 0 en la app. Deploy prod OK.
- HECHO 2026-11-18: Favoritos del paciente movido a pestaña del menú inferior (es destino de navegación, no ajuste); búsqueda+filtros del directorio fuera del AppBar verde → campo píldora sobre fondo glass. Deploy prod OK.
- HECHO 2026-11-18: WhatsApp bot verificado e2e en prod — menú de horas numeradas, confirmación sí/no, solicitud registrada, confirmación de cita y recordatorio 24h automático disparando correctamente (cita 19/11 14:30, recordatorio enviado 18/11). Cierra el pendiente 'hola→menú e2e' del backlog.
- HECHO 2026-11-18: Bandeja Solicitudes separada de Agenda (pestaña propia con badge, gestos →agenda/←rechaza+motivo, contexto del día expandible, resueltas 24h apagadas). Reagendo = contraoferta que el paciente confirma en portal o si/no por WhatsApp (estado respondiendo_propuesta). Caducidad: 24h espera o sin día de anticipación. Schema verificado en prod + ALTER check enum aplicado. Deploy OK.
- HECHO 2026-11-18: Selector de hora en grilla de chips (elegirHora compartido, 07-22h cada 30min) reemplaza el dial de manecillas en los 3 puntos: agendar cita, proponer hora, solicitar hora paciente. Deploy prod OK.
2026-11-18 17:02 - **HECHO (seeder realista + deploy)** — Reconstruido `DataSeeder`: 15 clínicos en 10 comunas con días laborales/duración/cupo propios; 10 pacientes chilenos (RUT con DV válido, Fonasa/Isapre/Capredena, antecedentes, foto iniciales); agenda completa del titular: agendada hoy, confirmada WhatsApp mañana, 3 pendientes en bandeja (1 con propuesta de reagendo activa), atendida ayer con evolución clínica, rechazada <24h con motivo, cancelada con motivo, 1 paciente bloqueado. Idempotente por teléfono/paciente+inicio/(paciente,profesional). Bug: en prod el titular no calza con SCONECT_SEED_CORREO → ahora busca por rol 'titular'. ALTER local: columna `evoluciones.eliminada` faltaba (ddl-auto no agrega NOT NULL a tablas con datos). mvn 23/23, deployado, prod verificado: 16 clínicos, 10 pacientes, 9 citas demo, bandeja con pendientes+propuesta (2026-11-18).
2026-11-19 08:45 - **HECHO (Flyway adoptado)** — Schema versionado: V1__baseline.sql = pg_dump --schema-only de prod (13 tablas, sin meta-comandos psql ni prefijo public.); baseline-on-migrate adopta bases existentes, vacías corren V1 completo. ddl-auto update→validate (Hibernate solo valida, Flyway es dueño del schema — si entidad no calza, boot falla temprano). Tests H2 con flyway off. Verificado: baseline en local+prod, V1 completo en schema vacío, 23/23 tests, prod health 200. REGLA nueva: todo cambio de schema = V(N)__x.sql nuevo, nunca ALTER manual ni ddl-auto. Cierra el pendiente Flyway del backlog (2026-11-19).
2026-11-19 09:25 - **HECHO (fix iconos prod)** — Causa: tree-shake de fuentes en release eliminaba glifos Symbols.* usados vía mapas/funciones (iconoDe/especialidad_iconos); debug no lo muestra y la PWA hereda el mismo build. Fix: tool/subset_symbols_font.py (post-build) subsetea MaterialSymbolsOutlined.ttf con los 48 codepoints usados → 146 KB. Requiere fonttools (pip). Regla deploy: flutter build web → python3 tool/subset_symbols_font.py → sync web. Deployado, fuente verificada en prod (149820b) (2026-11-19).
- **HECHO** — `front/SCN - front-widgets.md` creado (2026-11-19): inventario de widgets compartidos — AppButton con su API completa (variantes primary/danger/text, uso CTA vs diálogo) + OpcionCuenta/FondoApp/AppToast/ElegirFoto/CamaraPerfil/ElegirHora + tokens (esmeralda #004D40, radios 14/16, alturas 52/40). Primera aplicación de la regla [[Docs-first - estructura antes de construir]].
- **HECHO** — `back/SCN - back-arquitectura.md` creado (2026-11-19): mapa de 11 paquetes-por-dominio, contrato API por superficie (JWT staff / RBAC admin / portal por código / webhooks `X-Api-Key` / público), entidades e invariantes (`EstadoCita`×`OrigenCita`, evoluciones inmutables, archivos 20MB, código portal caducable, RBAC 26 permisos), infra Postgres+Flyway vs H2 local.
- **HECHO** — 2026-11-20: comando de backend local en MOC corregido — faltaba `SPRING_FLYWAY_ENABLED=false SPRING_JPA_HIBERNATE_DDL_AUTO=update` (sin eso H2 rechaza el SQL PostgreSQL de `db/migration` y el boot muere, `V1__baseline.sql` "Tipo de dato desconocido: ADD"). Preview relanzado: backend :8083 health 200, app :4203 sirviendo build de `0681295`.
- **HECHO** — 2026-11-20: BD local repoblada con `SCONECT_SEED_DEMO=true` (el seed ya existía desde el 17-11 del otro PC, faltaba el flag). Verificado: 10 pacientes, 9 citas con estados agendada/confirmada/solicitada/atendida/cancelada y orígenes app/whatsapp + 9 clínicos con media. Gotcha: `kill_shell` mata mvn pero deja el java huérfano en :8083 — hay que matar por `Get-NetTCPConnection -LocalPort 8083` antes de relanzar (síntoma: webServerStartStop falla y el proceso viejo sigue respondiendo 200).
- **HECHO** — 2026-11-20: spec `front/SCN - front-actualizacion-pwa.md` IMPLEMENTADA y pusheada (`691e874`): ActualizacionService (polling version.json 30min + resume), pwa_update + `sconectActualizar()` en index.html (SKIP_WAITING→controllerchange→reload), BannerActualizacion no-modal. analyze 0 · test 11/11 · build web OK. Primera spec front que siguió el ciclo completo docs-first (propuesta → build → spec actualizada).
