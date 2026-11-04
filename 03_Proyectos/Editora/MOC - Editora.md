---
tipo: proyecto
proyecto: editora
estado: activo
actualizado: 2026-10-27
tags: [editorial, catalogo, libros, acceso-abierto, angular, spring-boot, producto-propio]
---
# 📚 MOC — Editora

Plataforma editorial para editoriales pequeñas: catálogo público por
colecciones, ficha de libro con descarga y cita, y panel de gestión. Más
adelante suma convocatorias con evaluación e interoperabilidad (OAI-PMH,
DOI).

- **Repo:** `~/Escritorio/Desarrollo/editora` (GitHub `Nicolasmp92/editora`, **privado**).
- **Origen:** generado desde [[MOC - StarterCustomeKit|StarterCustomeKit v2]] con el remoto `template`.

## Navegación por necesidad

- **Quiero ver qué se hizo y cuándo** → `log.md` de esta carpeta (contexto y decisiones) + `log.md` del repo (detalle técnico)
- **Quiero la tabla de sesiones** → `registro_actividades.md`
- **Quiero el alcance y las fases** → `docs/alcance.md` en el repo · [[EDT - Roadmap y fases]]
- **Quiero levantar el stack**:
  - `cd backend && EDITORA_DB_URL='jdbc:h2:mem:editora;DB_CLOSE_DELAY=-1' EDITORA_DB_USER=sa EDITORA_DB_PASSWORD='' mvn spring-boot:run` (API en :8086; usar H2 mientras no exista la BD `editora`);
  - `npm start` en la raíz (:4206);
  - sitio público en `http://localhost:4206`, panel en `http://localhost:4206/panel`;
  - login `nikolasmp92@gmail.com` / `niko9214`.
- **Quiero ver las tareas** → [[Desarrollo]] (kanban maestro)

## Dominios

| Dominio | Entidades | Estado |
|---|---|---|
| Catálogo | `colecciones`, `libros` (+ archivos portada/PDF en disco) | Fase 1 completa: API pública y admin, sitio público y panel |
| Convocatorias | — | Fase 2 (pendiente) |
| Interoperabilidad | — | Fase 3: OAI-PMH, Scholar completo, exportación de citas |
| Plataforma | `usuarios`, JWT dual, preferencias | Heredado del kit |

## Decisiones estructurales vigentes

- **Producto genérico, no un desarrollo para un cliente.** Sin marca, datos
  ni documentos de la UOH. El seed es ficticio. La UOH es solo el *caso de
  diseño*.
- **Una instancia = una editorial** (sin multi-tenant). La identidad se
  configura en `features/catalogo/editorial.ts` hasta que exista un panel
  de ajustes.
- **Archivos validados por firma de bytes**, no por extensión ni
  Content-Type del cliente. Las rutas las arma el servidor.
- **Portada tipográfica generada** cuando no hay imagen: un catálogo sin
  portadas igual se ve editorial.
- **Sitio público en `/` y panel en `/panel`**: el SSR sirve el catálogo
  sin sesión.
- **Bloque de puertos 8086 / 4206 / 4006**, BD `editora` / `editora_user`.
