# Crear Seeders y Factories.

Titular: Niko

### **🫛Crear un Seeder**

```bash

php artisan make:seeder NombreSeeder

```

Esto genera un archivo en `database/seeders/`.

Dentro de la clase, defines **qué datos crear**.

Ejemplo simple:

```php
public function run(): void
{
    DB::table('users')->insert([
        'name' => 'Nye Tester',
        'email' => 'nye@example.com',
        'password' => bcrypt('password'),
    ]);
}

```

---

### ✅ **Crear una Factory**

```bash

php artisan make:factory NombreFactory --model=User

```

Esto genera un archivo en `database/factories/`.

Ejemplo básico de una Factory para `User`:

```php

public function definition(): array
{
    return [
        'name' => $this->faker->name(),
        'email' => $this->faker->unique()->safeEmail(),
        'password' => bcrypt('password'),
    ];
}

```

👉 Las Factories usan **Faker (recuerda ya lo tienes)**, una librería para generar datos falsos (nombres, mails, fechas) biene integrado en laravel .

---

## [👈🏻VOLVER](Seeders%20y%20Factories%20227d9e22edae805ab56cff080eb9fcdb.md)

## [SIGUIENTE 👉🏻](Ejecutar%20y%20combinar%20Seeders%20227d9e22edae80c3b69ad275fa7e9afc.md)