# Snippets útiles

Titular: Niko

## ✅ **2️⃣ Snippets útiles**

---

### 📌 **Insertar rápido**

```php

User::create([
    'name' => 'niko',
    'email' => 'nye@example.com',
    'password' => Hash::make('password'),
]);

```

---

### 📌 **Validar y guardar**

```php

$request->validate([
    'title' => 'required',
    'body' => 'required|min:10',
]);

Post::create($request->all());

```

---

### 📌 **Relación con Eager Loading**

```php

$posts = Post::with('comments')->get();

```

---

### 📌 **Route resource**

```php

Route::resource('posts', PostController::class);

```

---

### 📌 **Form Request**

```php

php artisan make:request StorePostRequest

```

```php

public function rules() {
    return [
        'title' => 'required',
        'body' => 'required|min:10',
    ];
}

```

---

### 📌 **Middleware personalizado**

```php

public function handle($request, Closure $next)
{
    if ($request->user()->role !== 'admin') {
        abort(403);
    }
    return $next($request);
}

```

---

### 📌 **Blade básico**

```php

@extends('layouts.app')

@section('title', 'Título Página')

@section('content')
  <h1>Hola, {{ $name }}</h1>
@endsection

```

---

## [👈🏻VOLVER](Lista%20ra%CC%81pida%20de%20comandos%20227d9e22edae801aad3de099af77bb7e.md)

## [SIGUIENTE 👉🏻](Consejos%20de%20produccio%CC%81n%20227d9e22edae805faa86fe348477ffa5.md)