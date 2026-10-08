---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: M
---
_Objetivo: entidad cliente asociable a ventas, con cuenta corriente para ventas a crédito (fiado)._

- [ ] Tabla `clientes`: nombre, teléfono/WhatsApp, correo, dirección; scoping por sucursal.
    
- [ ] Asociar cliente a la venta en el POS (opcional, buscador rápido).
    
- [ ] Cuenta corriente: venta a crédito, registro de abonos, saldo pendiente por cliente.
    
- [ ] Historial de compras del cliente.
    
- [ ] Estado de cuenta imprimible/compartible.
    
- [ ] Habilita: [[KPP - Ficha de mascota y recordatorio de recompra|ficha de mascota]], [[KPP - Canal online (catálogo público y pedidos)|canal online]].

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/clientes-fiado
```
