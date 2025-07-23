# Seeders y Factories

Titular: Niko

## ✅ **¿Qué son?**

En Laravel, los **Seeders** y **Factories** son herramientas para **llenar tu base de datos automáticamente con datos de prueba**.

---

### 📦 **Seeders**

- Son **archivos PHP** que guardan **instrucciones para poblar tablas**.
- Normalmente, se usan para **crear registros específicos** que siempre quieres tener:
    
    👉 Por ejemplo: un **usuario administrador**, un **rol fijo**, o algunos **datos base**.
    
- Son útiles para **automatizar la carga inicial de datos** cada vez que reinstalas o limpias tu base.

---

### 🧑‍🌾 **Factories**

- Son **plantillas** que definen **cómo generar datos falsos o aleatorios** para un modelo (usuario, post, producto, etc.).
- Laravel usa la librería **Faker** dentro de las factories:
    - 📚 **Faker** es una herramienta que **genera datos falsos realistas**: nombres, emails, textos, direcciones…
    - Laravel **ya trae Faker incluido** por defecto cuando creas un nuevo proyecto — **no necesitas instalarlo aparte** en la mayoría de los casos.
- Gracias a Faker, puedes crear **cientos de registros falsos**, sin tener que inventarlos uno a uno.

---

## ⚙️ **¿Para qué se usan juntos?**

Seeders y Factories suelen ir **de la mano**:

- Un **Seeder** llama a una **Factory** para generar **varios registros de golpe**.
- Son clave para:
    
    ✔️ **Probar relaciones** entre tablas (usuarios con posts, pedidos con productos, etc.).
    
    ✔️ Ver **datos reales** en formularios y vistas.
    
    ✔️ Preparar **pruebas automáticas** o demostraciones del proyecto.
    

---

✅ **Resumen corto:**

- **Seeders** = Scripts que llenan tablas.
- **Factories** = Plantillas para crear datos aleatorios.
- **Faker** = El motor que inventa los datos falsos.

---

🔗 En las siguientes secciones vas a ver **cómo crearlos, ejecutarlos y combinarlos** paso a paso.

---

## [👈🏻VOLVER](Laravel%20Wiki%20Todo%20lo%20necesario%20para%20aprender%20Larav%20227d9e22edae8085a463fc5448c36870.md)

## [SIGUIENTE 👉🏻](Crear%20Seeders%20y%20Factories%20227d9e22edae8039af0dcedddb731d6e.md)