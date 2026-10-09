---
status: Terminadas
proyecto: kaipetpoint
fase: pmv
criticidad: alta
esfuerzo: M
---
_Objetivo: permitir la venta de alimentos a granel (sueltos, por kg) desde el POS._

- [x] Catálogo: marcar producto como "a granel" y definir **valor por kg** (precio unitario por kilogramo).
    
- [x] POS / interfaz de venta: al agregar un producto a granel, solicitar la **cantidad en kg** (acepta decimales, ej. 0,5 kg).
    
- [x] Venta: **predecir/mostrar el valor final en vivo** según los kg ingresados (`total ítem = kg × valor por kg`), antes de confirmar.
    
- [x] Backend: cantidades fraccionadas en `venta_items` y descuento de stock en kg (revisar si `movimientos_stock.cantidad` admite decimales o se migra a `numeric`).
    
- [x] Comprobante/ticket: mostrar kg vendidos y valor por kg en el detalle del ítem.

---

## Implementado (2026-10-09, rama `feat/venta-a-granel`, commit `ac67372`)

- **Migración `V4__venta_a_granel.sql`**: `productos.a_granel BOOLEAN`; `venta_items.cantidad`, `movimientos_stock.cantidad`, `stock_sucursal.stock` y `stock_minimo` → `NUMERIC(12,3)` (precisión de gramos).
- **Backend**: `BigDecimal` en toda la cadena; granel admite ≤3 decimales, no-granel exige enteros (400 si no); stock insuficiente → 409; subtotal ítem = `precio × kg` redondeado a peso `HALF_UP`; movimientos manuales e ingreso rápido aceptan decimales en granel.
- **POS**: producto a granel abre diálogo de kg con **total estimado en vivo**; la línea del carrito muestra `X kg` (clic re-pesa); ingreso rápido de stock admite kg decimales.
- **Comprobante / historial / topbar / movimientos**: muestran `kg` y `$/kg` donde corresponde.
- **Tests**: `VentasServiceTest` (5 casos: granel fraccionado, 3 decimales, no-granel decimal rechazado, >3 decimales rechazado, cero rechazado) + spec POS (5 casos). 33/33 front + 6/6 backend verdes.
- **Smoke E2E en PostgreSQL real**: crear producto granel → entrada 20 kg → venta 0,5 kg = $1.995 servidor → stock 19,5 → anulación repone a 20 ✓.
