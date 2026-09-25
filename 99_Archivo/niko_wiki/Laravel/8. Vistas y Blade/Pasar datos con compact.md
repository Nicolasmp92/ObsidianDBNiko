# Pasar datos con compact

Titular: Niko

## 📦 **3️⃣ Pasar datos con `compact`**

---

### ✅ **Cómo funciona**

`compact()` es una función PHP que **crea un array asociativo**.

Laravel lo usa para pasar variables a la vista de forma limpia.

```php

public function index() {
    $posts = Post::latest()->get();
    $author = 'Nye';

    return view('posts.index', compact('posts', 'author'));
}

```

Equivalente a:

```php

return view('posts.index', ['posts' => $posts, 'author' => $author]);

```

En Blade:

```php

<h1>Posts de {{ $author }}</h1>

@foreach ($posts as $post)
  <p>{{ $post->title }}</p>
@endforeach

```

✅ **Tip:** Si necesitas procesar más datos, usa un array o `with()`:

```php

return view('home')->with(['title' => 'Inicio', 'subtitle' => 'Bienvenido']);

```

---

## [👈🏻VOLVER](Estructura%20de%20vistas.md)

## [SIGUIENTE 👉🏻](Directivas%20Blade.md)