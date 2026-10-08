---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: L
---
_Objetivo: controlar vencimientos de alimentos con lotes por producto y alertas preventivas._

- [ ] Tabla `lotes`: producto + sucursal + fecha de vencimiento + cantidad; nacen en entradas de stock/OC.
    
- [ ] FEFO al vender: descuenta del lote que vence primero.
    
- [ ] Alerta "vence en X días" en la campana del topbar + reporte de próximos a vencer.
    
- [ ] Merma por vencimiento como tipo de movimiento propio (trazable).
    
- [ ] Producto configurable: con/sin control de lote (accesorios no vencen).

**RIESGO** — modelo de stock se complica: saldo por sucursal × lote. Evaluar si el saldo por lote es derivado de movimientos o tabla aparte.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/lotes-vencimiento
```
