# Log — Global (raíz del vault)

Bitácora maestra append-only. Resume lo relevante entre sesiones y apunta al log detallado de cada proyecto (`03_Proyectos/<proyecto>/log.md`). Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO / PENDIENTE.

> **Regla de uso:** cualquier agente debe leer este archivo al inicio de una sesión de trabajo (y el log del proyecto que se toque). Al hacer trabajo significativo, agregar una línea aquí y/o en el log del proyecto correspondiente, y hacer commit+push para que el contexto viaje entre equipos.

- **HECHO** — Portafolio: sección Experience reescrita sin lista de clientes; deploy a GitHub Pages, commit `bcc0d3d` en `Nicolasmp92/Nicolasmp92.github.io` (2026-10-23). Detalle: [[03_Proyectos/Portafolio/log]].
- **DECISIÓN** — Empresa paraguas: **NAMP**. Productos: KaiPetPoint, BeanFlow, Sconect, ISO Manager. Dominio `namp.cl` comprado en NIC Chile; DNS administrado en Cloudflare (Free, DNS-only) (2026-10-23). Detalle: [[03_Proyectos/Empresa/log]].
- **HECHO** — Infra NAMP: VPS Hostinger KVM 2 Brasil `200.141.25.56` operativo — SSH por llave (usuario `niko`), UFW, Docker, Dokploy + Traefik, Uptime Kuma arriba (2026-10-23/24).
- **PENDIENTE** — Deploy KPP en Dokploy (servicio `kpp`, repo `kaipetpoint`, branch `feat/deploy`): falta env vars, dominio `kpp.namp.cl`+HTTPS, pg_dump cron, monitor Uptime Kuma. Estado detallado: [[03_Proyectos/Empresa/Estado - Infraestructura NAMP]].
- **PENDIENTE** — Legal/fiscal: validar giro SII para facturar SaaS (ya existe iniciación honorarios 2ª cat.); boleta electrónica/DTE es la brecha crítica de KPP vs incumbentes.
- **HECHO** — Producción NAMP (2026-10-24, PC casa): `https://namp.cl` (sitio empresa estático) y `https://kpp.namp.cl` (POS full-stack) en vivo vía Dokploy+Traefik con Let's Encrypt; autodeploy On Push en ambos. Commits clave: `14a6de8` (stack docker), `c2b3d88` (caddy profile standalone), `3e27718` (allowedHosts `*.namp.cl` — wildcard requiere `*.`, no `.`). Detalle: [[03_Proyectos/KaiPetPoint/log]] y [[03_Proyectos/NAMP/log]].
- **HECHO** — Ops: PC de casa con `ssh vps` (llave `niko-desktop-devin`); cron `pg_dump` diario 04:15 en el VPS (`~/backups/kpp/`, retención 14d); regla global de Devin: push automático post-tarea (`%APPDATA%/devin/AGENTS.md`). Detalle: [[03_Proyectos/Empresa/log]].
- **PENDIENTE** — Infra: probar login/venta/boleta en kpp.namp.cl; monitores Uptime Kuma; copia de backups fuera del VPS; datos de contacto reales en namp.cl/contacto; subdominios `demo`/`status` sin usar.
- **HECHO** — namp.cl: formulario de contacto operativo end-to-end (selector correo/WhatsApp + Cloudflare Email Routing `contacto@namp.cl`→Gmail + FormSubmit activado). Detalle: [[03_Proyectos/NAMP/log]].
- **RIESGO** — MP (ingenieriamp.cl): deploys GH Actions rotos desde 17-oct (secrets mailer/recaptcha); prod corre build del 15-ago, commits de seguridad sin publicar. Detalle: [[03_Proyectos/MP/log]].
- **HECHO** — UOH Linktree (`LINKTREE/` en repo repositorios-digitales-uoh): app Angular 22 para la bio de @bibliotecasuoh — tema menta→celeste UOH con focos, entrada escalonada + sheen, 11 enlaces oficiales (enviados por Paulina) con iconos SVG, chips LinkedIn/correo arriba. Pendiente: hosting público para poner en la bio (2026-10-26).
- **HECHO** — KPP prod: bug de sesión en recargas SSR corregido (`0e03791`, causa: fetch Node perdía cookie en redirect http→https del proxy; ahora SSR→backend por red interna) (2026-10-26).
- **HECHO** — UOH: linktree en vivo en `https://publicaciones.uoh.cl/enlaces/` — nuevo server SEXTOPLANO (172.16.0.130, Windows IIS+FTP) es nuestro; cert wildcard renovado (vencía 29-sep, ahora hasta 27-dic). Deploy: `npm run deploy-sexto` en LINKTREE/ (2026-10-26).
- **HECHO** — KPP mobile: desborde de grillas a 360px corregido (`minmax(0,1fr)` en `b306d06`+`bade949`; bug raíz compartido dashboard+POS) + botón Nueva venta full-width. Audit CDP headless reusable en `/tmp/shot.mjs` (2026-10-26).
