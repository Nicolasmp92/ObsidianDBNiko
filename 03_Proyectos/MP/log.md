---
tipo: log
proyecto: mp
---
# 📓 Log — MP

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

---

## 2026-05-18 → 2026-05-22 — Levantamiento de requerimientos

- **HECHO** — [[MP - Requerimientos]] levantado por sección: logo (extraer PNG de tarjeta de presentación), hero (fondo + eslogan con "soluciones integrales, ingeniería, construcción, asesoría"), bento hero, 4 servicios, quiénes somos.
- **HECHO** — Arriendo de Equipos: propuesta tipo catálogo definida (2026-05-22). Falta listado de equipos (lo envía don Marcelo), buscador, "ver más" (mostrar solo los 6 importantes), sin valores.
- **DECISIÓN** — Responsables por sección: Obras Civiles → don Marcelo, Arriendo de Equipos y Capacitaciones → niko, Estudios de Suelo y bento hero → xelo.
- **RIESGO** — Insumos externos bloquean avance: logo original, listados de servicios (Obras Civiles, Estudios de Suelo), listado de equipos, imágenes para galerías.
- **HECHO** — Próxima reunión agendada: miércoles 23 de junio (hora por definir). Temas: misión/visión, correos con el server.

## 2026-10-16 — Auditoría + extracción de credenciales del mailer

- **HECHO** — Auditoría de experto sobre el repo (seguridad, performance, SEO). Hallazgo crítico: contraseña SMTP y secret de reCAPTCHA hardcodeadas en `src/mailer.php`, commiteadas al repo. Otros hallazgos pendientes: CORS `*`, FTP plano en deploy, hero.png de 7.5MB como LCP, `routes` vacío (SPA sin páginas indexables por servicio).
- **HECHO** — Credenciales removidas de `src/mailer.php`: ahora carga `mailer.config.php` (busca junto al script en `public_html` y un nivel por encima del webroot). `php -l` OK y build de producción verificado.
- **HECHO** — `src/mailer.config.php` creado con las credenciales reales **solo en este equipo** (Niko, `C:\Users\Niko\Desktop\Desarrollo\MP`); está en `.gitignore` (`/src/mailer.config.php`), nunca se versiona. `src/mailer.config.example.php` queda como plantilla versionada.
- **HECHO** — Pipeline (`.github/workflows/deploy.yml`) actualizado: genera `mailer.config.php` en `dist/MP/browser/` desde los secrets `SMTP_PASSWORD` y `RECAPTCHA_SECRET`, y **aborta el deploy si faltan** (protección para no publicar un mailer sin credenciales). Nuevo `public/.htaccess` que deniega acceso HTTP a `mailer.config*.php`, `composer.*` y `vendor/`.
- **DECISIÓN** — Fuente de verdad de credenciales: local → `src/mailer.config.php` (gitignored); CI → GitHub secrets; servidor → `public_html/mailer.config.php` generado por deploy. Los PHP del mailer solo se copian al bundle en build de producción (no se sirven por `ng serve`).
- **RIESGO** — Las credenciales **siguen en el historial de git** (commits anteriores, ya pusheados a GitHub). Quitarlas del HEAD no las compromete menos: hay que rotar la contraseña SMTP en cPanel y el secret de reCAPTCHA en Google, y luego actualizar `mailer.config.php` local + los secrets de GitHub.
- **RIESGO** — Pushear a `main` gatilla deploy: si los secrets `SMTP_PASSWORD`/`RECAPTCHA_SECRET` no están creados en GitHub, el workflow falla a propósito; el mailer antiguo en cPanel sigue operativo hasta que un deploy exitoso lo reemplace.
- **RIESGO** — El heredoc del workflow expande variables: la contraseña SMTP **no debe contener** `$`, comillas ni backticks, o el config generado quedará corrupto.

## 2026-10-16 (2) — CORS restringido en mailer.php

- **HECHO** — `Access-Control-Allow-Origin: *` reemplazado por whitelist `https://ingenieriamp.cl` + `https://www.ingenieriamp.cl`, con `Vary: Origin`. Orígenes ajenos reciben **403 antes de procesar** (defensa en profundidad). Requests sin `Origin` (curl/server-to-server) pasan: para ellos CORS no aplica y la barrera real es reCAPTCHA v3.
- **RIESGO** — El formulario en dev local (`ng serve`, Origin `http://localhost:4200`) ya **no puede** probarse contra el mailer de producción: será rechazado con 403. Para pruebas locales usar un mailer de staging o añadir temporalmente el origen local.
- **RIESGO** — El fix llega a producción solo cuando el deploy corra OK: requiere los secrets `SMTP_PASSWORD`/`RECAPTCHA_SECRET` en GitHub (pendiente desde la entrada anterior). Hasta entonces el mailer viejo sigue en cPanel con CORS `*`.

