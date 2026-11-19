# Registro de actividades — Myk

Tabla append-only. Detalle narrativo en `log.md`.

| Fecha | Actividad | Evidencia |
|---|---|---|
| 2026-11-17 | Proyecto creado (MOC + log + registro + ficha hardware + roadmap) | archivos de esta carpeta |
| 2026-11-17 | Auditoría de hardware del equipo | [[MYK - Hardware del equipo]] (lscpu, free, lspci, df, ubuntu-drivers) |
| 2026-11-17 | Sección wiki `Inteligencia Artificial` creada + entrada Asimov | [[1. Index Inteligencia Artificial]], [[2. Las Tres Leyes de Asimov - de la ficción a la IA real]] |
| 2026-11-18 | Driver NVIDIA resuelto: prime-select on-demand + módulo del kernel; `nvidia-smi` OK (RTX 2060, 6 GB, CUDA 13.2) | [[MYK - Hardware del equipo]] § Estado del driver |
| 2026-11-18 | Ollama 0.40.16 instalado portable en `~/tools/ollama` + entrada wiki sobre runtimes | [[3. Ollama - el runtime que ejecuta modelos locales]] |
| 2026-11-19 | Primer modelo local `llama3.2:3b` + primera inferencia 100% GPU (84,8 tok/s) + API OpenAI verificada | `ollama ps`, `/api/generate`, `/v1/chat/completions` |
| 2026-11-19 | Repo `Nicolasmp92/myk` creado + primer código (`myk.py` CLI chat, stdlib) | github.com/Nicolasmp92/myk |
| 2026-11-19 | UI web Angular en `web/` — chat streaming vs Ollama, lint+tests+build verdes, dev :4207 | commit `c48ae02` |
| 2026-11-19 | Persona "Chari" + llamita SVG animada en toda la UI | commit `19ab84f` |
