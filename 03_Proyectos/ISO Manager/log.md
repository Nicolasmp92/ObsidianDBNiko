# log.md — ISO Manager (vault)

Bitácora de proyecto append-only. Detalle técnico completo en el `log.md`
del repo.

## 2026-10-25 — v0.1.0: matriz de cumplimiento operativa

**Hecho.** Proyecto generado desde StarterCustomeKit `main` (git archive
+ rebrand, patrón TaskFlow). Dominio `items` del kit reemplazado por
`cumplimientos`: normas ISO → requisitos → matriz de cumplimiento 1:1 con
estado (pendiente/en_proceso/cumple/no_conforme), responsable, fecha
objetivo, evidencia y comentarios append-only. Catálogo sembrado: ISO
9001/14001/45001/27001, ~66 cláusulas.

**Hecho.** Verificación completa: `mvn test` ✓, `npm test` 29/29 ✓,
`ng lint` ✓, build SSR ✓, smoke E2E H2 ✓ (login, matriz, PUT, comentarios,
validaciones 400/401, SSR redirect + proxy).

**Decisión.** Se adelantó el desarrollo respecto del plan
("post-F3, cuando KPP facture") — registrado como decisión del usuario.
El fit con el kit fue el esperado (roles, usuarios, alertas por vencimiento).

**Repo.** `github.com/Nicolasmp92/isomanager` (privado). Local:
`Desarrollo/isomanager`, puertos 8086/4206/4006.

**Siguiente.** Módulos del PMV en backlog: documentos controlados,
auditorías + acciones correctivas, indicadores, capacitaciones,
obligaciones legales.

## 2026-10-25 — v0.2.0: panel de responsabilidades + foco minero

**Hecho.** El usuario orientó el producto a procesos de la **minería**.
Nuevo panel `/responsabilidades`: cada norma tiene un dueño de
certificación (admin asigna, resto lee) — la persona que responde por
cargar documentación/evidencia de esa norma. Vista con avance por estado
y vencidos por norma.

**Hecho.** Catálogo suma ISO 55001 (activos) e ISO 50001 (energía) —
ambas muy exigidas en faenas. 6 normas, ~94 cláusulas.

**Hecho.** Verificación completa + push `0b4a03f`. Próxima iteración:
madurar el modelo con gente del rubro (qué significa "cargar
documentación": ¿archivos adjuntos? ¿documentos controlados?).

## 2026-10-25 — Cierre de sesión · punto de retomada

**Estado.** `main` = `0b4a03f` pusheado; v0.2.0 verificada; procesos dev
apagados. Working tree limpio.

**Retomar.** Levantar backend H2 (comando en `log.md` del repo o README)
+ `npm start`; la decisión abierta con el rubro: ¿el dueño de norma debe
tener permiso exclusivo para cargar evidencia? ¿Evidencia = adjunto real
(documento controlado) o referencia de texto? Backlog PMV: documentos
controlados, auditorías, indicadores, capacitaciones, legales.
