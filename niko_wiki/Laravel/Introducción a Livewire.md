# Introducción a Livewire

Titular: Niko

## ⚙️ **1️⃣ Introducción a Livewire**

**¿Qué es?**

Livewire es un **framework full-stack** para Laravel. Te permite crear **componentes dinámicos** que se actualizan **sin recargar la página** usando **AJAX + Blade + PHP**.

✔️ **No necesitas JavaScript complejo**.

✔️ Todo se escribe en Blade y PHP.

✔️ Responde a clicks, inputs y eventos en tiempo real.

---

**⏳ Ejemplo de dónde se usa:**

- Tablas dinámicas (con filtros y paginación)
- Formularios reactivos con validación instantánea
- Modales
- Menús desplegables y toggles
- Dashboards con estadísticas que se refrescan

---

### 📌 **Cómo funciona detrás**

- El componente tiene **propiedades** (`public $name`).
- Estas se **sincronizan** con HTML (`wire:model`).
- Cuando haces una acción (`wire:click`), se ejecuta un **método PHP** en el servidor.
- Livewire **devuelve solo el fragmento HTML actualizado**, sin recargar toda la página.

---

## ✅ **Instalación**

```bash
bash
CopiarEditar
composer require livewire/livewire

```

Luego, en tu `layouts/app.blade.php`:

```
blade
CopiarEditar
<head>
  @livewireStyles
</head>
<body>
  @yield('content')

  @livewireScripts
</body>

```

**Si falta uno, Livewire no funciona bien → siempre revisa!**

---

## [👈🏻VOLVER](0.%20Laravel%20index.md)

## [SIGUIENTE 👉🏻](Crear%20componentes.md)