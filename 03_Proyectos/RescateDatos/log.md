---
tipo: log
proyecto: rescuedatos
---
# 📓 Log — RescateDatos

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

Repo: este vault — `03_Proyectos/RescateDatos/scripts/consolidar_respaldos.py`.
Stack: Python 3.13, stdlib only.

---

## 2026-11-21 — Proyecto nace del caso Alejandra

- **HECHO** — Encargo: consolidar `E:\respaldos ale 1` (16.032 archivos, 44 GB, volcado plano) y `E:\respaldos ale 2` (20.806 archivos, 42 GB, perfil de usuario: escritorio/documentos/descargas/imagenes) en una sola carpeta ordenada por tipo. Resultado: `E:\Respaldo Ale\` con 8 categorías + `_Programas`, 0 errores, 28 s de ejecución. Carpetas origen eliminadas tras quedar vacías.
- **DECISIÓN** — Criterios aprobados por el cliente para este caso (base del pipeline): **mover** (no copiar) dentro del mismo disco · junk de programas a `_Programas/` (separado, no borrado) · **dedup por contenido** (md5 solo cuando colisionan nombre+tamaño). Evidencia: respuestas en sesión.
- **DECISIÓN** — Preservar estructura relativa dentro de cada categoría (`Imagenes/FOTOS/202505_b/...`), no volcado plano — la organización original (fechas, proyectos) es información. Se aplana solo el primer nivel si es carpeta de perfil (`escritorio`, `documentos`…, ver `STRIP`).
- **HECHO** — Junk identificado por exploración previa, no por extensión: `D5 Render/` (install, 12k archivos), `escritorio/AutoCAD 2024/` (install + samples), `Autodesk Vehicle Tracking 2024/`, `documentos/Adobe/` (perfil Premiere). ~60% del volumen total era programa reinstalable.
- **HECHO** — Métricas caso 1: 9.824 archivos de usuario movidos + 27.127 a `_Programas`; 16 renombrados por colisión; **0 duplicados idénticos** (los dos SSDs tenían datos disjuntos). Documentos = 492 archivos / 20 GB (láminas PDF de hasta 1,9 GB).
- **RIESGO** — El dedup actual solo detecta duplicados con **mismo nombre y mismo tamaño**; dos copias del mismo archivo con nombres distintos se conservan ambas (seguro pero no ahorra espacio). Pendiente: modo dedup global.
- **RIESGO** — `STRIP` asume nombres de carpetas de perfil en español/inglés; un respaldo con estructura distinta (ej. `Users/Ale/Desktop`) dejaría el prefijo completo. Ajustar por caso.
- **DECISIÓN** — El script se versiona dentro del vault (no en repo satélite): es una herramienta interna del servicio, evoluciona con la documentación.
