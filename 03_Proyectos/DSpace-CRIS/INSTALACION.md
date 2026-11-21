# INSTALACIÓN — DSpace-CRIS 2025.02.00 (receta probada)

Destilado de la bitácora UOH (`repositorios-digitales-uoh/DSPACE-CRIS/`):
es lo que corre el lab local y el servidor institucional. Cada trampa
citada ocurrió de verdad — no saltárselas.

## 0 · Requisitos

| Pieza | Detalle |
|---|---|
| Docker | Docker Desktop ≥28 con Compose v2 (Windows) o docker+plugin compose (Linux) |
| Imágenes | `4science/dspace-cris`, `-cli`, `-solr`, `-angular` — tag `dspace-cris-2025.02.00` (= DSpace 9.2, esquema `9.0.2025.02.13`) |
| Código | `git clone https://github.com/4Science/DSpace.git` → `git checkout dspace-cris-2025.02.00` |
| Puertos | 8080 (REST), 4000 (Angular SSR), 5432 (Postgres 15), 8983 (Solr) |
| RAM recomendada | ≥8 GB libres (JVM + Solr + Postgres en contenedores) |

## 1 · Levantar el stack

```bash
cd dspace-cris-lab   # el clon de 4Science/DSpace en el tag

# .env mínimo:
#   COMPOSE_PROJECT_NAME=dcris25
#   DSPACE_VER=dspace-cris-2025.02.00

docker compose up -d
```

El entrypoint del backend corre `database repair` + `migrate` solo — la
primera vez tarda un par de minutos. Verificar:

```bash
docker compose ps                                                  # todos Up
curl -s http://localhost:8080/server/api | head -c 200             # backend
curl -s "http://localhost:8983/solr/admin/info/system?wt=json"     # solr
# Angular SSR: http://localhost:4000
```

## 2 · Administrador (una sola vez)

```bash
docker compose -f docker-compose-cli.yml run --rm dspace-cli \
  create-administrator -e admin@cliente.tld -f Nombre -l Apellido -p '<clave>' -c es
```

## 3 · Entidades CRIS — OBLIGATORIO (trampa documentada)

Sin esto las cargas con workflow fallan. Son dos XML que ya vienen en
`dspace/config/entities/`:

```bash
docker compose -f docker-compose-cli.yml run --rm dspace-cli \
  initialize-entities -f relationship-types.xml

docker compose -f docker-compose-cli.yml run --rm dspace-cli \
  initialize-entities -f correction-relationship-types.xml
```

> **Por qué:** el servicio de solicitudes de corrección exige las 12
> relaciones `isCorrectionOfItem`; su ausencia hizo fallar la primera carga
> UOH (`relationship_type=0`). Además crea los 13 entity types
> (Publication, Person, OrgUnit, Journal, Project, Funding…).

## 4 · Datos iniciales (opcional según alcance)

```bash
docker compose -f docker-compose-cli.yml run --rm \
  -v "$PWD/mis-csv:/tmp/csv" dspace-cli \
  metadata-import -f /tmp/csv/archivo.csv -e admin@cliente.tld -v -w
```

- `-v -w` = validación + workflow. Patrón admin = `dspace-cli <comando>`.
- Los CSV del cliente van en una carpeta montada (`mis-csv:/tmp/csv`).
- Si el cliente trae campos custom, el esquema de metadatos se registra
  primero (lección UOH: `metadata-import` rechaza encabezados desconocidos).

## 5 · Persistencia y operación

| Volumen | Contenido |
|---|---|
| `pgdata` | toda la BD |
| `assetstore` | bitstreams (PDFs, fotos) |
| solr | índices de búsqueda |

- Apagar: `docker compose down` · Encender: `docker compose up -d` (datos intactos).
- Admin recurrente: `docker compose -f docker-compose-cli.yml run --rm dspace-cli <cmd>`.

## 6 · Trampas conocidas (de la bitácora UOH)

| Trampa | Síntoma | Fix |
|---|---|---|
| Falta `correction-relationship-types.xml` | `metadata-import -w` falla | §3 |
| Docker Desktop Windows cae | exit 255, API 500 | `wsl -t docker-desktop` y reintentar |
| Sin restart policy en el compose oficial | contenedores no vuelven tras caída | agregar `restart: unless-stopped` |
| Campos ocultos en vista "todos los metadatos" | metadatos visibles que no deberían | `metadata-security.cfg` (`settings = [0 1]` = solo admin) — mecanismo D8 |
| SSR/Angular sin `allowedHosts` | host rechazado tras proxy | configurar host en el frontend |

## 7 · Hacia producción del cliente

- Preferir **Linux** + Docker con `restart: unless-stopped` o systemd
  (propuesta completa en `DSPACE-CRIS/docs/servidor/propuesta-systemd-cris.md`
  del repo UOH).
- Traefik/nginx delante para HTTPS; puertos internos sin publicar.
- Backups: `pg_dump` cron + volumen assetstore (igual que KPP).
- NO clonar el lab con datos UOH: deploy desde tag limpio + seed propio.
