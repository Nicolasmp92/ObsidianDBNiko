---
tipo: nota-tecnica
proyecto: myk
actualizado: 2026-11-17
tags: [hardware, ia-local, gpu]
---

# MYK — Hardware del equipo (PC casa)

Ficha del hardware disponible para correr una IA local. Auditado 2026-11-17 (`lscpu`, `free -h`, `lspci`, `df -h`, `ubuntu-drivers devices`, `nvidia-smi`).

## Inventario

| Componente | Detalle |
|---|---|
| CPU | AMD Ryzen 7 3750H (Zen+, 4 núcleos / 8 hilos, base 2.3 GHz) |
| RAM | 15 GiB totales (≈4 GiB disponibles en el momento de la auditoría con el sistema en uso) |
| GPU dedicada | NVIDIA GeForce RTX 2060 Mobile (TU106M) — **6 GB GDDR6** |
| GPU integrada | AMD Radeon Vega Mobile (Picasso/Raven 2, en la APU) |
| Disco | 468 GB totales, **362 GB libres** |
| SO | Ubuntu 24.04.5 LTS |

## Estado del driver NVIDIA — ⚠️ punto bloqueante

- `nvidia-smi` **falla**: "couldn't communicate with the NVIDIA driver".
- Hay librerías instaladas de la versión **595.91.07** y `ubuntu-drivers` ofrece `nvidia-driver-580` / `580-open` / `470`.
- Hipótesis: módulo del kernel no cargado (kernel nuevo sin rebuild DKMS, o Secure Boot firmando mal el módulo). Verificar con `dkms status`, `mokutil --sb-state`, `lsmod | grep nvidia`.

## Qué implica para IA local

- **Con la RTX 2060 funcionando (6 GB VRAM):** modelos de ~7–8 mil millones de parámetros cuantizados a Q4/Q5 (GGUF) corren bien — es el rango "entrada estándar" de IA local.
- **Solo CPU (situación actual):** los mismos modelos funcionan pero lento (pocas palabras por segundo); los de ~3 B se vuelven la opción cómoda.
- **RAM 15 GiB:** suficiente para cargar el modelo en CPU si hiciera falta (un 7B Q4 ocupa ~4–5 GB).
- **Disco:** sobrado — un modelo GGUF pesa 2–8 GB.

## Referencias para la siguiente sesión

- Runtime candidato: Ollama (más simple) o llama.cpp (más control).
- Verificación mínima antes de instalar nada: que `nvidia-smi` responda.
