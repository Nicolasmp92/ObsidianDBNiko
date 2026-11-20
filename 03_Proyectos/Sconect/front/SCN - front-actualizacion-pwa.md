---
tipo: documentacion-tecnica
proyecto: sconect
actualizado: 2026-11-20
tags: [front, pwa, actualizacion, regla-docs-first]
---

# SCN — Spec: actualización de la PWA (prompt in-app)

**Estado: IMPLEMENTADO** (2026-11-20) — analyze 0 issues, test 11/11,
build web OK, `sconectActualizar()` sirviéndose en :4203. Regla madre:
[[Docs-first - estructura antes de construir]].

## Problema

La app se instala como PWA ("Agregar a pantalla de inicio" desde el demo
sslip.io). El service worker sirve la build cacheada: cuando sale versión
nueva, el usuario instalado **sigue viendo la vieja sin enterarse** — no hay
señal ni camino para actualizar.

## Decisión (acordada con el usuario 2026-11-20)

- **Prompt dentro de la app** (banner + botón "Actualizar"), NO push — no
  requiere servidor de push ni permisos extra.
- Solo web/PWA (`kIsWeb`); Android APK es caso futuro (otro mecanismo:
  endpoint de versión + descarga APK).

## Diseño

```
arranque app ──► fetch version.json?ts=... (sin caché)
                  │ firma = version + build_number
                  ▼
            guarda firma de ESTA sesión ──► [poll 30 min + al volver de
                  │                        segundo plano]
                  │ firma cambió? ──sí──► banner "Nueva versión" + Actualizar
                  ▼                                          │
            (nada, silencio)                          skipWaiting al SW
                                                      + reload → nueva build
```

### Componentes

| Pieza | Dónde | Qué hace |
|---|---|---|
| `ActualizacionService` | `core/pwa/` | `ChangeNotifier`: `iniciar()` lee `version.json`, guarda firma; re-verifica cada 30 min y al `resumed`; `hayActualizacion`, `aplicar()`, `despedir()` |
| `pwa_update*.dart` | `core/pwa/` | import condicional (mismo patrón que `pwa_install`): web → `window.sconectActualizar()` (JS en `index.html`); stub no-op |
| `sconectActualizar()` | `web/index.html` | `reg.update()` + `waiting.postMessage('SKIP_WAITING')` + `controllerchange`→`reload()`; fallbacks reload directo |
| `BannerActualizacion` | `core/widgets/` | `MaterialBanner` esmeralda no-modal: "Hay una nueva versión" + `Actualizar` + `Después` |
| Wiring | `main.dart` | servicio creado en `main()` tras `ensureInitialized`; `BannerActualizacion` envuelve `FondoApp(child)` |

**Desviación de la propuesta:** en vez de `package:web` + lógica SW en Dart,
el JS vive en `index.html` (`sconectActualizar`) y Dart lo invoca vía
`@JS` interop — mismo patrón ya establecido por `sconectInstalar`, sin
dependencias nuevas.

### Decisiones

- **Banner no-modal**: la actualización no bloquea atención clínica; el banner
  queda arriba hasta aplicar o cerrar (reaparece en próxima verificación si
  sigue pendiente).
- **Firma = `version`+`build_number`** de `version.json` (Flutter la genera;
  nginx ya la sirve `no-cache` desde el fix del 17-11). Fetch con `?ts=` por
  si otro proxy cachea.
- **Detección por polling+resume**, no por eventos SW: independiente del
  estado del SW (ausente, viejo, esperando).
- **Obligación operativa**: cada deploy debe bump `version: x.y.z+N` en
  `pubspec.yaml` o el prompt no se gatilla.

### Casos borde

- Offline / fetch falla → silencio (no mostrar nada, reintentar en próximo ciclo).
- Sin SW registrado → `aplicar()` hace `reload()` directo (el browser trae lo nuevo).
- Múltiples verificaciones sin aplicar → banner idempotente, sin spam.
- `dart:html`/`package:web` solo compila en web → **import condicional** con stub
  para que Android/iOS sigan compilando.

## Plan de prueba

1. `flutter build web` v1 → servir → abrir → sin banner.
2. Bump `version` en pubspec + rebuild → recargar pestaña → banner aparece en
   ≤30 min (verificación rápida: polling corto en debug).
3. Click "Actualizar" → reload → `version.json` nuevo activo, banner desaparece.
4. `flutter analyze` 0 + `flutter test` verde; build Android sin romper (stub).
