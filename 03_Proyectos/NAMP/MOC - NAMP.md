---
tipo: moc
estado: activo
actualizado: 2026-10-18
tags: [web, corporativo, portafolio, angular, ssr]
---

# MOC — NAMP (namp-ingenieria)

Plataforma web de NAMP: empresa de servicios informáticos. Nace como portafolio público y escala a módulos de servicios (consultoría, desarrollo a medida). Angular 22 SSR, standalone, tema dark/light nativo, sin librerías de UI (todo a medida).

## Navegación por necesidad

- **Quiero ver qué pasó y cuándo** → [[log]]
- **Quiero la tabla fecha/actividad/evidencia** → [[registro_actividades]]
- **Quiero las reglas del repo** → `.devin/rules/namp-rules.md` (screaming architecture, standalone, dark-first, dorado + esmeralda, mobile-first)

## Datos operativos

- Repo local: `C:\Users\Niko\Desktop\Desarrollo\namp-ingenieria` (renombrada de `nye-ingenieria` el 2026-10-24)
- Remote: `Nicolasmp92/namp-ingenieria` (`origin` local ya actualizado)
- Proyectos del portafolio: `src/app/portfolio/portfolio.data.ts` — fuente de verdad (interface `Project` + `PROJECTS`)
- Imágenes de tarjetas: `public/img/projects/` en WebP (sharp-cli, max 1440px, desde capturas del portafolio personal)
- Generador de captura del propio portafolio: `Desarrollo/.shots/capture-portafolio.js` (puppeteer-core + Chrome local, sin login)
- Rutas: `''` home · `/portfolio` · `/servicios` · `/contacto` — todas prerenderizadas
