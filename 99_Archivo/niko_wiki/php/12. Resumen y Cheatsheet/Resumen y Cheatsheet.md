# 📘 Wiki PHP – Capítulo 12: Resumen y Cheatsheet

---

## 🔹 Variables y Constantes

`$nombre = "Nye";   // Variable define("PI", 3.14); // Constante const APP = "WikiPHP"; // Constante`

---

## 🔹 Tipos de Datos

- **String** → `"Hola"`
    
- **Integer** → `25`
    
- **Float** → `3.14`
    
- **Boolean** → `true / false`
    
- **Array** → `["pera", "manzana"]`
    
- **Objeto** → instancias de clases
    
- **NULL** → sin valor
    

👉 Depuración:

`var_dump($variable);`

---

## 🔹 Operadores

- **Aritméticos**: `+ - * / %`
    
- **Comparación**: `== === != !== > < <=`
    
- **Lógicos**: `&& || !`
    
- **Asignación**: `= += -= *= /=`
    
- **Incremento**: `++ --`
    
- **Ternario**:
    
    `$msg = ($edad >= 18) ? "Mayor" : "Menor";`
    

---

## 🔹 Control de Flujo

`if ($a > 10) { ... }  elseif ($a == 10) { ... }  else { ... }  switch ($var) {     case 1: ...; break;     default: ...; }  for ($i=0; $i<5; $i++) { ... } while ($cond) { ... } do { ... } while ($cond);  foreach ($arr as $item) { ... }`

---

## 🔹 Funciones

`function sumar($a, $b = 0): int {     return $a + $b; }  $anonima = function($x) { return $x * 2; }; $flechita = fn($x) => $x * 2;`

---

## 🔹 Clases y Objetos

`class Persona {     public $nombre;     private $edad;      public function __construct($n, $e) {         $this->nombre = $n;         $this->edad = $e;     }      public function saludar() {         return "Hola, soy $this->nombre";     } }  $p = new Persona("Nye", 33); echo $p->saludar();`

- **public / private / protected** → visibilidad.
    
- **extends** → herencia.
    
- **interface / implements** → contratos.
    
- **trait** → reutilización.
    

---

## 🔹 Arrays

`$frutas = ["manzana", "pera"]; $persona = ["nombre" => "Nye", "edad" => 33];  count($frutas); in_array("pera", $frutas); array_push($frutas, "uva");  foreach ($persona as $k => $v) {     echo "$k: $v"; }`

👉 Moderno:

`array_map(fn($n) => $n*2, [1,2,3]);  // [2,4,6] array_filter([1,2,3], fn($n) => $n%2==0); // [2]`

---

## 🔹 Manejo de Errores

`try {     $div = 10 / 0; } catch (DivisionByZeroError $e) {     echo "Error: " . $e->getMessage(); } finally {     echo "Finalizado"; }`

👉 Personalizado:

`throw new Exception("Error propio");`

---

## 🔹 Superglobales

- `$_GET` → datos por URL
    
- `$_POST` → datos de formularios
    
- `$_FILES` → subida de archivos
    
- `$_SESSION` → variables de sesión
    
- `$_COOKIE` → cookies en navegador
    
- `$_SERVER` → info del servidor
    

---

## 🔹 Archivos

`file_put_contents("datos.txt", "Hola Mundo"); echo file_get_contents("datos.txt");  $json = json_encode(["nombre"=>"Nye"]); $datos = json_decode($json, true);`

---

## 🔹 Base de Datos (PDO)

`$pdo = new PDO("mysql:host=localhost;dbname=mi_base", "root", "");  $stmt = $pdo->prepare("SELECT * FROM usuarios WHERE edad > :edad"); $stmt->execute([":edad" => 18]);  foreach ($stmt as $fila) {     echo $fila["nombre"]; }`

---

## 🔹 Composer

`composer init composer require vendor/paquete`

👉 Gestiona dependencias y autoload (`vendor/autoload.php`).

---

## 🔹 Buenas Prácticas

✔ Usar **PDO** + prepared statements.  
✔ Seguir **PSR-12** (estándares).  
✔ Validar y sanitizar entradas (`htmlspecialchars`).  
✔ Usar **namespaces y autoload**.  
✔ Registrar errores en logs, no en pantalla.  
✔ Usar control de versiones (**Git/GitHub**).

---

# ✅ Super Resumen en 1 línea

- **PHP = server-side.**
    
- **Variables/constantes** guardan datos.
    
- **Operadores/condicionales/bucles** = lógica.
    
- **Funciones** = tareas reutilizables.
    
- **POO** = clases, objetos, herencia, `$this`.
    
- **Arrays/colecciones** = manipulación de datos.
    
- **Errores/excepciones** = control de fallos.
    
- **Superglobales** = comunicación con usuario y servidor.
    
- **Archivos y BD** = persistencia de datos.
    
- **Composer/PSR** = proyectos modernos y mantenibles.
    

---

🎉 Con este capítulo cierras el **Wiki completo de PHP** → desde lo básico hasta lo avanzado, todo explicado con ejemplos y buenas prácticas.

👉 Mi propuesta: ahora que ya tienes la **base de PHP cubierta**, podemos hacer un **nuevo Wiki de Laravel** (capítulos sobre rutas, controladores, Blade, Eloquent, Livewire, etc.).