---
status: Pendientes
proyecto: kaipetpoint
fase: fase-3
criticidad: media-alta
esfuerzo: M
---
_Objetivo: cobro con tarjeta/QR integrado al POS en vez de registrarlo a mano._

- [ ] Evaluar Flow / MercadoPago / WebPay: costos, API, QR en pantalla vs. terminal físico.
    
- [ ] Confirmación por webhook → la venta marca el medio de pago automáticamente.
    
- [ ] Multi-tienda: credenciales de pago **por tenant** (cada tienda cobra a su cuenta).

**RIESGO** — certificación y contratos por tienda; definir si el SaaS intermedia el pago o cada tenant usa sus credenciales.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/pagos-online
```
