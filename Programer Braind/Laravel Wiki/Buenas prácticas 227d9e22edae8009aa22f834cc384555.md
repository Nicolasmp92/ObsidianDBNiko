# Buenas prácticas

Titular: Niko

## ✅ **3️⃣ Buenas prácticas**

### ✏️ **Organiza bien carpetas**

- `routes/web.php` → solo define rutas, **nada de lógica**.
- `app/Http/Controllers` → controladores REST limpios.
- `app/Models` → define fillable, relaciones, scopes.

---

### 🔑 **Usa `.env` bien**

- No pongas claves API, tokens ni passwords fijos en el código.
- Define `APP_DEBUG=false` en producción.

---

### 🚫 **No edites migraciones ya migradas**

- Si necesitas cambiar columnas, **crea una migración nueva**.
- No borres migraciones viejas en proyectos reales.

---

### 🧹 **Versiona tu código**

- Usa **Git**. Crea commits claros.
- Ignora carpetas `vendor/`, `.env` y `/storage`.

---

### 🗂️ **Nombres claros**

- `PostController`, `UserSeeder`, `ProductFactory`.
- No uses `Test.php` para todo.

---

### 🧩 **Prueba y valida**

- Usa `php artisan tinker` para probar queries.
- Usa `Request` para validar formularios.
- Revisa logs: `storage/logs/laravel.log`.

---

### 🚀 **Mantenlo simple**

- Si algo se repite → convierte en **componente Blade** o **Livewire**.
- Si hay lógica repetida → **usa Traits** o Helpers.
- Si algo crece → divídelo en carpetas (`Admin/`, `API/`, `Auth/`).

---

**✅ Resultado:**

Menos bugs, menos dolores de cabeza y código más mantenible.

---

## [👈🏻VOLVER](Comandos%20para%20limpiar%20cache%CC%81%20227d9e22edae80aba16cdbe1f166b28f.md)

## [SIGUIENTE 👉🏻](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)