## 2026-10-16 (3) — Info disclosure en errores + hardening de archivos expuestos

- **HECHO** — El catch de `mailer.php` ya no devuelve `$mail->ErrorInfo` ni `$e->getMessage()` al cliente: ahora van a `error_log()` del servidor y el cliente recibe un mensaje genérico.
- **HECHO** — `.htaccess` ampliado: deniega `error_log` (en cPanel PHP escribe el log en `public_html/error_log`, que quedaría navegable y expondría el diálogo SMTP logueado — el fix de logging sin esta deny habría creado una nueva filtración), `*.md`, además de lo ya cubierto (`mailer.config*.php`, `composer.*`, `vendor/`).
- **RIESGO** — Todo lo de mailer sigue pendiente de publicación: requiere los GitHub secrets para que el deploy corra. Verificar el log de errores vía cPanel/FTP (HTTP denegado a propósito).

## 2026-10-18 — FTPS en deploy + hero.png migrado a WebP responsive

- **HECHO** — Deploy pasado de FTP plano a `protocol: ftps` (FTP-Deploy-Action): credenciales ya no viajan en claro. Si el servidor cPanel no acepta FTPS, el deploy fallará y habrá que evaluar `ftps-legacy` o sftp.
- **HECHO** — `hero.png` (7.5MB, 2752×1536) reemplazado por WebP responsive generado con sharp-cli: `hero-768.webp` 54KB, `hero-1280.webp` 126KB, `hero-1920.webp` 243KB (~97% menos). `hero.ts` usa `srcset`/`sizes="100vw"`; el preload de `index.html` usa `imagesrcset`/`imagesizes`/`type="image/webp"` sincronizado.
- **HECHO** — Nuevo `hero-og.jpg` (1200×630, 145KB) para `og:image`/`twitter:image`/JSON-LD: los scrapers sociales no siempre aceptan WebP y un PNG de 7.5MB podía agotar su timeout.
- **HECHO** — Eliminados `hero.png` y `hero2.png` (7.9MB, sin referencias). Carpeta `public/hero/`: 16MB → 584KB.
- **RIESGO** — Quedan ~29MB de imágenes sin optimizar en `obras-civiles/`, `equipos/`, `suelos/`, `sin-categorizar/` — el mismo tratamiento WebP conviene aplicarlo a galerías y `heroImage` de servicios.

## 2026-10-18 (2) — Lazy loading, assets muertos y reCAPTCHA on-demand

- **HECHO** — `service-detail.ts`: los 4 `loading="eager"` (heroes de detalle) pasados a `lazy`. El componente solo existe en el DOM al abrir un detalle (`@if currentArea()`), así que el eager forzaba descargas innecesarias si quedaba offscreen.
- **HECHO** — `public/sin-categorizar/` eliminada completa (11 archivos, 7.5MB): auditoría confirma **cero referencias** en `src/`. Assets: `public/` 45MB → 23MB. Recuperables desde historial de git si alguno se necesitaba.
- **HECHO** — reCAPTCHA v3 ya no carga global en `index.html`: `RecaptchaService` inyecta el script bajo demanda (`loadScript()` con promesa memoizada y retry tras error). `preload()` se llama al abrir el modal de contacto → token listo antes del envío. El timeout de 8s ahora cubre carga del script + ready + execute. Menos TBT y menos tracking de Google en visitas que no usan el formulario.
- **RIESGO** — Si el script de Google falla al cargar (adblock/red), `execute()` rechaza y el formulario muestra error — comportamiento correcto, pero antes el script ya venía cargado desde el HTML: conviene probar el envío real en producción tras el deploy.

## 2026-10-18 (3) — Rutas prerenderizadas por servicio + cierre de deuda menor

