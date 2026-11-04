---
tipo: pipeline-ideas
estado: activo
actualizado: 2026-10-22
tags: [empresa, ideas, backlog-productos]
---
# Ideas — Pipeline de productos

Ideas de productos futuros. Regla: anotar y soltar — nada entra al kanban de [[Desarrollo]] hasta que tenga cliente potencial o fase propia en el roadmap de [[MOC - Empresa]].

## 💡 ISO Manager (idea, 2026-10-22 → ✅ proyecto, 2026-10-25)

**Estado: en desarrollo** — v0.1.0 con matriz de cumplimiento operativa, ver [[MOC - ISO Manager]] y `github.com/Nicolasmp92/isomanager` (privado).

Sistema de gestión de cumplimiento normativo para empresas certificadas o en proceso de certificación ISO (9001 calidad, 14001 medioambiente, 45001 SST, 27001 seguridad de la información).

**Problema:** las empresas grandes mantienen sus sistemas de gestión en Excel + carpetas: documentos controlados sin versionado real, auditorías que se olvidan, no conformidades sin seguimiento, obligaciones legales dispersas. Cada re-certificación es un parto.

**Qué llevaría (PMV tentativo):**

- Matriz de cumplimientos: requisitos de la norma → estado, responsable, fecha límite, evidencia.
- Documentos controlados: versionado, aprobación, distribución, obsoletos.
- Auditorías internas: plan anual, hallazgos, no conformidades con acciones correctivas y fecha de cierre.
- Indicadores del sistema de gestión + alertas por vencimiento.
- Registro de capacitaciones y obligaciones legales aplicables.

**Fit con el stack:** altísimo — es literalmente el dominio de [[MOC - StarterCustomeKit|SCK]] (roles, auditoría/logs, documentos, notificaciones por vencimiento). Reusa la misma infra del VPS como SaaS multi-tenant (~1 GB/instancia).

**Mercado:** empresas certificadas ISO en Chile/LatAm que hoy pagan consultores o usan IsoTools (caro). Venta por el mismo canal que KPP una vez que haya casos de éxito.

**Cuándo atacar:** después de F3 del roadmap — necesita que KPP ya esté facturando. Mientras tanto esta idea vive aquí.
