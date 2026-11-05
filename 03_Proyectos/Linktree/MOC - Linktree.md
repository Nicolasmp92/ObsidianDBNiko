---
tipo: proyecto
proyecto: linktree
estado: produccion
actualizado: 2026-11-05
tags: [uoh, angular, enlaces, bibliotecas]
---
# MOC — Linktree (página de enlaces Bibliotecas UOH)

Página de enlaces para la bio de Instagram `@bibliotecasuoh`, desarrollada para
la UOH — también sirve como portafolio personal. En producción.

## Navegación por necesidad

- **Quiero ver qué pasó** → `log.md` de esta carpeta
- **Quiero el resumen por sesión** → `registro_actividades.md`
- **Quiero el código** → `~/Escritorio/Desarrollo/linktree` (github.com/Nicolasmp92/linktree)
- **Quiero desplegar** → `npm run deploy-sexto` (ver ficha)

## Ficha

- **Stack:** Angular 22 standalone, CSS plano, página única. `npm start` → :4300
- **Deploy:** `npm run deploy-sexto` → `ssh sexto` → `E:\FTP\enlaces\` →
  `https://publicaciones.uoh.cl/enlaces/` (SEXTOPLANO, Windows IIS+FTP, cuenta
  prestada `cristobal.merchan@uoh.cl`)
- **Origen:** copia desde `repositorios-digitales-uoh/LINKTREE/` (repo privado
  institucional) — allí vive el historial completo de diseño

## Pendientes destacados (detalle en log.md)

- Usuario propio en sexto-130 (hoy cuenta prestada de Cristóbal).
- Renovación del wildcard `*.uoh.cl`: vence **27-dic-2026**, falta asignar dueño.
- Limpiar copias locales de la llave privada del wildcard (Descargas/certs, /tmp, E:\FTP\temp).
- Decidir qué sirve la raíz `publicaciones.uoh.cl/` (hoy 403).
