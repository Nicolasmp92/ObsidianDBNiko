# 📐 Regla — Docs-first UI: estructura documentada antes de construir

**Vigente desde:** 2026-11-19 · **Aplica a:** todo proyecto con front (Angular, Flutter o lo que sea)

## El principio

Ningún módulo de UI nace sin su **spec escrita primero**. La documentación de la
estructura propuesta va *antes* de la implementación — no es un informe
posterior, es el contrato contra el que se construye y se revisa.

## Dónde vive

Cada proyecto con front tiene una subcarpeta `front/` en su documentación:

```
03_Proyectos/<Proyecto>/
├── MOC - <Proyecto>.md        # enlaza las notas front/*
├── front/
│   ├── <PREF> - front-widgets.md       # componentes compartidos (la "librería" interna)
│   ├── <PREF> - front-<pantalla>.md    # spec por pantalla/módulo, escrita ANTES de construir
│   └── <PREF> - front-tokens.md        # tokens de diseño cuando el sistema los tiene
```

## Qué documenta cada spec (antes de lanzar)

- **Árbol de componentes** de la pantalla/módulo: qué existe, qué se crea nuevo,
  qué es **compartido** (de `core/widgets`, `shared/`) vs **local**
- **API pública** de cada componente nuevo o compartido (props/inputs, eventos,
  variantes) — como se invoca, con ejemplo
- **Tokens usados**: colores (`AppColors.*`, variables CSS), radios, alturas,
  tipografía — no valores sueltos
- **Estados**: vacío / cargando / error / deshabilitado — se deciden en la spec,
  no improvisados en el render
- **Decisión de reuso**: por qué es compartido o por qué es local (YAGNI
  declarado, no accidental)

## Al cerrar la construcción

La spec se **actualiza** a lo construido — es documento de referencia mutable
(a diferencia del `log.md`, que es narrativo append-only). Si el módulo cambia,
la spec cambia en el mismo commit lógico.

## Por qué (origen de la regla)

- **Rescatable**: un módulo documentado se puede recrear desde la doc aunque el
  código se pierda (lección del incidente Myk 2026-11-19 — el repo sobrevivió,
  pero si no hubiera pusheado, la doc sería todo lo que quedaba)
- **Reusabilidad real**: los componentes no reusables nacen porque nadie sabe
  qué existe ya (lección Sconect — 7 pantallas copiando el mismo botón). La
  nota `front-widgets` es el inventario que evita re-inventar
- **Revisable**: el consejo de diseño y la auditoría evalúan contra un mapa
  escrito, no contra memoria

## Aplicación inicial

- [[SCN - front-widgets]] — primera nota viva del sistema (Sconect,
  `core/widgets`, nace del refactor `AppButton` 2026-11-19)
