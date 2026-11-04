# 🧩 4️⃣ Directivas Blade – `@extends`, `@section`, `@yield`, `@include`, `@csrf`, etc.

---

## 🧭 Introducción

Blade es el motor de plantillas de Laravel.  
Nos permite **separar el diseño del contenido**, escribir HTML de forma ordenada y **reutilizar partes comunes** como encabezados, menús o formularios.

Esta sección te explica **cómo se conectan las vistas entre sí**, indicando:

- **Dónde nace un archivo** (`layouts`, `partials`, etc.)
    
- **Desde dónde se llama o extiende**
    
- **Qué hace cada directiva** y **cuándo usarla**
    

---

## 🧱 Estructura típica de carpetas Blade

resources/
└── views/
    ├── components/              # Componentes Blade reutilizables
    │   ├── layouts/             # Layouts principales (auth, app, etc.)
    │   ├── auth/                # Componentes usados en vistas de login/register
    │   ├── forms/               # Formularios parciales
    │   └── ui/                  # Elementos de interfaz (botones, modales, etc.)
    │
    ├── livewire/                # Vistas que pertenecen a componentes Livewire
    │   ├── auth/
    │   ├── profile/
    │   ├── settings/
    │   └── dashboard.blade.php
    │
    ├── layouts/                 # Estructuras base de página
    │   ├── app.blade.php
    │   └── guest.blade.php
    │
    ├── partials/                # Fragmentos de código compartidos (head, footer, etc.)
    │   ├── head.blade.php
    │   └── footer.blade.php
    │
    ├── dashboard.blade.php      # Vista principal después del login
    ├── welcome.blade.php        # Página pública o de inicio
    └── auth/                    # Páginas de autenticación
        ├── login.blade.php
        ├── register.blade.php
        ├── forgot-password.blade.php
        └── reset-password.blade.php

---


## ✅ `@extends` → ¿Qué layout usa esta vista?

- 📌 **Se escribe al inicio de una vista individual**.
    
- 🔁 Sirve para **heredar una estructura base** (cabecera, scripts, etc).
    
- 🧭 Apunta a un archivo `.blade.php` dentro de `views/layouts`.
    

blade

CopiarEditar

`@extends('layouts.app')`

🧠 **¿Dónde?**

blade

CopiarEditar

`resources/views/pages/dashboard.blade.php`

---

## ✅ `@section` + `@yield` → Llenar espacios definidos por el layout

- `@section`: lo escribes en la vista hija (por ejemplo: `dashboard.blade.php`)
    
- `@yield`: se define en el layout (`layouts/app.blade.php`) y actúa como “zona vacía”.
    

---

### 🗂️ Layout base → `resources/views/layouts/app.blade.php`

blade

CopiarEditar

`<!DOCTYPE html> <html lang="es"> <head>     <title>@yield('title')</title>     @include('partials.head') </head> <body>     @include('partials.nav')      <main>         @yield('content')     </main> </body> </html>`

---

### 🧾 Vista que hereda el layout → `resources/views/pages/dashboard.blade.php`

blade

CopiarEditar

`@extends('layouts.app')  @section('title', 'Panel de Control')  @section('content')     <h1>Bienvenido, Niko</h1> @endsection`

---

## ✅ `@include` → Incluir fragmentos (partials)

- 📌 **Úsalo dentro de layouts o vistas**
    
- 💾 Carga archivos `.blade.php` que están en `resources/views/partials/`
    
- 🧰 Ideal para menús, alertas, formularios pequeños, modales
    

blade

CopiarEditar

`@include('partials.nav')`

✅ También puedes enviarle variables:

blade

CopiarEditar

`@include('partials.alert', ['type' => 'success', 'message' => 'Datos guardados'])`

---

## ✅ `@csrf` → Token de seguridad en formularios

- 📌 **Siempre que uses un formulario POST, PUT, PATCH o DELETE**.
    
- 🔒 Protege contra ataques tipo **CSRF (Cross-Site Request Forgery)**.
    

### 💡 ¿Dónde se escribe?

**Dentro de `<form>`**. Laravel se encarga del resto.

blade

CopiarEditar

`<form method="POST" action="/guardar">     @csrf     <input type="text" name="titulo">     <button type="submit">Guardar</button> </form>`

🔍 Laravel lo convierte en:

html

CopiarEditar

`<input type="hidden" name="_token" value="xxxxxxxx">`

---

## ✅ `@foreach`, `@if`, `@else`, `@isset`, `@empty`

Blade simplifica el uso de estructuras de control:

blade

CopiarEditar

`@foreach ($users as $user)   <p>{{ $user->name }}</p> @endforeach`

blade

CopiarEditar

`@if ($isAdmin)   <p>Bienvenido Admin</p> @elseif ($isUser)   <p>Bienvenido Usuario</p> @else   <p>Acceso denegado</p> @endif`

---

## ✅ Tips Nova 💡

✔️ Usa `layouts` para definir estructura global (header, footer, layout general).

✔️ Usa `partials` para fragmentos visuales que se repiten, sin lógica.

✔️ Usa `components` (`<x-alert>`, `<x-input>`) cuando necesites reutilizar elementos **con lógica propia**.

✔️ Limpia la caché de vistas si haces cambios en Blade y no se reflejan:

bash

CopiarEditar

`php artisan view:clear`

✔️ Mantén tu estructura ordenada:

bash

CopiarEditar

`views/ ├── layouts/ ├── partials/ ├── pages/`
---

## [👈🏻VOLVER](Pasar%20datos%20con%20compact.md)

## [SIGUIENTE 👉🏻](índex%20Laravel%2012.md)