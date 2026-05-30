---
status: Finalizadas
---
## Resumen de cambios realizados

**Problema**: Los filtros dejaban de responder al volver de la pantalla de detalles.

**Solución implementada**:

### 1. Nuevo evento [ReturnToList](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_event.dart:70:0-72:1)
- **Archivo**: [admin_exercises_event.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_event.dart:0:0-0:0)
- **Propósito**: Sincronizar el retorno desde detalle a lista con estado preservado

### 2. Handler [_onReturnToList](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_bloc.dart:358:2-365:3) en Bloc
- **Archivo**: [admin_exercises_bloc.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_bloc.dart:0:0-0:0) (líneas 359-369)
- **Función**: Emite `_cachedListState` al regresar, manteniendo filtros/búsqueda

### 3. Mejoras en handlers de filtros
- **[_onSearchAdminExercises](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_bloc.dart:98:2-129:3)** y **[_onToggleFilterAdminExercises](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_bloc.dart:213:2-229:3)**:
  - Usan `_cachedListState` cuando el estado actual no está cargado
  - Actualizan `_cachedListState` inmediatamente
  - Emiten cambios solo si la UI está en [AdminExercisesLoaded](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_state.dart:20:0-54:1)

### 4. Dispatch de [ReturnToList](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_event.dart:70:0-72:1) en UI
- **Archivo**: [exercise_detail.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/screens/exercise_detail.screen.dart:0:0-0:0)
- **Ubicaciones**: Todos los botones de retroceso (loading, error, detail)
- **Acción**: [ReturnToList](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_event.dart:70:0-72:1) → `Navigator.pop()`

### 5. Verificación UI
- **[exercises_list_container.widget.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/widgets/exercises_list_container.widget.dart:0:0-0:0)**: Botones de filtro en `BlocBuilder` escuchando `state.filter`

**Flujo completo**:
1. Aplicar filtro/búsqueda → `_cachedListState` se actualiza
2. Navegar a detalle → estado cambia a [AdminExerciseDetailLoaded](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_state.dart:105:0-112:1)
3. Regresar → [ReturnToList](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/exercises/presentation/bloc/admin_exercises_event.dart:70:0-72:1) emite `_cachedListState` con filtros intactos
4. Lista muestra filtros persistentes

**Resultado**: Los filtros ahora persisten al navegar entre lista y detalles.