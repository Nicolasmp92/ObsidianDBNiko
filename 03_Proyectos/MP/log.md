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
