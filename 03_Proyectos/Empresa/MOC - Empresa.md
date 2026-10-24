---
tipo: empresa
estado: activo
actualizado: 2026-10-22
tags: [empresa, roadmap, saas, hosting, comercial]
---
# MOC — Empresa (plan de trabajo)

Visión: convertir el stack propio ([[MOC - StarterCustomeKit|StarterCustomeKit]]) en productos SaaS para pymes chilenas. Primer producto: [[MOC - KaiPetPoint|KaiPetPoint]]. Principio rector: **mientras menos gastemos, más ganamos** — infra mínima viable que cubra producción real.

## Navegación por necesidad

- **Quiero ver qué pasó** → `log.md` de esta carpeta
- **Quiero las tareas de un producto** → kanban maestro en [[Desarrollo]]
- **Quiero la evaluación de hosting completa** → [[KPP - Hosting y despliegue para pruebas]]
- **Quiero ideas de productos futuros** → [[Ideas]] (pipeline: ISO Manager, …)

## Mercado (verificado 2026-10-22)

- **Tamaño:** ~3.400–3.600 tiendas mascota/veterinaria en Chile (+35–43% en 4–5 años, Xbrein); gasto potencial ~$200 mil millones CLP/mes. Driver estructural: más mascotas que niños.
- **Competencia POS+gestión:** Bsale Estándar ~$89.000 c/IVA (Básico ~$70.000 sin POS ni inventario); Fudo $25.500–52.500. **KPP a $19.990–29.990 es 3–4× más barato** con POS+inventario+cierre incluidos → precio de entrada correcto.
- **Brecha crítica:** todos los incumbentes incluyen boleta electrónica SII; KPP la tiene diferida. En Chile la boleta es obligatoria → es el cuello de botella real para facturar. Mitigación piloto: boleta por portal gratuito del SII en paralelo; antes del 2º cliente conviene emisor DTE por API (LibreDTE/SimpleFactura/Haulmer).
- **Break-even:** la puesta en marcha de 1 cliente ($99.990) paga la mitad del VPS; ~5 meses de un plan Base cubren el resto. El VPS además sirve a todos los proyectos → no es apuesta única.

## Economía

- **Ingreso KPP SaaS:** $19.990–29.990 CLP/mes por tienda + $99.990 puesta en marcha única ([[KPP - Cotización SaaS (arriendo mensual)|cotización]]). Alternativa: licencia on-premise ([[KPP - Cotización licencia perpetua on-premise|cotización]]).
- **Costo fijo:** VPS ≈ $8.54 USD/mes ≈ **$8.100 CLP/mes** (KVM 2, prepago 24m ≈ $195.000 CLP; renueva $17.19 USD ≈ $16.300 CLP) + dominio (gratis 1er año con el VPS). Escalar a KVM 4 (16 GB) cuesta +$3.500 CLP/mes — se paga solo con ~1/6 de un cliente SaaS.
- **Break-even:** 1 cliente cubre el hosting ~11 meses con solo la puesta en marcha; con 3 clientes el hosting es <10% del MRR.

## Infraestructura (un solo host)

- **Hostinger KVM 2 — DC São Paulo, plan 24 meses** (~$8.79/mes): 2 vCPU / 8 GB / 100 GB NVMe. Backups semanales incluidos + dominio gratis año 1.
- Docker + Dokploy (o compose + Caddy): HTTPS automático — requerido por el escáner de cámara de KPP.
- Una instancia PostgreSQL compartida, una BD por app; `pg_dump` diario por cron.
- Subdominios de un dominio: `app.` → KPP prod, `staging.` → pruebas clientela, raíz → web empresa, `demo.` → demos.
- Sitios estáticos (portafolio, MP, RECOS, colegio) quedan en GitHub Pages: $0. La web empresa puede ir en el VPS (dominio raíz) o GH Pages si es estática — decidir al construirla.
- Server UOH (CABID, 172.16.0.190) **no se migra**: es infra institucional.
- Capacidad: cada instancia SaaS ≈ 1 GB → ~5 stacks cómodos antes de escalar a KVM 4 (16 GB, $12.99 promo).

