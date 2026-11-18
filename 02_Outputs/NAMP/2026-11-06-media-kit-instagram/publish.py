#!/usr/bin/env python3
"""publish.py — Publica piezas del media kit en Instagram via Graph API.

Uso:
  ./publish.py post-01-lanzamiento.png --caption "Texto"
  ./publish.py post-02-servicios.png          # caption desde captions/<nombre>.txt
  ./publish.py historia.png --stories
  ./publish.py post.png --dry-run             # valida todo sin publicar

Requiere instagram/.env (ver PUBLICACION.md):
  IG_USER_ID, IG_ACCESS_TOKEN,
  VPS_SSH (user@host), VPS_MEDIA_DIR (ruta publica), MEDIA_BASE_URL

La imagen debe llegar a Instagram por URL publica: el script la sube al
VPS por scp, crea el contenedor y publica. Con --cleanup borra el PNG
del VPS al terminar (IG ya lo consumio).
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

API = "https://graph.facebook.com/v21.0"
ROOT = os.path.dirname(os.path.abspath(__file__))


def load_env():
    env = dict(os.environ)
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env.setdefault(k.strip(), v.strip())
    return env


def api_post(path, params):
    req = urllib.request.Request(f"{API}/{path}", data=urllib.parse.urlencode(params).encode())
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def api_get(path, params):
    req = urllib.request.Request(f"{API}/{path}?{urllib.parse.urlencode(params)}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(description="Publica una pieza del kit en Instagram.")
    ap.add_argument("png", help="PNG a publicar (ruta relativa al kit o absoluta)")
    ap.add_argument("--caption", help="Texto del post (si no, captions/<nombre>.txt)")
    ap.add_argument("--caption-file", help="Archivo con la caption")
    ap.add_argument("--stories", action="store_true", help="Publicar como historia")
    ap.add_argument("--cleanup", action="store_true", help="Borrar el PNG del VPS al terminar")
    ap.add_argument("--dry-run", action="store_true", help="Validar config y caption sin publicar")
    args = ap.parse_args()

    png = args.png if os.path.isabs(args.png) else os.path.join(ROOT, args.png)
    if not os.path.isfile(png):
        sys.exit(f"No existe {png}")

    caption = args.caption
    if not caption:
        cap_path = args.caption_file or os.path.join(ROOT, "captions", os.path.splitext(os.path.basename(png))[0] + ".txt")
        if os.path.isfile(cap_path):
            caption = open(cap_path).read().strip()
    if not caption:
        sys.exit("Falta caption (--caption o captions/<nombre>.txt)")

    env = load_env()
    missing = [k for k in ("IG_USER_ID", "IG_ACCESS_TOKEN", "VPS_SSH", "VPS_MEDIA_DIR", "MEDIA_BASE_URL") if not env.get(k)]
    if missing and not args.dry_run:
        sys.exit(f"Faltan variables en instagram/.env: {', '.join(missing)} (ver PUBLICACION.md)")

    remote_name = os.path.basename(png)
    base = env.get("MEDIA_BASE_URL", "https://<MEDIA_BASE_URL>/")
    image_url = urllib.parse.urljoin(base.rstrip("/") + "/", remote_name)

    if args.dry_run:
        print(f"OK dry-run: {png}")
        if missing:
            print(f"AVISO: faltan en .env -> {', '.join(missing)}")
        print(f"URL publica: {image_url}")
        print(f"Caption ({len(caption)} chars):\n---\n{caption}\n---")
        return

    # 1. Subir el PNG a una URL publica del VPS
    subprocess.run(["scp", "-q", png, f"{env['VPS_SSH']}:{env['VPS_MEDIA_DIR'].rstrip('/')}/{remote_name}"], check=True)
    print(f"subido -> {image_url}")

    try:
        # 2. Crear el contenedor de media
        params = {"image_url": image_url, "access_token": env["IG_ACCESS_TOKEN"]}
        if args.stories:
            params["media_type"] = "STORIES"
        else:
            params["caption"] = caption
        container = api_post(f"{env['IG_USER_ID']}/media", params)["id"]
        print(f"contenedor {container}")

        # 3. Esperar a que IG procese el contenedor
        for _ in range(30):
            status = api_get(container, {"fields": "status_code", "access_token": env["IG_ACCESS_TOKEN"]}).get("status_code")
            if status == "FINISHED":
                break
            if status == "ERROR":
                sys.exit("Instagram rechazo el contenedor (status_code=ERROR)")
            time.sleep(2)
        else:
            sys.exit("Timeout esperando el procesamiento del contenedor")

        # 4. Publicar
        media_id = api_post(f"{env['IG_USER_ID']}/media_publish",
                            {"creation_id": container, "access_token": env["IG_ACCESS_TOKEN"]})["id"]
        permalink = api_get(media_id, {"fields": "permalink", "access_token": env["IG_ACCESS_TOKEN"]}).get("permalink", "?")
        print(f"PUBLICADO {permalink}")
    finally:
        if args.cleanup:
            subprocess.run(["ssh", env["VPS_SSH"], "rm", "-f",
                            f"{env['VPS_MEDIA_DIR'].rstrip('/')}/{remote_name}"], check=False)


if __name__ == "__main__":
    main()
