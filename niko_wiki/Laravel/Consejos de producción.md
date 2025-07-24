# Consejos de producción

Titular: Niko

## ✅ **3️⃣ Consejos de Producción**

---

✔️ **Configura `.env` bien:**

```php

APP_ENV=production
APP_DEBUG=false

```

---

✔️ **Corre `php artisan config:cache` y `route:cache`** antes de subir.

---

✔️ **Usa `storage:link`** para subir archivos.

```bash

php artisan storage:link

```

---

✔️ **Protege tus claves API y bases:**

Nunca subas `.env` ni tokens a Git.

---

✔️ **Haz backups de tu base de datos regularmente.**

---

✔️ **Habilita HTTPS y CORS correctamente si trabajas con APIs.**

---

✔️ **Usa paquetes de roles (Spatie) para permisos más robustos.**

---

## [👈🏻VOLVER](Snippets%20útiles.md)

## [SIGUIENTE 👉🏻](Laravel%20index.md)