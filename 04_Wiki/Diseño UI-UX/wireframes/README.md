---
tipo: herramienta
actualizado: 2026-11-18
tags: [wireframes, herramienta, svg]
---

# wire-gen — generador de wireframes SVG

Genera wireframes de vistas móviles en SVG desde specs JSON declarativas. Nació para ejemplificar las entradas de Diseño UI-UX (alternativa ligera a Balsamiq, pasó `interrogatorio-adopcion` como versión mínima).

## Uso

```bash
cd wireframes
python3 gen.py specs/*.json        # → 98_Assets/wire-<name>.svg
python3 gen.py specs/x.json -o     # SVG por stdout
```

Sin dependencias (stdlib only). Verificación visual: `google-chrome --headless --screenshot=out.png file://…svg`.

## Spec (vocabulario de la entrada 3)

```jsonc
{
  "name": "ficha-clinico",            // → wire-ficha-clinico.svg
  "caption": "texto bajo el teléfono", // opcional
  "appBar": {
    "leading": "back | menu | none",
    "title": "Dr. Pérez",
    "actions": ["search", "share", "more", "bell", "filter"]
  },
  "body": [ /* elementos apilados — tabla abajo */ ],
  "fab": {"label": "+", "position": "end | center | start"},   // opcional
  "bottomBar": {"type": "cta", "text": "Agendar hora"}          // opcional
            // o {"type": "nav", "items": ["Inicio", "…"]}
}
```

### Elementos del body (se apilan con padding 16 / gap 12)

| `type` | Campos | Renderiza |
|---|---|---|
| `header` | `badge` | Avatar círculo + 2 líneas de texto (+ pill) |
| `image` | `h`, `label` | Caja con X (placeholder de imagen) |
| `card` | `title`, `lines`, `action` | Card con skeleton + botón opcional |
| `list` | `title`, `items`, `trailing` | Filas avatar+texto (+ pill por fila) |
| `chips` | `labels` | Fila de pills de filtro |
| `text` | `lines` | Líneas skeleton de párrafo |
| `input` | `label`, `placeholder` | Campo de formulario |
| `button` | `text`, `variant: filled\|outline\|text` | Botón a lo ancho |
| `grid` | `cols`, `items` | Mosaico de tiles (íconos/categorías) |
| `section` | `text` | Etiqueta de sección |
| `divider` / `spacer` | — / `h` | Línea / hueco |

### Overlays

`"overlay": {"type": "sheet", "title", "lines", "button"}` → bottom sheet con dim; `"type": "dialog"` → diálogo centrado.

## Reglas de uso

- SVGs generados van a `98_Assets/wire-*.svg` y se embeben con `![[wire-x.svg]]`.
- La spec es la fuente de verdad — editar la spec y regenerar, nunca el SVG a mano.
- Estilo: grises wireframe + azul `#4285f4` solo para la acción primaria.
