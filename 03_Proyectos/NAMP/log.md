---
tipo: log
proyecto: namp
---
# 📓 Log — NAMP

Bitácora narrativa **append-only**: las entradas nuevas van al final, nunca se reescribe el historial. Cada entrada se tipifica: **HECHO** (verificado con evidencia), **DECISIÓN** (qué se eligió y por qué), **HIPÓTESIS** (no confirmado aún), **RIESGO** (algo que puede romperse).

---

## 2026-10-18 — Portafolio poblado con proyectos reales

- **HECHO** — `src/app/portfolio/portfolio.data.ts` creado como fuente de verdad del dominio: interface `Project` (name, category, description, tags, image, link, status) + `PROJECTS` con 10 entradas — los 9 proyectos del portafolio personal (CABID, BeanFlow, KaiPetPoint, StarterCustomeKit, Frunexis, MP Ingeniería, RECOS, colegioangeles.cl, Tecnohoot) **más el propio portafolio** (nicolasmp92.github.io) como proyecto meta. Datos placeholder (E-commerce, App de Logística…) eliminados.
- **HECHO** — Tarjetas rediseñadas: captura real (o inicial con gradiente si falta imagen), categoría + estado, chips de stack y "Ver proyecto ↗" cuando hay link público.
- **DECISIÓN** — Filtros redefinidos por tipo de entrega: `Todos / Plataforma web / Sitio web` (antes Web/Mobile/Cloud, placeholders genéricos).
- **HECHO** — 10 capturas migradas del portafolio personal a `public/img/projects/` y convertidas a WebP con sharp-cli (7.9MB → ~630KB); screenshot de nicolasmp92.github.io generado con puppeteer desde `.shots/capture-portafolio.js`.
- **HECHO** — `ng build` OK (4 rutas prerenderizadas) + verificación visual con `ng serve`. Commit `d342e1d` pusheado a `main`.
- **HECHO** — Repo remoto renombrado en GitHub: `Nicolasmp92/nye-ingenieria` → `Nicolasmp92/namp-ingenieria`. `origin` local actualizado con `git remote set-url`; la carpeta local sigue llamándose `nye-ingenieria`.
- **RIESGO** — `cabid.cl` sigue resolviendo al sitio antiguo: la tarjeta de CABID no tiene link hasta apuntar el DNS al server nuevo (mismo RIESGO registrado en Portafolio).

## 2026-10-19 — Rebrand NYE → NAMP

- **HECHO** — Renombrado completo NYE → NAMP en el repo: marca visible (header brand, `<title>`, email de contacto `hola@nampingenieria.com`, README, comentario de `styles.scss`), proyecto Angular `NYEinformatica` → `nampingenieria` (dist + script `serve:ssr`), `storageKey` de tema `nye-theme` → `namp-theme`, spec del header actualizado, reglas `.devin/rules/nye-rules.md` → `namp-rules.md`. Commit `4fc03c9` pusheado a `main`.
- **HECHO** — `index.html` corregido a `lang="es"` (estaba en `en` pese a que todo el contenido es en español).
- **RIESGO** — La carpeta local sigue llamándose `nye-ingenieria`: el rename falló por bloqueo de archivos abiertos en el IDE. Renombrar manualmente con el IDE cerrado. El cambio de `storageKey` hace que usuarios previos pierdan la preferencia de tema guardada (vuelven a dark, que es el default — impacto nulo).
- **HIPÓTESIS** — El dominio de contacto `nampingenieria.com` es placeholder renombrado mecánicamente; confirmar el dominio real antes de publicar (igual que el teléfono `+58 000 000 0000` y "Caracas, Venezuela", que son placeholders del template — Chile usa `+56`).

## 2026-10-19 (2) — Logo hero a NAMP + destacados reales

- **HECHO** — Logo SVG del hero actualizado de NYE (3 letras) a NAMP (4): N dorada, A-M blancas, P esmeralda; posiciones x=64/88/112/136 (centrado en 100) y font-size 2.25rem → 2rem para acomodar la cuarta letra. Anillos orbitales intactos. Verificado con captura del render.
- **HECHO** — "Trabajos destacados" del home dejaba placeholders (E-commerce, Analítica, Logística): ahora toma `PROJECTS.slice(0,3)` de `portfolio.data.ts` (CABID, BeanFlow, KaiPetPoint) mostrando captura real en el thumb.
- **HECHO** — Commit `0917f8f` pusheado a `main`.

