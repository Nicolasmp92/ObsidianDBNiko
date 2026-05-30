---
status: En Aprobacion
---
GYM Paso 4 Ejecución y Tracking (User Experience)

- Rama: `feature/user-routine-execution`
    

- [x] Adaptar la vista "Mi Rutina" del usuario para que funcione bajo el modelo de "solo ejecución" (marcar como completado). ✅ 2026-05-21
    
- [x] Implementar la lógica de guardado de progreso y consulta del historial. ✅ 2026-05-21



---

#PROMPT 

Windsurf, estamos en la rama `feature/user-routine-execution`. El objetivo es conectar la vista existente de rutinas del usuario con la nueva arquitectura centralizada en el Admin.

**Tareas de Implementación:**

1. **Auditoría de la Vista Actual**:
    
    - Analiza la pantalla dentro del módulo `my_routines` donde el usuario actualmente visualiza y marca sus ejercicios como completados.
        
    - **No crees una vista nueva**. Reutiliza la UI existente (tarjetas, checkboxes, pestañas de días).
        
2. **Adaptación de la Fuente de Datos**:
    
    - Cambia la fuente de datos de esa vista. Ahora debe consumir estrictamente el endpoint `GET /routine/my-exercises` (que trae lo que el Admin le asignó).
        
    - Asegúrate de que el modelo de datos en el frontend se adapte a los cambios que hicimos recientemente (`reps` como int, `day_of_week` como int, `weight` casteado a double de forma segura).
        
3. **Lógica de Completado (Tracking)**:
    
    - Identifica la acción del checkbox o botón de 'Completar' que ya existe en la UI.
        
    - Conecta esa acción al endpoint `PATCH /routine/exercises/{id}/complete`.
        
    - Asegúrate de que el estado visual se actualice en tiempo real (ej. tachando el ejercicio) sin necesidad de recargar toda la pantalla.
        

**Objetivo**: Que la pantalla que el usuario ya conoce siga viéndose igual, pero ahora alimentada exclusivamente por el 'Plan Maestro' del Admin y sincronizada con los nuevos endpoints.