## 🐘 ¿Qué es PHP?

- PHP significa **“PHP: Hypertext Preprocessor”** (sí, es un acrónimo recursivo).
    
- Es un **lenguaje de programación interpretado**, lo que significa que el servidor lo lee y lo ejecuta **línea por línea**.
    
- Es **del lado del servidor (server-side)** → procesa la lógica antes de enviar el resultado al navegador.
    
- Es usado principalmente para crear **páginas web dinámicas** (que cambian según el usuario, la base de datos o la interacción).
    

👉 Ejemplo de página web con PHP:

```php 
<?php echo "Hola Mundo desde PHP!"; ?>
```

Si visitas esta página en el navegador, verás solo:

`Hola Mundo desde PHP!`

(el código PHP no se ve, solo el resultado).

---

## 📜 Breve Historia

- **1994**: Creado por **Rasmus Lerdorf** para manejar su página personal.
    
- **1995**: Lanzamiento público como “Personal Home Page Tools”.
    
- **2000**: Llega PHP 4 con el motor Zend.
    
- **2004**: PHP 5 introduce la **Programación Orientada a Objetos (POO)**.
    
- **2015**: PHP 7 da un salto enorme en **rendimiento**.
    
- **2020**: PHP 8 introduce nuevas características modernas como atributos y `match`.
    
- **2025**: La versión estable es **PHP 8.3** y ya se trabaja en **PHP 9**.
    

📌 Laravel 11/12 (el que tú usas) funciona sobre **PHP 8.2+**, así que estás al día.

---

## ⚙️ ¿Cómo funciona PHP en una web?

Cuando un usuario entra a una página con PHP ocurre esto:

1. El navegador pide la página → `https://miweb.com/index.php`
    
2. El **servidor web** (Apache, Nginx, etc.) detecta que es PHP.
    
3. El **motor PHP** interpreta el código PHP.
    
4. El resultado (HTML, JSON, texto, etc.) se envía al navegador.
    

👉 Diagrama simple:

`Usuario → Navegador → Servidor Apache/Nginx → Motor PHP → HTML → Navegador`

---

## 🛠️ Instalación y Entorno de Desarrollo

Para trabajar con PHP necesitas:

1. **Servidor web** (Apache, Nginx o incluso el embebido de PHP).
2. **PHP** instalado en tu sistema.
3. (Opcional) **Base de datos** como MySQL o MariaDB.
    

### Opciones comunes:

- **XAMPP** → Incluye Apache + PHP + MySQL (lo que usas ahora).
- **Laragon / MAMP / WAMP** → Alternativas amigables.
- **PHP Built-in Server** → Sin Apache:
    

`php -S localhost:8000`

Esto arranca un servidor local en el puerto 8000.

---

## 📂 Archivos PHP

- Un archivo PHP termina en `.php`.
- Dentro del archivo puedes mezclar **HTML y PHP**.
    

👉 Ejemplo:

```php 

<!DOCTYPE html>
 <html> 
	 <head>     
	 <title>Mi primera página PHP</title> 
	 </head> 
<body>     
	<h1>Bienvenido</h1>     
	<p> <?php echo "Hoy es " . date("d/m/Y"); ?>     </p> 
</body> 
</html>
```

El navegador verá algo como:

`Bienvenido Hoy es 15/09/2025`

---

## ✨ Características principales de PHP

1. **Multiplataforma** → funciona en Windows, Linux, Mac.
2. **Open Source** → libre y gratuito.
3. **Fácil de aprender** → sintaxis sencilla.
4. **Integración con HTML y JS** → puedes mezclar fácilmente.
5. **Amplio soporte en bases de datos** → MySQL, PostgreSQL, SQLite, etc.
6. **Comunidad gigante** → documentación, foros y frameworks (Laravel, Symfony, WordPress, etc.).
    

---

## 📌 Ejemplo práctico rápido

Archivo: `saludo.php`

`<?php $nombre = "Nye"; echo "Hola, $nombre! Bienvenido a PHP."; ?>`

Salida en el navegador:

`Hola, Nye! Bienvenido a PHP.`

---

## ✅ Resumen del Capítulo 1

- PHP = Lenguaje **interpretado, del lado del servidor**.
- Se usa para hacer **páginas dinámicas**.
- Nació en 1994 y sigue vigente en 2025 con PHP 8.3+.
- Funciona junto a un **servidor web** y puede integrarse con bases de datos.
- Se mezcla fácilmente con HTML.
- Es la base sobre la que funcionan frameworks como **Laravel**.