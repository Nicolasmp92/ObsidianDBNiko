# -*- coding: utf-8 -*-
# Consolida "respaldos ale 1" y "respaldos ale 2" en E:\Respaldo Ale por tipo de archivo.
import os, sys, shutil, hashlib, csv, time
from pathlib import Path

SRC_ROOTS = [Path(r"E:\respaldos ale 1"), Path(r"E:\respaldos ale 2")]
DST = Path(r"E:\Respaldo Ale")

# Directorios de programas -> _Programas (movimiento wholesale, sin tocar archivos)
JUNK = [
    (Path(r"E:\respaldos ale 1\D5 Render"), "D5 Render"),
    (Path(r"E:\respaldos ale 2\escritorio\AutoCAD 2024"), "AutoCAD 2024"),
    (Path(r"E:\respaldos ale 2\escritorio\Autodesk Vehicle Tracking 2024"), "Autodesk Vehicle Tracking 2024"),
    (Path(r"E:\respaldos ale 2\documentos\Adobe"), "Adobe"),
]

# Carpetas de perfil de usuario: se omiten como primer nivel dentro de la categoria
STRIP = {"escritorio", "documentos", "descargas", "imagenes", "downloads",
         "desktop", "documents", "pictures", "videos", "music"}

CATS = {
    "Documentos": {"pdf","doc","docx","xls","xlsx","ppt","pptx","odt","ods","odp",
                   "rtf","txt","csv","xps","epub","md","pub","vsd","vsdx","one"},
    "Imagenes": {"jpg","jpeg","png","gif","webp","svg","tif","tiff","bmp","heic","heif",
                 "ico","cr2","nef","arw","dng","raw","jfif","avif","jp2","exr","hdr"},
    "Videos": {"mp4","mov","avi","mkv","webm","m4v","3gp","wmv","mpg","mpeg","mts","m2ts","vob","flv"},
    "Audio": {"mp3","wav","m4a","aac","flac","ogg","opus","wma","mid","midi","aif","aiff"},
    "Proyectos": {"ai","psd","psb","indd","idml","eps","xd","fig","sketch","dwg","dxf","dwt",
                  "rvt","rfa","rte","skp","skb","d5a","d5s","prproj","aep","blend","obj","fbx",
                  "3ds","max","c4d","stl","step","stp","iges","igs","lsp","dyn","bak","sv$",
                  "pln","pla","3dm","gh","ghx"},
    "Correos": {"msg","eml","pst","ost","mbox"},
    "Comprimidos": {"zip","rar","7z","tar","gz","bz2","xz","cab","iso","dmg","tgz"},
    "Instaladores": {"exe","msi","msix","appx","pkg","deb","rpm"},
}
EXT2CAT = {e: c for c, exts in CATS.items() for e in exts}

def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def unique_dest(dest):
    n = 2
    while True:
        cand = dest.with_name(f"{dest.stem} ({n}){dest.suffix}")
        if not cand.exists():
            return cand
        n += 1

def dest_rel(src_root, f):
    rel = f.relative_to(src_root)
    parts = list(rel.parts)
    if len(parts) > 1 and parts[0].lower() in STRIP:
        parts = parts[1:]
    return Path(*parts)

def main():
    t0 = time.time()
    moved = renamed = dupdel = errors = 0
    log_mov = open(DST / "_log_movimientos.csv", "w", newline="", encoding="utf-8-sig")
    log_dup = open(DST / "_log_duplicados.csv", "w", newline="", encoding="utf-8-sig")
    wmov = csv.writer(log_mov); wdup = csv.writer(log_dup)
    wmov.writerow(["origen", "destino", "accion"])
    wdup.writerow(["origen_eliminado", "conservado_en", "md5"])

    # 1) Programas -> _Programas (rename wholesale)
    for src, name in JUNK:
        if not src.exists():
            print(f"[skip] no existe: {src}", flush=True); continue
        d = DST / "_Programas" / name
        d.parent.mkdir(parents=True, exist_ok=True)
        if d.exists():
            d = unique_dest(d)
        try:
            shutil.move(str(src), str(d))
            wmov.writerow([src, d, "programa_directorio"])
            print(f"[prog] {src} -> {d}", flush=True)
        except Exception as e:
            errors += 1
            wmov.writerow([src, d, f"ERROR: {e}"])
            print(f"[ERR] {src}: {e}", flush=True)

    # 2) Archivos de usuario por extension
    i = 0
    for root in SRC_ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dp = Path(dirpath)
            # no entrar en dirs ya movidos (por si quedaron residuos)
            dirnames[:] = [x for x in dirnames]
            for fn in filenames:
                i += 1
                f = dp / fn
                try:
                    if f.is_symlink():
                        continue
                    ext = f.suffix.lower().lstrip(".")
                    cat = EXT2CAT.get(ext, "Otros")
                    rel = dest_rel(root, f)
                    d = DST / cat / rel
                    d.parent.mkdir(parents=True, exist_ok=True)
                    accion = "movido"
                    if d.exists():
                        if d.stat().st_size == f.stat().st_size and md5(d) == md5(f):
                            h = md5(f)
                            f.unlink()
                            wdup.writerow([f, d, h])
                            wmov.writerow([f, d, "duplicado_identico_eliminado"])
                            dupdel += 1
                            if i % 500 == 0:
                                print(f"  ...{i} archivos ({moved} mov, {dupdel} dup)", flush=True)
                            continue
                        d = unique_dest(d)
                        accion = "renombrado"
                        renamed += 1
                    shutil.move(str(f), str(d))
                    wmov.writerow([f, d, accion])
                    moved += 1
                except Exception as e:
                    errors += 1
                    wmov.writerow([f, "", f"ERROR: {e}"])
                    print(f"[ERR] {f}: {e}", flush=True)
                if i % 500 == 0:
                    print(f"  ...{i} archivos ({moved} mov, {renamed} ren, {dupdel} dup)", flush=True)

    # 3) Borrar directorios vacios (bottom-up)
    emptied = 0
    for root in SRC_ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root, topdown=False):
            try:
                if not os.listdir(dirpath):
                    os.rmdir(dirpath); emptied += 1
            except OSError:
                pass
        leftover = sum(len(files) for _, _, files in os.walk(root)) if root.exists() else 0
        print(f"[fin-src] {root}: leftover_files={leftover}", flush=True)

    log_mov.close(); log_dup.close()
    print(f"DONE en {time.time()-t0:.0f}s | movidos={moved} renombrados={renamed} "
          f"duplicados_eliminados={dupdel} errores={errors} dirs_vacios_borrados={emptied}", flush=True)

if __name__ == "__main__":
    DST.mkdir(exist_ok=True)
    main()
