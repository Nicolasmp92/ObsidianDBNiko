# 📐 Convenciones del Vault

Reglas de orden del vault (Kaizen / Seiton): todo tiene su lugar y cada nota cuelga de un mapa.

## Estructura de carpetas

| Carpeta | Propósito |
|---|---|
| `00_Reglas_y_Estandares/` | Estándares de código y convenciones (esta nota + documentos de reglas) |
| `01_Inputs/` | Inbox: ideas sueltas, kanbans, material entrante y notas sin clasificar |
| `02_Outputs/` | Entregables producidos (posts, informes, propuestas) — subcarpeta por proyecto |
| `03_Proyectos/` | Proyectos en curso — una subcarpeta por proyecto |
| `04_Wiki/` | Base de conocimiento viva: lo aprendido, reutilizable entre proyectos |
| `98_Assets/` | Multimedia centralizada (imágenes, adjuntos) — sirve a todas las carpetas |
| `99_Archivados/` | Material histórico y notas depuradas (proyectos cerrados) |

## Prefijos de notas por proyecto

| Prefijo | Proyecto |
|---|---|
| `GYM - ` | App de gimnasio (archivado 2026-10-02 → `99_Archivados/Proyectos personales/GYM`) |
| `STK - N.` / `SCK-N` | StarterCustomeKit (serie de dominios numerada) |
| `MP - ` | Sitio web MP |
| `NAMP - ` | Plataforma web NAMP (empresa + portafolio) |
| `FX - ` | Frunexis |
| `SCN - ` | Sconect |
| `MOC - ` | Mapa de contenido de un proyecto o área |

## Estructura canónica por proyecto (modelo repositorios-digitales-uoh)

Cada carpeta de `03_Proyectos/<Proyecto>/` sigue esta forma; los archivos solo se crean con contenido real, no como andamiaje:

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

## Frontmatter controlado (vocabulario cerrado)

Para que [[Proyectos]] (base) y cualquier consulta funcionen, el frontmatter usa valores cerrados:

| Campo | Valores permitidos |
|---|---|
| `tipo` | `proyecto`, `empresa`, `log`, `registro`, `nota-tecnica`, `plan`, `roadmap`, `runbook`, `cotización`, `pipeline-ideas`, `documentacion-tecnica` |
| `estado` (solo `tipo: proyecto`/`empresa`) | `pipeline` (idea sin código), `activo` (en desarrollo), `pausado`, `produccion` (live, incluye interno), `archivado` |
| `proyecto` | slug del proyecto en minúsculas sin espacios (`kaipetpoint`, `namp`) |
| `actualizado` | fecha `YYYY-MM-DD` de la última modificación relevante |

- El detalle fino (rama, fase, subestado) va en el cuerpo del MOC o el log, **no** en `estado`.
- `tipo: empresa` queda fuera del dashboard de productos — es la capa meta (infra, comercial, pipeline).
- Las plantillas canónicas viven en `00_Reglas_y_Estandares/templates/` (plugin core Templates configurado): `MOC - Proyecto`, `log - Proyecto`, `registro_actividades - Proyecto`.
- La integridad del store de skills se verifica con `00_Reglas_y_Estandares/skills/MANIFEST.sha256` (mismo patrón que `.devin/` en UOH; regenerar al agregar/mutar una skill).

## Reglas del embudo

1. Nada entra directo a un proyecto: primero pasa por `01_Inputs/`.
2. Las imágenes van siempre a `98_Assets/` y se incrustan con `![[nombre.png]]`.
3. Toda nota de proyecto debe estar enlazada desde su `MOC - <Proyecto>`.
4. El tablero kanban maestro es [[Desarrollo]] — las notas de tarea usan el frontmatter `status:` (`Pendientes`, `En proceso`, `En Aprobacion`, `Finalizadas`).
5. Los commits y ramas siguen [[6. Conventional Commits|Conventional Commits]] y [[5. Convenciones de Nomenclatura de Ramas en Git|Convenciones de Nomenclatura de Ramas en Git]].
6. **`01_Inputs` se vacía al cierre de cada semana** (o al cerrar una sesión de trabajo larga): cada nota del inbox se clasifica a proyecto / wiki / outputs / archivo — o se borra. El inbox se mide por **rotación**, no por volumen; un `01_Inputs` que solo crece es una fuga del sistema igual que la raíz lo era antes.

## Documentos de estándares

- [[Estándares Front-End - Angular]] — reglas para el front (Angular 22, Signals, Tailwind + CDK headless, SSR, workflow y testing).
- [[Estándares Full-Stack - StarterCustomeKit]] — stack de arranque para proyectos nuevos (Angular 22 + Spring Boot + PostgreSQL) y metodología de trabajo estilo DSpace-CRIS (paquete `.devin`, skills por gatillo, bitácoras, cadena lab→dev→prod).
- [[Plugins de Obsidian - Setup]] — extensiones de comunidad requeridas por el vault (kanban, tablas, post-its).
- [[Extensiones de VS Code - Setup]] — extensiones recomendadas del IDE (Angular, Java, Spring Boot, lint/formato).
