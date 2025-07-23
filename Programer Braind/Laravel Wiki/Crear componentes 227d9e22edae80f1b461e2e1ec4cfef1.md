# Crear componentes

Titular: Niko

## 🧩 **2️⃣ Crear componentes**

---

### 📌 **Crear un componente básico**

```bash
bash
CopiarEditar
php artisan make:livewire TodoList

```

Esto crea:

```
swift
CopiarEditar
app/Livewire/TodoList.php
resources/views/livewire/todo-list.blade.php

```

---

### ✅ **Ejemplo real — Lista de tareas**

**TodoList.php**

```php
php
CopiarEditar
namespace App\\Livewire;

use Livewire\\Component;

class TodoList extends Component
{
    public $tasks = [];
    public $task;

    public function addTask()
    {
        if ($this->task) {
            $this->tasks[] = $this->task;
            $this->task = '';
        }
    }

    public function removeTask($index)
    {
        unset($this->tasks[$index]);
        $this->tasks = array_values($this->tasks);
    }

    public function render()
    {
        return view('livewire.todo-list');
    }
}

```

---

**todo-list.blade.php**

```
blade
CopiarEditar
<div>
    <input type=\"text\" wire:model.defer=\"task\" placeholder=\"Nueva tarea...\">
    <button wire:click=\"addTask\">Agregar</button>

    <ul>
        @foreach ($tasks as $index => $item)
            <li>
                {{ $item }}
                <button wire:click=\"removeTask({{ $index }})\">❌</button>
            </li>
        @endforeach
    </ul>
</div>

```

✅ **Explicación:**

- `public $tasks` → almacena lista.
- `wire:model.defer` → enlaza input con `$task`.
- `wire:click` → llama métodos `addTask` o `removeTask`.
- Cambiar `$tasks` → Livewire actualiza el HTML automáticamente.

---

### 📌 **Renderizarlo en una vista**

```
blade
CopiarEditar
<livewire:todo-list />

```

---

## [👈🏻VOLVER](Introduccio%CC%81n%20a%20Livewire%20227d9e22edae806d83c2cc40717ddf03.md)

## [SIGUIENTE 👉🏻](Comunicacio%CC%81n%20entre%20componentes%20227d9e22edae80418228c49ff3cd2e77.md)