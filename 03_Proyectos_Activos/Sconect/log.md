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
