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
- **HECHO** — Iconos de alerta en diálogos (`ae3b0cc`): `ConfirmarDialogo` deriva el icono del flag `peligroso` — triángulo rojo para acciones destructivas, icono info azul para confirmaciones neutras; el ingreso rápido del POS usa triángulo ámbar propio. 28/28.
- **HECHO** — Port del sistema de diálogos a **StarterCustomeKit** (`50891f6`, rama `feat/login-recordar`) y **Frunexis** (`4a3cd6d`, rama `feat/paletas-tema`): copiados `confirmar.dialog`, `dialogo-x`, piel `.dialogo` e iconos. SCK: usuarios + items-admin a modal. Frunexis: 6 páginas (familias, especies, temporadas, trabajadores, contratos, usuarios) — los 6 `confirm()` nativos eliminados; los `alert()` de error quedan pendientes para una fase posterior. lint/tests/build verdes en ambos.

## 2026-10-08 — Dirección SaaS y backlog nuevo

- **DECISIÓN** — KaiPetPoint será **SaaS multi-tienda**: el producto se arrienda a varias tiendas. El `root` actual evoluciona a super-admin de plataforma con panel para crear tiendas (nombre, logo, paleta, datos empresa). Misma regla estructural que multi-sucursal: BD única + `tienda_id` un nivel sobre `sucursal_id`. Tarea: [[KPP - SaaS multi-tienda y panel de tiendas]].
- **BACKLOG** — [[KPP - Venta de alimentos a granel]] (precio por kg + total estimado en vivo; revisar decimales en `movimientos_stock`) y [[KPP - Hosting y despliegue para pruebas]] (hay clientela esperando probar).
- **BACKLOG** — Lluvia de ideas general convertida en plan: [[KPP - Roadmap y priorización (PMV)]] prioriza todo el backlog por criticidad/viabilidad/esfuerzo en fases PMV → nicho/retención → SaaS; 19 tareas nuevas en el kanban.
- **HECHO** — Stack instalado en el equipo: repo clonado en `~/Escritorio/Desarrollo/kaipetpoint`, PostgreSQL 17 con BD `kaipetpoint`, backend :8084 + front :4204 corriendo, toda la suite verde.
- **HECHO** — Merge `feat/multisucursal` → `main` (incluía `feat/estadisticas-dashboard` completa; `comprobante-venta` y `login-recordar` ya estaban): Flyway V2+V3 aplicados, "Casa matriz" creada, admin → root. `main` pusheado — ya no hay trabajo feat pendiente de integrar.
- **HECHO** — Repaso responsivo móvil mergeado a `main` (fef3b6d + 79c6ccc): targets táctiles ≥44px, fix ">" suelto en login, kg en dashboard, marca oculta bajo sm. Acceso por WiFi verificado desde el celu.
- **HECHO** — Fallback ZXing para lector de cámara (d6614ee): Firefox/Safari/Samsung ahora leen códigos; BarcodeDetector sigue siendo el motor en Chromium. Ojo: la cámara exige HTTPS — sobre `http://10.56.64.124` el navegador la bloquea igual (workaround dev: flag de Chrome).
- **DECISIÓN** — Modelo comercial doble: SaaS arriendo (default) + licencia perpetua on-premise para quien pida comprar (pago único alto, sin fuente, updates cobradas). El on-premise es la válvula para clientes con necesidades divergentes. Política multi-tienda registrada en el roadmap: general→roadmap, nicho→cobrado+flag por tenant, divergente→no u on-premise.
- **HECHO** — Cotizaciones base de ambas modalidades: [[KPP - Cotización SaaS (arriendo mensual)]] ($19.990/mes base, $29.990 multi-sucursal, setup $99.990) y [[KPP - Cotización licencia perpetua on-premise]] ($1.490.000 licencia + $249.000 instalación + plan soporte $299.000/año). Borradores estimativos con términos y condiciones incluidos — ajustar antes de emitir a cliente real.
- **HECHO** — Caja, medios de pago y arqueo mergeado a `main` (fbc1103, V5): POS cobra efectivo (recibido/vuelto), tarjeta, transferencia o mixto con desglose `venta_pagos`; página `/caja` abre turno con fondo, registra retiros/ingresos y cierra con arqueo (esperado vs declarado). Arqueo por queries de suma, no colecciones lazy. Smoke E2E verde (doble apertura 409, insuficiente 400, diferencia −480).
- **HECHO** — Fix impresión de comprobante (24431d7): `window.print()` corría antes del render y capturaba "Cargando…"; ahora `afterRenderEffect` lo dispara con el ticket ya pintado.
- **HECHO** — Regla `.devin/rules/backend-bd-esquema.md`: esquema completo de la BD (13 tablas, V1–V5) con mandato — todo cambio al modelo exige migración Flyway + actualización de la regla en el mismo commit.

