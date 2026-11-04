---
status: Pendientes
proyecto: kaipetpoint
fase: fase-3
criticidad: critica-negocio
esfuerzo: XL
---
_Objetivo: convertir KaiPetPoint en SaaS multi-tienda — cada cliente arrienda su tienda, administrable desde un panel central._

## Modelo propuesto

- Jerarquía: **tienda (tenant)** > sucursal > usuario. El multi-sucursal actual (`sucursal_id`, BD única) se extiende con `tienda_id` un nivel arriba — misma decisión estructural: BD única + scoping, no una BD por tienda.
- Roles: **super-admin** (plataforma; evolución del `root` actual) > admin de tienda > vendedor.
- Branding por tienda: nombre display, logo, paleta (el kit ya trae preferencias/paletas) — extiende el backlog `app-identidad.ts` a identidad por tenant.

## Tareas

- [ ] Migración: tabla `tiendas` + `tienda_id` en sucursales/usuarios/catálogo/ventas/movimientos; todo lo existente se adscribe a "Patitas" (mismo patrón que V3 con "Casa matriz").
    
- [ ] Panel super-admin: CRUD de tiendas — nombre, **logo**, paleta/colores, datos de la empresa, activar/suspender.
    
- [ ] Scoping de seguridad: cada query acotada a tienda (vía sucursal) salvo super-admin; membresías usuario↔tienda.
    
- [ ] Onboarding de tienda nueva: crear admin inicial + seed mínimo (categorías, identidad).
    
- [ ] Branding aplicado: logo/nombre/colores de la tienda activa en login, sidebar y comprobante/ticket impreso.
    
- [ ] Revisar cookie `kaipetpoint_sucursal` y `SucursalResolver` → resolver tienda + sucursal.
    
- [ ] (Fase 2) Suscripciones/planes por tienda y límites (usuarios, sucursales, productos).

## Preguntas abiertas

- ¿Catálogo compartido entre tiendas o cada una el suyo? (Default: propio — Patitas vende mascotas, otra tienda puede ser de otro rubro.)
- ¿Puede un usuario pertenecer a varias tiendas?
- ¿Subdominio por tienda (`patitas.kaipetpoint.cl`) o una sola app con login que resuelve el tenant?

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/multi-tienda
```
