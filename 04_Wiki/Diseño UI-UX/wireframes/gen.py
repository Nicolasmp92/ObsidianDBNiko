#!/usr/bin/env python3
"""wire-gen — genera wireframes SVG de vistas móviles desde specs JSON.

Uso:
    python3 gen.py specs/*.json          # genera 98_Assets/wire-<name>.svg
    python3 gen.py specs/ficha.json -o   # imprime el SVG por stdout

La spec usa el vocabulario de la entrada 3 (composición de vistas):
    appBar    {leading: back|menu|none, title, actions: [search|share|more|bell|filter]}
    body      [elementos apilados — ver ELEMENTS]
    fab       {label: "+", position: end|center|docked}     (opcional)
    bottomBar {type: cta, text} | {type: nav, items: [...]} (opcional)
    overlay   {type: sheet|dialog, title, lines, button}    (opcional)

Sin dependencias: stdlib only. Los SVG usan grises de wireframe + un solo
acento azul para la acción primaria.
"""
import json
import sys
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[3] / "98_Assets"

# Lienzo y paleta (wireframe: grises + un acento para lo primario)
PW, PH, RX = 380, 800, 40          # phone width/height/radius
SCR = 20                            # borde interno del teléfono
STATUS_H, APPBAR_H = 28, 56
NAVBAR_H, CTABAR_H = 64, 84
PAD, GAP = 16, 12

C = {
    "frame": "#5f6368", "bg": "#ffffff", "region": "#f1f3f4",
    "line": "#dadce0", "skel": "#e8eaed", "txt": "#3c4043",
    "muted": "#9aa0a6", "pri": "#4285f4", "pritxt": "#ffffff",
    "safe": "#f8f9fa",
}

def esc(t):
    return escape(str(t), quote=True)

def R(x, y, w, h, fill=C["skel"], rx=4, stroke="none", sw=0, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}/>'

def T(x, y, t, size=12, fill=C["txt"], anchor="start", weight="normal"):
    return (f'<text x="{x}" y="{y}" font-family="system-ui,sans-serif" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}">{esc(t)}</text>')

def CIRC(cx, cy, r, fill=C["skel"], stroke="none", sw=0):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'

