 qu---
description: "Stack y metodología de arranque para proyectos nuevos: Angular 22 + Spring Boot + PostgreSQL, con el paquete .devin (skills por gatillo, bitácoras, cadena lab→dev→prod) como metodología de trabajo"
tipo: estandar
estado: vigente
creado: 2026-10-02
tags: [stack, metodologia, angular, spring-boot, postgresql, starterkitcustome]
---

# Stack de arranque — StarterCustomeKit (Full-Stack)

Stack y forma de trabajo estándar para proyectos nuevos (StarterCustomeKit v2,
Frunexis, web empresa, apps móviles). Una sola API sirve a **Angular (web) y
Flutter (mobile)** — por eso el backend es API-first, no monolito. Referencia
de código: **cabid**
(`~/Escritorio/Desarrollo/cabid`). Referencia de metodología: workspace
**repositorios-digitales-uoh** (`~/Escritorio/repositorios-digitales-uoh/.devin`).

# 1. Stack técnico

| Capa | Elección | Detalle |
|---|---|---|
| Frontend | Angular 22 | standalone, signals, TS ~6, RxJS 7.8. Reglas completas en [[Estándares Front-End - Angular]] |
| SSR | Express 5 (`:4000`) | proxifica `/api` al backend con `http-proxy-middleware` |
| Estilos | Tailwind CSS 4 + `@angular/cdk` | headless, sin Material; tokens vía `@theme` |
| Tests front | Vitest | `.spec.ts` junto al archivo |
| Backend | Spring Boot 3.5 + Java 17 | Maven. Deps mínimas: `web`, `data-jpa`, `security`, `validation`, `postgresql` |
| Auth API | JWT HS256 **dual** | Cookie `httpOnly + SameSite=Strict` para web + `Authorization: Bearer` para móvil (Flutter). STATELESS, BCrypt, rate-limit en login. Implementación manual con `javax.crypto` — cero dependencias extra |
| BD | PostgreSQL | BD + usuario dedicados por proyecto (nunca compartir). Hibernate `ddl-auto:update` en dev |
| Config | Variables de entorno | Prefijo `<APP>_`: `<APP>_DB_URL`, `<APP>_DB_USER`, `<APP>_DB_PASSWORD`, `<APP>_JWT_SECRET`, `<APP>_COOKIE_SECURE`, `<APP>_SEED_*` |
| Wiring dev | `ng serve :4200` → `proxy.conf.cjs` → `:8080` | Ojo: el dev-server consume el prefijo `/api` antes de reenviar → el `rewrite` lo antepone de vuelta |
| Tooling | npm, eslint (angular-eslint), prettier | `prettier-plugin-tailwindcss` obligatorio |

## Estructura monorepo

```
<proyecto>/
├── src/  angular.json  proxy.conf.cjs   # front Angular
├── backend/
│   ├── pom.xml
│   └── src/main/java/<pkg>/app/
│       ├── <App>Application.java
│       ├── config/SecurityConfig.java      # filter chain, BCrypt, stateless
│       ├── auth/                           # AuthController, JwtService, JwtAuthFilter
│       ├── <dominio>/                      # entidad + repository + controller público + AdminController
│       └── seed/DataSeeder.java            # admin + datos iniciales (solo primer arranque)
└── docs/backend.md                         # cómo levantar, env vars, endpoints
```

## Endpoints base del kit

```
POST   /api/auth/login     { correo, clave } → perfil + cookie
POST   /api/auth/logout    limpia cookie → 204
GET    /api/auth/me        sesión actual
GET    /api/<recurso>      público (solo visibles/publicados)
*      /api/admin/<recurso> CRUD autenticado
```

## Módulos del kit (port de los dominios SCK a Spring)

Heredados de [[SCK - Estrategia de Alcance]] — mismo alcance, nueva tecnología:
Auth/Users (roles), Notifications, Settings (key-value), Audit (trazabilidad),
Media (storage), Health (estado del sistema). Prioridad: Auth → Health → CRUD
ejemplo; el resto según necesidad del proyecto (YAGNI).

# 2. Metodología de trabajo (modelo DSpace-CRIS)

El workspace `repositorios-digitales-uoh/.devin/` es un **paquete portable**:
copiar la carpeta completa al nuevo proyecto/workspace y ejecutar su bootstrap.

```
.devin/
├── LAUNCHER.md                 # protocolo de adopción: verificar → leer → crear inyector
├── MANIFEST.sha256             # integridad del paquete (verificar antes de usar)
├── plantilla-inyector-skill.md
├── rules/                      # reglas vigentes del workspace
└── skills/                     # 8 skills del ciclo de desarrollo
```

## Skills por gatillo — activación obligatoria

