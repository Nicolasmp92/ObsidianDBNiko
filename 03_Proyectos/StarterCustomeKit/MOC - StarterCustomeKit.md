---
tipo: proyecto
proyecto: startercustomekit
estado: activo-v2-en-main
actualizado: 2026-10-02
tags: [starter, kit, angular, spring-boot, portafolio]
---
# 🧰 MOC — StarterCustomeKit

Kit base para arrancar proyectos rápido. Repo: `~/Escritorio/Desarrollo/StarterCustomeKit` (GitHub `Nicolasmp92/StarterCustomeKit`).

> **Cambio de stack (2026-10-02):** el kit migró de Laravel/Livewire a
> **Angular 22 + Spring Boot + PostgreSQL** con la metodología `.devin`
> incorporada. Stack y metodología vigentes: [[Estándares Full-Stack - StarterCustomeKit]].
> Las notas `STK-*`/`SCK-*` de abajo quedan como especificación funcional de
> los dominios (válidas), no como stack vigente. La v1 Laravel vive en el tag `v1-laravel`.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero saber qué entra al kit y qué no** → [[SCK - Alcance v2]] (gate anti scope-creep)
- **Quiero la estrategia** → [[SCK - Estrategia de Alcance]]
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Estado v2 (en `main`)

- Auth JWT dual (cookie `httpOnly` + Bearer), usuarios, roles admin/user, health, dominio-plantilla `items`, seed, RBAC base.
- Sidebar 3 estados (280/84/0px) con overlay móvil, tooltips CDK, persistencia localStorage.
- Puertos propios: API `8081`, dev `4201`, SSR `4001`. BD `sck`/`sck_user` en PostgreSQL.

## ✅ Dominios completados (especificación v1)

- [x] [[STK - 1. Dominio de Notificaciones (Prioridad Crítica)]] ✅ 2026-05-06
- [x] [[STK - 2. Dominio de Gestión de Usuarios (Prioridad Alta)]] ✅ 2026-05-07
- [x] [[STK - 3. Dominio de Permisos y Roles (Prioridad Media-Alta)]] ✅ 2026-05-09 — *portado a v2 como RBAC en Frunexis; pendiente de bajar al kit por regla de graduación*
- [x] [[STK - 4. Dominio de Configuración (Settings Global) (Prioridad Media)]] ✅ 2026-05-09
- [x] [[STK - 5. Pulido de Infraestructura de Tests (Prioridad Continua)]] ✅ 2026-05-11
- [x] [[SCK-6 Dominio de Auditoría & Logs]] ✅ 2026-05-11

## 🚧 En proceso

- [ ] [[SCK-7 UI Feedback & Notificaciones (Prioridad Media)]]

## 📋 Pendientes

- [ ] [[SCK-8 Media Management (Gestión de Archivos) (Prioridad Media)]]
- [ ] [[SCK-9 Panel de Super Admin (Control Central) (Prioridad Media)]]
- [ ] [[SCK-10 Instalador & DX (Developer Experience) (Prioridad Baja)]]

## 📚 Bitácora de setup (archivo)

Notas históricas de cómo se montó el kit v1, en `99_Archivo/Proyectos personales/StarterCustomeKit/`:

- [[1. Iniciando proyecto]]
- [[2. instalando lang control de Idiomas]]
- [[3. Roles y permisos Spatie]]
- [[4. Control de versiones con Git y GitHub]]
- [[5. Lucide para laravel]]
