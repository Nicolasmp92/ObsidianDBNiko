# Comunicación entre componentes

Titular: Niko

## 🔗 **3️⃣ Comunicación entre componentes**

---

Livewire permite que **un componente hable con otro** usando **eventos**.

---

### ✅ **Caso real — Notificar cuando algo cambia**

**Child Component (PostForm)**

```php
php
CopiarEditar
$this->emit('postCreated');

```

**Parent Component (PostTable)**

```php
php
CopiarEditar
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
php
CopiarEditar
$this->emit('showNotification', 'Guardado exitoso!');

```

```php
php
CopiarEditar
protected $listeners = ['showNotification'];

public function showNotification($msg) {
    $this->notification = $msg;
}

```

---

## [👈🏻VOLVER](Crear%20componentes%20227d9e22edae80f1b461e2e1ec4cfef1.md)

## [SIGUIENTE 👉🏻](Formularios%20y%20validaciones%20227d9e22edae80f3aaafd18af4bf28a5.md)