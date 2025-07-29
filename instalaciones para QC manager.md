el proyecto es laravel 11 considerar en la instalacion 
laravel recapchap 
laravel ecxel
dom pdf
image intervention
livewire v3


> 🗂️ Proyecto base Laravel 11.31 con dependencias oficiales de la empresa. Esta guía sigue el orden del `composer.json` real y contempla todos los paquetes, scripts y configuraciones implicadas.

---

## 🔧 Requisitos Previos

|Requisito|Detalles|
|---|---|
|PHP|^8.2|
|Composer|2.x|
|Node.js & npm|18.x o superior|
|MySQL|5.7+ o MariaDB|
|Git|Última versión|
|Extensiones PHP|`gd`, `mbstring`, `openssl`, etc.|

---

## 📦 Paso 1: Crear nuevo proyecto Laravel 11.31

> ⚠️ Laravel **no permite usar versiones exactas** como `11.31.*` al crear proyectos nuevos con `laravel/laravel`, ya que este paquete es solo una plantilla base.  
> La versión del framework real (`laravel/framework`) se ajusta después.

### 🛠️ Comando para crear el proyecto


```
composer create-project laravel/laravel nombre-proyecto  "11.*"
```

Luego entra a la carpeta 
```
cd nombre-proyecto
```
Este comando crea un nuevo proyecto Laravel con la versión más reciente disponible de Laravel 11 (por defecto).

---

### 🆙 (Opcional) Forzar versión específica del framework

Si quieres actualizar el framework internamente a una versión específica como `11.31`, puedes hacerlo luego:

bash

CopiarEditar
```
composer require laravel/framework:^11.31
```
✅ Esto actualiza solo el core del framework, no afecta la plantilla ni otros paquetes.

---
## 🧩 Paso 2: Instalación de dependencias

### 📦 Paquetes de producción


`# 📄 barryvdh/laravel-dompdf # Generación de documentos PDF a partir de vistas Blade. composer require barryvdh/laravel-dompdf:^3.1`


`# 🔐 biscolab/laravel-recaptcha # Integración de reCAPTCHA v2/v3 de Google para formularios seguros. composer require biscolab/laravel-recaptcha:^6.1`


`# 🖼️ intervention/image # Manipulación de imágenes (redimensionar, recortar, etc.). composer require intervention/image:2.7`


`# ⚡ livewire/livewire # Componentes dinámicos sin necesidad de usar JavaScript. composer require livewire/livewire:^3.6 -W`


`# 📊 maatwebsite/excel # Importación y exportación de archivos Excel/CSV. composer require maatwebsite/excel:^3.1`

---

### 🛠️ Paquetes de desarrollo


`# 🎲 fakerphp/faker # Generación de datos falsos para pruebas y desarrollo. composer require --dev fakerphp/faker:^1.23`


`# 🧩 laravel/breeze # Sistema básico de autenticación con Bootstrap. composer require --dev laravel/breeze:^2.3`


`# 🔍 laravel/pail # Visualizador interactivo de logs en consola. composer require --dev laravel/pail:^1.1`


`# 🧼 laravel/pint # Formateador automático de código PHP según PSR-12. composer require --dev laravel/pint:^1.13`


`# 🐳 laravel/sail # Entorno Docker oficial de Laravel. composer require --dev laravel/sail:^1.26`


`# 🔁 mockery/mockery # Framework para mocks y pruebas unitarias. composer require --dev mockery/mockery:^1.6`


`# ⚠️ nunomaduro/collision # Muestra errores y excepciones con estilo en consola. composer require --dev nunomaduro/collision:^8.1`


`# 🧪 pestphp/pest # Framework de testing con sintaxis simple y elegante. composer require --dev pestphp/pest:^3.8`


`# 🧪 pestphp/pest-plugin-laravel # Plugin para que Pest funcione perfectamente con Laravel. composer require --dev pestphp/pest-plugin-laravel:^3.2`
---

## ⚙️ Paso 3: Configuración inicial del proyecto

bash

CopiarEditar

`cp .env.example .env php artisan key:generate`

📝 Configura en `.env`:

- Base de datos (`DB_*`)
    
- Mail (`MAIL_*`)
    
- reCAPTCHA:
    
    env
    
    CopiarEditar
    
    `RECAPTCHA_SITE_KEY=tu_clave_publica RECAPTCHA_SECRET_KEY=tu_clave_secreta`
    

---

## 📁 Paso 4: Scripts automáticos post instalación

Laravel ya ejecutará automáticamente gracias a:

json

CopiarEditar

`"post-create-project-cmd": [   "@php artisan key:generate --ansi",   "@php -r \"file_exists('database/database.sqlite') || touch('database/database.sqlite');\"",   "@php artisan migrate --graceful --ansi" ]`

✅ Esto genera:

- Clave de aplicación
    
- Archivo `database.sqlite` si no existe
    
- Migraciones iniciales
    

---

## 🧠 Paso 5: Publicar assets y configs

Algunos paquetes requieren publicar archivos de configuración o vistas:

bash

CopiarEditar

`php artisan vendor:publish --provider="Barryvdh\DomPDF\ServiceProvider" php artisan vendor:publish --provider="Maatwebsite\Excel\ExcelServiceProvider" php artisan vendor:publish --provider="Biscolab\\ReCaptcha\\ReCaptchaServiceProvider"`

---

## 🌐 Paso 6: Instalar Breeze (si aplica)

bash

CopiarEditar

`php artisan breeze:install bootstrap --dark npm install && npm run build php artisan migrate`

> Breeze añade autenticación base con Bootstrap y Livewire listo para usar.

---

## 🖼️ Paso 7: Integrar Livewire

Ya instalado con `^3.6`, asegúrate de incluir en tu layout Blade principal:

blade

CopiarEditar

`<head>     @livewireStyles </head> <body>     ...     @livewireScripts </body>`

---

## 📜 Paso 8: Scripts personalizados (modo desarrollo)

Tu `composer.json` incluye este script `dev` para desarrollo:

bash

CopiarEditar

`composer run dev`

Este comando ejecuta:

- Servidor (`php artisan serve`)
    
- Cola de trabajos (`php artisan queue:listen`)
    
- Pail (logger visual)
    
- Vite con hot reload (`npm run dev`)
    

> 🧪 Usa `npx concurrently` para mostrar todo junto, con colores personalizados.

---

## 📊 Paquetes incluidos (resumen)

|Paquete|Función|
|---|---|
|**barryvdh/laravel-dompdf**|Generación de PDFs|
|**biscolab/recaptcha**|Validación reCAPTCHA de Google|
|**intervention/image**|Manipulación de imágenes|
|**maatwebsite/excel**|Importar/exportar Excel y CSV|
|**livewire/livewire**|Componentes dinámicos en tiempo real|
|**laravel/breeze**|Autenticación simple + Bootstrap|
|**laravel/pail**|Viewer de logs en consola|
|**laravel/pint**|Autoformateo de código PHP|
|**pestphp/pest**|Testing elegante con sintaxis fluida|

---

## ✅ Paso final: levantar el proyecto

bash

CopiarEditar

`php artisan serve`

y abre:

arduino

CopiarEditar

`http://localhost:8000`