## 2026-10-09 — Sesión de pulido (post-caja)

- **HECHO** — Fix crítico de lecturas de ventas (`81e1e73` → merge `c3e6f34`): `VentaResponse.de` leía `pagos` LAZY fuera de sesión → todos los GET /api/ventas daban 500 (historial, detalle, comprobante). El "Cargando…" del ticket era esto, no el timing del print. `listar`/`porId` ahora en `@Transactional(readOnly)`; `anular` inicializa `pagos` dentro de su tx.
- **HECHO** — La venta exige turno de caja abierto (`1e81a09` → `4bd92b6`): `crear` valida sesión antes de persistir → 409 "La caja está cerrada: abre el turno". POS muestra banner con "Ir a Caja" y Cobrar deshabilitado. Smoke: sin turno 409, con turno venta 55 OK con vuelto.
- **HECHO** — Flujo del comprobante: "Volver" → "Nueva venta" (`ea2f016` → `90c7d40`); el usuario sigue vendiendo sin rodeos por el historial.
- **HECHO** — Historial honesto (`13bf29e` → `4d953eb`): `@empty` ya no confunde error de red con día sin ventas — mensaje de error en rojo, "Cargando…" y vacío son estados distintos.
- **HECHO** — Escáner integrado al POS (`104412e` → `3e4b723`): sale del menú; `/escaner` queda como escáner remoto (PC + teléfono) alcanzable desde el modo escáner de Nueva venta. En un solo equipo la cámara del POS agrega directo al carrito.
- **HECHO** — Catálogo unificado (`a48e756` → `0c89e00`): un ítem "Catálogo" con pestañas Productos/Marcas/Categorías; URLs hijas intactas; h1s redundantes fuera; íconos `marca`/`categoria`/`scan` limpiados.
- **HECHO** — Alta rápida de marca/categoría (`1b7c9db` → `f4c49ca`): opción "+ Nueva…" al final de cada select del producto abre mini-diálogo, crea y auto-selecciona.
- **HECHO** — Paleta en cierres (`a0bdff4` → `6473fc1`): × de modales, resultado de búsqueda y toasts pasan a `text-primary`/`bg-primary-soft`.
- **HECHO** — Tooltip no bloquea clicks (`6bfafde` → `d81bc87`): pane con `pointer-events-none` (se empujaba sobre el FAB y tragaba el primer tap → "demora" al abrir novedades) + posición de respaldo a la izquierda del host.
- **ESTADO** — Todo en `main` pusheado; suite verde (20/20 backend, 33/33 front, lint, build). Turno demo de caja abierto (fondo $20.000) en Casa matriz. Próximo PMV según kanban: clientes/fiado; pendiente hosting (HTTPS resuelve cámara) y la tarea OPS de clonar repos + esquemas BD.

## 2026-10-16 — Flujo DTE interno (boleta SII, fase 1)

