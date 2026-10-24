---
status: En curso
proyecto: kaipetpoint
fase: pmv
criticidad: critica
esfuerzo: L
---
_Objetivo: emitir boleta electrónica desde el POS — obligatoria para la venta formal en Chile._

- [x] Flujo interno DTE completo (mergeado a `main`, `420f11b`): emisión post-venta sin bloquear el cobro, cola con reintentos automáticos (5 intentos, scheduler 60 s), reintento manual admin, NC tipo 61 al anular, folio/timbre/estado en ticket e historial.
- [x] Bandeja de boletas (`f8020bc`): `/admin/boletas` lista pendientes/errores con reintento individual o en lote — las ventas nunca se pisan (documento único por venta).
- [x] Emisor configurable por sucursal (panel root → "Emisor DTE"): proveedor, RUT, razón social, giro, resolución SII; API key por nombre de env var (secreto nunca en BD).
- [x] Proveedor `simulado` funcional con folio correlativo — valida todo el flujo sin credenciales. El ticket impreso lo declara "SIMULADA — SIN VALIDEZ TRIBUTARIA".
- [ ] Ejecutar los trámites de [[Guia - Boleta electronica SII]]: firma electrónica, habilitación ante SII, CAF tipo 39.
- [ ] Formato completo de boleta real: **falta la dirección + comuna del emisor** en el encabezado (obligatoria) y la línea de **vuelto** en el ticket; el RUT del cliente aparece solo en el bloque de abono, no junto al nombre. Detectado revisando una boleta simulada impresa.
- [ ] Elegir proveedor real (SimpleAPI ~$15–30k/mes por emisor, Openfactura, o LibreDTE self-hosted) e implementar el bean `EmisorDte` correspondiente — la interfaz ya está, no se toca el dominio de ventas.
- [ ] Certificación ante SII con el proveedor elegido (ambiente de pruebas → producción).
- [ ] RCOF / reporte diario de boletas y folios de contingencia para caídas del SII.
- [ ] Multi-tienda: credenciales y folios **por tenant** — encaja en el panel de tiendas ([[KPP - SaaS multi-tienda y panel de tiendas]]); hoy el emisor es por sucursal, en SaaS sube un nivel.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/boleta-sii
```
