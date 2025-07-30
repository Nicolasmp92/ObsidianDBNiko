# Registro, login y logout

Titular: Niko

## 🗂️ **2️⃣ Registro, login y logout**

---

### ✅ **Flujo típico**

1️⃣ **Usuario se registra** → se guarda en tabla `users`

2️⃣ **Laravel valida** → campos obligatorios, correo único, password seguro

3️⃣ **Se inicia sesión automáticamente** (si quieres)

4️⃣ **Usuario puede logearse después** → `Auth::attempt` verifica email y password

5️⃣ **Cerrar sesión** → `Auth::logout` destruye la sesión

---

### 📌 **Ejemplo: Registrar usuario**

**Form `register.blade.php`**

```
blade
CopiarEditar
<form method=\"POST\" action=\"{{ route('register') }}\">
    @csrf
    <input type=\"text\" name=\"name\" placeholder=\"Nombre\" required>
    <input type=\"email\" name=\"email\" placeholder=\"Correo\" required>
    <input type=\"password\" name=\"password\" placeholder=\"Contraseña\" required>
    <input type=\"password\" name=\"password_confirmation\" placeholder=\"Repite contraseña\" required>
    <button type=\"submit\">Registrarse</button>
</form>

```

---

### 📌 **Validación y guardado**

**RegisterController.php**

```php
php
CopiarEditar
use App\\Models\\User;
use Illuminate\\Support\\Facades\\Hash;

public function store(Request $request)
{
    $request->validate([
        'name' => 'required',
        'email' => 'required|email|unique:users',
        'password' => 'required|min:8|confirmed',
    ]);

    $user = User::create([
        'name' => $request->name,
        'email' => $request->email,
        'password' => Hash::make($request->password),
    ]);

    Auth::login($user);

    return redirect('/dashboard');
}

```

✅ `Hash::make` cifra el password.

✅ `Auth::login` inicia sesión después de registrar.

---

### 📌 **Login**

**LoginController.php**

```php
php
CopiarEditar
use Illuminate\\Support\\Facades\\Auth;

public function authenticate(Request $request)
{
    $credentials = $request->only('email', 'password');

    if (Auth::attempt($credentials)) {
        $request->session()->regenerate();
        return redirect()->intended('/dashboard');
    }

    return back()->withErrors([
        'email' => 'Credenciales incorrectas',
    ]);
}

```

---

### 📌 **Logout**

```php
php
CopiarEditar
public function logout(Request $request)
{
    Auth::logout();

    $request->session()->invalidate();
    $request->session()->regenerateToken();

    return redirect('/');
}

```

---

## [👈🏻VOLVER](Breeze%20y%20Auth%20básica.md)

## [SIGUIENTE 👉🏻](Roles%20y%20middlewares.md)