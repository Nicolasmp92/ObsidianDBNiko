# Crear y ejecutar migraciones

Titular: Niko

## 🦜 **¿Qué es una migración?**

Las **migraciones** son **archivos PHP** que describen **qué tablas debe tener tu base de datos** y cómo se estructuran (columnas, índices, llaves foráneas, etc.).

🔑 Es **un archivo especial en Laravel** que dice **cómo debe crearse una tabla** o **cómo debe cambiarse**.

Es como **un “instructivo” paso a paso** para que Laravel sepa:

- Qué tabla crear (ejemplo: `users`)
- Qué columnas tendrá (ejemplo: `name`, `email`, `password`)
- Qué tipo de dato es cada columna (texto, número, fecha…)

👉 Laravel lee estas migraciones y las aplica **usando Artisan** [[Qué es Artisan|¿que es artisan?]].

---

## 🧱 **¿Para qué sirven?**

✅ **Organiza cambios:**

Si mañana quieres **agregar una columna nueva** o **cambiar algo**, **no editas directo en phpMyAdmin**  (en SQL), sino que creas otra migración.

✅ **Deja historial:**

Cada migración queda **guardada**. Así puedes saber **cuándo y por qué se creó o cambió algo**.

✅ **Facilita trabajo en equipo:**

Todos los programadores ejecutan la misma migración y tienen **la misma base de datos**, sin errores.

---

## ⚙️ **Cómo crear una migración**

```bash

php artisan make:migration create_posts_table --create=posts

```

Esto crea un archivo en `database/migrations/` con dos métodos:

- `up()`: lo que ocurre al aplicar la migración (crear o modificar).
- `down()`: lo que ocurre al revertirla (rollback).

---

## 🧩 **Ejemplo real**

```php
public function up(): void
{
    Schema::create('posts', function (Blueprint $table) {
        $table->id(); // 🔑 ID autoincremental.
        $table->string('title'); // 📌 Texto corto (máx 255).
        $table->text('content'); // 📜 Texto largo.
        $table->integer('views'); // 🔢 Número entero.
        $table->boolean('published')->default(false); // ✅ True/false.
        $table->date('published_at')->nullable(); // 📅 Fecha (puede ser nulo).
        $table->dateTime('reviewed_at')->nullable(); // ⏰ Fecha y hora.
        $table->float('rating', 8, 2)->nullable(); // 📏 Decimal simple.
        $table->decimal('price', 8, 2)->nullable(); // 💲 Decimal para dinero.
        $table->enum('status', ['draft', 'published', 'archived']); // 🎚️ Opciones limitadas.
        $table->json('metadata')->nullable(); // 🗂️ JSON.
        $table->binary('file')->nullable(); // 🗄️ Binario.
        $table->uuid('uuid'); // 🔐 UUID.
        $table->foreignId('user_id')->constrained(); // 🔗 FK a 'users'.
        $table->timestamps(); // 🕒 created_at & updated_at.
        $table->softDeletes(); // 🗑️ deleted_at.
        $table->rememberToken(); // 🔑 Token de sesión.
    });
}

public function down(): void
{
    Schema::dropIfExists('posts'); // 🚫 Borra tabla si existe.
}

```

---

## 🔄 **¿Cómo se ejecutan?**

- `php artisan migrate` — Ejecuta migraciones pendientes.
- `php artisan migrate:rollback` — Revierte la última tanda.
- `php artisan migrate:refresh` — Revierte **todo** y vuelve a migrar.
- `php artisan migrate:fresh` — Borra **todo** y migra desde cero.
- `php artisan migrate:status` — Ver qué migraciones se han corrido.
- |`php artisan migrate:reset` — Revierte **todas las migraciones**, pero **no vuelve a ejecutarlas**


---

## 🔑 **Tips reales**

✅ **Siempre revisa [`.env`](Instalación%20Paso%20a%20Paso.md)** antes de migrar — asegúrate de estar conectado a la **base de datos correcta**.

✅ Si haces **muchos cambios chiquitos**, agrúpalos: no generes mil migraciones por cada columna.

✅ Para cambios **más complejos** (renombrar columnas o cambiar tipo de dato) instala `doctrine/dbal`:

```bash

composer require doctrine/dbal

```

---

## 🔍 **¿Qué es `doctrine/dbal`?**

📦 `doctrine/dbal` es **un paquete extra de PHP** que Laravel **usa internamente** para poder hacer **operaciones más complejas** en la base de datos.

✅ **DBAL** significa **DataBase Abstraction Layer**, en español: **“Capa de Abstracción de Base de Datos”**.

En palabras simples: es como un **traductor** que **se comunica con distintos tipos de bases de datos** (MySQL, PostgreSQL, SQLite...) de forma **estándar y segura**.

---

## 🧩 **¿Por qué lo necesito?**

Laravel por defecto **NO puede hacer todo** con su propio motor de migraciones.

👉 Por ejemplo:

- **Renombrar una columna** (`renameColumn`)
- **Cambiar el tipo de dato** de una columna (`change`)

Estas operaciones **necesitan que Laravel entienda bien la estructura de tu base de datos**, y para eso usa **DBAL** como ayuda.

---

## ⚙️ **¿Cómo se instala?**

Muy fácil, se instala con Composer:

```bash

composer require doctrine/dbal

```

Después de eso, Laravel **ya puede entender y ejecutar migraciones más avanzadas** como:

```php

Schema::table('posts', function (Blueprint $table) {
    $table->renameColumn('old_name', 'new_name');
    $table->string('title', 500)->change();
});

```

Sin `doctrine/dbal`, estas instrucciones **lanzan error**.

---

## ✅ **En resumen**

- **`doctrine/dbal`** es **un ayudante** para Laravel.
- Lo necesitas **sólo cuando haces cosas avanzadas** con migraciones.
- Lo instalas una sola vez y queda listo.

## 🎉 **Resumen**

👉 Una migración = **“instrucción guardada”** de tu base de datos.

👉 Se ejecuta con `php artisan migrate`.

👉 Te permite mantener **orden, control y trabajo en equipo**.

---

## [👈🏻VOLVER](Conexión%20a%20MySQL%20phpMyAdmin.md)

## [SIGUIENTE 👉🏻](Editar%20tablas%20existentes.md)