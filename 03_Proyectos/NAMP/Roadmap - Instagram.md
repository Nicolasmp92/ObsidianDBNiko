---
tipo: plan
proyecto: namp
estado: en-curso
actualizado: 2026-11-18
tags: [instagram, marketing, marca]
---

# Roadmap — Instagram NAMP

Pasos para dejar el perfil de Instagram operativo. La cuenta ya existe
y tiene contenido antiguo (fotos e historias) → hay fase de limpieza.
Material gráfico listo en `02_Outputs/NAMP/2026-11-06-media-kit-instagram/`
(avatar, 3 posts semilla, 4 portadas de destacadas, plantillas, README
del kit). Render multiplataforma: `render.sh` (Linux/macOS) y
`render.ps1` (Windows). Pipeline documentado en la skill
`contenido-instagram` del store.

## Fase 0 — Decisiones (bloquea todo)

- [ ] **Definir handle definitivo.** Candidatos por orden de
  consistencia con la marca: `@namp.cl`, `@namp_ingenieria`,
  `@nampingenieria`. Verificar disponibilidad en instagram.com — el
  mismo handle conviene reservarlo también en LinkedIn/TikTok aunque
  no se usen aún. Si la cuenta actual ya tiene handle, decidir si se
  conserva o se cambia (se puede cambiar sin perder seguidores).
- [ ] **Correo de la cuenta:** pasar a `contacto@namp.cl` (ya recibe
  vía Cloudflare Email Routing → Gmail).
- [ ] **Tipo de cuenta: Profesional/Empresa** — da estadísticas, botón
  de contacto y categoría ("Software" / "Servicio de TI"). Se puede
  convertir una cuenta personal sin perder contenido ni seguidores.

## Fase 1 — Limpieza de la cuenta existente

Hay fotos e historias previas que no representan la marca. Regla:
**archivar primero, eliminar solo lo decidido** — archivar oculta el
contenido sin borrarlo (recuperable desde "Tu actividad → Archivadas").

- [ ] **Posts del feed:** Perfil → cada publicación → ⋯ → *Archivar*.
  Masivo: Menú ☰ → *Tu actividad* → *Fotos y videos* → *Publicaciones*
  → *Seleccionar* → marcar todas → *Archivar* (o *Eliminar* si ya se
  sabe que no sirven).
- [ ] **Historias activas:** desaparecen solas a las 24 h. Para borrar
  una antes: abrirla → ⋯ → *Eliminar*.
- [ ] **Destacadas:** en el perfil, mantener presionada la destacada →
  *Eliminar destacada* (las historias archivadas quedan intactas).
- [ ] **Historias archivadas:** *Tu actividad* → *Archivadas* →
  *Historias* → abrir → ⋯ → *Eliminar* (opcional, no se ven público).
- [ ] **Reels:** mismo flujo que posts (pestaña reels del perfil).
- [ ] **Etiquetadas:** pestaña de etiquetas del perfil → revisar fotos
  personales etiquetadas → ⋯ → *Ocultar de mi perfil* o quitar etiqueta.
- [ ] **Seguidos/bio:** dejar de seguir cuentas ajenas a la marca si
  aplica; limpiar bio antigua (se reescribe en la fase siguiente).

## Fase 2 — Configurar el perfil

- [ ] **Nombre visible:** `NAMP Ingeniería` (indexable en búsqueda de
  IG, mejor que solo "NAMP").
- [ ] **Foto de perfil:** `avatar-instagram.png` (renderizada
  1080×1080 pensada para el crop circular).
- [ ] **Bio** (máx. 150 caracteres), propuesta:
  > Ingeniería de software a medida
  > Consultoría · Desarrollo · Cloud · UX
  > Prueba el demo: demo.namp.cl
- [ ] **Enlace:** `namp.cl` (si después hacen falta varios links,
  evaluar página `/enlaces` propia en namp.cl en vez de Linktree —
  mismo patrón que el linktree UOH).
- [ ] **Botones de contacto** (cuenta profesional): `contacto@namp.cl`
  + WhatsApp `+56 9 6397 8090` (`wa.me/56963978090`).

## Fase 3 — Contenido semilla (antes de difundir el perfil)

Un perfil vacío no convierte. Publicar 3 piezas antes de compartir el
handle con nadie:

- [x] **Post 1 — Lanzamiento:** `post-01-lanzamiento.png` (listo).
  Caption base:
  > Somos NAMP. Ingeniería de software a medida: soluciones limpias,
  > escalables y centradas en resultados. Consultoría, desarrollo
  > y soporte — conversemos en namp.cl
  > #desarrollodesoftware #softwarechile #pymeschile #consultoriati
- [x] **Post 2 — Servicios:** `post-02-servicios.png` (listo 2026-11-18)
  — los 3 servicios reales del sitio espejando las cards de
  `/servicios` (índice de etapa 01–03), CTA "Conversemos". Caption
  sugerido:
  > Un solo equipo para cada etapa: consultoría, desarrollo a medida
  > y soporte continuo. Cuéntanos tu idea en namp.cl
  > #desarrolloamedida #consultoriati #pymeschile
- [x] **Post 3 — Prueba social:** `post-03-kpp.png` (listo 2026-11-18)
  — POS real de `demo.namp.cl` en mockup de navegador, chips "Demo
  abierto" + "Precio fundador $19.990 + IVA", CTA "Explorar el demo".
  Caption sugerido:
  > KaiPetPoint ya está en línea: punto de venta para tiendas de
  > mascotas con ventas, caja, inventario y despachos. Pruébalo libre
  > en demo.namp.cl — precio fundador $19.990 + IVA.
  > #puntodeventa #pos #mascotas #softwarechile
- [x] **Destacadas** (portadas fijas bajo la bio): 4 portadas en
  `destacadas/` (listo 2026-11-18) — `</>` Servicios, grilla
  Proyectos, monitor+play Demo KPP, sobre Contacto.
  **Pendiente:** las historias que alimentan cada destacada
  (`plantilla-historia.html` lista para usar).

## Fase 4 — Operación

- [ ] **Meta Business Suite** (business.facebook.com): vincular la
  cuenta IG → permite programar posts/historias desde el PC y ver
  bandeja unificada. Requiere página de Facebook de NAMP (crearla
  básica, no hace falta alimentarla).
- [ ] **Cadencia realista:** 1 post/semana + historias cuando haya
  avance real (deploys, features, antes/después). Calidad sobre
  volumen — el kit garantiza coherencia visual.
- [ ] **Agregar el handle** al footer de `plantilla-post.html` y
  `plantilla-historia.html` cuando quede definido (zona "Visítanos
  namp.cl" → "@handle · namp.cl").
- [x] Merge de `feat/media-kit-instagram` → `main` en GitHub (`b8c8ad1`,
  2026-11-06 — el isotipo ya está en producción).

## Pendientes externos

- [ ] Revisar el clon obsoleto `Desarrollo/NYEinformatica` (contiene el
  post con datos placeholder — no publicar ese PNG por error).
