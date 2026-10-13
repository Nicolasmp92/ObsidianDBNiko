---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: media-alta
esfuerzo: M
---
_Objetivo: cargar y operar el catálogo a escala — importación masiva, etiquetas y productos compuestos._

- [ ] Importación masiva CSV de productos (marca/categoría/precio/código de barras/stock inicial). El reporte de catálogo+stock existente sirve como plantilla. Clave para el onboarding de tiendas del SaaS.
    
- [ ] Etiquetas de precio imprimibles con código de barras (térmica/Zebra).
    
- [ ] Kits/packs: SKU compuesto que al venderse descuenta stock de sus componentes.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/catalogo-avanzado
```
