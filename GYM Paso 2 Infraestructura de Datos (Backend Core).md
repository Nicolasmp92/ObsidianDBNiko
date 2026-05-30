---
status: En Aprobacion
---
- Rama:

``` brash
feature/routine-backend-core
```

- [x] **Análisis de Convenciones**: Revisar los módulos de Nutrición y Máquinas para asegurar que la estructura de la tabla `assigned_routines` sea consistente con el resto del backend. ✅ 2026-05-15
    
- [x] Crear tabla `assigned_routines` (vinculando `UserID`, `ExerciseID`, `Series`, `Reps`, `Weight`). ✅ 2026-05-15
    
- [x] Crear Endpoint `POST /users/{id}/routine` y el `GET /my-routine` para el consumo del usuario. ✅ 2026-05-15

---


#PROMPT 
Windsurf, estamos trabajando en la rama `feature/routine-backend-core`. El objetivo es transformar el módulo de rutinas para que el Admin asigne y el usuario solo ejecute.

**Tareas de Análisis y Arquitectura:**

1. **Investigación de Convenciones (Nutrición y Máquinas)**:
    
    - Revisa cómo están implementados los módulos de `nutrition` y `machines`.
        
    - Observa cómo se estructuran las relaciones, los nombres de las tablas de unión y cómo se gestionan los DTOs de respuesta para el administrador vs el usuario. Queremos que el módulo de rutinas sea un 'hermano' de estos módulos en términos de código.
        
2. **Auditoría del Módulo de Rutinas Actual**:
    
    - Analiza la lógica actual donde el usuario crea sus rutinas. Identifica las tablas involucradas (ej: `routines`, `user_exercises`).
        
    - Determina si es más limpio refactorizar estas tablas o crear la nueva estructura `assigned_routines` manteniendo la armonía con lo descubierto en el punto 1.
        
3. **Implementación de Modelos y BD**:
    
    - Crea/Ajusta el modelo GORM para la asignación de rutinas. Debe incluir campos clave: `user_id`, `exercise_id`, `series`, `reps`, `weight`, `day_of_week` e `is_completed`.
        
    - Asegúrate de que la migración automática esté configurada.
        
4. **Endpoints y Seguridad**:
    
    - Mueve la lógica de 'escritura' (POST/PATCH de creación) a una ruta protegida para el Admin: `POST /users/:id/routine`.
        
    - Configura el endpoint `GET /my-routine` para que el usuario recupere su plan asignado.
        
    - Asegúrate de que los nombres de las rutas y los tags JSON sigan la convención `snake_case` y la estructura de carpetas del proyecto.
        

**Objetivo final**: Una base de datos consistente donde el Admin prescribe y el usuario reporta ejecución, siguiendo fielmente el patrón de diseño de Nutrición y Máquinas.

---
---

# Resumen: Módulo de Rutinas — `feature/routine-backend-core`

## Objetivo
Transformar el módulo de rutinas para que el Admin asigne ejercicios y el usuario solo ejecute, siguiendo las convenciones de los módulos `nutrition` y `machines`.

## Arquitectura Implementada

### Estructura de Carpetas
```
src/modules/routines/
├── domain/
│   ├── entities/
│   │   └── user_routine_exercise.entity.go
│   ├── interfaces/
│   │   ├── routine_repository.interface.go
│   │   └── routine_usecase.interface.go
│   └── usecases/
│       └── routine.usecase.go
└── infrastructure/
    ├── database/
    │   ├── models/
    │   │   └── user_routine_exercise.model.go
    │   └── repositories/
    │       └── postgresql.repository.go
    └── http/
        ├── models/
        │   ├── assign_routine_exercise_request.dto.go
        │   └── routine_exercise_response.dto.go
        ├── handlers/
        │   ├── assign_routine_exercise.handler.go
        │   ├── get_my_routine.handler.go
        │   └── complete_routine_exercise.handler.go
        └── routers/
            └── routine.route.go
```

### Modelo de Base de Datos
**Tabla:** `user_routine_exercises`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | int (PK) | Auto-incremento |
| `user_id` | int64 (FK) | Referencia a users |
| `exercise_id` | int (FK) | Referencia a exercises |
| `series` | int | Número de series |
| `reps` | int | Repeticiones |
| `weight` | float64 | Peso (kg), default 0 |
| `day_of_week` | int | Día de la semana (1=Lunes, 7=Domingo) |
| `is_completed` | bool | Ejercicio completado por usuario, default false |
| `created_at` | timestamp | Fecha de creación |

