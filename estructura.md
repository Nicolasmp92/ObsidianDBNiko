---
tipo: mapa
actualizado: 2026-11-05
---

# 🗂️ Estructura del vault

Árbol de carpetas y propósito de cada una. Reglas detalladas en [[00_Reglas_y_Estandares/reglas/Convenciones del Vault|Convenciones del Vault]] y mapa de contenido en [[README]].

```text
ObsidianDBNiko/
│
├── README.md                     → mapa general del vault
├── estructura.md                 → este archivo (árbol de carpetas)
├── log.md                        → bitácora maestra global (append-only,
│                                   entradas tipificadas: HECHO / DECISIÓN /
│                                   HIPÓTESIS / RIESGO / PENDIENTE)
├── inyector-skill.md             → enrutador de skills del vault (qué skill
│                                   activar según la tarea — derivado local)
│
├── 00_Reglas_y_Estandares/       → PRIMERA: convenciones, estándares y skills
│   ├── reglas/                   → reglas de orden (Convenciones del Vault)
│   ├── estandares/               → estándares de código y setups
│   ├── skills/                   → skills de agente reutilizables (SKILL.md)
│   └── log.md                    → registro propio de la carpeta
│
├── 01_Inputs/  → INBOX: todo entra aquí primero
│   └── Desarrollo.md             → tablero kanban maestro
│
├── 02_Outputs/                   → entregables producidos: posts, informes,
│   │                               propuestas — subcarpeta por proyecto
│   └── log.md                    → registro de entregables (qué, cuándo, para qué)
│
├── 03_Proyectos/                 → proyectos en curso (uno por carpeta)
│   │                               estructura canónica por proyecto:
│   │                               MOC - <P>.md + log.md + registro_actividades.md
│   ├── BeanFlow/     ├── Cabid/          ├── Editora/      ├── Empresa/
│   ├── Frunexis/     ├── ISO Manager/    ├── KaiPetPoint/  ├── Linktree/
│   ├── MP/           ├── NAMP/           ├── Portafolio/   ├── Sconect/
│   └── StarterCustomeKit/                └── TaskFlow/
│
├── 04_Wiki/                      → base de conocimiento VIVA (Laravel, PHP, JS,
│   │                               Git, Docker, APIs, Metodologías) — lo que
│   │                               aprendo y reutilizo entre proyectos
│
├── 98_Assets/                    → multimedia centralizada (imágenes, adjuntos)
│                                   compartida por TODAS las carpetas
│
└── 99_Archivados/                → material histórico (no se borra, se archiva)
    └── Proyectos personales/     → proyectos cerrados (GYM, sconect, SCK v1)
```

## Flujo (embudo)

`capturar (01_)` → `proyecto (03_)` → `entregar (02_)` → `conocimiento (04_)` → `archivar (99_)`

- Notas nuevas caen en `01_Inputs/` (configurado en `.obsidian/app.json` → `newFileFolderPath`).
- Las imágenes siempre a `98_Assets/` con `![[nombre.png]]`.
- Toda nota de proyecto cuelga de su `MOC - <Proyecto>`.
- Lo entregado (posts, informes, propuestas) se registra en `02_Outputs/<proyecto>/` + `log.md`.
- Lo aprendido se destila a `04_Wiki/`; lo cerrado se archiva en `99_Archivados/`.
