---
tipo: nota-tecnica
proyecto: StarterCustomeKit
estado: vigente
fecha: 2026-10-02
tags: [alcance, angular, spring-boot, metodologia]
---

# SCK — Alcance v2 (Angular + Spring Boot)

> **Verificado 2026-10-02 contra el repo clonado**
> (`~/Escritorio/Desarrollo/StarterCustomeKit`, rama `main`). Inventario real:
> **6 dominios, 56 archivos en `app/Domains/`, 77 vistas Blade**, i18n en/es,
> Socialite, Sail. La lista MVP de abajo queda ratificada sin cambios.

## Inventario v1 — qué se porta como *decisión* (no como código)

| Asset v1 | Equivalente v2 |
|---|---|
| Actions `__invoke` + DTOs `final readonly` | Services/use-cases + `record` en Spring; `signal`-based services en Angular |
| `UserPolicy` (anti auto-eliminación) | Regla en `@PreAuthorize` / método del service |
| `BuildUserChangeSet` (diff antes/después) | Patrón reutilizable cuando Audit entre al kit |
| `Loggable` trait + `activity_logs` | JPA entity listeners / AOP — cuando Audit se gradúe |
| `SettingsManager` key-value | Tabla `settings` + service — cuando se gradúe |
| 77 vistas Blade + capa JS propia (sidebar, splash, tooltip, theme, notify) | **Perdidas** — Livewire no porta. Las *decisiones UI* sí: dark mode, sidebar colapsable, breadcrumbs, login con wallpaper → componentes `shared/` Angular según estándar |
| i18n en/es + laravel-lang | Cabid: i18n faseado — cadenas centralizadas hasta 2º idioma real |
| `.devin/rules/` ya existía en el repo | Buen precedente: el kit v2 lleva `.devin/` completo desde el día 1 |
| Foto de perfil (upload/delete + nav reactiva) | Fue la última feature real de v1 → candidata a graduarse si un proyecto la pide; el CRUD ejemplo puede demostrar upload |

## Verificación contra Frunexis (2ª evidencia, mismo día)

Frunexis (`~/Escritorio/Desarrollo/Frunexis`) es **fork del starter** — su
historial muestra `merge template/main` y existe `.devin/workflows/update-template.md`
(documenta `git remote add template` + `merge -X theirs`). El modelo
template→proyecto **ya funcionó una vez**. Qué maduró ahí:

- **El patrón de dominio escala bien**: `Actions/<Entidad>/` con
  sub-namespaces, `Policies/` por entidad, `Services/` (`ActiveSeasonService`)
  — mismo idioma que cabid pedirá en Spring (`<dominio>/` con service +
  repository + controllers).
- **Hardening real que no está en la v1**: middlewares `EnsureUserIsActive`
  (usuario inactivo → logout en el request) y `CheckPasswordExpiration`.
  Equivalente v2: check en `JwtAuthFilter` (campo `enabled`) — entra al MVP
  como parte de Auth, es barato y retrofit molesto.
- **Deuda visible**: `app/Livewire/` y `app/Http/Controllers/Agenda/` fuera de
  `Domains/` — fuga de arquitectura cuando se trabaja rápido. En v2 la regla
  va escrita en el estándar, no en la memoria.
- **CI/CD**: 5 workflows de GitHub, pero `deploy.yml` está copiado de MP
  (`dist/MP/browser`, FTP a cPanel) — no corresponde a un proyecto Laravel.
  **Decisión pendiente v2:** el front Angular sí despliega por FTP a cPanel;
  el backend Java necesita host con JVM (VPS/PaaS) — resolver antes del primer
  deploy real, no ahora.
- **Sync kit→proyecto**: el mecanismo `git merge -X theirs template/main` se
  conserva para v2 (misma estructura = mismo truco). Documentarlo en el kit.

## Lección del kit anterior

El problema no fue el stack: fue el alcance. El kit creció a **10 dominios**
(6 completados + 4 pendientes) — eso es un producto SaaS, no un starter.
Criterio de éxito del kit: *minutos desde clone hasta la primera feature de
negocio*, no cantidad de features propias.

## Regla de pertenencia (el gate contra el scope creep)

> **Un módulo entra al kit solo si TODO proyecto derivado lo necesita el día 1,
> o si su costo de agregarlo después es alto** (infraestructura transversal).
> Lo demás es dominio del proyecto hijo, no del kit.

**Regla de graduación:** un módulo del backlog se promueve al kit cuando 2
proyectos reales lo necesitaron, o cuando su retrofit sea caro (p. ej. algo
que toque auth o la capa HTTP). Un solo proyecto que lo use no basta.

## ✅ Dentro del MVP (piso transversal)

| Módulo | Justificación día-1 |
|---|---|
| Auth JWT **dual**: cookie `httpOnly` (web) + Bearer (mobile) — `login|logout|me` + check `enabled` en filtro | Todo proyecto lo necesita; retrofit caro. Dual-mode porque el mismo back sirve Angular y Flutter. Check activo viene de `EnsureUserIsActive` (Frunexis) |
| Users CRUD admin + roles simples (admin/user) | Auth sin gestión de usuarios es inútil; sin Spatie-equivalente — `@PreAuthorize` basta |
| Health endpoint | Diagnóstico universal, 20 líneas |
| 1 dominio CRUD ejemplo (público + admin) | La plantilla que se copia para cada feature real |
| `DataSeeder` (admin inicial) | Primer arranque sin SQL manual |
| Wiring proxy `4200 → 4000 → 8080` + env vars `<APP>_*` | La fricción que cabid ya resolvió |
| Paquete `.devin/` + `inyector-skill.md` + README/log/registro | La metodología es el diferenciador del kit |
| Front: shell con login + layout + guards + el CRUD ejemplo | Espejo del backend |

## ❌ Fuera del MVP (con razón)

| Módulo | Por qué no |
|---|---|
| Notifications omnicanal | Cada proyecto define sus canales; retrofit barato |
| Settings panel (key-value) | YAGNI hasta el 2º proyecto que lo pida |
| Audit logs | Valioso pero no día-1; interceptor HTTP lo agrega después |
| Media/S3 | Varía por proyecto (local vs S3 vs ninguno) |
| SuperAdmin + impersonate | Feature de SaaS multi-cliente, no de starter |
| Multi-tenancy | La ambición que desbordó el kit v1; ningún proyecto actual la pide |
| Instalador CLI | Prematuro: el checklist de [[Estándares Full-Stack - StarterCustomeKit]] ya cubre el arranque |
| i18n | Faseado igual que cabid: solo cuando exista un 2º idioma real |
| Toasts/UI feedback framework | Se añade con el primer proyecto que lo ejerza |

## Condición de falsación

Si al arrancar Frunexis o la web de la empresa resulta que **>2 módulos de la
lista ❌ se necesitaron el día 1**, la regla de pertenencia está mal calibrada
y esta nota se revisa.

## Plan tras el clon del repo v1

1. Inventario de lo **rescatable**: patrones (Actions `__invoke`, DTOs readonly),
   tests de dominio, componentes UI — no se porta código Laravel, se porta el
   catálogo de decisiones.
2. Verificar esta lista contra el código real: ¿algo del MVP falta o sobra?
3. Ratificar → estado `vigente` → entonces sí: scaffold nuevo repo.
