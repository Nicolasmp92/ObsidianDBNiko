# Directivas (@extends, @section, @yield, @include)

Titular: Niko

🧩 **4️⃣ Directivas Blade — @extends, @section, @yield, @include**

---

### ✅ **@extends**

Indica **qué layout usar**:

```php

@extends('layouts.app')

```

---

### ✅ **@section y @yield**

`@section` define un bloque de contenido.

`@yield` indica **dónde se mostrará** ese bloque en el layout.

**Ejemplo: `layouts/app.blade.php`**

```php

<title>@yield('title')</title>

<body>
  @yield('content')
</body>

```

**Ejemplo: `posts/index.blade.php`**

```php

@extends('layouts.app')

@section('title', 'Listado de Posts')

@section('content')
  <h1>Posts</h1>
  @foreach ($posts as $post)
    <p>{{ $post->title }}</p>
  @endforeach
@endsection

```

---

### ✅ **@include**

Incluye un partial:

```

@include('partials.nav')

```

Puedes pasarle datos:

```php

@include('partials.alert', ['type' => 'error', 'message' => 'Ups!'])

```

---

### ✅ **@csrf**

En formularios POST, siempre pon

@csrf es una directiva Blade que inserta automáticamente un token CSRF en formularios HTML.
Sirve para proteger la aplicación contra ataques CSRF (Cross-Site Request Forgery).

**🔒 ¿Qué es CSRF?**

Un ataque donde alguien envía formularios falsos a tu servidor para ejecutar acciones sin autorización.

Laravel previene esto validando que cada formulario venga con un **token único y válido**.

**🔧 ¿Cómo se usa?**

Siempre dentro de formularios `POST`, `PUT`, `PATCH` o `DELETE`:

```html
<--! NOTA:  @csrf SIMPRE DENTRO DEL FORM O TE FALLA -->
<form method="POST" action="/guardar">
    @csrf
    <input type="text" name="titulo">
    <button type="submit">Guardar</button>
</form>

```

Laravel inyecta:

```html

<input type="hidden" name="_token" value="xxxxxxxxxxxxxxxxxxxx">

```

Este token se valida en el backend **automáticamente**.

---

### ✅ **@foreach, @if y otras**

Blade tiene **versiones limpias** de estructuras de control:

```php

@foreach ($users as $user)
  <p>{{ $user->name }}</p>
@endforeach

@if ($isAdmin)
  <p>Bienvenido Admin</p>
@elseif ($isUser)
  <p>Bienvenido Usuario</p>
@else
  <p>Acceso denegado</p>
@endif

```

---

## ✅ **Tips Nova**

✔️ Usa **layouts** para evitar copiar headers y footers en cada archivo.

✔️ Reutiliza **partials** para fragmentos como navbar, modals, formularios.

✔️ Usa **components** cuando un bloque necesita lógica interna (ej: `x-alert`).

✔️ Limpia la caché de vistas con:

```bash

php artisan view:clear

```

✔️ Organiza las carpetas: `views/layouts`, `views/partials`, `views/pages` → tu estructura se lee sola.

---

## [👈🏻VOLVER](Pasar%20datos%20con%20compact%20227d9e22edae80c697dafb25b1057ef2.md)

## [SIGUIENTE 👉🏻](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)