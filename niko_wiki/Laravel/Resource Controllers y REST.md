# Resource Controllers y REST

Titular: Niko

### **📌 ¿Qué es un CONTROLADOR?**

Un **Controlador** es una **clase PHP** (archivo `.php`) que **organiza la lógica de tu app web**.

**Piénsalo así:**

- 📥 **Recibe la petición** → lo que hace el usuario (URL, formulario, botón).
- ⚙️ **Procesa la acción** → consulta base de datos, valida datos, aplica reglas.
- 📤 **Devuelve la respuesta** → muestra una página (Blade), un JSON (API), redirige, etc.

---

### ✅ **¿Qué es REST?**

**REST** (Representational State Transfer) es un **estándar** para organizar **rutas y controladores** de forma predecible y coherente.

Laravel usa REST para que cada **recurso** (Posts, Users, Products) tenga:

- **URLs claras y semánticas**
- **Métodos separados por acción**

---

**Ejemplo mental:**

Un `PostController` REST **organiza toda la lógica CRUD** de *Posts* sin inventar rutas raras.

---

### ✅ **¿Qué es un Resource Controller?**

Un **Resource Controller** es un controlador que **ya viene estructurado** con los **7 métodos REST (RESTful)** más comunes ICSSEUD:

| Método    | Qué hace                       |
| --------- | ------------------------------ |
| `index`   | Mostrar todos los recursos     |
| `create`  | Mostrar formulario de creación |
| `store`   | Guardar el nuevo recurso       |
| `show`    | Mostrar uno solo               |
| `edit`    | Mostrar formulario de edición  |
| `update`  | Actualizar recurso             |
| `destroy` | Borrar recurso                 |

---

### 📌 **Cómo crear uno**

```bash
php artisan make:controller ProductController --resource

```

Laravel crea:

```php
class ProductController extends Controller
{
    public function index() { /* Mostrar lista */ }
    public function create() { /* Form crear */ }
    public function store(Request $request) { /* Guardar */ }
    public function show($id) { /* Mostrar uno */ }
    public function edit($id) { /* Form editar */ }
    public function update(Request $request, $id) { /* Actualizar */ }
    public function destroy($id) { /* Borrar */ }
}

```

---

### ✅ **Cómo registrar un Resource Controller**

“Registrar” = decirle a Laravel *qué URLs usarán este controlador*.

```php
Route::resource('products', ProductController::class);

```

Esto genera rutas REST automáticamente:

- `GET /products` → `index()`
- `GET /products/create` → `create()`
- `POST /products` → `store()`
- `GET /products/{id}` → `show()`
- `GET /products/{id}/edit` → `edit()`
- `PUT /products/{id}` → `update()`
- `DELETE /products/{id}` → `destroy()`

---

### ✅ **¿Por qué usar Resource Controllers?**

✔️ Organiza tu lógica **en un solo archivo** → fácil de encontrar.

✔️ Sigue **un estándar universal** → todos los devs Laravel entienden `index()`, `store()`, etc.

✔️ **Ahorras tiempo:** defines todas las rutas de golpe, no una por una.

---

### ✅ **Ejemplo real PostController**

```php
<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Storage;

class UserController extends Controller
{
    // 🧾 Mostrar todos los usuarios
    public function index()
    {
        $usuarios = User::latest()->paginate(10);
        return view('usuarios.index', compact('usuarios'));
    }

    // 🧾 Formulario para crear nuevo usuario
    public function create()
    {
        return view('usuarios.create');
    }

    // 🧾 Guardar nuevo usuario con imagen
    public function store(Request $request)
    {
        $request->validate([
            'name'     => 'required|string|min:3',
            'email'    => 'required|email|unique:users,email',
            'password' => 'required|min:6',
            'image'    => 'nullable|image|max:2048', // imagen opcional
        ]);

        $data = $request->all();
        $data['password'] = Hash::make($data['password']);

        if ($request->hasFile('image')) {
            $data['image'] = $request->file('image')->store('usuarios', 'public');
        }

        User::create($data);

        return redirect()->route('usuarios.index')->with('success', 'Usuario creado correctamente.');
    }

    // 🧾 Mostrar un solo usuario
		   public function show($id)
		{
		    $usuario = User::findOrFail($id); // 🔍 Busca al usuario, o lanza error 404 si no existe
		
		    return view('usuarios.show', compact('usuario'));
		}

    // 🧾 Formulario para editar usuario
    public function edit(User $usuario)
    {
        return view('usuarios.edit', compact('usuario'));
    }

    // 🧾 Actualizar usuario
    public function update(Request $request, User $usuario)
    {
        $request->validate([
            'name'     => 'required|string|min:3',
            'email'    => 'required|email|unique:users,email,' . $usuario->id,
            'image'    => 'nullable|image|max:2048',
        ]);

        $data = $request->all();

        if ($request->hasFile('image')) {
            // Borra imagen anterior si existe
            if ($usuario->image) {
                Storage::disk('public')->delete($usuario->image);
            }
            $data['image'] = $request->file('image')->store('usuarios', 'public');
        }

        $usuario->update($data);

        return redirect()->route('usuarios.index')->with('success', 'Usuario actualizado.');
    }

    // 🧾 Eliminar usuario
    public function destroy(User $usuario)
    {
        if ($usuario->image) {
            Storage::disk('public')->delete($usuario->image);
        }

        $usuario->delete();

        return redirect()->route('usuarios.index')->with('success', 'Usuario eliminado.');
    }
}
```

---

**✅ Resultado:**

Un solo archivo maneja toda la lógica CRUD de **Posts**, sin rutas duplicadas ni closures sueltos.

---

## [👈🏻VOLVER](Controladores%20¿que%20son%20y%20como%20crearlos.md)

## [SIGUIENTE 👉🏻](Métodos%20(index,%20create,%20store…).md)