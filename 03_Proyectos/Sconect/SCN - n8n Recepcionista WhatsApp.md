---
tipo: nota-tecnica
proyecto: sconect
estado: superseded
actualizado: 2026-11-06
tags: [n8n, whatsapp, bot, integracion, recepcionista]
---
# SCN — n8n Recepcionista por WhatsApp

> **SUPERSEDED 2026-11-06** — n8n salió del camino crítico. La arquitectura
> elegida e implementada es backend + WAHA: ver
> [[SCN - Recepcionista WhatsApp (WAHA + backend)]]. Esta nota se conserva
> porque el contrato `/api/webhooks/**` sigue sirviendo para bots externos.

**Objetivo:** un paciente escribe al WhatsApp de la consulta → el bot le ofrece
horas libres → agenda su solicitud → el clínico confirma desde su agenda.
El clínico deja de contestar "¿tiene hora?" a mano = **el feature que vende**.

## Contrato backend — SERVIDO (2026-11-05, commit `ead323d`)

| Endpoint | Para qué |
|---|---|
| `GET /api/webhooks/preferencias` | duración de cita, días laborales, cupo diario, flag sobrecupo del titular |
| `GET /api/webhooks/agenda?desde&hasta` | citas ocupadas en un rango (no canceladas) |
| `POST /api/webhooks/citas` | crea la solicitud (estado `solicitada`, busca/crea paciente por teléfono, respeta día laboral/bloqueo/solape/cupo; `solicitudSobrecupo` + flag → sobrecupo solicitado) |
| `POST /api/webhooks/portal/codigo` | código de acceso al portal para entregarlo por WhatsApp (idempotente, 404 si no es paciente) |

Auth: `X-Api-Key` en todos (`SCONECT_WEBHOOK_API_KEY` — cambiar en prod).

## Flujo conversacional propuesto

```text
Paciente: "hola, quiero hora"
  → n8n: GET preferencias + GET agenda (próximos 7 días laborales)
  → bot ofrece 3-4 horas libres (slots = duracionCitaMin)
Paciente: elige una
  → POST /citas {telefono, inicio, motivo}
  → 201: "Solicitud enviada — <Nombre> te confirmará"
  → 409 cupo: "Día lleno. ¿Otro día?" (si sobrecupoBot → "¿pedir hora extra al clínico?")
  → 409 solape: reprogramar oferta
  → 400 día no laboral: ofrecer siguiente laboral
Clínico: confirma/rechaza en agenda (ya existe en la app)
```

Comandos extra del bot: `"mi código"` → `POST /portal/codigo` → entrega el
código del portal; `"cancelar"` → fase 2 (DELETE citas del portal existe,
falta vía webhook si se quiere por chat).

## Provider de WhatsApp — DECISIÓN PENDIENTE DEL USUARIO

| | Meta Cloud API (oficial) | Evolution API (self-hosted) | WAHA |
|---|---|---|---|
| Costo | ~USD 0.005–0.08/mensaje (conversación) | Gratis (VPS propio ya pagado) | Core gratis; Plus ~$ |
| Riesgo | Cero — canal oficial | **Ban del número** posible (ToS) | Igual que Evolution |
| Setup | Verificación de empresa + app Meta + número dedicado | Docker + QR scan con WhatsApp normal | Docker + QR |
| Tiempo a producción | Días (verificación Meta) | Horas | Horas |
| Fit "dinero rápido" | Malo para piloto | **Mejor para MVP** | Alternativa |

**Recomendación:** Evolution API en Dokploy para el piloto (costo $0, setup en
horas, el número del clínico es el suyo). Meta Cloud API cuando haya un
cliente pagando que justifique la formalidad — el flujo n8n no cambia, solo
el nodo de entrada/salida.

## Despliegue

1. Dokploy VPS: servicio `n8n` (template) + servicio `evolution-api` (compose) — ambos tras `namp.cl` subdominios (`n8n.`, `wa.`).
2. n8n → sconect API: backend debe estar desplegado (hoy corre local :8083 — **sconect aún no tiene deploy en VPS**; eso es prerrequisito real del bot en producción).
3. `SCONECT_WEBHOOK_API_KEY` fuerte en prod + `SCONECT_PORTAL_DEV_CODE=false`.

## Pendientes abiertos

- [ ] Decisión provider (tabla arriba)
- [ ] Deploy de sconect al VPS (backend + Postgres) — prerrequisito
- [ ] n8n en Dokploy + workflow importable (JSON)
- [ ] Evolution API + QR del número del clínico
- [ ] Rate-limit en `POST /citas` del webhook (hoy solo valida reglas de negocio)
- [ ] Notificación al clínico cuando entra una solicitud por el bot
