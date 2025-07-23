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

## [👈🏻VOLVER](Sin%20ti%CC%81tulo%20227d9e22edae80e8bd23c9c0d9a52c4e.md)

## [SIGUIENTE 👉🏻](Proteccio%CC%81n%20y%20Agrupacio%CC%81n%20Avanzada%20227d9e22edae8089afb1eb3b50b799cc.md)