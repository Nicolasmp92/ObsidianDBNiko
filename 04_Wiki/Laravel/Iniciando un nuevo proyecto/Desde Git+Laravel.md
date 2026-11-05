# 🚀 Clonar y Configurar un Proyecto Laravel 12 desde GitHub

## 📦 Requisitos previos

Antes de comenzar asegúrate de tener instalado:

- [[Index PHP|PHP 8.2 o superior]]
- [[2. Composer]]
- Node.js y npm (opcional, para compilar assets)
- MySQL o MariaDB
- Git
- Un servidor local como Laravel Valet, XAMPP, WAMP, Laragon o similar

---

## 📁 Paso 1: Clonar el repositorio

Abre la terminal y ejecuta:

```bash
git clone https://github.com/usuario/nombre-del-repositorio.git
```

🔹 Esto creará una carpeta con el nombre del proyecto, descargando todos los archivos del repositorio.

## 📂 Paso 2: Ingresar a la carpeta del proyecto

```bash
cd nombre-del-repositorio
```

## 🧬 Paso 3: Instalar dependencias de PHP con Composer

```bash
composer install
```

📌 Este comando leerá el archivo composer.json e instalará todas las librerías necesarias, como Laravel y sus paquetes.

## 🔒 Paso 4: Copiar el archivo .env
Laravel utiliza este archivo para la configuración del entorno (base de datos, correo, claves, etc.)
```bash
cp .env.example .env
```

## 🔑 Paso 5: Generar la APP_KEY

```bash
php artisan key:generate
```

🧩 Laravel necesita esta clave para cifrar contraseñas y sesiones.

## ⚙️ Paso 6: Configurar la base de datos
Abre el archivo **.env** y edita estas líneas con tus datos de conexión:
```ini
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nombre_base_datos
DB_USERNAME=usuario
DB_PASSWORD=contraseña
```

🛠️ Si usas phpMyAdmin, crea primero la base de datos manualmente.

## 🛠️ Paso 7: Ejecutar migraciones
bash
```
php artisan migrate
```
Esto creará todas las tablas necesarias en la base de datos, según lo definido en la carpeta database/migrations.

## 🌱 Paso 8 (Opcional): Poblar la base de datos con datos de prueba
```bash
php artisan db:seed
```
🔸 Solo si el proyecto tiene seeders definidos.

## 🎨 Paso 9 (Opcional): Instalar dependencias Front-End
Si el proyecto usa Laravel Mix o Vite para manejar CSS y JS:

```bash
npm install
```
Luego, para desarrollo:

```bash
npm run dev
```
O para producción:
```bash
npm run build
```

```bash
npm install && npm run dev
```
Esto **sí levanta un servidor de desarrollo** en otro puerto (como `http://localhost:5173`) que sirve tus archivos JS/CSS y los actualiza en vivo.
## 🌐 Paso 10: Levantar el servidor
Levanta el servidor de laravel
```bash
php artisan serve
```
📍 Por defecto estará disponible en:

```cpp
http://127.0.0.1:8000
```
📁 Acceso a carpeta de imágenes storage
Laravel guarda archivos subidos en storage/app/public, pero para acceder por web necesitas un enlace simbólico:

```bash
php artisan storage:link
```
🔗 Esto crea un enlace desde public/storage hacia storage/app/public

✅ Proyecto listo para trabajar
Ya puedes comenzar a explorar, programar y probar tu aplicación.

🧠 Notas adicionales
Para limpiar la caché (útil cuando se editan archivos .env o rutas):

```bash
php artisan config:clear
php artisan cache:clear
php artisan route:clear
php artisan view:clear
```
🗂️ Estructura de carpetas importantes

| Carpeta           | Contenido                                                 |
|-------------------|-----------------------------------------------------------|
| `app/`            | Lógica principal del sistema (modelos, controladores, etc)|
| `routes/`         | Definición de rutas web y API                             |
| `resources/views/`| Archivos Blade (HTML + PHP)                               |
| `database/`       | Migraciones, seeders y factories                          |
| `public/`         | Archivos visibles públicamente (CSS, JS, imágenes, etc)   |
| `storage/`        | Archivos subidos, logs, y caché                           |
