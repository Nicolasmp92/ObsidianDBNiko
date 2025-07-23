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

## [👈🏻VOLVER](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)

## [SIGUIENTE 👉🏻](Snippets%20u%CC%81tiles%20227d9e22edae80c3aa98c29d15673880.md)