# Media kit — NAMP Ingeniería (Instagram)

Piezas de marca para redes, derivadas 1:1 del sistema visual del sitio
(`src/styles.scss` + hero de `home`). Todo es HTML/SVG propio, sin
dependencias: se edita texto y se exporta a PNG con `render.ps1`.

## Contenido

| Archivo | Uso | Tamaño |
|---|---|---|
| `brand/logo-mark.svg` | Isotipo (anillos + NAMP) para fondos oscuros | 200×200 viewBox |
| `brand/logo-horizontal.svg` | Isotipo + wordmark, fondos oscuros | 640×200 viewBox |
| `brand/logo-horizontal-light.svg` | Isotipo + wordmark, fondos claros | 640×200 viewBox |
| `avatar-instagram.png` | Foto de perfil (crop circular IG) | 1080×1080 |
| `post-01-lanzamiento.png` | Post de lanzamiento | 1080×1080 |
| `plantillas/plantilla-post.html` | Base para posts del feed | 1080×1080 |
| `plantillas/plantilla-historia.html` | Base para historias | 1080×1920 |
| `plantillas/plantilla-destacada.html` | Portadas de destacadas | 1080×1080 |

## Marca

- **Isotipo**: dos anillos orbitales (arco dorado exterior, arco esmeralda
  interior, cada uno con su nodo) + sigla `NAMP` — N dorado, AM texto,
  P esmeralda. Es el mismo grafismo del hero del sitio; no redibujarlo.
- **Wordmark**: `NAMP` bold + ` Ingeniería` en dorado (como el header).
- **Tagline**: «Ingeniería de software a medida».

## Paleta

| Token | Dark | Light |
|---|---|---|
| Fondo | `#0a0a0b` | `#fafafa` |
| Superficie | `#141416` / `#1d1d20` | `#ffffff` / `#f1f1f3` |
| Borde | `#2a2a2e` | `#e2e2e6` |
| Texto | `#f4f4f5` | `#18181b` |
| Muted | `#a1a1aa` | `#52525b` |
| Dorado | `#d4af37` | `#b8912b` |
| Esmeralda | `#10b981` | `#059669` |

## Tipografía

Inter → Segoe UI → system-ui (mismo stack del sitio). Titulares 700 con
tracking -2px; eyebrows en mayúsculas con tracking amplio.

## Reglas de uso

- Isotipo solo sobre carbón/oscuro o con la variante `-light` en claro.
- No cambiar el orden de colores de la sigla (N dorado / AM neutro / P esmeralda).
- Dejar aire alrededor del isotipo ≥ alto de una letra de la sigla.
- En historias, respetar la zona segura (250px arriba y abajo sin texto).
- No usar otros colores de acento: dorado = lujo/CTA, esmeralda = innovación/eyebrow.

## Renderizar PNGs

```powershell
cd instagram
.\render.ps1                                          # todas las piezas
.\render.ps1 -File plantillas\plantilla-post.html -Out post-02-demo.png
```

Para un post nuevo: copiar `plantillas/plantilla-post.html` a
`post-XX-slug.html`, editar las zonas `<!-- EDITAR -->` y renderizar.

## Pendientes

- [ ] Handle de Instagram de NAMP sin definir — agregar `@handle` en el
      footer de las piezas cuando exista.
- [ ] Convertir textos de los SVG a outlines si el kit sale a terceros
      (hoy dependen de Inter/Segoe instalada).
