---
tipo: proyecto
proyecto: taskflow
estado: activo
actualizado: 2026-10-24
tags: [tareas, kanban, colaborativo, angular, spring-boot]
---
# ✅ MOC — TaskFlow

Tablero colaborativo de tareas para equipos chicos — "un Notion liviano":
tareas con prioridad, responsable, fecha límite y hilo de comentarios.
Repo: `~/Escritorio/Desarrollo/taskflow` ↔ `github.com/Nicolasmp92/taskflow`
(privado). Generado desde [[MOC - StarterCustomeKit|StarterCustomeKit v2]]
el 2026-10-20 (git archive + rebrand, mismo patrón que KaiPetPoint).

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero levantar el stack** → `backend: mvn spring-boot:run` (:8085) + `npm start` (:4205); login `nikolasmp92@gmail.com` / `niko9214`, o `colaborador@taskflow.dev` / `taskflow-demo-2026`
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Dominios (en `main`)

| Dominio | Entidades | Estado |
|---|---|---|
| Tareas | `tareas`, `tarea_comentarios` | Completo; tablero 3 columnas, asignación, comentarios |
| Plataforma | `usuarios`, JWT dual, preferencias/paletas | Heredado del kit; `SesionResponse` ganó `id` |

## Decisiones estructurales vigentes

- Nombre: `taskflow` (paquetes, BD, cookie `taskflow_token`, claves `taskflow.*`, env `TASKFLOW_*`). Display: TaskFlow.
- Colaboración plena: todo autenticado ve/edita todas las tareas; solo el creador o un admin elimina (`eliminable` calculado en el DTO).
- `/api/usuarios` expone id+nombre de activos para asignar; la administración sigue en `/api/admin/usuarios`.
- La campana del topbar se alimenta de `/api/tareas/resumen` (mis abiertas, vencidas primero) — dejó el placeholder del kit.
- Puertos: API `8085`, dev `4205`, SSR `4005`. BD `taskflow`/`taskflow_user` en PostgreSQL 18 (pendiente crear — mientras corre en H2).
