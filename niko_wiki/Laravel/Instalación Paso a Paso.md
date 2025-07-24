# Instalación Paso a Paso

Titular: Niko

<aside>
💡

Laravel se instala usando **Composer**, el gestor de dependencias de PHP. Aquí tienes el paso a paso para crear tu primer proyecto:

</aside>

---

## 📦 1. Verifica PHP y Composer

Abre tu terminal o consola y ejecuta estos comandos para asegurarte de tener **PHP** y **Composer** listos:

```bash
php -v
```

**Ejemplo de salida:**

```bash

PHP 8.2.12 (cli) (built: Oct 31 2023 15:12:23) (ZTS Visual C++ 2019 x64)

```

```bash
composer -v

```

**Ejemplo de salida:**

```bash

Composer version 2.7.2 2024-04-05 11:15:05

```

Si ves algo similar, significa que **PHP y Composer están funcionando bien** y puedes continuar.

🚩 **Si no, sigue leyendo:**

👌[Si lo tienes, Clic acá.](Instalación%20Paso%20a%20Paso.md)

---

## 🧩 2. ¿No tienes PHP ni Composer?

Si al correr los comandos dice *“php no se reconoce como un comando interno…”* o algo parecido, significa que **no están instalados** o no están en el **PATH**.

---

### 📥 **Cómo instalar PHP**

👉 Lo más fácil es instalar un **servidor local** como **XAMPP**, **MAMP** o **Laragon**, porque traen PHP incluido.

- **XAMPP:** https://www.apachefriends.org/es/index.html
- **Laragon (muy recomendado para Windows):** [https://laragon.org/](https://laragon.org/)

Cuando instalas uno de estos, **ya tienes PHP listo, [puedes Verificar ☝️ .](Instalación%20Paso%20a%20Paso.md)**

---

### 📥 **Cómo instalar Composer**

Una vez tengas PHP funcionando, descarga Composer:

- **Composer:** [https://getcomposer.org/](https://getcomposer.org/)
- 

Sigue el instalador paso a paso. Normalmente **Composer detecta PHP automáticamente**. Si no lo hace, tendrás que indicarle la ruta del archivo `php.exe` (en XAMPP suele estar en `C:\xampp\php\php.exe`).

---

✅ **Tip extra:**

Después de instalar, cierra y abre de nuevo la terminal. A veces necesita actualizar las variables de entorno para reconocer `php` y `composer`.

---

## 📂 3. Crea tu proyecto Laravel

Para crear un proyecto nuevo, navega a la carpeta donde quieres guardarlo (por ejemplo, dentro de tu servidor local `htdocs` o `www`).

```bash

cd ruta/donde/quieres/tu/proyecto

```

Ahora ejecuta este comando:

```bash

composer create-project laravel/laravel nombre_del_proyecto

```

Reemplaza `nombre_del_proyecto` por el nombre de tu app (ejemplo: `BeanFlow_coffee`).

---

## ⚙️ 4. Ingresa a la carpeta del proyecto

```bash

cd nombre_del_proyecto

```

---

## 🚀 5. Levanta el servidor de desarrollo

Laravel trae un servidor local integrado. Para usarlo, ejecuta:

```bash

php artisan serve

```

Si todo está bien, verás algo como:

```bash

Starting Laravel development server: http://127.0.0.1:8000

```

Abre ese enlace en tu navegador para ver tu proyecto funcionando.

---

## ✅ 6. Configura `.env`

Laravel crea automáticamente el archivo `.env`. Ahí defines la conexión a la base de datos, nombre del proyecto, puerto, etc.

Ejemplo de configuración básica para MySQL:

```bash

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nombre_de_la_bd
DB_USERNAME=root
DB_PASSWORD=

```

Asegúrate de crear la base de datos en **phpMyAdmin** antes de correr migraciones.

---

## ⚡ Tip

Si usas **XAMPP** o **Laragon**, asegúrate de que **Apache** y **MySQL** estén activos.

---

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Estructura%20de%20carpetas.md)