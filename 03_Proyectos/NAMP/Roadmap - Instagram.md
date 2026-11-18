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

## Fase 0 — Decisiones (resuelta 2026-11-18 con datos de namp.cl)

- [x] **Handle: `@namp.cl`** (primario) — los puntos son válidos en
  usernames de IG y calza 1:1 con el dominio. Fallbacks en orden:
  `@nampingenieria` → `@namp_ingenieria`. Reservar el mismo handle en
  LinkedIn/TikTok aunque no se usen aún. No verificable remoto (IG
  sirve muro de login a bots): si la cuenta actual ya tiene otro
  handle, cambiarlo — se puede sin perder seguidores.
- [x] **Correo de la cuenta: `contacto@namp.cl`** — ya recibe vía
  Cloudflare Email Routing → Gmail (verificado 2026-10-25).
- [x] **Tipo de cuenta: Profesional/Empresa** — namp.cl se define como
  "Consultora de servicios informáticos" (og:description) y vende
  servicios + productos: categoría **Empresa de software** (o
  "Servicio de TI"). Da estadísticas, botones de contacto y Meta
  Business Suite. Convertir una personal no pierde contenido ni
  seguidores.
- [x] **Nombre visible: `NAMP Ingeniería`** — igual que `og:site_name`
  y `<title>` del sitio; indexable en búsqueda de IG.
- [x] **Bio** (máx. 150 chars, derivada del og:description del sitio):
  > Consultora de servicios informáticos — Santiago, Chile
  > Desarrollo a medida · consultoría · soporte
  > Pruébalo: demo.namp.cl
- [x] **Enlace:** `namp.cl` (si hacen falta varios links, evaluar
  `/enlaces` propio en vez de Linktree — patrón linktree UOH).
- [x] **Botones de contacto:** `contacto@namp.cl` + WhatsApp
  `+56 9 6397 8090` (`wa.me/56963978090` — el del footer/contacto).

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

## Fase 2 — Configurar el perfil (aplicar lo resuelto en Fase 0)

- [ ] **Nombre visible:** `NAMP Ingeniería`.
- [ ] **Foto de perfil:** `avatar-instagram.png` (renderizada
  1080×1080 pensada para el crop circular).
- [ ] **Bio:** la de Fase 0 (verificada ≤150 caracteres).
- [ ] **Enlace:** `namp.cl`.
- [ ] **Botones de contacto** (cuenta profesional): `contacto@namp.cl`
  + WhatsApp `+56 9 6397 8090` (`wa.me/56963978090`).
- [x] **Handle `@namp.cl`** ya integrado en plantillas y los 3 posts
  (footer "@namp.cl · namp.cl", historia "@namp.cl") — re-render hecho
  2026-11-18.

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
- [x] ~~**Agregar el handle**~~ — `@namp.cl` ya está en las piezas
  (resuelto en Fase 0).
- [x] Merge de `feat/media-kit-instagram` → `main` en GitHub (`b8c8ad1`,
  2026-11-06 — el isotipo ya está en producción).

## Pendientes externos

- [ ] Revisar el clon obsoleto `Desarrollo/NYEinformatica` (contiene el
  post con datos placeholder — no publicar ese PNG por error).
