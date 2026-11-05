---
tipo: proyecto
estado: produccion-interna
actualizado: 2026-11-05
tags: [uoh, angular, spring-boot, cruch, sitio-institucional]
---
# MOC — CABID (sitio institucional CRUCH)

Sitio institucional del CABID (CRUCH) desarrollado para la UOH — también sirve
como pieza de portafolio personal. En producción interna en el servidor
`cabid-uoh`.

## Navegación por necesidad

- **Quiero ver qué pasó** → `log.md` de esta carpeta
- **Quiero el resumen por sesión** → `registro_actividades.md`
- **Quiero el código** → `~/Escritorio/Desarrollo/cabid` (github.com/Nicolasmp92/cabid)
- **Quiero desplegar** → rsync + mvn package + npm build + restart systemd (ver log)

## Ficha

- **Stack:** Angular 22 SSR (Express 5) + Spring Boot + PostgreSQL + Tailwind 4
- **Server:** `ssh cabid` → 172.16.0.190, app en `/opt/cabid/app` (copia, no git),
  systemd `cabid-backend` + `cabid-frontend`, nginx :80 → front :4000 → proxy `/api` → :8080
- **Uploads:** `CABID_ARCHIVOS_DIR=/opt/cabid/uploads` en el server

## Pendientes destacados (detalle en log.md)

- Cutover DNS: `cabid.cl` aún apunta al sitio antiguo (198.12.239.238).
- Respaldo del dir `uploads` + tests de integración backend.
- Borrar rama remota `feat/iconos-material` (ya mergeada).
