# Roles y middlewares

Titular: Niko

## 🚦 **3️⃣ Roles y middlewares**

---

### ✅ **Middleware `auth`**

Protege rutas: solo usuarios autenticados pueden entrar.

```php
php
CopiarEditar
Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth']);

```

---

### ✅ **Crear roles**

Laravel no trae roles por defecto, pero puedes usar:

- Un campo `role` en la tabla `users`
- O un paquete como **Spatie Laravel Permission**

---

### 📌 **Ejemplo básico con campo `role`**

**Migración:**

```php
php
CopiarEditar
$table->string('role')->default('user');

```

---

**Middleware personalizado**

```bash
bash
CopiarEditar
php artisan make:middleware AdminMiddleware

```

**AdminMiddleware.php**

```php
php
CopiarEditar
public function handle($request, Closure $next)
{
    if (auth()->check() && auth()->user()->role === 'admin') {
        return $next($request);
    }

    abort(403);
}

```

---

**Registrar middleware** en `Kernel.php`:

```php
php
CopiarEditar
protected $routeMiddleware = [
    'admin' => \\App\\Http\\Middleware\\AdminMiddleware::class,
];

```

---

**Usar en rutas**

```php
php
CopiarEditar
Route::get('/admin', function () {
    return 'Panel admin';
})->middleware(['auth', 'admin']);

```

✅ Así solo usuarios con `role = 'admin'` pueden entrar.

---

### 📌 **Paquete Spatie**

Si tu app crece, mejor usa Spatie Laravel Permission para:

- Crear roles y permisos dinámicos
- Asignarlos a usuarios
- Validar con `can()` o `hasRole()`

---

## ✅ **Tips Nova**

✔️ Breeze es perfecto para auth simple y rápido.

✔️ Protege todo con `auth` → no confíes en el frontend.

✔️ Usa `Hash::make` para nunca guardar passwords sin cifrar.

✔️ Crea middlewares para roles.

✔️ Para APIs → usa Sanctum o Passport (tokens).

---

## [👈🏻VOLVER](Registro,%20login%20y%20logout.md)

## [SIGUIENTE 👉🏻](0.%20Laravel%20index.md)