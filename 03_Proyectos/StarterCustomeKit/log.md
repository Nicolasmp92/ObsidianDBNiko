---
tipo: log
proyecto: startercustomekit
---
# 📓 Log — StarterCustomeKit

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

La bitácora técnica autoritativa vive en el repo (`log.md` + `registro_actividades.md`); esta nota resume hitos y decisiones para consulta desde el vault.

---

## 2026-10-02 — Migración al stack v2 (Angular + Spring Boot)

- **DECISIÓN** — El kit migra de Laravel/Livewire a **Angular 22 SSR + Spring Boot 3.5 + PostgreSQL**. Motivo: stack más empresarial, con más campo laboral, alineado con cabid. La v1 Laravel queda preservada en git (tag `v1-laravel`).
- **DECISIÓN** — Alcance MVP acotado por gate anti scope-creep ([[SCK - Alcance v2]]): auth dual (cookie web + Bearer móvil), usuarios, roles, health, items como dominio-plantilla, seed, paquete `.devin`. Regla de graduación: un dominio entra al kit solo cuando 2 proyectos reales lo necesiten.
- **HECHO** — Contenido del repo reemplazado en rama `feat/stack-v2-angular-spring`; mergeado a `main` vía PR #22.
- **HECHO** — Backend: JWT dual, `usuarios`, `items`, health, seed; `mvn test` + `package` verdes; smoke curls OK (cookie `sck_token` httpOnly + Bearer).
- **HECHO** — Frontend: Angular 22 SSR, login → me → logout E2E, proxy `/api` en dev y SSR con `FRUNEXIS_API_URL`-equivalente (`SCK_API_URL`); fix de Express consumiendo prefijo `/api` (pathRewrite) y `allowedHosts` con localhost.
- **HECHO** — Sidebar de la v1 **recreada** (no copiada): 3 estados (expandida 280px / compacta 84px / oculta), overlay móvil <1024px, tooltips portaleados con CDK Overlay, antiflash `sidebar-ready`, sticky `h-svh`. Commits `30f6964`, `9c76988`, `5dc5209`.
- **DECISIÓN** — Selector de layouts de menú **rechazado** por regla de graduación (0 proyectos lo necesitaban); el seam queda documentado, no implementado.
- **HECHO** — Bloque de puertos propio commiteado: API `8081`, front `4201`, SSR `4001` (mapa: DSpace-CRIS 8080/4200/4000 reservado · SCK 8081 · Frunexis 8082 · sconect 8083). PR #23.
- **HECHO** — PostgreSQL dedicada `sck`/`sck_user` (clave dev `sck_dev`); backend migrado de H2 a PG; seed persistido.
- **RIESGO** — Token de GitHub quedó expuesto en chat; pendiente revocación manual en Developer Settings. Remote del repo sigue en SSH sin clave registrada (push se hizo por HTTPS con credencial guardada).

## Pendientes / reglas vigentes

- Agregar dependencia o patrón difícil de revertir → skill `interrogatorio-adopcion` primero.
- Toda sesión abre/cierra con `continuidad-sesion`; los logs del repo son append-only (`guarda-edicion-concurrente`).
- Hosting del backend Java: pendiente (el deploy FTP→cPanel de la v1 no aplica; evaluar VPS/PaaS).

## 2026-10-03/04 — Paletas, login estándar, credenciales unificadas

