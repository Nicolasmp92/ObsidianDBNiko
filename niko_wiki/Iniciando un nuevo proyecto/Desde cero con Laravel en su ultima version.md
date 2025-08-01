### ✅ Objetivo:

- **Laravel 12**
- **Breeze** con **Bootstrap** (no Tailwind)
- **Bootstrap y AdminLTE 4** instalados vía Vite (localmente)
- Nada de Tailwind CSS
- Preparado para seguir desarrollando tu cafetería

---

## 🧱 Paso a paso limpio (sin Tailwind)

---
### ✅ 1. Crear el proyecto Laravel 12

```bash
`laravel new beanflow_cafe cd beanflow_cafe`
```
---
### ✅ 2. Instalar Breeze con Bootstrap
``` bash
composer require laravel/breeze --dev 
php artisan breeze:install 
npm install
```
Este comando te instala:

- Bootstrap 5
    
- Autenticación completa: login, registro, verificación de email, etc.
    
- Layouts y views base (`layouts/app.blade.php`, `auth/login.blade.php`, etc.)
    

👉 **¡No instala Tailwind!**

---

### ✅ 3. Instalar AdminLTE 4 (vía npm)

bash

CopiarEditar

`npm install admin-lte @fortawesome/fontawesome-free`

---

### ✅ 4. Integrar AdminLTE en los assets existentes

#### `resources/css/app.css`

Reemplaza todo por:

css

CopiarEditar

`@import "admin-lte/dist/css/adminlte.css"; @import "@fortawesome/fontawesome-free/css/all.css"; @import "bootstrap";`

#### `resources/js/app.js`

Reemplaza todo por:

js

CopiarEditar

`import './bootstrap'; import 'admin-lte';`

---

### ✅ 5. Compilar assets

bash

CopiarEditar

`npm run dev`

---

### ✅ 6. Migrar base de datos

bash

CopiarEditar

`php artisan migrate`

---

### ✅ 7. Probar login y vistas

Inicia el servidor:

bash

CopiarEditar

`php artisan serve`

Ve a `http://localhost:8000/register`, regístrate y prueba el sistema.

---

¿Te genero ahora el nuevo layout `layouts/adminlte.blade.php` basado en Breeze + AdminLTE con sidebar y navbar?