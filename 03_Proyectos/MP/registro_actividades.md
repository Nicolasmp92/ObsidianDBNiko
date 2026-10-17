---
tipo: registro
proyecto: mp
---
# Registro de actividades — MP

Tabla estructurada **append-only**. Una fila por actividad verificable; las filas nuevas van al final.

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-05-22 | Levantamiento de requerimientos por sección (logo, hero, bento, 4 servicios, quiénes somos, correos) | nota `MP - Requerimientos` (status: En proceso) |
| 2026-05-22 | Propuesta tipo catálogo para Arriendo de Equipos | checkbox ✅ en `MP - Requerimientos` |
| 2026-10-16 | Auditoría de seguridad/performance/SEO del repo MP | entrada `## 2026-10-16` en `log.md` |
| 2026-10-16 | Credenciales SMTP/reCAPTCHA extraídas de `mailer.php` a `mailer.config.php` local (gitignored); deploy las inyecta desde GitHub secrets; `.htaccess` protege el config | commit en `MP` rama `main` (`.gitignore`, `angular.json`, `src/mailer.php`, `src/mailer.config.example.php`, `public/.htaccess`, `.github/workflows/deploy.yml`) |
