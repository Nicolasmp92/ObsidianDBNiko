---
tipo: proyecto
proyecto: beanflow
estado: activo-v2-en-rama
actualizado: 2026-10-05
tags: [restaurante, pos, comandas, angular, spring-boot, portafolio]
---
# ☕ MOC — BeanFlow

POS de restaurante/café: salón con mesas, comandas, cocina, carta con recetas, bodega (insumos + movimientos) y cuenta. Repo: `~/Escritorio/Desarrollo/BeanFlow` (GitHub `Nicolasmp92/BeanFlow`). Linaje: proyecto Laravel original → renombrado/absorbido en [[MOC - StarterCustomeKit|StarterCustomeKit]] → v2 reconstruido sobre el mismo stack Angular+Spring.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (resumen) + `log.md` del repo (detalle)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero levantar el stack** → `backend: mvn spring-boot:run` (:8085) + `npm start` (:4205); login `nikolasmp92@gmail.com` / `niko9214` (convención unificada)
- **Dev sin PostgreSQL** → `BEANFLOW_DB_URL=jdbc:h2:mem:beanflow;DB_CLOSE_DELAY=-1` + `SPRING_FLYWAY_LOCATIONS=classpath:db/migration-h2` (datos volátiles, sin índice parcial)
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Dominios (v2, en `refactor/stack-angular-spring`)

| Dominio | Entidades | Estado |
|---|---|---|
| Salón | `mesas`, `comandas`, `comanda_items` | Completo; una comanda abierta por mesa (índice parcial PG) |
| Cocina | vista de items pendiente→preparando→listo | Completo |
| Carta | `categorias`, `productos`, `receta_items` | Completo; items de comanda congelan nombre+precio |
| Bodega | `insumos`, `movimientos_insumo` | Completo; `stock_resultante` por fila (saldo auditable) |
| Acceso | `usuarios` con rol simple (`garzon`/`cocina`/`caja`/`admin`), JWT en cookie | Heredado del kit |

## Decisiones estructurales vigentes

- Puertos: API `8085`, dev `4205`, SSR `4005` (reservados: 8080/4200/4000 DSpace-CRIS, 8081-84 los demás proyectos).
- **BD PostgreSQL `beanflow`/`beanflow_user` pendiente de aprovisionar** — el backend corre en H2 en memoria mientras tanto; los datos se pierden al reiniciar y `uq_comanda_abierta_por_mesa` no se enforcea en H2.
- Historia del nombre: el proyecto Laravel 2025 era BeanFlow (`beanflow_livewire`); sus notas wiki fueron reescritas como SCK y el código v2 quedó en `Desarrollo/BeanFlow`.
