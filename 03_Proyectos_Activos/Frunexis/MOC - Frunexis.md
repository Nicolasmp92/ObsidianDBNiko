---
tipo: proyecto
proyecto: frunexis
estado: activo-v2-en-main
actualizado: 2026-10-02
tags: [agricola, contratos, temporadas, angular, spring-boot, portafolio]
---
# 🍒 MOC — Frunexis

Sistema de gestión agrícola: catálogo de especies/temporadas, trabajadores y contratos por temporada. Repo: `~/Escritorio/Desarrollo/Frunexis` (GitHub `Nicolasmp92/Frunexis`). Reconstruido sobre [[MOC - StarterCustomeKit|StarterCustomeKit v2]].

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero ver el modelo RBAC** → sección "Acceso" del `README.md` del repo
- **Quiero levantar el stack** → `backend: mvn spring-boot:run` (:8082) + `npm start` (:4202); login `admin@frunexis.dev` / `frunexis-admin-2026`
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Dominios (v2, en `main`)

| Dominio | Entidades | Estado |
|---|---|---|
| Catálogo | `species_families`, `species`, `seasons` | Completo; temporada vigente exclusiva |
| Personal | `workers`, `contracts` | Completo; hoja de vida 8 tabs, contratos drill-down temporadas→especies→lista |
| Acceso | `roles`, `permisos`, `rol_permisos`, `usuario_permisos` | RBAC granular, 38 permisos, 3 presets |
| Plataforma | `usuarios`, JWT dual | Heredado del kit |

## Decisiones estructurales vigentes

- **Agenda NO es de Frunexis**: era arrastre de la transición; ese concepto vive en `sconect` (proyecto futuro, Flutter).
- Placeholders honestos: los tabs de asistencia/disciplina/documentos/evaluaciones/notas/remuneraciones existen en la hoja de vida pero **sin persistencia** — son intención, no feature.
- Puertos: API `8082`, dev `4202`, SSR `4002` (DSpace-CRIS tiene reservado 8080/4200/4000).
- BD `frunexis`/`frunexis_user` en PostgreSQL; Hibernate `ddl-auto: update` en dev.
- Versión Laravel original preservada en tag `v1-laravel`.