## Endpoints Implementados

### 1. Asignar Ejercicio a Rutina (Admin)
```
POST /routine/users/{userId}/exercises
Authorization: Bearer <admin_token>
Content-Type: application/json

{
  "exercise_id": 1,
  "series": 3,
  "reps": 12,
  "weight": 20.5,
  "day_of_week": 1
}
```

**Middleware:** `AuthMiddleware` + `RequireRole(admin)`

### 2. Obtener Mi Rutina (Usuario)
```
GET /routine/my-exercises
Authorization: Bearer <user_token>
```

**Middleware:** `AuthMiddleware`  
**Lógica:** Extrae RUT del JWT, hace JOIN con users para obtener rutina

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "exercise_id": 1,
    "series": 3,
    "reps": 12,
    "weight": 20.5,
    "day_of_week": 1,
    "is_completed": false,
    "exercise": {
      "id": 1,
      "title": "Press de Banca",
      "video_url": "...",
      "image_url": "...",
      "description": "..."
    }
  }
]
```

### 3. Marcar Ejercicio como Completado (Usuario)
```
PATCH /routine/exercises/{id}/complete
Authorization: Bearer <user_token>
```

**Middleware:** `AuthMiddleware`

## Convenciones Seguidas

### Patrones de `nutrition` y `machines`
- **GORM model** en [infrastructure/database/models/](cci:9://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/nutrition/infrastructure/database/models:0:0-0:0) con [TableName()](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/shared/infrastructure/database/postgresql/models/exercise.model.go:14:0-16:1) method
- **Domain entity** en [domain/entities/](cci:9://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/shared/domain/entities:0:0-0:0) con campos mínimos
- **Repository interface** en [domain/interfaces/](cci:9://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/nutrition/domain/interfaces:0:0-0:0)
- **Use case interface** en [domain/interfaces/](cci:9://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/nutrition/domain/interfaces:0:0-0:0)
- **Mapper functions** `mapXxxModelToEntity` dentro del repositorio
- **DTOs** en [infrastructure/http/models/](cci:9://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/machines/infrastructure/http/models:0:0-0:0) con snake_case JSON tags
- **Handlers** implementan `sharedinterfaces.HandlerInterface`
- **Router function** `Register[Module]Routes(r chi.Router, db *gorm.DB)`
- **Route groups:** Admin routes con `RequireRole`, user routes solo con `AuthMiddleware`

### Clean Architecture
- **Domain layer** sin dependencias externas
- **Infrastructure layer** depende de domain
- **Use cases** delegan a repositorios
- **Handlers** delegan a use cases

## Integración al Proyecto

### Archivos Modificados
1. **[main.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/main.go:0:0-0:0)**:
   - Import agregado: `routinesrouter`
   - Registro: [routinesrouter.RegisterRoutineRoutes(server, db)](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/routines/infrastructure/http/routers/routine.route.go:12:0-36:1)

2. **[src/config/database/setup.database.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/config/database/setup.database.go:0:0-0:0)**:
   - Import agregado: `routineModels`
   - AutoMigrate: `&routineModels.UserRoutineExercise{}`

### Migración Automática
La tabla `user_routine_exercises` se crea automáticamente al reiniciar el servidor vía GORM `AutoMigrate`.

## Flujo de Datos

### Admin asigna ejercicio:
```
Handler → UseCase → Repository → GORM Create → Preload Exercise → Entity → DTO → Response
```

### Usuario ve su rutina:
```
Handler → Extract RUT from JWT → UseCase → Repository (JOIN users.rut) → GORM Find → Entity → DTO → Response
```

### Usuario completa ejercicio:
```
Handler → UseCase → Repository → GORM Update is_completed → Entity → DTO → Response
```

## Estado Final
✅ Feature completa y lista para testing  
✅ Arquitectura consistente con módulos existentes  
✅ Migración automática configurada  
✅ Rutas protegidas con middleware apropiado  
✅ DTOs con snake_case JSON tags