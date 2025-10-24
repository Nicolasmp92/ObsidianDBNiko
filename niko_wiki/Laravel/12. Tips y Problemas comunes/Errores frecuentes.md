# Errores frecuentes

Titular: Niko

## 🐞 **1️⃣ Errores frecuentes**

### ✅ **1. Cache que no se borra**

**Síntoma:**

- Cambias algo en Blade, rutas, configs... ¡y nada pasa!
- Ves la versión vieja.

**Solución:**

Limpia la caché:

```bash
bash
CopiarEditar
php artisan view:clear       # Limpia caché de vistas Blade compiladas
php artisan config:clear     # Limpia caché de configuración
php artisan route:clear      # Limpia caché de rutas
php artisan cache:clear      # Limpia caché de la aplicación

```

---

### ✅ **2. Migraciones duplicadas**

**Síntoma:**

- Ejecutas `migrate` y da error: tabla ya existe, clave duplicada, etc.

**Solución rápida:**

```bash
bash
CopiarEditar
php artisan migrate:rollback
php artisan migrate:reset
php artisan migrate:fresh   # Borra TODO y migra limpio

```

---

### ✅ **3. Seeders no insertan nada**

**Síntoma:**

- `db:seed` corre pero la tabla queda vacía.

**Revisa:**

- Que tengas `run()` implementado.
- Que uses `Model::factory()->create()` o `DB::table()->insert()` correctamente.
- Que la BD del `.env` sea la misma en la que miras.

---

### ✅ **4. Error 419 — Token CSRF**

**Síntoma:**

- Formularios que dicen *“419 Page Expired”*.

**Solución:**

- Siempre usa `@csrf` dentro de `<form>`:
    
    ```
    blade
    CopiarEditar
    <form method="POST">
      @csrf
    </form>
    
    ```
    

---

### ✅ **5. Route [name] not defined**

**Síntoma:**

- Error: *Route [algo] not defined*.

**Solución:**

- Asegúrate de haber puesto `.name()` al final de tu ruta:
    
    ```php
    php
    CopiarEditar
    Route::get('/profile', [ProfileController::class, 'index'])->name('profile');
    
    ```
    
- Usa `php artisan route:list` para ver todas las rutas y nombres.

---

## [👈🏻VOLVER](índex%20Laravel%2012.md)

## [SIGUIENTE 👉🏻](Comandos%20para%20limpiar%20caché.md)