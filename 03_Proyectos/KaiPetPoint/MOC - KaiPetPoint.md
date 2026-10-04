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
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Dominios (en `main` + ramas de trabajo)

| Dominio | Entidades | Estado |
|---|---|---|
| Catálogo | `marcas`, `categorias`, `productos` | Completo; bajas lógicas preservan historial |
| Inventario | `movimientos_stock` | Completo; entradas/salidas/ajustes manuales + trazas automáticas de venta/anulación |
| Ventas | `ventas`, `venta_items` | Completo; POS con comprobante post-cobro, anulación admin repone stock |
| Plataforma | `usuarios`, JWT dual, preferencias/paletas | Heredado del kit |

## Decisiones estructurales vigentes

- **Nombre**: `kaipetpoint` (paquetes, BD, cookie `kaipetpoint_token`, claves `kaipetpoint.*`, env `KAIPETPOINT_*`). Display: KaiPetPoint. La instancia Patitas vive en el seed — rebrandable.
- Stock = saldo derivado de `movimientos_stock`; nunca negativo (409 al cobrar sin stock).
- Total de venta siempre calculado en servidor con precio vigente.
- Puertos: API `8084`, dev `4204`, SSR `4004`. BD `kaipetpoint`/`kaipetpoint_user` en PostgreSQL.
- Roles simples del kit (admin/user): vendedor vende, admin gestiona + anula.
- SSR con sesión: `ssrCookieInterceptor` reenvía la cookie a `/api/*` en render por petición (sin él, F5 cerraba sesión).

## Backlog declarado

Clientes/proveedores · reportes por rango · identidad extraída a config (`app-identidad.ts`) · portar fix SSR a SCK/Frunexis.
