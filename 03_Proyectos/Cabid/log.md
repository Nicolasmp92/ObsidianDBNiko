# Log — CABID (sitio institucional CRUCH)

Bitácora append-only. Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO.

Repo: `~/Escritorio/Desarrollo/cabid` (github.com/Nicolasmp92/cabid).
Stack: Angular 22 SSR (Express 5) + Spring Boot + PostgreSQL + Tailwind 4.
Server: `ssh cabid` → 172.16.0.190 (cabid-uoh), app en `/opt/cabid/app` (copia, no git), systemd `cabid-backend` + `cabid-frontend`, nginx :80 → front :4000 → proxy `/api` → :8080.

## 2026-10-15

- **HECHO** — Iconos Material autoalojados mergeados a main (`5a871cf`→`c456f01`), woff2 local, sin Google Fonts.
- **HECHO** — Directiva: vicepresidencia vacante con "Por definir" y tarjetas preparadas para foto (`foto` opcional, avatar circular, iniciales de respaldo) — `0866412`.
- **HECHO** — Subida real de imágenes (`008cec1`): `POST /api/admin/archivos` multipart (JPG/PNG/WebP/GIF ≤5MB, nombre UUID) + `GET /api/archivos/{nombre}` público; dir `CABID_ARCHIVOS_DIR=/opt/cabid/uploads` en el server. Forms de evento y noticia con botón "Subir imagen" + preview.
- **HECHO** — Enlaces de eventos tipados y múltiples (`b26265c`): `urlInscripcion`/`urlInfo`/`urlSitio`; filas progresivas en el form (completar una habilita la siguiente con los tipos restantes); público muestra un botón por enlace con etiqueta; URLs no http/https se omiten. `urlExterna`+`tipoUrlExterna` legado migra al guardar.
- **HECHO** — Form eventos: `hora` ahora `type="time"`; `*` de obligatorios en rojo (evento y noticia); spec de App arreglado (faltaba provideRouter, venía roto de main).
- **HECHO** — Nav admin remarcado con pills+iconos y "Ver sitio" en pestaña nueva (`5a513b7`). Bug: `routerLinkActive` no se importaba — el activo nunca funcionó.
- **HECHO** — Desplegado a producción interna (172.16.0.190): rsync + mvn package + npm build + restart systemd; `ddl-auto: update` agregó columnas solas. API verificada 200 con campos nuevos.
- **HECHO** — CABID agregado al portafolio (`64c9c25` + gh-pages) con 6 capturas.
- **RIESGO** — `cabid.cl` resuelve a 198.12.239.238 (sitio ANTIGUO); el nuevo está solo en la IP interna. Falta cutover DNS (o que la UOH apunte el dominio al server nuevo). Evento de prueba en prod con `urlExterna:"asdasd"` — limpiar desde admin.
- **RIESGO** — Postgres local de este equipo tiene rol `cabid_user` con clave desconocida (no es `cabid_dev`). Resetear con `sudo -u postgres psql -c "ALTER USER cabid_user WITH PASSWORD 'cabid_dev';"` si se quiere backend local.
- **PENDIENTE** — Borrar rama remota `feat/iconos-material` (ya mergeada). Tests de integración backend (H2/Testcontainers). Systemd ya existe; falta respaldo del dir uploads.
