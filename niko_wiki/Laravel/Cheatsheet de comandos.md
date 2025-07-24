# Cheatsheet de comandos

Titular: Niko

<aside>
💡

¿Qué es este Cheatsheet?
Este Cheatsheet no reemplaza la lista completa de comandos Artisan. Es una **hoja de consulta rápida** con los **comandos más usados** organizados por flujo real de desarrollo.  
Úsalo cuando ya sabes **qué hace cada comando** y solo quieres **recordar la sintaxis exacta** sin leer toda la explicación.  

✅ **Tip:** Si tienes dudas sobre **qué hace cada comando**, revisa primero la [**sección completa de Comandos Artisan**](Comandos%20más%20usados.md), donde todo está explicado paso a paso.

</aside>

### ⚙️ **🔑 Instalación y Configuración**

```bash

php artisan key:generate             # Generar APP_KEY
php artisan config:cache             # Cachear configuración
php artisan config:clear             # Limpiar caché de configuración
php artisan cache:clear              # Limpiar caché de la app
php artisan route:cache              # Cachear rutas
php artisan route:clear              # Limpiar caché de rutas
php artisan view:clear               # Limpiar caché de vistas

```

---

### 🧩 **✨ Generación de Código**

```bash

php artisan make:controller NombreController    # Crear controlador
php artisan make:model Nombre                   # Crear modelo
php artisan make:migration create_tabla --create=tabla # Crear migración
php artisan make:seeder NombreSeeder            # Crear seeder
php artisan make:factory NombreFactory          # Crear factory
php artisan make:middleware NombreMiddleware    # Crear middleware
php artisan make:request NombreRequest          # Crear form request
php artisan make:policy NombrePolicy            # Crear policy
php artisan make:resource NombreResource        # Crear resource API

```

---

### 🗄️ **📂 Base de Datos**

```bash

php artisan migrate                 # Ejecutar migraciones
php artisan migrate:rollback        # Revertir último lote de migraciones
php artisan migrate:fresh           # Borrar y migrar desde cero
php artisan migrate:refresh         # Revertir y volver a migrar
php artisan migrate:status          # Ver estado de migraciones
php artisan db:seed                 # Ejecutar seeders
php artisan db:seed --class=UserSeeder  # Ejecutar seeder específico
php artisan schema:dump             # Dump SQL del esquema
php artisan db:wipe                 # Borrar todas las tablas

```

---

### 🔍 **🗺️ Rutas y Utilidades**

```bash

php artisan route:list              # Ver lista de rutas
php artisan storage:link            # Crear enlace storage → public

```

---

### 🚀 **🧪 Consola y Pruebas**

```bash

php artisan tinker                  # Consola interactiva

```

---

### ⚡ **⚙️ Optimización y Mantenimiento**

```bash

php artisan optimize                # Optimizar app (caches)
php artisan optimize:clear          # Limpiar cachés de optimización

```

---

### 📦 **📦 Gestión de Paquetes**

```bash

php artisan vendor:publish          # Publicar archivos de paquetes
php artisan package:discover        # Registrar paquetes

```

---

### 🧵 **⏱️ Colas y Tareas Programadas**

```bash

php artisan queue:work              # Procesar colas
php artisan queue:listen            # Escuchar trabajos en cola
php artisan schedule:run            # Ejecutar tareas programadas

```

---

### 🧭 **ℹ️ Información y Ayuda**

```bash

php artisan list                    # Listar todos los comandos
php artisan help comando            # Ayuda sobre un comando
php artisan --version               # Ver versión de Laravel

```

---

## ✅ **Tips finales Nova**

- ⚡ **TOP uso diario:** `make:*`, `migrate`, `rollback`, `serve`, `route:list`.
- 🧩 **Siempre limpia config:** `config:cache` cada vez que cambies `.env` o `config/`.
- 🧪 **Prueba ideas:** `tinker` es oro puro para probar consultas Eloquent.
- 🗂️ **Al subir a producción:** `optimize` y `route:cache` = app más rápida.

---

## [👈🏻VOLVER](Comandos%20más%20usados.md)

## [SIGUIENTE 👉🏻](Conexión%20a%20MySQL%20phpMyAdmin.md)