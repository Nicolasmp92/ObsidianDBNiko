# 🌍 Wiki — Instalación y configuración de Lang en Laravel

## 📌 1. ¿Qué es `lang` en Laravel?

Laravel incluye un sistema de **localización** que permite mostrar textos en diferentes idiomas.  
Ejemplo: mostrar `"Login"` en inglés o `"Iniciar sesión"` en español, según la configuración.

---

## 📌 2. Instalación

Instala el paquete de traducciones con Composer:
```
composer require laravel-lang/common
```
Luego revisa la lista de idiomas en la página oficial:  
🔗 [Laravel Lang — Locales disponibles](https://laravel-lang.com/available-locales-list.html#lists-available-locales-so)

Selecciona el idioma que quieras configurar:
```
	# Para español 
	php artisan lang:add es  
	
	# Para inglés 
	php artisan lang:add en
```
---

## 📌 3. Configuración

En el archivo `.env` define los locales:

```
APP_LOCALE=es 
APP_FALLBACK_LOCALE=en 
APP_FAKER_LOCALE=es_ES
```

👉 `APP_FALLBACK_LOCALE` sirve como idioma de respaldo.  
👉 `APP_FAKER_LOCALE` define el idioma de los datos falsos generados por `faker`.

---

## 📌 4. Uso en Blade

En las vistas puedes llamar traducciones con `__()`:

`{{ __('Login') }} {{ __('auth.failed') }}`

Ejemplo de `resources/lang/es/auth.php`:

```
return [     
	'failed' => 'Estas credenciales no coinciden con nuestros registros.',             'password' => 'La contraseña es incorrecta.', 
	];`
```
---

✅ Con esto ya tienes tu Laravel listo para trabajar en múltiples idiomas.