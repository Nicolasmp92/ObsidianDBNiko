---
tipo: plan
proyecto: kaipetpoint
actualizado: 2026-10-08
---
# 🗺️ Roadmap — KaiPetPoint

Todo el backlog priorizado por **criticidad** (¿bloquea operar o cobrar?), **viabilidad** (¿qué tan directo con el stack actual: patrones existentes vs. integración externa/hardware?) y **esfuerzo** (S/M/L/XL). La fase indica cuándo conviene atacarlo.

## Criterios

- **PMV**: lo mínimo para que una tienda real opere y cobre con confianza. El orden de la tabla es el orden sugerido de ataque.
- **Fase 2**: valor de nicho mascotas y retención; exige PMV estable.
- **Fase 3**: escala SaaS e integraciones externas.

## PMV — operación real

| # | Tarea | Criticidad | Viabilidad | Esfuerzo | Nota |
|---|---|---|---|---|---|
| 1 | [[KPP - Hosting y despliegue para pruebas]] | Crítica | Alta | M | Sin esto no hay pruebas con clientela |
| 2 | [[KPP - Caja, medios de pago y arqueo]] | Crítica | Alta | M | Cobrar y cuadrar caja es lo mínimo operable |
| 3 | [[KPP - Venta de alimentos a granel]] | Alta | Media | M | Pedido explícito; revisar decimales en stock |
| 4 | [[KPP - Clientes y cuenta corriente (fiado)]] | Alta | Alta | M | Base para fiado, historial, mascotas y recompra |
| 5 | [[KPP - Lotes y fechas de vencimiento]] | Alta | Media | L | Los alimentos vencen; modelo stock×sucursal×lote |
| 6 | [[KPP - Proveedores y órdenes de compra]] | Alta | Alta | M | Reposición real + precio costo (habilita márgenes) |
| 7 | [[KPP - Catálogo avanzado (importación CSV, etiquetas, kits)]] | Media-Alta | Alta | M | CSV es clave para el onboarding de tiendas |
| 8 | [[KPP - Promociones y descuentos]] | Media | Alta | M | Descuento trazado por usuario |
| 9 | [[KPP - Operaciones de venta (suspendidas, devoluciones, cotizaciones)]] | Media | Alta | M | |
| 10 | [[KPP - Boleta electrónica SII]] | Crítica | Media | L | Obligatoria para venta formal en CL; depende de trámites + API de terceros |

## Fase 2 — nicho y retención

| Tarea | Criticidad | Viabilidad | Esfuerzo | Nota |
|---|---|---|---|---|
| [[KPP - Analítica (márgenes, ABC, reposición)]] | Alta | Alta | M | Depende de precio costo (OC) |
| [[KPP - Ficha de mascota y recordatorio de recompra]] | Alta | Media-Alta | M | Diferenciador del nicho; depende de Clientes |
| [[KPP - Toma de inventario físico]] | Media | Media | M | Conteo ciego desde teléfono |
| [[KPP - Servicios y agenda (peluquería, baño)]] | Media | Media | M | Ítems sin stock + agenda |
| [[KPP - Balanza integrada para venta a granel]] | Media | Media | M | Requiere hardware de prueba |
| [[KPP - Comisiones por vendedor y notificaciones push]] | Media | Media | M | |
| [[KPP - Exportación contable]] | Media | Alta | S | |
| [[KPP - Modo offline (PWA)]] | Media | Baja-Media | XL | Postergado hasta estabilizar multi-sucursal |

## Fase 3 — SaaS e integraciones

| Tarea | Criticidad | Viabilidad | Esfuerzo | Nota |
|---|---|---|---|---|
| [[KPP - SaaS multi-tienda y panel de tiendas]] | Crítica (negocio) | Media | XL | `tienda_id` sobre `sucursal_id`; branding por tenant |
| [[KPP - Canal online (catálogo público y pedidos)]] | Alta | Media | L | Argumento de venta fuerte para el SaaS |
| [[KPP - Pagos online integrados]] | Media-Alta | Media | M | Credenciales por tenant en multi-tienda |
| [[KPP - Integración WhatsApp Business]] | Alta | Media | M | MVP con wa.me, luego API oficial Meta |

## Dependencias

- **Clientes** habilita: fiado, ficha de mascota, recompra, canal online.
- **Venta a granel** habilita: balanza integrada.
- **Precio costo (OC)** habilita: márgenes y analítica de rentabilidad.
- **Multi-sucursal estable** habilita: modo offline (riesgo de reconciliación al cuadrado).
- **Multi-tienda** afecta: credenciales SII/pagos/branding por tenant — conviene decidir el modelo antes de integrar SII.
