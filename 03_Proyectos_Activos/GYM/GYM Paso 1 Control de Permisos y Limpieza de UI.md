---
status: En Aprobacion
---
- Rama: `feature/routine-permissions-ui`
    

- [x] **Eliminar** de raíz los botones de creación de rutinas y ejercicios en la vista del usuario final (evitar código muerto). ✅ 2026-05-15
    
- [x] Implementar el "Candado de Navegación": el ícono de rutinas solo debe ser visible si `IsRoutineEnabled` es `true`. ✅ 2026-05-15
    
- [x] En la `UserRoutineScreen` del Admin, habilitar el punto de entrada (botón o acceso) para la futura gestión de ejercicios. ✅ 2026-05-15


  ---

#PROMPT 
Windsurf, vamos a trabajar en la rama `feature/routine-permissions-ui`. El objetivo es restringir las capacidades de creación del usuario sin eliminar definitivamente el código, centralizando el control en el Admin.

**Tareas:**

1. **Ocultamiento Condicional (Usuario)**:
    
    - Identifica las pantallas del módulo de rutinas donde el usuario puede añadir, editar o eliminar ejercicios y rutinas.
        
    - En lugar de borrar el código, envuelve los botones (como el `FloatingActionButton` o iconos de edición) en un condicional.
        
    - **Regla**: Si el rol del usuario no es 'ADMIN', estos elementos no deben renderizarse (puedes usar un simple `if (isAdmin) ...` o devolver un `SizedBox.shrink()`).
        
2. **Candado de Navegación Dinámico**:
    
    - En `main_navigation.screen.dart`, localiza el ítem del menú de 'Rutinas'.
        
    - Configura su visibilidad para que dependa estrictamente del booleano `IsRoutineEnabled` (o `isRoutineEnabled` según el modelo de datos del usuario).
        
    - Si el valor es `false`, el ítem de Rutinas debe desaparecer completamente del menú inferior para ese usuario.
        
3. **Punto de Entrada Admin**:
    
    - En la pantalla `UserRoutineScreen` que creamos para el administrador, asegúrate de que el botón de 'Ver rutinas asignadas' esté operativo.
        
    - Por ahora, este botón debe navegar a una pantalla de marcador de posición (placeholder) que diga 'Constructor de Rutinas en Desarrollo'.
        

**Nota técnica**: Utiliza `AppLogger` para imprimir en consola el estado de `IsRoutineEnabled` al cargar la aplicación y verificar que la lógica de navegación responda correctamente al cambio.

---

#windsurf

Primero creo la rama desde `feature/routine-management` y luego exploro la estructura de rutinas:





La rama actual ya incluye el PR #79 (routine-management mergeado en dev). Verifico que los archivos clave estén presentes:

Ahora exploro el módulo de rutinas del usuario:



Ahora verifico el `UserEntity`, `AppLogger`, y el placeholder actual:



Falta verificar `AuthLocalDataSource` y `UserModel` para entender cómo fluye `hasRoutine`:



Tengo todo el contexto. Creo el plan:
**Tarea 1** — [UserProfile](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/entities/user_profile.entity.dart:0:0-38:1) + mapper:

**Tarea 2** — Crear `RoutineBuilderPlaceholderScreen`:

**Tarea 3** — [UserRoutineScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/users/presentation/screens/user_routine/user_routine.screen.dart:7:0-49:1): actualiza el botón para navegar al nuevo placeholder:

**Tarea 4** — [MainNavigationScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:31:0-36:1): nav condicional + [AppLogger](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/core/utils/app_logger.dart:3:0-54:1). Es el cambio más complejo — refactorizo los getters y el listener:
**Tarea 5** — [MyRoutinesScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/my_routines.screen.dart:10:0-17:1): ocultar botones de creación para usuarios GYM:


Todo implementado. Resumen de cambios en `feature/routine-permissions-ui`:

---

## Cambios realizados

### 1. [user_profile.entity.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/entities/user_profile.entity.dart:0:0-0:0)
Añadido campo `isRoutineEnabled` (default `false`), mapeado desde `is_rutine_enabled` del endpoint `/users/profile` en [profile_api.repository.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/data/repositories/profile_api.repository.dart:0:0-0:0).

### 2. [RoutineBuilderPlaceholderScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/routine_builder_placeholder.screen.dart:2:0-79:1) *(nuevo)*
[lib/modules/my_routines/presentation/screens/routine_builder_placeholder.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/routine_builder_placeholder.screen.dart:0:0-0:0) — pantalla standalone que muestra "Constructor de Rutinas en Desarrollo" con ícono de construcción y botón de retroceso.

### 3. [user_routine.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/users/presentation/screens/user_routine/user_routine.screen.dart:0:0-0:0)
El botón "Ver plan de rutina" ahora navega a [RoutineBuilderPlaceholderScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/routine_builder_placeholder.screen.dart:2:0-79:1) en lugar del placeholder genérico.

### 4. [main_navigation.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:0:0-0:0)
- Campo `_isRoutineEnabled` en el estado del widget
- `_pages` y `_navItems` usan `if (_isRoutineEnabled)` para incluir condicionalmente el tab de Rutinas
- `listenWhen` detecta cambios en `userProfile?.isRoutineEnabled` para reaccionar al load del perfil
- `setState` ajusta el `_currentIndex` a 0 si el tab activo desaparece
- [AppLogger](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/core/utils/app_logger.dart:3:0-54:1) imprime en consola `role` e `isRoutineEnabled` al inicializar y al cambiar

### 5. [my_routines.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/my_routines.screen.dart:0:0-0:0)
Botones "Agregar día" y "Agregar ejercicio" envueltos en `if (_isAdmin(context))`. El método [_isAdmin](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/my_routines/presentation/screens/my_routines.screen.dart:555:2-558:3) lee el rol desde [AuthBloc](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_bloc.dart:7:0-67:1) sin modificar la firma de ningún método existente.