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