- **HECHO** — El sitio deja de ser una sola página: `''` → `HomeComponent`, `'servicios/:slug'` → `ServiceDetailPageComponent` (slugs: `obras-civiles`, `arriendo-de-equipos`, `estudios-de-suelo`), `'**'` → redirect home. Build prerenderiza **4 rutas** con `<title>`, description, og:* y canonical propios por servicio (verificado en `dist/browser/servicios/*/index.html`). Tarjetas de servicio ahora son `<a routerLink>` reales — crawlers pueden seguirlas.
- **HECHO** — Datos de servicios extraídos a `src/app/data/services.data.ts` (fuente de verdad: `SERVICE_DETAILS`, `SERVICE_SLUGS`, `serviceBySlug`). Nuevo `SeoService` (title/meta/canonical por ruta). Navbar es router-aware: anchors `#` navegan a `/` + fragment desde páginas de detalle. `anchorScrolling` + `scrollPositionRestoration` habilitados.
- **HECHO** — `robots.txt` y `sitemap.xml` creados en `public/` (antes existían solo en un dist antiguo — no estaban versionados). Sitemap lista las 4 rutas.
- **HECHO** — Galerías convertidas a WebP con sharp-cli (73 archivos jpg/png → webp, max 1920px, q80): `obras-civiles`, `suelos`, `equipos`. Referencias actualizadas en `services.data.ts`. `public/` quedó en ~22MB todo-webp.
- **HECHO** — Naming: `contact.service.ts` → `contact-info.service.ts` (`ContactInfoService`), `contacto.service.ts` → `mailer.service.ts` (`MailerService`). Eliminado `testimonials.ts` (dead code). `telefono` ahora es campo propio del payload (`CorreoPayload.telefono` → línea "Teléfono:" en el correo, mailer.php actualizado).
- **HECHO** — WhatsApp FAB (bottom-right, `wa.me/56976481490` con mensaje prellenado) junto al de Instagram. `AnalyticsService` creado: page_view por navegación + evento `generate_lead` en envíos exitosos; es no-op hasta descomentar el snippet GA4 en `index.html` (falta Measurement ID real — **pendiente del cliente/niko**).
- **HECHO** — Tests: 4 specs nuevos (ContactInfoService, ContactModalService, RecaptchaService timeout, services.data) + fix del spec obsoleto de App. `ng test`: **14/14 pasan**. CI: `checkout@v4` + `cache: npm`. Budget initial subido a 650kB (router añadió ~17kB).
- **RIESGO** — GA4 inactivo hasta crear la propiedad y poner el ID en `index.html`. El deploy sigue bloqueado por los secrets `SMTP_PASSWORD`/`RECAPTCHA_SECRET`.

## 2026-10-18 (4) — Revertir WhatsApp FAB: el cliente no lo quiere

- **DECISIÓN** — El cliente **no quiere WhatsApp como canal del sitio** (ya lo había rechazado antes; el FAB agregado por sugerencia fue revertido). Registrado también en `MP - Requerimientos` sección "Restricciones del cliente" para no volver a proponerlo. Canales válidos: formulario/mailer, teléfonos, Instagram.
- **HECHO** — WhatsApp FAB eliminado de `app.html`; queda solo el FAB de Instagram (bottom-left).

## 2026-10-25 — Crédito "Creado por NAMP" + deploys rotos descubiertos

- **HECHO** — Footer: línea "Creado por NAMP Ingeniería" → `https://namp.cl` (target blank). Commit `e8c9dba` en `main`.
- **RIESGO CRÍTICO** — **Todos los deploys a cPanel fallan desde el 17-oct**: GitHub Actions en rojo (~1 min cada run). Último deploy OK: **15-ago** — prod en `ingenieriamp.cl` corre build viejo (`Last-Modified` lo confirma): los commits de oct (seguridad SMTP/recaptcha, perf hero WebP, revert WhatsApp FAB, prerender por servicio) **nunca se publicaron**. Hipótesis principal: el step "Generar mailer.config.php" aborta si faltan los secrets `SMTP_PASSWORD`/`RECAPTCHA_SECRET` — guard introducido justo en los commits de seguridad del 17-oct que nunca despegaron.
- **PENDIENTE (Niko)** — Revisar run fallido en Actions (step rojo + error) y/o verificar que existan los secrets `SMTP_PASSWORD`, `RECAPTCHA_SECRET`, `FTP_*` en Settings → Secrets. Hasta que se arregle, nada de lo pusheado a `main` llega a prod.

## 2026-10-27 — Deploys desbloqueados: secrets creados