- **HECHO** — Sistema de paletas de acento (`1754a65`, rama `feat/paletas-tema` sobre `feat/h1-enterprise`): 4 acentos vía `data-paleta`, tokens de estado `danger`/`success`/`warning`+`-soft`, selector con swatches en `/perfil`, anti-flash. 14 colores sueltos migrados a tokens.
- **HECHO** — Login estándar (`cf364da`, `feat/login-recordar`): recordar correo `sck.recordar-correo`, toggle clave, mailto soporte, bloque de marca.
- **HECHO** — Credenciales seed unificadas: `nikolasmp92@gmail.com`/`niko9214` (`chore/credenciales-seed-unificadas`).
- **HECHO** — Fix sesión SSR portado desde KaiPetPoint (`3abf342` en `feat/login-recordar`): `ssrCookieInterceptor` reenvía cookie a `/api/*` en el server, `AuthService` sin guard de plataforma, `httpErrorInterceptor` solo-browser. F5 ya no cierra sesión.
- **HECHO** — Fix tooltip portado desde KaiPetPoint (`e949d54`): `DomPortal` de CDK 22 exige `parentNode` — el nodo se ancla a `body` antes de adjuntar y se retira al ocultar. Spec de regresión incluido.
- **RIESGO** — `feat/h1-enterprise` sigue sin mergear a `main`.
- **HECHO** — Sistema de diálogos modales portado desde KaiPetPoint (`50891f6`, rama `feat/login-recordar`): piel única `.dialogo` en styles.css, `ConfirmarDialogoComponent` + helper `confirmar()` con iconos de alerta (triángulo rojo destructivo / info azul neutro), `app-dialogo-x` de cierre estándar. Formularios de usuarios e items-admin pasan a `ng-template` + `dialog.open`; `window.confirm` eliminado. Spec del diálogo incluido; lint · 25/25 · build verdes.
- **HECHO** — Shell completo portado desde KaiPetPoint (rama `feat/shell-kpp`, pusheada): topbar (toggle sidebar + ciclo tema + menú usuario), página `Mi cuenta` /perfil (datos, clave, preferencias), `PreferencesService` con tema/paletas/accesibilidad (claves `sck.*`), toasts globales, interceptores http-error + ssr-cookie en `app.config`, diálogos CDK, notas de versión, anti-flash en index.html, dark mode + 4 paletas + `.dialogo` en styles.css, fix tooltip DomPortal. Backend: `PUT /api/perfil` y `/api/perfil/clave` con re-emisión de JWT/cookie al cambiar correo. lint · 15/15 · build SSR · mvn · smoke HTTP 8/8 verdes.
- **RIESGO/CHOQUE** — `feat/shell-kpp` solapa con `feat/perfil-preferencias` y `feat/login-recordar` (sin mergear): ambas ya tenían perfil/preferencias/toasts/diálogos/interceptores hechos en casa. Versiones nuevas son más completas (4 paletas, toasts, backend perfil); las antiguas aportan lo suyo único: login recordar, CI pipeline, backend enterprise (flyway/RFC7807), CRUD usuarios mejorado, credenciales seed. Pendiente decidir orden de merge.
- **HECHO** — Consolidación en `main` (opción 1 del usuario): `feat/shell-kpp` mergeada primero (`683be4e`), luego `feat/login-recordar` (`ccb2bdb`, contiene todo `feat/perfil-preferencias`). Resolución: su versión para topbar (con campana placeholder de notificaciones), usuarios CRUD (búsqueda, edición, icon buttons, switch activo), items-admin en modal, login recordar/mostrar clave/marca, specs nuevos (perfil, topbar, usuarios, confirmar), auth.service con fix SSR (sin guard de plataforma — `/me` corre en server vía ssrCookieInterceptor), sidebar con logo, login prerender + resto Server; mi versión para app.config (locale es), shell con BotonNotas, toasts/dialogo-x canónicos KPP. Rescatado backend enterprise: Flyway (baseline-on-migrate adopta la BD real — verificado, `flyway_schema_history` creada y `ddl-auto: validate` pasa), RFC 7807 con mapa `errores` por campo, actuator health, OpenAPI/Swagger, CI GitHub Actions. Post-merge: 25/25 tests, lint, build SSR, smoke login+perfil+400-RFC7807+actuator+swagger verdes.
- **HECHO** — `feat/ci-workflow` era idéntico al ci.yml ya mergeado; ramas restantes (`dev`, `chore/puertos-propios`, `feat/h1-enterprise`, `feat/stack-v2-angular-spring`) vacías vs main.
