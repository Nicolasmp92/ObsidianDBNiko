# Métodos (index, create, store…)

Titular: Niko

### 🟢 **`index()` — Mostrar todos**

- 📌 **Qué hace:** Lista **todos los recursos** de ese modelo (Posts, Users, Productos).
- 📌 **Para qué sirve:** Páginas de inicio, panel de admin, listado con paginación.
- 📌 **Qué devuelve:** Una **vista Blade** con una **colección** de filas.

```php
public function index() {
    $posts = Post::latest()->paginate(10);
    return view('posts.index', compact('posts'));
}

```

**Ejemplo:**

Visitas `/posts` → Ves una tabla con los últimos 10 posts.

---

### 🟢 **`create()` — Formulario de creación**

- 📌 **Qué hace:** Muestra un **formulario vacío** para crear un nuevo recurso.
- 📌 **Para qué sirve:** Mostrar campos `<input>` para llenar datos nuevos.
- 📌 **Qué devuelve:** Una **vista Blade** con el formulario.

```php
public function create() {
    return view('posts.create');
}

```

**Ejemplo:**

Visitas `/posts/create` → Ves un formulario para escribir un nuevo post.

---

### 🟢 **`store()` — Guardar nuevo**

- 📌 **Qué hace:** Procesa **los datos enviados** desde `create()` y **los guarda** en la base.
- 📌 **Para qué sirve:** Validar datos, crear fila nueva.
- 📌 **Qué devuelve:** Redirige a `index()` o `show()` con mensaje.

```php
public function store(Request $request) {
    $validated = $request->validate([
        'title' => 'required|min:3',
        'body' => 'required|min:10',
    ]);

    Post::create($validated);

    return redirect()->route('posts.index')->with('success', 'Post creado!');
}

```

**Ejemplo:**

Rellenas formulario → haces submit → `store()` guarda y redirige al listado.

---

### 🟢 **`show($id)` — Ver uno solo**

- 📌 **Qué hace:** Muestra **un recurso específico** (una fila).
- 📌 **Para qué sirve:** Ver detalles de un post, perfil de usuario, ficha de producto.
- 📌 **Qué devuelve:** Una **vista Blade** con **solo una fila**.

```php
public function show($id) {
    $post = Post::findOrFail($id);
    return view('posts.show', compact('post'));
}

```

**Ejemplo:**

Visitas `/posts/5` → Ves solo el post #5.

✅ **Tip:** Si no existe, `findOrFail()` devuelve **404 automático**.

---

### 🟢 **`edit($id)` — Formulario de edición**

- 📌 **Qué hace:** Muestra un formulario **con los datos ya cargados**.
- 📌 **Para qué sirve:** Editar algo existente.
- 📌 **Qué devuelve:** Una **vista Blade** con formulario + valores actuales.

```php
public function edit($id) {
    $post = Post::findOrFail($id);
    return view('posts.edit', compact('post'));
}

```

**Ejemplo:**

Visitas `/posts/5/edit` → Formulario con título y cuerpo llenos.

---

### 🟢 **`update()` — Guardar cambios**

- 📌 **Qué hace:** Procesa los datos editados y **actualiza la fila**.
- 📌 **Para qué sirve:** Aplicar cambios del formulario de `edit()`.
- 📌 **Qué devuelve:** Redirige a `index()` o `show()`.

```php
public function update(Request $request, $id) {
    $validated = $request->validate([
        'title' => 'required',
        'body' => 'required',
    ]);

    $post = Post::findOrFail($id);
    $post->update($validated);

    return redirect()->route('posts.index')->with('success', 'Post actualizado!');
}

```

**Ejemplo:**

Envías formulario de edición → `update()` actualiza → vuelves a la lista.

---

### 🟢 **`destroy()` — Borrar**

- 📌 **Qué hace:** Elimina la fila de la base.
- 📌 **Para qué sirve:** Borrar un post, eliminar un usuario.
- 📌 **Qué devuelve:** Redirige a `index()` con mensaje de éxito.

```php
public function destroy($id) {
    $post = Post::findOrFail($id);
    $post->delete();

    return redirect()->route('posts.index')->with('success', 'Post eliminado!');
}

```

**Ejemplo:**

Click en botón “Eliminar” → `destroy()` borra → vuelves a la lista sin el recurso.

---

## ✅ **Tips finales Nova**

✔️ Usa `Route::resource('posts', PostController::class)` → Laravel mapea todo.

✔️ `findOrFail` = 404 automático si no existe.

✔️ Valida SIEMPRE → `validate()` o **Form Requests**.

✔️ Usa `with('success', '...')` para flash messages.

✔️ Mantén 1 Controlador por recurso: limpio y entendible.

---

## [👈🏻VOLVER](Resource%20Controllers%20y%20REST.md)

## [SIGUIENTE 👉🏻](Laravel%20index.md)