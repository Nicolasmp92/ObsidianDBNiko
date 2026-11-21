---
status: Pendientes
proyecto: kaipetpoint
fase: monetización
criticidad: alta
esfuerzo: M
---

# KPP — Pasarela de suscripciones SaaS (cobro del arriendo)

_Objetivo: cobrar el arriendo mensual a las tiendas automáticamente, con la
suscripción como entidad del dominio — la pasarela queda como adaptador
reemplazable. **No confundir** con `KPP - Pagos online integrados` (eso es
el cobro en el POS al cliente final de cada tienda)._

## Decisión (análisis 2026-11-20)

**Flow Suscripciones** como pasarela inicial, con **cobro manual por
transferencia** como puente para los primeros clientes. Oneclick Mall /
PatPass queda como migración futura si la comisión duele.

Por qué Flow (verificado 20-nov): API de suscripciones nativa (planes,
registro de tarjeta por redirect, cobro automático, `trial_period_days`,
cupones), 2,89%+IVA depósito a 3 días (3,19% día siguiente), sin costo
fijo, sandbox disponible.

Descartado: Stripe/Paddle (no dan cuenta comercio Chile directo / MoR
caro); Oneclick directo (burocracia código comercio + scheduler de cobros
propio, sin beneficio a esta escala); estado de suscripción solo en Flow
(dependencia frágil — vive en nuestra BD).

## Módulo `suscripciones/` (backend)

```
Plan(id, nombre, monto, moneda, trialDias)
Suscripcion(usuarioId, planId, estado, proveedorSubId, periodoFin)
estado ∈ {TRIAL, ACTIVA, VENCIDA, SUSPENDIDA, CANCELADA}
```

- `FlowClient`: firma `s` con secretKey sobre params ordenados.
  `customer/create` + `customer/register` (URL registro tarjeta),
  `subscription/create`, `payment/getStatus`, `subscription/get`.
- Webhook: `POST /api/pagos/flow/retorno` + urlConfirmation → verificar
  firma → actualizar estado + `periodoFin`.
- Front: botón Suscribirse → backend crea customer → redirect Flow →
  retorno → `getRegisterStatus` → `subscription/create`.
- Scheduler diario: `VENCIDA` + gracia (ej. 7 días) → `SUSPENDIDA`.
- Envs: `FLOW_API_KEY`, `FLOW_SECRET`, `FLOW_ENV=sandbox|prod`.

## Gates

- [ ] Cuenta Flow sandbox creada (acción usuario: registrarse en
      sandbox.flow.cl)
- [ ] Modelo `Plan`/`Suscripcion` + migración Flyway
- [ ] `FlowClient` + endpoint webhook con verificación de firma
- [ ] Flujo e2e en sandbox: suscribir → cobro → webhook → estado ACTIVA
- [ ] Suspensión por impago operativa
- [ ] **Boleta electrónica evaluada en paralelo** — el cliente pedirá
      boleta/factura, no tarjeta (ver `KPP - Boleta electrónica SII`)

## Condición de falsación

Si los primeros ~10 clientes pagan sin fricción por transferencia, la
integración puede postergarse; si la comisión de Flow erosiona el margen
con volumen, migrar a Oneclick (el dominio ya lo permite).
