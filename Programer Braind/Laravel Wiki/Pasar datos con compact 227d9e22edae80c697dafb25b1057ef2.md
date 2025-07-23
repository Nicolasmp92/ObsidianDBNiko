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

## [👈🏻VOLVER](Estructura%20de%20vistas%20(layouts,%20partials,%20component%20227d9e22edae80ea8206e976ad966dc0.md)

## [SIGUIENTE 👉🏻](Directivas%20(@extends,%20@section,%20@yield,%20@include)%20228d9e22edae802ca39eee03d9a3f774.md)