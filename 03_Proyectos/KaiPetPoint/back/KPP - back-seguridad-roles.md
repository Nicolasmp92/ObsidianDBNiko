---
tipo: documentacion-tecnica
proyecto: kaipetpoint
actualizado: 2026-11-24
tags: [back, seguridad, roles, repartidor, security-config]
---

# KPP — Roles y permisos de API

Matriz canónica de acceso. Regla madre: [[Docs-first - estructura antes de construir]].

## Roles (`usuarios.rol`, `ROLE_*` en Spring)

| Rol | Quién | Acceso |
|---|---|---|
| `root` | dueño/plataforma | todo + `/api/root/**` (hereda `ROLE_ADMIN` en `JwtAuthFilter`) |
| `admin` | dueño tienda | `/api/admin/**` + todo el operativo |
| `user` | vendedor | operativo de tienda (ventas, caja, catálogo lectura, clientes, despachos) |
| `repartidor` | reparto | `/api/despachos/**` + `/api/auth/**` + `/api/perfil/**` — nada más |

## Cadena de matchers (`SecurityConfig`, orden = precedencia)

1. públicos: `/error`, `/api/auth/login`, `/api/health`, `/api/demo/config`,
   `/actuator/health`, swagger
2. `/api/root/**` → `ROOT`
3. `/api/admin/**` → `ADMIN`
4. `/api/despachos/**`, `/api/auth/**`, `/api/perfil/**` → autenticado (todos los roles)
5. `/api/**` → `USER|ADMIN|ROOT` — **repartidor queda fuera del resto del operativo**
6. `anyRequest` → deny

## Altas/cambios de rol

`AdminUsuariosController.Peticion.rol` valida `admin|user|root|repartidor`.
Delegar `root` sigue exigiendo ser root (control aparte del patrón).

## Invariantes

- La cookie JWT lleva el rol; el front usa ese claim para guards/menú, pero
  la autoridad real es esta cadena — el front puede ocultar, nunca conceder.
- Cambiar la clave revoca tokens (V16): degradar un repartidor a user no
  requiere tocar su sesión — el rol nuevo aplica en su JWT vigente.
