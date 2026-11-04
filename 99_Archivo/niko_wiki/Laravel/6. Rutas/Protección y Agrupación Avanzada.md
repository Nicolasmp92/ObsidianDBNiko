# Protección y Agrupación Avanzada

Titular: Niko

## 🔒 **Middleware — ¿Qué es y para qué sirve?**

**👉 ¿Qué es?**

Un **middleware** es un **filtro** que intercepta la solicitud **antes o después** de que llegue al controlador.

Se usa para:

- Verificar **autenticación** (`auth`).
- Validar **roles o permisos**.
- Revisar si el correo está **verificado** (`verified`).
- Aplicar **CORS**, HTTPS, logs o cambios globales.

---

**👉 ¿Cómo se usa?**

Cuando agregas `.middleware('auth')` a una ruta:

```php
Route::get('/dashboard', function () {
    return 'Bienvenido!';
})->middleware('auth');

```

➡️ Laravel revisa:

- **¿Está logueado?**
- ✅ Si sí → permite.
- ❌ Si no → redirige a login.

---

**Puedes encadenar varios:**

```php
->middleware(['auth', 'verified'])

```

**Ejemplo real:**

```php
Route::get('/profile', function () {
    return 'Perfil';
})->middleware(['auth', 'verified']);

```

---

## 📌 **Cómo crear tu propio middleware**

```bash
php artisan make:middleware CheckAdmin

```

Esto crea:

```
app/Http/Middleware/CheckAdmin.php

```

**Ejemplo:**

```php
public function handle($request, Closure $next)
{
    if (auth()->user()?->role !== 'admin') {
        abort(403);
    }

    return $next($request);
}

```

---

**Regístralo en `Kernel.php`:**

```php
protected $routeMiddleware = [
    'admin' => \App\Http\Middleware\CheckAdmin::class,
];

```

Y úsalo:

```php
Route::get('/admin', function () {
    return 'Panel admin';
})->middleware(['auth', 'admin']);

```

---

## 🗂️ **Agrupar Rutas — ¿Por qué hacerlo?**

---

Cuando tienes **múltiples rutas** que:

- Comparten el mismo **prefix** (`/admin`).
- Usan el mismo **middleware**.
- O tienen un **namespace** común.

👉 Agruparlas **ahorra repetir**.

---

### ✅ **Ejemplo básico**

```php
Route::prefix('admin')->middleware(['auth', 'admin'])->group(function () {
    Route::get('/users', function () {
        return 'Usuarios admin';
    });

    Route::get('/settings', function () {
        return 'Configuración admin';
    });
});

```

---

**¿Qué pasa aquí?**

- Las URLs reales son:
    
    ```
    /admin/users
    /admin/settings
    
    ```
    
- Ambas rutas:
    
    ✅ Verifican `auth`
    
    ✅ Verifican `admin`
    

---

## ✅ **Suma un `name` base**

Puedes agregar un **prefijo para nombres**:

```php
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/users', function () {
        // route('admin.users')
    })->name('users');

    Route::get('/settings', function () {
        // route('admin.settings')
    })->name('settings');
});

```

---

## ✅ **Usar Namespace**

Laravel moderno **prefiere `::class`**, pero si organizas en carpetas:

```php
Route::namespace('Admin')->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
});

```

---

## ⚡ **Agrupación combinada con controladores**

```php
Route::prefix('admin')->middleware('auth')->group(function () {
    Route::get('/posts', [PostController::class, 'index']);
    Route::get('/posts/create', [PostController::class, 'create']);
});

```

---

## 🔑 **Tips extra — Buenas prácticas**

✔️ Usa `middleware` para **dividir acceso** (usuarios normales vs admins).

✔️ **Agrupa por áreas**: `admin`, `user`, `api`.

✔️ Para **APIs**, usa `api.php` con `throttle` (limitar peticiones).

✔️ **Nombra rutas clave**:

```php
Route::get('/profile', [ProfileController::class, 'show'])->name('profile');

```

Después puedes usar `route('profile')` en Blade.

✔️ **Verifica tus rutas**:

```bash
php artisan route:list

```

Te muestra:

- Métodos (GET, POST)
- URL completa
- Middleware aplicado
- Nombre de ruta
- Acción (`Controlador@método`)

---

## ✅ **Ejemplo PRO — Todo Junto**

```php
Route::prefix('admin')
    ->middleware(['auth', 'admin'])
    ->name('admin.')
    ->group(function () {
        Route::get('/dashboard', [AdminDashboardController::class, 'index'])->name('dashboard');
        Route::resource('/users', AdminUserController::class);
    });

```

Esto crea:

- `/admin/dashboard` con `route('admin.dashboard')`
- `/admin/users` con todos los métodos REST (`index`, `create`, `store`…)

---

**Resultado:**

- Rutas limpias.
- Protegidas.
- Fáciles de mantener.
- Sin repetir `auth` ni `prefix` en cada línea.

---

## [👈🏻VOLVER](Parámetros%20y%20Nombres.md)

## [SIGUIENTE 👉🏻](Controladores%20¿que%20son%20y%20como%20crearlos.md)