| Señal | Skill | Cuándo |
|---|---|---|
| Encargo amplio/vago o sistema desconocido | `triage-entrada` | antes de tocar archivos |
| Decisión de arquitectura o varias alternativas | `exploracion-analisis` | antes de implementar |
| Crear/migrar/reestructurar una app | `desarrollo-aplicaciones` | antes de escribir código |
| Dependencia, herramienta o patrón nuevo | `interrogatorio-adopcion` | antes de incorporarlo |
| Abrir/cerrar sesión con trabajo pendiente | `continuidad-sesion` | al inicio y al cierre |
| Editar archivos compartidos (logs, bitácoras) | `guarda-edicion-concurrente` | antes de escribir |
| Falla reproducible o resultado roto | `diagnostico-fallas` | antes de corregir |
| Promover entrega o afirmar completitud | `auditoria-evidencia` | después de implementar |

Cadenas habituales: feature sustantiva = triage → exploración → desarrollo →
auditoría; falla = diagnóstico → desarrollo → auditoría; dependencia nueva =
interrogatorio → desarrollo.

## Reglas nucleares

- **Un solo `log.md` por nivel** (raíz = transversal; proyecto = su línea).
  Append-only: lo superado se marca `SUPERADO <fecha>`, no se borra ni reordena.
- **`registro_actividades.md`**: tabla por sesión —
  `Fecha | Tipo | Tarea | Insumos leídos | Salida | Notas`.
- **Agenda única** con IDs estables (`<PRY>-OT-NNN`), ordenada por prioridad.
- **Hecho / hipótesis / decisión separados** siempre — nunca mezclar en una
  misma afirmación.
- **Cadena lab → dev → prod**: nada escribe en producción sin haber pasado la
  cadena. Scripts mutables: `--dry-run` por defecto, `--apply` explícito, sin
  URL de prod como default, manifiesto + rollback declarado antes de escribir.
- **`inyector-skill.md` por proyecto**: tabla tarea→skill→salida esperada,
  cadenas habituales, restricciones, punto de retomada. El agente lo lee al
  abrir sesión en vez de cargar todo el paquete.
- **Mejora gobernada**: una mejora de skill/regla nace como candidata con
  evidencia; solo reemplaza la base con aprobación explícita y rollback.

## Estructura documental por proyecto

```
<proyecto>/
├── README.md                 # frontmatter + estado + actores + principios + índice por necesidad
├── log.md                    # narrativo append-only (## YYYY-MM-DD · título)
├── registro_actividades.md   # tabla de sesiones
├── inyector-skill.md         # enrutamiento local de skills
├── docs/                     # bitacora-<tema>.md, runbooks, investigaciones/, referencias/, tutoriales/
├── input/  output/  data/    # con _superseded/ y _historico/ para lo archivado
└── scripts/
```

# 3. Arranque rápido (checklist)

1. **Front**: `ng new <app>` con SSR, o copiar la base de cabid. Tailwind 4 +
   CDK + Vitest + prettier/eslint según [[Estándares Front-End - Angular]].
2. **Back**: proyecto Maven desde start.spring.io con las 5 deps base; portar
   `config/`, `auth/` y `seed/` de `cabid/backend` como punto de partida.
3. **Wiring**: `proxy.conf.cjs` con rewrite de `/api`; `server.ts` (Express)
   proxifica a `$<APP>_API_URL` (default `http://localhost:8080`).
4. **BD**: `CREATE USER` + `CREATE DATABASE` dedicados; env vars `<APP>_*`.
5. **Metodología**: copiar `.devin/` al proyecto, ejecutar `LAUNCHER.md` →
   generar `inyector-skill.md` local.
6. **Docs**: `README.md` + `log.md` + `registro_actividades.md` + agenda con
   primera entrada `## <fecha> · Inicio del proyecto` (stack, decisiones,
   estructura creada).
7. **Git**: un repo por proyecto; Conventional Commits en español; ramas
   `<tipo>/<descripcion-corta-kebab>`. Documentación y código pueden vivir en
   el mismo repo (a diferencia de UOH, donde la bitácora vive separada del
   código institucional).

# 4. Diferencias respecto al kit anterior (Laravel)

El StarterCustomeKit original era Laravel 12 + Breeze + Livewire/Volt
(`99_Archivo/Proyectos personales/StarterCustomeKit/`). Esta versión lo
**supera** como stack oficial: backend Java/Spring por campo laboral y perfil
empresarial, frontend Angular idéntico a cabid, y metodología `.devin`
incorporada desde el arranque. Las notas `STK-*`/`SCK-*` quedan como
especificación funcional de los dominios a portar, no como stack vigente.
