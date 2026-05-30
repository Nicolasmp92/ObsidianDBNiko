---
status: Finalizadas
---
_Objetivo: El "seguro de vida". Registrar qué hace cada usuario para soporte y seguridad._

- [x] Crear migración para la tabla `activity_logs` (user_id, action, model, changes, ip, etc). ✅ 2026-05-11
    
- [x] Implementar el Trait `Loggable` para modelos Eloquent. ✅ 2026-05-11
    
- [x] Crear Action `CaptureActivity` para eventos manuales del sistema. ✅ 2026-05-11
    
- [x] Desarrollar una vista básica de historial para el Super Admin. ✅ 2026-05-11

---
#RAMA

``` bash
git checkout dev && git pull origin dev && git checkout -b feature/audit-domain
```

---

#PROMPT


### 🚀 Prompt para SCK-6: Dominio de Auditoría

> **Actúa como Senior Laravel Architect.** Vamos a implementar el **Dominio de Auditoría (Activity Log)** en el **StarterCustomeKit (SCK)** para registrar la trazabilidad de las acciones de los usuarios.
> 
> **Tareas a ejecutar:**
> 
> 1. **Migración:** Crea la tabla `activity_logs` con los campos: `user_id` (nullable), `action` (string, ej: 'created', 'updated'), `model_type` (string), `model_id` (unsignedBigInt), `changes` (json, para guardar el before/after), `ip_address` (string) y `user_agent` (text).
>     
> 2. **Modelo y Dominio:** Crea `app/Domains/Audit/Models/ActivityLog.php`.
>     
> 3. **Trait `Loggable`:** Crea `app/Domains/Audit/Traits/Loggable.php`. Este trait debe usar los "Model Events" de Eloquent (`created`, `updated`, `deleted`) para registrar automáticamente en la tabla de logs. Debe detectar qué campos cambiaron y guardarlos en el campo `changes`.
>     
> 4. **Action `CaptureActivity`:** Crea `app/Domains/Audit/Actions/CaptureActivity.php` con un método `__invoke` para registrar eventos manuales que no dependan de un modelo (ej: "Login fallido", "Exportación de datos").
>     
> 5. **Implementación:** > - Agrega el trait `Loggable` al modelo `User`.
>     
>     - En la vista Volt `resources/views/livewire/users/index.blade.php`, reemplaza el feed estático de "User Activity" del Dashboard por una consulta real a los últimos 5-10 registros de `ActivityLog`.
>         
> 6. **Validación:** Ejecuta `php artisan test` para asegurar que la infraestructura base no se rompió y que los logs se están guardando al crear o editar un usuario.
>



---


#resultado 

# Resumen: Dominio Audit (Activity Log)

## Implementación completa

### 1. Migración
- [database/migrations/2026_05_11_200000_create_activity_logs_table.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/database/migrations/2026_05_11_200000_create_activity_logs_table.php:0:0-0:0)
- Campos: `user_id`, `action`, `model_type`, `model_id`, `changes` (json), `ip_address`, `user_agent`
- Índices en `model_type/model_id`, `user_id`, `created_at`

### 2. Modelo
- [app/Domains/Audit/Models/ActivityLog.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Models/ActivityLog.php:0:0-0:0)
- Relación `BelongsTo` a [User](cci:9://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User:0:0-0:0)
- Método [actionLabel()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Models/ActivityLog.php:65:4-79:5) → texto descriptivo por acción
- Método [actionMeta()](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Models/ActivityLog.php:47:4-63:5) → array con icono Lucide y colores Tailwind

### 3. Trait Loggable
- [app/Domains/Audit/Traits/Loggable.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Traits/Loggable.php:0:0-0:0)
- Escucha eventos Eloquent: `created`, `updated`, `deleted`
- Construye payload `before/after` con cambios detectados
- Excluye campos sensibles: [password](cci:9://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/livewire/password:0:0-0:0), `remember_token`, `two_factor_*`
- Envuelto en `try/catch` para no romper lógica de negocio

### 4. Action CaptureActivity
- [app/Domains/Audit/Actions/CaptureActivity.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Actions/CaptureActivity.php:0:0-0:0)
- Para eventos manuales sin modelo (login, logout, exports)
- Firma: [__invoke(string $action, ?string $modelType, ?int $modelId, array $changes)](cci:1://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/User/Actions/UpdateUser.php:26:4-69:5)

### 5. Integraciones
- **User model** → agregado `use Loggable` (audita automático)
- **AuthenticateUser** → inyecta [CaptureActivity](cci:2://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/app/Domains/Audit/Actions/CaptureActivity.php:13:0-39:1), registra `login` y `login_failed`
- **Dashboard** → feed real con 8 últimos ActivityLog, iconos dinámicos, usuario, fecha e IP

### 6. Validación
- Migración ejecutada: ✓
- Tests: 26/28 pasan (2 fallos pre-existentes de Breeze, no relacionados)

## Archivo de cambios por sesión

| Archivo                                                                                                                                                                                                                                          | Estado                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| [resources/views/profile/edit.blade.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/profile/edit.blade.php:0:0-0:0)                                                                         | Refactorizado con estilos del módulo users |
| [resources/views/livewire/profile/update-profile-information-form.blade.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/livewire/profile/update-profile-information-form.blade.php:0:0-0:0) | Estilos zinc/indigo, SweetAlert notify     |
| [resources/views/livewire/profile/update-password-form.blade.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/livewire/profile/update-password-form.blade.php:0:0-0:0)                       | Estilos zinc/indigo, SweetAlert notify     |
| [resources/views/livewire/profile/delete-user-form.blade.php](cci:7://file://wsl.localhost/Ubuntu-24.04/home/niko/Proyectos/StarterCustomeKit/resources/views/livewire/profile/delete-user-form.blade.php:0:0-0:0)                               | Modal inline con Alpine, estilos zinc      |
| `app/Domains/Audit/` (dominio completo)                                                                                                                                                                                                          | Nuevo                                      |


