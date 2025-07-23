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

## [👈🏻VOLVER](Registro,%20login%20y%20logout%20227d9e22edae80c08b96e3f23d2a81ac.md)

## [SIGUIENTE 👉🏻](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)