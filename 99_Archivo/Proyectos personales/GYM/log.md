---
tipo: log
proyecto: gym
---
# 📓 Log — GYM

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

---

## 2026-05-04 — Fixes de UI (batch 1)

- **HECHO** — Corregido: al volver del detalle del ejercicio se perdía la función de filtros (todos/activos/desactivados).
- **HECHO** — Etiquetas de edición generadas en textbox de exercicesdetails.

## 2026-05-05 — Fixes de UI (batch 2)

- **HECHO** — Switch bajado al costado del título + responsividad con título largo.
- **HECHO** — Botón de editar implementado con su vista.

## 2026-05-07 — Sesión admin

- **HECHO** — Cierre de sesión para el módulo de admin.

## 2026-05-13 — Crear rutinas

- **HECHO** — Pantalla Crear Rutinas.

## 2026-05-15 → 2026-05-26 — Roadmap pasos 1–5

- **HECHO** — Paso 1: control de permisos y limpieza de UI (2026-05-15).
- **HECHO** — Paso 2: infraestructura de datos / backend core (2026-05-15).
- **HECHO** — Paso 3: constructor de rutinas, admin UX (2026-05-19).
- **HECHO** — Paso 4: ejecución y tracking, user experience (2026-05-21).
- **HECHO** — Paso 5: gestión granular y edición de rutinas (2026-05-26).

## Pendientes abiertos

- **HIPÓTESIS** — Bug "filtros de activo/inactivo no funcionan": pendiente verificar si quedó resuelto con el fix de filtros del 2026-05-04.
- Paso 6: modo entrenamiento activo y pausa.
- Paso 7: temporizador de descanso inteligente.
