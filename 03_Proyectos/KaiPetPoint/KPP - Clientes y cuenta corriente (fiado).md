---
status: Terminadas
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: M
---
_Objetivo: entidad cliente asociable a ventas, con cuenta corriente para ventas a crédito (fiado)._

- [x] Tabla `clientes`: nombre, teléfono/WhatsApp, correo, dirección; scoping por sucursal. (V7)
    
- [x] Asociar cliente a la venta en el POS (opcional, buscador rápido + alta rápida).
    
- [x] Cuenta corriente: venta a crédito (`fiado` en venta_pagos), registro de abonos, saldo derivado por cliente.
    
- [x] Historial de compras del cliente (últimas 50, en la ficha).
    
- [x] Estado de cuenta imprimible/compartible (`/clientes/:id/estado`).
    
- [ ] Habilita: [[KPP - Ficha de mascota y recordatorio de recompra|ficha de mascota]], [[KPP - Canal online (catálogo público y pedidos)|canal online]].

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/clientes-fiado
```
