# Guía — Boleta electrónica SII para KaiPetPoint

Pasos para que KaiPetPoint pueda emitir boletas electrónicas legalmente en Chile.
Estado: **diferido — no implementado**. Esta guía cubre los trámites; la integración
técnica recomendada es vía API de terceros (ver sección final).

---

## Parte 1 — Trámites (persona/empresa, en sii.cl)

### 1. Tener emisor tributario
- Necesitas un RUT con **iniciación de actividades** vigente (primera o segunda
  categoría). Si vendes como persona, inicia actividades en sii.cl →
  "Iniciación de actividades".
- Inscríbete en el régimen que corresponda (el contador ayuda aquí).

### 2. Certificado digital
- En sii.cl → "Certificado Digital" → **generar certificado propio** (gratis)
  o comprar uno a un proveedor certificado (E-Sign, Acepta, etc.).
- El certificado es un archivo `.pfx/.p12` con clave — es la identidad digital
  de la empresa ante el SII. **Guárdalo como un secreto.**

### 3. Obtener folios (CAF)
- En SII → "Folios / CAF" pides rangos de folios por tipo de documento.
  Para boleta: **DTE tipo 39** (boleta electrónica) o 41 (exenta).
- El CAF es un XML con claves privadas de folio — el software lo usa para
  timbrar cada boleta. Se descargan por tramos; hay que re-pedir al agotarse.

### 4. Certificación (obligatoria antes de producción)
- SII tiene un **ambiente de certificación/maullido**: se emiten documentos de
  prueba contra un "set de muestras" que SII revisa.
- Si usas **software de terceros ya certificado** (recomendado), este paso lo
  reduce bastante el proveedor — ellos ya están certificados y tu empresa solo
  hace la "autorización del software" en el portal.
- SII también ofrece su propio emisor gratuito ("SII Facturación") — sirve
  como respaldo o coexistencia, pero no se integra a un POS.

### 5. Producción
- Emitir boletas tipo 39, timbre electrónico (PDF417) impreso en el ticket.
- **Libro de boletas electrónicas / RCOF**: envío diario del resumen de
  folios consumidos — el proveedor/sotfware lo hace automático.
- **Contingencia**: si SII o internet cae, se emiten boletas de contingencia
  con folios reservados y se informan después.

---

## Parte 2 — Opciones de software (qué integra KaiPetPoint)

| Opción | Esfuerzo | Costo aprox. | Nota |
|---|---|---|---|
| **API de terceros** (LibreDTE, SimpleAPI, Openfactura) | ~1 semana de código | $15.000-30.000/mes por emisor | Recomendada: certificación y timbre los resuelve el proveedor |
| LibreDTE self-hosted | Integración + operar su stack PHP | Gratis (open source) | Gratis pero sumas otra app que mantener |
| Emisión propia (DIY) | Meses | $0 + certificación propia | XML DTE firmado, TED PDF417, CAF, SOAP, libro de boletas — NO recomendado |
| Portal SII gratuito | 0 | $0 | Sin integración; el cajero digita dos veces |

**Diseño recomendado para KaiPetPoint** (cuando se retome):
1. `POST /api/ventas` ya calcula neto/IVA — al confirmar, llamar la API del
   proveedor con los ítems.
2. Guardar en `venta`: `folio`, `tipo_dte`, `pdf_url`/`xml_url` del proveedor.
3. El ticket impreso pasa a ser la boleta real (con timbre PDF417 del proveedor).
4. Anulación → "nota de crédito electrónica" o invalidación según proveedor.

---

## Checklist resumen

- [ ] RUT + iniciación de actividades
- [ ] Certificado digital registrado en SII
- [ ] Elegir proveedor de emisión (o portal SII como coexistencia)
- [ ] CAF de folios tipo 39
- [ ] Certificación en ambiente de prueba SII
- [ ] Integración API en `ventas` (folio + PDF + timbre)
- [ ] Plan de contingencia (folios reservados)

*Redactado 2026-10-04 — verificar vigencia en sii.cl antes de ejecutar.*
