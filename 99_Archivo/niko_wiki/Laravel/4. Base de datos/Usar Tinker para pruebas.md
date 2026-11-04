# Usar Tinker para pruebas

Titular: Niko

**Tinker** es una consola **interactiva** que te permite **ejecutar código PHP y consultas Eloquent** **directamente**, sin crear rutas, controladores ni vistas.

---

### 📌 **Cómo abrir Tinker**

```bash

php artisan tinker

```

Ejemplo de comandos dentro de Tinker:

```php

User::all(); // Ver todos los usuarios
User::find(1); // Buscar usuario con ID 1
User::create([
  'name' => 'Nye',
  'email' => 'nye@example.com',
  'password' => bcrypt('123456'),
]); // Crear usuario

```

---

### 📌 **¿Qué es Eloquent?**

👉 **Eloquent** es el **ORM de Laravel** (Object Relational Mapper).

En palabras simples: **te permite trabajar con tablas de la base de datos como si fueran objetos PHP**.

✅ Ejemplo:

- `User::all()` → Trae todos los registros de la tabla `users`.
- `Post::create([...])` → Crea un nuevo post.

Así **no escribes SQL a mano** → Laravel lo hace por ti.

👉 Si quieres aprender Eloquent a fondo, ve [aquí el tema completo de **Eloquent** ➜](Qué%20es%20Eloquent.md) 

---

### 📌 **Para qué sirve Tinker**

- Probar **consultas Eloquent** sin armar controladores.
- Crear registros de prueba rápido.
- Revisar relaciones: `User::find(1)->posts`.

---

✅ **Tip:**

Si algo falla, **Tinker muestra el error al instante** → Ideal para testear **factories**, **modelos**, **relaciones** y seeds, **sin dañar tu proyecto real**.

---

## ✅ **Resumen — Buenas prácticas**

✔️ Configura bien tu `.env`.

✔️ Crea bases en phpMyAdmin **antes** de migrar.

✔️ Usa **migraciones** para cambiar estructura → **no toques phpMyAdmin directo**.

✔️ Prueba tus consultas con **Tinker** para no romper nada en producción.

---

## [👈🏻VOLVER](Editar%20tablas%20existentes.md)

## [SIGUIENTE 👉🏻](Seeders%20y%20Factories.md)