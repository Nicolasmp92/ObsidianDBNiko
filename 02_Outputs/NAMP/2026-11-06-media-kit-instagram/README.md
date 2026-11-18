# Media kit — NAMP Ingeniería (Instagram)

Piezas de marca para redes, derivadas 1:1 del sistema visual del sitio
(`src/styles.scss` + hero de `home`). Todo es HTML/SVG propio, sin
dependencias de build: se edita texto y se exporta a PNG con `render.sh`
(Linux/macOS) o `render.ps1` (Windows).

## Contenido

| Archivo | Uso | Tamaño |
|---|---|---|
| `brand/logo-mark.svg` | Isotipo (arcos + N) para fondos oscuros | 200×200 viewBox |
| `brand/logo-horizontal.svg` | Isotipo + wordmark, fondos oscuros | 640×200 viewBox |
| `brand/logo-horizontal-light.svg` | Isotipo + wordmark, fondos claros | 640×200 viewBox |
| `brand/fonts.css` | `@font-face` Inter variable empaquetada | — |
| `fonts/` | Inter 4.1 variable (woff2) + licencia OFL | ~340 KB |
| `avatar-instagram.png` | Foto de perfil (crop circular IG) | 1080×1080 |
| `post-01-lanzamiento.png` | Post de lanzamiento | 1080×1080 |
| `post-02-servicios.png` | Post de servicios (los 3 reales del sitio) | 1080×1080 |
| `post-03-kpp.png` | Post prueba social: POS KaiPetPoint real | 1080×1080 |
| `assets/` | Capturas reales para las piezas (kpp-pos/panel/demo) | — |
| `destacadas/` | Portadas de destacadas: servicios, proyectos, demo-kpp, contacto | 1080×1080 |
| `plantillas/plantilla-post.html` | Base para posts del feed | 1080×1080 |
| `plantillas/plantilla-historia.html` | Base para historias | 1080×1920 |
| `plantillas/plantilla-destacada.html` | Portadas de destacadas | 1080×1080 |

## Marca

- **Isotipo**: monograma **N** geométrica en trazo puro (path propio, sin
  fuente) dentro de dos arcos orbitales (dorado exterior, esmeralda
  interior, cada uno con su nodo) sobre anillos tenues. Mismo grafismo
  del hero y del header del sitio; no redibujarlo.
- **Wordmark**: `NAMP` bold con N dorado / AM neutro / P esmeralda +
  ` Ingeniería` o `INGENIERÍA` en dorado (como el header).
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

**Inter variable empaquetada** en `fonts/` (v4.1, OFL) enlazada vía
`brand/fonts.css` — los renders ya no dependen de la fuente instalada en
el PC y calzan con el sitio, que carga Inter real. Fallback: Segoe UI →
system-ui. Titulares 700 con tracking -2px; eyebrows en mayúsculas con
tracking amplio.

## Reglas de uso

- Isotipo solo sobre carbón/oscuro o con la variante `-light` en claro.
- La N siempre en color texto del tema; los arcos siempre dorado afuera
  y esmeralda adentro — no invertir ni recolorear.
- Dejar aire alrededor del isotipo ≥ el ancho del trazo de la N.
- En historias, respetar la zona segura (250px arriba y abajo sin texto).
- No usar otros colores de acento: dorado = lujo/CTA, esmeralda = innovación/eyebrow.
- Contenido siempre real: servicios, precios y demos son los del sitio
  (`/servicios`, `/precios`, demo.namp.cl), nunca inventados.

## Renderizar PNGs

```bash
cd instagram
./render.sh                                          # todas las piezas (Linux/macOS)
./render.sh plantillas/plantilla-post.html post-XX.png 1080 1080
```

```powershell
.\render.ps1                                          # todas las piezas (Windows)
.\render.ps1 -File plantillas\plantilla-post.html -Out post-XX.png
```

Ambos scripts esperan con `--virtual-time-budget` a que carguen fuentes
y assets. Para un post nuevo: copiar `plantillas/plantilla-post.html` a
`post-XX-slug.html`, editar las zonas `<!-- EDITAR -->` y renderizar.
Las capturas de `assets/` se renuevan con Playwright contra demo.namp.cl
(ver `post-03-kpp.html` para el formato de mockup de navegador).

## Pendientes

- [ ] Handle de Instagram de NAMP sin definir — agregar `@handle` en el
      footer de las piezas cuando exista.
- [ ] Historias reales para alimentar las destacadas (hoy solo hay
      portadas; `plantilla-historia.html` está lista).
