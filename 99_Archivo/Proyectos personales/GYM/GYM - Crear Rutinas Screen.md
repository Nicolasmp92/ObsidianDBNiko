---
status: En Aprobacion
---
---

# Proximos features (solicitud de jefatura o historia):

1.- Hacer screen de rutina por usuario en ADMIN (users -> rutinas). 
Que se muestre parecido a nutrición donde se puede activar o desactivar si el usuario tiene rutinas o no. (Se supone que el usuario si paga más, tiene rutina y esto lo activa el admin). 

Primer paso, mistrar el título del usar y el switch como lo tiene nutricion. 

Ese es el primer PR. 

El segundo PR, sería añadir rutina personalizada al usuario. 
* Que se muestre como el de nutrición, en vez de plan de nutrición, plan de rutina:

*Para tener en consideración a futuro: El usuario si tiene activo por el adminlas rutinas, puede ver en el menú de navegación el icono de rutinas y puede hacerlas y tener el historial de rutinas


---

# Desarrollo del requerimiento atravez de gemini.


### 🟢 Etapa 1: Preparación del Terreno (Backend)

Antes de que el Admin pueda apretar un botón, el sistema debe saber qué es ese botón.

- **BD:** Agregar el campo `has_routine` (booleano) a la tabla de usuarios.
    
- **Seeder:** Actualizar los usuarios de prueba para que algunos tengan rutina y otros no (para testear).
    
- **API:** Crear un endpoint `PATCH /users/{id}/routine-status` que solo reciba el nuevo estado del switch.
    
- **DTO:** Asegurarnos de que cuando el Admin pida la lista de usuarios, el JSON incluya si tienen rutina o no.
    

### 🟡 Etapa 2: La "Cáscara" Visual (Frontend)

Aquí es donde creamos la interfaz siguiendo el estilo del módulo de Nutrición que ya conoces.

- **Entity:** Agregar `hasRoutine` al modelo de `User` en Flutter.
    
- **Repository:** Crear la función para llamar al nuevo endpoint PATCH.
    
- **UI - Listado:** En la lista de usuarios de Admin, añadir un indicador visual (un icono pequeño de pesas, por ejemplo) si el usuario tiene rutina activa.
    
- **UI - Detalle:** Crear la pantalla donde aparecerá el **Switch**. Debe ser una copia funcional de la de nutrición: Título del usuario + Switch de activación.
    

### 🔴 Etapa 3: Lógica y Permisos (El "Candado")

Esto es lo que hace que la app sea inteligente.

- **Bloc:** Manejar el estado del switch. Mientras la API responde, el switch debe mostrar un estado de carga o estar deshabilitado para evitar múltiples clicks.
    
- **Navegación Dinámica:** Aquí es donde ocurre la magia:
    
    - Si `hasRoutine` es `true`, el usuario ve el icono de Rutinas en su menú inferior.
        
    - Si es `false`, el icono desaparece o muestra un mensaje de "Contacta a tu Admin para activar este plan".
        

---

### 📝 Resumen del primer PR (El "MVP")

Tu meta para el primer Pull Request es: **"Que el Admin pueda entrar a un usuario, mover un Switch, y que ese cambio se guarde en la BD"**. Nada más. Sin ejercicios, sin planes complejos aún. Solo el permiso.

### ¿Cómo lo ves, Niko?

Si estás de acuerdo con este orden:

1. **¿Empezamos con el Backend?** (Migración de BD y nuevo endpoint PATCH).
    
2. **¿O prefieres maquetar primero el Switch en Flutter?**
    

Dime cuál es el primer paso que quieres dar y te doy los prompts para **Windsurf**. ¡Vamos por ese nuevo feat!