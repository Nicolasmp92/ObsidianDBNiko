---
tipo: runbook
estado: vigente
actualizado: 2026-10-30
tags: [seguridad, vps, kernel, parches, runbook]
---
# Seguridad — Gestión de parches del VPS

Política de actualización del sistema operativo del VPS Hostinger (Ubuntu 24.04, `ssh vps`). Ver también: [[Estado - Infraestructura NAMP]].

## Política vigente (2026-10-30)

- **`unattended-upgrades` activo**: instala actualizaciones de seguridad automáticamente en su corrida nocturna (`APT::Periodic::Unattended-Upgrade "1"` en `/etc/apt/apt.conf.d/20auto-upgrades`).
- **Auto-reboot nocturno**: `/etc/apt/apt.conf.d/52auto-reboot-namp.conf`
  - `Unattended-Upgrade::Automatic-Reboot "true"`
  - `Unattended-Upgrade::Automatic-Reboot-WithUsers "true"`
  - `Unattended-Upgrade::Automatic-Reboot-Time "05:00"` — después del `pg_dump` (04:15) y antes del pull local de backups (05:30).
- **Criterio**: parches del SO nunca quedan esperando acción humana. El reboot a las 05:00 minimiza impacto (horario valle) y el stack completo se auto-recupera (verificado 2026-10-30).

## Auto-recuperación del stack tras reboot (verificado)

| Componente | Política | ¿Vuelve solo? |
|---|---|---|
| Docker daemon | `systemctl is-enabled docker` = enabled | ✅ al boot |
| Traefik (Dokploy) | restart `always` | ✅ |
| KPP prod (front/back/postgres) | restart `unless-stopped` | ✅ |
| KPP demo (front/back/postgres) | restart `unless-stopped` | ✅ |
| Sitio namp.cl | restart `unless-stopped` | ✅ |
| Uptime Kuma | restart `always` | ✅ |
| Dokploy + dokploy-postgres | Swarm services replicated 1/1 | ✅ (swarm re-schedulea) |

## Runbook

### ¿Hay parche de kernel pendiente?
```bash
ssh vps "uname -r && apt update -qq && apt list --upgradable 2>/dev/null | grep -i linux"
```
Si no aparece ningún `linux-image`/`linux-headers`, el parche aún no existe en los repos de Ubuntu.

### ¿Reboot pendiente?
```bash
ssh vps "ls /var/run/reboot-required && cat /var/run/reboot-required.pkgs"
```

### ¿Forzar parche + reboot ahora? (solo si es urgente y el parche YA está publicado)
```bash
ssh vps "sudo apt update && sudo apt upgrade -y"
ssh vps "sudo reboot"   # ~1-2 min de caida de TODOS los servicios
```

### ¿Se aplicó bien tras el reboot automático?
```bash
ssh vps "uname -r && docker ps --format '{{.Names}} {{.Status}}'"
```
Esperado: todos los contenedores `Up` + Kuma manda correo DOWN→UP esa madrugada (**falsa alarma esperada, no es incidente**).

## Historial de parches

| Fecha | CVE / motivo | Acción |
|---|---|---|
| 2026-10-30 | **CVE-2026-98432** — kernel Linux, RCE remoto en gestión de conexiones de red (aviso Hostinger 29-oct). Debian ya tenía fix; Ubuntu aún no publicaba. | Kernel `6.8.0-147-generic`. Se habilitó auto-reboot nocturno + se aplicaron 4 upgrades no-kernel (cloud-init, monarx-agent, ubuntu-pro-client×2). Cuando Canonical publique, se instala y reinicia solo a las 05:00. |
