# 🐘 # Wiki: Instalar Laravel + Breeze (Tailwind, sin Bootstrap)

> **Objetivo**: Dejar tu proyecto Laravel recién creado corriendo con **autenticación** lista, **TailwindCSS** y (opcional) **Livewire**.  
> **Stack recomendado para ti**: `livewire` (Volt Class API + Alpine + Tailwind).

---

## 📦 Requisitos previos (una sola vez)

- **PHP 8.2+** (XAMPP/WAMP/Valet/Docker).
    
- **Composer** (gestor de dependencias PHP).
    
- **Node.js 18+** y **npm** (para compilar assets con Vite).
    
- Servidor MySQL activo (XAMPP u otro).
    

> 💡 Verifica versiones:

`php -v composer -V node -v npm -v`

---

## 🛠️ Instalación paso a paso (proyecto nuevo)

### 1) Crear el proyecto y entrar a la carpeta

`composer create-project laravel/laravel mi_proyecto cd mi_proyecto`

- **Qué hace**: descarga Laravel y prepara su esqueleto inicial.
    

---

### 2) Generar `.env` y `APP_KEY`

`# Linux/Mac cp .env.example .env # Windows PowerShell copy .env.example .env  php artisan key:generate`

- **Qué hace**: `.env` guarda tus credenciales/variables locales.
    
- `key:generate` crea `APP_KEY` (clave de cifrado de sesiones/tokens).
    

---

### 3) Configurar base de datos en `.env`

Abre el archivo `.env` y ajusta:

`DB_CONNECTION=mysql DB_HOST=127.0.0.1 DB_PORT=3306        # si cambiaste el puerto en XAMPP, pon ese DB_DATABASE=mi_proyecto DB_USERNAME=root DB_PASSWORD=`

> 💡 Crea la BD vacía en phpMyAdmin con el mismo nombre (`mi_proyecto`).

---

### 4) Instalar Breeze

`composer require laravel/breeze --dev php artisan breeze:install`

Al ejecutar el instalador, verás:

`Which Breeze stack would you like to install?    Blade with Alpine ...................... blade   Livewire (Volt Class API) with Alpine .. livewire   Livewire (Volt Functional API) with Alpine .. livewire-functional   React with Inertia ..................... react   Vue with Inertia ....................... vue   API only ............................... api`

**¿Cuál elijo?**

- **`blade`** → Blade + Tailwind + Alpine (simple y liviano).
    
- **`livewire`** → **Recomendado para ti** (Tailwind + Alpine + Livewire).
    
- `livewire-functional` → Livewire sintaxis funcional (más nuevo).
    
- `react` / `vue` → con Inertia (si vas full SPA).
    
- `api` → sólo endpoints de auth (sin frontend).
    

---

### 5) Instalar dependencias front y compilar

`npm install npm run dev`

- **Qué hace**: descarga paquetes JS y levanta **Vite** en modo desarrollo con **Tailwind** listo.
    

> 📝 _No_ uses `composer run dev` a menos que tú definas ese script en `composer.json`. El estándar es `npm run dev`.

---

### 6) Migraciones de base de datos

`php artisan migrate`

- **Qué hace**: crea tablas iniciales (users, passwords, etc.).
    

---

### 7) Levantar el servidor

`php artisan serve`

Abre 👉 `http://127.0.0.1:8000`

Con Breeze tendrás rutas para:

- Login: `/login`
    
- Registro: `/register`
    
- Password reset: `/forgot-password`
    
- Email verification: `/verify-email` (si lo habilitas)
    

---

## 📚 ¿Qué es Breeze?

- **Starter kit oficial** para auth básica (login, registro, reset, verificación).
    
- Usa **Tailwind CSS** + **Alpine.js**.
    
- Ofrece stacks: **Blade**, **Livewire**, **React**, **Vue** o **API only**.
    

### Diccionario rápido Breeze

- **Blade** → motor de plantillas de Laravel.
    
- **Alpine.js** → JS mínimo para interactividad.
    
- **TailwindCSS** → utilidades CSS.
    
- **Livewire** → componentes PHP reactiv@s sin escribir mucho JS.
    
- **Volt** → forma moderna de declarar componentes Livewire.
    
- **Inertia** → puente Laravel ↔ React/Vue (sin API REST explícita).
    
