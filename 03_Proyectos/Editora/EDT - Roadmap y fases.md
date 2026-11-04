---
tipo: roadmap
proyecto: editora
actualizado: 2026-10-27
---
# EDT — Roadmap y fases

Volver a [[MOC - Editora]]. El contrato completo está en `docs/alcance.md`
del repo.

| Fase | Contenido | Criterio de salida | Estado |
|---|---|---|---|
| 1 — Catálogo | Colecciones, libros, portada/PDF, sitio público, panel | Un editor publica un libro y el lector lo descarga | ✅ 2026-10-27 |
| 2 — Convocatorias | Llamado, postulación con archivo, evaluadores, decisión | Una postulación de prueba recorre todo el ciclo | Pendiente |
| 3 — Interoperabilidad | OAI-PMH `oai_dc`, `citation_*` absolutas, exportación BibTeX/RIS | Un validador OAI acepta `Identify` y `ListRecords` | Pendiente |
| 4 — Producción | EPUB/audio, DOI vía Crossref, estadísticas de descarga | Según demanda real (regla de graduación) | — |

## Siguientes pasos concretos

- [ ] Crear la BD PostgreSQL `editora` (ver [[Proyectos - Setup y arranque]]) y dejar de depender de H2
- [ ] `citation_pdf_url` absoluta (origen público configurable)
- [ ] Panel de ajustes: identidad de la editorial (nombre, sello, correo, logo), hoy constante en el código
- [ ] Fase 2: modelo de convocatoria y postulación
- [ ] Demo pública para el portafolio (hosting en el VPS Dokploy, ver [[Estado - Infraestructura NAMP]])

## Fuera de alcance (con razón)

- Multi-tenant: fue lo que desbordó el kit v1. Una instancia es una editorial.
- Pagos: el caso inicial es acceso abierto.
- Importador desde OMP: solo si un cliente real lo pide.
