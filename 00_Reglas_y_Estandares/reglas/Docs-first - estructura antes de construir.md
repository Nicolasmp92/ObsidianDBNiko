# 📐 Regla — Docs-first: estructura documentada antes de construir

**Vigente desde:** 2026-11-19 (extendida a backend el mismo día) · **Aplica a:**
todo proyecto — front (Angular, Flutter) y back (Spring, lo que sea)

## El principio

Ningún módulo nace sin su **spec escrita primero**. La documentación de la
estructura propuesta va *antes* de la implementación — no es un informe
posterior, es el contrato contra el que se construye y se revisa.

## Dónde vive

Cada proyecto tiene subcarpetas por capa en su documentación:

```
03_Proyectos/<Proyecto>/
├── MOC - <Proyecto>.md          # enlaza las notas front/* y back/*
├── front/                        # specs de UI (widgets, pantallas, tokens)
│   ├── <PREF> - front-widgets.md    # inventario de componentes compartidos
│   ├── <PREF> - front-<pantalla>.md # spec por pantalla, ANTES de construir
│   └── <PREF> - front-tokens.md     # tokens de diseño si los hay
└── back/                         # specs de servidor (dominios, API, datos)
    ├── <PREF> - back-arquitectura.md # mapa de módulos + contratos + entidades
    └── <PREF> - back-<modulo>.md     # spec por módulo nuevo, ANTES de construir
```

## Qué documenta cada spec

**Front** (antes de lanzar):

- Árbol de componentes: qué existe, qué se crea, qué es **compartido** vs local
- API pública de cada componente (props/inputs, eventos, variantes) con ejemplo
- Tokens usados (colores, radios, alturas, tipografía) — no valores sueltos
- Estados: vacío / cargando / error / deshabilitado
- Decisión de reuso: por qué compartido o local (YAGNI declarado)

**Back** (antes de lanzar):

- **Módulos/dominios**: paquetes, qué resuelve cada uno, límites entre ellos
- **Contrato API**: prefijos de rutas, endpoints por módulo, quién los autentica
- **Entidades e invariantes**: modelo de datos, estados/enums y transiciones,
  reglas de negocio que el código debe respetar (ej. *evoluciones inmutables*)
- **Seguridad**: roles/permisos que protegen cada superficie
- **Integraciones**: webhooks, providers externos, colas — con su contrato

## Al cerrar la construcción

La spec se **actualiza** a lo construido — es documento de referencia mutable
(a diferencia del `log.md`, narrativo append-only). Si el módulo cambia, la
spec cambia en el mismo commit lógico.

## Por qué (origen de la regla)

- **Rescatable**: un módulo documentado se recrea desde la doc aunque el código
  se pierda (lección del incidente Myk 2026-11-19)
- **Reusabilidad real**: no se re-inventa lo que ya existe si hay inventario
  (lección Sconect — 7 pantallas copiando el mismo botón)
- **Revisable**: la auditoría evalúa contra un mapa escrito, no contra memoria
- **Coherente**: el backend tiene las mismas trampas — entidades duplicadas,
  rutas huérfanas, invariantes que solo viven en la cabeza de quien escribió

## Aplicación inicial

- [[SCN - front-widgets]] — inventario `core/widgets` (refactor `AppButton`)
- [[SCN - back-arquitectura]] — mapa de módulos Spring + API + invariantes
