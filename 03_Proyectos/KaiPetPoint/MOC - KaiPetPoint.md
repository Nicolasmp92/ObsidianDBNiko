---
tipo: proyecto
proyecto: kaipetpoint
estado: activo
actualizado: 2026-10-04
tags: [pos, tienda, mascotas, patitas, inventario, ventas, angular, spring-boot]
---
# 🐾 MOC — KaiPetPoint

Punto de venta e inventario para tiendas — primera instancia: **Patitas** (alimentos de mascotas). Repo: `~/Escritorio/Desarrollo/kaipetpoint` (GitHub `Nicolasmp92/kaipetpoint`, privado). Generado desde [[MOC - StarterCustomeKit|StarterCustomeKit v2]]; antes se llamaba *Mostrador* (renombrado 2026-10-04).

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero levantar el stack** → `backend: mvn spring-boot:run` (:8084) + `npm start` (:4204); login `nikolasmp92@gmail.com` / `niko9214`
- **Levantar en compu pega (Windows, sin Postgres)** → `cd backend && SPRING_FLYWAY_ENABLED=false SPRING_JPA_HIBERNATE_DDL_AUTO=update KAIPETPOINT_DB_URL="jdbc:h2:mem:kaipetpoint;DB_CLOSE_DELAY=-1" KAIPETPOINT_DB_USER=sa KAIPETPOINT_DB_PASSWORD= ~/tools/apache-maven-3.9.9/bin/mvn spring-boot:run` (H2 en memoria + seed; sin el flag Flyway falla — migraciones son SQL PostgreSQL). Front: `npm start` en la raíz (:4204, proxy `/api`→:8084 vía `proxy.conf.cjs`)
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)
- **Quiero ver quién visita las demos** → access log de Traefik en el VPS (`/etc/dokploy/traefik/dynamic/access.log`, JSON, rotación diaria×30): `ssh niko@200.141.25.56 "sudo grep '\"RequestHost\":\"demo.namp.cl\"' /etc/dokploy/traefik/dynamic/access.log | python3 -c 'import sys,json; [print(json.loads(l)[\"ClientHost\"], json.loads(l)[\"RequestPath\"], json.loads(l).get(\"request_User-Agent\",\"-\")[:50]) for l in sys.stdin]' | sort | uniq -c | sort -rn"`. Cubre TODOS los sitios (namp.cl, kpp.namp.cl, sconect.namp.cl…) — cambiar el RequestHost
- ~~**Quiero emitir boletas SII**~~ → **descartado 2026-11-20** (no se implementará; [[Guia - Boleta electronica SII]] queda como referencia)
- **Quiero el modelo de datos y diagramas** → [[KPP - Modelo de datos y flujos]] (ER Mermaid post-V17 + flujos venta/fiado/caja/importación; tablas al detalle en `.devin/rules/backend-bd-esquema.md` del repo)

## Dominios (en `main` + ramas de trabajo)

| Dominio | Entidades | Estado |
|---|---|---|
| Catálogo | `marcas`, `categorias`, `productos` | Completo; bajas lógicas + importación CSV masiva (2026-10-29) |
| Inventario | `movimientos_stock`, `stock_sucursal` | Completo; saldo derivado por sucursal, nunca negativo |
| Ventas | `ventas`, `venta_items`, `venta_pagos` | Completo; descuentos, mixto, anulación repone stock |
| Clientes/fiado | `clientes`, `cliente_abonos` | Completo; cuenta corriente derivada + abono junto a venta |
| Caja | `caja_sesiones`, `caja_movimientos`, `aperturas_cajon` | Completo; arqueo con diferencia + cajón auditado |
| Despachos/ofertas | `despachos`, `zonas_despacho`, `ofertas` | Completo; tarifa por zona, precio por cantidad |
| Plataforma | `usuarios`, JWT dual, preferencias/paletas | Sesión sliding 2h/cap 12h + revocación por cambio de clave (V16) + tour primer uso (V17) |

## Decisiones estructurales vigentes

- **Nombre**: `kaipetpoint` (paquetes, BD, cookie `kaipetpoint_token`, claves `kaipetpoint.*`, env `KAIPETPOINT_*`). Display: KaiPetPoint. La instancia Patitas vive en el seed — rebrandable.
- Stock = saldo derivado de `movimientos_stock`; nunca negativo (409 al cobrar sin stock).
- Total de venta siempre calculado en servidor con precio vigente.
- Puertos: API `8084`, dev `4204`, SSR `4004`. BD `kaipetpoint`/`kaipetpoint_user` en PostgreSQL.
- Roles simples del kit (admin/user): vendedor vende, admin gestiona + anula.
- SSR con sesión: `ssrCookieInterceptor` reenvía la cookie a `/api/*` en render por petición (sin él, F5 cerraba sesión).

## Backlog declarado

Backlog completo priorizado por criticidad/viabilidad/esfuerzo en [[KPP - Roadmap y priorización (PMV)]] — fases: **PMV** (operación real) → nicho/retención → SaaS. Sueltos aún sin fase: reportes por rango · identidad extraída a config (`app-identidad.ts`).
**Descartado:** boleta SII integrada — decisión 2026-11-20 (era diferida; el flujo DTE interno ya había salido en V15). **Diferido documentado:** modo offline → [[KPP - Modo offline (PWA)]] con su justificación intacta.