- **API Only** → endpoints de auth sin vistas.
    

---

## 🗂️ Estructura que agrega Breeze

Según el stack, encontrarás:

- **Rutas**: `routes/auth.php`
    
- **Controladores**: `app/Http/Controllers/Auth/*`
    
- **Vistas**: `resources/views/auth/*`
    
- **Componentes Livewire** (si elegiste `livewire`)
    
- **Tailwind + Vite** ya configurados en `resources/` y `vite.config.js`
    

---

## 🔐 Email / Reset de contraseña (importante)

Para que **reset de contraseña** y **verificación de email** funcionen, configura correo en `.env`:

`MAIL_MAILER=smtp MAIL_HOST=smtp.gmail.com MAIL_PORT=587 MAIL_USERNAME=tu_correo@gmail.com MAIL_PASSWORD=tu_password_o_app_password MAIL_ENCRYPTION=tls MAIL_FROM_ADDRESS=tu_correo@gmail.com MAIL_FROM_NAME="${APP_NAME}"`

> 💡 En desarrollo puedes usar **Mailhog**, **Mailpit** o **Mailtrap** para testear emails sin enviar reales.

---

## 🧩 Pasos opcionales útiles (recomendados)

### A) Crear usuario rápido (sin registro)

`php artisan tinker >>> \App\Models\User::factory()->create(['email' => 'admin@example.com', 'password' => bcrypt('secret')]);`

### B) Enlaces de almacenamiento (uploads)

`php artisan storage:link`

- **Qué hace**: crea enlace `public/storage` para servir archivos subidos.
    

### C) Limpiar cachés si algo se rompe

`php artisan optimize:clear`

### D) Compilar para producción

`npm run build`

---

## 🧭 Guía corta (checklist mínimo)

1. `composer create-project laravel/laravel mi_proyecto`
    
2. `cd mi_proyecto`
    
3. Copiar `.env` y **generar key**:
    
    - `cp .env.example .env` (o `copy .env.example .env`)
        
    - `php artisan key:generate`
        
4. Configurar DB en `.env`
    
5. `composer require laravel/breeze --dev`
    
6. `php artisan breeze:install` → elige **`livewire`** (recomendado)
    
7. `npm install && npm run dev`
    
8. `php artisan migrate`
    
9. `php artisan serve` → abre `http://127.0.0.1:8000`
    

---

## 🧯 Problemas comunes y fixes rápidos

- **MySQL no conecta** (`SQLSTATE[HY000] [2002]`):
    
    - Verifica puerto (`DB_PORT`) y que MySQL esté arriba (XAMPP).
        
    - Crea la BD en phpMyAdmin con el **mismo nombre** que en `.env`.
        
- **Node/NPM no encontrados**:
    
    - Instala Node LTS 18+ y reinicia terminal.
        
- **Tailwind no aplica estilos**:
    
    - Asegúrate de haber corrido `npm run dev` y que la página cargue los assets de Vite.
        
    - Revisa `resources/css/app.css` y que `@vite(['resources/css/app.css','resources/js/app.js'])` esté en tu layout.
        
- **Errores raros de caché**:
    
    - `php artisan optimize:clear`
        

---

## 🎯 ¿Cuándo elegir cada stack?

- **blade**: Sitios simples, server-rendered, poco JS.
    
- **livewire (recomendado)**: Formularios y dashboards reactivos sin SPA.
    
- **react/vue (Inertia)**: Si quieres SPA sin armar API separada.
    
- **api**: Backend puro para frontend aparte (mobile/SPA).
    

---

## 🧪 Mini explicación de cada paso (como profe 🧑‍🏫)

- `composer create-project` → descarga el esqueleto de Laravel.
    
- `cp .env.example .env` → crea tu archivo de variables local.
    
- `php artisan key:generate` → clave de cifrado para sesiones/tokens.
    
- Config DB en `.env` → para que Eloquent se conecte.
    
- `composer require laravel/breeze --dev` → trae el instalador de auth.
    
- `php artisan breeze:install` → genera vistas/rutas/controladores de auth y stack elegido.
    
- `npm install && npm run dev` → compila Tailwind y levanta Vite para assets.
    
- `php artisan migrate` → crea tablas base (users, etc.).
    
- `php artisan serve` → servidor local para ver la app.