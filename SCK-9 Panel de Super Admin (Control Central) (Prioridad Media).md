---
status: Pendientes
---
Objetivo: Diferenciar el rol de "Dueño de la Plataforma" (tú) del "Dueño del Negocio" (cliente). Controlar la salud del sistema y la configuración global.


- [ ] Refactor del Dashboard: Eliminar métricas estáticas e integrar widgets de "Salud del Sistema" (Logs de errores, estado de Queues).
    
- [ ] Crear interfaz visual para la tabla `Settings` (cambiar Nombre de App, Logo y modo de registro).
    
- [ ] Añadir funcionalidad de "Impersonate" para que el Super Admin pueda entrar como cualquier usuario para dar soporte.

---

``` bash
git checkout dev && git pull origin dev && git checkout -b feature/super-admin-panel
```