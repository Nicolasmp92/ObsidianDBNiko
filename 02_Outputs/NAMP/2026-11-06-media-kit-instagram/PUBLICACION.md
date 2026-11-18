# Publicación automatizada — Instagram Graph API

`publish.py` publica cualquier pieza del kit con un comando. Usa la API
oficial de Meta — **no** usar librerías no oficiales (instagrapi y
similares): violan los ToS y arriesgan la cuenta.

## Setup único (~20 min, una sola vez)

### 1. Cuenta profesional + página de Facebook

- Instagram → Configuración → Tipo de cuenta → Profesional →
  categoría *Software/Servicios informáticos*.
- Vincular una **página de Facebook** de NAMP (crearla básica desde
  facebook.com/pages/create — la API la exige aunque no se alimente).

### 2. App de Meta y token

1. En [developers.facebook.com](https://developers.facebook.com) →
   *Mis apps* → *Crear app* → tipo **Business** → nombre `NAMP Instagram`.
2. En el panel de la app → *Agregar producto* → **Instagram** →
   *Instagram Graph API*.
3. *Graph API Explorer* → seleccionar la app → *Generate Access Token*
   con permisos:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_show_list`
4. Intercambiar por token de **larga duración** (60 días, renovable):
   ```
   GET https://graph.facebook.com/v21.0/oauth/access_token
       ?grant_type=fb_exchange_token
       &client_id={APP_ID}&client_secret={APP_SECRET}
       &fb_exchange_token={TOKEN_CORTO}
   ```

### 3. Obtener IG_USER_ID

```
GET /me/accounts                      → id de la página FB
GET /{page-id}?fields=instagram_business_account  → IG_USER_ID
```

### 4. Directorio público en el VPS — ✅ YA HECHO (2026-11-18)

Instagram descarga la imagen desde una URL pública. Ya quedó montado:
contenedor `ig-media` (nginx:alpine) en el VPS sirviendo
`~/ig-media/media-ig` vía Traefik con la regla
`Host(namp.cl) && PathPrefix(/media-ig)` + cert let's encrypt.

Verificado: `curl https://namp.cl/media-ig/test.txt` → `test-ok`.
El `.env` ya trae `VPS_SSH=vps`, `VPS_MEDIA_DIR=/home/niko/ig-media/media-ig`,
`MEDIA_BASE_URL=https://namp.cl/media-ig/` — no tocar.

### 5. Configurar y probar

```bash
cp .env.example .env   # rellenar IG_USER_ID, IG_ACCESS_TOKEN, VPS_*
./publish.py post-01-lanzamiento.png --dry-run
./publish.py post-01-lanzamiento.png --cleanup
```

## Uso

```bash
./publish.py post-01-lanzamiento.png            # caption de captions/<nombre>.txt
./publish.py post-02-servicios.png --caption "…"
./publish.py historia.png --stories             # historias soportadas
./publish.py post.png --cleanup                 # limpia el VPS al terminar
```

La caption se toma de `captions/<nombre-del-png>.txt` si existe;
`--caption` tiene prioridad.

## Límites de la API (lo que sigue manual)

- **No crea destacadas ni las alimenta** — se gestionan en la app.
- **No archiva ni borra contenido antiguo** — limpieza manual (Fase 1).
- Carruseles soportados (varios containers hijos) — pendiente si se usa.
- Límite de la API: 25 posts publicados / 24 h por cuenta.
- El token de larga duración expira a los ~60 días: `publish.py` fallará
  con error de auth → refrescar en Graph API Explorer.
