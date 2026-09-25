# 📘 Wiki PHP – Capítulo 8: Superglobales y Formularios

## 8.1 🔹 ¿Qué son las Superglobales?

Son **variables especiales** que PHP crea automáticamente y están disponibles en todo el programa (no necesitas declararlas).

Principales:

- `$_GET` → Datos enviados por URL.
    
- `$_POST` → Datos enviados por formularios.
    
- `$_REQUEST` → Combina GET y POST.
    
- `$_SESSION` → Datos temporales por usuario.
    
- `$_COOKIE` → Datos almacenados en el navegador.
    
- `$_FILES` → Archivos subidos.
    
- `$_SERVER` → Información del servidor y petición.
    

---

## 8.2 🔹 Formularios en PHP

Un formulario en HTML manda datos a un archivo PHP.

👉 Ejemplo básico:

`<form method="POST" action="procesar.php">     <input type="text" name="nombre" placeholder="Tu nombre">     <input type="number" name="edad" placeholder="Edad">     <button type="submit">Enviar</button> </form>`

👉 En `procesar.php`:

`<?php $nombre = $_POST["nombre"]; $edad = $_POST["edad"];  echo "Hola $nombre, tienes $edad años."; ?>`

---

## 8.3 🔹 $_GET (Datos por URL)

Se usan cuando el formulario tiene `method="GET"` o cuando pasamos datos en la URL.

👉 Ejemplo:

`https://miweb.com/procesar.php?nombre=Nye&edad=33`

👉 Código en `procesar.php`:

`<?php echo $_GET["nombre"]; // Nye echo $_GET["edad"];   // 33 ?>`

📌 GET es visible en la URL → no se debe usar para datos sensibles (ej. contraseñas).

---

## 8.4 🔹 $_POST (Datos de formulario)

Se usa con `method="POST"`.  
Los datos **no aparecen en la URL** y son más seguros.

`<?php if ($_SERVER["REQUEST_METHOD"] == "POST") {     $nombre = $_POST["nombre"];     echo "Hola $nombre!"; } ?>`

---

## 8.5 🔹 $_REQUEST

Mezcla `$_GET` y `$_POST`.  
No es tan recomendable porque no diferencia el origen.

`<?php $nombre = $_REQUEST["nombre"];`

---

## 8.6 🔹 $_FILES (Subida de archivos)

Cuando un formulario incluye `enctype="multipart/form-data"`, podemos subir archivos.

👉 Formulario:

`<form method="POST" action="subir.php" enctype="multipart/form-data">     <input type="file" name="archivo">     <button type="submit">Subir</button> </form>`

👉 PHP:

`<?php $archivo = $_FILES["archivo"]["name"]; $tmp = $_FILES["archivo"]["tmp_name"];  move_uploaded_file($tmp, "uploads/" . $archivo);  echo "Archivo subido con éxito"; ?>`

---

## 8.7 🔹 $_SESSION (Sesiones)

Las sesiones guardan datos temporales por usuario (hasta que cierre navegador o expire).  
👉 Se usan mucho para login y carritos de compra.

`<?php session_start();  $_SESSION["usuario"] = "Nye"; echo "Usuario guardado en sesión.";`

En otra página:

`<?php session_start(); echo $_SESSION["usuario"]; // Nye`

---

## 8.8 🔹 $_COOKIE (Cookies)

Se guardan en el navegador del usuario.

👉 Crear cookie:

`setcookie("idioma", "es", time() + 3600); // dura 1 hora`

👉 Leer cookie:

`echo $_COOKIE["idioma"]; // es`

---

## 8.9 🔹 $_SERVER

Contiene información del servidor y la petición.

👉 Ejemplo:

`echo $_SERVER['SERVER_NAME'];  // localhost echo $_SERVER['PHP_SELF'];     // /procesar.php echo $_SERVER['REQUEST_METHOD']; // GET o POST`

---

## 8.10 🔹 Seguridad en Formularios

1. **Validar datos** → comprobar que lo ingresado es correcto.
    
    `if (empty($_POST["nombre"])) {     echo "El nombre es obligatorio"; }`
    
2. **Escapar HTML** → evitar ataques XSS.
    
    `$nombre = htmlspecialchars($_POST["nombre"]);`
    
3. **Tokens CSRF** → Laravel ya los maneja con `@csrf`.
    

---

## 8.11 🔹 Ejemplo Integrador

Formulario `index.html`:

`<form method="POST" action="login.php">     <input type="text" name="usuario" placeholder="Usuario">     <input type="password" name="clave" placeholder="Contraseña">     <button type="submit">Ingresar</button> </form>`

Archivo `login.php`:

`<?php session_start();  $usuario = $_POST["usuario"]; $clave = $_POST["clave"];  if ($usuario === "admin" && $clave === "1234") {     $_SESSION["usuario"] = $usuario;     echo "Bienvenido $usuario"; } else {     echo "Credenciales inválidas"; } ?>`

---

## ✅ Resumen del Capítulo 8

- **$_GET** → datos por URL.
- **$_POST** → datos de formularios.
- **$_REQUEST** → mezcla de GET y POST (poco usado).
- **$_FILES** → subida de archivos.
- **$_SESSION** → datos por usuario (ej. login).
- **$_COOKIE** → datos guardados en navegador.
- **$_SERVER** → información del servidor/petición.
    
- Siempre validar y sanitizar entradas (`htmlspecialchars`).