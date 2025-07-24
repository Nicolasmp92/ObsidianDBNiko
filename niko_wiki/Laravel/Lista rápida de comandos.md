# Lista rápida de comandos

Titular: Niko

## ✅ **1️⃣ Lista rápida de comandos**

Estos son **Artisan** y otros básicos que **sí o sí usarás a diario**:

---

### 📌 **Migraciones y Base de Datos**

```bash

php artisan migrate           # Ejecuta migraciones pendientes
php artisan migrate:rollback  # Revertir última migración
php artisan migrate:refresh   # Revertir y volver a correr
php artisan migrate:fresh     # Borrar todas las tablas y migrar
php artisan db:seed           # Ejecutar seeders
php artisan migrate:fresh --seed  # Limpiar y poblar en uno

```

---

### 📌 **Generar Código**

```bash

php artisan make:model NombreModelo
php artisan make:controller NombreController
php artisan make:migration create_table --create=tabla
php artisan make:seeder NombreSeeder
php artisan make:factory NombreFactory --model=Modelo
php artisan make:middleware NombreMiddleware
php artisan make:request NombreRequest
php artisan make:policy NombrePolicy
php artisan make:resource NombreResource
php artisan make:command NombreComando

```

---

### 📌 **Servidor y Optimización**

```bash

php artisan serve                # Iniciar servidor local
php artisan optimize             # Generar archivos cacheados
php artisan optimize:clear       # Limpiar cachés optimizados
php artisan route:list           # Ver todas las rutas y métodos
php artisan tinker               # Abrir consola interactiva

```

---

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Snippets%20útiles.md)