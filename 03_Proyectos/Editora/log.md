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

## 2026-10-27 — Pivote institucional: el alcance crece a Editorial + Biblioteca

- **DECISIÓN (institucional, en registro):** reunión con jefaturas
  (Bernardo + Cristóbal). La plataforma ya no es solo Editorial:
  también digitaliza y publica libros de Biblioteca; se interconecta
  con Koha (metadata) y con el repo de libros (.6); el panel propio
  guarda el proceso en ambos sistemas. Registro completo en el repo
  UOH: `OMP/EDITORA/docs/decisiones/2026-10-27-*.md` y propuesta PMV en
  `OMP/EDITORA/docs/propuestas/propuesta-plataforma-pmv.md`.
- **HECHO:** Koha tiene API REST v1 viva (lectura pública de biblios en
  MARCXML/marc-in-json) y OAI-PMH operativo — la integración de lectura
  es real hoy; la escritura requiere cuenta staff (pendiente).
- **HECHO:** Editora pasa de «producto editorial propio» a núcleo del
  PMV institucional. OMP queda como fallback del concurso abr-2027.
- **RIESGO:** sin acuerdo escrito de IP/licencia (donación + open
  source AGPL propuesto) no se inicia fase 2. El nombre «Editora» ya
  no cubre el alcance — nombre institucional pendiente.
- **PENDIENTE:** crear BD `editora` (sudo) sigue abierto; contrato del
  repo .6 con Cristóbal; cuenta staff Koha con DTI.
- **HECHO.** Adaptador Koha de lectura implementado y verificado contra
  el Koha real de la UOH: preview + importar registro → borrador con
  procedencia `biblioteca`, `koha_biblio_id` y `koha_url` (V3). Panel
  «Importar de Koha» con preview; catálogo público filtra por origen;
  ficha enlaza al OPAC. Tests 19/19 back + 28/28 front; E2E biblio 100.
  Commit `473f264` (rama `feat/integracion-koha`). Escritura a Koha
  pendiente de credencial staff.
- **HECHO.** BD `editora` creada — PostgreSQL persistente (Flyway V1–V3
  limpio), se cierra el riesgo de datos volátiles en H2.
- **HECHO.** «Ver sitio público» del sidebar al topbar (icono globo,
  pestaña nueva). Commit `04b59a4`.
- **HECHO.** Footer institucional UOH (adaptado del tema DSpace-CRIS)
  + tokens `uoh-*` con los hex del XMLUI de producción en `styles.css`.
  Commit `cf726e7`.
- **HECHO.** Eliminados seeders mock: `DataSeeder` = solo bootstrap del
  admin; borrados `seed/*.json`. BD purgada y repoblada con 8 biblios
  reales de Koha (100, 102–107, 110). Commit `58ba8e1`.
- **HECHO.** Importar de Koha acepta ISBN además de biblionumber
  (resolución vía OPAC público, sin credenciales). Commits `1e3f796`,
  `5077bea`. 20/20 back.
- **HECHO.** Topbar sticky + fixes móviles portados de KPP; CI workflow
  del kit mergeado; nuevo `POST /{id}/estado` (un PUT parcial borraba
  metadata — bug encontrado y cerrado con test). Commits `5f66d2e`,
  `013616d`, `9b73813`. Guía de arranque actualizada: BD ya aprovisionada.
- **HECHO + DECISIÓN.** Editorial y Biblioteca separados como dos
  productos: `/editorial` y `/biblioteca`, home por secciones, nav
  nuevo; propuesta PMV §13 documenta el modelo por módulos. Commit
  `215306d`.
- **HECHO.** Catálogo Editorial poblado con 6 libros reales UOH
  recuperados del ensayo OMP (leída su BD postgres en `~/omp/pgdata`
  :5433): 1814 Rancagua, los dos Booklets «¡Profe, yo también
  existo!», Navegando San Vicente, Guía de escritura académica e
  Iniciativa de aprendizaje autónomo — todos con PDF en la nueva
  «Colección Ensayos UOH». Descartados los 2 submissions técnicos
  (Monografía demo, Prueba Import). PDFs pesados comprimidos con gs
  /ebook (113→19 MB, 80→11 MB). Novedades actualizadas, commit
  `6f9e72d`. Detalle: `OMP/EDITORA/log.md` (noche 7).
- **HECHO.** Lector de PDF propio en `/libros/:slug/leer` (ruta
  inmersiva fuera del layout): pdf.js 6.4 con worker como asset,
  backend con rangos HTTP (206) para descarga progresiva, ajuste
  ancho/página + zoom, teclado y swipe, slider de posición, pantalla
  completa, y retoma donde quedó (localStorage). «Leer en línea» es
  ahora el CTA primario de la ficha. v0.3.0, commit `1415e42`.
- **HECHO.** Marca institucional real en el sitio público: logo
  Unidad de Bibliotecas (media kit) en navbar sticky con blur +
  sombra al scroll + barra de progreso navy; logo UOH blanco en el
  footer navy. `EDITORIAL` → «Editorial UOH». Commit `4c9a2cc`.
- **HECHO.** Página `/nosotros` con misión y visión literales de la
  Propuesta Editorial UOH 2026 (láminas 6–7) + cita de Rectoría.
  Commit `1e08a49`.
- **HECHO.** Rediseño del home: hero navy UOH full-bleed con
  buscador glass, abanico de portadas, stats y lomo de colores de
  la paleta. Commit `d35da3e`.
- **HECHO.** Panel de libros con filtros del modelo de negocio:
  procedencia Editorial/Biblioteca, estado, colección y «falta
  PDF». Commit `b654e95`.
- **HECHO.** Portadas reales para los 6 títulos Editorial,
  renderizadas del PDF (pdftoppm) y subidas por el API. El hero y
  /editorial ya muestran carátulas reales.
- **HECHO.** «Modo lectura»: FAB de accesibilidad en el sitio
  público con tamaño de texto, papel sepia/contraste, tipografía
  legible, regla de lectura, enlaces subrayados y movimiento
  reducido. Commit `60d61f4`.
