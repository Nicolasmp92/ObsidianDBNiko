---
tipo: documentacion-tecnica
proyecto: kaipetpoint
actualizado: 2026-11-24
tags: [front, inputs, clp, miles, granel, convenciones]
---

# KPP — Inputs de montos CLP (`appMiles`) y convenciones visuales

Spec viva. Regla madre: [[Docs-first - estructura antes de construir]].

## `appMiles` — separador de miles al tipear

`<input appMiles>` en `shared/miles.directive.ts` (espejo de `appRut`):
filtra a dígitos y reformatea en vivo con `.` como separador de miles
(`5000` → `5.000`). El modelo conserva el texto formateado; `NgControl.setValue`
lo propaga igual en `ngModel` y `formControlName`.

- `shared/utils/miles.ts`
  - `formatearMiles(texto): string` — dígitos agrupados de a 3 desde la derecha.
  - `montoDe(texto): number` — parsea el formato: quita `.` (miles), coma→punto
    (decimal CLP legacy), NaN→0. **Parser único de montos tipeados.**
- Suscripción a `valueChanges`: cuando el modelo se setea programático
  (ej. "recibido exacto" en POS), el input se reformatea sin emitir — la
  directiva solo escribe `el.value`, no vuelve a `setValue`.

### Campos con `appMiles` (montos CLP)

| Vista | Campo |
|---|---|
| Nueva venta | `recibidoTexto`, `abonoTexto`, `mixtoEfectivo`, `mixtoTarjeta`, `mixtoTransferencia`, `mixtoFiado` |
| Caja | `fondoTexto`, `montoMovimiento`, `declaradoTexto` |
| Cliente detalle | `monto` (abono, reactive form) |

**Fuera de alcance (decisión):** `descuentoTexto` (comparte %/CLP y admite
decimales), cantidades/kg/stock (no son dinero), folio, barcode.
`type="number"` (precio producto, tarifa zona, ofertas) no puede mostrar `.`
— convertirlos a texto cambia el tipo del modelo; se evalúa si el usuario lo pide.

### Parseo

Los sitios que consumen montos tipeados usan `montoDe` — nunca `numeroDe`
(ese sigue para descuentos/kg donde `.` no es separador de miles):
- `caja.numero()` → delega a `montoDe`.
- `nueva-venta` → `montoDe` en recibido/abono/mixto; `numeroDe` en descuento.
- `cliente-detalle` → `montoDe(monto)` al enviar.

## Tag granel ≠ estado

El chip `app-granel-chip` era ámbar (`warning`) — mismo token que "stock bajo",
"oferta" y el borde de alerta: se leía como advertencia. **Granel es un tipo
de producto, no un estado** → identidad neutra: chip sólido `bg-text text-surface`,
borde de tarjeta `border-text/40`. No depende de la paleta de acento (la paleta
Ámbar haría colisionar `primary` con `warning` otra vez).

## Pieles reutilizables (`styles.css`)

La regla `h-11` (44px táctil) ahora vive en clases semánticas, no repetida
en cada página — misma filosofía que `.dialogo`:

- `.btn` — `inline-flex h-11 items-center justify-center gap-2 rounded-lg
  px-4 text-sm font-medium disabled:opacity-50`. Variantes:
  `.btn-primario`, `.btn-secundario` (borde + hover muted), `.btn-peligro`.
  El sitio aporta solo layout: `w-full`, `flex-1`, `mt-3`, `sm:px-5`…
- `.input` — `h-11 rounded-lg border border-border bg-surface px-3 text-sm
  outline-none focus:border-primary`. Sirve para input, select y textarea;
  el ancho lo da el sitio.
- `.acciones-form` — fila de acciones al pie (diálogo o form inline):
  `mt-4 flex gap-2 sm:justify-end` + hijos `flex-1 sm:flex-none`
  (mitades en móvil, natural a la derecha en escritorio).

**`sm:h-9` eliminado del codebase** (14 ocurrencias): la regla ≥44px no
tiene excepción de densidad desktop. En la práctica la diferencia es
36→44px — se verifica visualmente que nada se desarme.
Migración: ~174 strings de clase reemplazados en 28 archivos, 15 footers
de formulario unificados a `.acciones-form`.
