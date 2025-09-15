# 📘 Wiki PHP – Capítulo 2: Fundamentos

## 2.1 🔹 Variables

- Son "cajitas" donde guardamos valores.
- Siempre comienzan con el símbolo `$`.
- No necesitas declarar el tipo (PHP es **débilmente tipado**).
    

👉 Ejemplo:

```php
	<?php $nombre = "Nye";// String 
		$edad = 33;// Entero 
		$altura = 1.69;// Decimal 
		$activo = true;// Booleano  
		echo "Hola, me llamo $nombre y tengo $edad años."; ?>
		
```

📌 Reglas para nombres de variables:

- Deben empezar con `$` y una letra o guion bajo.
- No pueden empezar con número (`$2nombre ❌`).
- Sensibles a mayúsculas/minúsculas (`$nombre` ≠ `$Nombre`).
    

---

## 2.2 🔹 Constantes

- Son como variables, pero su valor **no cambia**.
- Se definen con `define()` o `const`.
    

👉 Ejemplo:

```php
<?php 
	define("PI", 3.1416); 
	const APP_NAME = "Mi Aplicación";  
	
	echo PI;// 3.1416 
	echo APP_NAME;   // Mi Aplicación ?>
```

---

## 2.3 🔹 Tipos de Datos

PHP maneja varios tipos básicos:

1. **String (texto)** → `"Hola"`
2. **Integer (entero)** → `25`
3. **Float (decimal)** → `3.14`
4. **Boolean (verdadero/falso)** → `true`, `false`
5. **Array (listas de valores)** → `["manzana", "pera"]`
6. **Objeto** → instancias de clases
7. **NULL** → sin valor
    

👉 Ejemplo:

```php
<?php 
	$texto = "PHP"; 
	$numero = 2025; 
	$decimal = 8.3; 
	$verdad = true; 
	$nada = null;  
	var_dump($texto, $numero, $decimal, $verdad, $nada); 
?>
```

📌 `var_dump()` muestra el tipo y valor → súper útil para depuración.

---

## 2.4 🔹 Operadores

### 2.4.1 Aritméticos

```php
	$a = 10; 
	$b = 3;  
	
	echo $a + $b; // 13 (suma) 
	echo $a - $b; // 7  (resta) 
	echo $a * $b; // 30 (multiplicación) 
	echo $a / $b; // 3.333 (división) 
	echo $a % $b; // 1  (módulo - resto)
```

---

### 2.4.2 Asignación

```php
	$x = 5; 
	$x += 3;  // equivale a $x = $x + 3 → 8 
	$x -= 2;  // equivale a $x = $x - 2 → 6 
	$x *= 4;  // 24 
	$x /= 6;  // 4
	
```

---

### 2.4.3 Comparación

```php
	$a = 5; 
	$b = "5";  
	
	var_dump($a == $b);  // true (solo compara valor) 
	var_dump($a === $b); // false (compara valor y tipo) 
	var_dump($a != $b);  // false 
	var_dump($a !== $b); // true 
	var_dump($a > 3);    // true 
	var_dump($a <= 5);   // true 
```

📌 Ojo con `==` (comparación flexible) vs `===` (comparación estricta).

---

### 2.4.4 Lógicos

```php
$edad = 20;  

if ($edad >= 18 && $edad <= 30) {
     echo "Edad válida"; 
     }  

if ($edad < 18 || $edad > 65) {
    echo "Fuera de rango"; 
    }  
          
if (!$activo) {    
    echo "No está activo"; 
    }
```

---

### 2.4.5 Incremento y Decremento

```php
	$i = 1; 
	echo ++$i; // 2 (pre-incremento) 
	echo $i++; // 2 (post-incremento, luego será 3)
```

---

## 2.5 🔹 Conversiones de Tipo

PHP convierte automáticamente, pero también puedes forzar:

```php
	$a = "10"; 
	$b = (int)$a;  // convierte string a entero 
	$c = (float)"3.14"; // string a float 
	$d = (string)123;   // número a texto
```

---

## 2.6 🔹 Ejemplo Integrador

```php
<?php 
	$nombre = "Nye"; 
	$edad = 33; 
	$altura = 1.69; 
	$activo = true; 
	define("APP", "WikiPHP");  
	echo "Bienvenido a " . APP . "<br>"; 
	echo "Hola, me llamo 
	$nombre, tengo 
	$edad años y mido 
	$altura metros.<br>";  
	if ($activo) {     
	echo "El usuario está activo."; 
	} else {    
	 echo "El usuario no está activo."; 
	} ?>
```

---

## ✅ Resumen del Capítulo 2

- **Variables** → `$nombre` (cambian).
    
- **Constantes** → `define("PI", 3.14)` (no cambian).
    
- **Tipos de datos** → string, int, float, bool, array, objeto, null.
    
- **Operadores** → aritméticos, asignación, comparación, lógicos, incremento.
    
- **Conversiones** → automáticas o forzadas con `(int)`, `(float)`, `(string)`.