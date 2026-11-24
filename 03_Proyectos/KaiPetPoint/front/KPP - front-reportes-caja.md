---
tipo: documentacion-tecnica
proyecto: kaipetpoint
actualizado: 2026-11-24
tags: [front, reportes, caja, csv, regla-docs-first]
---

# KPP — Reportes descargables (Dashboard + Caja)

Spec viva del módulo de reportes CSV. Regla madre: [[Docs-first - estructura antes de construir]].

## Contrato

Descargas CSV (Excel es-CL: separador `;`, BOM UTF-8) generadas en servidor.

| Reporte | Endpoint | Rango | Rol |
|---|---|---|---|
| Ventas — detalle por ítem | `GET /api/ventas/reporte?desde&hasta` | sí | autenticado |
| Catálogo y stock actual | `GET /api/reportes/productos` | no | autenticado |
| Movimientos de inventario | `GET /api/admin/reportes/movimientos?desde&hasta` | sí | admin |

`desde`/`hasta` son `LocalDate` ISO — la granularidad es el **día completo**,
no el turno. Un turno que cruza medianoche descarga ambos días.

## Puntos de entrada

- **Dashboard** (`dashboard.page.ts`): sección «Reportes» con selector de tipo,
  fechas desde/hasta (default: mes en curso → hoy) y botón «Descargar para Excel».
- **Caja** (`caja.page.ts`):
  - Turno abierto: botón a ancho completo «Descargar ventas de hoy en Excel»
    en la tarjeta del turno — rango día de apertura → hoy (un turno olvidado
    abierto ayer trae ambos días).
  - Historial «Turnos recientes»: dentro del detalle expandido de cada turno,
    botón «Descargar ventas del dd-MM en Excel» (o «dd-MM → dd-MM» si cruza
    medianoche). Rango = día de apertura → día de cierre (o hoy si sigue abierto).
  - Etiqueta honesta: el CSV cubre **todas las ventas del día** en la sucursal,
    no solo las del turno (dos turnos el mismo día comparten reporte).

## Layout de Caja (2026-11-24)

La fila superior de Caja es `grid lg:grid-cols-2` (`items-start`): la tarjeta
de estado («Caja cerrada» o «Turno abierto», según corresponda) a la izquierda
y «Cajón de dinero» a la derecha — antes la apertura quedaba angosta centrada
y el cajón a lo ancho. En móvil/tablet apilan (mobile-first). Movimientos
manuales y cierre con arqueo siguen a lo ancho debajo de la grilla.

## Piezas compartidas

- `shared/utils/descarga.ts`
  - `isoLocal(d: Date): string` — YYYY-MM-DD en hora local (toISOString corre
    el día hacia atrás por UTC). Antes vivía duplicada en dashboard.
  - `descargarArchivo(blob: Blob, nombre: string): void` — objectURL + anchor
    sintético + revoke. Browser-only: se llama desde click, nunca en SSR.

## Estados

- `descargando`: deshabilita el botón y cambia el texto a «Generando…».
  En historial se deshabilita solo el botón del turno en curso (por `s.id`).
- Error HTTP: toast «No se pudo generar el reporte.»
- Sin validación de rango en Caja (las fechas vienen del turno, no del usuario).

## Reuso y no-reuso

- Reusado: endpoint existente `api/ventas/reporte` (cero backend nuevo),
  patrón de descarga del dashboard extraído a `shared/utils`.
- No reusado: `importar-productos.parser.ts` (parseo CSV de entrada,
  dirección opuesta). `ReporteCsv.java` es del lado servidor.
- Decisión: extraer util a los **2** call sites (dashboard + caja) y no antes —
  el patrón ya demostró que viaja entre features.

## Verificación

- `descarga.spec.ts`: formato `isoLocal` (padding, medianoche local) y
  `descargarArchivo` (anchor con nombre, revoke llamado) bajo jsdom.
- Regresión dashboard: mismo flujo de descarga tras el refactor.
- 360 px: botones `h-11`/touch ≥44 px en ambas tarjetas.