- **DECISIÓN** — La integración SII se construye en dos fases: primero todo el flujo interno detrás de la interfaz `EmisorDte` con un proveedor **`simulado`** funcional (folio correlativo, timbre de juguete, estados); el conector real (SimpleAPI/Openfactura/LibreDTE) entra después como un bean nuevo sin tocar ventas. Motivo: los trámites SII (certificado, CAF tipo 39, habilitación) y la cuenta de proveedor aún no existen — no se puede certificar sin ellos, pero sí dejar lista toda la maquinaria.
- **DECISIÓN** — La venta **nunca se bloquea** por la emisión: el documento queda `pendiente` dentro de la misma transacción de la venta y se timbra en segundo plano (executor post-commit — intentar tx nueva dentro del callback de commit falla por contexto de sincronización muerto). Scheduler reintenta cada 60 s hasta 5 intentos → `error`; el admin puede reintentar manual desde el historial.
- **HECHO** — Rama `feat/boleta-sii` (`420f11b`): V8 (`sucursal_emisor` 1:1 + `documentos_dte` con tipos 39/61, folio, timbre, UQ parcial una boleta por venta), paquete `dte/` completo, `dte` en `VentaResponse`, endpoints `/api/admin/dte` (bandeja+reintento) y `/api/root/sucursales/{id}/emisor`. Anular una venta emite NC 61 referenciando la boleta. El ticket declara "SIMULADA — SIN VALIDEZ TRIBUTARIA" mientras el proveedor sea `simulado`.
- **HECHO** — Panel root: diálogo "Emisor DTE" por sucursal (proveedor, RUT, razón social, giro, resolución SII, nombre de env var con la API key — el secreto nunca se persiste). Badge de boleta en historial + estado en el comprobante post-cobro.
- **VERIFICADO** — Smoke E2E: venta 201 con DTE pendiente → emitido con folio y timbre; venta con emisor deshabilitado pasa igual y queda en cola; reintento manual emite; anulación genera NC 61. Tests 34/34 backend, 33/33 front, lint y build verdes. Casa matriz configurada con emisor simulado habilitado.
- **PENDIENTE** — Trámites SII (gratis): iniciación/confirmación de actividades, certificado digital, CAF tipo 39, certificación. Elegir proveedor real (~$15–30k/mes por emisor, lo paga el cliente-tienda en el modelo SaaS) o evaluar LibreDTE self-hosted. Merge de `feat/boleta-sii` a `main` pendiente de revisión.
- **HECHO** — Bandeja de boletas (`f8020bc`): `/admin/boletas` lista los documentos tributarios de la sucursal — filtro "Sin emitir" (pendiente+error), emitidas y todas, con venta/monto/vendedor y reintento individual o en lote. Los documentos no se pisan: cada venta tiene su boleta única.
- **HECHO** — Borrador persistente del POS (`f79a709`): la venta en curso se guarda en `localStorage` (ids + cantidades + cliente + pago) y se rehidrata contra el catálogo fresco tras una recarga. Causa probable del reporte: el live-reload de `ng serve` refrescó la página sobre un carrito sin persistencia.

## 2026-10-16 — RUT del cliente + cobro combinado de fiado

- **HECHO** — `feat/boleta-sii` mergeada a `main` (`420f11b`→`63dabf8`): flujo DTE + bandeja + borrador persistente + fixes.
- **HECHO** — RUT del cliente (`63dabf8`, V9): `clientes.rut` único por sucursal, validación módulo 11 server-side (`Rut.java` — DV malo → 400, duplicado → 409), normalización a `12.345.678-9`, buscable con o sin formato. Campo en listado, detalle y alta rápida del POS (buscar por RUT pre-llena el campo RUT, no el nombre).
- **HECHO** — Máscara de RUT (`52215e4`): directiva `appRut` filtra caracteres no-RUT, tope "999.999.999-K" (fin del tipeo infinito), auto-formato progresivo y borde rojo + `aria-invalid` cuando el DV no verifica. Rangos por tipo son heurística, no regla — no se rechazan. 17 tests nuevos (`shared/utils/rut.spec.ts`), espejo de `Rut.java`.
- **HECHO** — Seed de clientes (`a9f7f70`): 14 fichas Casa matriz + 2 Centro, RUTs reales con DV válido (empresa 76.x, DV-K), 3 escenarios de fiado (deuda completa, abono parcial, saldada). `asegurarRuts()` corre en cada arranque y asigna RUT sintético válido a cualquier ficha sin RUT — fichas legacy reparadas (0 sin RUT verificado).
- **HECHO** — Aviso de deudor en POS (`9cb2ced`): al elegir cliente con saldo salta toast "debe $X — cobrar" + chip enlaza a la ficha para abonar.
- **HECHO** — Cobro combinado (`2499fe2`, V10): el abono a la deuda va **junto a la venta** en una sola transacción — `venta_id` + `saldo_posterior` en `cliente_abonos`. El abono NO entra a la boleta (esa deuda ya tributó); el ticket declara "Abono cuenta corriente — nombre — RUT", medio, y deuda pendiente congelada en `saldo_posterior`. Recibido/vuelto cubren venta + abono. Probado por el usuario en vivo (venta 73: $24.470 + abono $1.780, deuda saldada).
- **HECHO** — Locale es-CL (`ab195f5`): el signo `$` va a la **izquierda** ("$9.990"); el locale `es` genérico lo dejaba a la derecha en toda la app.
- **DECISIÓN tributaria** — Cobrar fiado dentro de una boleta nueva tributaría IVA dos veces: el abono es registro `cliente_abonos` aparte de la venta, trazado a ella pero fuera del DTE. El comprobante transparenta el pago de deuda como respaldo del cliente.
- **PENDIENTE** — Boleta real: falta dirección+comuna del emisor en encabezado y línea de vuelto (detectado en boleta impresa). Trámites SII externos siguen pendientes (certificado, CAF, proveedor real).
- **ESTADO** — Todo en `main` pusheado; backend 42/42, front 50/50, lint y build verdes. Turno demo de caja abierto.
## 2026-10-24 — Stack Docker verificado end-to-end

