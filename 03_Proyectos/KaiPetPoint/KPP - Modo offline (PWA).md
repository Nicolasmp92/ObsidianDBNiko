---
status: Pendientes
proyecto: kaipetpoint
fase: fase-2
criticidad: media
esfuerzo: XL
---
_Objetivo: seguir vendiendo sin conexión y reconciliar al volver._

- [ ] PWA + cola de ventas local con reconciliación al recuperar red (diseño propuesto y diferido hasta estabilizar multi-sucursal).
    
- [ ] Catálogo cacheado para consulta sin conexión.
    
- [ ] Reglas de conflicto: qué pasa si el stock ya no alcanza al reconciliar.

**RIESGO** — reconciliación de stock offline multi-sucursal es complejidad al cuadrado; mantener postergado hasta que lo demás esté estable.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/offline-pwa
```
