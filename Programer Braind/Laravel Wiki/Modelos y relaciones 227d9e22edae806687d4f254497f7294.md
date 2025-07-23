# Modelos y relaciones

Titular: Niko

## 🧩 **2️⃣ Modelos y Relaciones**

---

### ✅ **Crear un Modelo**

```bash

php artisan make:model Post

```

Esto crea:

```

app/Models/Post.php

```

---

### 📌 **Ejemplo de modelo con fillable**

```php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Model;

class Post extends Model
{
    protected $fillable = ['title', 'body'];
}

```

**`$fillable`** define qué columnas se pueden asignar en masa.

---

### ✅ **Relaciones entre modelos**

Laravel tiene métodos claros para representar relaciones de base de datos:

---

### 📌 **1:1 — Uno a uno**

**Ejemplo:** Un `User` tiene un `Profile`.

```php

// User.php
public function profile()
{
    return $this->hasOne(Profile::class);
}

// Profile.php
public function user()
{
    return $this->belongsTo(User::class);
}

```

Usar:

```php

$user = User::find(1);
echo $user->profile->bio;

```

---

### 📌 **1:N — Uno a muchos**

**Ejemplo:** Un `Post` tiene muchos `Comment`.

```php

// Post.php
public function comments()
{
    return $this->hasMany(Comment::class);
}

// Comment.php
public function post()
{
    return $this->belongsTo(Post::class);
}

```

Usar:

```php

$post = Post::find(1);
foreach ($post->comments as $comment) {
    echo $comment->body;
}

```

---

### 📌 **N:M — Muchos a muchos**

**Ejemplo:** `User` y `Role`.

```php

// User.php
public function roles()
{
    return $this->belongsToMany(Role::class);
}

// Role.php
public function users()
{
    return $this->belongsToMany(User::class);
}

```

Usar:

```php

$user = User::find(1);
foreach ($user->roles as $role) {
    echo $role->name;
}

```

Laravel maneja la tabla pivote automáticamente (`role_user`).

---

### 📌 **Relaciones avanzadas**

✅ **hasManyThrough:** Por ejemplo, `Country` tiene muchos `Post` a través de `User`.

✅ **Polymorphic:** Una `Photo` puede pertenecer a `User` **o** `Post`.

```php

// Photo.php
public function imageable()
{
    return $this->morphTo();
}

// User.php
public function photos()
{
    return $this->morphMany(Photo::class, 'imageable');
}

// Post.php
public function photos()
{
    return $this->morphMany(Photo::class, 'imageable');
}

```

---

## [👈🏻VOLVER](Que%CC%81%20es%20Eloquent%20227d9e22edae806e8d1cf1267ac7b338.md)

## [SIGUIENTE 👉🏻](Consultas%20ba%CC%81sicas%20y%20avanzadas%20227d9e22edae8088bb66d7ec15a330d9.md)