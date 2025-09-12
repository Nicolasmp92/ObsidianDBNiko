#  Archivo .env y Configuración

Titular: Niko

El archivo `.env` es clave en Laravel: guarda **todas las variables de entorno** que definen cómo se comporta tu aplicación. Aquí configuras la conexión a la base de datos, la clave de la app (`APP_KEY`), el entorno (`APP_ENV`) y otras credenciales.

Ejemplo de `.env` básico:

```
APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:xxxxxxxxx
APP_DEBUG=true
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nombre_de_la_bd
DB_USERNAME=root
DB_PASSWORD=

```

Cuando cambias algo en `.env`, ejecuta `php artisan config:cache` para que Laravel actualice la configuración. **Nunca subas `.env` a Git**, porque guarda datos sensibles.

El archivo `.env` tiene **credenciales privadas**:

- Usuario y clave de la base de datos
- Claves API
- Secretos de sesión

Si lo subes a Git, **cualquiera que vea el repositorio puede robar esos datos**.

---

## ✅ **Solución: Ignorar `.env`**

Git usa un archivo llamado **`.gitignore`** para saber **qué archivos NO subir nunca**.

---

### 📂 **1️⃣ Abre tu `.gitignore`**

Laravel ya trae uno por defecto, está en la raíz del proyecto.

Ábrelo y revisa que tenga una línea así:

```bash

.env

```

Eso le dice a Git: **“Ignora cualquier archivo llamado `.env`”**.

---

### ⚙️ **2️⃣ Si ya lo subiste sin querer**

Si `.env` **ya está en Git**, hay que decirle a Git que **deje de rastrearlo**:

```bash

git rm --cached .env

```

- `-cached` le dice a Git: **“Elimínalo del repositorio remoto pero déjalo en tu carpeta local.”**

Después **confirma** el cambio:

```bash

git commit -m "Remove .env from tracking"
git push

```

Así desaparece del repositorio.

---

### 📌 **3️⃣ Deja una plantilla**

Crea un archivo llamado **`.env.example`** con los mismos campos, **pero sin claves reales**:

```
env
CopiarEditar
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
DB_HOST=127.0.0.1
DB_DATABASE=example_db
DB_USERNAME=root
DB_PASSWORD=

```

Así, tus compañeros pueden copiarlo:

```bash

cp .env.example .env

```

---

## 🗂️ **Resumen clave**

✅ Pon `.env` en `.gitignore`.

✅ Si ya se subió: `git rm --cached .env`.

✅ Usa `.env.example` como plantilla limpia.

✅ Ejecuta `php artisan config:cache` cuando cambies variables importantes.

---

## [👈🏻VOLVER](Estructura%20de%20carpetas.md)

## [SIGUIENTE 👉🏻](Qué%20es%20Artisan.md)