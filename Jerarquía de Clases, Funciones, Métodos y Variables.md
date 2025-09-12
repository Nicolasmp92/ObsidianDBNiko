
### 🔹 Clase

- **Definición**: Plantilla o molde para crear **objetos**.
    
- **Contiene**:
    
    - **Propiedades** → variables internas que definen el estado del objeto.
    - **Métodos** → funciones internas que definen el comportamiento del objeto.

### 🔹 Función

- **Definición**: Bloque de código reutilizable, independiente de las clases.
- **Uso**: Se llama directamente por su nombre.
- **Variables locales**: Solo existen dentro de la función.

### 🔹 Método

- **Definición**: Una función que vive dentro de una clase.
- **Uso**: Se invoca a través de un objeto → `$objeto->metodo()`.
- **Alcance**: Puede usar tanto variables locales como las propiedades de la clase.

### 🔹 Variable

- **Definición**: Espacio de memoria donde se guarda un valor (número, texto, booleano, objeto, etc.).
- **Tipos**:
    - **Locales** → viven dentro de una función o método.
    - **Propiedades** → variables que pertenecen a una clase.

---

### 📊 Esquema jerárquico

```
📦 Clase  
	┣ 📜 Propiedades (variables de clase)  
	┗ 🔧 Métodos      
		┣ Variables locales      
		┗ Uso de propiedades con $this 
	⚙️ Función independiente  
			┗ Variables locales
```
---

### 📌 Ejemplo práctico

```php
<?php 
	// Función normal 
	function sumar($a, $b){
	     $resultado = $a + $b;// variable local     
	     return $resultado; 
	}  
	
	// Clase 
	class Persona{     
		public $nombre; // propiedad     
		public $edad;   // propiedad      
		
		// Método con variable local
		 public function saludar(){
		    $mensaje = "Hola, soy " . $this->nombre; // $mensaje es local
		    return $mensaje;     
		}      
			
	public function cumplirAnios() {         $this->edad++; // modifica propiedad de clase     } }  // Uso de función echo sumar(2, 3); // 5  // Uso de clase $persona = new Persona(); $persona->nombre = "Nye"; $persona->edad = 33;  echo $persona->saludar(); // Hola, soy Nye $persona->cumplirAnios(); echo $persona->edad; // 34
```

---

## 📖 2. Diccionario de Palabras Reservadas y Conceptos

---

### 🐘 PHP — Palabras reservadas principales

_(no se pueden usar como nombres de variables, funciones o clases)_

- **class** → define una clase.
    
- **function** → define una función o método.
    
- **public, private, protected** → modificadores de acceso para propiedades/métodos.
    
- **static** → define un método/propiedad estática.
    
- **const** → constante dentro de una clase.
    
- **new** → crea un nuevo objeto de una clase.
    
- **extends** → herencia de clases.
    
- **implements** → implementar una interfaz.
    
- **interface** → contrato de métodos que deben implementarse.
    
- **trait** → bloque de métodos reutilizables.
    
- **abstract** → clase o método abstracto (debe ser implementado en herencia).
    
- **final** → evita sobreescritura de clase/método.
    
- **return** → devuelve un valor.
    
- **if, else, elseif** → condicionales.
    
- **switch, case, default** → condicional múltiple.
    
- **for, foreach, while, do** → bucles.
    
- **break, continue** → control de bucles.
    
- **try, catch, finally, throw** → manejo de excepciones.
    
- **namespace, use** → organización de clases.
    
- **global** → acceder a variables globales.
    
- **var** → define variables (obsoleto, se usa `public` en clases).
    
- **isset, unset, empty** → manejo de variables.
    
- **echo, print** → imprimir en pantalla.
    
- **include, require** → incluir archivos externos.
    
- **declare, instanceof** → control de ejecución y chequeo de objetos.
    

---

### 🌐 Laravel — Conceptos clave

- **Artisan** → CLI de Laravel (ej: `php artisan migrate`).
    
- **Migration** → archivo para crear o modificar tablas de BD.
    
- **Seeder** → archivo para insertar datos de prueba en BD.
    
- **Factory** → genera datos falsos (faker) para pruebas.
    
- **Model** → representa una tabla de la BD usando Eloquent ORM.
    
- **Controller** → recibe peticiones y ejecuta lógica de negocio.
    
- **Route** → define rutas de acceso a controladores/vistas.
    
- **Middleware** → filtro para las peticiones (ej: auth).
    
- **Blade** → motor de plantillas para vistas.
    
- **Eloquent** → ORM de Laravel para interactuar con la base de datos.
    
- **Pivot** → tabla intermedia para relaciones Many-to-Many.
    
- **Service Container** → sistema de inyección de dependencias.
    
- **Queue** → sistema de colas para tareas en segundo plano.
    
- **Event/Listener** → sistema de eventos.
    
- **Job** → tarea que se ejecuta en background.
    
- **Observer** → escucha cambios en modelos (ej: created, updated).
    

---

### ⚡ Livewire — Conceptos clave

- **Component** → clase + vista que maneja lógica y presentación.
    
- **wire:model** → sincroniza un campo HTML con una propiedad de la clase.
    
- **wire:click** → ejecuta un método al hacer clic.
    
- **wire:loading** → muestra algo mientras se procesa.
    
- **wire:submit.prevent** → evita refresh del form y ejecuta método.
    
- **$this** → referencia al componente Livewire actual.
    
- **emit** → enviar un evento desde un componente.
    
- **listen** → escuchar eventos desde otro componente.
    
- **mount()** → método que se ejecuta al inicializar el componente.
    
- **render()** → método obligatorio que devuelve la vista.
    
- **updated()** → se ejecuta al actualizar una propiedad.
    
- **validate()** → método para validar datos en Livewire.
    
- **dispatch()** → enviar evento al frontend (JS).
    

---

✅ Con esto tienes un **manual de referencia rápida**.  
Mi recomendación: lo copies en tu **wiki de Obsidian** y lo uses como mapa base, y luego vamos agregando ejemplos avanzados de Laravel (migraciones, relaciones, autenticación, etc.).