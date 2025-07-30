# 🛡️ Manejo de Roles en Laravel con Breeze y Spatie Laravel-Permission

## 📌 Introducción

En una aplicación Laravel, asignar **roles** a los usuarios es fundamental para controlar el acceso a diferentes partes del sistema. Esta entrada explica **la forma más óptima y escalable** de trabajar roles, utilizando el paquete **Spatie Laravel-Permission** junto con **Laravel Breeze** como sistema de autenticación base.

---

## ⚙️ ¿Qué hace Laravel Breeze?

Cuando instalamos Laravel Breeze y ejecutamos las migraciones, se crean automáticamente estas tablas:

- `users`: tabla principal de usuarios.
- `password_reset_tokens`: recuperación de contraseñas.
- `personal_access_tokens`: tokens de API (opcional, usado por Sanctum).

```bash
php artisan breeze:install
php artisan migrate
```
✅ Ya tienes tu tabla users lista para usar.

📦 Instalando Spatie Laravel-Permission
Este paquete permite asignar roles y/o permisos a los usuarios de forma flexible.

📥 Instalación
```
composer require spatie/laravel-permission
```
📤 Publicar migraciones y migrar
```bash
php artisan vendor:publish --provider="Spatie\Permission\PermissionServiceProvider"
php artisan migrate
```
🧱 Tablas que se crean automáticamente:

|Tabla|Descripción|
|---|---|
|`roles`|Lista de roles (`admin`, `editor`, etc.)|
|`permissions`|Permisos individuales (opcional)|
|`model_has_roles`|Relaciona usuarios con roles|
|`model_has_permissions`|Relaciona usuarios con permisos|
|`role_has_permissions`|Relaciona roles con permisos|
✅ Si solo usarás roles (sin permisos), puedes ignorar las de permissions.

🔗 Configuración en el Modelo User
En el archivo app/Models/User.php, agregar el trait:

```php
use Spatie\Permission\Traits\HasRoles;

class User extends Authenticatable
{
    use HasRoles;
}
```
🛠️ Creación de Roles
Puedes crear los roles desde Tinker o desde un seeder:
```php

use Spatie\Permission\Models\Role;

Role::create(['name' => 'admin']);
Role::create(['name' => 'editor']);
Role::create(['name' => 'ventas']);
```
👤 Asignar un rol a un usuario
```php

$user = User::find(1);
$user->assignRole('admin');
```
También puedes usar:
```php
$user->syncRoles(['editor']); // Elimina otros roles y asigna solo este
```
🔐 Validar rol en vistas Blade
```blade
@role('admin')
    <a href="/admin">Panel de Administración</a>
@endrole

@if(auth()->user()->hasRole('editor'))
    <p>Bienvenido, editor.</p>
@endif
```
🔐 Middleware por rol
En routes/web.php puedes proteger rutas así:
```
Route::middleware(['role:admin'])->group(function () {
    Route::get('/dashboard', [AdminController::class, 'index']);
});
```
Para múltiples roles:
```php

Route::middleware(['role:admin|editor'])->group(function () {
    // Rutas compartidas
});
```
🧪 Verificación rápida desde Tinker
```bash

php artisan tinker
>>> $user = \App\Models\User::find(1)
>>> $user->hasRole('admin') // true o false
>>> ```
## ✅ Conclusión

Usar **Spatie Laravel-Permission** junto con **Breeze** permite:

- Una solución **profesional y escalable**.
    
- Separar lógica de roles y permisos claramente.
    
- Aplicar seguridad con middleware o en Blade.
    
- Usar métodos directos como `hasRole()`, `assignRole()`, `syncRoles()`.
    
Ideal para proyectos con múltiples perfiles como:

- `admin`
    
- `editor`
    
- `ventas`

|Tipo de proyecto|Enfoque recomendado|
|---|---|
|Proyecto pequeño|`users.rol` (columna simple)|
|Proyecto mediano|Relación muchos a muchos|
|Proyecto profesional|✅ Spatie Laravel-Permission|
