---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: M
---
_Objetivo: permitir la venta de alimentos a granel (sueltos, por kg) desde el POS._

- [ ] Catálogo: marcar producto como "a granel" y definir **valor por kg** (precio unitario por kilogramo).
    
- [ ] POS / interfaz de venta: al agregar un producto a granel, solicitar la **cantidad en kg** (acepta decimales, ej. 0,5 kg).
    
- [ ] Venta: **predecir/mostrar el valor final en vivo** según los kg ingresados (`total ítem = kg × valor por kg`), antes de confirmar.
    
- [ ] Backend: cantidades fraccionadas en `venta_items` y descuento de stock en kg (revisar si `movimientos_stock.cantidad` admite decimales o se migra a `numeric`).
    
- [ ] Comprobante/ticket: mostrar kg vendidos y valor por kg en el detalle del ítem.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/venta-a-granel
```
