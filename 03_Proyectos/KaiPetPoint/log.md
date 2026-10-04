---
tipo: log
proyecto: kaipetpoint
---
# 📓 Log — KaiPetPoint

Bitácora narrativa **append-only**: entradas nuevas al final. Tipos: **HECHO** / **DECISIÓN** / **HIPÓTESIS** / **RIESGO**. La bitácora técnica autoritativa vive en el repo.

---

## 2026-10-03 — Génesis desde SCK

- **DECISIÓN** — POS de tienda genérico generado desde StarterCustomeKit (patrón Frunexis: `git archive` + renombrado). Nombre inicial: Mostrador.
- **HECHO** — Dominio `items` reemplazado por tienda: catálogo (marcas/categorías/productos), `movimientos_stock`, `ventas`+`venta_items` transaccional. Seed Patitas (6 marcas, 4 categorías, 10 productos).
- **HECHO** — Smoke end-to-end: venta descuenta stock, movimientos con `venta_id`, anulación repone, 409 sin stock, 401 sin sesión. `mvn test` · lint · 22/22 · build verdes.
- **HECHO** — Repo publicado `Nicolasmp92/Mostrador` (privado) vía API GitHub.

## 2026-10-04 — Login estándar + comprobante + fix SSR + rename

- **HECHO** — Login estándar portado de SCK (`4353251`): recordar correo `kaipetpoint.recordar-correo`, toggle clave, mailto soporte, marca.
- **HECHO** — Comprobante post-cobro (`2d3c5d9`): al cobrar, boleta con #/fecha/vendedor/items/total del servidor + "Nueva venta" / "Ver ventas". Toast de éxito eliminado (redundante).
- **HECHO** — **Fix crítico SSR** (`b5cdfbe`): F5 cerraba sesión porque el guard corría en Node sin cookie. `ssrCookieInterceptor` reenvía la cookie a `/api/*` en SSR; `httpErrorInterceptor` solo actúa en navegador. Verificado: con cookie → 200, sin cookie → 302 /login.
- **DECISIÓN** — Rename **Mostrador → KaiPetPoint** (`d81f353`): marca del nicho mascotas. Renombrado integral: paquete Java, BD, cookie, claves `kaipetpoint.*`, env vars, repo GitHub. **RIESGO** — el nombre amarra al nicho; para reusar el POS en otra tienda habría que rebrandear (solo superficial).
- **RIESGO** — SCK y Frunexis comparten el bug de sesión en SSR (heredado del kit); pendiente portar el fix.

## 2026-10-04 — Estadísticas, calendario, tooltips y reportes

- **HECHO** — `GET /api/ventas/estadisticas` + dashboard rediseñado (`d7805d7`): ventas hoy, promedio, stock bajo, barras 7 días en CSS puro, top 5 productos 30 días. Solo ventas confirmadas.
- **HECHO** — Calendario mensual en `/ventas` (`373b4ff`, `c6d9e08`): `GET /api/ventas/calendario?desde&hasta` + `?fecha=` en el listado; punto de acento marca días con ventas; `LOCALE_ID='es'`.
- **HECHO** — "Ticket promedio" → "Promedio por venta" + iconos ⓘ con tooltips CSS accesibles (`bd96fb7`).
- **HECHO** — **Fix crítico inventario** (`4b97072`): los ajustes manuales grababan el movimiento pero NO movían el stock — el controller cargaba el producto detached y `setStock` nunca flusheaba. `em.merge()` re-adjunta dentro de la transacción. Ventas no lo padecían (entidad ya manejada).
- **DECISIÓN** — Reportes a Excel como **CSV con BOM UTF-8 + separador `;`** en vez de `.xlsx`: Excel es-CL lo abre directo, cero dependencias, una fila por ítem vendido = pivotable. Endpoint `GET /api/ventas/reporte?desde&hasta` + tarjeta de descarga con rango en el dashboard (`3b29079`).
- **HECHO** — Stock bajo simulado vía movimientos `ajuste` trazables ("Merma simulacion dev"): Cat Chow 4/5, Master Dog 3/6, Royal Canin Kitten 2/3 → tarjeta "Stock bajo" = 3.
- **HECHO** — Comprobante imprimible (`f21ea0b`): ruta `/ventas/:id/imprimir` **fuera del shell** (sin sidebar/topbar en el papel), formato ticket monocromo apto térmica/A4, marca "ANULADA" si aplica. Auto-abre el diálogo de impresión al cargar; entradas desde el detalle del historial y el comprobante post-cobro.
- **HECHO** — Escaneo de códigos de barras (`f14538e`, V2 `codigo_barras` único parcial): ① pistola USB (teclea+Enter en input del POS), ② cámara del equipo con **BarcodeDetector nativo** (sin deps; fallback manual si el navegador no soporta), ③ teléfono como escáner remoto vía buzón `/api/scan` en memoria por usuario (TTL 5 min, tope 50) — la caja drena con polling 2,5 s. Formulario de producto captura el código por cámara/pistola/"recibir del teléfono". **RIESGO** — cámara en LAN http exige contexto seguro: en teléfono requiere https o localhost; manual/HID siempre funcionan.
- **HECHO** — Buscador de venta por folio (`5f21719`): el N° impreso en el comprobante se busca directo en `/api/ventas/{id}` (independiente del top-100 del listado); resultado con detalle + Imprimir; 404 → toast "no existe".
- **HECHO** — Desglose IVA 19% (`84c61a7`): precios del catálogo **incluyen** IVA; `VentaResponse` lleva `neto`/`iva` calculados en servidor (`neto = total/1.19`, redondeo comercial). Desglosado en ticket impreso, comprobante post-cobro y columnas "Neto/IVA venta" del CSV.
- **HECHO** — Reportes múltiples (`6b03013`): la tarjeta del dashboard es ahora selector — Ventas por ítem (rango), Catálogo+stock con valor (instantáneo, autenticado) y Movimientos de inventario (rango, solo admin `/api/admin/reportes/movimientos`, mismo nivel que el endpoint de inventario). Helper `ReporteCsv` centraliza BOM+escape; el option admin se oculta a no-admins.
- **HECHO** — Filtro+orden en Inventario (`a8f1df9`): texto libre (producto/motivo/usuario/#venta), filtro por tipo de movimiento y orden por fecha/cantidad/producto — client-side sobre el top-100 del libro.
- **HECHO** — **Fix tooltip sidebar** (`c6ac8a3`): la directiva ya estaba cableada en compacto pero `DomPortal` de CDK 22 exige `parentNode` — lanzaba error silencioso por hover y *ningún* tooltip de la app se veía. Se ancla el nodo a `body` antes de adjuntar y se retira al ocultar. Spec de regresión (`tooltip.directive.spec.ts`) simula hover y verifica el overlay. **RIESGO** — SCK y Frunexis comparten la directiva rota; portar el fix junto al de SSR.
