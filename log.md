# Log — Global (raíz del vault)

Bitácora maestra append-only. Resume lo relevante entre sesiones y apunta al log detallado de cada proyecto (`03_Proyectos/<proyecto>/log.md`). Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO / PENDIENTE.

> **Regla de uso:** cualquier agente debe leer este archivo al inicio de una sesión de trabajo (y el log del proyecto que se toque). Al hacer trabajo significativo, agregar una línea aquí y/o en el log del proyecto correspondiente, y hacer commit+push para que el contexto viaje entre equipos.

- **HECHO** — Portafolio: sección Experience reescrita sin lista de clientes; deploy a GitHub Pages, commit `bcc0d3d` en `Nicolasmp92/Nicolasmp92.github.io` (2026-10-23). Detalle: [[03_Proyectos/Portafolio/log]].
- **DECISIÓN** — Empresa paraguas: **NAMP**. Productos: KaiPetPoint, BeanFlow, Sconect, ISO Manager. Dominio `namp.cl` comprado en NIC Chile; DNS administrado en Cloudflare (Free, DNS-only) (2026-10-23). Detalle: [[03_Proyectos/Empresa/log]].
- **HECHO** — Infra NAMP: VPS Hostinger KVM 2 Brasil `200.141.25.56` operativo — SSH por llave (usuario `niko`), UFW, Docker, Dokploy + Traefik, Uptime Kuma arriba (2026-10-23/24).
- **PENDIENTE** — Deploy KPP en Dokploy (servicio `kpp`, repo `kaipetpoint`, branch `feat/deploy`): falta env vars, dominio `kpp.namp.cl`+HTTPS, pg_dump cron, monitor Uptime Kuma. Estado detallado: [[03_Proyectos/Empresa/Estado - Infraestructura NAMP]].
- **PENDIENTE** — Legal/fiscal: validar giro SII para facturar SaaS (ya existe iniciación honorarios 2ª cat.); boleta electrónica/DTE es la brecha crítica de KPP vs incumbentes.
