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
| `GYM - ` | App de gimnasio |
| `STK - N.` / `SCK-N` | StarterCustomeKit (serie de dominios numerada) |
| `MP - ` | Sitio web MP |
| `MOC - ` | Mapa de contenido de un proyecto o área |

## Reglas del embudo

1. Nada entra directo a un proyecto: primero pasa por `01_Laboratorio_y_Borradores/`.
2. Las imágenes van siempre a `00_Assets/` y se incrustan con `![[nombre.png]]`.
3. Toda nota de proyecto debe estar enlazada desde su `MOC - <Proyecto>`.
4. El tablero kanban maestro es [[Desarrollo]] — las notas de tarea usan el frontmatter `status:` (`Pendientes`, `En proceso`, `En Aprobacion`, `Finalizadas`).
5. Los commits y ramas siguen [[6. Conventional Commits|Conventional Commits]] y [[5. Convenciones de Nomenclatura de Ramas en Git|Convenciones de Nomenclatura de Ramas en Git]].

## Documentos de estándares

- [[Estándares Front-End - Angular]] — reglas para el front (Angular 22, Signals, Tailwind + CDK headless, SSR, workflow y testing).
- [[Plugins de Obsidian - Setup]] — extensiones de comunidad requeridas por el vault (kanban, tablas, post-its).
- [[Extensiones de VS Code - Setup]] — extensiones recomendadas del IDE (Angular, Java, Spring Boot, lint/formato).
