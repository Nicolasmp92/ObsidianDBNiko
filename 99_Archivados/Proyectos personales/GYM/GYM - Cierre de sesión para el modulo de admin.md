---
status: En Aprobacion
fecha: 2026-05-05
---
### feature/admin-profile-module

El módulo de admin no cuenta con un cierre de sesión, sin embargo el modulo de user si lo tiene, es necesario replicarlo para terminar con un modulo para el cierre de secion del administrador.

---
### imagenes de user profile:![[Pasted image 20260505150152.png]]


![[Pasted image 20260505150132.png]]





---

#BACKEND: Sobre las tareas realizadas:

# Resumen de la Feature: `GET /users/profile`

## Archivos creados

- **[profile_response.dto.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/http/models/profile_response.dto.go:0:0-0:0)** — DTO de respuesta con campos `Id`, `Rut`, `Name`, `Lastname`, `Email`, `ImageUrl`, `RoleId`, `RoleName`
- **[user_profile.handler.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/http/handlers/user_profile.handler.go:0:0-0:0)** — Handler que extrae el RUT del contexto JWT, llama al use case y serializa la respuesta

---

## Archivos modificados

### Dominio
- **[users_usecase.interface.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/interfaces/users_usecase.interface.go:0:0-0:0)** — Método [GetUserProfile(ctx, rut int)](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/usecases/users.usecase.go:57:0-59:1) agregado a la interfaz
- **[users_repository.interface.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/interfaces/users_repository.interface.go:0:0-0:0)** — Método [GetUserProfileByRut(ctx, rut int)](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/interfaces/users_repository.interface.go:14:1-14:80) agregado a la interfaz
- **[user.entity.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/shared/domain/entities/user.entity.go:0:0-0:0)** (shared) — Campo `Email string` agregado a la entidad de dominio

### Infraestructura — Base de datos
- **[user.model.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/shared/infrastructure/database/postgresql/models/user.model.go:0:0-0:0)** (shared GORM) — Columna `Email *string` nullable agregada, AutoMigrate la crea automáticamente
- **[postgresql.repository.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/database/repositories/postgresql.repository.go:0:0-0:0)** (users) — Implementación de [GetUserProfileByRut](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/interfaces/users_repository.interface.go:14:1-14:80) con `Preload("Role")` + mapeo de `Email` en [mapUserModelToEntity](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/database/repositories/postgresql.repository.go:186:0-223:1)
- **[sign_up.postgresql.repository.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/credentials/sign_up/infrastructure/database/repositories/sign_up.postgresql.repository.go:0:0-0:0)** — Mapeo de `Email` al crear usuarios nuevos
- **[users.usecase.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/usecases/users.usecase.go:0:0-0:0)** — Implementación de [GetUserProfile](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/domain/usecases/users.usecase.go:57:0-59:1) delegando al repositorio

### Infraestructura — HTTP
- **[users.route.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/http/routers/users.route.go:0:0-0:0)** — Ruta `GET /users/profile` registrada bajo `AuthMiddleware`

### Seeder
- **[setup.database.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/config/database/setup.database.go:0:0-0:0)** — Emails agregados a los 3 usuarios de prueba + loop de sincronización que hace `UPDATE email WHERE rut = ?` para usuarios ya existentes (sin borrar la BD)

---

## Correcciones aplicadas durante el desarrollo

| Problema | Solución |
|---|---|
| [respondWithJSONError](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/http/handlers/user_profile.handler.go:67:0-71:1) redeclarada | Eliminada del handler, ya existe en [users_list.handler.go](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-backend/src/modules/users/infrastructure/http/handlers/users_list.handler.go:0:0-0:0) |
| `email` no aparecía en respuesta | Eliminado `omitempty` del tag JSON |
| Usuarios existentes sin email | Loop de upsert en seeder actualiza email por RUT al reiniciar |
| `404` en el endpoint | Path corregido de `/profile` → `/users/profile` para coincidir con Flutter |

---

## Flujo completo implementado

```
JWT → AuthMiddleware → extrae RUT del contexto
    → UserProfileHandler
    → UsersUseCase.GetUserProfile(rut)
    → PostgresqlRepository.GetUserProfileByRut(rut)
    → GORM: SELECT * FROM users WHERE rut = ? + Preload("Role")
    → mapUserModelToEntity → sharedentities.User
    → ProfileResponse DTO
    → JSON 200 OK
```

## Deuda técnica anotada
- `LoginResponse.imageUrl` usa camelCase mientras el resto del proyecto usa snake_case → pendiente para refactor global de API.
  
  
  
  ---

# #Front sobre las tareas realizadas:

# Resumen — `feature/admin-profile-module` (Frontend)

## 1. Entidades y Dominio

**[user_profile.entity.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/entities/user_profile.entity.dart:0:0-0:0)** — Nueva entidad para el perfil del administrador:
- Campos: `id`, `rut`, `name`, `lastname`, `email`, `imageUrl`, `roleName`
- Soporte [copyWith](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/entities/user_profile.entity.dart:19:2-37:3)

**`profile.interface.dart`** (auth module) — Contrato para obtener el perfil vía API

**[get_profile.usecase.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/usecases/get_profile.usecase.dart:0:0-0:0)** (auth module) — Use case que invoca el repositorio de perfil

---