- **HECHO** — Deploy stack completo en `main` (`14a6de8`): `backend/Dockerfile` (maven→jre-17), `Dockerfile` raíz (node:22-alpine, ng build→server.mjs), `docker-compose.yml` (postgres:16 + backend + frontend SSR + caddy:2 con healthchecks y redes internal/web), `Caddyfile` (`{$DOMAIN}`→frontend:4004; sin dominio sirve :80 por IP, con dominio HTTPS automático), `.env.example` con todas las vars.
- **HECHO** — Smoke real: `docker compose build`+`up` → Postgres fresco ejecuta migraciones V1–V15 + DataSeeder; `POST /api/auth/login` devuelve 200 con JWT y sucursales seed. Home redirige a /login (guard OK).
- **HECHO** — `http-proxy-middleware` movido a `dependencies`: `server.ts` lo usa en runtime y `npm ci --omit=dev` de la imagen prod lo excluía — habría roto el SSR recién en producción.
- **HECHO** — Rama `refactor/deuda-tecnica-pos` (v0.7.0: ofertas, despachos, cajón, retiro SII) estaba 3 commits sin pushear → respaldada a origin.
- **DECISIÓN** — Hosting objetivo: VPS ~US$5 (Hetzner/Contabo) con este compose + Caddy; alternativa $0: Oracle Always Free. Descartados free-tier por capas (cold starts matan la demo) y managed por capas (~US$20+, overkill).
- **RIESGO** — El `.env` de producción necesita secrets reales (JWT, DB, seed). Para demo pública falta: dominio, banner/etiqueta de demo, datos de ejemplo y reset periódico de la BD.

## 2026-10-24 (pm) — kpp.namp.cl en producción (Dokploy)

- **HECHO** — `https://kpp.namp.cl` 302 → `/login` con Let's Encrypt. Dokploy compose desde `main`: postgres + backend + frontend SSR (caddy quedó bajo `profiles: [standalone]` — Traefik ya ocupa 80/443 y enruta directo a `frontend:4004`). Env vars reales en Dokploy (DB, JWT, seed); login test → 401 correcto (seed clave propia, no la dev).
- **HECHO** — `allowedHosts` anti-SSRF del SSR de Angular exigía fix doble (`4e66bb9` + `3e27718`): agregar `namp.cl` y wildcard `*.namp.cl` — la sintaxis con punto (`.namp.cl`) **no** funciona; el matcher usa `startsWith("*.")` + `endsWith`. Verificado con `Host: kpp.namp.cl` local → 302.
- **NOTA** — El deploy vía webhook On Push gatilla pero no siempre recompila la imagen (24s); si un push no toma efecto usar **Rebuild** en Dokploy.
- **ESTADO** — namp.cl (sitio empresa, estático nginx) y kpp.namp.cl (POS, full stack) ambos en producción en el VPS Hostinger Brasil.

## 2026-10-26 — Bug: sesión perdida en recargas (producción)

