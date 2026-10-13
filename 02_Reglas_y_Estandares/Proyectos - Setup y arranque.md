---
tipo: estandar
tema: setup-proyectos
actualizado: 2026-10-09
---
# 🚀 Cómo levantar cada proyecto

Guía única para arrancar cualquier proyecto en este equipo (o uno nuevo). Todos los repos viven en `~/Escritorio/Desarrollo/` y en GitHub `Nicolasmp92`.

## Requisitos comunes (una sola vez)

| Herramienta | Versión | Verificar |
|---|---|---|
| Java | 17 | `java -version` |
| Maven | 3.8+ | `mvn -v` |
| Node + npm | LTS | `node -v` / `npm -v` |
| PostgreSQL | 17 corriendo en :5432 | `pg_isready` |
| Flutter | solo Sconect | `flutter --version` |

## Tabla resumen

| Proyecto | Carpeta local | API | Dev | SSR | BD PostgreSQL |
|---|---|---|---|---|---|
| StarterCustomeKit | `StarterCustomeKit` | 8081 | 4201 | 4001 | `sck` / `sck_user` |
| Frunexis | `Frunexis` | 8082 | 4202 | — | `frunexis` / `frunexis_user` |
| Sconect | `sconect` (monorepo) | 8083 | — (Flutter) | — | `sconect` |
| KaiPetPoint | `kaipetpoint` | 8084 | 4204 | 4004 | `kaipetpoint` / `kaipetpoint_user` |
| BeanFlow | `BeanFlow` | 8085 | 4205 | — | `beanflow` / `beanflow_user` ⚠️ |
| MP | — | — | — | — | sin repo aún |

**Login unificado en todos**: `nikolasmp92@gmail.com` / `niko9214` (seed). En Sconect el rol es `titular`.

## Secuencia estándar (Spring Boot + Angular)

```bash
# 0) Clonar (solo si falta)
cd ~/Escritorio/Desarrollo
git clone https://github.com/Nicolasmp92/<repo>.git && cd <repo>

# 1) Base de datos (una sola vez; sudo postgres)
sudo -u postgres psql -c "CREATE USER <bd>_user PASSWORD '<bd>_dev';"
sudo -u postgres psql -c "CREATE DATABASE <bd> OWNER <bd>_user;"
# ⚠️ un comando por -c: CREATE DATABASE no puede ir en el mismo -c que CREATE ROLE

# 2) Backend (terminal 1)
cd backend && mvn spring-boot:run        # API en :80XX

# 3) Frontend (terminal 2)
npm install                              # solo la primera vez
npm start                                # dev server en :42XX
```

## Notas por proyecto

### StarterCustomeKit (8081/4201)
Kit base Angular 22 SSR + Spring Boot + PostgreSQL del que nacen los demás. BD `sck` (clave dev `sck_dev`).

### Frunexis (8082/4202)
Gestión agrícola. BD `frunexis`; Hibernate `ddl-auto: update` en dev (no Flyway).

### Sconect (8083 + Flutter)
Monorepo: `backend/` es Spring Boot (`cd backend && mvn spring-boot:run`); `app/` es Flutter (`cd app && flutter run`). BD `sconect`. Webhooks n8n documentados en el README del repo.

### KaiPetPoint (8084/4204/4004)
POS multi-sucursal. BD `kaipetpoint` (clave dev `kaipetpoint_dev`), migraciones Flyway automáticas al arrancar. Fallback H2: `KAIPETPOINT_DB_URL=jdbc:h2:mem:kpp;DB_CLOSE_DELAY=-1` (datos volátiles). SSR en :4004 (`npm run serve:ssr` tras `npm run build`).

### BeanFlow (8085/4205)
POS de restaurante. ⚠️ **BD `beanflow`/`beanflow_user` nunca se aprovisionó** — corre en H2 en memoria:
```bash
BEANFLOW_DB_URL=jdbc:h2:mem:beanflow;DB_CLOSE_DELAY=-1 \
SPRING_FLYWAY_LOCATIONS=classpath:db/migration-h2 \
mvn spring-boot:run
```
Para persistir: crear la BD con la secuencia estándar y arrancar sin las env vars.

### MP
Sitio web corporativo en levantamiento de requerimientos — **no tiene repo todavía**. Estado y pendientes en [[MOC - MP]].

## Troubleshooting rápido

- **`La dirección ya se está usando`** → otro backend sigue vivo: `ss -tlnp | grep 80XX` y `kill <pid>`.
- **Auth PostgreSQL falla** → verificar que el rol existe (`sudo -u postgres psql -c '\du'`) y que la BD fue creada en un `-c` separado.
- **Datos desaparecen al reiniciar** → estás en H2; falta crear la BD PostgreSQL del proyecto.
- **Login 401** → el seed corre solo si la BD estaba vacía al primer arranque; revisar `KAIPETPOINT_SEED_*` o el seeder del proyecto.
