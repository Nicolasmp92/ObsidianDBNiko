# Flujo completo — Paso a Paso

Titular: Niko

## ✅ 1️⃣ **Rutas (`web.php`)**

```php

use App\Http\Controllers\UserController;

Route::get('/usuarios', [UserController::class, 'index'])->name('usuarios.index');

Route::get('/usuarios/crear', [UserController::class, 'create'])->name('usuarios.create');

Route::post('/usuarios', [UserController::class, 'store'])->name('usuarios.store');

Route::get('/usuarios/{id}', [UserController::class, 'show'])->name('usuarios.show');

Route::get('/usuarios/{id}/editar', [UserController::class, 'edit'])->name('usuarios.edit');

Route::put('/usuarios/{id}', [UserController::class, 'update'])->name('usuarios.update');

Route::delete('/usuarios/{id}', [UserController::class, 'destroy'])->name('usuarios.destroy');

```

📌 **Clave:** Todo igual, solo que `store` y `update` ahora aceptarán imagen.

---

## ✅ 2️⃣ **Controlador (`UserController.php`)**

```php

<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{
    public function index() {
        $users = User::all();
        return view('usuarios.index', compact('users'));
    }

    public function create() {
        return view('usuarios.create');
    }

    public function store(Request $request) {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users',
            'password' => 'required|string|min:6',
            'profile_image' => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048'
        ]);

        $validated['password'] = Hash::make($validated['password']);

        if ($request->hasFile('profile_image')) {
            $imageName = time() . '.' . $request->profile_image->extension();
            $request->profile_image->move(public_path('uploads/profiles'), $imageName);
            $validated['profile_image'] = 'uploads/profiles/' . $imageName;
        }

        User::create($validated);

        return redirect()->route('usuarios.index')->with('success', 'Usuario creado!');
    }

    public function show($id) {
        $user = User::findOrFail($id);
        return view('usuarios.show', compact('user'));
    }

    public function edit($id) {
        $user = User::findOrFail($id);
        return view('usuarios.edit', compact('user'));
    }

    public function update(Request $request, $id) {
        $user = User::findOrFail($id);

        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email',
            'profile_image' => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048'
        ]);

        if ($request->hasFile('profile_image')) {
            $imageName = time() . '.' . $request->profile_image->extension();
            $request->profile_image->move(public_path('uploads/profiles'), $imageName);
            $validated['profile_image'] = 'uploads/profiles/' . $imageName;
        }

        $user->update($validated);

        return redirect()->route('usuarios.index')->with('success', 'Usuario actualizado!');
    }

    public function destroy($id) {
        $user = User::findOrFail($id);
        $user->delete();

        return redirect()->route('usuarios.index')->with('success', 'Usuario eliminado!');
    }
}

```

---

## ✅ 3️⃣ **Vistas Blade**

📂 Carpeta: `resources/views/usuarios/`

---

### ✔️ `index.blade.php`

```html
<h1>Lista de Usuarios</h1>

<a href="{{ route('usuarios.create') }}">Crear nuevo usuario</a>

<table>
  <thead>
    <tr>
      <th>Nombre</th><th>Email</th><th>Imagen</th><th>Acciones</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($users as $user)
      <tr>
        <td>{{ $user->name }}</td>
        <td>{{ $user->email }}</td>
        <td>
          @if($user->profile_image)
            <img src="{{ asset($user->profile_image) }}" width="50">
          @else
            Sin imagen
          @endif
        </td>
        <td>
          <a href="{{ route('usuarios.edit', $user->id) }}">Editar</a>

          <form method="POST" action="{{ route('usuarios.destroy', $user->id) }}">
            @csrf
            @method('DELETE')
            <button type="submit">Eliminar</button>
          </form>
        </td>
      </tr>
    @endforeach
  </tbody>
</table>

```

---

### ✔️ `create.blade.php`

```html
<h1>Crear Usuario</h1>

<form method="POST" action="{{ route('usuarios.store') }}" enctype="multipart/form-data">
  @csrf

  <input type="text" name="name" placeholder="Nombre"><br>
  <input type="email" name="email" placeholder="Email"><br>
  <input type="password" name="password" placeholder="Contraseña"><br>

  <label>Imagen de perfil:</label>
  <input type="file" name="profile_image"><br>

  <button type="submit">Guardar</button>
</form>

```

---

### ✔️ `edit.blade.php`

```html
<h1>Editar Usuario</h1>

<form method="POST" action="{{ route('usuarios.update', $user->id) }}" enctype="multipart/form-data">
  @csrf
  @method('PUT')

  <input type="text" name="name" value="{{ $user->name }}"><br>
  <input type="email" name="email" value="{{ $user->email }}"><br>

  @if($user->profile_image)
    <p>Imagen actual:</p>
    <img src="{{ asset($user->profile_image) }}" width="100">
  @endif

  <label>Subir nueva imagen:</label>
  <input type="file" name="profile_image"><br>

  <button type="submit">Actualizar</button>
</form>

```

---

## ✅ 4️⃣ **Modelo (`User.php`)**

```php

protected $fillable = ['name', 'email', 'password', 'profile_image'];

```

---

## 📌 Clave

- `enctype="multipart/form-data"` es obligatorio para enviar archivos.
- Las imágenes se guardan en `/public/uploads/profiles`.
- El campo `profile_image` guarda la **ruta relativa**.
- `asset()` en Blade genera la URL correcta.

---

## 🚀 **Resultado**

Tu CRUD ahora:

- **Crea** usuarios con foto.
- **Edita** y **actualiza** foto de perfil.
- Muestra la imagen en la tabla.
- Guarda la ruta en la BD.

---

## [👈🏻VOLVER](Que%20es%20un%20CRUD.md)

## [SIGUIENTE 👉🏻](índex%20Laravel%2012.md)