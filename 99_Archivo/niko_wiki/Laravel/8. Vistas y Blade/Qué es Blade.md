# Qué es Blade.

Titular: Niko

## ✨ **1️⃣ Qué es Blade**

**Blade** es el **motor de plantillas de Laravel**.

Convierte archivos `.blade.php` en HTML **dinámico**, mezclando datos PHP y estructura HTML **sin romper la cabeza**.

### 📌 **Ventajas reales**

✅ **Limpio**: Escribes `{{ $variable }}` en lugar de `<?php echo ?>`.

✅ **Seguro**: Escapa HTML automáticamente → evita inyecciones.

✅ **Directivas legibles**: `@if`, `@foreach`, `@extends`, `@section` → no necesitas abrir y cerrar PHP a cada rato.

✅ **Rápido**: Laravel cachea vistas Blade compiladas para que carguen rápido.

---

### ✅ **Ejemplo real: página básica**

**`resources/views/welcome.blade.php`**

```html
<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <title>Bienvenido</title>
</head>
<body>
    <h1>Hola, {{ $name }}</h1>

    @if ($age >= 18)
        <p>Eres mayor de edad.</p>
    @else
        <p>Eres menor de edad.</p>
    @endif

    <ul>
        @foreach ($hobbies as $hobby)
            <li>{{ $hobby }}</li>
        @endforeach
    </ul>
</body>
</html>

```

**Controlador**

```php
public function show() {
    $name = 'Niko';
    $age = 25;
    $hobbies = ['Leer', 'Codear', 'Gatos'];

    return view('welcome', compact('name', 'age', 'hobbies'));
}

```

✅ Resultado: HTML con nombre, edad, hobbies → sin PHP feo en la vista.

---

## [👈🏻VOLVER](índex%20Laravel%2012.md)

## [SIGUIENTE 👉🏻](Estructura%20de%20vistas.md)