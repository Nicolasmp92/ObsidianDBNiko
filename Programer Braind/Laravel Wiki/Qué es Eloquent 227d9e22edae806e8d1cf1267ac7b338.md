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

## [👈🏻VOLVER](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)

## [SIGUIENTE 👉🏻](Modelos%20y%20relaciones%20227d9e22edae806687d4f254497f7294.md)