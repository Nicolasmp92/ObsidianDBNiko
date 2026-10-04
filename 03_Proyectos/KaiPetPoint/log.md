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
- **DECISIÓN** — Multi-sucursal se implementa con **BD única + `sucursal_id`** (no una BD por sucursal): catálogo compartido, stock por sucursal (`stock_sucursal`), rol `root` con panel de administración de sucursales. La BD-por-sucursal se descartó: migraciones N veces, agregación externa para consolidar, y ningún requisito de aislamiento lo justifica a esta escala.
- **DIFERIDO** — Boleta SII (guía de trámites en `Guia - Boleta electronica SII.md`; integración recomendada = API de terceros) y modo offline (propuesta: PWA + cola con reconciliación; postergado hasta que multi-sucursal esté estable — offline multi-sucursal es complejidad al cuadrado).
- **HECHO** — Semáforo de stock en el POS + campana real (`d70d1a2`): cada producto en Nueva venta muestra disponibilidad real (estante − carrito) con rojo/ámbar/verde (sin stock / bajo mínimo / normal) — el "+" opaco ahora tiene motivo visible. La campana del topbar dejó el placeholder: lista agotados primero luego bajo mínimo, badge con conteo, enlace a catálogo, se recarga al abrir.
- **HECHO** — Card "Menos vendidos — 30 días" en el Panel (`2712029`): `menosVendidos` en `/api/ventas/estadisticas` parte del catálogo activo (productos con 0 ventas = la alerta útil, una agregación sobre items nunca los vería). "sin ventas" en danger cuando unidades = 0. Grilla del panel → 3 columnas en desktop.
- **HECHO** — **Fix tooltip sidebar** (`c6ac8a3`): la directiva ya estaba cableada en compacto pero `DomPortal` de CDK 22 exige `parentNode` — lanzaba error silencioso por hover y *ningún* tooltip de la app se veía. Se ancla el nodo a `body` antes de adjuntar y se retira al ocultar. Spec de regresión (`tooltip.directive.spec.ts`) simula hover y verifica el overlay. **RIESGO** — SCK y Frunexis comparten la directiva rota; portar el fix junto al de SSR.

## 2026-10-04 — Multi-sucursal implementado (rama `feat/multisucursal`, `5b7e9f7`)

- **HECHO** — Migración V3 `sucursales`/`usuario_sucursal`/`stock_sucursal` + `sucursal_id` en ventas y movimientos. Todo lo existente se adscribe a "Casa matriz" (min(id) de sucursales); el primer admin queda `root`. `productos.stock`/`stock_minimo` se copian a `stock_sucursal` y se eliminan de `productos`.
- **HECHO** — `SucursalResolver`: cookie `kaipetpoint_sucursal` (web/SSR — el interceptor la reenvía gratis) > header `X-Sucursal-Id` (móvil) > primera permitida. El backend **siempre** valida membresía: cookie manipulada = 403. Root opera todas las activas y `JwtAuthFilter` le suma `ROLE_ADMIN` (hereda /api/admin/**).
- **HECHO** — Scoping total: ventas, historial, estadísticas, calendario, reportes CSV, movimientos, stock del catálogo y anulación van acotados a la sucursal activa. El chequeo de stock vive solo en `InventarioService.registrar` (el pre-check de VentasService se eliminó — duplicaba y raceaba).
- **HECHO** — Panel root `/api/root/sucursales` + `/root/sucursales` en el front: crear/editar sucursal, activar/desactivar y asignar equipo (membresía usuario↔sucursal). Al crear sucursal se siembra fila de stock por producto (saldo 0); usuario nuevo nace miembro de la sucursal activa del admin.
- **HECHO** — Selector de sucursal en el topbar (solo si hay >1; una sola se muestra como etiqueta). Cambiar sucursal = escribir cookie + **recarga completa** — los `httpResource` cachean por página y navegar no los invalida.
- **VERIFICADO en vivo** — Smoke multi-sucursal: crear suc2, venta sin stock en suc2 → 409, entrada +10 y venta → stock suc2=9 mientras suc1 intacta (16), historiales aislados, cajero nuevo solo ve Casa matriz, cajero con `X-Sucursal-Id: 2` → 403, cajero → `/api/root` → 403, root → `/api/admin/usuarios` → 200.
- **NOTA** — `mvn compile` · lint · 27/27 · build verdes. El cambio va en rama propia `feat/multisucursal` (regla: una rama por cambio); queda pendiente merge a main junto a `feat/estadisticas-dashboard`.
- **HECHO** — Delegación de rol `root` (`a643cac`): el selector de rol ofrece "Root" solo a usuarios root; el backend exige `ROLE_ROOT` para crear/editar/apagar/borrar cuentas root (cubría toma de control: un admin podía cambiarle la clave a un root) y bloquea quitar al último root activo. Smoke: admin→root = 403 en los 3 vectores; root→crear root = 201.
- **HECHO** — Ingreso rápido de stock desde el POS (`8819d61`): el `+` ya no bloquea — al topar stock insuficiente (lista, carrito o escáner) abre un panel que pide el **saldo real en estante**; `POST /api/inventario/ingreso-rapido` (cualquier autenticado) asienta la **diferencia** como `entrada` trazable al usuario. Solo suma: si declara menos de lo registrado → 400 apuntando al ajuste admin. Smoke: delta servidor (stockReal 7 sobre 5 → +2), user-role OK, 404 producto, FK impide borrar usuario con movimientos.
- **INCIDENTE** — `smoke-cookies.txt` (JWT de sesión de prueba) quedó en el commit `8819d61`; removido en `c68ed20` + `.gitignore`. El token sigue en el historial — JWT dev que expira solo; si se endurece, reescribir historia antes del merge a main.
- **HECHO** — Sistema de diálogos modales (`fb39a53`): CDK Dialog headless en toda la app. Piel única `.dialogo` en styles.css (un cambio = todos los modales). Formularios de usuarios/productos/categorías/marcas/sucursales y el ingreso rápido del POS pasan de secciones inline que empujaban el layout a `ng-template` + `dialog.open`; `window.confirm` reemplazado por `ConfirmarDialogoComponent` compartido + helper `confirmar()` (eliminar usuario, desactivar producto/categoría/marca, anular venta). Spec nuevo del diálogo; 28/28.
- **HECHO** — Boton X estandar en todos los dialogos (`e41c5f2`): componente `app-dialogo-x` compartido, × absoluta arriba a la derecha del marco `.dialogo`. Emite evento (DialogRef no es inyectable en dialogos por TemplateRef). Equivale a cancelar en confirmaciones. 28/28.
