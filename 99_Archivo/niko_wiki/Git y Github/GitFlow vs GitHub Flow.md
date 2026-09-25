**Tags:** #Git #FlujoDeTrabajo #Ramas

# GitFlow vs GitHub Flow

Dos estrategias de ramificación según el tamaño del equipo y la frecuencia de despliegue.

## GitFlow

- Ramas permanentes: `main` (producción) y `develop` (integración).
- Ramas temporales: `feature/*`, `release/*`, `hotfix/*`.
- Pensado para releases versionados y equipos grandes.
- Más ceremonia: merges en dos direcciones y sincronización `main`/`develop`.

## GitHub Flow

- Una sola rama principal (`main`) + `feature/*` de vida corta.
- Merge a `main` vía Pull Request + revisión + deploy continuo.
- Ideal para proyectos web con despliegues frecuentes y equipos chicos.

## Cuál elegir

| Contexto | Estrategia recomendada |
|---|---|
| Deploy varias veces por semana | GitHub Flow |
| Releases versionadas (v1.2, v2.0) | GitFlow |
| Proyecto personal / MVP | GitHub Flow |
| Equipo grande con QA formal | GitFlow |

> En tus proyectos (GYM, StarterCustomeKit) el patrón usado es `dev` + `feature/*` con merge por PR — una variante simple de GitHub Flow.

---
**Relacionado:** [[Convenciones de Nomenclatura de Ramas en Git]] | [[Conventional Commits]] | [[1 Index Git y Github]]
