# Controladores ¿que son y como crearlos?

Titular: Niko

Un **Controlador** es una **clase PHP** que organiza la **lógica de tu aplicación**.

En Laravel, se encarga de **recibir la solicitud (request)**, procesarla (por ejemplo, consultar la base de datos) y **devolver una respuesta** (una vista Blade, un JSON, una redirección).

👉 **Sin controladores**, toda la lógica se pondría en `routes/web.php` → eso sería un caos y difícil de mantener.

---

### 📌 **Cómo crear un Controlador**

Usa Artisan para generarlos automáticamente:

```bash
php artisan make:controller UserController

```

Esto crea `app/Http/Controllers/UserController.php`.

---

### ✅ **Ejemplo mínimo**

```php
namespace App\\Http\\Controllers;

use App\\Models\\User;

class UserController extends Controller
{
    // Mostrar todos los usuarios
    public function index() {
        $users = User::all();
        return view('users.index', compact('users'));
    }
}

```

---

### 📌 **¿Dónde se ubican?**

Todos los controladores viven en:

```bash
app/Http/Controllers/

```

Puedes agruparlos por carpetas:

```sql
Controllers/
 ├── Admin/
 ├── Auth/
 ├── API/

```

---

### ✅ **Tip real**

- Si un controlador **solo devuelve una vista estática**, puedes usar closures directamente en la ruta.
- Pero en cuanto tengas **más de 2 rutas relacionadas** → crea un controlador.
- Esto te ayuda a aplicar **Middleware**, **validar Requests**, **organizar mejor el código**.

---
