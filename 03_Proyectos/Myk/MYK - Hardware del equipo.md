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

## Estado del driver NVIDIA — ✅ RESUELTO (2026-11-18)

`nvidia-smi` responde: RTX 2060, **6.144 MiB VRAM**, driver **595.99.02**, **CUDA 13.2**, ~1W en idle.

**Causa raíz (dos capas):**
1. `prime-select` estaba en modo `intel` → generaba `/usr/lib/modprobe.d/blacklist-nvidia.conf` con `alias nvidia off`, que bloqueaba la carga del módulo (el error críptico `could not insert 'off'` venía de ahí).
2. Faltaba `linux-modules-nvidia-595-open-<kernel>` para los kernels nuevos (Ubuntu usa módulos precompilados por kernel, no DKMS — `dkms status` vacío es normal aquí).

**Fix aplicado:**
```bash
sudo apt install linux-modules-nvidia-595-open-<kernel>  # módulo del kernel vigente
sudo prime-select on-demand                            # borra el blacklist
sudo modprobe nvidia nvidia_uvm                        # carga sin reiniciar
```

- Modo `on-demand`: pantalla en la iGPU Vega, RTX libre para cómputo CUDA — ideal para inferencia local sin quemar batería.
- Kernels cubiertos: módulos nvidia instalados para -42 y -43; `full-upgrade` mantiene el metapaquete `linux-modules-nvidia-595-open-generic-hwe-24.04` al día.
- Lección: si `nvidia-smi` vuelve a fallar tras update de kernel → revisar `prime-select query`, `lsmod | grep nvidia` y que exista `linux-modules-nvidia-595-open-$(uname -r)`.

## Qué implica para IA local

- **Con la RTX 2060 funcionando (6 GB VRAM):** modelos de ~7–8 mil millones de parámetros cuantizados a Q4/Q5 (GGUF) corren bien — es el rango "entrada estándar" de IA local.
- **Solo CPU (situación actual):** los mismos modelos funcionan pero lento (pocas palabras por segundo); los de ~3 B se vuelven la opción cómoda.
- **RAM 15 GiB:** suficiente para cargar el modelo en CPU si hiciera falta (un 7B Q4 ocupa ~4–5 GB).
- **Disco:** sobrado — un modelo GGUF pesa 2–8 GB.

## Referencias para la siguiente sesión

- Runtime candidato: Ollama (más simple) o llama.cpp (más control).
- Verificación mínima antes de instalar nada: que `nvidia-smi` responda.