def LINE(x1, y1, x2, y2, stroke=C["line"], sw=1.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'

def icon(name, cx, cy, r=9, color=C["muted"]):
    """Glifos simples para appBar/botones."""
    if name == "back":
        return (LINE(cx + 4, cy, cx - 4, cy, color, 2) +
                LINE(cx - 4, cy, cx - 1, cy - 5, color, 2) +
                LINE(cx - 4, cy, cx - 1, cy + 5, color, 2))
    if name == "menu":
        return "".join(LINE(cx - r + 2, cy + dy, cx + r - 2, cy + dy, color, 2)
                       for dy in (-4, 0, 4))
    if name == "search":
        return (CIRC(cx - 1, cy - 1, r - 3, "none", color, 2) +
                LINE(cx + 4, cy + 4, cx + r - 1, cy + r - 1, color, 2))
    if name == "share":
        return (LINE(cx, cy + r - 2, cx, cy - r + 2, color, 2) +
                LINE(cx, cy - r + 2, cx - 4, cy - r + 6, color, 2) +
                LINE(cx, cy - r + 2, cx + 4, cy - r + 6, color, 2))
    if name == "more":
        return "".join(CIRC(cx, cy + dy, 1.8, color) for dy in (-5, 0, 5))
    if name == "bell":
        return CIRC(cx, cy, r - 3, "none", color, 2)
    if name == "filter":
        return "".join(LINE(cx - r + 2, cy + dy, cx + r - 2, cy + dy, color, 2)
                       for dy in (-4, 0, 4)) + "".join(
            CIRC(cx + dx, cy + dy, 2.2, C["region"], color, 1.5)
            for dx, dy in ((-3, -4), (3, 0), (-1, 4)))
    if name == "avatar":
        return CIRC(cx, cy - 2, r - 3.5, color) + R(cx - r + 2, cy + 3, 2 * r - 4, 6, color, 3)
    return CIRC(cx, cy, r - 3, "none", color, 2)  # fallback: círculo hueco

# ---------- elementos del body: cada uno devuelve (svg, alto) ----------

def el_header(x, y, w, e):
    out = [CIRC(x + 28, y + 30, 26, C["line"]),
           R(x + 68, y + 14, w - 68 - 60, 13, C["skel"], 6),
           R(x + 68, y + 36, w - 68 - 110, 10, C["skel"], 5)]
    if e.get("badge"):
        out.append(R(x + w - 52, y + 18, 44, 18, "none", 9, C["line"], 1.2))
    return "".join(out), 64

def el_image(x, y, w, e):
    h = e.get("h", 140)
    out = [R(x, y, w, h, C["region"], 8, C["line"], 1.2),
           LINE(x + 8, y + 8, x + w - 8, y + h - 8, C["line"], 1),
           LINE(x + w - 8, y + 8, x + 8, y + h - 8, C["line"], 1)]
    if e.get("label"):
        out.append(T(x + w / 2, y + h / 2 + 4, e["label"], 11, C["muted"], "middle"))
    return "".join(out), h

def el_card(x, y, w, e):
    lines = e.get("lines", 2)
    h = 20 + lines * 16 + (26 if e.get("action") else 8)
    out = [R(x, y, w, h, "none", 8, C["line"], 1.4)]
    if e.get("title"):
        out.append(T(x + 14, y + 22, e["title"], 12, C["txt"], "start", "600"))
    for i in range(lines):
        lw = w - 28 - (40 if i == lines - 1 else 0)
        out.append(R(x + 14, y + 34 + i * 16, lw, 9, C["skel"], 4.5))
    if e.get("action"):
        out.append(R(x + w - 76, y + h - 34, 62, 24, "none", 6, C["line"], 1.4))
        out.append(T(x + w - 45, y + h - 18, e["action"], 10, C["muted"], "middle"))
    return "".join(out), h

def el_list(x, y, w, e):
    items = e.get("items", 3)
    h = (26 if e.get("title") else 0) + items * 52
    out = []
    y0 = y
    if e.get("title"):
        out.append(T(x, y0 + 16, e["title"], 12, C["muted"], "start", "600"))
        y0 += 26
    for i in range(items):
        ry = y0 + i * 52
        out += [CIRC(x + 20, ry + 22, 16, C["line"]),
                R(x + 48, ry + 12, w - 48 - 70, 11, C["skel"], 5.5),
                R(x + 48, ry + 30, w - 48 - 130, 8, C["skel"], 4)]
        if e.get("trailing"):
            out.append(R(x + w - 56, ry + 12, 48, 22, "none", 6, C["line"], 1.2))
        if i < items - 1:
            out.append(LINE(x + 48, ry + 50, x + w, ry + 50, C["line"], 1))
    return "".join(out), h

def el_chips(x, y, w, e):
    labels = e.get("labels", ["chip", "chip", "chip"])
    out, cx = [], x
    for lb in labels:
        cw = len(lb) * 7.5 + 26
        out.append(R(cx, y, cw, 30, "none", 15, C["line"], 1.4))
        out.append(T(cx + cw / 2, y + 19, lb, 11, C["txt"], "middle"))
        cx += cw + 8
    return "".join(out), 30

def el_text(x, y, w, e):
    lines = e.get("lines", 2)
    out = [R(x, y + i * 16, w - (i == lines - 1) * 70, 10, C["skel"], 5)
           for i in range(lines)]
    return "".join(out), lines * 16 - 6

def el_input(x, y, w, e):
    h = 52 if e.get("label") else 36
    out = []
    if e.get("label"):
        out.append(T(x, y + 12, e["label"], 11, C["muted"]))
        y += 20
    out.append(R(x, y, w, 36, "none", 8, C["line"], 1.4))
    if e.get("placeholder"):
        out.append(T(x + 12, y + 22, e["placeholder"], 11, C["muted"]))
    return "".join(out), h

def el_button(x, y, w, e):
    v = e.get("variant", "filled")
    txt = e.get("text", "Acción")
    if v == "text":
        return T(x + w / 2, y + 20, txt, 12, C["pri"], "middle"), 30
    fill = C["pri"] if v == "filled" else "none"
    stroke = "none" if v == "filled" else C["line"]
    tc = C["pritxt"] if v == "filled" else C["txt"]
    return (R(x, y, w, 44, fill, 10, stroke, 1.4) +
            T(x + w / 2, y + 27, txt, 13, tc, "middle", "600")), 44

def el_grid(x, y, w, e):
    cols, n = e.get("cols", 4), e.get("items", 8)
    cell, gap = (w - (cols - 1) * 10) / cols, 10
    rows = -(-n // cols)
    out = []
    for i in range(n):
        cx, cy = x + (i % cols) * (cell + gap), y + (i // cols) * (cell + 24 + gap)
        out.append(R(cx, cy, cell, cell, "none", 8, C["line"], 1.4))
        out.append(CIRC(cx + cell / 2, cy + cell / 2, cell / 3.2, C["skel"]))
        out.append(R(cx + cell * 0.18, cy + cell + 6, cell * 0.64, 7, C["skel"], 3.5))
    return "".join(out), rows * (cell + 24) + (rows - 1) * gap

def el_section(x, y, w, e):
    return T(x, y + 14, e.get("text", "Sección"), 11, C["muted"], "start", "600"), 22

def el_divider(x, y, w, e):
    return LINE(x, y + 4, x + w, y + 4, C["line"], 1), 8

ELEMENTS = {
    "header": el_header, "image": el_image, "card": el_card, "list": el_list,
    "chips": el_chips, "text": el_text, "input": el_input, "button": el_button,
    "grid": el_grid, "section": el_section, "divider": el_divider,
    "spacer": lambda x, y, w, e: ("", e.get("h", 24)),
}

# ---------- regiones ----------

def app_bar(x, y, w, ab):
    out = [R(x, y, w, APPBAR_H, C["region"], 0)]
    lx = x + 16
    if ab.get("leading", "back") != "none":
        out.append(icon(ab.get("leading", "back"), lx + 6, y + APPBAR_H / 2))
        lx += 36
    out.append(T(lx, y + APPBAR_H / 2 + 5, ab.get("title", ""), 15, C["txt"], "start", "600"))
    ax = x + w - 16
    for a in ab.get("actions", [])[:3]:
        out.append(icon(a, ax - 9, y + APPBAR_H / 2))
        ax -= 34
    out.append(LINE(x, y + APPBAR_H, x + w, y + APPBAR_H, C["line"], 1))
    return "".join(out)

def bottom_bar(x, y, w, bb):
    if bb.get("type", "nav") == "cta":
        out = [R(x, y, w, CTABAR_H, C["bg"], 0),
               LINE(x, y, x + w, y, C["line"], 1)]
        bx, bw = x + PAD, w - 2 * PAD
        out.append(R(bx, y + 18, bw, 48, C["pri"], 12))
        out.append(T(x + w / 2, y + 48, bb.get("text", "Acción"), 14, C["pritxt"], "middle", "600"))
        return "".join(out), CTABAR_H
    items = bb.get("items", ["Inicio", "Buscar", "Perfil"])[:5]
    out = [R(x, y, w, NAVBAR_H, C["region"], 0),
           LINE(x, y, x + w, y, C["line"], 1)]
    cw = w / len(items)
    for i, lb in enumerate(items):
        cx = x + cw * i + cw / 2
        out.append(R(cx - 9, y + 10, 18, 18, C["skel"], 4, C["muted"], 1.2))
        out.append(T(cx, y + 50, lb, 10, C["txt"], "middle"))
    return "".join(out), NAVBAR_H

def fab(x_screen, y_bottom, w, f):
    label = f.get("label", "+")
    pos = f.get("position", "end")
    cx = {"end": x_screen + w - 44, "center": x_screen + w / 2,
          "start": x_screen + 44}.get(pos, x_screen + w - 44)
    cy = y_bottom - 28
    return (CIRC(cx, cy, 28, C["pri"], C["line"], 1) +
            T(cx, cy + 8, label, 22, C["pritxt"], "middle", "600"))

def overlay(x, y, w, h, ov):
    out = [R(x, y, w, h, "#000000", 0, "none", 0)]
    out[0] = out[0].replace('fill="#000000"', 'fill="#202124" fill-opacity="0.45"')
    if ov.get("type") == "dialog":
        dw, dh = w - 64, 150 + ov.get("lines", 1) * 16
        dx, dy = x + 32, y + h / 2 - dh / 2
        out.append(R(dx, dy, dw, dh, C["bg"], 12))
        out.append(T(dx + 20, dy + 32, ov.get("title", "Diálogo"), 14, C["txt"], "start", "600"))
        for i in range(ov.get("lines", 1)):
            out.append(R(dx + 20, dy + 48 + i * 16, dw - 40 - i * 50, 9, C["skel"], 4.5))
        out.append(T(dx + dw - 24, dy + dh - 18, ov.get("button", "Aceptar"), 12, C["pri"], "end", "600"))
        return "".join(out)
    sh = 170 + ov.get("lines", 1) * 16
    sy = y + h - sh
    out.append(f'<path d="M {x} {sy+20} Q {x} {sy} {x+20} {sy} L {x+w-20} {sy} '
               f'Q {x+w} {sy} {x+w} {sy+20} L {x+w} {y+h} L {x} {y+h} Z" fill="{C["bg"]}"/>')
    out.append(R(x + w / 2 - 18, sy + 10, 36, 4, C["line"], 2))
    out.append(T(x + 24, sy + 44, ov.get("title", "Bottom sheet"), 14, C["txt"], "start", "600"))
    for i in range(ov.get("lines", 1)):
        out.append(R(x + 24, sy + 60 + i * 16, w - 48 - i * 50, 9, C["skel"], 4.5))
    if ov.get("button"):
        out.append(R(x + 24, y + h - 72, w - 48, 44, C["pri"], 10))
        out.append(T(x + w / 2, y + h - 44, ov["button"], 13, C["pritxt"], "middle", "600"))
    return "".join(out)

# ---------- ensamblado ----------

def render(spec):
    sx, sy, sw, sh = SCR, SCR, PW - 2 * SCR, PH - 2 * SCR
    vh = PH + (30 if spec.get("caption") else 0)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PW} {vh}">',
           R(8, 8, PW - 16, PH - 16, "none", RX, C["frame"], 2.5),
           R(sx, sy, sw, sh, C["bg"], RX - 14)]
    clip_id = "scr"
    out.append(f'<clipPath id="{clip_id}"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{RX-14}"/></clipPath>')
    out.append(f'<g clip-path="url(#{clip_id})">')

    # safety region + status bar
    out.append(R(sx, sy, sw, STATUS_H, C["safe"], 0))
    out.append(T(sx + 18, sy + 18, "9:41", 11, C["muted"]))
    out.append(R(sx + sw - 44, sy + 9, 26, 11, "none", 3, C["muted"], 1.2))
    out.append(R(sx + sw - 41, sy + 11.5, 16, 6, C["muted"], 1.5))

    y = sy + STATUS_H
    if ab := spec.get("appBar"):
        out.append(app_bar(sx, y, sw, ab))
        y += APPBAR_H

    body_top = y
    bb_svg, bb_h = "", 0
    if bb := spec.get("bottomBar"):
        bb_svg, bb_h = bottom_bar(sx, sy + sh - bb_h_placeholder(bb), sw, bb)
    body_bottom = sy + sh - bb_h - 8
    out.append(R(sx, sy + sh - 8, sw, 8, C["safe"], 0))  # safety inferior

    # body: apilar elementos
    bx, bw = sx + PAD, sw - 2 * PAD
    by = body_top + PAD
    for e in spec.get("body", []):
        fn = ELEMENTS.get(e.get("type"))
        if not fn:
            continue
        svg, h = fn(bx, by, bw, e)
        out.append(svg)
        by += h + GAP
    if by > body_bottom:
        print(f"  aviso: '{spec.get('name','?')}' desborda {by - body_bottom:.0f}px del body", file=sys.stderr)

    if bb_svg:
        out.append(bb_svg)
    if f := spec.get("fab"):
        fy = sy + sh - bb_h - 8 if bb_h else sy + sh - 8
        out.append(fab(sx, fy, sw, f))
    if ov := spec.get("overlay"):
        out.append(overlay(sx, sy, sw, sh, ov))

    out.append("</g>")
    if cap := spec.get("caption"):
        out.append(T(PW / 2, PH + 20, cap, 11, C["muted"], "middle"))
    out.append("</svg>")
    return "".join(out)

def bb_h_placeholder(bb):
    return CTABAR_H if bb.get("type", "nav") == "cta" else NAVBAR_H

def main():
    stdout = "-o" in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not files:
        sys.exit(__doc__)
    for f in files:
        spec = json.loads(Path(f).read_text())
        svg = render(spec)
        name = spec.get("name") or Path(f).stem
        if stdout:
            print(svg)
        else:
            ASSETS.mkdir(exist_ok=True)
            out = ASSETS / f"wire-{name}.svg"
            out.write_text(svg)
            print(f"✓ {out.name}  ←  {f}")

if __name__ == "__main__":
    main()
