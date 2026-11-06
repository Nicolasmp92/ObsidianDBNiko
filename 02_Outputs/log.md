# Log — 02_Outputs (entregables)

Registro append-only de todo lo producido para entregar: posts, informes,
propuestas, presentaciones. Convención: subcarpeta por proyecto
(`02_Outputs/<proyecto>/`), nombre con fecha `YYYY-MM-DD-<slug>`.

Entradas tipificadas: ENTREGADO / BORRADOR / DECISIÓN.

## 2026-11-11

- **DECISIÓN** — Se crea `02_Outputs/` como zona de entregables del vault:
  separa "lo producido" de "lo en curso" (03_Proyectos) y de la captura
  (01_Inputs). Ref: `estructura.md` + Convenciones del Vault.
- **PENDIENTE** — Posts de Instagram de MP y NAMP viven en sus repos satélite
  (`<repo>/instagram/`); registrar aquí referencias cuando se publiquen, no
  duplicar los archivos.

## 2026-11-06

- **BORRADOR** — Media kit Instagram NAMP en repo satélite `namp-ingenieria`, rama `feat/media-kit-instagram`: `instagram/` (brand/*.svg, avatar PNG, post-01-lanzamiento PNG con datos reales, plantillas feed/historia/destacada + previews, render.ps1, README del kit). Publicación pendiente: falta merge a `main` y handle de IG.
- **DECISIÓN** — Corrección del usuario: los entregables sí se copian físicamente a `02_Outputs/<proyecto>/` (la regla anterior de "no duplicar" queda solo como referencia cruzada; el vault es la fuente de entrega). Fuente editable espejo sigue en el repo satélite.
- **ENTREGADO** — `NAMP/2026-11-06-media-kit-instagram/`: media kit completo — isotipo SVG (mark + horizontal dark/light), avatar PNG, post lanzamiento PNG con datos reales, plantillas feed/historia/destacada + previews, render.ps1, README. Espejo en `namp-ingenieria` rama `feat/media-kit-instagram` (pendiente merge). Falta handle IG.
- **ENTREGADO (v2)** — `NAMP/2026-11-06-media-kit-instagram/` resincronizado: isotipo rediseñado (monograma N + arcos, sin fuentes) propagado a logos SVG, avatar, post-01 y plantillas. El mismo mark quedó integrado en la web (header/hero/favicon/og-cover) en `feat/media-kit-instagram` → `ddc26d1`.
