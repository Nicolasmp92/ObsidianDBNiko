# Qué es Eloquent

Titular: Niko

## **1️⃣ Qué es Eloquent**

**Eloquent** es el **ORM oficial de Laravel**: un **mapeador objeto-relacional**.

👉 Traducido: Eloquent convierte cada **tabla** de tu base de datos en una **clase PHP**, y cada **fila** en una **instancia de esa clase**.

✅ Ventajas:

- Escribes **poco SQL manual** → consultas legibles.
- Relaciona tablas como **objetos PHP**.
- Facilita migraciones y relaciones sin complicarte.

---

### 📌 **Ejemplo mínimo**

**Tabla:** `users`

**Modelo:** `User`

```php

use App\\Models\\User;

$user = User::find(1);
echo $user->name;

```

En lugar de escribir `SELECT * FROM users WHERE id = 1`, usas `User::find(1)`.

---

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Modelos%20y%20relaciones.md)