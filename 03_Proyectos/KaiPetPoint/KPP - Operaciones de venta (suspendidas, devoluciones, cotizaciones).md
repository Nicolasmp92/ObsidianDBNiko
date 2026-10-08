---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: media
esfuerzo: M
---
_Objetivo: cubrir los flujos de venta que hoy no existen más allá de cobrar y anular._

- [ ] Suspender venta: guardar carrito por usuario/sucursal y retomarlo después.
    
- [ ] Devolución/cambio: repone stock, anula ítem o venta parcial, trazada a la venta original (la anulación total ya existe).
    
- [ ] Cotización: documento sin descuento de stock, convertible a venta al aceptarse.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/operaciones-venta
```
