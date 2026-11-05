# 📘 Wiki PHP – Capítulo 7: Manejo de Errores y Excepciones

## 7.1 🔹 Tipos de Errores en PHP

1. **Errores de sintaxis** → cuando el código está mal escrito (faltan `;` o llaves).
    - PHP los detecta antes de ejecutar.
    - Ejemplo:
        ``` php
	     echo "Hola" // ❌ falta punto y coma 
        ```
        
2. **Errores en tiempo de ejecución** → ocurren mientras el script corre.
    
    - Ejemplo: división por cero.
        
3. **Errores lógicos** → el código funciona pero da un resultado incorrecto.
    
    - Ejemplo: sumar en vez de restar.
        

---

## 7.2 🔹 Manejo Básico de Errores

PHP puede mostrar errores en pantalla (modo desarrollo) o registrarlos en logs.

👉 Para mostrar errores (solo en desarrollo):

`ini_set('display_errors', 1); error_reporting(E_ALL);`

👉 Para ocultarlos en producción:

`ini_set('display_errors', 0);`

---

## 7.3 🔹 Excepciones (`try`, `catch`, `finally`)

Una **excepción** es un error que podemos “atrapar” para manejarlo sin que la aplicación se rompa.

👉 Ejemplo:

`<?php try {     $division = 10 / 0;  // Error } catch (DivisionByZeroError $e) {     echo "Error: División por cero"; } finally {     echo "Este bloque siempre se ejecuta"; }`

📌 Flujo:

- `try` → código que puede fallar.
    
- `catch` → qué hacer si hay error.
    
- `finally` → se ejecuta siempre (haya error o no).
    

---

## 7.4 🔹 Lanzar Excepciones

Puedes lanzar tus propios errores con `throw`.

`function dividir($a, $b) {     if ($b == 0) {         throw new Exception("No se puede dividir entre cero");     }     return $a / $b; }  try {     echo dividir(10, 0); } catch (Exception $e) {     echo "Error: " . $e->getMessage(); }`

---

## 7.5 🔹 Tipos de Excepciones en PHP

- `Exception` → genérica.
    
- `Error` → errores graves.
    
- `DivisionByZeroError` → división entre cero.
    
- `TypeError` → tipo de dato incorrecto.
    
- `PDOException` → errores de base de datos (cuando usas PDO).
    

---

## 7.6 🔹 Personalizar Excepciones

Puedes crear tus propias excepciones extendiendo `Exception`.

`class MiExcepcion extends Exception {}  try {     throw new MiExcepcion("Algo salió mal"); } catch (MiExcepcion $e) {     echo "Error personalizado: " . $e->getMessage(); }`

---

## 7.7 🔹 Manejo de Errores con Funciones

- `trigger_error("Mensaje", E_USER_WARNING)` → genera un error manual.
    
- `set_error_handler("funcion")` → define cómo manejar los errores.
    

👉 Ejemplo:

`function miManejador($errno, $errstr) {     echo "Error [$errno]: $errstr"; } set_error_handler("miManejador");  echo 10 / 0; // Error manejado por la función`

---

## 7.8 🔹 Ejemplo Integrador

`<?php function conectarBD($host, $user, $pass) {     if ($host != "localhost") {         throw new Exception("No se pudo conectar al servidor");     }     return "Conexión exitosa"; }  try {     echo conectarBD("otrohost", "root", ""); } catch (Exception $e) {     echo "Error de conexión: " . $e->getMessage(); } finally {     echo "<br>Proceso finalizado"; }`

Salida:

`Error de conexión: No se pudo conectar al servidor Proceso finalizado`

---

## ✅ Resumen del Capítulo 7

- **Errores de sintaxis** → rompe antes de ejecutar.
    
- **Errores de ejecución** → ocurren al correr.
    
- **Errores lógicos** → código mal planteado.
    
- **try/catch/finally** → atrapar y manejar excepciones.
    
- **throw** → lanzar errores propios.
    
- **Excepciones personalizadas** → clases que extienden `Exception`.
    
- **Funciones de manejo** → `set_error_handler`, `trigger_error`.
    

---

📌 Con esto ya puedes **prevenir caídas en tu aplicación** y dar mensajes claros al usuario o registrar errores en logs.

---

**Anterior:** [[Arrays y Colecciones]] | **Siguiente:** [[Superglobales y Formularios]]