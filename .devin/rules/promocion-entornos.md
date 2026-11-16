---
tipo: regla
estado: vigente
creado: 2026-10-01
tags: [promocion, entornos, produccion, seguridad-operacional]
---

# Reglas · cadena de promoción lab → dev → producción

> Regla genérica del paquete (origen: auditoría de la cadena de
> despliegue): ninguna operación escribe directo en producción. Toda
> carga/cambio sube por la cadena con verificación en cada escalón. Los
> nombres de los entornos se concretan por proyecto.

## 1 · La cadena es obligatoria y unidireccional

```
lab (local, Docker/dev)     →   dev (servidor, stack real)   →   producción
        │                              │                            │
   ensayo + carga inicial        verificación recreando         solo cuando dev
   de datos/diseño               el ambiente servidor           demostró funcionar
```

- **Nada se escribe en el host de producción** desde un script, import o
  comando que no haya corrido antes completo en lab y verificado en dev.
- Producción es **destino final**, nunca ambiente de prueba ni de iteración.

## 2 · Escrituras seguras por defecto (cierra EV-06)

Todo script que muta un servicio remoto (fotos, relaciones, estructuras,
imports REST) debe cumplir:

- `--dry-run` (solo simulación) como comportamiento **por defecto**;
  escribir exige `--apply` explícito.
- La URL destino se exige explícita o por ambiente (`--env lab|dev|prod`);
  ningún script lleva una URL de producción como default.
- Un allowlist por ambiente rechaza el host de producción salvo flag
  `--prod` adicional.
- Antes de escribir: manifiesto de lo que se va a tocar (IDs, conteos,
  destino) y respaldo/rollback declarado.

## 3 · Verificación en dev antes de subir

Un cambio "pasa a dev" = está desplegado en el servidor dev y verificado
**a nivel ambiente recreado**, no solo "carga en mi máquina":

- servicios/contenedores `active` (y auto-restart) tras reboot;
- endpoints respondiendo (API, UI, proxy frontal);
- datos/relaciones visibles en la UI;
- rollback ensayado al menos una vez.

## 4 · Qué viaja y cómo

- **Código**: por git — cada proyecto define su canal (remoto nube o bare
  en dev).
- **Datos**: `scp`/`rsync` controlado + import por los procedimientos del
  sistema — nunca reemplazo directo de BD entre ambientes.
- **Datos sensibles** (ej. datos de personas reales): solo con
  autorización explícita; dev trabaja con sintéticos por defecto.

## 5 · Excepción

La única escritura a producción permitida sin haber pasado por la cadena es
una **corrección de incidente urgente**, documentada en bitácora el mismo
día con causa y rollback.
