# Log — Myk

Bitácora append-only. Tipos: HECHO / DECISIÓN / HIPÓTESIS / RIESGO / PENDIENTE.

Repo: sin repo satélite (fase documental en el vault).
Stack: por definir (Ollama / llama.cpp candidatos).

## 2026-11-17

- **DECISIÓN** — Nace el proyecto **Myk**: investigar e implementar una IA de manera local en este equipo. Metodología: la del vault (MOC + log tipificado + registro; conocimiento destilado a `04_Wiki/`). El usuario declara partir desde cero → el material se escribe en nivel introductorio.
- **HECHO** — Auditoría de hardware del equipo documentada en [[MYK - Hardware del equipo]]: Ryzen 7 3750H (4c/8t), 15 GiB RAM, RTX 2060 Mobile 6 GB + iGPU Radeon Vega, 362 GB libres, Ubuntu 24.04.5.
- **RIESGO** — Driver NVIDIA roto: librerías de la versión 595.91.07 instaladas pero `nvidia-smi` no logra comunicar con el driver → la GPU no sirve para inferencia hasta resolverlo (módulo no cargado / posible Secure Boot o kernel nuevo sin rebuild). Sin GPU, solo queda CPU (lento pero usable con modelos pequeños).
- **HECHO** — Creada sección `04_Wiki/Inteligencia Artificial/` con índice y primera entrada: [[2. Las Tres Leyes de Asimov - de la ficción a la IA real]] (fuentes reales citadas: Brookings, FLI/Asilomar, The Conversation, MIT Press Reader, Computerphile).
- **PENDIENTE** — Próximos temas wiki sugeridos: qué es un LLM e inferencia vs entrenamiento, cuantización (GGUF/Q4), panorama de runtimes locales (Ollama, llama.cpp, LM Studio), modelos open-weight que caben en 6 GB VRAM.
