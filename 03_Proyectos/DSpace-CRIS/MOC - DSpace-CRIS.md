---
tipo: proyecto
proyecto: dspace-cris
estado: pipeline
actualizado: 2026-11-20
tags: [dspace-cris, cris, repositorio-institucional, trabajo-externo, docker]
---

# MOC — DSpace-CRIS (producto de arranque rápido)

Trabajo independiente de la línea UOH. Nació por un encargo externo de
instalación y puesta en marcha, pero **el producto real es el kit
reutilizable**: metodología + receta + baseline de cumplimiento chileno
(ANID/OpenAIRE/COAR) para que el próximo encargo similar sea rápido.
Reutiliza el conocimiento de la bitácora del lab UOH con frontera estricta:
**cero datos ni configuración UOH**.

## Navegación por necesidad

- **Quiero ver qué pasó** → `log.md` de esta carpeta
- **Quiero la tabla fecha/actividad/evidencia** → `registro_actividades.md`
- **Quiero la metodología de trabajo por fases** → `METODOLOGIA.md`
- **Quiero el estándar chileno exigible (ANID)** → `ESTANDARES-CL.md`
- **Quiero decirle al cliente qué datos entregar** → `DATOS-CLIENTE.md` (enviable tal cual)
- **Quiero la receta de instalación probada** → `INSTALACION.md`
- **Quiero el lab/clon del código** → `C:\Users\Niko\dspace-cris-lab`
- **Quiero la fuente de conocimiento UOH** → `C:\Users\Niko\Desktop\repositorios-digitales-uoh\DSPACE-CRIS\` (log.md, docs/servidor, docs/tutoriales, docs/referencias)

## Ficha

- **Cliente:** contacto externo — alcance, dominio y servidor destino por definir
- **Repo/código:** `C:\Users\Niko\dspace-cris-lab` (clon `4Science/DSpace` @ tag `dspace-cris-2025.02.00`, detached HEAD) — es el lab ya montado en este PC; decidir si el deploy del cliente forkea desde aquí o clon limpio
- **Stack:** DSpace-CRIS **2025.02.00** (= DSpace 9.2) vía Docker Compose — backend REST :8080, Angular SSR :4000, PostgreSQL 15 :5432, Solr :8983, Matomo opcional, CLI por `docker-compose-cli.yml`
- **Base de conocimiento:** `repositorios-digitales-uoh/DSPACE-CRIS/` (bitácora 3 meses: cargas, entidades, metadatos, ANID, servidor)

## Pendientes destacados (detalle en log.md)

- Definir alcance con el cliente: dominio, servidor (propio/VPS/nube), HTTPS, usuarios admin, volumen de datos inicial
- Decidir si el lab de este PC se reusa como base o se arma clon limpio para el cliente
- Checklist de puesta en marcha: compose → migración → admin → `initialize-entities` → verificación
- Cotización/alcance formal del trabajo (instalación vs. instalación + datos + tema)
