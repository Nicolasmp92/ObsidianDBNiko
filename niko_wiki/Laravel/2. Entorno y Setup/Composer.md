 🧰 Instalación de Composer

## 📌 ¿Qué es Composer?

**Composer** es el **gestor de dependencias de PHP**.  
Te permite instalar librerías y frameworks como Laravel fácilmente y mantener todo organizado en el archivo `composer.json`.

> 💡 Es similar a `npm` en Node.js o `pip` en Python.

---

## ✅ Requisitos

- Tener instalado **PHP 8.2 o superior**.
- Tener acceso a la terminal o consola del sistema.
- Para Laravel, Composer es **imprescindible**.

---

## 🖥️ Instalación paso a paso

### 🔹 Windows

1. Ve al sitio oficial:  
   👉 [https://getcomposer.org/Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe)

2. Ejecuta el instalador.

3. Cuando te pregunte por la ruta de PHP:
   - Si usas XAMPP:  
     📁 `C:\xampp\php\php.exe`

4. Termina la instalación. Composer quedará disponible globalmente en tu terminal.

5. Abre una terminal (`cmd`) y escribe:

```bash
composer --version
🔸 Si ves algo como Composer version 2.x.x, ¡está funcionando!

🔹 Linux / macOS
Ejecuta estos comandos en terminal:

bash
Copiar
Editar
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php composer-setup.php
php -r "unlink('composer-setup.php');"
Mueve el ejecutable para que sea global:

bash
Copiar
Editar
sudo mv composer.phar /usr/local/bin/composer
Verifica la instalación:

bash
Copiar
Editar
composer --version
📁 ¿Dónde se guarda Composer?
Composer se ejecuta desde terminal y crea estos dos archivos importantes:

Archivo	¿Para qué sirve?
composer.json	Lista todas las dependencias del proyecto
composer.lock	Guarda las versiones exactas instaladas

Se guardan en la raíz del proyecto, por ejemplo:

pgsql
Copiar
Editar
mi-proyecto/
├── app/
├── composer.json
├── composer.lock
├── vendor/
📦 La carpeta vendor/ contiene todas las librerías instaladas.

📥 Comandos útiles
Comando	Descripción
composer install	Instala todas las dependencias del composer.lock
composer update	Actualiza todas las dependencias a las versiones más recientes
composer require nombre/paquete	Instala una nueva librería y la agrega a composer.json
composer dump-autoload	Reconstruye las clases autoload si agregas archivos manualmente

🧪 Verificación rápida
bash
Copiar
Editar
composer --version
php --version
Ambos deben estar disponibles para usar Laravel correctamente.

🧠 Tips finales
Composer solo funciona con PHP.

Siempre usa Composer desde la carpeta del proyecto (donde esté el composer.json).

Si clonas un proyecto Laravel de GitHub, ejecuta composer install para que funcione.

🔗 Recursos
Sitio oficial: https://getcomposer.org

Guía rápida: https://getcomposer.org/doc/00-intro.md