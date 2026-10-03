---
tipo: proyecto
proyecto: sconect
estado: activo-mvp-backend-listo
actualizado: 2026-10-02
tags: [salud, agenda, pacientes, whatsapp, n8n, flutter, spring-boot]
---
# 🩺 MOC — Sconect

Plataforma de gestión clínica para profesionales que atienden **particular** (kinesiología, podología, nutrición, medicina alternativa…): agenda + evolución de pacientes + **agendamiento por WhatsApp vía n8n**. Repo: `~/Escritorio/Desarrollo/sconect` (monorepo: `backend/` Spring Boot + `app/` Flutter).

PRD original (especificación del dominio): `99_Archivo/Proyectos personales/sconect_project/Product Requirements Document.md` — ojo: dice stack Go, el vigente es Spring Boot.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero el contrato de los webhooks n8n** → sección "Webhooks n8n" del `README.md` del repo
- **Quiero levantar el backend** → `cd backend && mvn spring-boot:run` (:8083); login `admin@sconect.dev` / `sconect-admin-2026`
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Estado (2026-10-02)

Backend completo y verificado:

| Pieza | Estado |
|---|---|
| RBAC titular/administrativo (26 permisos, delegación) | ✅ smoke OK |
| Pacientes / Citas (estado + origen whatsapp) | ✅ |
| Evoluciones **inmutables** | ✅ (sin PUT/DELETE por diseño) |
| Archivos clínicos (multipart, 20MB, `./uploads`) | ✅ |
| Webhooks n8n (`X-Api-Key`) | ✅ 201/401 verificados |
| App Flutter | 🚧 skeleton: login mock, falta conectar al backend |
| Flujo n8n/WhatsApp real | ⬜ fase 2 (contrato API ya servido) |
| AuditLog + reportes (PRD) | ⬜ fase 2 |

## Decisiones vigentes

- **Modelo de cuenta**: titular + administrativo con permisos delegables (el `administrativo` NO ve evoluciones por defecto — privacidad clínica). Multi-profesional fuera del MVP.
- **Multidisciplina** vive en `usuarios.especialidad`, no en la estructura.
- Reglas protegidas: paciente con historial → soft-delete; cita con evoluciones → cancelar (409).
- Puertos: API `8083` (bloque sconect). Repos previos archivados: `SConect-Laravel` (vacío), `sconect-app` (skeleton reutilizado dentro del monorepo).
