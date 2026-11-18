---
name: contenido-instagram
description: Produce piezas de Instagram (posts, historias, portadas de destacadas, carruseles) coherentes con la marca mediante plantillas HTML renderizadas a PNG con Chrome headless, captions incluidos. Usar siempre que se pida crear contenido, publicaciones, posts, historias, destacadas, carruseles o publicidad para Instagram/redes, actualizar un media kit, o renovar capturas de producto para piezas gráficas — aunque el usuario no diga "media kit" ni "render". No usar para publicar en Instagram ni para decidir handle/estrategia de cuenta (decisión humana).
---

# Contenido Instagram

## 1. Regla dura

Toda pieza deriva de la marca y los datos reales del proyecto: isotipo,
paleta, tipografía, servicios, precios y demos son los del sitio/repo,
nunca inventados ni placeholder. Si el sitio cambió, la pieza cambia:
releer la fuente antes de dibujar, no confiar en piezas antiguas.

La pieza se diseña en HTML/CSS autónomo y se exporta a PNG con Chrome
headless — no se editan PNGs a mano ni se maquetan en herramientas
externas. El PNG es artefacto; el HTML es la fuente versionable.

## 2. Formatos

| Pieza | Tamaño | Reglas |
|---|---|---|
| Post feed | 1080×1080 (o 1080×1350 en 4:5) | Una idea por pieza, un CTA |
| Historia | 1080×1920 | Zona segura: 250 px arriba y abajo sin texto |
| Portada destacada | 1080×1080 | Un glifo grande centrado; legible a ~60 px (círculo miniatura) |
| Carrusel | N páginas del mismo tamaño | Numeración solo si el contenido es secuencia |
| Avatar perfil | 1080×1080 | Pensado para crop circular; mark centrado con aire |

## 3. Pipeline de producción

1. **Fuentes de verdad**: leer el README del kit del proyecto y los
   tokens reales del sitio (`styles.scss`, componentes de marca). Si la
   pieza menciona servicios, precios o pantallas, cotejar contra el
   sitio/app reales antes de escribir el copy.
2. **Plantilla**: duplicar la plantilla del formato (`plantilla-*.html`)
   a `post-XX-slug.html` y editar solo las zonas marcadas. Cada HTML
   fija su tamaño en `html,body` y enlaza la fuente empaquetada del kit.
3. **Tipografía empaquetada**: la marca viaja como woff2 local en el kit
   (`fonts/` + `brand/fonts.css` con `@font-face`). Nunca depender de la
   fuente instalada en el PC — el render debe ser idéntico en cualquier
   máquina.
4. **Capturas de producto**: se toman de la app real con Playwright o
   Chrome headless (login demo → cerrar modales/tours/overlays →
   capturar la vista representativa) y se guardan en `assets/` del kit.
   Se renuevan cuando la app cambia.
5. **Render**: script del kit (`render.sh` / `render.ps1`) —
   `chrome --headless=new --screenshot --window-size=<ancho>,<alto>
   --hide-scrollbars --force-device-scale-factor=1
   --virtual-time-budget=8000`. El budget espera fuentes y assets.
6. **Revisión visual**: mirar el PNG a tamaño de consumo (~360 px de
   ancho para feed). Verificar: titular legible, nada cortado ni
   solapado, CTA único y accionable, footer con sitio/handle, acentos de
   color según reglas de marca.
7. **Caption**: se entrega junto a la pieza — primera línea que
   engancha, valor concreto, CTA con destino real, hashtags acotados y
   relevantes (no muro de tags).

## 4. Límites

- No publica en Instagram ni programa publicaciones.
- No decide handle, tipo de cuenta ni qué archivar/borrar: son
  decisiones del propietario y se registran como pendientes.
- No altera la marca (isotipo, paleta, jerarquía de acentos): si la
  marca no resuelve la pieza, la decisión sube al humano.
- Archivar antes de eliminar cualquier contenido existente.

## 5. Activación, procedimiento y verificación

Activar al crear contenido de Instagram/redes, al actualizar un media
kit o al renovar capturas de producto para piezas. Procedimiento:
fuentes de verdad → plantilla → render → revisión visual → caption.
Si falta el kit del proyecto, crear primero su base de marca
(isotipo, paleta, tipografía empaquetada, plantillas) antes que piezas
sueltas.

Salida declarada: piezas producidas vs. pedidas (denominador), ruta de
los PNG y sus fuentes HTML, caption propuesto por pieza, datos
cotejados con su fuente, y pendientes humanos (handle, publicación,
limpieza de cuenta).
