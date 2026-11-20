---
tipo: nota-tecnica
actualizado: 2026-11-20
tags: [herramientas, windows, instalador, venta, distribucion, flutter]
---

# Empaquetado Windows para vender — opciones

> **Pregunta:** ¿cómo convertir una app Flutter Windows en un producto
> instalable vendible? Análisis barajado el 2026-11-20.

## La pieza base

`flutter build windows` produce `.exe` + DLLs nativas (skia/impeller incluido,
sin runtime externo). Esa carpeta hay que empaquetarla en instalador:

| Opción | Costo | Auto-update | Store | Nota |
|---|---|---|---|---|
| **Inno Setup** | Gratis | No (manual o script) | No | El clásico indie: instalador .exe propio, licencia, desinstalador |
| **MSIX** | Gratis | **Sí** (AppInstaller feed — un XML en el VPS apunta al .msix nuevo, Windows actualiza solo) | Requerido p/ Store | El estándar moderno; sin firma confiable Windows lo bloquea |
| **NSIS** | Gratis | No | No | Alternativa a Inno, más low-level |
| **WiX/MSI** | Gratis | Vía deployment corporativo | No | Orientado enterprise (GPO/SCCM), overkill |

## El problema real: firma de código

Un `.exe`/`msix` **sin firma** dispara SmartScreen: "Windows protegió su PC —
editor desconocido". Para vender, eso mata la confianza:

| Opción | Costo aprox | Efecto |
|---|---|---|
| Sin firma | $0 | Warning rojo en cada instalación — solo vale para beta/círculo propio |
| **Azure Trusted Signing** | ~$9-10/mes | Nueva vía Microsoft, firma válida + reputación se acumula |
| Cert OV (Sectigo/DigiCert) | $80-250/año | Reputación SmartScreen **se construye** con installs (primeras semanas igual sale warning) |
| Cert EV | $300-400/año | Reputación SmartScreen **instantánea** — caro pero limpio desde el día 1 |

## Actualización post-venta

- **MSIX + AppInstaller**: publicas `app.appinstaller` (XML con URL del paquete)
  en el VPS; Windows chequea solo → el patrón "version endpoint" que ya
  diseñamos para la PWA resuelto por el SO. La vía más elegante con nuestra
  infra.
- **Inno + endpoint propio**: la app consulta `/api/app/version` (mismo
  endpoint planeado para Android), baja el instalador nuevo y lo lanza.
  Más trabajo pero sin MSIX.

## Venta: cobro y licencia

- **Pasarela que entrega licencia**: Gumroad / Lemon Squeezy / Paddle —
  ellos cobran, entregan el instalador y opcionalmente generan license keys.
  Comisión ~5-10% + fees; cero backend propio.
- **Licencia propia**: endpoint `POST /api/license/validar` en el backend;
  la app pide clave al primer uso. Necesario solo si se vende por fuera de
  las pasarelas.
- **Microsoft Store**: $19 cuenta individual, ellos cobran/instalan/actualizan —
  pero revisión + MSIX firmado obligatorios.

## Recomendación barajada (Sconect/KPP)

1. **Corto plazo (beta vendible)**: Inno Setup + Azure Trusted Signing
   (~$10/mes) — instalador propio, warning limpio, distribución por VPS o
   pasarela.
2. **Si escala**: MSIX + AppInstaller en el VPS (auto-update gratis por el SO)
   y eventualmente Microsoft Store ($19) para visibilidad.
3. **Cobro**: empezar con pasarela (Lemon Squeezy/Paddle) — no construir
   e-commerce propio hasta que haya señal de ventas.

## Fuentes

- Flutter: `flutter build windows` — https://docs.flutter.dev/platform-integration/windows/building
- Inno Setup — https://jrsoftware.org/isinfo.php
- MSIX + AppInstaller — https://learn.microsoft.com/windows/msix/app-installer/app-installer-file-overview
- Azure Trusted Signing — https://learn.microsoft.com/azure/trusted-signing/
