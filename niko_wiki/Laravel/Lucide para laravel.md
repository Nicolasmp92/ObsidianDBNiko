# 📌 Wiki — Instalación de Lucide Icons en Laravel

## 1. Instalación

Instala el paquete vía Composer:

```
composer require mallardduck/blade-lucide-icons
```
Esto integra el set completo de íconos **Lucide** en Blade.

---

## 2. Uso en Blade

Los íconos se pueden usar como componentes Blade de cierre automático que se compilarán en íconos SVG:

```html
<x-lucide-activity />
```

También puedes pasar clases a tus componentes de icono:

```html
<x-lucide-album class="w-6 h-6 text-gray-500"/>
```

E incluso utiliza estilos en línea:

```html
<x-lucide-anchor style="color: #555"/>
```

Los íconos sólidos se pueden referenciar de la siguiente manera:

```html
<x-lucide-bike />
```

### Iconos SVG sin procesar

Si desea utilizar los íconos SVG sin procesar como activos, puede publicarlos usando:

```shell
php artisan vendor:publish --tag=blade-lucide-icons --force
```

Luego úsalos en tus vistas como:

```html
<img src="{{ asset('vendor/blade-lucide-icons/cloud-moon.svg') }}" width="10" height="10"/>
``````



---

## 3. Caché de íconos (opcional)

Para mejorar rendimiento en producción:

```
# Genera cache de íconos 
php artisan icons:cache   

 # Limpia cache
php artisan icons:clear  
```
---

✅ Con esto ya puedes usar cualquier ícono de Lucide.dev directamente en tus vistas Blade.