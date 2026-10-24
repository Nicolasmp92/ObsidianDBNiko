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

1. **Esperar propagación DNS**: `namp.cl` está en Cloudflare "Pending" hasta que NIC publique los nuevos NS (zona .cl se actualiza cada ~30 min). Verificar: `dig NS namp.cl` → deben aparecer `*.ns.cloudflare.com`. Cuando Cloudflare marque "Active", seguir.
2. **En Dokploy → servicio `kpp` → pestaña Environment**: pegar las env vars de producción (DB password, JWT secret, seed clave/correo, JWT horas, COOKIE_SECURE=true). Los valores están guardados en las env vars del servicio/secrets — NO commitear al repo ni al vault.
3. **Pestaña Domains**: dominio `kpp.namp.cl` → servicio `frontend`, puerto contenedor `4004`, HTTPS activado.
4. **Deploy** y revisar logs (build Maven + Angular tarda varios min).
5. Probar login admin, una venta POS, stock, boleta.
6. Configurar monitor en Uptime Kuma para `https://kpp.namp.cl`.
7. Cron `pg_dump` diario de Postgres + retención (backups fuera del VPS lo antes posible).
8. Subdominios previstos (registros A → 200.141.25.56 ya creados en Cloudflare): `namp.cl`/`www` (web empresa), `kpp` (POS), `demo` (staging), `status` (Uptime Kuma).

## Notas

- `COOKIE_SECURE=true` solo funciona con HTTPS real (kpp.namp.cl con certificado).
- Empresa umbrella: **NAMP** (Nicolás Antonio Muñoz Palacios — nombre provisional). Productos: KaiPetPoint/KPP, BeanFlow, Sconect, ISO Manager.
- El dominio gratis de Hostinger quedó sin reclamar (no ofrecen `.cl`; `.io` renovaba ~$75/año — descartado).
- NIC Chile NO ofrece DNS — por eso Cloudflare como proveedor de zona DNS (gratis, PoP Santiago).
- Registros DNS en Cloudflare están en modo **DNS only** (proxy naranja apagado) para que Traefik/Let's Encrypt funcionen sin conflicto.
- Pendiente legal: ampliar giro SII (ya tiene honorarios 2ª cat.) para facturar SaaS — revisar con contador.
