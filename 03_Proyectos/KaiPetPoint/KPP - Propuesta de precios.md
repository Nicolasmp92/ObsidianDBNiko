# KPP — Propuesta de precios (2026-10-29)

Estado: **PROPUESTA pendiente de decisión** — Nicolás define el número final.

## Contexto del producto

KPP hoy es un POS/gestión general (ventas, cierre de caja, catálogo, clientes
con estado de cuenta, inventario, ofertas, despachos, escáner, multi-sucursal,
multi-rol). Sin DTE (facturación electrónica en roadmap). Marca pet-friendly
pero el producto sirve a cualquier comercio chico.

## Anclas de mercado (investigado 2026-10-29)

| Competidor | Precio | Incluye |
|---|---|---|
| Bsale Básico | 1,5 UF ≈ $60.000 +IVA/mes | Facturación DTE, **sin POS ni inventario** |
| Bsale Estándar | 1,9 UF ≈ $93.201 +IVA/mes | POS + inventario + DTE (1.000 docs) |
| Bsale Full | 2,9 UF ≈ $110.000 +IVA/mes | + tienda online |
| VetLink (vet) | $29.990/mes | Un solo plan, todo incluido |
| PetCore (vet) | $19.990–29.990 +IVA/mes | Agenda/ficha clínica (no POS) |
| MiVetApp (vet) | $39.990/mes | Plan único veterinario |
| OpenFactura | ~$30.000/mes equiv. | Solo emisión DTE |

**Lectura**: todo lo que tiene POS + inventario en Chile parte arriba de $60k
cuando incluye DTE (Bsale). El segmento "comercio chico que no necesita DTE
integrado todavía" (boleta manual/SII gratis) está mal atendido: Bsale es caro
y genérico, los vet-software no tienen POS real.

## Recomendación

### Plan único — $19.990 + IVA / mes, todo incluido

- Una sola decisión, cero código de gating por planes (hoy no existe ninguna
  barrera por plan en KPP — cualquier tier exigiría desarrollo)
- Menos de la mitad del competidor más barato con POS comparable
- Todo: sucursales ilimitadas, usuarios, soporte directo con el desarrollador

### Estructura comercial lanzamiento

- **Precio fundador**: primeros 10 clientes congelan $19.990 de por vida
  (precio de lista objetivo después: $24.990 +IVA)
- **Setup remoto gratis** (~1h: configuración, usuarios, impresora) — liviano,
  no escala mal
- **Migración = importación self-service por plantilla Excel/CSV** — feature
  a construir (alta prioridad: habilita onboarding sin trabajo manual de
  NAMP). El cliente carga SU inventario; escala a infinitos clientes
- **Migración asistida opcional cobrada** (~$150.000 cotizado) — para quien
  quiera que se lo hagamos; trabajo manual real, se cobra como tal
- **Garantía 30 días**: si no le sirve, se devuelve el primer pago
- **Cobro**: transferencia mensual o link de pago Flow (sin integración)
- **DTE**: honesto en la página — "emites tu boleta en el portal gratuito del
  SII mientras; DTE integrado viene en el roadmap"

### Por qué no tiers ahora

- Dos tiers exigirían gating por plan en código (~trabajo real) y el límite
  natural (sucursales) cortaría una feature que hoy es ventaja competitiva
- Con 0 clientes, optimizar segmentación es prematuro — el cuello de botella
  es conseguir el primero
- Si la objeción #1 resulta ser "caro", bajar hay tiempo; subir nunca es
  agradable

### Economía (aprox.)

- Infra actual (VPS Hostinger KVM2 + dominio): ~$12.000/mes
- **1 cliente paga toda la infraestructura**. 10 clientes ≈ $200k/mes.

## Para implementar en namp.cl

- Sección/página `/precios` (o KPP landing): plan único, lista de features,
  badge "Precio fundador", CTAs → demo.namp.cl + WhatsApp/contacto
- Sin pasarela de pago por ahora (contratación por contacto = correcto a
  esta escala)

## Dependencia de producto identificada

- **Importador CSV/Excel de productos (y luego clientes)** — prerequisito
  real para vender sin regalar horas de carga manual. Va antes de la
  página de precios si queremos que la promesa "carga tu inventario en
  minutos" sea cierta el día que salga publicada

## Riesgos / honestidad

- Sin DTE, un cliente que necesite boleta electrónica integrada no cierra
  hoy — la página debe decirlo claro (filtra, no decepciona)
- Precio bajo puede leerse como "juguete" — se compensa con demo real +
  status page pública + garantía
