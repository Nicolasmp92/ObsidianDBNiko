# 📘 Wiki PHP – Capítulo 11: Temas Avanzados

## 11.1 🔹 Programación Funcional en PHP

PHP soporta estilos **funcionales** además de POO.

- **Funciones anónimas**
    

`$suma = function($a, $b) { return $a + $b; }; echo $suma(2, 3); // 5`

- **Funciones flecha** (PHP 7.4+)
    

`$doble = fn($x) => $x * 2; echo $doble(4); // 8`

- **Uso con arrays**
    

`$numeros = [1,2,3,4,5]; $pares = array_filter($numeros, fn($n) => $n % 2 === 0); print_r($pares); // [2,4]`

📌 En Laravel esto se refleja en `Collection::map()`, `filter()`, `reduce()`.

---

## 11.2 🔹 Composer

El **gestor de dependencias de PHP**.  
Sirve para instalar librerías y frameworks.

👉 Instalar un paquete:

`composer require monolog/monolog`

👉 Archivo `composer.json`:

`{   "require": {     "monolog/monolog": "^3.0"   } }`

📌 Laravel usa Composer para instalarse y manejar dependencias (`laravel/breeze`, `livewire/livewire`, etc.).

---

## 11.3 🔹 PSR (PHP Standards Recommendations)

Son **estándares de código** definidos por la comunidad.  
Sirven para que todo proyecto PHP sea consistente.

Los más importantes:

- **PSR-1**: Estándares básicos de código.
    
- **PSR-2**: Estilo de código (indentación, llaves, espacios).
    
- **PSR-4**: Autoloading de clases (Laravel lo usa).
    
- **PSR-12**: Reglas extendidas de formato de código.
    

👉 Ejemplo de PSR-4 (autoloading):

`{   "autoload": {     "psr-4": {       "App\\": "src/"     }   } }`

---

## 11.4 🔹 Namespaces

Permiten organizar clases y evitar conflictos de nombres.

👉 Ejemplo:

`namespace App\Models;  class User {     public $name = "Nye"; }`

👉 Para usarlo:

`use App\Models\User;  $u = new User();`

📌 En Laravel, todos los modelos están bajo el namespace `App\Models`.

---

## 11.5 🔹 Buenas Prácticas en PHP

1. **Usar PDO con prepared statements** → seguridad.
    
2. **Seguir PSR-12** → código limpio.
    
3. **Usar Composer** → no reinventar la rueda.
    
4. **Validar y sanitizar entradas**.
    
5. **Usar control de versiones (Git/GitHub)**.
    
6. **Errores a logs, no en pantalla** en producción.
    
7. **Dividir código en clases y métodos** (no todo en un solo archivo).
    

---

## 11.6 🔹 Autoload y Namespaces en Proyectos

En proyectos modernos no tienes que hacer `require` manual de cada clase.  
Composer se encarga del **autoload**.

👉 Ejemplo:

`require 'vendor/autoload.php';  $logger = new Monolog\Logger('mi_app');`

📌 En Laravel, todo esto ya viene configurado automáticamente.

---

## 11.7 🔹 Tipado Estricto

PHP es débilmente tipado, pero puedes activar tipado estricto para más seguridad.

`declare(strict_types=1);  function suma(int $a, int $b): int {     return $a + $b; }  echo suma(5, 3); // 8`

📌 Sin `strict_types`, PHP convierte automáticamente strings a números, etc.

---

## 11.8 🔹 Patrones de Diseño

Muy usados en Laravel y frameworks:

- **Singleton** → una sola instancia global.
    
- **Factory** → crea objetos de forma centralizada.
    
- **Repository** → capa intermedia para acceso a BD.
    
- **MVC (Modelo–Vista–Controlador)** → arquitectura de Laravel.
    

---

## 11.9 🔹 Ejemplo Integrador

Supongamos un mini proyecto con buenas prácticas.

`<?php declare(strict_types=1);  namespace App\Services;  class Calculadora {     public function sumar(int $a, int $b): int {         return $a + $b;     } }  // Autoload con PSR-4 use App\Services\Calculadora;  $calc = new Calculadora(); echo $calc->sumar(10, 5); // 15`

---

## ✅ Resumen del Capítulo 11

- **Programación funcional** → funciones flecha, map, filter, reduce.
    
- **Composer** → gestor de dependencias.
    
- **PSR** → estándares de código (PSR-4 muy usado en Laravel).
    
- **Namespaces** → organización y autoload.
    
- **Buenas prácticas** → seguridad, legibilidad, modularidad.
    
- **Tipado estricto** → más robustez.
    
- **Patrones de diseño** → base de frameworks modernos.
    

---

📌 Con esto ya pasaste de **PHP básico → PHP profesional**, lo que te prepara para frameworks como Laravel.

👉 Próximo paso → **Capítulo 12: Resumen y Cheatsheet de PHP**, donde condensamos TODO el Wiki en tablas rápidas (perfecto para imprimir o tener en Obsidian como guía rápida).