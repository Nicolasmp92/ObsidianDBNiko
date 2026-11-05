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
│
├── 00_Reglas_y_Estandares/       → PRIMERA: convenciones, estándares y skills
│   ├── reglas/                   → reglas de orden (Convenciones del Vault)
│   ├── estandares/               → estándares de código y setups
│   ├── skills/                   → skills de agente reutilizables (SKILL.md)
│   └── log.md                    → registro propio de la carpeta
│
├── 01_Laboratorio_y_Borradores/  → INBOX: todo entra aquí primero
│   └── Desarrollo.md             → tablero kanban maestro
│
├── 03_Proyectos/                 → proyectos en curso (uno por carpeta)
│   │                               estructura canónica por proyecto:
│   │                               MOC - <P>.md + log.md + registro_actividades.md
│   ├── BeanFlow/     ├── Cabid/          ├── Editora/      ├── Empresa/
│   ├── Frunexis/     ├── ISO Manager/    ├── KaiPetPoint/  ├── Linktree/
│   ├── MP/           ├── NAMP/           ├── Portafolio/   ├── Sconect/
│   └── StarterCustomeKit/                └── TaskFlow/
│
├── 98_Assets/                    → multimedia centralizada (imágenes, adjuntos)
│
└── 99_Archivo/                   → material histórico (no se borra, se archiva)
    ├── niko_wiki/                → base de conocimiento (Laravel, PHP, JS,
    │                               Git, Docker, APIs, Metodologías)
    └── Proyectos personales/     → proyectos cerrados (GYM, sconect, SCK v1)
```

## Flujo (embudo)

`capturar (01_)` → `procesar/clasificar` → `proyecto (03_)` → `archivo (99_)`

- Notas nuevas caen en `01_Laboratorio_y_Borradores/` (configurado en `.obsidian/app.json` → `newFileFolderPath`).
- Las imágenes siempre a `98_Assets/` con `![[nombre.png]]`.
- Toda nota de proyecto cuelga de su `MOC - <Proyecto>`.
