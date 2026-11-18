#!/usr/bin/env bash
# render.sh — Exporta las piezas del media kit a PNG con Chrome headless.
#
# Uso:
#   ./render.sh                        # renderiza todas las piezas de la tabla
#   ./render.sh plantillas/plantilla-post.html post-02-x.png 1080 1080
#
# Requiere google-chrome/chromium. Cada HTML define su tamaño en <style>
# (html,body); el window-size debe coincidir. --virtual-time-budget espera
# a que las fuentes (Inter empaquetada) y assets terminen de cargar.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser)"

render() { # html png w h
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 \
    --virtual-time-budget=8000 \
    --window-size="$3,$4" \
    --screenshot="$ROOT/$2" "file://$ROOT/$1" >/dev/null 2>&1
  if [ -f "$ROOT/$2" ]; then echo "OK   $2"; else echo "FAIL $2"; fi
}

if [ $# -ge 2 ]; then
  render "$1" "$2" "${3:-1080}" "${4:-1080}"
  exit 0
fi

render "post-01-lanzamiento.html"      "post-01-lanzamiento.png"      1080 1080
render "post-02-servicios.html"        "post-02-servicios.png"        1080 1080
render "post-03-kpp.html"              "post-03-kpp.png"              1080 1080
render "avatar-instagram.html"         "avatar-instagram.png"         1080 1080
render "destacadas/servicios.html"     "destacadas/servicios.png"     1080 1080
render "destacadas/proyectos.html"     "destacadas/proyectos.png"     1080 1080
render "destacadas/demo-kpp.html"      "destacadas/demo-kpp.png"      1080 1080
render "destacadas/contacto.html"      "destacadas/contacto.png"      1080 1080
