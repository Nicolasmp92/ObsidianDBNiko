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

## Tareas

- [ ] Evaluar opciones de hosting según costo/esfuerzo: VPS único con Docker (Hetzner, DigitalOcean, Contabo) vs PaaS administrado (Render, Railway, Fly.io) vs VPS + BD administrada.
    
- [ ] Estimar costo mensual de cada opción (app + PostgreSQL + backups) y elegir.
    
- [x] Definir estrategia de despliegue: Dockerfile del backend (jar) + front SSR + compose ✅ 2026-10-09 — `backend/Dockerfile` (multi-etapa Maven→JRE), `Dockerfile` raíz (Angular build→Node SSR), `docker-compose.yml` (db+backend+frontend) en rama `feat/deploy`. Pendiente `docker build` real (sin docker local).
    
- [ ] Configurar variables de entorno `KAIPETPOINT_*` en el ambiente remoto (BD, JWT, etc.).
    
- [ ] HTTPS + dominio (Caddy/Traefik con certificado automático, o el que entregue el PaaS).
    
- [ ] Ambiente separado de pruebas (staging) para que la clientela pruebe sin mezclar datos reales.
    
- [ ] Backups automáticos de PostgreSQL.
    
- [ ] Smoke post-deploy: login, venta descuenta stock, comprobante, reportes.

---

``` bash
git checkout main && git pull origin main && git checkout -b feat/deploy
```
