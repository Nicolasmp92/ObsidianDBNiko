---
tipo: plan
proyecto: namp
estado: en-curso
actualizado: 2026-11-06
tags: [instagram, marketing, marca]
---

# Roadmap — Instagram NAMP

Pasos para dejar el perfil de Instagram operativo. Material gráfico ya
listo en `02_Outputs/NAMP/2026-11-06-media-kit-instagram/` (avatar, post
de lanzamiento, plantillas, README del kit).

## Fase 0 — Decisiones (bloquea todo)

- [ ] **Definir handle.** Candidatos por orden de consistencia con la
  marca: `@namp.cl`, `@namp_ingenieria`, `@nampingenieria`. Verificar
  disponibilidad en instagram.com — el mismo handle conviene reservarlo
  también en LinkedIn/TikTok aunque no se usen aún.
- [ ] **Correo de la cuenta:** usar `contacto@namp.cl` (ya recibe vía
  Cloudflare Email Routing → Gmail).
- [ ] **Tipo de cuenta: Profesional/Empresa** — da estadísticas, botón
  de contacto y categoría ("Software" / "Servicio de TI").

## Fase 1 — Crear y configurar el perfil

- [ ] Crear la cuenta en la app de IG (la configuración fina solo se
  puede desde el móvil).
- [ ] **Nombre visible:** `NAMP Ingeniería` (el nombre es indexable en
  búsqueda de IG, mejor que solo "NAMP").
- [ ] **Foto de perfil:** `avatar-instagram.png` (ya renderizada
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

## Fase 2 — Contenido semilla (antes de difundir el perfil)

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
  Servicios, portafolio Proyectos, carrito/monitor Demo KPP, sobre
  Contacto. Las historias que alimentan cada destacada salen de
  `plantilla-historia.html`.

## Fase 3 — Operación

- [ ] **Meta Business Suite** (business.facebook.com): vincular la
  cuenta IG → permite programar posts/historias desde el PC y ver
  bandeja unificada. Requiere página de Facebook de NAMP (crearla
  básica, no hace falta alimentarla).
- [ ] **Cadencia realista:** 1 post/semana + historias cuando haya
  avance real (deploys, features, antes/después). Calidad sobre
  volumen — el kit garantiza coherencia visual.
- [ ] **Agregar el handle** al footer de `plantilla-post.html` y
  `plantilla-historia.html` cuando exista (zona "Visítanos namp.cl"
  → "@handle · namp.cl").
- [ ] Merge de `feat/media-kit-instagram` → `main` en GitHub (el PNG
  ya está en el vault, pero el espejo fuente debe quedar en main).

## Pendientes externos

- [ ] Revisar el clon obsoleto `Desarrollo/NYEinformatica` (contiene el
  post con datos placeholder — no publicar ese PNG por error).
