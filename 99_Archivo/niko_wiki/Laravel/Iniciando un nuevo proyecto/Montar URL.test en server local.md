# 🌐 Usar dominios locales `.test` en Laravel

## 🧾 Introducción

Cuando desarrollamos una aplicación Laravel de forma local, normalmente accedemos a ella mediante una URL como:
```
http://localhost:8000
```
Sin embargo, esto puede volverse incómodo cuando trabajamos con múltiples proyectos, entornos, o queremos simular un entorno de producción.

Por eso, podemos configurar un **dominio local personalizado** como:


```yalm
http://tudominio.test
```


Esto se logra redirigiendo el nombre de dominio a nuestro propio computador (localhost) mediante el archivo `hosts` de Windows y, opcionalmente, un servidor como Apache o Laravel Sail.

---

## 🎯 ¿Para qué sirve?

- Acceder a tu proyecto Laravel desde una URL **más legible y profesional**.
- Simular un entorno **más cercano al real**, como `https://miempresa.test`.
- Configurar **múltiples proyectos Laravel** sin que se mezclen puertos (`:8000`, `:8001`, etc).
- Probar funcionalidades como **redirecciones, subdominios, cookies, HTTPS**, etc.

---

## ✅ Ventajas

- ✅ Puedes usar nombres fáciles de recordar.
- ✅ Te da flexibilidad para probar cosas como cookies de sesión por dominio.
- ✅ Ideal para equipos que comparten estructuras y proyectos.

---

## ⚠️ Desventajas

- ⚠️ Requiere acceso de administrador para editar `hosts`.
- ⚠️ Si no se configura bien, puede causar confusión o conflictos con DNS reales.
- ⚠️ Solo funciona en tu equipo local, **no se ve desde otros dispositivos**.

---

## 🧭 Paso 1: Configurar archivo `hosts` en Windows

1. Abre **Bloc de notas como administrador**.
2. Abre este archivo:
```
C:\Windows\System32\drivers\etc\hosts
```
3. Agrega esta línea:
```yaml
127.0.0.1 tudominio.test
```

> Reemplaza `tudominio.test` por lo que desees, como `miapp.test`, `qcmanager.test`, etc.

---

## 🛠️ Paso 2: Configurar tu servidor local

### 🔸 Opción A: Usando XAMPP (Apache)

Editar:
```
C:\xampp\apache\conf\extra\httpd-vhosts.conf
```

Agregar:

```apache
<VirtualHost *:80>
    ServerName tudominio.test
    DocumentRoot "C:/xampp/htdocs/mi-proyecto/public"

    <Directory "C:/xampp/htdocs/mi-proyecto/public">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
Reiniciar Apache.
```
---
🔸 Opción B: Usando Laravel Sail

En .env:
```ini
APP_URL=http://tudominio.test
```

En hosts:
```ini
127.0.0.1    tudominio.test
```

Levantar Sail:
```
./vendor/bin/sail up
```
🔸 Opción C: Usando php artisan serve
```bash
php artisan serve --host=tudominio.test --port=8000

// o solo usar 

php artisan serve
```
Acceder desde:

```
http://tudominio.test:8000

// respectivamente 

http://localhost:8000/
```
🧪 Verificación

Abre el navegador y ve a:
```
http://tudominio.test     o    http://localhost:8000/
```
Si todo está bien configurado, deberías ver tu app cargando correctamente.

🧼 Solución si no carga
Vaciar caché DNS:
```bash
ipconfig /flushdns
```