- **HECHO** — Reproducido y corregido (`0e03791`): toda recarga completa mandaba a /login con cookie válida. Causa: SSR llamaba `/api/*` a la URL pública `http://` (Angular ignora `x-forwarded-proto`); el 301→https hacía que el fetch de Node descartara la cookie en el cambio de origen → guard anónimo. Afectaba cambio escritorio/mobile, F5, `cambiarSucursal` (location.assign) y retorno de suspensión del teléfono.
- **FIX** — `ssrCookieInterceptor` ahora apunta a `KAIPETPOINT_API_URL` (`http://backend:8084`, red interna) en SSR vía token `API_INTERNA` en `app.config.server.ts`. Test de regresión falla contra código viejo, pasa con el fix. Verificado en prod: SSR con cookie → 200; sin cookie → 302/login (guard sigue protegiendo).
- **NOTA** — Si otras páginas también usan recarga completa (location.assign) ya quedan cubiertas: la sesión sobrevive a cualquier render SSR.

## 2026-10-26 — Auditoría mobile 360px (headless CDP)

- **HECHO** — Método: Chrome headless + CDP (`/tmp/shot.mjs`) mide `scrollWidth` y lista elementos desbordados contra viewport 360, con cookie JWT firmada en VPS. `body { overflow-x: clip }` hacía que el desborde se viera como corte sin scroll.
- **CAUSA** — Grids con breakpoint-only (`grid lg:grid-cols-N`) dejan columna implícita `auto` → se dimensiona al max-content del ítem más ancho (dashboard: 7 barras × max-w-12 = 424px → página 423px; /ventas/nueva: 407px).
- **FIX** — `0e03791` (sesión), `b306d06` (dashboard: minmax(0,1fr) + min-w-0 en tarjetas + botón Nueva venta full-width en móvil), `bade949` (misma guarda en nueva-venta, sucursales, usuarios, perfil, productos, cliente-detalle, movimientos).
- **VERIFICADO en prod** — 360px: dashboard, /ventas/nueva, /ventas, /catalogo/productos, /login, /caja → `scrollWidth=360`, cero elementos desbordados.
- **PENDIENTE** — Auditar rutas restantes (despachos, clientes, inventario, ofertas, sucursales, perfil) y revisar UX táctil/tiempos, no solo overflow.

## 2026-10-26 — Topbar <=340px + carrito auditado

- **HECHO** — `/ventas/nueva` con carrito lleno (4 items, incl. a granel vía diálogo kg) a 360px: `scrollWidth=360`, sin desbordes — el desborde de "venta actual" era el mismo grid ya corregido en `bade949`.
- **FIX** — `0040eba`: a 320px el topbar desbordaba 15px (selector sucursal + 3 botones 44px). Toggle de tema oculto bajo `sm` (sigue en Perfil) + nombre de sucursal `max-w-24` en móvil. Verificado: 320 y 360 limpios en prod.
- **PENDIENTE** — Si la usuaria reporta de nuevo desborde en venta actual, pedir: modelo/ancho del teléfono y qué estado (¿con items? ¿con oferta? ¿diálogo abierto?).

## 2026-10-26 — Topbar sticky

- **HECHO** — `bcc278e` + `41e4e08`: topbar sticky para que el menú quede accesible al scrollear. Detalle fino: el sticky debía ir en el **host** `app-topbar` (`host.class`), no en el `<header>` interno — un sticky solo se mueve dentro de su padre, y el host medía lo mismo que la barra. z-30 < backdrop drawer z-40. Verificado en prod: scrollY 1264 → barra en top 0.

## 2026-10-26 — Eliminar sucursal como root
- HECHO: el panel root no tenia forma de eliminar sucursales (faltaba endpoint DELETE y boton; no era bug de permisos). Se agrego DELETE /api/root/sucursales/{id} + boton Eliminar con dialogo de confirmacion peligrosa (f4fbaf6).
- DECISIÓN: borrado fisico solo si la sucursal NO tiene historial (ventas, movimientos, despachos, caja, aperturas, clientes, abonos) → con historial responde 409 y se sugiere desactivarla. Stock/ofertas/zonas se borran explicito; membresias caen por cascade.
- HECHO: verificado en prod con JWT firmado en VPS — sucursal vacia se elimina (204), Casa matriz → 409 con detalle de bloqueos, 404 inexistente, 401 sin token. Dos errores encontrados en verificacion: queries a tablas DTE ya eliminadas por V15 (ffa9226) y stock_sucursal sin cascade (bc00d67).
- PENDIENTE: si la usuaria quiere eliminar una sucursal con ventas (ej. Patitas), no se podra — solo desactivarla. Evaluar si hace falta archivar/ocultar sucursales inactivas en selectores.
- HECHO: refinado el criterio — el listado expone `eliminable` por sucursal (misma logica de bloqueos del DELETE). Con historial el boton Eliminar queda deshabilitado (title explica) y solo se ofrece desactivar (09fb927). Verificado en prod: Casa matriz y Centro → false; Patitas (sin datos) → true.

