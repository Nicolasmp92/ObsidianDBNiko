---
status: Finalizadas
---
_Objetivo: Llevar la administración de usuarios al estándar de dominios._

- [x] **Refactor de `UserController`**: Migrar toda la lógica de creación, edición y estados (activo/inactivo) a `app/Domains/User/Actions`. ✅ 2026-05-06
    
- [x] **Políticas de Seguridad (Policies)**: Implementar reglas para que un usuario no pueda eliminarse a sí mismo o editar administradores sin permisos. ✅ 2026-05-06
    
- [x] **Optimización de Búsqueda**: Mejorar el componente Volt de la lista de usuarios para que sea más performante con grandes volúmenes de datos. ✅ 2026-05-07

---
# Tareas Realizadas:



# Resumen: Migración Dominio User a Screaming Architecture

## 1. Refactor de `UserController` a Actions ✅

**Archivos eliminados:**
- [app/Http/Controllers/Users/UserController.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Http/Controllers/Users/UserController.php:0:0-0:0) (107 LOC, código muerto sin rutas)

**Estructura creada:**
```
app/Domains/User/
├── Actions/
│   ├── CreateUser.php           — DB::transaction + Hash + syncRoles + notificación
│   ├── UpdateUser.php           — snapshot + BuildUserChangeSet + notificaciones condicionales
│   ├── DeleteUser.php           — guard anti-self + DomainException
│   ├── ToggleUserStatus.php     — flip activo/inactivo
│   └── BuildUserChangeSet.php   — diff antes/después (name, email, status, role, password)
└── DataTransferObjects/
    ├── CreateUserData.php       — final readonly {name, email, plainPassword, status, role, notify}
    └── UpdateUserData.php       — final readonly {name, email, ?plainPassword, status, ?role, notify}
```

**Volt refactorizado ([users/index.blade.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/livewire/users/index.blade.php:0:0-0:0)):**
- `save()` — 50 LOC → 26 LOC: delega a [CreateUser](cci:2://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/CreateUser.php:13:0-44:1)/[UpdateUser](cci:2://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/UpdateUser.php:15:0-72:1) con DTOs
- `deleteConfirmed()` — delega a [DeleteUser](cci:2://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/DeleteUser.php:8:0-21:1) + `catch DomainException`
- `toggleStatus()` — delega a [ToggleUserStatus](cci:2://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/ToggleUserStatus.php:8:0-17:1)
- Eliminados: `buildAllChanges()`, `buildUserChanges()`, [addChange()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/BuildUserChangeSet.php:39:4-55:5) (~55 LOC muerto)
- Imports limpiados: `Hash`, 6 clases de Notifications eliminadas

**Tests:** `3 failed, 25 passed` — baseline intacto, sin regresiones.

---

## 2. Políticas de Seguridad (Policies) ✅

**Archivo creado:**
- [app/Domains/User/Policies/UserPolicy.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:0:0-0:0)

**Reglas implementadas:**
| Método | Lógica |
|---|---|
| [viewAny](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:10:4-13:5) | requiere `users.access` |
| [view](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:15:4-18:5) | requiere [users.view](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:15:4-18:5) |
| [create](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:20:4-23:5) | requiere [users.create](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:20:4-23:5) |
| [update](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:25:4-29:5) | requiere `users.edit` + [canActOn()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:41:4-52:5) |
| [delete](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:31:4-39:5) | requiere [users.delete](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:31:4-39:5) + no self + [canActOn()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:41:4-52:5) |

**[canActOn()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Policies/UserPolicy.php:41:4-52:5)** — impide que un `admin` actúe sobre un `super-admin`. El `super-admin` bypass todo vía `Gate::before` ya existente.

**Registro:**
- [AppServiceProvider::boot()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Providers/AppServiceProvider.php:22:4-37:5): `Gate::policy(User::class, UserPolicy::class)`

**Integración Volt PHP:**
- `save()` → `authorize('update', $user)` / `authorize('create', User::class)` antes de Actions
- `deleteConfirmed()` → `authorize('delete', $user)` + `catch(AuthorizationException)`
- `toggleStatus()` → `authorize('update', $user)` antes de Action

**Integración Blade:**
- Botón **Crear**: `@can('create', User::class)`
- Botón **Estado** (toggle): `@can('update', $u)` — badge estático si no tiene permiso
- Botón **Editar**: `@can('update', $u)`
- Botón **Eliminar**: `@can('delete', $u)`

**Tests:** `3 failed, 25 passed` — baseline intacto.

---

## 3. Optimización de Búsqueda (Volt) ✅

**Problema resuelto:**
- Ordenar por `role` cargaba **todos** los usuarios en RAM (`->get()`) → `sortBy()` → `LengthAwarePaginator` manual
- Escalaba O(n) con el total de usuarios

**Solución implementada:**
- **JOIN DB** `model_has_roles` + `roles` solo cuando `sortBy === 'role'`
- `orderByRaw('COALESCE(roles.name, ?) asc|desc', ['zzz'])` — usuarios sin rol al final (ASC) / inicio (DESC)
- `select('users.*')` — evita colisiones de IDs en el JOIN
- Sanitización de `$direction` y `$column` antes de raw SQL
- Eager loading mantenido: `->with('roles', 'permissions')`
- Eliminados: `->get()`, `$users->sortBy()`, `new LengthAwarePaginator()` (~20 LOC)

**Resultado:**
- Paginación nativa siempre (`->paginate()`)
- Escalado O(page) — solo carga la página actual
- Conteo `COUNT(*)` de MySQL en lugar de `$collection->count()`

**Tests:** `3 failed, 25 passed` — baseline intacto.

---

## Métricas finales

| Métrica             | Valor                                  |
| ------------------- | -------------------------------------- |
| Archivos creados    | 8 (5 Actions + 2 DTOs + 1 Policy)      |
| Archivos eliminados | 1 (UserController)                     |
| LOC eliminados      | ~162 (controller + dead code en Volt)  |
| LOC agregados       | ~180 (domain structure)                |
| Tests               | 25 passing, 3 failing (pre-existentes) |
| Autoload classes    | 8481 → 8488 (+7)                       |