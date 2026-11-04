---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: media
esfuerzo: S
---
_Objetivo: entregar al contador la información lista para el mes._

- [ ] Libro de ventas por período (reusa el helper `ReporteCsv` existente).
    
- [ ] Exportación de compras/OC cuando existan proveedores.
    
- [ ] Formato consumible por contador o importable a software contable.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/exportacion-contable
```
