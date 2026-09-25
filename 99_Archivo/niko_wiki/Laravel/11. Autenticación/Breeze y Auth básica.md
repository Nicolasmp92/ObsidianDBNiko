# Breeze y Auth básica

Titular: Niko

### ✅ **¿Qué es Breeze?**

**Breeze** es un **starter kit oficial** de Laravel para implementar **autenticación básica** (registro, login, logout) **rápido y sin complicaciones**.

Incluye:

- Formularios Blade ya listos
- Controladores para registrar y autenticar usuarios
- Rutas protegidas
- Middleware `auth`
- Validación y sesión configurada

---

### 📌 **Instalación paso a paso**

```bash

composer require laravel/breeze --dev

php artisan breeze:install

npm install && npm run dev

php artisan migrate

```

✔️ Esto:

1️⃣ Instala Breeze

2️⃣ Crea vistas de login, registro y dashboard

3️⃣ Genera rutas y controladores (`AuthController`)

4️⃣ Migra tablas (`users`)

---

### ✅ **Estructura generada**

- `routes/web.php` → rutas `/login`, `/register`, `/dashboard`
- `app/Http/Controllers/Auth/` → controladores de registro y login
- `resources/views/auth/` → vistas Blade: `login.blade.php`, `register.blade.php`
- Middleware `auth` ya aplicado

---
**IMPORTANTE:** seguramente cuando crees un nuevo proyecto, querrás asignar roles a tu aplicación, esto generalmente se puede hacer de forma manual pero existe un complemento llamado [[Spatie Laravel-Permission]] que te permite gestionar los roles de una forma mas eficas. 


## [👈🏻VOLVER](índex%20Laravel%2012.md)

## [SIGUIENTE 👉🏻](Registro,%20login%20y%20logout.md)