## 5.1 🔹 ¿Qué es la POO?

- Un **paradigma de programación** (forma de pensar y organizar el código).
    
- Se basa en **clases** (planos) y **objetos** (instancias reales).
    
- Permite organizar el código como si fueran **entidades del mundo real** con características y acciones.
    

👉 Ejemplo real:

- Clase: **Coche**
    
- Objeto: mi coche, tu coche.
    
- Propiedades: color, marca, modelo.
    
- Métodos: arrancar, frenar, acelerar.
    

---

## 5.2 🔹 Clases y Objetos

### Clase

Un **molde** que define propiedades y métodos.

`<?php class Persona {     public $nombre;     public $edad;      public function saludar() {         return "Hola, soy $this->nombre y tengo $this->edad años.";     } }`

### Objeto

Una **instancia real** creada a partir de una clase.

`<?php $persona1 = new Persona(); $persona1->nombre = "Nye"; $persona1->edad = 33;  echo $persona1->saludar(); // Hola, soy Nye y tengo 33 años. ?>`

---

## 5.3 🔹 Propiedades

Son **variables dentro de una clase**.  
Definen características del objeto.

`class Coche {     public $marca;     public $color; }`

---

## 5.4 🔹 Métodos

Son **funciones dentro de la clase**.  
Representan acciones que el objeto puede hacer.

`class Coche {     public $marca;      public function arrancar() {         return "El coche $this->marca está arrancando 🚗";     } }`

---

## 5.5 🔹 `$this`

- Representa el **objeto actual**.
    
- Sirve para acceder a sus propiedades y métodos.
    

`class Persona {     public $nombre;      public function presentarse() {         return "Hola, soy " . $this->nombre;     } }`

---

## 5.6 🔹 Constructores y Destructores

### Constructor (`__construct`)

Se ejecuta **automáticamente al crear un objeto**.

`class Persona {     public $nombre;      public function __construct($nombre) {         $this->nombre = $nombre;     } }  $p = new Persona("Elizabeth"); echo $p->nombre; // Elizabeth`

### Destructor (`__destruct`)

Se ejecuta **cuando el objeto deja de existir**.

`class Test {     public function __destruct() {         echo "Objeto destruido";     } }`

---

## 5.7 🔹 Modificadores de Acceso

Controlan la **visibilidad** de propiedades y métodos.

- `public` → accesible desde cualquier parte.
    
- `private` → solo dentro de la clase.
    
- `protected` → dentro de la clase y clases hijas.
    

👉 Ejemplo:

`class CuentaBancaria {     public $titular;     private $saldo = 0;      public function depositar($monto) {         $this->saldo += $monto;     }      public function verSaldo() {         return $this->saldo;     } }`

---

## 5.8 🔹 Herencia

Una clase puede **heredar de otra**.  
La clase hija recibe propiedades y métodos de la clase padre.

`class Animal {     public function hacerSonido() {         return "Hace un sonido";     } }  class Perro extends Animal {     public function hacerSonido() {         return "Guau 🐶";     } }  $miPerro = new Perro(); echo $miPerro->hacerSonido(); // Guau 🐶`

---

## 5.9 🔹 Polimorfismo

Permite que **un mismo método** se comporte diferente en distintas clases.

`class Figura {     public function area() {         return 0;     } }  class Cuadrado extends Figura {     public $lado;     public function __construct($lado) {         $this->lado = $lado;     }     public function area() {         return $this->lado * $this->lado;     } }  $figura = new Cuadrado(5); echo $figura->area(); // 25`

---

## 5.10 🔹 Interfaces

Definen un **contrato** (métodos que deben implementarse).

`interface Animal {     public function hacerSonido(); }  class Gato implements Animal {     public function hacerSonido() {         return "Miau 🐱";     } }`

---

## 5.11 🔹 Traits

Permiten **reutilizar código** en varias clases sin herencia.

`trait Mensajes {     public function saludar() {         return "Hola desde el trait 👋";     } }  class Usuario {     use Mensajes; }  $u = new Usuario(); echo $u->saludar();`

---

## 5.12 🔹 Namespaces y Autoload

Sirven para organizar el código en proyectos grandes.

`namespace App\Models;  class User {     public $name; }`

📌 En Laravel esto se usa mucho:  
`App\Models\User` → está dentro del namespace `App\Models`.

---

## 5.13 🔹 Ejemplo Integrador

`<?php class Usuario {     public $nombre;     private $email;      public function __construct($nombre, $email) {         $this->nombre = $nombre;         $this->email = $email;     }      public function presentarse() {         return "Soy $this->nombre y mi correo es $this->email";     } }  $u = new Usuario("Nye", "nye@correo.com"); echo $u->presentarse(); // Soy Nye y mi correo es nye@correo.com ?>`

---

## ✅ Resumen del Capítulo 5

- **Clase** → molde.
    
- **Objeto** → ejemplar real.
    
- **Propiedades** → características.
    
- **Métodos** → acciones.
    
- **$this** → referencia al objeto actual.
    
- **Constructor/Destructor** → al crear o destruir objetos.
    
- **Modificadores** → public, private, protected.
    
- **Herencia** → una clase hereda de otra.
    
- **Polimorfismo** → métodos con diferente comportamiento.
    
- **Interfaces y Traits** → contratos y reutilización.
    
- **Namespaces** → organización de código.
- 