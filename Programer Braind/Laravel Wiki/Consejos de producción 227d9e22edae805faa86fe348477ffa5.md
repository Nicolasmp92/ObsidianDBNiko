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

## [👈🏻VOLVER](Snippets%20u%CC%81tiles%20227d9e22edae80c3aa98c29d15673880.md)

## [SIGUIENTE 👉🏻](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)