## 2. Data Layer

**[profile_api.repository.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/data/repositories/profile_api.repository.dart:0:0-0:0)** — Repositorio que consume `GET /users/profile`:
- Mapper con claves snake_case del backend: `image_url`, `role_name`, `rut` (int→String)
- Manejo de `DioException` y errores inesperados
- Logs operacionales con `AppLogger`

---

## 3. Auth BLoC

**`auth_event.dart`** — Nuevo evento `LoadProfileRequested`

**[auth_state.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:0:0-0:0)** — Estado [Authenticated](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:19:0-34:1) extendido con campo `UserProfile? userProfile` + [copyWith](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/entities/user_profile.entity.dart:19:2-37:3)

**`auth_bloc.dart`** — Handler `_onLoadProfileRequested`:
- Solo ejecuta si el estado actual es [Authenticated](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:19:0-34:1)
- En éxito: emite [Authenticated(userProfile: profile)](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:19:0-34:1)
- En fallo: mantiene el estado actual sin romper la sesión

---

## 4. Login BLoC

**[login_bloc.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/login/presentation/bloc/login_bloc.dart:0:0-0:0)** — Recibe `AuthBloc` como dependencia e invoca `LoadProfileRequested` tras un login exitoso

---

## 5. Pantalla [AdminProfileScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/profile/presentation/screens/admin_profile/admin_profile.screen.dart:4:0-105:1)

**Nueva pantalla** con diseño moderno UI/UX:
- `BlocBuilder<AuthBloc>` — datos 100% dinámicos desde el backend
- Avatar con imagen de red + fallback a ícono
- Badge con `roleName`
- Card de información: correo, RUT, nombre completo
- Fallback graceful: si `userProfile` es null usa los datos de [UserEntity](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/login/domain/entities/user.entity.dart:0:0-20:1)
- Botón de logout con diálogo de confirmación

---

## 6. Navegación

**[main_navigation.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:0:0-0:0)**:
- [AdminProfileScreen](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/profile/presentation/screens/admin_profile/admin_profile.screen.dart:4:0-105:1) agregada como 5ª pestaña en admin (`_pages` + `_navItems`)
- `BlocListener` con `listenWhen` para re-inicializar rol y cargar datos admin cuando `AuthBloc` pasa de no-Authenticated → Authenticated (cubre el flujo post-login)

---

## 7. DI / [main.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/main.dart:0:0-0:0)

- [ProfileApiRepository](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/data/repositories/profile_api.repository.dart:8:0-70:1) instanciado con `apiClient.dio` (interceptor de auth automático)
- [GetProfileUseCase](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/domain/usecases/get_profile.usecase.dart:4:0-10:1) (auth module) conectado al `AuthBloc`
- [LoginBloc](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/login/presentation/bloc/login_bloc.dart:7:0-46:1) recibe `authBloc` como parámetro

---

## Flujo completo

```
Login / Session restore
       │
       ▼
 AuthBloc: CheckSessionRequested
       │
       ▼
 Authenticated(user)  ──►  LoadProfileRequested
                                   │
                            GET /users/profile
                                   │
                                   ▼
                    Authenticated(user, userProfile)
                                   │
                                   ▼
                       AdminProfileScreen rebuild
                       muestra email, rol, RUT, avatar
```

---


# Resumen — Fix Logout Manual Admin

## Problema
El botón "Cerrar Sesión" del perfil de administrador mostraba la pantalla `SessionExpiredDialog` con contador, comportamiento reservado para sesiones expiradas automáticamente.

## Cambios realizados

### 1. [auth_state.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:0:0-0:0)
[Unauthenticated](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:36:0-43:1) ahora distingue el origen:

```dart
class Unauthenticated extends AuthState {
  final bool isManualLogout;
  const Unauthenticated({this.isManualLogout = false});
}
```

- `isManualLogout: true` → acción explícita del usuario
- `isManualLogout: false` (default) → sesión expirada / token inválido

---

### 2. [auth_bloc.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_bloc.dart:0:0-0:0)
[_onLogoutRequested](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_bloc.dart:60:2-66:3) simplificado — sin [AuthLoading](cci:2://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/auth/presentation/bloc/auth_state.dart:15:0-17:1) intermedio, emite el estado final directo:

```dart
await clearUserSessionUseCase();
emit(const Unauthenticated(isManualLogout: true));
```

---

### 3. [main_navigation.screen.dart](cci:7://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:0:0-0:0)
Lógica de reset refactorizada en tres métodos:

- **[_resetAllBlocs](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:198:2-212:3)** — extrae el reset de todos los blocs (reutilizable)
- **[_resetAllBlocsAndNavigate](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:214:2-217:3)** — logout manual → reset + `context.go('/login')` inmediato
- **[_resetAllBlocsAndShowDialog](cci:1://file:///c:/Users/Niko/OneDrive/Desktop/Desarrollo/gym/gym-mobile/lib/modules/navigation/presentation/screens/main_navigation.screen.dart:198:2-223:3)** — sesión expirada → reset + `SessionExpiredDialog`

El `BlocListener` enruta según el flag:
```dart
if (state.isManualLogout) {
  _resetAllBlocsAndNavigate(context);   // directo a login
} else {
  _resetAllBlocsAndShowDialog(context); // pantalla de expiración
}
```