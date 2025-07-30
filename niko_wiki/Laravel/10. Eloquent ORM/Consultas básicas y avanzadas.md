# Consultas básicas y avanzadas

Titular: Niko

## 📌 **3️⃣ Consultas básicas y avanzadas**

---

### ✅ **Consultas básicas**

```php

// Obtener todos
$users= User::all();

// Obtener uno
$users= User::find(1);

// Filtrar
$users= User::where('status', 'published')->get();

// Ordenar
$users= User::orderBy('created_at', 'desc')->get();

// Paginación
$users= User::paginate(10);

```

---

### ✅ **Insertar**

```php
Post::create([
    'title' => 'Nuevo Post',
    'body' => 'Contenido...',
]);

```

👉 Recuerda: usa `$fillable` o `$guarded` en el modelo para permitir `create()`.

---

### ✅ **Actualizar**

```php

$post = Post::find(1);
$post->title = 'Título actualizado';
$post->save();

```

---

### ✅ **Eliminar**

```php

Post::destroy(1);

// o
$post = Post::find(1);
$post->delete();

```

---

### ✅ **Consultas avanzadas**

---

**Scopes personalizados**

```php

// Post.php
public function scopePublished($query)
{
    return $query->where('status', 'published');
}

// Usar
$posts = Post::published()->get();

```

---

**Eager Loading (optimizar consultas)**

```php

$posts = Post::with('comments')->get();

```

Evita la **N+1 Problem**: carga posts y comentarios juntos.

---

**Chunk (procesar datos grandes)**

```php

Post::chunk(100, function ($posts) {
    foreach ($posts as $post) {
        // hacer algo
    }
});

```

---

## ✅ **Tips Nova**

✔️ Eloquent = menos SQL manual → más legible.

✔️ Usa `fillable` para evitar MassAssignmentException.

✔️ Usa relaciones → reduce joins manuales.

✔️ Para APIs → combina Eloquent + Resources (`php artisan make:resource`).

✔️ Usa `withTrashed` si tienes `SoftDeletes`.

---

## [👈🏻VOLVER](Modelos%20y%20relaciones.md)

## [SIGUIENTE 👉🏻](A0.%20Laravel%20index.md)