- **HECHO** — Confirmado el diagnóstico del 25-oct: en Settings → Secrets solo existían `FTP_*`; faltaban `SMTP_PASSWORD` y `RECAPTCHA_SECRET` (el guard del workflow abortaba sin ellos desde el 17-oct). Niko los creó desde cPanel + reCAPTCHA admin.
- **HECHO** — Deploy gatillado con commit vacío `3057e12`: workflow verde, FTP OK. `ingenieriamp.cl` ya sirve el build del 27-oct (Last-Modified confirma) — publicado TODO lo acumulado desde el 15-ago: crédito "Creado por NAMP" en footer, páginas por servicio con SEO, WebP, revert WhatsApp FAB, seguridad mailer.
- **VERIFICADO** — `https://ingenieriamp.cl` contiene "Creado por NAMP" + link a namp.cl en el HTML servido.
- **HECHO** — Repo clonado en este equipo (`~/Escritorio/Desarrollo/mp`); remote renombrado `mp` → `MP` en GitHub (origin actualizado).
- **PENDIENTE leve** — GA4 sigue sin Measurement ID en index.html; revisar que el formulario de contacto envíe correo real con el mailer ya deployado.

## 2026-11-24 — Insignia NAMP orbital en footer + deploy bloqueado (FTP 530)

- **HECHO** — Crédito "Desarrollado por NAMP Ingeniería · namp.cl" con la marca orbital animada completa (mismo componente que footer del portafolio y navbar de namp.cl, clases `namp-*`): N trazada, cometas, plano orbital, Capricornio. `currentColor` para tema claro/oscuro, `prefers-reduced-motion` ok. Sustituye al crédito de texto plano (`e8c9dba`, quedaba absorbido en el merge de origin/main → refactor).
- **HECHO** — Merge `origin/main` → `refactor/services-UIUX-refactor` (conflicto en footer.ts resuelto: insignia animada + su separador border-t) → ff a `main` (`49c2dc3`) → push gatilla Actions.
- **BLOQUEO** — Deploy FTP a cPanel **falló con `530 Login authentication failed`** (secrets FTP_USERNAME/FTP_PASSWORD inválidos o rotados desde el último deploy OK del 27-oct). Requiere actualizar secrets en GitHub o subir `dist/MP/browser/` manual al hosting LiteSpeed (147.124.195.39). 
- **CORRECCIÓN (25-11)** — El "RIESGO" del guard de secrets era lectura errada: el `exit 1` sí existe y el paso pasó OK (los `::error::` en el log eran el texto del script, no su ejecución). SMTP_PASSWORD/RECAPTCHA_SECRET siguen presentes. Único fallo real: FTP 530.

## 2026-11-25 — Deploy desbloqueado: insignia NAMP live en ingenieriamp.cl

- **HECHO** — Diagnóstico FTP completo: la cuenta `niko_ftp@ingenieriamp.cl` estaba chrooteada a `~/niko_ftp` (carpeta vacía) — por eso el 530/despiste. Recreada con `Directory: public_html` (cuenta dedicada de deploys, mejor que usar `ingenier5`).
- **HECHO** — Secrets `FTP_USERNAME`/`FTP_PASSWORD` actualizados por API (PyNaCl sealed box + token de git credential).
- **BUG DEPLOY** — Primer run verde pero sin efecto: `server-dir: /public_html/` + cuenta ya chrooteada a public_html = upload anidado en `public_html/public_html/`. Fix `server-dir: /` en `c281ae5` (rama `fix/ftp-server-dir`). Restos del upload anidado borrados por FTP.
- **HECHO** — Run `c281ae5` success → `ingenieriamp.cl` sirve `main-ZRGQAXSQ.js` con `namp-credit`/`namp-logo-n` verificados. La insignia orbital NAMP ("Desarrollado por NAMP Ingeniería · namp.cl") está live. Publicó además todo lo acumulado del merge (Obras Civiles refactor, páginas por servicio, etc.).
- **NOTA** — Workflow ahora 100% funcional: push a `main` → Actions → FTP correcto. Cuenta `niko_ftp` chrooteada a public_html (superficie mínima).

## 2026-11-25 (2) — Insignia NAMP como card + fix portafolio base href

- **HECHO** — El crédito inline pasó a card bordeada como la del footer del portafolio: caja `rounded-xl border` con sombra, eyebrow "DESARROLLADO POR", "NAMP Ingeniería" en semibold y "namp.cl" en dorado, marca orbital w-11. Commit `5eea6ad` → Actions success → live (`main-P6MVGYAW.js`).
- **BUG PORTAFOLIO** — `nicolasmp92.github.io` no renderizaba: el último `npx ng deploy --base-href=/` corrió en Git Bash y MSYS convirtió `/` en `C:/laragon/bin/git/` — el `<base href>` apuntaba a una ruta local y todos los assets 404. Fix: `MSYS_NO_PATHCONV=1 npx ng deploy --base-href=/`. **Regla: siempre anteponer MSYS_NO_PATHCONV=1 a ng deploy con flags que lleven / en Git Bash.**
