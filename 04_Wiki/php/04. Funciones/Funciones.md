# 📘 Wiki PHP – Capítulo 4: Funciones

## 4.1 🔹 ¿Qué es una función?

Una **función** es un bloque de código que:

- Tiene un **nombre**.
    
- Se puede **ejecutar varias veces** (reutilizable).
    
- Puede recibir **parámetros** (entradas).
    
- Puede devolver un **valor** (salida).
    

👉 Ejemplo básico:

`<?php function saludar() {     echo "Hola Mundo!"; }  saludar(); // Llama la función ?>`

---

## 4.2 🔹 Parámetros

Puedes enviar valores a la función.

👉 Ejemplo:

`<?php function saludar($nombre) {     echo "Hola, $nombre!"; }  saludar("Nye");  // Hola, Nye! saludar("Elizabeth");  // Hola, Elizabeth! ?>`

---

## 4.3 🔹 Valores de Retorno

Una función puede **devolver un resultado** en vez de solo mostrarlo.

👉 Ejemplo:

`<?php function sumar($a, $b) {     return $a + $b; }  $resultado = sumar(5, 3); echo $resultado; // 8 ?>`

---

## 4.4 🔹 Parámetros por Defecto

Si no pasas un valor, se usará el predeterminado.

👉 Ejemplo:

`<?php function bienvenida($nombre = "Invitado") {     echo "Bienvenido, $nombre"; }  bienvenida();         // Bienvenido, Invitado bienvenida("Nye");    // Bienvenido, Nye ?>`

---

## 4.5 🔹 Parámetros con Tipado (PHP 7+)

Puedes forzar el tipo de dato.

👉 Ejemplo:

`<?php function areaRectangulo(int $base, int $altura): int {     return $base * $altura; }  echo areaRectangulo(5, 3); // 15 ?>`

📌 El `: int` después de los parámetros significa que la función devuelve un entero.

---

## 4.6 🔹 Funciones con número variable de argumentos

Con `...` (splat operator), una función recibe cualquier cantidad de parámetros.

👉 Ejemplo:

`<?php function sumarTodo(...$numeros) {     return array_sum($numeros); }  echo sumarTodo(1, 2, 3, 4, 5); // 15 ?>`

---

## 4.7 🔹 Funciones Anónimas (Closures)

Son funciones **sin nombre**, que se pueden guardar en variables o pasar como argumento.

👉 Ejemplo:

`<?php $saludar = function($nombre) {     return "Hola, $nombre!"; };  echo $saludar("Nye"); ?>`

---

## 4.8 🔹 Funciones Flecha (PHP 7.4+)

Versión simplificada de una función anónima.

👉 Ejemplo:

`<?php $doble = fn($x) => $x * 2;  echo $doble(4); // 8 ?>`

---

## 4.9 🔹 Funciones Recursivas

Una función puede llamarse a sí misma.  
Ejemplo típico: **factorial**.

👉 Ejemplo:

`<?php function factorial($n) {     if ($n <= 1) return 1;     return $n * factorial($n - 1); }  echo factorial(5); // 120 ?>`

---

## 4.10 🔹 Funciones Incorporadas (Built-in)

PHP trae **muchísimas funciones listas**.  
Ejemplos comunes:

- `strlen($txt)` → largo de un string.
    
- `strtolower($txt)` / `strtoupper($txt)` → minúsculas / mayúsculas.
    
- `count($array)` → cantidad de elementos.
    
- `array_merge($a, $b)` → unir arrays.
    
- `date("d/m/Y")` → fecha actual.
    

👉 Ejemplo:

`<?php echo strlen("Hola"); // 4 echo strtoupper("php"); // PHP ?>`

---

## 4.11 🔹 Diferencia entre Funciones y Métodos

- **Función**: definida fuera de una clase.
    
- **Método**: definida dentro de una clase.
    

👉 Ejemplo:

`<?php // Función function sumar($a, $b) { return $a + $b; }  // Método dentro de clase class Calculadora {     public function sumar($a, $b) {         return $a + $b;     } } ?>`

---

## 4.12 🔹 Ejemplo Integrador

`<?php function saludoPersonalizado($nombre, $edad = 18) {     return "Hola $nombre, tienes $edad años."; }  echo saludoPersonalizado("Nye", 33); // Hola Nye, tienes 33 años. echo saludoPersonalizado("Elizabeth"); // Hola Elizabeth, tienes 18 años. ?>`

---

## ✅ Resumen del Capítulo 4

- **Funciones** → bloques de código reutilizables.
    
- **Parámetros** → reciben valores.
    
- **Retorno** → devuelven resultados.
    
- **Por defecto** → valores preestablecidos.
    
- **Tipado** → obliga al tipo de datos.
    
- **Variádicas (`...`)** → reciben muchos argumentos.
    
- **Anónimas & Flecha** → más compactas.
    
- **Recursivas** → se llaman a sí mismas.
    
- **Funciones built-in** → ya vienen en PHP.

---

**Anterior:** [[Control de Flujo]] | **Siguiente:** [[Programación Orientada a Objetos (POO)]]
    

---

