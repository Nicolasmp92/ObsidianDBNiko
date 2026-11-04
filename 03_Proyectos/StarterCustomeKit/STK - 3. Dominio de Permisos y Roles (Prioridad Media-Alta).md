---
status: Finalizadas
---
### 3. Dominio de Permisos y Roles (Prioridad: Media-Alta)

_Objetivo: Desacoplar la lógica de Spatie de la infraestructura global._

- [x] **Migración de `PermissionTags`**: Mover el componente Livewire y su lógica a `app/Domains/Permissions`. ✅ 2026-05-09


- [x] **Actions de Sincronización**: Crear Actions para asignar roles y permisos, evitando que los controladores toquen directamente los métodos de Spatie. ✅ 2026-05-09