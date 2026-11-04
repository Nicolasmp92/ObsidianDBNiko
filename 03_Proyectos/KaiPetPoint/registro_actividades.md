---
tipo: registro
proyecto: kaipetpoint
---
# 📋 Registro de actividades — KaiPetPoint

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-10-03 | Génesis desde SCK: dominio tienda completo, seed Patitas, puertos 8084/4204/4004 | `3409f65` + smoke |
| 2026-10-03 | Repo publicado `Nicolasmp92/Mostrador` (privado) | push `main` |
| 2026-10-04 | Login estándar (recordar correo, toggle clave, marca) | `4353251` |
| 2026-10-04 | Comprobante post-cobro + acceso directo a historial | `2d3c5d9` |
| 2026-10-04 | Fix sesión SSR: cookie reenviada en render servidor | `b5cdfbe` + curl 200/302 |
| 2026-10-04 | Rename integral Mostrador→KaiPetPoint (código, BD, repo, env) | `d81f353` + verificación verde |
| 2026-10-04 | Carpeta de proyecto creada en `03_Proyectos/` del vault | esta nota |
| 2026-10-04 | Estadísticas dashboard: endpoint agregado + tarjetas/gráfico CSS | `d7805d7` |
| 2026-10-04 | Calendario mensual de ventas + filtro por día + indicador | `373b4ff`, `c6d9e08` |
| 2026-10-04 | Tooltips ⓘ accesibles + "Promedio por venta" | `bd96fb7` |
| 2026-10-04 | Fix: ajustes manuales de inventario no persistían stock | `4b97072` |
| 2026-10-04 | Reporte CSV para Excel (`/api/ventas/reporte`) + descarga en dashboard | `3b29079` |
| 2026-10-04 | Comprobante imprimible en ticket (`/ventas/:id/imprimir`) | `f21ea0b` |
| 2026-10-04 | Escaneo: pistola USB, cámara nativa y teléfono remoto (`/api/scan`) + V2 codigo_barras | `f14538e` |
| 2026-10-04 | Buscador de venta por folio + imprimir desde resultado | `5f21719` |
| 2026-10-04 | Desglose IVA 19% en comprobantes y CSV | `84c61a7` |
| 2026-10-04 | Reportes: selector ventas/catálogo/movimientos en dashboard | `6b03013` |
| 2026-10-04 | Inventario: filtro por tipo/texto + ordenamiento del libro | `a8f1df9` |
| 2026-10-04 | Fix tooltip: DomPortal sin parentNode nunca renderizaba | `c6ac8a3` + spec |
| 2026-10-04 | Dashboard: card "Menos vendidos" (incluye productos con 0 ventas) | `2712029` |
| 2026-10-04 | Semáforo de stock en POS + alertas reales en campana topbar | `d70d1a2` 25/25 |
| 2026-10-04 | Multi-sucursal: V3, stock por tienda, panel root, selector en topbar | `5b7e9f7` en `feat/multisucursal` + smoke 2 sucursales |
| 2026-10-04 | Delegación de rol root entre roots + protección de último root | `a643cac` |
| 2026-10-04 | Ingreso rapido de stock en POS (saldo real -> entrada trazable) | `8819d61` + revert `c68ed20` |
| 2026-10-04 | Sistema de dialogos modales CDK (formularios + confirmaciones) | `fb39a53` 28/28 |
| 2026-10-04 | Boton X de cierre estandar en todos los dialogos | `e41c5f2` |
| 2026-10-04 | Iconos de alerta en dialogos (triangulo rojo peligroso / info azul neutro) | `ae3b0cc` 28/28 |
| 2026-10-16 | Flujo DTE interno: V8 + EmisorDte simulado + cola reintentos + NC 61 | `420f11b` en `feat/boleta-sii` + smoke E2E |
| 2026-10-16 | Bandeja de boletas `/admin/boletas` — no emitidas + reintento lote | `f8020bc` |
| 2026-10-16 | Borrador persistente del POS (localStorage, rehidrata vs catálogo fresco) | `f79a709` |
| 2026-10-16 | RUT del cliente: módulo 11, único por sucursal, buscable (V9) | `63dabf8` + smoke |
| 2026-10-16 | Máscara de RUT en vivo: filtra, acota, verifica DV | `52215e4` 50/50 |
| 2026-10-16 | Seed de clientes con RUTs válidos + fiado demo + reparación legacy | `a9f7f70`, `9cb2ced` |
| 2026-10-16 | Cobro combinado venta+abono fiado (V10, ticket transparenta deudor) | `2499fe2` 42/42 + venta 73 en vivo |
| 2026-10-16 | Locale es-CL — signo $ a la izquierda en toda la app | `ab195f5` |
| 2026-10-24 | Stack Docker VPS-ready: Dockerfiles + compose (pg/backend/SSR/caddy) + Caddyfile; smoke end-to-end OK (login 200 + seed) | `14a6de8` en `main` |
| 2026-10-24 | Rama `refactor/deuda-tecnica-pos` (v0.7.0) respaldada a origin (estaba 3 commits sin pushear) | `741970d` |
| 2026-10-24 | kpp.namp.cl en producción (Dokploy compose main, Traefik + LE); fix allowedHosts `*.namp.cl` | `3e27718` + `4e66bb9` |
