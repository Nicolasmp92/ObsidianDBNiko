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

## Incidente 2026-11-19 — muerte del SSD secundario (D:)

- **Qué pasó:** con `llama3.2:3b` corriendo en GPU (84,8 tok/s) + **otros proyectos abiertos** (sistema ya cargado), el usuario envió un "hola" en la UI web de Chari → el equipo completo se congeló → apagado forzado con el botón → el SSD `HS-SSD-E100 512G` (disco 0, D:, donde vivía Ubuntu 24.04 + Juegos) **no volvió a enumerar**: ni BIOS, ni Windows, ni el initramfs de Ubuntu lo detectan. Disco muerto a nivel de hardware.
- **Hipótesis causal:** SSD white-label frágil + apagado en mitad de escritura. Alternativa complementaria: el propio fallo del disco pudo causar el cuelgue (I/O timeouts congelan Linux). Antecedente: el enclosure USB Realtek ya se había "colgado en escritura sostenida" (13-nov) — el ecosistema de storage económico mostraba fragilidad.
- **Daño colateral:** NTFS de C: dañado en `SoftwareDistribution\Download` (Windows Update) → autoreparado en el arranque siguiente (hoy sano). Entrada EFI `ubuntu` zombie en NVRAM.
- **Lo salvado:** repo `Nicolasmp92/myk` ya en GitHub (UI + Chari); notas de reconstrucción en esta ficha + [[3. Ollama - el runtime que ejecuta modelos locales]] + [[4. Modelos de IA - familias open-weight y como elegir para tu hardware]].

## REGLA — Preflight antes de carga pesada (vigente desde 2026-11-19)

Antes de ejecutar inferencia IA o cualquier carga sostenida (build grande, entrenamiento, batch) en este equipo:

1. **Listar qué ya corre** — cerrar proyectos/pestañas no esenciales (RAM 15 GiB se agota rápido; el cuelgue fue con varios proyectos abiertos).
2. **Chequeo mínimo:** RAM libre (`free -h` / Administrador de tareas), temperatura (`sensors`), espacio en disco.
3. **Modelo vs hardware:** verificar que el modelo cuadre en VRAM sin swap (regla de la entrada 4 de wiki: params×bytes + KV cache). `llama3.2:3b` = ~2,6 GB VRAM — OK; un 8B quedaría al límite.
4. **Storage:** preferir disco de marca para cargas de I/O; los SSD genéricos murieron ya dos veces bajo estrés.
5. **Si el equipo se congela:** esperar ~2 min antes del apagado forzado — los timeouts de I/O a veces se resuelven y el corte a mitad de escritura es lo que mata SSDs.

## Referencias para la siguiente sesión

- Runtime candidato: Ollama (más simple) o llama.cpp (más control).
- Verificación mínima antes de instalar nada: que `nvidia-smi` responda.
