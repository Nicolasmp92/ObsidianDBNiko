# Estado actual — Infraestructura NAMP

> Snapshot del estado del VPS/servicios para retomar el trabajo desde cualquier equipo. Última actualización: 2026-10-29.

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
- Alias local `ssh vps` en `~/.ssh/config` del compu dev (cris-dev) **y del PC de casa** (`niko-desktop-devin`, agregada 2026-10-24 vía consola web Hostinger). Otros equipos: agregar su llave pública a `~/.ssh/authorized_keys` del server. Ojo: generar llaves con passphrase vacía real (`-N ""`), no literal `""`.
- Firewall UFW: solo puertos 22 / 80 / 443 / 3000.
- Docker 29.9.x instalado.
- **Dokploy** corriendo → panel: http://200.141.25.56:3000 (trae Traefik → HTTPS automático Let's Encrypt).
- Uptime Kuma desplegado → http://kaipetpoint-uptimekuma-64bf96-200-141-25-56.sslip.io
- Proyecto Dokploy `kaipetpoint`, servicio compose `kpp` creado apuntando a repo `Nicolasmp92/kaipetpoint`, branch `feat/deploy`, compose `./docker-compose.yml`. GitHub App `Dokploy-2026-10-23-i5n9be` instalada solo sobre ese repo.
- **Sandbox demo KPP** (2026-10-27): stack manual en `/opt/kpp-demo` con `docker-compose.demo.yml` — postgres+backend+frontend propios, volumen separado, unido a `dokploy-network` con labels Traefik → `https://demo.namp.cl`. Endpoint público `/api/demo/config` entrega credenciales `demo@kaipetpoint.cl` / `KppDemo.2026`; `DemoGuard` bloquea mutaciones de cuenta; `DemoResetService` resetea la BD a las 04:00. Ojo al sincronizar código: **excluir `.env` del rsync** (el .env local de dev sobreescribió el del VPS una vez y expuso credenciales reales en el endpoint público).

## Pendiente 🔲 (en este orden)

1. ~~**Esperar propagación DNS**~~ ✅ 2026-10-24 — `namp.cl` resuelve al VPS y responde vía Traefik.
2. ~~**En Dokploy → servicio `kpp` → pestaña Environment**~~ ✅ 2026-10-24 — vars `KAIPETPOINT_*` configuradas (DB, JWT, seed, COOKIE_SECURE=true).
3. ~~**Pestaña Domains**~~ ✅ 2026-10-24 — `kpp.namp.cl` → `frontend:4004` HTTPS. Además `namp.cl`+`www.namp.cl` → servicio `web` (proyecto `namp`, sitio estático nginx).
4. ~~**Deploy**~~ ✅ 2026-10-24 — ambos servicios en producción: `namp.cl` 200 y `kpp.namp.cl` 302→`/login` con Let's Encrypt. Fixes aplicados en `main`: caddy bajo profile `standalone` (`c2b3d88`), `allowedHosts` con wildcard `*.namp.cl` (`3e27718` — la sintaxis `.namp.cl` no funciona en Angular).
5. Probar login admin, una venta POS, stock, boleta (con las credenciales seed reales).
6. Configurar monitores de uptime para `namp.cl`, `kpp.namp.cl` y `demo.namp.cl`. ✅ 2026-10-29 — panel Kuma accesible en `https://status.namp.cl` (router websecure+certresolver agregado al compose de Dokploy, backup en `.bak`; el dominio sslip.io viejo quedó muerto). **Monitores creados y verificados UP** (via `uptime-kuma-api` por Socket.IO desde `~/.local/bin/kuma-monitors.py`): namp.cl, kpp.namp.cl (200/302), demo.namp.cl — intervalo 60s, todos verdes. Credenciales del panel en `~/.config/namp/kuma.env` (chmod 600). **Alertas**: notificacion SMTP Gmail configurada y probada (correo de test llego a nikolasmp92@gmail.com), asignada a los 3 monitores y marcada como default — via `~/.local/bin/kuma-notify.py`. **Limitación estructural**: Kuma corre EN el mismo VPS — detecta caídas de app/contenedor pero NO la muerte del host; para eso haría falta un check externo (UptimeRobot gratis).
7. ~~Cron `pg_dump` diario de Postgres + retención~~ ✅ 2026-10-24 — `~/backups/backup-kpp.sh` en cron niko `15 4 * * *`, dumps `-Fc` en `~/backups/kpp/`, retención 14 días. **Copia fuera del VPS** ✅ 2026-10-29 — el PC dev jala los dumps por rsync (cron `30 5 * * *` → `/home/niko/backups/kpp-vps/`, retención 30 días). **Ojo**: solo corre si el PC está encendido a esa hora — evaluar storage cloud (rclone) como destino independiente.
8. ~~Subdominios previstos~~ ✅ `demo.namp.cl` desplegado 2026-10-27 como sandbox público de ventas (ver arriba). `status` (Uptime Kuma) ✅ desplegado 2026-10-29 — panel en `status.namp.cl`; la instancia nunca habia completado el setup inicial (wizard de BD + admin) y tenia cero monitores.

## Notas

- `COOKIE_SECURE=true` solo funciona con HTTPS real (kpp.namp.cl con certificado).
- Empresa umbrella: **NAMP** (Nicolás Antonio Muñoz Palacios — nombre provisional). Productos: KaiPetPoint/KPP, BeanFlow, Sconect, ISO Manager.
- El dominio gratis de Hostinger quedó sin reclamar (no ofrecen `.cl`; `.io` renovaba ~$75/año — descartado).
- NIC Chile NO ofrece DNS — por eso Cloudflare como proveedor de zona DNS (gratis, PoP Santiago).
- Registros DNS en Cloudflare están en modo **DNS only** (proxy naranja apagado) para que Traefik/Let's Encrypt funcionen sin conflicto.
- Pendiente legal: ampliar giro SII (ya tiene honorarios 2ª cat.) para facturar SaaS — revisar con contador.
