# Parámetros y Nombres

Titular: Niko

### **Parámetros dinámicos**

Para recibir datos en la URL:

```php
Route::get('/users/{id}', function ($id) {
    return 'ID: '.$id;
});

```

---

### 📌 **Opcionales**

```php
Route::get('/users/{name?}', function ($name = 'Invitado') {
    return 'Hola, '.$name;
});

```

---

### 📌 **Restricciones**

Valida con `where`:

```php
Route::get('/users/{id}', function ($id) {
    return $id;
})->where('id', '[0-9]+');

```

---

### 📌 **Nombrar rutas**

Poner nombres ayuda a generar URLs:

```php
Route::get('/profile', [UserController::class, 'profile'])
    ->name('profile');

```

Blade:

```php
<a href=\"{{ route('profile') }}\">Mi Perfil</a>

```

---

## [👈🏻VOLVER](Estructura%20y%20Tipos%20de%20Rutas.md)

## [SIGUIENTE 👉🏻](Protección%20y%20Agrupación%20Avanzada.md)