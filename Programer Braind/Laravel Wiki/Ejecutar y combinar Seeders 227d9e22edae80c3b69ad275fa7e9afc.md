# Ejecutar y combinar Seeders.

Titular: Niko

### ✅ **Cómo correr un Seeder**

Ejecuta **todos los seeders** registrados en `DatabaseSeeder.php`:

```bash

php artisan db:seed

```

Ejecuta **un Seeder específico**:

```bash

php artisan db:seed --class=UserSeeder

```

---

### ✅ **Combinar Factories y Seeders**

Normalmente **usas Factories dentro de Seeders** para poblar muchas filas con un solo comando.

Ejemplo:

```php

public function run(): void
{
    // Crear 50 usuarios usando la factory
    \\App\\Models\\User::factory(50)->create();
}

```

En `DatabaseSeeder.php` puedes combinar múltiples seeders:

```php

public function run(): void
{
    $this->call([
        UserSeeder::class,
        PostSeeder::class,
    ]);
}

```

---

### ✅ **Borrar y poblar de nuevo**

Si quieres **borrar todo y volver a sembrar** en limpio:

```bash

php artisan migrate:fresh --seed

```

Esto:

1️⃣ Elimina todas las tablas.

2️⃣ Ejecuta las migraciones de cero.

3️⃣ Corre los Seeders.

---

## 📌 **Tips Finales**

- ⚙️ **Seeders** = scripts que llenan datos → corren con `db:seed`.
- 🧑‍🌾 **Factories** = moldes → definen cómo generar datos random.
- 🗂️ Siempre combina ambos para poblar **varias tablas relacionadas**.
- 🧪 Usa **Tinker** para probar factories:
    
    ```php
    
    \\App\\Models\\User::factory()->create();
    
    ```
    

---

## [👈🏻VOLVER](Crear%20Seeders%20y%20Factories%20227d9e22edae8039af0dcedddb731d6e.md)

## [SIGUIENTE 👉🏻](Sin%20ti%CC%81tulo%20227d9e22edae80e8bd23c9c0d9a52c4e.md)