---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: M
---
_Objetivo: gestionar proveedores y compras de reposición con recepción trazable a stock._

- [ ] Tabla `proveedores`: contacto, condiciones comerciales.
    
- [ ] Órdenes de compra: ítems + cantidades + costo unitario; estados borrador/enviada/recibida.
    
- [ ] Recepción (total o parcial) asienta `movimientos_stock` de entrada trazado a la OC.
    
- [ ] Precio costo en producto (actualizado por última compra) — habilita [[KPP - Analítica (márgenes, ABC, reposición)|márgenes]].
    
- [ ] Relación con lotes: la recepción puede capturar fecha de vencimiento ([[KPP - Lotes y fechas de vencimiento]]).

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/proveedores-oc
```
