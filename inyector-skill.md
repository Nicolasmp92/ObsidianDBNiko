---
tipo: inyector-skills
estado: derivado-local
paquete: store-local (base: skills-programacion-esenciales UOH + 2 externas anthropics/skills)
paquete_sha256: n/a  # este vault guarda el STORE, no el paquete canónico; el manifiesto verificable vive en repositorios-digitales-uoh/.devin/MANIFEST.sha256
paquete_ruta: 00_Reglas_y_Estandares/skills/
proyecto_raiz:
  pc-personal: C:/Users/ferlu/Desktop/ObsidianDBNiko
  pc-trabajo:  C:/Users/nicolas.munoz/Desktop/ObsidianDBNiko  # verificar ruta real en la pega
actualizado: 2026-11-05
---

# Inyector local de skills — Vault ObsidianDBNiko

> Este archivo enruta trabajo. No reemplaza las skills del store ni concede
> permisos. Al activar una skill, leer su `SKILL.md` canónico en
> `00_Reglas_y_Estandares/skills/<nombre>/`.

## Objetivo del proyecto

Vault documental y de **orquestación del desarrollo**: concentra reglas,
estándares, skills y bitácoras tipificadas de todos los proyectos (NAMP, KPP,
Editora, MP, UOH...). El código vive en repos satélite; aquí vive el
conocimiento y la coordinación. Éxito observable: cada proyecto con
`MOC + log + registro_actividades` al día, decisiones tipificadas en `log.md`,
y todo el trabajo commiteado/pusheado para viajar entre PCs.

## Restricciones

- Escritura autorizada: todo el vault.
- Ejecución autorizada: scripts locales y comandos de lectura; código de
  proyectos solo en su repo satélite, no aquí.
- Acciones irreversibles: prohibidas sin confirmación humana explícita.
- Prohibido commitear secretos (`.env`, credenciales, tokens).
- `.obsidian/` está en `.gitignore`: la config local NO viaja entre PCs
  (replicar cambios de config a mano en la otra máquina).
- Presupuesto: un humano con deadlines; priorizar acciones reversibles.

## Tabla de activación

| Tarea o señal | Skill | Orden | Salida esperada | No activar cuando |
|---|---|---|---|---|
| Encargo amplio/vago ("revisa esto", "ordena X") | `triage-entrada` | 1 | Trabajo acotado + rutas + costo + lo no mirado | Encargo ya acotado con criterio |
| Decisión de estándar, arquitectura, estructura del vault | `exploracion-analisis` | Antes de implementar | Nivel declarado + criterio de salida + tabla/qué-NO | Consulta simple, micro-decisión con default |
| Desarrollar feature o app en repo satélite | `desarrollo-aplicaciones` | Tras decisión | Línea vertical mínima + prueba + log del proyecto actualizado | Corrección aislada con contrato establecido |
| Nueva dependencia, herramienta, patrón o plugin | `interrogatorio-adopcion` | Antes de incorporar | 5 respuestas + veredicto único | Cambio barato y reversible |
| Abrir/cerrar sesión, retomar trabajo pendiente | `continuidad-sesion` | Al inicio/cierre | Estado del disco verificado; punto de retomada | Tarea de una sola sesión sin estado |
| Editar `log.md`, `registro_actividades.md`, MOCs u otro archivo que la otra máquina pueda haber tocado | `guarda-edicion-concurrente` | Antes de escribir | Releer → parche puntual → añadir al final en bitácoras | Archivo de autor único de esta sesión |
| Falla reproducible, resultado que no cuadra, sync roto | `diagnostico-fallas` | Antes de corregir | Reproducción + hipótesis fechada + corrección acotada | Causa evidente nombrada por el error |
| Auditar entrega, documento, post o afirmar completitud | `auditoria-evidencia` | Después de implementar | Denominadores + gates + veredicto separado | Cosecha primaria, inventario de movimientos |
| Probar/verificar app web local (UI, screenshots, consola) | `webapp-testing` | Con el server arriba o `with_server.py` | Script Playwright + evidencia visual/consola | App no web, o test ya cubierto por el framework del repo |
| Crear skill nueva, mejorar/evaluar una existente | `skill-creator` | Tras capturar intención | SKILL.md draft + evals si el output es verificable | Edición puntual sin eval (va directo) |

## Cadenas habituales

| Situación | Secuencia de skills | Gate de salida |
|---|---|---|
| Nueva funcionalidad sustantiva | `triage-entrada` → `exploracion-analisis` → `desarrollo-aplicaciones` → `auditoria-evidencia` | pruebas y evidencia suficientes |
| Falla reproducible | `diagnostico-fallas` → `desarrollo-aplicaciones` → `auditoria-evidencia` | reproducción negativa tras la corrección |
| Dependencia/patrón nuevo | `interrogatorio-adopcion` → `desarrollo-aplicaciones` | adopción justificada o descarte registrado |
| Reanudación con cambios ajenos (la pega también edita/pushea) | `continuidad-sesion` → `guarda-edicion-concurrente` | estado reconciliado antes de editar |
| Skill nueva al store | `skill-creator` → registro en `00_Reglas_y_Estandares/log.md` | SKILL.md validado + entrada tipificada |

## Adaptaciones locales

- La "bitácora" es `log.md` (raíz, tipificada) + `03_Proyectos/<P>/log.md`
  + `registro_actividades.md` por proyecto — mapear ahí lo que las skills
  llaman log/punto de retomada.
- Las skills canónicas viven en el **store** `00_Reglas_y_Estandares/skills/`
  (no en `.devin/`). Al activar una, leer su `SKILL.md` ahí.
- 3 skills también instaladas globalmente en `%APPDATA%\devin\skills\`
  (`continuidad-sesion`, `guarda-edicion-concurrente`, `diagnostico-fallas`) —
  mismo contenido, el store es la fuente para distribuir a otros repos.
- Concurrencia real: dos PCs (personal + pega) editan y pushean este repo.
  `git pull` antes de escribir archivos compartidos no es opcional.
- Embudo: notas nuevas caen en `01_Laboratorio_y_Borradores/`; imágenes a
  `98_Assets/`; toda nota de proyecto cuelga de su MOC (ver Convenciones).
- `webapp-testing` requiere Python + Playwright headless en la máquina.
- `skill-creator` con evals necesita subagentes/viewer; sin ellos queda
  limitada a redactar `SKILL.md` — declarar la limitación al usarla.

## Mejoras candidatas

| Skill | Evidencia | Candidata | Prueba | Estado |
|---|---|---|---|---|
| Ninguna | - | - | - | - |

## Verificación

- Integridad del paquete: `no_evaluable` en este repo (store sin manifiesto
  propio). Fuentes verificadas: `.devin` de repositorios-digitales-uoh
  (52/52 blobs vs MANIFEST, 2026-11-05) + `anthropics/skills` (Apache 2.0).
- Skills leídas: 10/10 (8 del paquete UOH + `webapp-testing` + `skill-creator`)
- Recursos requeridos leídos: bajo demanda por skill activada
- Ultimo caso de enrutamiento probado: incorporación de las 2 skills externas
  al paquete UOH (2026-11-05)
- Resultado: `pass`

## Punto de retomada

Inyector creado y adoptado. Siguiente acción: al abrir sesión usar
`continuidad-sesion` (leer `log.md` raíz + último registro del proyecto a
tocar). Regenerar este inyector si cambia el store o dos casos demuestran
enrutamiento incorrecto.
