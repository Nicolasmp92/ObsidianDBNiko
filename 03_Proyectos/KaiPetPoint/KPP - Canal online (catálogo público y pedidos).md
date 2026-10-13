---
status: Pendientes
proyecto: kaipetpoint
fase: fase-3
criticidad: alta
esfuerzo: L
---
_Objetivo: cada tienda tiene vitrina web con pedidos de retiro — argumento de venta del SaaS._

- [ ] Catálogo público sin login (ruta pública o subdominio por tienda) con stock visible.
    
- [ ] Pedido online → retiro en tienda: llega como venta pendiente de confirmar en el POS.
    
- [ ] Datos de contacto del pedido → clientes (si existe [[KPP - Clientes y cuenta corriente (fiado)|CRM]]).
    
- [ ] Depende de: [[KPP - SaaS multi-tienda y panel de tiendas]] para aislamiento por tienda.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/canal-online
```
