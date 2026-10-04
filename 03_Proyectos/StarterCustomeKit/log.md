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
- **RIESGO** — Bug de sesión en SSR (F5 cierra sesión) existe aquí también; el fix está probado en KaiPetPoint (`ssrCookieInterceptor`) — pendiente portar. Además `feat/h1-enterprise` sigue sin mergear a `main`.
