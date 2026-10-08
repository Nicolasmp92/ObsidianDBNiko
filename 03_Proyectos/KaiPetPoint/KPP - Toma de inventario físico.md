---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: media
esfuerzo: M
---
_Objetivo: conteo físico del estoque con cierre trazado como ajustes._

- [ ] Sesión de conteo por sucursal (total o por categoría/marca).
    
- [ ] Conteo ciego desde el teléfono (escáner de cámara ya existe vía BarcodeDetector).
    
- [ ] Cierre de sesión: diferencias asientan ajustes de `movimientos_stock` trazados a la sesión.
    
- [ ] Reporte de diferencias (faltantes/sobrantes) para el dueño.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/inventario-fisico
```
