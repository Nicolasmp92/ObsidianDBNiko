---
tipo: proyecto
proyecto: isomanager
estado: activo
actualizado: 2026-10-25
tags: [iso, cumplimiento, normas, angular, spring-boot, namp]
---
# ✅ MOC — ISO Manager

Sistema de gestión de cumplimiento normativo (SGC) para empresas
certificadas o en proceso: matriz requisito → estado con responsable,
fecha objetivo, evidencia e hilo de comentarios.
Repo: `~/Escritorio/Desarrollo/isomanager` ↔ `github.com/Nicolasmp92/isomanager`
(privado). Generado desde [[MOC - StarterCustomeKit|StarterCustomeKit v2]]
el 2026-10-24 (git archive + rebrand, mismo patrón que TaskFlow/KaiPetPoint).
Producto del paraguas [[MOC - NAMP|NAMP]] — idea origen en
[[Ideas#ISO Manager|Empresa/Ideas.md]] (2026-10-22), adelantada respecto
del plan original (post-F3) por decisión del usuario.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero levantar el stack** → `backend: mvn spring-boot:run` (:8086) + `npm start` (:4206); login `nikolasmp92@gmail.com` / `niko9214`, o `colaborador@isomanager.dev` / `isomanager-demo-2026`
- **Modo H2 sin PostgreSQL** → `ISOMANAGER_DB_URL='jdbc:h2:mem:isomanager;DB_CLOSE_DELAY=-1'` (sin el flag la BD se vacía tras suspender — lección TaskFlow)

## Dominios (en `main`)

| Dominio | Entidades | Estado |
|---|---|---|
| Cumplimiento | `normas`, `requisitos`, `cumplimientos`, `cumplimiento_comentarios` | Completo: matriz fija 1:1, 4 estados, evidencia, hilo |
| Plataforma | `usuarios`, JWT dual, preferencias/paletas | Heredado del kit; `SesionResponse` ganó `id` |

## Catálogo sembrado

ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018 · ISO 27001:2022 —
~66 cláusulas clave del esquema HLS/Anexo SL en `seed/requisitos.json`.

## Decisiones estructurales vigentes

- Nombre: `isomanager` (paquetes, BD, cookie `isomanager_token`, claves `isomanager.*`, env `ISOMANAGER_*`). Display: ISO Manager.
- **La matriz es fija**: una fila de `cumplimientos` por `requisito` (1:1 vía UNIQUE). Sin alta ni baja por API — se actualiza estado/responsable/fecha/evidencia. La norma ES la matriz.
- Estados: `pendiente` → `en_proceso` → `cumple` + `no_conforme` (abierto = todo lo que no es `cumple`).
- `requisitos.orden` numérico: el orden alfabético de `clausula` pondría 4.10 antes que 4.2.
- `/api/usuarios` expone id+nombre de activos para asignar responsables; administración sigue en `/api/admin/usuarios`.
- Colaboración plena: todo autenticado actualiza cualquier fila y comenta (igual que TaskFlow — sin permisos por fila en el MVP).
- Campana del topbar alimentada por `/api/cumplimientos/resumen` (mis abiertos, vencidos primero).
- Puertos: API `8086`, dev `4206`, SSR `4006`. BD `isomanager`/`isomanager_user` en PostgreSQL (pendiente crear — mientras corre en H2).

## PMV pendiente (del documento de la idea)

Matriz de cumplimientos ✅ (v0.1.0). Siguientes módulos en backlog:
documentos controlados con versionado, auditorías internas + no
conformidades con acciones correctivas, indicadores con alertas,
capacitaciones y obligaciones legales.
