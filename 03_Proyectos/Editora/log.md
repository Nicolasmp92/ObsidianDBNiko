# 📓 Log — Editora

Bitácora narrativa **append-only**. Las entradas nuevas van al final y nunca
se reescribe el historial. Cada entrada se tipifica:
- **HECHO**: verificado con evidencia;
- **DECISIÓN**: qué se eligió y por qué;
- **HIPÓTESIS**: aún no confirmado;
- **RIESGO**: algo que puede romperse.

La bitácora técnica autoritativa vive en el repo (`log.md` +
`registro_actividades.md`). Esta nota guarda el contexto estratégico y los
hitos.

---

## 2026-10-27 — Origen y fase 1

- **DECISIÓN (contexto estratégico).** La Propuesta Editorial UOH (ago-2026)
  mostró que la vitrina pública de la editorial es chica: unos 8 títulos al
  año en 3 colecciones. En UOH se sigue con OMP como sistema institucional
  (rama B recomendada: OMP como motor + frontend moderno). En paralelo nace
  **Editora** como producto propio por tres motivos:
  - aprendizaje full-stack;
  - portafolio;
  - un software vendible a otras editoriales pequeñas.

  Motivo personal declarado: el contrato a honorarios hace estratégico tener
  un producto propio. Regla: cero datos, marca o documentos de la UOH en el
  repo, y trabajo en un repo personal privado.
- **DECISIÓN.** Nombre **Editora** (descartados Colofón, Folio y Ex Libris;
  Ex Libris choca con la empresa de software de bibliotecas). Repo
  **privado** porque la intención es comercial.
- **HECHO.** Fork de StarterCustomeKit v2 (Angular 22 SSR + Spring Boot 3.5
  + PostgreSQL). Renombrado completo sck→editora y puertos 8086/4206/4006.
- **HECHO.** Fase 1 funcional de punta a punta:
  - colecciones y libros con portada y PDF validados por firma de bytes;
  - sitio público editorial: inicio, catálogo con filtros, colecciones y
    ficha con descarga, cita APA y meta `citation_*`;
  - panel de libros y colecciones.

  Evidencia:
  - `mvn test` 12/12, con invariantes: borrador da 404 público, PDF falso da
    400, colección con libros da 409;
  - `npm test` 28/28 y lint limpio;
  - bundle de 103 kB gzip;
  - smoke E2E: PDF descargado idéntico byte a byte;
  - capturas a 1440 y 360 px sin scroll horizontal.
- **RIESGO.** La BD PostgreSQL `editora` no existe aún (requiere sudo). Hoy
  corre en H2: los datos se pierden al reiniciar la API. Comando pendiente
  en [[Proyectos - Setup y arranque]].
- **RIESGO.** `citation_pdf_url` es relativa. Hay que hacerla absoluta con
  el origen público antes de pedir indexación en Scholar.
- **HIPÓTESIS (comercial).** El diferencial frente a OMP es una interfaz
  moderna lista para usar, con el modelo editorial nativo. Por validar con
  la segunda editorial interesada, no antes.