## 2026-10-20 — Proyectos inactivos ocultos

- **DECISIÓN** — `colegioangeles.cl` y `Tecnohoot` comentados en `PROJECTS` (no eliminados): están inactivos y si vuelven se remasterizan primero. Sus imágenes webp quedan en `public/img/projects/` para ese caso. El portafolio muestra 8 proyectos.
- **HECHO** — Verificado en el HTML prerenderizado de `/portfolio`: ambos nombres ausentes. Commit pusheado a `main`.

## 2026-10-20 (2) — Reorden del portafolio

- **HECHO** — `PROJECTS` reordenado: top 3 = KaiPetPoint, CABID, MP Ingeniería; luego Portafolio Personal y RECOS; cierre con BeanFlow, StarterCustomeKit, Frunexis. El home hereda el top 3 automáticamente (`PROJECTS.slice(0,3)` en destacados). Verificado en el HTML servido.

## 2026-10-24 — Carpeta local renombrada

- **HECHO** — `C:\Users\Niko\Desktop\Desarrollo\nye-ingenieria` → `namp-ingenieria`. El intento del 19-10 fallaba por procesos node huérfanos del `ng serve` y archivos abiertos en el IDE; hoy sin procesos activos el rename pasó limpio. Git, remote (`namp-ingenieria`) y reglas `.devin/rules/namp-rules.md` intactos. Local y remoto ahora usan el mismo nombre.

## 2026-10-24 — Deploy stack estático (Docker + nginx)

- **HECHO** — `namp.cl` ya resuelve al VPS (`200.141.25.56`) y responde 404 vía Traefik — DNS Cloudflare propagado; ítem 1 del plan de infra superado. Google ya indexa el dominio.
- **HECHO** — Artefactos deploy (`29963e9` en `main`): `Dockerfile` (node build → `nginx:alpine` sirviendo `dist/nampingenieria/browser`), `nginx.conf` (cache 1y assets, fallback SPA, redirect www→namp.cl), `docker-compose.yml` (servicio `web` puerto 80, dominios vía Dokploy). NAMP es 100% prerenderizado → estático, sin Node en prod.
- **VERIFICADO** — Imagen `namp-web` construida local: `/`, `/portfolio`, `/servicios`, `/contacto` y rutas inexistentes → 200 (fallback SPA).
- **DECISIÓN** — Deploy por Dokploy (Traefik ya gestiona HTTPS), no por compose manual.
- **PENDIENTE** — Crear servicio compose `namp-web` en Dokploy (repo `namp-ingenieria`, branch `main`), dominios `namp.cl` + `www.namp.cl` → `web:80`, deploy. Este PC no tiene llave SSH del VPS (vive en el note TUF): se generó `id_ed25519` local pendiente de autorizar en `authorized_keys`.

## 2026-10-24 (pm) — namp.cl en producción

- **HECHO** — `https://namp.cl` responde 200 con certificado Let's Encrypt (Traefik/Dokploy); `www.namp.cl` → 301 → apex. Deploy vía Dokploy: proyecto `namp`, servicio compose `web` (repo `namp-ingenieria`, branch `main`, `./docker-compose.yml`), Trigger **On Push** (cada push a main redespliega solo), dominios `namp.cl`+`www.namp.cl` → `web:80` con HTTPS.
- **HECHO** — GitHub App `Dokploy-2026-10-23-i5n9be` ampliada a `namp-ingenieria` para acceso al repo.
- **NOTA** — En Dokploy, los cambios de Domains requieren redeploy manual para que Traefik cree rutas/certs (el banner azul lo advierte); el primer deploy tardó ~2 min (npm ci + ng build) y los certs salieron a los ~60s del deploy.

## 2026-10-24 (noche) — SEO, footer y contacto real

