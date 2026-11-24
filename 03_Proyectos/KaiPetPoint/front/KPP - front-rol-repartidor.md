---
tipo: documentacion-tecnica
proyecto: kaipetpoint
actualizado: 2026-11-24
tags: [front, roles, repartidor, despachos, seguridad]
---

# KPP — Rol `repartidor`

Rol nacido con el módulo de despachos: el repartidor solo necesita ver sus
entregas y marcar su estado. Spec viva — [[Docs-first - estructura antes de construir]].

## Qué ve

| Superficie | Repartidor |
|---|---|
| `/despachos` (lista + cambio de estado) | sí |
| `/perfil` (su cuenta, clave, preferencias) | sí |
| Todo lo demás (panel, ventas, caja, catálogo, clientes…) | no — redirect a `/despachos` |

- Sidebar (`shell.component`): un solo ítem, Despachos.
- Campana de stock (topbar): oculta — consume `/api/catalogo`, fuera de su alcance.
- Selector de sucursal: igual que todos (sus despachos son por sucursal activa).

## Piezas

- `auth.service`: `esRepartidor = usuario?.rol === 'repartidor'`.
- `auth.guard`: `staffGuard` — repartidor fuera de `/despachos` y `/perfil`
  → `UrlTree('/despachos')`. Aplicado a todas las rutas de tienda.
- `usuarios.page`: opción "Repartidor" en el selector de rol (crear/editar).
- Backend: contrato en [[../back/KPP - back-seguridad-roles]] — el guard del
  front es UX; la autoridad es `SecurityConfig`.

## Alta

Admin crea usuario → rol "Repartidor" → asigna sucursal → el repartidor entra
directo a `/despachos` (cualquier otra ruta rebota ahí).

## Límites declarados

- `/api/despachos` lista **todos** los despachos de la sucursal — no hay
  asignación por repartidor (entidad `Despacho` no tiene `repartidor_id`):
  es la cola del equipo, no una lista personal. Si se necesita asignación,
  es feature nueva con migración.
