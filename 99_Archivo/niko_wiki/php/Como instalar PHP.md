## 🚀 Cómo instalar PHP en tu equipo (Windows)

> **Objetivo:** Tener PHP funcionando en tu computador local para poder ejecutar archivos `.php` desde la terminal o con un servidor local.

---

### 🔧 OPCIÓN 1: Instalar PHP en Windows (manual)

#### 🧱 Paso 1: Descargar PHP

1. Ve a la web oficial:  
    👉 https://windows.php.net/download/
    
2. Descarga la última versión **Non Thread Safe (NTS)** de 64 bits:  
    Ejemplo: `php-8.3.9-nts-Win64-vs16.zip`
    

#### 🗂 Paso 2: Descomprimir PHP

1. Crea una carpeta en `C:\php`
    
2. Descomprime ahí el archivo `.zip` que bajaste
    

#### 🛠 Paso 3: Configurar variables de entorno

1. Abre el **Panel de Control**
    
2. Ir a **Sistema > Configuración avanzada del sistema**
    
3. Click en **Variables de entorno**
    
4. En la variable llamada `Path` → haz clic en **Editar**
    
5. Agrega esta nueva ruta:
    
    makefile
    
    CopiarEditar
    
    `C:\php`
    

#### ✅ Paso 4: Verificar que funcione

1. Abre la terminal (cmd o PowerShell)
    
2. Escribe:
    
    bash
    
    CopiarEditar
    
    `php -v`
    
    Si ves algo como esto:
    
    bash
    
    CopiarEditar
    
    `PHP 8.3.9 (cli) (built: Jul 15 2025) ...`
    
    🎉 ¡PHP está listo en tu PC!
    

---

### 🧳 OPCIÓN 2: PHP portátil en pendrive

> Si no puedes instalar cosas en tu computador del trabajo, usa esta opción.

1. Crea una carpeta en tu **pendrive**, por ejemplo `php-portable`
    
2. Descarga desde:  
    👉 https://windows.php.net/download/
    
3. Descomprime en esa carpeta del pendrive
    
4. Dentro de tu terminal escribe:
    
    bash
    
    CopiarEditar
    
    `./php-portable/php.exe archivo.php`
    
    Así puedes ejecutar PHP directamente sin instalar nada.
    

---

## ⚡ OPCIÓN 3: Instalar XAMPP (la más rápida y completa)

> 🐣 **Recomendada si estás comenzando.**  
> Incluye PHP, MySQL (phpMyAdmin), y Apache en un solo programa.

---

### ✅ ¿Qué es XAMPP?

Es un **paquete todo-en-uno** que te instala:

|Software|Función|
|---|---|
|Apache|Servidor web para correr PHP|
|PHP|El lenguaje que vamos a usar|
|MySQL|Base de datos compatible con Laravel|
|phpMyAdmin|Panel web para manejar la base de datos|

---

### 🔧 Paso 1: Descargar XAMPP

1. Entra a:  
    👉 https://www.apachefriends.org/es/index.html
    
2. Elige la versión para Windows (que diga **PHP 8.2 o superior**).
    

---

### 📦 Paso 2: Instalar

1. Ejecuta el instalador
    
2. Durante la instalación, asegúrate de marcar:  
    ✅ **Apache**, ✅ **MySQL**, ✅ **phpMyAdmin** y ✅ **PHP**
    

---

### 🚀 Paso 3: Usar XAMPP

1. Abre el **Panel de Control de XAMPP**
    
2. Inicia **Apache** (y también **MySQL** si vas a usar base de datos)
    
3. Abre tu navegador y visita:  
    👉 `http://localhost`
    

Si todo va bien, verás la pantalla de bienvenida de XAMPP.

---

### 📁 ¿Dónde va el código PHP?

Coloca tus archivos `.php` dentro de la carpeta:

makefile

CopiarEditar

`C:\xampp\htdocs\`

Ejemplo:  
`C:\xampp\htdocs\hola.php`

Y luego visita en tu navegador:  
👉 `http://localhost/hola.php`

---

### 🧪 ¿Probamos?

Crea el archivo `hola.php`:

php

CopiarEditar

`<?php echo "¡Hola Nye, tu servidor PHP funciona!"; ?>`