- **HECHO** — SEO base (merge `efc5f72` en `main`, desplegado): `robots.txt`, `sitemap.xml` (4 rutas), meta description + Open Graph + Twitter card en `index.html`, `og-cover.png` de marca (1200×630, desde `og-cover.svg` con sharp-cli), `theme-color`, canonical por ruta. Servicio `src/app/shared/services/seo.ts` setea title/description/og:url/canonical por página — queda horneado en el prerender (verificado en dist).
- **HECHO** — Footer global (`d26a8e8`): `shared/layout/footer/` standalone — marca, nav, email, Santiago-Chile, copyright con año dinámico. Mobile-first con vars de tema.
- **HECHO** — Contacto real (merge `1f6e78d`): `contacto@namp.cl`, WhatsApp `+56 9 6397 8090` (`wa.me/56963978090`), Santiago, Chile. El formulario abre WhatsApp con mensaje pre-armado (nombre/email/mensaje → `wa.me?text=`); botón "Enviar por WhatsApp". WhatsApp también agregado al footer.
- **HECHO** — Tarjetas "Proyectos destacados" del home clickeables: nombre → link externo del proyecto (o `/portfolio` si no tiene), stretched-link en CSS. KPP: `link` GitHub → `https://kpp.namp.cl/` (ya en producción).
- **DECISIÓN** — Flujo de trabajo: ramas `feat/*` → merge a `main` (Dokploy autodespliega on push). Trabajo desde Devin Desktop con preview local en `ng serve`.
- **PENDIENTE** — CABID: agregar `link` en `portfolio.data.ts` cuando `cabid.cl` apunte al server nuevo (semanas próximas). Actualizar `sitemap.xml` al agregar rutas nuevas.

## 2026-10-24 — Cierre del día (estado final)

- **ESTADO** — `namp.cl` en producción (Dokploy, nginx estático, LE, autodeploy on push). `kpp.namp.cl` en producción (stack completo). Pendientes NAMP: datos de contacto reales en `/contacto` (tel +58 y Caracas son placeholders), agregar link de kpp.namp.cl a la tarjeta KPP del portfolio, y evaluar link/demo para CABID cuando apunte el DNS.

## 2026-10-25 — CTA visible en destacados del home

- **HECHO** — Tarjetas "Proyectos destacados": eran clickeables (stretched-link) pero sin señal consistente — CABID no mostraba cue alguna. Ahora todas llevan "Ver proyecto ↗" (externo) / "Ver detalle →" (sin link → `/portfolio`) en dorado bajo el nombre, estilo espejo de `portfolio__link`. Commit `b261a25` en `main`, verificado en prod (2↗ + 1→). Capturas de verificación: `Desarrollo/.shots/out/namp-home-*.png` (script `capture-namp-home.js`, sirve para capturar namp.cl o localhost).

## 2026-10-25 (2) — Formulario de contacto a correo (FormSubmit)

- **HECHO** — Descubierto: `namp.cl` no tiene MX ni SPF → `contacto@namp.cl` no puede recibir correos (rebota). VPS Hostinger KVM **no incluye email** (el "Free Business Email" es solo de planes web/cloud hosting; para VPS es add-on pago ~$1.59/mes).
- **DECISIÓN** — Combo elegido: **Cloudflare Email Routing** (gratis, forward `contacto@namp.cl` → correo real de Niko; CF agrega MX/SPF solo) + **FormSubmit** (gratis, sin cuenta, endpoint AJAX + honeypot). Rechazadas: Zoho (más setup), Hostinger Email (pago), mailer propio en VPS (puerto 25/PTR/spam — alto mantenimiento).
- **HECHO** — Formulario reimplementado (`3e3f6f3` + fix `911b826` en `main`): POST fetch a `formsubmit.co/ajax/contacto@namp.cl` con `_subject` (nombre), `_replyto` (email visitante), `_template: table`, `_captcha: false`, honeypot `_honey`; estados sending/sent/error con fallback a WhatsApp. Se valida `json.success === 'true'` (el endpoint devuelve 200 aun con `success:false`).
- **VERIFICADO** — Endpoint responde correcto: sin `Referer` lo rechaza (el browser lo manda), con `Referer` pide activación ("Activate Form" link por email). La activación re-dispara sola en el próximo submit.
- **PENDIENTE (Niko)** — 1) Activar Email Routing en Cloudflare → `contacto@namp.cl` → forward a su correo (verifica destino por email; CF agrega MX/SPF). 2) Enviar un mensaje de prueba en `namp.cl/contacto` → llega email de activación al correo real → click "Activate Form". 3) Listo: los submits siguientes llegan al inbox.

## 2026-10-25 (3) — Contacto: selector de canal correo/WhatsApp

- **HECHO** — Formulario con selector de canal (pills estilo filtros de portafolio): "Por correo" → FormSubmit (nombre/email/mensaje), "Por WhatsApp" → `wa.me` con mensaje pre-armado (nombre/mensaje). Signal `channel` en el componente; tabs con `role="tablist"`. Fix colateral: `.contact__info-link` → `display:block` (el label quedaba pegado al valor al reemplazar `<p>` por `<a>`). Commit `034caac` en `main`. Verificado con capturas puppeteer (`capture-namp-contacto.js`, acepta URL base por argv).