## Roadmap por fases

### F0 — Infraestructura (esta semana)

- [x] Contratar KVM 2 Brasil (24m) ✅ 2026-10-22 — IP `200.141.25.56`, `ssh vps`.
- [ ] Registrar/apuntar dominio + DNS subdominios en Traefik.
- [x] Docker + Dokploy ✅ 2026-10-23 — panel http://200.141.25.56:3000.
- [ ] Deploy KPP producción desde rama `feat/deploy` (compose ya listo) + env `KAIPETPOINT_*`.
- [ ] Staging separado para pruebas de clientela (BD limpia con seed).
- [ ] `pg_dump` diario + Uptime Kuma en el mismo VPS.
- [ ] Smoke post-deploy: login, venta descuenta stock, comprobante, cámara bajo HTTPS.
- [x] Verificar latencia real SP→Chile ✅ ~95-100 ms desde casa (más que los ~50 ms de backbone; validar con app real).

### F1 — Presencia comercial

- [ ] Web de la empresa: servicios, casos, contacto WhatsApp. **Decidir:** reusar repo `Nicolasmp92` (Angular existente) o crear nueva.
- [ ] Landing de KPP con demo pública apuntando a staging.
- [ ] Portafolio público ✓ (ya en https://nicolasmp92.github.io/).

### F2 — Primer cliente (Patitas / clientela esperando)

- [ ] **Iniciación de actividades en SII** — prerequisito para emitir boleta/factura. **Parcial:** ya tiene iniciación de honorarios (2ª categoría, por su trabajo UOH). Pendiente: revisar con contador si el giro cubre venta de suscripciones SaaS (normalmente 1ª categoría — factura/boleta de venta) o si hay que ampliar giro / crear SpA vía "Tu Empresa en un Día". Con giro informático, la compra del VPS pasa a ser gasto deducible (responder IVA de servicios del exterior con contador).
- [ ] Piloto KPP en producción con datos reales.
- [ ] Cobrar puesta en marcha ($99.990) + primer mes.
- [ ] Feedback semanal → realimentar backlog PMV ([[KPP - Roadmap y priorización (PMV)|roadmap KPP]]).

### F3 — Crecimiento

- [ ] Segunda tienda = instancia extra (~1 GB) — sin costo de hosting adicional.
- [ ] Boleta SII como módulo cotizable ([[KPP - Boleta electrónica SII]]).
- [ ] Referidos y marketing local (Rancagua / O'Higgins).
- [ ] Evaluar [[MOC - Sconect|Sconect]] como segundo producto (nicho salud, backend listo).

## Qué NO se adopta (y por qué)

- **PaaS por servicio (Railway/Render/Fly):** $15–60 **por stack** → $75–300/mes para los proyectos; mata el margen SaaS.
- **Oracle Cloud Free en producción:** $0 pero riesgo de reclamación de VM con clientes pagando. Vale solo para staging/desechable.
- **Hetzner CX33 (~$10.6):** runner-up válido si se prefiere facturación por hora sin prepago; pierde por latencia (US East ≈ 130 ms vs SP ≈ 60–80 ms) y por no incluir dominio.
- **KVM 1 (4 GB, $6.49):** ahorra $2.30/mes pero deja sin staging ni instancias cliente — ahorro falso.
- **VPS con DC en Chile (inan.cl, hostnet.cl, GCP southamerica-west1):** ~10 ms vs ~50 ms SP→Stgo, pero la mitad de RAM por 2.5–4× el precio (~$16–40 USD por 4 GB vs $8.79 por 8 GB). ~40 ms no justifican 3× el costo; contingencia si el peering Chile→Brasil sale malo o surge exigencia de residencia de datos.
- **Migrar CABID al VPS:** infra institucional UOH, fuera de alcance.

## Condición de falsación de la decisión de hosting

Si uptime < 99.5% en 60 días con cliente real, o CPU steal recurrente, o soporte deficiente → migrar a Hetzner (el compose es portable; costo ≈ una tarde).
