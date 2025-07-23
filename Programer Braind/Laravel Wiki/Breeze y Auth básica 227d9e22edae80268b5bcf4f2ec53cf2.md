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
bash
CopiarEditar
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

## [👈🏻VOLVER](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)

## [SIGUIENTE 👉🏻](Registro,%20login%20y%20logout%20227d9e22edae80c08b96e3f23d2a81ac.md)