## 2026-10-25 (4) — Formulario de correo funcionando end-to-end

- **HECHO** — Cloudflare Email Routing activo en `namp.cl`: MX `route*.mx.cloudflare.net` + DKIM/SPF agregados por CF; regla `contacto@namp.cl` → Gmail de Niko (destino verificado). `contacto@namp.cl` recibe correo real.
- **HECHO** — FormSubmit activado (`success:true` verificado por POST al endpoint AJAX). **Gotcha**: cada submit a un form sin activar genera un NUEVO token que invalida los anteriores — con el delay del forwarding hay que abrir SOLO el email más reciente (los viejos dan "token not found").
- **HECHO** — Selector de canal en `/contacto` (pills estilo portfolio): "Por correo" → FormSubmit (nombre/email/mensaje, honeypot, reply-to del visitante, template table); "Por WhatsApp" → wa.me con mensaje pre-armado. Deploy `034caac` + `911b826`.
- **PENDIENTE leve** — `_captcha:false` + honeypot; si llega spam, activar captcha de FormSubmit o migrar a Web3Forms (key por email).

## 2026-10-27 — Responsivo móvil: header hamburguesa

- **HECHO** — Auditoría CDP a 360/320px: la nav inline (brand + 4 links + toggle ≈610px) forzaba el layout viewport a ~610px en TODAS las rutas → página entera "achicada" con links cortados. Fix `df31b3a` en `main` (autodeploy): menú hamburguesa ≤768px — dropdown full-width, botón 44px con aria-expanded/controls, cierre al navegar/Escape/resize; header semitransparente permanente; `overflow:clip` en hero (anillos SVG desbordaban); spec de App reparado (faltaba `provideRouter`, estaba roto en main) + tests del menú.
- **VERIFICADO** — Prod: `/`, `/portfolio`, `/servicios`, `/contacto` → `scrollWidth=360` sin elementos >361px; menú abre/cierra/navega OK (CDP); desktop ≥769px nav inline intacta.
- **DECISIÓN** — Repo `namp-ingenieria` clonado a `~/Escritorio/Desarrollo/namp-ingenieria` en este equipo (antes solo existía en el otro PC como `nye-ingenieria`).
- **PENDIENTE** — Notificaciones por correo de KPP diferidas hasta generar ingresos (ver [[../Empresa/log]] 2026-10-27).

## 2026-10-27 — Capa visual "detalle premium"

- **HECHO** — Rediseño con libertad total (`00076d3`, en prod): dos directivas nuevas en `shared/directives/` — `appReveal` (IntersectionObserver, fade-up al entrar al viewport, delay escalonado; la clase solo se agrega en browser → HTML prerenderizado nunca queda invisible/SEO seguro) y `appSpotlight` (halo dorado que sigue al cursor vía --mx/--my, solo puntero). Hero: entrada escalonada, resplandor aurora tras los anillos, cue de scroll → `#servicios`. Cinta marquee del stack tech. Header: barra de progreso de scroll (gradiente dorado→esmeralda). Thumbs de proyectos con zoom, CTA con borde en gradiente, selección dorada, scrollbar a tono, guion dorado en eyebrows. Todo respeta `prefers-reduced-motion`.
- **VERIFICADO** — 4/4 tests, build OK, prerender de 4 rutas; auditoría CDP en producción: las 4 rutas × 320/360/768/1280px con `scrollWidth` exacto, cero desbordes. Script reusable: `/tmp/namp-audit/audit.mjs` (CDP: screenshot + overflow por ruta/ancho).
- **DECISIÓN** — Budget `anyComponentStyle` sube de 4→8kB en `angular.json` (home.css quedó en 6.14kB; sigue siendo CSS artesanal mínimo).
- **PENDIENTE** — Ideas de siguiente nivel si se quiere: hero con texto en gradiente animado, sección de métricas/proceso, modo light con la misma capa de motion (ya funciona por tokens, sin QA visual dedicado).
- **HECHO** — Footer redistribuido estilo ingenieriamp.cl a pedido del usuario (`799c95c`, en prod): fila brand+tagline | copyright centrado | contacto con íconos (mail/WhatsApp); fila de ubicación (copyright migra aquí en móvil <720px); nav centrado; franja firma "Diseñado y construido a mano, sin plantillas." Todo con tokens NAMP, sin Tailwind. Tests 4/4, build OK.
