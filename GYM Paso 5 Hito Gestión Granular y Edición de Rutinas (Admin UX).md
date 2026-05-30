---
status: En Aprobacion
---
### Registro de Requerimiento - GYM Paso 5

**Hito: Gestión Granular y Edición de Rutinas (Admin UX)**

- **Rama:** `feature/admin-routine-editor`
    
- **Estado:** 🕒 Pendiente
    
- **Prioridad:** Alta (Optimización y Refinamiento Operativo)
    

#### 🎯 Objetivo

Permitir al Administrador corregir, reprogramar o eliminar ejercicios específicos ya asignados dentro de la planificación semanal de un alumno. La edición es **granular por día**, asegurando que modificar un ejercicio un lunes no altere el mismo ejercicio programado para otro día de la semana.

#### 🛠️ Especificaciones Técnicas por Instancia

### 🚀 PROMPT 1: Instancia BACKEND (Go)

"Windsurf, estamos en la rama `feature/admin-routine-editor`. Vamos a expandir el módulo de rutinas para permitir que el Admin edite y elimine asignaciones existentes.

**Tareas en el Backend:**

1. **Endpoint de Edición (PATCH)**:
    
    - Registra `r.Patch("/routine/exercises/{id}", updateUserRoutineHandler.Handle)` dentro del grupo protegido por `RequireRole(admin)`.
        
    - El handler debe leer el `id` del registro (`user_routine_exercises`) desde la URL.
        
    - Debe permitir actualizar campos de forma parcial: `series`, `reps`, `weight` y `day_of_week`.
        
2. **Endpoint de Eliminación (DELETE)**:
    
    - Registra `r.Delete("/routine/exercises/{id}", deleteUserRoutineHandler.Handle)` en el grupo de Admin.
        
    - Debe eliminar físicamente el registro correspondiente de la tabla intermedia.
        
3. **Validación**: Asegura que el `day_of_week` se mantenga restringido en el rango de 1 a 7.
    

**Objetivo**: Habilitar el control total de escritura (Update/Delete) para el rol de Administrador de manera segura y eficiente."

### 🚀 PROMPT 2: Instancia MOBILE (Flutter)

"Windsurf, estamos en la rama `feature/admin-routine-editor`. El objetivo es implementar la interfaz de edición y borrado de ejercicios desde la perspectiva del Administrador.

**Tareas en el Mobile:**

1. **Interacción y Modal (UI)**:
    
    - En la vista del Admin (`UserRoutineScreen`), haz que al tocar una tarjeta de ejercicio se despliegue un `EditExerciseSheet`.
        
    - Este modal debe precargar los valores actuales del ejercicio (`series`, `reps`, `weight`, `day_of_week`).
        
    - Añade un botón visible de 'Eliminar Ejercicio' (icono de basura) con un diálogo de confirmación.
        
2. **Lógica de BLoC**:
    
    - Agrega los eventos `UpdateUserExerciseRequested` y `DeleteUserExerciseRequested` a `AdminRoutineBloc`.
        
    - Conéctalos a los nuevos endpoints `PATCH /routine/exercises/{id}` y `DELETE /routine/exercises/{id}` respectivamente.
        
3. **Mapeo Seguro y Reactividad**:
    
    - Mantén el tipado defensivo (`(map['weight'] as num?)?.toDouble() ?? 0.0`) para el peso.
        
    - **Comportamiento Reactivo**: Al confirmar los cambios, la UI debe reflejar la actualización inmediatamente. Si el Admin cambia el día del ejercicio (ej. de Lunes a Martes), el componente debe desaparecer del bloque del lunes y renderizarse en el del martes de forma instantánea.
        

**Objetivo**: Lograr una gestión fluida en tiempo real que permita reestructurar la agenda deportiva del alumno con un par de toques."