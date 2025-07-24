# Qué es Artisan

Titular: Niko

## 🤖 **Artisan CLI**

**Artisan** es la **interfaz de línea de comandos de Laravel**. Es una herramienta súper poderosa para automatizar tareas comunes del framework sin tener que hacerlas manualmente.

Con Artisan puedes:

✅ Crear controladores, modelos, migraciones, seeders y factories.

✅ Ejecutar migraciones y rollback.

✅ Limpiar caché de configuración y rutas.

✅ Levantar el servidor local (`serve`).

✅ Ejecutar comandos personalizados que tú mismo crees.

---

### 📌 **Comandos más usados**

Algunos comandos que usarás casi todos los días:

```bash

php artisan serve

```

Inicia el servidor local en `http://127.0.0.1:8000`.

```bash

php artisan make:controller NombreController

```

Crea un nuevo **Controlador**.

```bash

php artisan make:model NombreModelo

```

Crea un **Modelo Eloquent**.

```bash

php artisan make:migration create_tabla --create=tabla

```

Crea una **Migración**.

```bash

php artisan migrate

```

Ejecuta todas las migraciones pendientes.

```bash

php artisan migrate:rollback

```

Revierte la última migración.

```bash

php artisan db:seed

```

Ejecuta los **Seeders**.

```bash

php artisan route:list

```

Muestra todas las rutas definidas.

```bash

php artisan config:cache

```

Regenera la caché de configuración.

---

### ✅ **Cheatsheet rápido**

- **make:** genera cosas nuevas (`controller`, `model`, `migration`, `seeder`...)
- **migrate:** controla la base de datos
- **db:seed:** pobla la base de datos
- **route:list:** revisa rutas
- **config:cache:** limpia y vuelve a cachear configuración

---

💡 **Tip:** Para ver **todos los comandos disponibles**, solo escribe:

```bash

php artisan list

```

---

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Comandos%20más%20usados.md)