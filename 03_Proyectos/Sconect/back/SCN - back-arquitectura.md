---
tipo: documentacion-tecnica
proyecto: sconect
actualizado: 2026-11-19
tags: [back, arquitectura, spring, regla-docs-first]
---

# SCN — Arquitectura del backend

Mapa de módulos del backend Spring Boot 3.5 / Java 17. **Antes de crear un
módulo o endpoint nuevo: leer aquí** — evita dominios duplicados y rutas
huérfanas. Regla madre: [[Docs-first - estructura antes de construir]].

## Módulos (package-por-dominio, `io.github.nicolasmp92.sconect.*`)

| Paquete | Resuelve | Prefijo API |
|---|---|---|
| `auth` | Login + JWT (AuthController, JwtService, JwtAuthFilter) | `/api/auth` |
| `acceso` | RBAC: `Rol` + `Permiso` (clave, nombre, categoría) — 26 permisos | `/api/admin` |
| `usuarios` | Staff: `Usuario`, perfil propio, preferencias/horario (`DiaEspecial`), admin de usuarios | `/api/perfil`, `/api/preferencias`, `/api/admin/usuarios` |
| `clinica` | Dominio clínico: `Paciente`, `Cita`, `Evolucion`, `ArchivoClinico`, `PacienteBloqueado`, `CaducidadSolicitudesService` | `/api/clinica/**` |
| `portal` | Portal paciente: `CodigoAccesoPaciente` (entra por código, sin cuenta) | `/api/portal` |
| `bot` | Bot WhatsApp: `BotConversacion`, `BotService`, `RecordatorioService`, `WahaClient` | `/api/bot` |
| `webhooks` | Entrada n8n (auth `X-Api-Key`) | `/api/webhooks` |
| `health` | Liveness | `/api/health` |
| `comun` | `EntidadBase` (id/audit compartidos) | — |
| `config` | `SecurityConfig` (filtro JWT + reglas por ruta) | — |
| `seed` | `DataSeeder` (datos demo/dev vía `SCONECT_SEED_*`) | — |

## Contrato API — superficies

- **Autenticadas (JWT, header `Authorization`)**: `/api/clinica/**`,
  `/api/perfil`, `/api/preferencias` — staff logueado
- **Admin** (JWT + permisos RBAC): `/api/admin/**`
- **Portal paciente** (código de acceso, sin JWT de staff): `/api/portal`
- **Máquina-a-máquina**: `/api/webhooks` (`X-Api-Key`), `/api/bot`
- **Públicas**: `/api/auth/login`, `/api/health`

## Entidades e invariantes clave

| Entidad | Notas |
|---|---|
| `Cita` | `EstadoCita`: `agendada` → `confirmada` → `atendida` / `cancelada` / `no_asistio`; `solicitada` = pendiente de aprobación. `OrigenCita`: `manual` / `whatsapp` / `app` |
| `Evolucion` | **Inmutable por diseño** — no hay PUT/DELETE. Corrección = nueva evolución |
| `Paciente` | `PacienteBloqueado` bloquea su acceso al portal |
| `ArchivoClinico` | Multipart, máx 20 MB, storage `./uploads` |
| `CodigoAccesoPaciente` | Token de entrada del portal; caduca (servicio `CaducidadSolicitudes`) |
| `Rol`/`Permiso` | RBAC declarativo — permiso por clave; titular lo tiene todo, administrativo delegado |

## Infra

- **BD**: PostgreSQL en prod/dev; H2 in-mem para local (`SCONECT_DB_URL` +
  `ddl-auto=update`, Flyway off — migraciones PostgreSQL-only en `db/migration`)
- **Seed**: `SCONECT_SEED_CORREO`/`SCONECT_SEED_CLAVE` → titular demo
- **Demo**: `/opt/sconect-demo` en VPS, `sconect.200.141.25.56.sslip.io`