## 2026-10-27 — Sesiones seguras + demo público + tour de primer uso
- HECHO: sesion JWT renovada a estandar de mercado — sliding 2h (renovacion transparente por actividad) + cap absoluto 12h desde el login real (claim `orig` preservado) + revocacion por version de sesion al cambiar clave (V16) + usuarios desactivados rechazados en cada request (98ea11f, fix constructor @Autowired 8e4e06f). Verificado en prod: V16 aplicada, backend sano.
- DECISIÓN: el link de KPP en el portafolio de namp.cl apunta a demo.namp.cl (no al admin real) — un prospecto jamas debe heredar una sesion abierta (544b090 en namp-ingenieria).
- HECHO: sandbox demo completo en el VPS — stack docker-compose.demo.yml propio (backend+postgres+frontend, volumen separado, /opt/kpp-demo), labels Traefik sobre dokploy-network. Publico: https://demo.namp.cl. Endpoint publico /api/demo/config expone credenciales demo@kaipetpoint.cl (14473fd + labels 694593e).
- HECHO: UI demo — tarjeta de credenciales + boton "Entrar con la cuenta demo" en login; banner MODO DEMO con aviso de reinicio nocturno en el shell. DemoGuard bloquea mutaciones de cuenta/usuarios en modo demo. DemoResetService resetea la BD a las 04:00.
- HECHO: tour de bienvenida de primer uso (fase 3) — V17 usuarios.tutorial_completado, PUT /api/perfil/tutorial, TourService+TourComponent propios (overlay+spotlight por data-tour, fallback centrado, Escape=omitir, 5 pasos). Se muestra una sola vez por usuario (de08ba0). Lint+62 tests front+47 backend verdes.
- PENDIENTE: verificar en prod que el tour aparece tras login con flag false; comprobar que el reset nocturno del demo corre a las 04:00; revisar cobertura completa de DemoGuard.
- PENDIENTE: notificaciones por correo (creacion de usuario, cambio de clave) diferidas hasta generar ingresos — Resend gratis + DNS en Cloudflare cuando toque; el dueno centraliza las cuentas de correo.
- RIESGO: al resincronizar el codigo al VPS con rsync se copio el .env local de desarrollo (con credenciales personales reales) sobre el .env del demo → /api/demo/config expuso brevemente correo+clave personales al publico. Resuelto: .env del VPS reescrito solo con credenciales demo y volumen postgres recreado. Leccion: excluir .env del rsync y NUNCA usar claves reales en .env locales. Si esa clave se reutiliza en otro servicio, rotarla.
- HECHO: verificado en prod — V17 tutorial aplicada, backend reiniciado limpio, demo.namp.cl sano con credenciales correctas y tutorialCompletado:false (el prospecto vera el tour al entrar).
- HECHO: tour omite el paso de sucursal cuando el usuario tiene una sola — el selector del topbar no existe para ellos, el paso era ruido (9fd9353).
- DECISIÓN: el tour orienta por interfaz, no por negocio — pasos: barra superior (accesos), menú lateral (navegacion+☰), zona de contenido, perfil al pie del menú. Se eliminan anchors por entidad (sucursal, ventas, caja); lo estructural no se explica, se descubre usandolo (97aa6be).
- HECHO: acuse demo obligatorio — modal con icono de alerta que el prospecto debe confirmar ("Entendido") por sesion de navegador; el banner estatico no se leia. En demo el tour ahora sale en CADA ingreso sin persistir el flag (5ccc0c2).
- HECHO: fix contraste en tabs del catalogo — el texto activo quedaba ilegible porque routerLinkActive=text-surface perdia contra text-text-muted por orden del CSS; ahora binding condicional (5ccc0c2).
- DECISIÓN: el acuse demo tampoco persiste — el sandbox lo visitan personas distintas, persistirlo supone que quien confirma es quien entra despues. Vive solo en memoria y se rearma en cada login/carga (dc18d21).
