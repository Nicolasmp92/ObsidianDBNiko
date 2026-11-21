---
tipo: proyecto
proyecto: rescuedatos
estado: activo
actualizado: 2026-11-21
tags: [recuperacion, datos, servicio, scripts, encargos]
---
# MOC — RescateDatos

Servicio recurrente: consolidar y ordenar datos rescatados de equipos dañados (SSD/note mojado, disco muerto, backup bruto). Se reciben carpetas con volcados de recuperación y se entrega UNA carpeta central organizada por tipo de archivo, con trazabilidad completa. Caso 1: Alejandra (2 SSDs de note mojado → `E:\Respaldo Ale`, 36.838 archivos).

## Navegación por necesidad

- **Quiero ver qué pasó** → `log.md` de esta carpeta
- **Quiero el resumen por sesión** → `registro_actividades.md`
- **Quiero cómo funciona el script** → [[RescateDatos - Script consolidar_respaldos]]
- **Quiero el código** → `scripts/consolidar_respaldos.py` (versionado en este vault)

## Ficha

- **Repo:** este vault (`03_Proyectos/RescateDatos/scripts/`)
- **Stack:** Python 3, stdlib only (os/shutil/hashlib/csv) — portable, cero deps
- **Entregable:** carpeta única `<Disco>:\Respaldo <Cliente>\` + `_log_movimientos.csv`

## Pipeline del servicio

1. **Triage**: identificar volcados vs carpetas de programas (junk: installs de AutoCAD/D5/Adobe, `Engine`, `Binaries`, dll/pyc masivos).
2. **Decidir con el cliente**: mover vs copiar · junk → `_Programas/` vs excluir · dedup por hash vs conservar todo.
3. **Ejecutar** `consolidar_respaldos.py` con `SRC_ROOTS`, `DST` y `JUNK` parametrizados al caso.
4. **Verificar**: conteo origen = destino, `leftover_files=0`, errores=0 en el log.

## Pendientes destacados (detalle en log.md)

- Dry-run mode (preview de categorías sin mover nada)
- Dedup global por hash (hoy solo colisiones de nombre+tamaño)
- Reporte resumen legible para entregar al cliente
