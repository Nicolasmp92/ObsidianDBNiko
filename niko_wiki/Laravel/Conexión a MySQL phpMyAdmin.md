# Conexión a MySQL/phpMyAdmin

Titular: Niko

Laravel se conecta a tu base de datos **leyendo los datos del archivo `.env`**.

Aquí defines **qué motor usas**, **dónde está tu servidor**, **qué usuario y contraseña usa**, y **qué base de datos va a modificar**.

Ejemplo típico de configuración `.env` para MySQL con **XAMPP**, **Laragon** o similar:

```

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nombre_de_tu_bd
DB_USERNAME=root
DB_PASSWORD=

```

---

✅ **¿Qué hace cada línea?**

- `DB_CONNECTION` — El tipo de base de datos. Normalmente `mysql`.
- `DB_HOST` — La dirección del servidor. Local casi siempre es `127.0.0.1`.
- `DB_PORT` — Puerto de MySQL, por defecto `3306`.
- `DB_DATABASE` — El **nombre de tu base de datos** (debes crearla antes).
- `DB_USERNAME` — Usuario con permisos. Localmente suele ser `root`.
- `DB_PASSWORD` — Contraseña del usuario (en XAMPP suele estar vacía).

---

## ✅ **Tip Importante**

Laravel **no crea la base de datos vacía** como tal.

Tú debes **crear primero la base vacía** en **phpMyAdmin** (o con otro gestor, como MySQL Workbench).

---

### 📌 **Ejemplo paso a paso**

1️⃣ Abre **phpMyAdmin**

2️⃣ Ve a **Bases de Datos**

3️⃣ Escribe el nombre (ejemplo: `nuevabase_datos`)

4️⃣ Haz clic en **Crear**

Con eso tienes **la base lista**, vacía.

Cuando ejecutes:

```bash

php artisan migrate

```

Laravel **crea todas las tablas adentro**, usando las migraciones que tengas.

---

## ✅ **Prueba tu conexión**

Si al correr `php artisan migrate` aparece el error:

```php

SQLSTATE[HY000] [1049] Unknown database 'nuevabase_datossss'
//Ojo aca esta mal escrito (por eso el error)☝🏻
```

significa que **MySQL no encuentra la base**.

Verifica:

- 📌 **Nombre exacto** en `.env`:
    
    ```php
    
    DB_DATABASE=nuevabase_datos
    
    ```
    
- 📌 **Que la base exista** en phpMyAdmin.
    
    **Dato real:** A veces, en **XAMPP** (con MySQL sin clave root), puede **crear la base automáticamente** si tienes permisos amplios — *pero no es seguro ni recomendado depender de eso.*
    
- 📌 **Que el usuario tenga permisos:**
    
    Por defecto `root` en XAMPP no tiene clave (`DB_USERNAME=root` y `DB_PASSWORD=`).
    
    Si usas otro usuario, asegúrate de darle permisos de **CREAR** y **MODIFICAR**.
    

---

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Crear%20y%20ejecutar%20migraciones.md)