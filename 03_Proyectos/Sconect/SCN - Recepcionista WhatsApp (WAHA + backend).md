---
tipo: nota-tecnica
proyecto: sconect
estado: implementado-piloto
actualizado: 2026-11-06
tags: [whatsapp, bot, waha, recepcionista, arquitectura]
---
# SCN — Recepcionista WhatsApp: WAHA + backend

> Reemplaza la arquitectura n8n de [[SCN - n8n Recepcionista WhatsApp]]
> (el contrato `/api/webhooks/**` sigue vivo para bots externos, pero el
> recepcionista ya no pasa por n8n).

## Decisión (2026-11-06)

| Capa | Elección | Por qué |
|---|---|---|
| Lógica del bot | **Backend Spring Boot** (`io.github.nicolasmp92.sconect.bot`) | máquina de estados tipada, testeable, versionada y deployada con el dominio — sin servicio extra opaco |
| Transporte WhatsApp | **WAHA** (contenedor en el stack demo, engine GOWS) | REST simple, gratis (Apache-2.0, tiers free desde 2026-06), pairing code sin depender de re-escanear QR |
| n8n | **fuera del camino crítico** | sigue disponible para glue no crítico (Calendar, correo, CRM) sin bloquear |

Motivación: los primeros 1.000 service-messages/mes de Meta Cloud API pasaron
a cobrarse (oct-2026), y el flujo del recepcionista es una máquina de ~6
estados — un orquestador genérico era sobrediseño.

## Arquitectura

```text
Paciente WhatsApp
  → WAHA (contenedor sconect-demo-waha-1, engine GOWS)
  → WHATSAPP_HOOK_URL → POST /api/bot/whatsapp/{SCONECT_BOT_TOKEN}
  → BotController → BotService (estado en tabla bot_conversaciones)
  → WahaClient → POST waha:3000/api/sendText → respuesta al paciente
```

- Todo dentro de la red Docker `internal` del stack `sconect-demo`: WAHA no se
  expone a internet. Su dashboard (pairing/QR) solo por túnel SSH:
  `ssh -L 3000:localhost:3000 niko@200.141.25.56` → `http://localhost:3000`.
- Auth del webhook: token en el path (WAHA no firma requests). Generado en
  `.env` del VPS, nunca en el repo.
- `WAHA_API_KEY` protege la API de WAHA dentro de la red.
- Sesión persistida en volumen `waha-sessions` → `/app/.sessions`.

## Máquina de estados (`bot_conversaciones.estado`, expira a los 30 min)

```text
menu ── "1" ──→ [paciente nuevo] esperando_nombre ──→ eligiendo_dia
     └── "1" ──→ [paciente conocido] eligiendo_dia
eligiendo_dia ──N──→ eligiendo_hora ──N──→ confirmando ──"si"──→ cita solicitada
                                          (día lleno + sobrecupoBot)
                                          └──→ decidiendo_sobrecupo ──"si"──→ cita sobrecupo
menu ── "2" ──→ código portal idempotente (reusa codigos_portal)
menu ── "3" ──→ derivación a contacto humano
"menu"/"cancelar"/"hola" en cualquier estado → vuelve al menú
```

Reglas de agenda espejo del backend: días laborales + `dias_especiales`
(bloqueado cierra / extra abre), jornada 09:00–(09+`horasTrabajoDia`), slots
de `duracionCitaMin`, sin pasadas (≥30 min anticipación), sin solapes, cupo
`maxPacientesDia`. La cita queda `solicitada` (origen `whatsapp`) — el
clínico confirma desde su agenda, igual que el flujo n8n propuesto.

## Archivos

| Pieza | Ruta |
|---|---|
| Webhook WAHA | `backend/.../bot/BotController.java` |
| Máquina de estados | `backend/.../bot/BotService.java` |
| Estado conversación | `bot/BotConversacion.java` + repo |
| Cliente WAHA | `bot/WahaClient.java` |
| Tests | `src/test/.../bot/BotServiceTest.java` (4 casos, WahaClient mockeado) |
| Compose | `deploy/demo/docker-compose.demo.yml` (servicio `waha`) |
| Config | `application.yml`: `sconect.bot.webhook-token`, `sconect.waha.*` |

Envs nuevas (en `/opt/sconect-demo/.env`): `SCONECT_BOT_TOKEN`,
`SCONECT_WAHA_API_KEY`, `SCONECT_WAHA_SESSION=default`.

## Riesgos declarados

- **WAHA es no-oficial** (WhatsApp Web via whatsmeow): riesgo de ban del
  número — apto para piloto, no para producción con clientes reales.
  Migración natural si escala: Meta Cloud API (oficial) — la máquina de
  estados queda intacta, solo cambia el adaptador (BotController + WahaClient).
- **Número del consultorio**: la sesión vinculada es una cuenta real de
  WhatsApp; usar número dedicado del consultorio, no el personal.
- Sin Flyway: la tabla `bot_conversaciones` la crea `ddl-auto` (pendiente
  general del proyecto, no específico del bot).

## Verificación (2026-11-06)

- `mvn test` 11/11 (4 nuevos del bot: agendar desde cero, portal solo
  registrados, reset con menu, input inválido).
- Deploy VPS: `waha` healthy, `health` ok con api key, webhook token malo
  → 401 / token real → 200, app `sconect.namp.cl` sigue 200.

## Paso que le queda al usuario — vincular número (pendiente)

**Estado 2026-11-06 cierre**: sesión `default` creada con engine GOWS pero en
`FAILED` — el QR expiró dos veces sin escanearse (rota cada ~60s y llega al
usuario con demora). Próximo paso al retomar:

1. `POST /api/sessions/default/restart` (X-Api-Key de `.env`) → vuelve a
   `SCAN_QR_CODE`.
2. Preferir **pairing code** sobre QR: `POST /api/default/auth/request-code`
   con `{"phoneNumber":"569…"}` → el usuario ingresa el código en WhatsApp
   (Dispositivos vinculados → "Vincular con número de teléfono") — sin
   cámara ni carrera contra el timeout. Falta: número del consultorio.
3. Dashboard alternativo: `ssh -L 3000:localhost:3000 niko@200.141.25.56`
   → `localhost:3000/dashboard` (admin / clave en `.env` del VPS:
   `SCONECT_WAHA_DASH_*`). El túnel muere si el contenedor se recrea.
