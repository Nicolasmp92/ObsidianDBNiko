---
tipo: proyecto
proyecto: sconect
estado: activo
actualizado: 2026-11-05
tags: [salud, agenda, pacientes, whatsapp, n8n, flutter, spring-boot]
---
# 🩺 MOC — Sconect

Plataforma de gestión clínica para profesionales que atienden **particular** (kinesiología, podología, nutrición, medicina alternativa…): agenda + evolución de pacientes + **agendamiento por WhatsApp vía n8n**. Repo: `~/Escritorio/Desarrollo/sconect` (PC pega) y `Desktop/Desarrollo/sconect` (PC casa) — monorepo: `backend/` Spring Boot + `app/` Flutter.

PRD original (especificación del dominio): `99_Archivados/Proyectos personales/sconect_project/Product Requirements Document.md` — ojo: dice stack Go, el vigente es Spring Boot.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero el contrato de los webhooks n8n** → sección "Webhooks n8n" del `README.md` del repo
- **Quiero levantar el backend local** → `cd backend && SCONECT_DB_URL="jdbc:h2:mem:sconect;DB_CLOSE_DELAY=-1" SCONECT_DB_USER=sa SCONECT_DB_PASSWORD= SCONECT_SEED_CORREO=nikolasmp92@gmail.com SCONECT_SEED_CLAVE=niko9214 SCONECT_CORS_ORIGENES="http://localhost:*,http://127.0.0.1:*" ~/tools/apache-maven-3.9.9/bin/mvn spring-boot:run` (:8083); login `nikolasmp92@gmail.com` / `niko9214` (rol `titular`)
- **Quiero levantar la app web local** → `cd app` y `cmd /c "C:\Users\ferlu\tools\flutter-sdk\flutter\bin\flutter.bat run -d web-server --web-port=4203"` → http://localhost:4203 (Flutter 3.47.9 portable; `flutter.bat` solo vía `cmd /c` desde Git Bash)
- **Quiero abrir la demo pública** → https://sconect.200.141.25.56.sslip.io (login `demo@sconect.cl`). Stack `/opt/sconect-demo` en el VPS; redeploy = compilar jar+web en dev → `tar czf - . | ssh niko@200.141.25.56 "tar xzf - -C /opt/sconect-demo"` → `docker compose -f docker-compose.demo.yml up -d --build`. Secrets en `/opt/sconect-demo/.env` (chmod 600, no van al repo)
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Estado (2026-11-05)

Backend completo y verificado:

| Pieza | Estado |
|---|---|
| RBAC titular/administrativo (26 permisos, delegación) | ✅ smoke OK |
| Pacientes / Citas (estado + origen whatsapp) | ✅ |
| Evoluciones **inmutables** | ✅ (sin PUT/DELETE por diseño) |
| Archivos clínicos (multipart, 20MB, `./uploads`) | ✅ |
| Webhooks n8n (`X-Api-Key`) | ✅ 201/401 verificados |
| App Flutter (auth real, pacientes, agenda, evoluciones, portal) | ✅ conectada al backend |
| Demo pública en VPS | ✅ `sconect.200.141.25.56.sslip.io` (pendiente DNS `sconect.namp.cl`) |
| Flujo n8n/WhatsApp real | ⬜ contrato API servido; falta workflow + provider |
| AuditLog + reportes (PRD) | ⬜ fase 2 |

## Pendientes al 2026-11-05 (orden de ataque)

1. **DNS `sconect.namp.cl` → `200.141.25.56`** en NIC Chile — dueño: usuario. Traefik ya tiene la regla; al propagarse el dominio real queda con HTTPS solo.
2. Monitor Kuma (`status.namp.cl`) para el dominio demo — después del DNS.
3. **Provider WhatsApp** (decisión): Meta Cloud API vs Evolution API vs WAHA — ver matriz en [[SCN - n8n Recepcionista WhatsApp]].
4. Workflow n8n del recepcionista (el contrato API ya está: preferencias/código/sobrecupo).
5. Recordatorios 24h (`recordadoEn` ya existe en `citas`).
6. UI agenda: atenuar días no laborales/bloqueados + horarios por día.
7. **Flyway antes de producción real** (2 incidentes con `ddl-auto` ya).
8. Bug conocido: `PUT /api/preferencias` con campos ausentes los desactiva (un PUT solo con `sobrecupoBot` borra `maxPacientesDia`) — decidir si el contrato cambia a PATCH parcial.
9. Ventana mínima de anulación en portal; logo en comprobantes.
10. H2 de dev es en memoria (se borra al reiniciar); si se quiere persistencia local → `jdbc:h2:file:./data/sconect` con credenciales controladas.

## Decisiones vigentes

- **Modelo de cuenta**: titular + administrativo con permisos delegables (el `administrativo` NO ve evoluciones por defecto — privacidad clínica). Multi-profesional fuera del MVP.
- **Multidisciplina** vive en `usuarios.especialidad`, no en la estructura.
- Reglas protegidas: paciente con historial → soft-delete; cita con evoluciones → cancelar (409).
- Puertos: API `8083` (bloque sconect). Repos previos archivados: `SConect-Laravel` (vacío), `sconect-app` (skeleton reutilizado dentro del monorepo).
