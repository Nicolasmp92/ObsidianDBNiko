# 📘 Wiki PHP – Capítulo 3: Control de Flujo

## 3.1 🔹 Condicionales (if / else)

Permiten tomar **decisiones** según una condición.

👉 Ejemplo simple:

```<?php $edad = 18;  if ($edad >= 18) {     echo "Eres mayor de edad"; } else {     echo "Eres menor de edad"; } ?>```

👉 Con varias condiciones:

`<?php $nota = 75;  if ($nota >= 90) {     echo "Excelente"; } elseif ($nota >= 60) {     echo "Aprobado"; } else {     echo "Reprobado"; } ?>`

---

## 3.2 🔹 Switch

Cuando tienes **muchos casos posibles**, `switch` es más limpio que muchos `if`.

👉 Ejemplo:

`<?php $dia = "martes";  switch ($dia) {     case "lunes":         echo "Inicio de semana";         break;     case "martes":     case "miércoles":         echo "Mitad de semana";         break;     case "viernes":         echo "Casi fin de semana";         break;     default:         echo "Día normal"; } ?>`

📌 `break` evita que se sigan ejecutando los demás casos.

---

## 3.3 🔹 Bucles

Sirven para **repetir instrucciones**.

---

### 🔁 For

Repite un número conocido de veces.

`<?php for ($i = 1; $i <= 5; $i++) {     echo "Número: $i <br>"; }`

---

### 🔁 While

Repite **mientras** la condición sea verdadera.

`<?php $i = 1; while ($i <= 5) {     echo "Número: $i <br>";     $i++; }`

---

### 🔁 Do...While

Ejecuta **al menos una vez**, aunque la condición sea falsa.

`<?php $i = 1; do {     echo "Número: $i <br>";     $i++; } while ($i <= 5);`

---

### 🔁 Foreach

Especial para recorrer arrays.

`<?php $frutas = ["manzana", "pera", "uva"];  foreach ($frutas as $fruta) {     echo $fruta . "<br>"; }`

👉 Con clave y valor:

`<?php $persona = ["nombre" => "Nye", "edad" => 33];  foreach ($persona as $clave => $valor) {     echo "$clave: $valor <br>"; }`

---

## 3.4 🔹 Control dentro de bucles

- **break** → corta el bucle.
    
- **continue** → salta a la siguiente iteración.
    

👉 Ejemplo:

`<?php for ($i = 1; $i <= 5; $i++) {     if ($i == 3) continue; // salta el número 3     if ($i == 5) break;    // corta el bucle en 5     echo "Número: $i <br>"; }`

---

## 3.5 🔹 Operador Ternario

Versión corta de un `if...else`.

👉 Ejemplo:

`<?php $edad = 20; echo ($edad >= 18) ? "Mayor de edad" : "Menor de edad";`

---

## 3.6 🔹 Match (PHP 8+)

Parecido a `switch`, pero más moderno y limpio.

👉 Ejemplo:

`<?php $estado = 2;  $resultado = match ($estado) {     1 => "Activo",     2 => "Inactivo",     3 => "Pendiente",     default => "Desconocido", };  echo $resultado; // Inactivo`

---

## 3.7 🔹 Ejemplo Integrador

`<?php $usuarios = ["Nye", "Elizabeth", "Bastián"];  foreach ($usuarios as $user) {     if ($user == "Nye") {         echo "Admin detectado: $user <br>";     } else {         echo "Usuario común: $user <br>";     } }`

---

## ✅ Resumen del Capítulo 3

- **if / else** → decisiones simples.
    
- **switch / match** → muchas opciones.
    
- **for / while / do...while** → repetir acciones.
    
- **foreach** → recorrer arrays fácilmente.
    
- **break / continue** → controlar bucles.
    
- **operador ternario** → atajo para if.