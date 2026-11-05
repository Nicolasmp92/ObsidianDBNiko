# Comunicación entre componentes

Titular: Niko

## 🔗 **3️⃣ Comunicación entre componentes**

---

Livewire permite que **un componente hable con otro** usando **eventos**.

---

### ✅ **Caso real — Notificar cuando algo cambia**

**Child Component (PostForm)**

```php

$this->emit('postCreated');

```

**Parent Component (PostTable)**

```php

protected $listeners = ['postCreated' => 'reloadPosts'];

public function reloadPosts()
{
    $this->posts = Post::latest()->get();
}

```

✅ **Así funciona:**

1️⃣ El hijo dispara `emit()`.

2️⃣ El padre escucha y ejecuta `reloadPosts()`.

3️⃣ El padre refresca su lista.

---

### 📌 **Pasar parámetros al emitir**

```php

$this->emit('showNotification', 'Guardado exitoso!');

```

```php

protected $listeners = ['showNotification'];

public function showNotification($msg) {
    $this->notification = $msg;
}
```

---

## [👈🏻VOLVER](Crear%20componentes.md)

## [SIGUIENTE 👉🏻](Formularios%20y%20validaciones.md)