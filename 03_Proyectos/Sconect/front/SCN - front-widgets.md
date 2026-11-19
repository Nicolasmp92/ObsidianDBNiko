---
tipo: documentacion-tecnica
proyecto: sconect
actualizado: 2026-11-19
tags: [front, widgets, flutter, regla-docs-first]
---

# SCN — Widgets compartidos (`app/lib/core/widgets/`)

Inventario de componentes de UI compartidos. **Antes de crear un widget nuevo:
mirar aquí si ya existe.** Regla madre: [[Docs-first - estructura antes de construir]].

## AppButton — botón estándar (2026-11-19)

`lib/core/widgets/app_button.dart` — el botón de la app. Centraliza lo que
antes se copiaba en 7 pantallas.

```dart
enum AppButtonVariant { primary, danger, text }

AppButton(
  label: 'Agendar cita',          // texto del botón
  onPressed: _guardar,            // acción
  loading: _guardando,            // spinner 22px + deshabilita solo
  icon: Icons.calendar_month,     // opcional
  variant: AppButtonVariant.danger, // primary (default) | danger | text
  expand: true,                   // ancho completo (default) | compacto
  height: 52,                     // 52 formularios | 40 acciones de diálogo
)
```

| Uso | Config |
|---|---|
| CTA de formulario | `expand: true, height: 52` (default) |
| Acción destructiva en diálogo | `variant: danger, expand: false, height: 40` |
| Confirmación en diálogo | `variant: primary, expand: false, height: 40` |
| Acción textual | `variant: text` |

Adoptado en 16 call sites (cita, evolución, paciente, perfil, preferencias,
login, portal entrada/home, cámara, directorio, solicitudes, pacientes list).
Bonus al migrar: deshabilitar durante `loading` (el portal permitía
doble-submit) y color esmeralda consistente (los `FilledButton` por defecto
salían morado M3 — `MaterialApp` no define `theme:`).

## Otros compartidos

| Widget | Archivo | Qué hace |
|---|---|---|
| `OpcionCuenta` / `PieCerrarSesion` | `opcion_cuenta.dart` | Tarjeta de la pestaña Cuenta (ícono+título+detalle+chevron) y pie con "Cerrar sesión" destructivo |
| `FondoApp` | `fondo_app.dart` | Degradado menta + manchas esmeralda detrás de todo (los Scaffold van transparentes) |
| `AppToast` | `app_toast.dart` | Notificación estándar |
| `ElegirFoto` | `elegir_foto.dart` | Selector/recorte de foto de perfil |
| `CamaraPerfil` | `camara_perfil.dart` | Cámara en vivo: vista previa espejo, guía circular, Usar/Repetir |
| `ElegirHora` | `elegir_hora.dart` | Picker de hora compartido (agenda + portal) |

## Tokens (de `core/theme/app_colors.dart`)

`primary` `#004D40` (esmeralda) · `secondaryText` `#546E7A` ·
`surface` `#E0FFFFFF` (vidrio ~88% sobre FondoApp) · `background` transparent.
Radios: 14 botones, 16 tarjetas. Alturas: 52 CTA, 40 acciones de diálogo.
