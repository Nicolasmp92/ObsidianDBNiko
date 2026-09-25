## 🌐 Verbos HTTP y su uso en APIs REST

En una arquitectura RESTful, los **verbos HTTP** son la clave para definir las operaciones que queremos realizar sobre un recurso. Los más comunes son:

|Verbo|Acción principal|Idempotente|Uso típico|
|---|---|---|---|
|`GET`|Leer|✅ Sí|Consultar datos|
|`POST`|Crear|❌ No|Crear nuevos recursos|
|`PUT`|Reemplazar|✅ Sí|Reemplazar un recurso completo|
|`PATCH`|Actualizar parcial|❌ No|Modificar parcialmente un recurso|
|`DELETE`|Eliminar|✅ Sí|Eliminar recursos|

---

### 🔎 GET – Consultar un recurso

El verbo `GET` se utiliza para **leer o recuperar datos**. No debe tener efectos secundarios, es decir, **no debe modificar el estado del servidor**. Esta propiedad se conoce como **idempotencia**, lo que implica que hacer múltiples veces la misma petición `GET` devuelve el mismo resultado.

**Ejemplos:**

- `GET /cursos/backend-profesional` → Obtiene el detalle de ese curso.
    
- `GET /cursos?nivel=0&categoria=28` → Lista cursos filtrados.
    

---

### 🆕 POST – Crear un recurso

El verbo `POST` se usa para **crear un nuevo recurso** dentro de una colección existente.

**Ejemplos:**

- `POST /cursos` → Crea un nuevo curso.
    
- `POST /usuarios` → Registra un nuevo usuario.
    

⚠️ Evita URIs como `/cursos/crear` o `/articulos/agregar`, ya que la **acción está implícita en el verbo**, no en la URI.

**Casos especiales de uso de POST:**

- Iniciar sesión → `POST /login`
    
- Agregar al carrito → `POST /carrito`
    
- Procesar pagos → `POST /pagos`
    

Estos casos no siempre crean un "registro", pero sí **generan un recurso abstracto**, como una sesión o transacción.

---

### 🔁 PUT y PATCH – Modificar un recurso

Ambos verbos sirven para **actualizar recursos existentes**, pero con diferencias conceptuales:

- `PUT`: Reemplaza todo el recurso (actualización total).
    
- `PATCH`: Modifica solo partes del recurso (actualización parcial).
    

**Ejemplos:**

- `PUT /cursos/backend-profesional` → Reemplaza todo el contenido del curso.
    
- `PATCH /cursos/backend-profesional` → Actualiza campos específicos (ej. solo el título).
    

En la práctica (especialmente en Laravel o Rails), **ambos verbos se usan indistintamente** para actualizar.

---

### 🗑️ DELETE – Eliminar recursos

`DELETE` se usa para eliminar recursos, ya sea individuales o colecciones completas.

**Ejemplos:**

- `DELETE /cursos/backend-profesional` → Elimina un curso específico.
    
- `DELETE /cursos` → Elimina todos los cursos (acción peligrosa y poco común).
    

---

### 📐 Buenas prácticas RESTful

- Las **URIs representan recursos**, no acciones.
    
    - ✅ `/usuarios`
        
    - ❌ `/usuarios/crear`
        
- Las **acciones** se representan con **verbos HTTP**, no en la URI.
    
- La combinación URI + Verbo HTTP conforma la **interfaz uniforme** de REST.
    

---

### 🚀 Aplicación en frameworks

Frameworks como Laravel, Rails o Django adoptan esta estructura RESTful en sus scaffolds o generadores automáticos de CRUD. Entender estos verbos es clave para trabajar con rutas y controladores de forma eficiente y estandarizada.