# Log — Portafolio (Nicolasmp92.github.io)

Bitácora append-only. Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO.

- **HECHO** — Poblado con proyectos del stack nuevo (2026-10-14, `9f9378d`): BeanFlow, KaiPetPoint, StarterCustomeKit y Frunexis agregados al array `projects` de `experience.component.ts` con capturas reales de vistas autenticadas (22 screenshots generados con puppeteer-core desde `Desarrollo/.shots/capture.js`, copiadas a `public/img/`).
- **DECISIÓN** — Deploy por `ng deploy` (angular-cli-ghpages → rama `gh-pages`), **no** por push a `main`: `main` guarda el fuente; el sitio público se publica solo con `npx ng deploy` (build producción + push a `gh-pages`). baseHref `/` por dominio propio.
- **HECHO** — CV regenerado con el formato original (2026-10-14, `ae318e7`): nuevo cargo al tope — Coordinador de Infraestructura de Información Científica, Universidad de O'Higgins (2026–Actualidad). HTML replicando el diseño → PDF con puppeteer → páginas 3-4 (certificados de título escaneados) injertadas del PDF original con `pdf-lib`. Skills actualizados con stack vigente (Java/Spring Boot, Angular).
- **HECHO** — `chileagrofood` eliminado de proyectos (2026-10-14).
- **RIESGO** — El CV es HTML estático en `.shots/cv-nuevo.html` (fuera del repo): si se regenera a futuro, conviene mover la plantilla al repo del portafolio para versionarla.
