# Formularios y validaciones

Titular: Niko

## ✅ **4️⃣ Formularios y Validaciones**

---

Livewire valida igual que Laravel clásico, **pero en vivo**.

---

### 📌 **Ejemplo real — Formulario de usuario**

**UserForm.php**

```php
php
CopiarEditar
public $name;
public $email;

protected $rules = [
    'name' => 'required|min:3',
    'email' => 'required|email|unique:users,email',
];

public function save()
{
    $this->validate();

    User::create([
        'name' => $this->name,
        'email' => $this->email,
    ]);

    session()->flash('message', 'Usuario guardado!');
    $this->reset(['name', 'email']);
}

```

---

**user-form.blade.php**

```
blade
CopiarEditar
<form wire:submit.prevent=\"save\">
    <input type=\"text\" wire:model.lazy=\"name\" placeholder=\"Nombre\">
    @error('name') <span>{{ $message }}</span> @enderror

    <input type=\"email\" wire:model.lazy=\"email\" placeholder=\"Email\">
    @error('email') <span>{{ $message }}</span> @enderror

    <button type=\"submit\">Guardar</button>
</form>

@if (session()->has('message'))
    <p>{{ session('message') }}</p>
@endif

```

---

### 📌 **Explicación clave**

- `wire:model.lazy` → enlaza input con propiedad solo al salir del input (menos peticiones).
- `wire:submit.prevent` → previene reload y llama `save()`.
- `session()->flash()` → mensaje temporal.
- `$this->reset()` → limpia inputs.

---

### ✅ **Validación en vivo**

Puedes validar mientras se escribe:

```php
php
CopiarEditar
public function updated($field)
{
    $this->validateOnly($field);
}

```

✅ Esto valida solo la propiedad que se edita.

---

## ⚙️ **Extras útiles Livewire**

---

### ✅ **wire:loading**

Para mostrar **cargando...**

```
blade
CopiarEditar
<button wire:click=\"save\">Guardar</button>
<span wire:loading>Guardando...</span>

```

---

### ✅ **wire:key**

Útil en listas dinámicas:

```
blade
CopiarEditar
@foreach ($tasks as $index => $task)
  <div wire:key=\"task-{{ $index }}\">{{ $task }}</div>
@endforeach

```

Evita bugs cuando el DOM se reorganiza.

---

### ✅ **Combinar con Alpine.js**

Para interacciones en el navegador:

```
blade
CopiarEditar
<div x-data=\"{ open: false }\">
  <button @click=\"open = !open\">Toggle</button>
  <div x-show=\"open\">Hola!</div>
</div>

```

Livewire y Alpine se **complementan** perfecto.

---

## ✅ **Tips Nova para Livewire**

✔️ Usa `php artisan livewire:make` o `make:livewire` para crear todo más rápido.

✔️ Si algo se rompe, revisa la consola → Livewire da mensajes claros.

✔️ Combina con Laravel Breeze para forms y auth instantáneos.

✔️ Si algo se queda pegado: `php artisan view:clear` o `composer update`.

✔️ Mide bien los estados: **no pongas lógica excesiva en cada render**.

---

## [👈🏻VOLVER](Comunicación%20entre%20componentes.md)

## [SIGUIENTE 👉🏻](Laravel%20index.md)