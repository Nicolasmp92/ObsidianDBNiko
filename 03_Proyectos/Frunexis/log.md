---
tipo: log
proyecto: frunexis
---
# 📓 Log — Frunexis

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

La bitácora técnica autoritativa vive en el repo (`log.md` + `registro_actividades.md`); esta nota resume hitos y decisiones para consulta desde el vault.

---

## 2026-10-02 — Migración al stack SCK v2

- **DECISIÓN** — Alcance del reemplazo: catálogo (familias, especies, temporadas) + personal (trabajadores, contratos). **Agenda excluida** (arrastre de la transición; va a `sconect`). Partida limpia, sin migración de datos productivos.
- **HECHO** — Contenido del repo reemplazado por el kit en `feat/stack-v2-sck`, renombrado `sck`→`frunexis`, dominio `items` eliminado. Mergeado a `main` vía PR #10 (`b969b80`); v1 Laravel en tag `v1-laravel`.
- **HECHO** — Entidades y controllers portados con reglas de negocio verificadas: 409 por rut duplicado, 409 por familia con especies y por trabajador con contratos (la v1 hacía cascade; bloquear preserva el historial laboral), `nullOnDelete` de temporada/especie en contratos.
- **HECHO** — BD `frunexis`/`frunexis_user` creada; `include-message=always` para que los mensajes de reglas lleguen al front.
- **DECISIÓN** — Enums unificados en español (la v1 mezclaba `activa`/`active`/`male`).

## 2026-10-02 — Puertos propios + réplica de la estructura madura

- **HECHO** — Bloque de puertos commiteado: API `8082`, dev `4202`, SSR `4002`. DSpace-CRIS reservado en 8080/4200/4000. PR #11.
- **HECHO** — **RBAC granular** (réplica del spatie v1, normalizado): `roles`, `permisos`, `rol_permisos`, `usuario_permisos`; `usuarios.rol` → FK. 38 permisos `dominio.accion` en `seed/acceso.json`; presets `super-admin`/`admin`/`user`. `@PreAuthorize` en 7 controllers.
- **DECISIÓN** — Authorities resueltas **por request desde BD** (no en el JWT): una query extra a cambio de revocación instantánea sin re-login (la v1 cacheaba con spatie). Smoke verificado: grant directo de `users.view` aplicó al instante.
- **DECISIÓN** — Permisos directos de usuario = override **aditivo** (otorgan, nunca revocan). Si aparece necesidad de revocación puntual, es decisión nueva a registrar.
- **HECHO** — Estructura madura v1 replicada: hoja de vida del trabajador con **8 tabs** (datos y contratos reales; asistencia/disciplina/documentos/evaluaciones/notas/remuneraciones como placeholders — la v1 tampoco tenía tablas), contratos en **drill-down** temporadas→especies→lista, **temporada vigente exclusiva**, modal de permisos con pills por categoría (patrón `PermissionTags` de la v1).
- **HECHO** — Bug de la v1 corregido: las rutas pedían `workers.view`/`contracts.view` pero el seeder nunca los creó; la matriz v2 los incluye.
- **HECHO** — BD regenerada (drop/create) al migrar `usuarios.rol` string → `rol_id` FK; `ddl-auto: update` no convierte la columna. Válido solo sin datos productivos.
- **HECHO** — Iteración promovida a `main`: PR #12 (RBAC+estructura, merge `ebbcd27`) y PR #13 (docs/bitácoras, merge `1103032`).

## Pendientes conocidos

- Revocar el token de GitHub expuesto en chat (manual, Developer Settings).
- `sconect` absorberá el dominio Agenda cuando se aborde (Flutter, tiene app y Laravel previos en `~/Escritorio/Desarrollo/`).

## 2026-10-03/04 — Credenciales unificadas + paletas + login + fix SSR pendiente

- **DECISIÓN** — Convención unificada de credenciales en los tres repos: seed siembra `nikolasmp92@gmail.com` / `niko9214`. En Frunexis el admin existente se actualizó en vivo en PostgreSQL. Rama `chore/credenciales-seed-unificadas`.
- **HECHO** — Sistema de paletas portado desde SCK (`cb65de1`, rama `feat/paletas-tema`): `PreferencesService`, `data-paleta` en `<html>`, 4 acentos, tokens de estado, anti-flash, página `/preferencias` (sin forms de cuenta — el backend no tiene `/api/perfil`), icono `ajustes`, `LayoutService.fijar()`. Migrados 14 colores sueltos → tokens. Fix bonus: prerender roto en `main` corregido (rutas con params → `RenderMode.Server`).
- **HECHO** — Login estándar portado (`96c734c`): recordar correo `frunexis.recordar-correo`, toggle clave, mailto soporte, marca Frunexis.
- **HECHO** — Fix sesión SSR portado desde KaiPetPoint (`9d76aa1` en `feat/paletas-tema`): `ssrCookieInterceptor` + `AuthService` sin guard de plataforma. Diferencia vs kit: este front **no** tiene http-error interceptor, el de cookie quedó como único interceptor. F5 ya no cierra sesión.
- **HECHO** — Fix tooltip portado desde KaiPetPoint (`4b3105f`): `DomPortal` de CDK 22 exige `parentNode` — el nodo se ancla a `body` antes de adjuntar. Aplicaba a sidebar compacto y cualquier `appTooltip`. Spec de regresión incluido.
- **RAMAS PENDIENTES de merge/push**: `feat/paletas-tema` (incluye login + fixes SSR/tooltip), `chore/credenciales-seed-unificadas`.
- **HECHO** — Sistema de diálogos modales portado desde KaiPetPoint (`4a3cd6d`, rama `feat/paletas-tema`): piel única `.dialogo`, `ConfirmarDialogoComponent` + `confirmar()` con iconos de alerta, `app-dialogo-x`. 6 páginas convertidas de formulario inline (que empujaba el layout) a modal: familias, especies, temporadas, trabajadores, contratos y usuarios. Los 6 `window.confirm` de eliminación reemplazados por el diálogo compartido (botón rojo destructivo). **PENDIENTE** — los `alert()` de error en deletes siguen nativos; evaluar toast o diálogo de error en una fase posterior. lint · 12/12 · build verdes.
