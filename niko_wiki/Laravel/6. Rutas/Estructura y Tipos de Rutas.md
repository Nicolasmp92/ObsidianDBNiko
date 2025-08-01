#Estructura y Tipos de Rutas

Titular: Niko

# Estructura y Tipos de Rutas

---

## **¿Qué es una ruta en Laravel?**

Imagina que tu aplicación web es una **casa gigante** con **muchas puertas**

- Una **ruta** es la **dirección** que usas para abrir una **puerta específica**.
- Cada **URL** (ej: `/`, `/usuarios`, `/posts/5`) se conecta con un **código PHP** que dice: **¿Qué hago cuando alguien entra por aquí?**

---

### 🔑 **¿Qué hace una ruta?**

**👉 Toma la URL → Ejecuta código → Devuelve algo al navegador.**

Por ejemplo:

```
Route::get('/', function () {
    return 'Hola mundo!';
});
```

✔️ Cuando alguien entra a `http://tusitio.com/`

Laravel corre ese `function` y devuelve **“Hola mundo!”**.

---

## ✅ **📍 Partes de una ruta**

Miremos una ruta **desarmada**:

```
Route::get('/usuarios', [UserController::class, 'index'])->name('usuarios.index');
```

---

### 📌 **1️⃣ Método HTTP**

- `get` → Dice **qué tipo de acción es**.
    - `GET` = Mostrar datos.
    - `POST` = Enviar datos (crear algo).
    - `PUT` o `PATCH` = Actualizar algo.
    - `DELETE` = Borrar algo.

```
Route::get(...)
Route::post(...)
```

---

### 📌 **2️⃣ URL**

- `'/usuarios'` → Es la **ruta física** que se pone en el navegador.
- Ejemplo: `http://tusitio.com/usuarios`

---

### 📌 **3️⃣ Acción**

- `[UserController::class, 'index']`
    
    👉 Dice **qué archivo y qué función PHP ejecutar**.
    
    - `UserController` → Clase donde está la lógica.
    - `index` → Método dentro de esa clase.
    
    ✅ Esto reemplaza un `return view(...)` desde el controlador.
    

---

### 📌 **4️⃣ Nombre interno (`name`)**

- `>name('usuarios.index')` → Crea un **alias** para usar en enlaces.
- Así puedes escribir:
    
    ```
    <a href="{{ route('usuarios.index') }}">Usuarios</a>
    ```
    
    En vez de poner la URL a mano.
    

---

## ✅ **📍 ¿Dónde se escriben?**

Laravel organiza rutas en archivos:

| Archivo | Para qué sirve |
| --- | --- |
| `web.php` | Rutas **web**, con vistas Blade, sesiones, cookies. |
| `api.php` | Rutas **API REST**, devuelven JSON, sin sesiones. |

---

## ✅ **📍 Ejemplo real en `web.php`**

```
Route::get('/', function () {
    return view('welcome');
});
```

- **`/`** → URL raíz.
- `view('welcome')` → Muestra el archivo `resources/views/welcome.blade.php`.

---

## ✅ **📍 Mostrar una vista SIN controlador**

Cuando no necesitas lógica, puedes usar:

```
Route::view('/acerca', 'info.acerca')->name('info.acerca');
```

Laravel busca la vista en:

```
resources/views/info/acerca.blade.php
```

- Cada `.` representa una carpeta.
- `info.acerca` se traduce como `info/acerca.blade.php` dentro de la carpeta `views`.

✅ Esto reemplaza totalmente a usar un controlador que hace `return view('info.acerca');`

---

## ✅ **📍 Agrupar rutas con `prefix`**

Si tienes **varias rutas parecidas**, Laravel deja **agruparlas**.

Ejemplo:

```
Route::prefix('usuarios')->group(function () {
    Route::get('/', function () {
        return 'Lista de usuarios';
    });

    Route::get('/crear', function () {
        return 'Crear usuario';
    });
});
```

👉 Esto crea:

- `/usuarios`
- `/usuarios/crear`

---

## ✅ **📍 Prefijo de nombre (`as`)**

Para no escribir todos los nombres uno por uno:

```
Route::prefix('usuarios')->as('usuarios.')->group(function () {
    Route::get('/', function () {
        return 'Lista de usuarios';
    })->name('index');

    Route::get('/crear', function () {
        return 'Crear usuario';
    })->name('crear');
});
```

Esto arma:

- Ruta `/usuarios` → nombre `usuarios.index`
- Ruta `/usuarios/crear` → nombre `usuarios.crear`

---

## ✅ **📍 CRUD rápido con `Route::resource()`**

Laravel tiene un **atajo** para crear todas las rutas necesarias de un CRUD (Crear, Leer, Editar, Borrar) de golpe:

```
Route::resource('posts', PostController::class);
```

Esto hace **7 rutas**:

- `/posts` (index)
- `/posts/create` (create)
- `/posts` (store)
- `/posts/{id}` (show)
- `/posts/{id}/edit` (edit)
- `/posts/{id}` (update)
- `/posts/{id}` (destroy)

---

## 🏑 **✅ Resumen simple**

✔️ **Una ruta = una puerta**

✔️ **URL = dirección de la puerta**

✔️ **Método (`GET`, `POST`...) = tipo de acción**

✔️ **Controlador = quién abre la puerta y decide qué devolver**

✔️ **`name()` = apodo para llamar la puerta sin escribir la dirección a mano**

## [👈🏻VOLVER](Laravel%20index.md)

## [SIGUIENTE 👉🏻](Parámetros%20y%20Nombres.md)