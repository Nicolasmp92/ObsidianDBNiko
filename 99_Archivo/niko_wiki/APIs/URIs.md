## ¿Qué son las URIs en REST?

Una **URI** (_Uniform Resource Identifier_, o Identificador Uniforme de Recursos) es la forma estándar de **identificar un recurso** dentro de una API RESTful. Las URIs forman parte fundamental de la arquitectura REST, ya que **representan los recursos con los que interactuamos**.

En otras palabras:

> Una URI es la dirección a la que enviamos una solicitud para consultar, crear, modificar o eliminar un recurso.

---

### 🧱 Estructura de una URI RESTful

text

CopiarEditar

									`https://api.ejemplo.com/usuarios/42         └────┬────┘ └───────┬────────┘ 						Dominio        Recurso`

- `https://api.ejemplo.com` → dominio o base URL de la API.
    
- `/usuarios` → colección de recursos.
    
- `/usuarios/42` → recurso individual con ID 42.
    

---

### 📐 Buenas prácticas RESTful con URIs

1. ✅ **Las URIs deben representar recursos, no acciones**
    
    ❌ Incorrecto:
    
    h
    
    CopiarEditar
    
    `POST /usuarios/crear GET  /productos/editar`
    
    ✅ Correcto:
    
    http
    
    CopiarEditar
    
    `POST /usuarios         → Crear nuevo usuario PUT /productos/32      → Editar producto con ID 32`
    
    👉 _La acción se indica con el verbo HTTP (POST, PUT, DELETE...), no en el nombre de la URI._
    

---

2. ✅ **Usa sustantivos, no verbos en URIs**
    
    Las URIs deben describir **qué es** el recurso, no lo que se va a hacer.
    
    - ✅ `/tareas`
        
    - ❌ `/obtenerTareas`, `/borrarTarea`
        

---

3. ✅ **Las URIs deben ser en plural para colecciones**
    
    - ✅ `/libros` → colección de libros
        
    - ✅ `/libros/1` → libro individual
        
    - ❌ `/libro/1` (menos común, aunque técnicamente válido)
        

---

4. ✅ **Evita estructuras anidadas innecesarias**
    
    Úsalas solo si existe una relación jerárquica real.
    
    - ✅ `/usuarios/42/direcciones` → Direcciones del usuario 42
        
    - ❌ `/usuarios/42/crearDireccion`
        

---

### 🔄 La fórmula RESTful

|Verbo HTTP|URI|Acción|
|---|---|---|
|GET|`/usuarios`|Obtener todos los usuarios|
|GET|`/usuarios/5`|Obtener el usuario con ID 5|
|POST|`/usuarios`|Crear un nuevo usuario|
|PUT|`/usuarios/5`|Reemplazar al usuario 5|
|PATCH|`/usuarios/5`|Modificar parcialmente al usuario 5|
|DELETE|`/usuarios/5`|Eliminar al usuario 5|

---

### 🧭 URI + Verbo HTTP = Interfaz Uniforme REST

REST promueve una interfaz uniforme donde:

- Las URIs representan _el qué_ (el recurso)
    
- Los verbos HTTP representan _el cómo_ (la acción)
    

Esto hace que las APIs REST sean:

- Predecibles
    
- Fáciles de entender
    
- Estándar para cualquier desarrollador