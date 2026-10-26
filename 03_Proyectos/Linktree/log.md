# Log — Linktree (página de enlaces Bibliotecas UOH)

Bitácora append-only. Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO.

Repo: `~/Escritorio/Desarrollo/linktree` (github.com/Nicolasmp92/linktree).
Origen: copia desde `repositorios-digitales-uoh/LINKTREE/` (repo privado institucional) — allí vive el historial completo de diseño.
Stack: Angular 22 standalone, CSS plano, página única. `npm start` → :4300.
Deploy producción: `npm run deploy-sexto` → `ssh sexto` → `E:\FTP\enlaces\` → `https://publicaciones.uoh.cl/enlaces/` (server SEXTOPLANO, Windows IIS+FTP, VM del Proxmox UOH — cuenta prestada `cristobal.merchan@uoh.cl`, llave `id_ed25519` en administrators_authorized_keys).
Contexto: desarrollo para la UOH (bio de @bibliotecasuoh) — también portfolio personal, como CABID.

## 2026-10-26

- **HECHO** — App construida y en producción: tema menta→celeste UOH con focos superiores, logo oficial Unidad de Bibliotecas, entrada escalonada + sheen hover + tap táctil, 11 enlaces oficiales (de Paulina) con iconos SVG, chips LinkedIn/correo, sección "Actividades" rotativa (Torneo Juegos de Mesa), footer con campus + Google Maps.
- **DECISIÓN** — Sección `actividades` separada de `enlaces`: las campañas rotan (cuando el array queda vacío la etiqueta desaparece sola).
- **HECHO** — TLS institucional: el wildcard `*.uoh.cl` del server estaba vencido desde el 29-sep; PEMs que mandó Cristóbal eran la renovación → PFX generado, importado y binding 443 rebajado. Vence **27-dic-2026**.
- **PENDIENTE** — Usuario propio en sexto-130 (hoy cuenta prestada de Cristóbal); decidir qué sirve la raíz `publicaciones.uoh.cl/` (403); dueño de la renovación dic-27; limpiar copias locales de la llave privada del wildcard (hoy en ~/Descargas/certs + /tmp + E:\FTP\temp).
- **RIESGO** — La llave privada del wildcard `*.uoh.cl` viajó por WhatsApp y hay copias en varios sitios — mitigar con almacenamiento en Bitwarden + shred, idealmente rotación.
