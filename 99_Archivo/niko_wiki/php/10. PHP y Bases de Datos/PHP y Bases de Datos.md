# 📘 Wiki PHP – Capítulo 10: PHP y Bases de Datos

## 10.1 🔹 Conexión a MySQL

En PHP tenemos dos formas principales:

- **MySQLi** (mejorado, estilo procedural u orientado a objetos).
    
- **PDO (PHP Data Objects)** → más moderno y flexible (recomendado).
    

---

## 10.2 🔹 Conexión con MySQLi

### Estilo Orientado a Objetos

`<?php $conexion = new mysqli("localhost", "root", "", "mi_base");  if ($conexion->connect_error) {     die("Error de conexión: " . $conexion->connect_error); }  echo "Conexión exitosa!"; ?>`

### Estilo Procedural

`<?php $conexion = mysqli_connect("localhost", "root", "", "mi_base");  if (!$conexion) {     die("Error: " . mysqli_connect_error()); }  echo "Conexión OK"; ?>`

---

## 10.3 🔹 Conexión con PDO (Recomendado)

`<?php try {     $conexion = new PDO("mysql:host=localhost;dbname=mi_base", "root", "");     $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);     echo "Conexión exitosa con PDO!"; } catch (PDOException $e) {     echo "Error: " . $e->getMessage(); } ?>`

📌 Ventaja → PDO funciona con **muchos motores de BD** (MySQL, PostgreSQL, SQLite, etc.).

---

## 10.4 🔹 Consultas Básicas (SELECT)

### MySQLi

`$resultado = $conexion->query("SELECT * FROM usuarios");  while ($fila = $resultado->fetch_assoc()) {     echo $fila["nombre"] . "<br>"; }`

### PDO

`$stmt = $conexion->query("SELECT * FROM usuarios");  while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {     echo $fila["nombre"] . "<br>"; }`

---

## 10.5 🔹 Insertar Datos

### MySQLi

`$sql = "INSERT INTO usuarios (nombre, email) VALUES ('Nye', 'nye@mail.com')"; if ($conexion->query($sql)) {     echo "Usuario agregado"; }`

### PDO

`$stmt = $conexion->prepare("INSERT INTO usuarios (nombre, email) VALUES (:nombre, :email)"); $stmt->execute([     ":nombre" => "Nye",     ":email" => "nye@mail.com" ]); echo "Usuario agregado con PDO";`

---

## 10.6 🔹 Update y Delete

### PDO

`// Update $stmt = $conexion->prepare("UPDATE usuarios SET email = :email WHERE id = :id"); $stmt->execute([":email" => "nuevo@mail.com", ":id" => 1]);  // Delete $stmt = $conexion->prepare("DELETE FROM usuarios WHERE id = :id"); $stmt->execute([":id" => 1]);`

---

## 10.7 🔹 Sentencias Preparadas (Prepared Statements)

Evitan **SQL Injection** (ataques con consultas manipuladas).

👉 Ejemplo inseguro (NO hacerlo):

`$sql = "SELECT * FROM usuarios WHERE email = '" . $_POST["email"] . "'";`

👉 Ejemplo seguro con PDO:

`$stmt = $conexion->prepare("SELECT * FROM usuarios WHERE email = :email"); $stmt->execute([":email" => $_POST["email"]]); $usuario = $stmt->fetch(PDO::FETCH_ASSOC);`

📌 Esto es la base de cómo Laravel protege las consultas con Eloquent.

---

## 10.8 🔹 Fetch Modes en PDO

- `PDO::FETCH_ASSOC` → array asociativo.
    
- `PDO::FETCH_OBJ` → objeto.
    
- `PDO::FETCH_BOTH` → array asociativo + numérico.
    

`$stmt = $conexion->query("SELECT * FROM usuarios"); $usuario = $stmt->fetch(PDO::FETCH_OBJ); echo $usuario->nombre;`

---

## 10.9 🔹 Transacciones (PDO)

Sirven para ejecutar varias consultas como **una sola operación**.  
Si algo falla, se revierte todo.

`try {     $conexion->beginTransaction();      $conexion->exec("INSERT INTO cuentas (usuario, saldo) VALUES ('Nye', 1000)");     $conexion->exec("UPDATE cuentas SET saldo = saldo - 500 WHERE usuario = 'Nye'");      $conexion->commit(); // Confirma cambios } catch (Exception $e) {     $conexion->rollBack(); // Revierte cambios     echo "Error: " . $e->getMessage(); }`

---

## 10.10 🔹 Ejemplo Integrador

Archivo: `usuarios.php`

`<?php try {     $conexion = new PDO("mysql:host=localhost;dbname=mi_base", "root", "");     $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);      $stmt = $conexion->prepare("SELECT * FROM usuarios WHERE edad >= :edad");     $stmt->execute([":edad" => 18]);      foreach ($stmt as $fila) {         echo $fila["nombre"] . " - " . $fila["email"] . "<br>";     }  } catch (PDOException $e) {     echo "Error: " . $e->getMessage(); } ?>`

---

## ✅ Resumen del Capítulo 10

- **MySQLi** → conexión y consultas simples.
    
- **PDO** → más seguro y multiplataforma (recomendado).
    
- **Consultas básicas** → `SELECT, INSERT, UPDATE, DELETE`.
    
- **Prepared Statements** → protegen de SQL Injection.
    
- **Transacciones** → aseguran consistencia de datos.
    

---

📌 Con este capítulo ya sabes cómo **PHP maneja bases de datos**, la base sobre la que Laravel construye **Eloquent ORM**.  
En Laravel, en vez de `PDO` o `mysqli`, usas cosas como:

`User::where("edad", ">=", 18)->get();`

pero internamente sigue siendo SQL.

👉 Próximo paso → **Capítulo 11: Temas Avanzados (funcional, Composer, PSR, buenas prácticas)**, donde ya llevamos PHP a nivel profesional.

---

**Anterior:** [[Manejo de Archivos]] | **Siguiente:** [[php Temas Avanzados]]