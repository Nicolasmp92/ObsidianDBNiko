# 📐 Convenciones del Vault

Reglas de orden del vault (Kaizen / Seiton): todo tiene su lugar y cada nota cuelga de un mapa.

## Estructura de carpetas

| Carpeta | Propósito |
|---|---|
| `00_Assets/` | Multimedia centralizada (imágenes, adjuntos) |
| `01_Laboratorio_y_Borradores/` | Inbox: ideas sueltas, kanbans, notas sin clasificar |
| `02_Reglas_y_Estandares/` | Estándares de código y convenciones (esta nota + documentos de reglas) |
| `03_Proyectos_Activos/` | Proyectos en curso — una subcarpeta por proyecto |
| `99_Archivo/` | Material histórico, wiki de referencia y notas depuradas |

## Prefijos de notas por proyecto

| Prefijo | Proyecto |
|---|---|
| `GYM - ` | App de gimnasio (archivado 2026-10-02 → `99_Archivo/Proyectos personales/GYM`) |
| `STK - N.` / `SCK-N` | StarterCustomeKit (serie de dominios numerada) |
| `MP - ` | Sitio web MP |
| `FX - ` | Frunexis |
| `SCN - ` | Sconect |
| `MOC - ` | Mapa de contenido de un proyecto o área |

## Estructura canónica por proyecto (modelo repositorios-digitales-uoh)

Cada carpeta de `03_Proyectos_Activos/<Proyecto>/` sigue esta forma; los archivos solo se crean con contenido real, no como andamiaje:

```text
<Proyecto>/
  MOC - <Proyecto>.md        # ficha: frontmatter (tipo/estado/actualizado/tags)
                             # + "Navegación por necesidad" (quiero X → doc)
  log.md                   # bitácora narrativa append-only, entradas
                             # tipificadas: HECHO / DECISIÓN / HIPÓTESIS / RIESGO
  registro_actividades.md  # tabla append-only: Fecha | Actividad | Evidencia
  <notas prefijadas>       # notas de trabajo, todas enlazadas desde el MOC
  _historico/              # notas superadas (cuando existan; nunca se borran)
```

Reglas (adaptadas de la convención 2026-09-25 del repo UOH):

- El `MOC` es la ficha del proyecto: qué es, estado, navegación **por necesidad** («quiero X»), no solo por nombre.
- El `log.md` es **append-only y tipificado**: distingue lo verificado (HECHO) de lo elegido (DECISIÓN), lo supuesto (HIPÓTESIS) y lo que puede romperse (RIESGO). Las entradas nuevas van al final.
- `registro_actividades.md` es la tabla de sesiones: una fila por actividad verificable, con evidencia. Si el proyecto tiene repo propio con su registro, esta tabla resume y apunta al autoritativo.
- Una nota superada no se borra: se mueve a `_historico/` o se marca `SUPERADO <fecha>` apuntando a la vigente.
- Toda nota de proyecto cuelga de su MOC (regla 3 del embudo) y el kanban maestro sigue siendo [[Desarrollo]].

## Reglas del embudo

1. Nada entra directo a un proyecto: primero pasa por `01_Laboratorio_y_Borradores/`.
2. Las imágenes van siempre a `00_Assets/` y se incrustan con `![[nombre.png]]`.
3. Toda nota de proyecto debe estar enlazada desde su `MOC - <Proyecto>`.
4. El tablero kanban maestro es [[Desarrollo]] — las notas de tarea usan el frontmatter `status:` (`Pendientes`, `En proceso`, `En Aprobacion`, `Finalizadas`).
5. Los commits y ramas siguen [[6. Conventional Commits|Conventional Commits]] y [[5. Convenciones de Nomenclatura de Ramas en Git|Convenciones de Nomenclatura de Ramas en Git]].

## Documentos de estándares

- [[Estándares Front-End - Angular]] — reglas para el front (Angular 22, Signals, Tailwind + CDK headless, SSR, workflow y testing).
- [[Estándares Full-Stack - StarterCustomeKit]] — stack de arranque para proyectos nuevos (Angular 22 + Spring Boot + PostgreSQL) y metodología de trabajo estilo DSpace-CRIS (paquete `.devin`, skills por gatillo, bitácoras, cadena lab→dev→prod).
- [[Plugins de Obsidian - Setup]] — extensiones de comunidad requeridas por el vault (kanban, tablas, post-its).
- [[Extensiones de VS Code - Setup]] — extensiones recomendadas del IDE (Angular, Java, Spring Boot, lint/formato).
