---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: critica
esfuerzo: M
---
_Objetivo: registrar cómo se cobra cada venta y cuadrar la caja al cierre del turno._

- [ ] Medio de pago en la venta: efectivo (con **cálculo de vuelto**), tarjeta, transferencia, pago mixto; campo `medio_pago` en `ventas` + comprobante lo muestra.
    
- [ ] Apertura de caja: fondo inicial declarado + usuario/turno/sucursal.
    
- [ ] Movimientos de caja: retiros e ingresos manuales con motivo (trazables).
    
- [ ] Cierre con arqueo: esperado (fondo + ventas en efectivo − retiros) vs declarado, diferencia registrada.
    
- [ ] Resumen de turno para el dueño (ventas por medio de pago, diferencias).

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/caja-medios-pago
```
