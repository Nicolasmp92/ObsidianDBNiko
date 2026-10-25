# Estado actual — Infraestructura NAMP

> Snapshot del estado del VPS/servicios para retomar el trabajo desde cualquier equipo. Última actualización: 2026-10-24.

## Recursos contratados

| Recurso | Detalle |
|---|---|
| VPS | Hostinger KVM 2 (2 vCPU, 8 GB RAM, 96 GB NVMe) — región São Paulo, Brasil |
| IP pública | `200.141.25.56` |
| Hostname | `srv2087549.hstgr.cloud` |
| SO | Ubuntu 24.04 LTS (actualizado) |
| Dominio empresa | `namp.cl` — comprado en NIC Chile (Webpay), titular Nicolás Muñoz |
| DNS | Cloudflare (plan Free) — NS: `andy.ns.cloudflare.com` + segundo NS asignado por Cloudflare |

## Estado del servidor (hecho ✅)

- SSH solo por llave (password deshabilitado). Usuario `niko` con sudo + grupo docker.
- Alias local `ssh vps` en `~/.ssh/config` del compu dev (cris-dev). Otros equipos: agregar su llave pública a `~/.ssh/authorized_keys` del server.
- Firewall UFW: solo puertos 22 / 80 / 443 / 3000.
- Docker 29.9.x instalado.
- **Dokploy** corriendo → panel: http://200.141.25.56:3000 (trae Traefik → HTTPS automático Let's Encrypt).
- Uptime Kuma desplegado → http://kaipetpoint-uptimekuma-64bf96-200-141-25-56.sslip.io
- Proyecto Dokploy `kaipetpoint`, servicio compose `kpp` creado apuntando a repo `Nicolasmp92/kaipetpoint`, branch `feat/deploy`, compose `./docker-compose.yml`. GitHub App `Dokploy-2026-10-23-i5n9be` instalada solo sobre ese repo.

## Pendiente 🔲 (en este orden)

1. ~~**Esperar propagación DNS**~~ ✅ 2026-10-24 — `namp.cl` resuelve al VPS y responde vía Traefik.
2. ~~**En Dokploy → servicio `kpp` → pestaña Environment**~~ ✅ 2026-10-24 — vars `KAIPETPOINT_*` configuradas (DB, JWT, seed, COOKIE_SECURE=true).
3. ~~**Pestaña Domains**~~ ✅ 2026-10-24 — `kpp.namp.cl` → `frontend:4004` HTTPS. Además `namp.cl`+`www.namp.cl` → servicio `web` (proyecto `namp`, sitio estático nginx).
4. ~~**Deploy**~~ ✅ 2026-10-24 — ambos servicios en producción: `namp.cl` 200 y `kpp.namp.cl` 302→`/login` con Let's Encrypt. Fixes aplicados en `main`: caddy bajo profile `standalone` (`c2b3d88`), `allowedHosts` con wildcard `*.namp.cl` (`3e27718` — la sintaxis `.namp.cl` no funciona en Angular).
5. Probar login admin, una venta POS, stock, boleta (con las credenciales seed reales).
6. Configurar monitor en Uptime Kuma para `https://namp.cl` y `https://kpp.namp.cl`.
7. Cron `pg_dump` diario de Postgres + retención (backups fuera del VPS lo antes posible).
8. Subdominios previstos (registros A → 200.141.25.56 ya creados en Cloudflare): `demo` (staging), `status` (Uptime Kuma). Ya desplegados: `namp.cl`/`www` y `kpp`.

## Notas

- `COOKIE_SECURE=true` solo funciona con HTTPS real (kpp.namp.cl con certificado).
- Empresa umbrella: **NAMP** (Nicolás Antonio Muñoz Palacios — nombre provisional). Productos: KaiPetPoint/KPP, BeanFlow, Sconect, ISO Manager.
- El dominio gratis de Hostinger quedó sin reclamar (no ofrecen `.cl`; `.io` renovaba ~$75/año — descartado).
- NIC Chile NO ofrece DNS — por eso Cloudflare como proveedor de zona DNS (gratis, PoP Santiago).
- Registros DNS en Cloudflare están en modo **DNS only** (proxy naranja apagado) para que Traefik/Let's Encrypt funcionen sin conflicto.
- Pendiente legal: ampliar giro SII (ya tiene honorarios 2ª cat.) para facturar SaaS — revisar con contador.
