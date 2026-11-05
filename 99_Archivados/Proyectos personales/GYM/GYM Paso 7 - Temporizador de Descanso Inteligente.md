---
status: Pendientes
---
**Hito: Recuperación Guiada (User UX)**

- **Rama:** `feature/rest-timer`
    
- **Estado:** 🕒 Pendiente
    

#### 🎯 Objetivo

Automatizar el cálculo del descanso. Cuando el usuario termina una serie de un ejercicio duro, no debería tener que adivinar cuándo volver a empezar.

#### 🛠️ Especificaciones Técnicas

- **UI/UX:** Un cronómetro regresivo flotante o integrado en la tarjeta del ejercicio (ej. 90 segundos).
    
- **Interacción:** Al presionar "Completar Ejercicio", se dispara automáticamente el temporizador.
    
- **Flexibilidad (La regla de oro):** El usuario debe poder saltar el descanso (botón "Skip") o sumar/restar tiempo (+30s / -30s) si el equipo está ocupado o se siente recuperado antes.
    
- **Feedback:** Vibración sutil del teléfono al finalizar el tiempo (usando el paquete `haptic_feedback`).




---
### PROMPTS


### 🚀 PROMPT: Instancia MOBILE (Flutter)

"Windsurf, estamos en la rama `feature/rest-timer`. Vamos a implementar un temporizador de descanso inteligente para el usuario tras completar un ejercicio.

**Tareas de Implementación:**

1. **Dependencias:**
    
    - Añade el paquete `haptic_feedback` (o `vibration`) a `pubspec.yaml` para dar respuesta táctil.
        
2. **Lógica de Estado (`RoutineBloc`):**
    
    - Añade variables al estado: `isResting` (bool) y `restSecondsRemaining` (int).
        
    - Crea eventos: `StartRestTimer` (inicia con 90 segundos por defecto), `StopRestTimer` (cancela/salta el descanso), y `AdjustRestTime` (recibe un int para sumar o restar segundos).
        
    - Usa un `Timer` independiente para este conteo regresivo.
        
3. **Trigger Automático:**
    
    - En la lógica de la pantalla, cuando el usuario presione el checkbox para completar un ejercicio (y el `ToggleExerciseCompletion` sea exitoso), dispara automáticamente el evento `StartRestTimer(90)`.
        
4. **UI del Temporizador (Reactiva y no intrusiva):**
    
    - Muestra un banner inferior flotante (o un `BottomSheet` persistente pero que no bloquee la pantalla) cuando `isResting` sea `true`.
        
    - La UI debe mostrar: el tiempo regresivo grande, un botón de `+30s`, un botón de `-30s`, y un botón de `Saltar` (Skip).
        
5. **Feedback Final:**
    
    - Cuando el contador llegue a `0`, dispara una vibración sutil, cierra el banner y emite `StopRestTimer`.
        

**Objetivo:** Que el usuario tenga un asistente automático que le avise cuándo volver a levantar las pesas, con total flexibilidad para ajustar el tiempo."






---
![[Pasted image 20260527115310.png]]


ojo si se elimina el dia 1 el dia no se puede ejecutar por falta del dia anteriro
como propuesta se trabajara solo por numeros, sin lunes martes etc, esto permite partir el dia 1 por ejemplo en cualquier dia de la semana, 

por ejemplo si parto el dia 1 el domingo el lunes deberia recetear



ERROR 
al agregar un dia nuevo no se actualiza el listado automanticamente: