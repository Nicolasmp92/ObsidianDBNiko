.

---

# 📘 Wiki PHP – Capítulo 6: Arrays y Colecciones

## 6.1 🔹 ¿Qué es un Array?

Un **array** es una **lista de valores** en una sola variable.  
Puede guardar **números, textos, booleanos, incluso otros arrays**.

👉 Ejemplo:

`$frutas = ["manzana", "pera", "uva"]; echo $frutas[0]; // manzana`

📌 Los arrays en PHP son muy flexibles → funcionan como listas, diccionarios y hasta matrices.

---

## 6.2 🔹 Tipos de Arrays

### 6.2.1 Arrays Indexados (con índices numéricos)

Los elementos tienen posiciones numéricas automáticas (`0, 1, 2...`).

`$colores = ["rojo", "verde", "azul"]; echo $colores[1]; // verde`

---

### 6.2.2 Arrays Asociativos (con claves personalizadas)

Cada valor tiene un nombre como clave.

`$persona = [     "nombre" => "Nye",     "edad" => 33,     "activo" => true ];  echo $persona["nombre"]; // Nye`

---

### 6.2.3 Arrays Multidimensionales

Arrays dentro de arrays.

`$usuarios = [     ["nombre" => "Nye", "edad" => 33],     ["nombre" => "Elizabeth", "edad" => 30] ];  echo $usuarios[1]["nombre"]; // Elizabeth`

---

## 6.3 🔹 Recorrer Arrays

### foreach (lo más común)

`$animales = ["perro", "gato", "pez"];  foreach ($animales as $animal) {     echo $animal . "<br>"; }`

👉 Con clave y valor:

`$persona = ["nombre" => "Nye", "edad" => 33];  foreach ($persona as $clave => $valor) {     echo "$clave: $valor <br>"; }`

---

## 6.4 🔹 Funciones útiles de Arrays

PHP trae muchas funciones incorporadas para arrays:

- `count($array)` → cantidad de elementos.
    
- `in_array("valor", $array)` → busca si un valor existe.
    
- `array_push($array, "nuevo")` → agrega al final.
    
- `array_pop($array)` → elimina el último.
    
- `array_merge($a, $b)` → une arrays.
    
- `array_keys($array)` → devuelve todas las claves.
    
- `array_values($array)` → devuelve todos los valores.
    

👉 Ejemplo:

`$frutas = ["manzana", "pera"]; array_push($frutas, "uva"); // ["manzana", "pera", "uva"]  if (in_array("uva", $frutas)) {     echo "Sí hay uva"; }`

---

## 6.5 🔹 Ordenar Arrays

- `sort($array)` → ordena ascendente.
    
- `rsort($array)` → ordena descendente.
    
- `asort($array)` → ordena por valores manteniendo claves.
    
- `ksort($array)` → ordena por claves.
    

👉 Ejemplo:

`$numeros = [3, 1, 5, 2]; sort($numeros); // [1, 2, 3, 5]`

---

## 6.6 🔹 Map, Filter y Reduce

Funciones modernas que transforman arrays.

### map → aplica función a cada elemento

`$numeros = [1, 2, 3, 4]; $dobles = array_map(fn($n) => $n * 2, $numeros); print_r($dobles); // [2, 4, 6, 8]`

### filter → filtra según condición

`$numeros = [1, 2, 3, 4, 5]; $pares = array_filter($numeros, fn($n) => $n % 2 == 0); print_r($pares); // [2, 4]`

### reduce → reduce todo a un solo valor

`$numeros = [1, 2, 3, 4, 5]; $suma = array_reduce($numeros, fn($acum, $n) => $acum + $n, 0); echo $suma; // 15`

---

## 6.7 🔹 Arrays en PHP vs Colecciones en Laravel

En **Laravel**, los arrays se vuelven más poderosos con **Collections**:

👉 Ejemplo en Laravel:

`$usuarios = collect([     ["nombre" => "Nye", "edad" => 33],     ["nombre" => "Elizabeth", "edad" => 30] ]);  $mayores = $usuarios->where("edad", ">", 31);  dd($mayores);`

📌 Collections = arrays con **métodos extra** (`map`, `filter`, `pluck`, `sum`, `avg`...).  
👉 Son **muy usadas en Eloquent** (al traer datos de la BD).

---

## 6.8 🔹 Ejemplo Integrador

`$productos = [     ["nombre" => "Café", "precio" => 1200],     ["nombre" => "Té", "precio" => 900],     ["nombre" => "Jugo", "precio" => 1500], ];  // Mostrar productos mayores a 1000 foreach ($productos as $p) {     if ($p["precio"] > 1000) {         echo $p["nombre"] . " cuesta " . $p["precio"] . "<br>";     } }`

---

## ✅ Resumen del Capítulo 6

- **Array indexado** → lista con índices numéricos.
    
- **Array asociativo** → lista con claves personalizadas.
    
- **Array multidimensional** → arrays dentro de arrays.
    
- **foreach** → la forma más usada para recorrer.
    
- **Funciones útiles** → `count`, `in_array`, `array_push`, `array_merge`.
    
- **Ordenación** → `sort`, `rsort`, `asort`, `ksort`.
    
- **map, filter, reduce** → programación funcional con arrays.
    
- **Collections en Laravel** → arrays mejorados con métodos extra.