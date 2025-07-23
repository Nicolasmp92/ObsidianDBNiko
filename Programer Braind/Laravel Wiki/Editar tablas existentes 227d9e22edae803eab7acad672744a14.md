# Editar tablas existentes

Titular: Niko

Cuando necesites **agregar, cambiar o eliminar columnas**, **no uses phpMyAdmin directo**. Laravel usa **migraciones** para dejar todo **documentado y versionado**.

---

### 📌 **Ejemplo — Agregar columna**

```bash

php artisan make:migration add_prueba_column_to_ejemplo_tables --table="ejemplo"

```

En el archivo generado, editas `up()`:

```php

public function up(): void
{
    Schema::table('ejemplo', function (Blueprint $table) {
        $table->string('prueba')->nullable();
    });
}

public function down(): void
{
    Schema::table('ejemplo', function (Blueprint $table) {
        $table->dropColumn('prueba');
    });
}
```

---

### 

---

## [👈🏻VOLVER](Crear%20y%20ejecutar%20migraciones%20227d9e22edae80129ef5e9f11d2e8757.md)

## [SIGUIENTE 👉🏻](Usar%20Tinker%20para%20pruebas%20227d9e22edae8068a232f4b8b6e3549d.md)