---
status: Pendientes
---
**Hito: Tracking Real y Flexibilidad (User UX)**

- **Rama:** `feature/active-training-mode`
    
- **Estado:** 🕒 Pendiente
    

#### 🎯 Objetivo

Transformar el estado pasivo de la UI en un "Modo Concentración" real. La pantalla no debe apagarse mientras se entrena, y el usuario debe tener un cronómetro global que pueda pausarse ante cualquier interrupción en el gimnasio.

#### 🛠️ Especificaciones Técnicas

- **Gestión de Pantalla:** Implementar el paquete `wakelock_plus` para mantener la pantalla encendida (solo durante el estado activo).
    
- **Estados del `RoutineBloc`:**
    
    - Nuevo estado: `RoutinePaused`.
        
    - Nuevos eventos: `PauseRoutine` y `ResumeRoutine`.
        
- **Cronómetro Global:** Un _Timer_ en Flutter que cuente los minutos/segundos de la sesión. Al pausar, el timer se detiene y la pantalla puede volver a apagarse (liberando batería).
    
- **Reset de Ejercicios:** Al ejecutar `EndRoutine` (Terminar entrenamiento), disparar un evento que limpie visualmente el estado `isCompleted` para que al día siguiente la lista esté fresca.

---
### PROMPTS

### 🚀 PROMPT 1: Instancia BACKEND (Go)

"Windsurf, estamos en la rama `feature/active-training-mode`. Vamos a crear el endpoint necesario para cerrar y resetear la sesión de entrenamiento diaria del usuario.

**Tareas en el Backend:**

1. **Endpoint de Cierre (POST)**:
    
    - Registra `r.Post("/routine/my-exercises/finish", finishRoutineHandler.Handle)` dentro del grupo de usuarios autenticados (con middleware de autenticación normal, no Admin).
        
2. **Payload e Identificación**:
    
    - Debe recibir en el body el `day_of_week` (int).
        
    - Debe extraer el `userId` o `rut` directamente del token del usuario logueado.
        
3. **Lógica de Base de Datos (Reset)**:
    
    - En el repositorio, ejecuta un UPDATE con GORM en la tabla `user_routine_exercises`.
        
    - Condición: Donde `user_id = usuario_logueado` AND `day_of_week = day_of_week_recibido`.
        
    - Acción: Cambiar el campo `is_completed` a `false` para todos esos registros.
        

**Objetivo**: Permitir que cuando el alumno termine su día de entrenamiento, el backend limpie sus "checks" verdes para que la rutina quede fresca para la siguiente semana."

### 🚀 PROMPT 2: Instancia MOBILE (Flutter)

"Windsurf, estamos en la rama `feature/active-training-mode`. Vamos a transformar la sesión de entrenamiento en un entorno real, reactivo y con soporte para Pausas.

**Tareas en el Mobile:**

1. **Paquetes y Pantalla Activa**:
    
    - Agrega y usa `wakelock_plus`. Cuando la rutina se inicie (`StartRoutine`), activa el wakelock para mantener la pantalla encendida. Al terminar (`EndRoutine`) o pausar, desactívalo.
        
2. **Refactor de `RoutineBloc` (Manejo de Tiempo y Pausa)**:
    
    - Añade un `Timer` interno al Bloc para llevar un cronómetro global de la sesión (minutos y segundos).
        
    - Agrega los eventos `PauseRoutineRequested` y `ResumeRoutineRequested`, con sus respectivos estados `RoutinePaused` y `RoutineActive`.
        
3. **UI del Cronómetro y Control**:
    
    - En `my_routines.screen.dart`, cuando la rutina esté activa, muestra el tiempo transcurrido en tiempo real en la parte superior.
        
    - Añade botones limpios para **Pausar / Reanudar** el entrenamiento.
        
4. **Conexión Real al Terminar**:
    
    - Al presionar 'Terminar Rutina', el Bloc debe hacer un POST al nuevo endpoint `POST /routine/my-exercises/finish` enviando el día actual.
        
    - Tras el éxito de la petición, despacha `EndRoutine` de forma local y ejecuta un `FetchMyRoutines` para refrescar la UI con los checkboxes limpios.
        

**Objetivo**: Crear un modo concentración real con cronómetro, pausa para imprevistos y sincronización definitiva con el backend."