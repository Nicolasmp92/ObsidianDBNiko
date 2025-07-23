# Estructura de carpetas

Titular: Niko

<aside>
💡

👉 Laravel utiliza una estructura de directorios organizada y coherente, pensada para facilitar un desarrollo rápido, escalable y fácil de mantener. Aquí tienes un recorrido por cada componente principal:

</aside>

### 📁 Directorios del Nivel Raíz

- **`app/`** — Contiene el código principal de la aplicación, como modelos, controladores, middleware, eventos, jobs, etc.
- **`bootstrap/`** — Incluye archivos de arranque del framework y la caché de configuración.
- **`config/`** — Guarda todos los archivos de configuración de la aplicación (base de datos, mail, auth, etc).
- **`database/`** — Aquí viven migraciones, seeders y factories para poblar la base de datos.
- **`public/`** — Es el punto de entrada web (`index.php`) y guarda archivos públicos: CSS, JS, imágenes.
- **`resources/`** — Contiene vistas Blade, assets sin compilar (SASS, JS) y archivos de idioma.
- **`routes/`** — Define todas las rutas de la aplicación, separadas por contexto.
- **`storage/`** — Guarda logs, cachés, archivos generados o subidos por usuarios.
- **`tests/`** — Contiene tests automáticos escritos con PHPUnit o Pest.
- **`vendor/`** — Contiene las dependencias instaladas con Composer. Nunca se modifica a mano.

### 📂 Dentro de `app/`

Este directorio aloja casi toda la lógica de tu aplicación, organizada por responsabilidad:

- **`Http/`** — Controladores, middleware y Requests para gestionar las solicitudes HTTP.
- **`Models/`** — Modelos Eloquent que representan tablas de la base de datos.
- **`Providers/`** — Proveedores de servicios que configuran y arrancan la aplicación.
- **`Console/`** — Comandos personalizados de Artisan.
- **`Exceptions/`** — Manejadores de excepciones personalizadas.
- **`Events/`** — Eventos del sistema que puedes disparar.
- **`Listeners/`** — Clases que escuchan y responden a eventos.
- **`Jobs/`** — Tareas que se pueden encolar o ejecutar en segundo plano.
- **`Mail/`** — Clases para crear correos electrónicos.
- **`Notifications/`** — Notificaciones para email, SMS, Slack, etc.
- **`Policies/`** — Políticas de autorización para controlar permisos.
- **`Rules/`** — Reglas de validación personalizadas.

### 🗂️ Directorios de Rutas

Laravel organiza las rutas en archivos separados para mayor claridad:

- **`routes/web.php`** — Rutas web con soporte de sesiones, CSRF, etc.
- **`routes/api.php`** — Rutas para APIs sin estado (normalmente devuelven JSON).
- **`routes/console.php`** — Define comandos de consola usando closures.
- **`routes/channels.php`** — Define canales de Broadcasting para websockets.

## **📂 Directorios convencionales (no vienen por defecto)**

Además de las carpetas **core**, muchos proyectos Laravel crean carpetas **opcionales** para **organizar mejor** la estructura. No son obligatorias, pero ayudan a **mantener limpio** el proyecto.

---

### ### 📌 **Ejemplos comunes**

- **`resources/views/layouts/`**
    - Contiene **layouts base** de Blade, como `app.blade.php` o `master.blade.php`.
    - Ejemplo: `layouts/app.blade.php`.
- **`resources/views/partials/`**
    - Guarda **fragmentos reutilizables**: header, footer, navbars, alerts.
    - Ejemplo: `partials/navbar.blade.php`.
- **`resources/views/components/`**
    - Componentes Blade (`<x-alert>`, `<x-button>`).
    - Laravel recomienda separarlos para reutilizarlos en vistas.
- **`resources/views/emails/`**
    - Plantillas Blade para correos (`welcome.blade.php`, `reset-password.blade.php`).
- **`app/Helpers/`**
    - Clases o funciones helper personalizadas.
    - No existe por defecto; se crea manualmente.
- **`app/Services/`**
    - Lógica específica de negocio (cálculos, integraciones externas).
    - Ayuda a separar lógica compleja de los controladores.
- **`app/Traits/`**
    - Traits PHP reutilizables.
    - Útil para compartir lógica entre clases.
- **`app/Repositories/`**
    - Implementa el patrón **Repository** para separar la lógica de acceso a datos.
    - Opcional pero común en proyectos grandes.

---

### ### ⚙️ **Clave**

📌 Laravel **no te obliga** a usar estos directorios, pero la comunidad los adopta porque:

- Mejoran la organización.
- Hacen el código **más limpio**.
- Facilitan la reutilización.

Laravel no necesita configuración extra: si existen, los carga igual.

### ⚙️ Flujo de Trabajo de Desarrollo

Laravel promueve un flujo de trabajo limpio y eficiente:

- Genera componentes con Artisan: `php artisan make:controller`, `make:model`, `make:migration`…
- Define rutas en `routes/`.
- Desarrolla la lógica en controladores, modelos y middlewares.
- Diseña interfaces con vistas Blade en `resources/views/`.
- Gestiona la base de datos con migraciones y seeders.

✅ Esta estructura bien definida hace que proyectos chicos o grandes sean fáciles de escalar y mantener. Laravel combina flexibilidad y organización, adaptándose a cada necesidad real.

📌 Tip extra: Si alguna carpeta no la usas aún (por ejemplo, `Listeners` o `Mail`), no pasa nada. Laravel la crea cuando la necesites, usando `php artisan make:*`.

---

## [👈🏻VOLVER](Instalacio%CC%81n%20Paso%20a%20Paso%20227d9e22edae8115b4aec54d81524445.md)

## [SIGUIENTE 👉🏻](Archivo%20env%20y%20Configuracio%CC%81n%20227d9e22edae80d98531e145b1c42401.md)