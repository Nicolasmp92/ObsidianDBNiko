---
tipo: plan
proyecto: namp
estado: en-curso
actualizado: 2026-11-06
tags: [instagram, marketing, marca]
---

# Roadmap — Instagram NAMP

Pasos para dejar el perfil de Instagram operativo. La cuenta ya existe
y tiene contenido antiguo (fotos e historias) → hay fase de limpieza.
Material gráfico listo en `02_Outputs/NAMP/2026-11-06-media-kit-instagram/`
(avatar, post de lanzamiento, plantillas, README del kit).

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

- [ ] **Post 1 — Lanzamiento:** `post-01-lanzamiento.png` (listo).
  Caption base:
  > Somos NAMP. Ingeniería de software a medida: soluciones limpias,
  > escalables y centradas en resultados. Consultoría, desarrollo,
  > cloud y diseño UX/UI — conversemos en namp.cl
  > #desarrollodesoftware #softwarechile #pymeschile #consultoriati
- [ ] **Post 2 — Servicios:** copiar `plantilla-post.html` →
  `post-02-servicios.html`, titular tipo "Todo lo que tu negocio
  necesita en un solo equipo", CTA "Agenda una llamada". Renderizar
  con `render.ps1`.
- [ ] **Post 3 — Prueba social:** KaiPetPoint con captura de
  `demo.namp.cl` (POS real en producción). Caption: producto vivo,
  demo abierto, precio fundador $19.990+IVA.
- [ ] **Destacadas** (historias fijas bajo la bio): crear 3–4 portadas
  con `plantilla-destacada.html`, cambiando solo el glifo: `</>`
  Servicios, portafolio Proyectos, monitor Demo KPP, sobre Contacto.
  Las historias que alimentan cada destacada salen de
  `plantilla-historia.html`.

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
- [ ] Merge de `feat/media-kit-instagram` → `main` en GitHub (el PNG
  ya está en el vault, pero el espejo fuente debe quedar en main).

## Pendientes externos

- [ ] Revisar el clon obsoleto `Desarrollo/NYEinformatica` (contiene el
  post con datos placeholder — no publicar ese PNG por error).
