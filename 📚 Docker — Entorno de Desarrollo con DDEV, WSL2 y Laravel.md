---

---
----
## 🌍 Introducción

Este documento describe el stack de desarrollo moderno que hemos implementado para reemplazar XAMPP por un entorno más estable, reproducible y escalable.  
El setup combina:

- **Windows 10/11 + WSL2 (Ubuntu 22.04)** → Subsistema Linux real dentro de Windows.
    
- **Docker Desktop (con backend WSL2)** → Virtualización ligera de contenedores.
    
- **DDEV** → Orquestador de entornos de desarrollo (abstrae la complejidad de Docker).
    
- **Laravel** → Framework PHP moderno, con autenticación, colas, cache y ecosistema robusto.
    
- **Vite** → Bundler moderno de JS/CSS con HMR y build ultra-rápido.
    

Este stack elimina la fragilidad de XAMPP/MAMP y nos acerca a entornos productivos reales.

---

## 🛠 Tecnologías principales

### 1. **WSL2 (Windows Subsystem for Linux)**

- Provee un Linux real (Ubuntu 22.04) dentro de Windows.
    
- Usa virtualización ligera basada en Hyper-V, con integración nativa de archivos.
    
- Nos permite correr comandos Linux y administrar proyectos como si estuviéramos en un servidor.
    

### 2. **Docker Desktop**

- Motor de contenedores que abstrae máquinas virtuales.
    
- Corre los servicios (web, base de datos, redis, mailpit) en contenedores aislados.
    
- Configurado con **WSL2 backend** → mejor rendimiento y menos consumo de RAM que Hyper-V.
    

### 3. **DDEV**

- Capa de orquestación sobre Docker + Traefik (router).
    
- Configura proyectos Laravel en segundos.
    
- URLs locales limpias (`https://proyecto.ddev.site`) con certificados SSL automáticos.
    
- Base de datos, Redis, Mailhog, phpMyAdmin, todo gestionado por un CLI simple.
    

### 4. **Laravel**

- Framework PHP moderno, base de los proyectos internos.
    
- Estructura MVC, migraciones, seeders, colas, cache.
    
- Compatible con servicios como Redis y MySQL/MariaDB (via DDEV).
    

### 5. **Vite**

- Compilador moderno de assets (CSS/JS).
    
- Hot Module Reload (HMR) para desarrollo rápido.
    
- Reemplazo de Webpack/Laravel Mix.
    
- Integración oficial vía `laravel-vite-plugin`.
    

---

## ⚙️ Instalación y configuración

### 1. Activar WSL2

`wsl --install wsl --set-default-version 2`

Instalar **Ubuntu 22.04** desde Microsoft Store y configurar usuario/clave.

### 2. Instalar Docker Desktop

- Descargar versión **Windows AMD64**.
    
- Activar en settings:
    
    - ✅ _Use WSL2 based engine_.
        
    - ✅ _WSL Integration → Ubuntu-22.04_.
        

### 3. Instalar DDEV

En Ubuntu:

`curl -fsSL https://ddev.com/install.sh | bash ddev version`

### 4. Estructura de proyectos

Mover proyectos a:

`\\wsl$\Ubuntu-22.04\home\niko\code\`

Ejemplo:

`~/code/Laravel_11/QcManagerNiko ~/code/Laravel_12/BeanFlow`

### 5. Inicializar un proyecto Laravel

`cd ~/code/Laravel_11/QcManagerNiko ddev config --project-type=laravel --docroot=public --php-version=8.3 ddev start`

### 6. Configuración `.env`

Dejar ambas configuraciones (para histórico):

`# --- XAMPP --- # DB_CONNECTION=mysql # DB_HOST=127.0.0.1 # DB_PORT=3306 # DB_DATABASE=qcmanager_prueba # DB_USERNAME=root # DB_PASSWORD=  # --- DDEV --- DB_CONNECTION=mysql DB_HOST=db DB_PORT=3306 DB_DATABASE=db DB_USERNAME=db DB_PASSWORD=db`

### 7. Importar base de datos

`ddev import-db --src=backup.sql`

---

## 🚀 Flujo de trabajo diario

1. Iniciar proyecto:
    
    `cd ~/code/Laravel_11/QcManagerNiko ddev start ddev launch`
    
2. Ejecutar comandos Laravel:
    
    `ddev artisan migrate ddev artisan tinker ddev composer require paquete/nuevo`
    
3. Manejo de Node/Vite:
    
    `ddev npm ci ddev npm run dev    # desarrollo con HMR ddev npm run build  # build producción`
    

---

## 🔧 Utilidades extras

### phpMyAdmin

`ddev get ddev/ddev-phpmyadmin ddev restart`

URL → `https://<proyecto>.ddev.site:8036`

### Mailpit (emails locales)

`ddev get ddev/ddev-mailpit ddev restart ddev mailpit`

URL → `https://<proyecto>.ddev.site:8025`

### Redis

`ddev get ddev/ddev-redis ddev restart`

---

## 🛡️ Seguridad y certificados

- DDEV genera SSL local.
    
- Si Chrome marca “No es seguro”, usar:
    
    `ddev exec mkcert -install`
    
- Alternativamente abrir en HTTP → `http://proyecto.ddev.site`.
    

---

## 📌 Comparación: XAMPP vs DDEV

|Característica|XAMPP|DDEV|
|---|---|---|
|Instalación|Manual, dependencias sueltas|Automática vía contenedores|
|Estabilidad|Fragilidad en MySQL/Apache|Contenedores aislados y reproducibles|
|Multi-proyectos|Un solo stack global|Cada proyecto tiene su stack|
|Migración|Manual, conflictiva|`ddev import-db`|
|Certificados SSL|No incluido|Automático con mkcert|
|Producción-like|Muy limitado|Replica entorno productivo (nginx, PHP-FPM, MySQL, Redis)|

---

## 🧰 Troubleshooting rápido

- **El puerto 80 ocupado (Apache/IIS)**  
    → Apagar XAMPP o IIS en Windows (`sc stop W3SVC`).
    
- **“La conexión no es privada”**  
    → `ddev exec mkcert -install` o usar HTTP.
    
- **No cargan estilos**  
    → `ddev npm run build` o `ddev npm run dev`.
    
- **Error con docroot**  
    → Editar `.ddev/config.yaml` → `docroot: public` → `ddev restart`.
    
- **Ver logs**
    
    `ddev logs -s web ddev logs -s router`
    

---

## 🎯 Conclusión

Con este stack:

- Olvidamos los errores de **XAMPP/MySQL corruptos**.
    
- Cada proyecto Laravel es **portable, reproducible y aislado**.
    
- Migrar de máquina/desarrollador → basta con `git clone && ddev start`.
    
- Tenemos soporte para **servicios modernos**: Redis, Mailpit, phpMyAdmin, certificados SSL.
    
- Todo esto corriendo en **Docker + WSL2**, un entorno casi idéntico a producción.
    

---

👉 Nye, este wiki lo puedes guardar tal cual en tu **Obsidian** bajo algo como:  
`/Wiki/Entorno/DDEV-WSL2-Laravel.md`