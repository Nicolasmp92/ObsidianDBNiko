---
status: Pendientes
proyecto: kaipetpoint
fase: pmv
criticidad: critica
esfuerzo: M
prioridad: urgente
vencimiento: 2026-10-09
---
_Objetivo: adquirir hosting para desplegar KaiPetPoint y comenzar pruebas reales con la clientela._

## Requisitos del stack a alojar

- Backend: Spring Boot (`mvn spring-boot:run`, API :8084) → JVM + build Maven.
- Frontend: Angular con SSR (`npm start` :4204, SSR :4004) → Node.js.
- BD: PostgreSQL (`kaipetpoint` / `kaipetpoint_user`).

## Comparación de opciones (evaluado 2026-10-22)

El stack a alojar es el mismo en todos los proyectos nuevos (Spring Boot + Angular SSR + PostgreSQL ≈ 1–1.5 GB RAM por stack), ya dockerizado en `feat/deploy`. Los sitios estáticos quedan en GitHub Pages ($0).

| Opción | Recursos | Costo/mes | Notas |
|---|---|---|---|
| **Hetzner CX33** (US East) | 4 vCPU / 8 GB / 80 GB | ~$10.6 | Por hora, sin permanencia. Backups +20%. Alza de precios abr/jun 2026 ya aplicada |
| **Hostinger KVM 2** | 2 vCPU / 8 GB / 100 GB | $8.99 (24 meses prepago, ~$216 upfront; renueva $14.99) | Backups semanales incluidos, dominio gratis 1er año, DC en Brasil |
| **Vultr São Paulo** | 2 vCPU / 4 GB / 80 GB | ~$20–30 | Menor latencia a Chile (~60-80 ms vs ~130 ms US East); SP cobra ~1.5× |
| **PaaS** (Railway/Render/Fly) | por servicio | $15–60 **por stack** → $75–300 por 5 | Cero ops; no escala bien para multi-proyecto |
| **Oracle Free Tier** | 4 ARM / 24 GB | $0 | Solo staging: riesgo de reclamación y capacidad escasa |
| **VPS en Chile** (inan.cl, hostnet.cl) | 2 vCPU / **4 GB** | $15.000–22.000 CLP (~$16–23 USD) | Latencia local ~10 ms vs ~50 ms SP→Stgo; la mitad de RAM por ~2.5× el precio. No compensa (~40 ms no valen 3× el costo) |
| **GCP `southamerica-west1`** (Santiago) | 4 GB | ~$30–40 USD | DC real en Chile; precio cloud enterprise, no VPS |

Latencias medidas (WonderNetwork/Check-Host, oct 2026): Stgo→SP ≈ 49–58 ms · Stgo→DC local ≈ 5–15 ms · Stgo→Miami/US East ≈ 110–150 ms. Riesgo de peering: algunos ISPs chilenos rutean a Brasil vía USA (~150 ms) → verificar con ping post-contratación.

**Recomendación:** VPS 8 GB + Docker + Dokploy/Coolify (panel PaaS self-hosted: git push → deploy, HTTPS automático vía Caddy/Traefik — requerido por la cámara del escáner — y backups programados). Una sola instancia PostgreSQL con una BD por proyecto → `pg_dump` único. Con el modelo SaaS de KPP, cada instancia cliente ≈ 1 stack extra (~1 GB); 8 GB ≈ 6 stacks antes de escalar a 16 GB (~$13–19/mes).

Dominio: uno solo + subdominios por proyecto (`kpp.dominio.cl`, `beanflow.dominio.cl`, …).

## Tareas

- [x] Evaluar opciones de hosting según costo/esfuerzo: VPS único con Docker (Hetzner, DigitalOcean, Contabo) vs PaaS administrado (Render, Railway, Fly.io) vs VPS + BD administrada. ✅ 2026-10-22 — ver tabla arriba.
    
- [x] Estimar costo mensual de cada opción (app + PostgreSQL + backups). ✅ 2026-10-22 — VPS ≈ $9–11/mes total; PaaS ≈ $15–60/mes por stack.
    
- [ ] **Contratar Hostinger KVM 2 (DC Brasil, 24 meses, ~$8.79/mes)** — decisión tomada 2026-10-22 vía análisis de 3 ramas; ver [[MOC - Empresa]] y log de Empresa. Falsación: uptime <99.5% en 60 días → migrar a Hetzner CX33.
    
- [x] Definir estrategia de despliegue: Dockerfile del backend (jar) + front SSR + compose ✅ 2026-10-09 — `backend/Dockerfile` (multi-etapa Maven→JRE), `Dockerfile` raíz (Angular build→Node SSR), `docker-compose.yml` (db+backend+frontend).
    
- [x] Verificar build y stack reales ✅ 2026-10-24 — `docker compose build` + `up` OK en local: Postgres fresco corre las 15 migraciones Flyway + seed; login `POST /api/auth/login` 200 con JWT vía Caddy→SSR→backend. Incluye `Caddyfile` (HTTPS automático con `DOMAIN`, o `:80` por IP). Commit `14a6de8` en `main`. Fix incluido: `http-proxy-middleware` movido a `dependencies` (era runtime del SSR).
    
- [ ] Configurar variables de entorno `KAIPETPOINT_*` en el ambiente remoto (BD, JWT, etc.) — `.env.example` ya documenta todas las vars del compose.
    
- [ ] HTTPS + dominio (Caddy/Traefik con certificado automático, o el que entregue el PaaS) — `Caddyfile` listo: basta `DOMAIN=kpp.dominio.cl` en `.env`. Pendiente comprar/asignar dominio.
    
- [ ] Ambiente separado de pruebas (staging) para que la clientela pruebe sin mezclar datos reales.
    
- [ ] Backups automáticos de PostgreSQL.
    
- [ ] Smoke post-deploy: login, venta descuenta stock, comprobante, reportes.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/deploy
```
