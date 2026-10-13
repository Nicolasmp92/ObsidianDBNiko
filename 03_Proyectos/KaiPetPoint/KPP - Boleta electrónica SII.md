---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: critica
esfuerzo: L
---
_Objetivo: emitir boleta electrónica desde el POS — obligatoria para la venta formal en Chile._

- [ ] Ejecutar los trámites de [[Guia - Boleta electronica SII]]: firma electrónica, habilitación ante SII.
    
- [ ] Integración vía API de terceros (decisión ya tomada en la guía).
    
- [ ] Emisión automática al cobrar + reimpresión desde el historial.
    
- [ ] Multi-tienda: credenciales y folios **por tenant** — encaja en el panel de tiendas ([[KPP - SaaS multi-tienda y panel de tiendas]]); decidir el modelo antes de integrar.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/boleta-sii
```
