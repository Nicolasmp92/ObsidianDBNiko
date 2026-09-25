# 🌐 ¿Qué es una API REST o RESTful?

## 📘 Definición general

Una **API REST** (o **RESTful API**) es un tipo de interfaz que permite que **dos sistemas se comuniquen entre sí** a través del protocolo HTTP, siguiendo los principios definidos por el estilo arquitectónico REST (_Representational State Transfer_).

Dicho de forma simple:

> Una API REST permite a distintas aplicaciones hablar entre sí usando peticiones HTTP (GET, POST, PUT, DELETE…) con reglas claras, ordenadas y predecibles.

---

## 🧠 ¿Qué significa REST?

**REST** no es un estándar, sino un _estilo de arquitectura_ para el diseño de sistemas distribuidos, propuesto por **Roy Fielding** en su tesis doctoral (2000).

### 🔑 Principios fundamentales de REST

|Principio|Descripción breve|
|---|---|
|**Cliente-servidor**|Separación entre la interfaz del cliente y la lógica del servidor.|
|**Sin estado**|Cada solicitud HTTP debe contener toda la información necesaria (no guarda sesión).|
|**Cacheable**|Las respuestas pueden ser cacheadas si es posible.|
|**Interfaz uniforme**|Toda la comunicación se hace usando una interfaz común basada en recursos y verbos HTTP.|
|**Sistema en capas**|El cliente no necesita saber si está hablando con el servidor o con intermediarios.|
|_(Opcional)_ **Código bajo demanda**|Permite que el servidor envíe código ejecutable (como scripts) al cliente.|

---

## 🔗 ¿Y qué significa que sea RESTful?

El término **RESTful** se refiere a una API que **sigue fielmente los principios REST**. Es una API bien estructurada, coherente y alineada con las buenas prácticas de diseño REST.

**✅ Una API RESTful hace lo siguiente:**

- Usa verbos HTTP correctamente (GET, POST, PUT, DELETE…)
    
- Usa URIs que representan recursos (`/usuarios`, `/productos/42`)
    
- Devuelve respuestas en formatos comunes como JSON o XML
    
- Es predecible, limpia y fácil de consumir por otros sistemas
    

**❌ Una API no RESTful podría:**

- Usar `POST` para todo (incluso para consultar)
    
- Usar URLs como `/crearUsuario`, `/borrarProducto?id=2`
    
- Incluir estado de sesión (no cumple el principio stateless)
    

---

## 🛠️ ¿Dónde se usa una API REST?

Una API REST es ideal para conectar:

- Aplicaciones web con servidores
    
- Aplicaciones móviles con backend
    
- Sistemas externos con tu sistema
    
- Microservicios entre sí
    

**Ejemplo real:**

http

CopiarEditar

`GET https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6`

👉 Devuelve los datos del artista Avicii desde la API RESTful de Spotify.

---

## 🎯 Ventajas de usar REST

✅ Estándar y entendible  
✅ Escalable  
✅ Multiplataforma  
✅ Usa HTTP, que es ampliamente soportado  
✅ Funciona bien con JSON, ideal para frontends modernos