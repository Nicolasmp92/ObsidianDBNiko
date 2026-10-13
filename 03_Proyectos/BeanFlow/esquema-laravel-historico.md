# BeanFlow — Esquema Laravel histórico (registro de migración)

> Foto del esquema **previo** a la migración al stack Angular + Spring
> Boot (merge `ea07d99`, 2026-10-13). Se conserva **solo como registro**:
> el proyecto ya no se alimenta de Laravel. Fuente: migraciones PHP de
> `main` previo al merge (commit `d2be7a5`, 2025-10-24).

## Contexto

La v1 Laravel era un **starter kit de autenticación** (Laravel 12 +
Livewire + Volt), no un POS — no aportaba dominio de negocio al rewrite.
El POS de restaurante se diseñó desde cero en el stack nuevo.

## Tablas del esquema Laravel

| Migración | Tabla(s) | Contenido |
|---|---|---|
| `0001_01_01_000000_create_users_table` | `users`, `password_reset_tokens`, `sessions` | auth estándar Laravel |
| `0001_01_01_000001_create_cache_table` | `cache`, `cache_locks` | infraestructura |
| `0001_01_01_000002_create_jobs_table` | `jobs`, `job_batches`, `failed_jobs` | colas |
| `2025_08_08_195202_update_users_table_add_missing_columns` | `users` (+columnas) | perfil extendido |
| `2025_08_14_170511_create_permission_tables` | `permissions`, `roles`, `model_has_permissions`, `model_has_roles`, `role_has_permissions` | spatie/laravel-permission |
| `2025_09_28_152837_add_theme_to_users_table` | `users` (+`theme`) | preferencia visual |

## Equivalencias en el stack nuevo

| Concepto Laravel | Destino en Angular + Spring |
|---|---|
| `users` + roles spatie | `usuarios` con `rol` simple (garzon/cocina/caja/admin) — V1 Flyway |
| `sessions`/`cache`/`jobs` | sin equivalente — JWT en cookie, sin colas ni caché de servidor |
| `theme` | preferencia de tema en el front |

Esquema vigente: `.devin/rules/backend-bd-esquema.md` en el repo.
