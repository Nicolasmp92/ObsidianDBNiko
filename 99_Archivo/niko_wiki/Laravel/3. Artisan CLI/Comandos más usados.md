# Comandos más usados

Titular: Niko

### ⚙️ **1️⃣ Instalación y Configuración**

```bash

php artisan key:generate             # Genera APP_KEY de la aplicación
php artisan config:cache             # Genera caché de configuración
php artisan config:clear             # Limpia caché de configuración
php artisan cache:clear              # Limpia caché general de la app
php artisan route:cache              # Genera caché de rutas
php artisan route:clear              # Limpia caché de rutas
php artisan view:clear               # Limpia caché de vistas compiladas

```

---

### 🧩 **2️⃣ Generación de Código**

```bash

php artisan make:controller NombreController    # Crear controlador
php artisan make:model Nombre                   # Crear modelo Eloquent
php artisan make:modell nombre -cr              # Crea un modelo + un controlador con formato resources
php artisan make:migration create_nombre_table --create=nombre_tabla # Crear migración
php artisan make:seeder NombreSeeder            # Crear seeder
php artisan make:factory NombreFactory          # Crear factory
php artisan make:middleware NombreMiddleware    # Crear middleware
php artisan make:request NombreRequest          # Crear form request
php artisan make:policy NombrePolicy            # Crear policy de autorización
php artisan make:command NombreComando          # Crear comando personalizado
php artisan make:resource NombreResource        # Crear resource para API

```

---

### 🗄️ **3️⃣ Base de Datos**

```bash
php artisan migrate                 # Ejecutar migraciones pendientes
php artisan migrate:fresh           # Borrar tablas y volver a migrar desde cero
php artisan migrate:refresh         # Revertir y volver a migrar
php artisan migrate:reset           # Revertir todas las migraciones
php artisan migrate:rollback        # Revertir último lote de migraciones
php artisan migrate:status          # Mostrar estado de migraciones
php artisan migrate:install         # Crear tabla de control de migraciones

php artisan db:seed                 # Ejecutar seeders
php artisan db:seed --class=UserSeeder  # Ejecutar seeder específico
php artisan schema:dump             # Generar archivo SQL del esquema
php artisan db:wipe                 # Eliminar todas las tablas, vistas y tipos

```

---

### 🚀 **4️⃣ Servidor de Desarrollo**

```bash
php artisan serve                   # Iniciar servidor local (http://127.0.0.1:8000)
php artisan serve --port=8080       # Iniciar servidor en puerto específico

```

---

### 🧪 **5️⃣ Tinker**

```bash
php artisan tinker                  # Abrir consola interactiva para probar código/Eloquent

```

---

### ⚡ **6️⃣ Optimización y Mantenimiento**

```bash
php artisan optimize                # Optimizar aplicación (cachea rutas, config)
php artisan optimize:clear          # Limpiar caché de optimización

```

---

### 📦 **7️⃣ Gestión de Paquetes**

```bash
php artisan vendor:publish          # Publicar archivos de configuración/vistas de paquetes
php artisan package:discover        # Registrar paquetes automáticamente

```

---

### 🧵 **8️⃣ Colas y Scheduling**

```bash
php artisan queue:work              # Procesar trabajos encolados
php artisan queue:listen            # Escuchar trabajos en cola continuamente
php artisan schedule:run            # Ejecutar tareas programadas (cron)
php artisan storage:link            # Crear enlace simbólico `storage/app/public` → `public/storage`

```

---

### 🧐 **9️⃣ Información y Ayuda**

```bash

php artisan list                    # Mostrar todos los comandos disponibles
php artisan help nombre-comando     # Mostrar ayuda de un comando específico
php artisan --version               # Mostrar versión de Laravel

```

---

## ✅ **Notas Finales**

📌 **Tip:** Cuando no recuerdes algo, usa `php artisan list` para ver todo, o `php artisan help comando` para ver cómo se usa cada uno.

💡 **Truco:** Es buena práctica correr `optimize:clear` antes de subir a producción si has cambiado rutas, vistas o config.

---

## [👈🏻VOLVER](Qué%20es%20Artisan.md)

## [SIGUIENTE 👉🏻](Conexión%20a%20MySQL%20phpMyAdmin.md)