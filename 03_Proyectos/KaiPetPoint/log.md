---
tipo: log
proyecto: kaipetpoint
---
# 📓 Log — KaiPetPoint

Bitácora narrativa **append-only**: entradas nuevas al final. Tipos: **HECHO** / **DECISIÓN** / **HIPÓTESIS** / **RIESGO**. La bitácora técnica autoritativa vive en el repo.

---

## 2026-10-03 — Génesis desde SCK

- **DECISIÓN** — POS de tienda genérico generado desde StarterCustomeKit (patrón Frunexis: `git archive` + renombrado). Nombre inicial: Mostrador.
- **HECHO** — Dominio `items` reemplazado por tienda: catálogo (marcas/categorías/productos), `movimientos_stock`, `ventas`+`venta_items` transaccional. Seed Patitas (6 marcas, 4 categorías, 10 productos).
- **HECHO** — Smoke end-to-end: venta descuenta stock, movimientos con `venta_id`, anulación repone, 409 sin stock, 401 sin sesión. `mvn test` · lint · 22/22 · build verdes.
- **HECHO** — Repo publicado `Nicolasmp92/Mostrador` (privado) vía API GitHub.

## 2026-10-04 — Login estándar + comprobante + fix SSR + rename

- **HECHO** — Login estándar portado de SCK (`4353251`): recordar correo `kaipetpoint.recordar-correo`, toggle clave, mailto soporte, marca.
- **HECHO** — Comprobante post-cobro (`2d3c5d9`): al cobrar, boleta con #/fecha/vendedor/items/total del servidor + "Nueva venta" / "Ver ventas". Toast de éxito eliminado (redundante).
- **HECHO** — **Fix crítico SSR** (`b5cdfbe`): F5 cerraba sesión porque el guard corría en Node sin cookie. `ssrCookieInterceptor` reenvía la cookie a `/api/*` en SSR; `httpErrorInterceptor` solo actúa en navegador. Verificado: con cookie → 200, sin cookie → 302 /login.
- **DECISIÓN** — Rename **Mostrador → KaiPetPoint** (`d81f353`): marca del nicho mascotas. Renombrado integral: paquete Java, BD, cookie, claves `kaipetpoint.*`, env vars, repo GitHub. **RIESGO** — el nombre amarra al nicho; para reusar el POS en otra tienda habría que rebrandear (solo superficial).
- **RIESGO** — SCK y Frunexis comparten el bug de sesión en SSR (heredado del kit); pendiente portar el fix.
