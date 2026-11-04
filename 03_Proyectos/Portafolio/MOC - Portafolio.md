---
tipo: moc
estado: activo
actualizado: 2026-10-14
tags: [portafolio, github-pages, angular]
---

# MOC — Portafolio (Nicolasmp92.github.io)

Sitio personal público en GitHub Pages. Angular + Bootstrap, deploy por `angular-cli-ghpages`.

## Navegación por necesidad

- **Quiero ver qué pasó** → [[log]]
- **Quiero la tabla fecha/actividad/evidencia** → [[registro_actividades]]

## Datos operativos

- Repo: `C:\Users\Niko\Desktop\Desarrollo\Nicolasmp92.github.io`
- Sitio: https://nicolasmp92.github.io/
- **Publicar:** `npx ng deploy` (push a `main` NO publica — el sitio vive en la rama `gh-pages`)
- Proyectos/capturas: array `projects` en `src/app/components/experience/experience.component.ts`, imágenes en `public/img/`
- CV descargable: `public/pdf/Nicolas_Munoz_Palacios_CV.pdf` (enlazado desde `home.component.html`); plantilla fuente en `Desarrollo/.shots/cv-nuevo.html`
- Generador de capturas de los proyectos: `Desarrollo/.shots/capture.js` (puppeteer-core + Chrome local, login por inyección de cookie)
