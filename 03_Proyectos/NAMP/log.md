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
