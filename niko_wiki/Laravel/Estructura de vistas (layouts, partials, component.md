# Estructura de vistas (layouts, partials, components).

Titular: Niko

## ✅ **1️⃣ ¿Qué es una vista?**

Una **vista** es un archivo `.blade.php` que define **el HTML** que verá el usuario. Laravel usa **Blade**, su motor de plantillas, para **combinar PHP + HTML** de forma clara y reutilizable.

---

### 🔍 **Ejemplo real de vistas**

- Página de inicio → `home.blade.php`
- Listado de posts → `posts/index.blade.php`
- Formulario de login → `auth/login.blade.php`

Todas viven dentro de:

```bash

resources/views/

```

---

## ✅ **2️⃣ ¿Cómo se crea una vista?**

### 📌 **Ubicación**

Todas las vistas se guardan en `resources/views/`.

Puedes usar **subcarpetas** para organizarlas mejor:

```bash

resources/views/
 ├── layouts/
 ├── partials/
 ├── components/
 ├── pages/
 ├── auth/
 ├── admin/

```

---

### 📌 **Extensión**

Los archivos Blade **siempre** terminan en:

```

.blade.php

```

---

### 📌 **Cómo crear a mano**

- Crea la carpeta si no existe: `posts/`
- Dentro: `index.blade.php` o `create.blade.php`

---

### 📌 **Contenido**

Dentro puedes usar:

- HTML puro
- Variables: `{{ }}`
- Directivas Blade: `@if`, `@foreach`, `@extends`, `@section`, `@yield`, `@include`

---

### 📌 **Ejemplo práctico**

```
@extends('layouts.app')

@section('title', 'Lista de Posts')

@section('content')
    <h1>Posts</h1>
    @foreach ($posts as $post)
        <h2>{{ $post->title }}</h2>
    @endforeach
@endsection

```

✔️ `@extends` → Usa un layout base.

✔️ `@section` → Define contenido dinámico.

✔️ `@yield` → Hueco en el layout donde se inserta la sección.

---

### 📌 **Mostrar la vista desde un controlador**

```php
public function index() {
    $posts = Post::latest()->paginate(10);
    return view('posts.index', compact('posts'));
}

```

---

## ✅ **3️⃣ Layouts, Partials y Components**

---

### 🗂️ **📌 Layouts**

Un **layout** es una **plantilla base**: estructura general (`<html>`, `<head>`, `<body>`, `<main>`, footer, etc.).

```html
DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>@yield('title')</title>
</head>
<body>

    @include('partials.header')
    @include('partials.nav')

    <main>
        @yield('content')
    </main>

    @include('partials.footer')

</body>
</html>

```

**Clave:**

- `@yield` es un **hueco dinámico** que se llena con `@section` desde la vista hija.
- `@include` **pega un archivo parcial tal cual está**.

---

### 🧩 **📌 Partials**

Un **partial** es un **fragmento reutilizable**:

- Header
- Nav
- Footer
- Alertas
- Sidebar
- Scripts extra

```

@include('partials.header')
@include('partials.nav')
@include('partials.footer')
@include('partials.alerts')

```

---

### ⚙️ **📌 Components Blade**

Los **Components** son **partials avanzados**, que:

- Se usan como **etiquetas personalizadas** (`<x-alert>`).
- Aceptan **props** (parámetros).
- Tienen **slots** (contenido dinámico interno).

```

<x-alert type="success" message="Guardado correctamente" />

<x-card>
    <h2>Hola mundo</h2>
</x-card>

```

---

## ✅ **4️⃣ ¿Cuándo usar `@include` y `@yield`?**

| `@include` | `@yield` + `@section` |
| --- | --- |
| Pega un archivo Blade tal cual | Reserva un hueco para que una vista hija lo llene |
| Se usa para bloques fijos (nav, footer) | Se usa para contenido **variable** (main, título, secciones) |
| No tiene `@section` asociado | Siempre necesita `@section` en la vista hija |
| Ejemplo: `@include('partials.nav')` | Ejemplo: `@yield('content')` en layout + `@section('content')` en vista |

---

**Resumen mental:**

✅ `@include` = Copiar y pegar

✅ `@yield` = Reservar un espacio → `@section` lo llena

---

## ✅ **5️⃣ Listado de carpetas comunes**

| Carpeta | Contenido típico |
| --- | --- |
| `layouts/` | Layouts base: `app.blade.php`, `admin.blade.php` |
| `partials/` | Fragmentos: `header`, `footer`, `nav`, `alerts`, `sidebar` |
| `components/` | Componentes Blade con props/slots |
| `emails/` | Plantillas Blade para correos |
| `pages/` | Vistas por página o secciones de contenido |

---

**Ejemplo de partials reales:**

- `partials/header.blade.php`
- `partials/nav.blade.php`
- `partials/footer.blade.php`
- `partials/alerts.blade.php`
- `partials/sidebar.blade.php`

---

## ✅ **6️⃣ Ejemplo de flujo real**

1️⃣ Layout: `layouts/app.blade.php` define estructura

2️⃣ Partials: `@include('partials.nav')`, `@include('partials.footer')`

3️⃣ Vista: `home.blade.php` extiende el layout con `@extends('layouts.app')`

4️⃣ La vista define `@section('content')` → rellena el `@yield('content')`

---

## ✅ **7️⃣ Extra — Laravel View Maker**

Si quieres crear vistas rápido:

```bash

composer require laracasts/make
php artisan make:view posts.index

```

---

## ✅ **Resumen clave**

✔️ **`@include`** = fragmentos fijos → **partials**

✔️ **`@yield` + `@section`** = espacios dinámicos → **layouts + vistas hijas**

✔️ **`<x-Component>`** = componentes Blade con props y slots

---

### 📌 **Esta estructura mantiene tu app ordenada, DRY y escalable.**

---

## [👈🏻VOLVER](Qué%20es%20Blade.md)

## [SIGUIENTE 👉🏻](Pasar%20datos%20con%20compact.md)