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

## 2026-11-18

- **HECHO** — RIESGO del driver NVIDIA resuelto: `nvidia-smi` OK — RTX 2060, 6.144 MiB VRAM, driver 595.99.02, CUDA 13.2. Causa raíz de dos capas: (1) `prime-select intel` tenía blacklist-nvidia.conf (`alias nvidia off`) bloqueando el módulo — el error `could not insert 'off'` delataba el alias; (2) faltaba el paquete `linux-modules-nvidia-595-open` para el kernel vigente. Fix: instalar módulo del kernel + `prime-select on-demand` + `modprobe`. Detalle completo en [[MYK - Hardware del equipo]].
- **HECHO** — Kernel actualizado a 7.0.0-43 con su módulo nvidia-595-open correspondiente; GPU queda disponible para CUDA en modo on-demand (pantalla sigue en iGPU Vega).

## 2026-11-18 (tarde)

- **HECHO** — Ollama v0.40.16 instalado **portable** en `~/tools/ollama` (tarball oficial, sin sudo ni systemd; el script oficial requiere root). Servidor detecta la RTX 2060 solo: CUDA0, 5,5 GiB disponibles, contexto default 4096.
- **RIESGO menor** — Pull de `llama3.2:3b` se cayó a la mitad por DNS transitorio (`r2.cloudflarestorage.com` no resolvía en 127.0.0.53) — mismo síntoma intermitente ya visto con GitHub. Resolver reintenta y listo.

## 2026-11-19

- **HECHO** — **Primera IA local corriendo**: `llama3.2:3b` descargado (2,0 GB → `~/.ollama/models`), inferencia verificada **100% GPU** — 40 tokens en 0,5 s = **84,8 tok/s**, 2,6 GB en VRAM, contexto 4096.
- **HECHO** — API compatible OpenAI verificada: `GET /v1/models` lista el modelo y `POST /v1/chat/completions` responde → cualquier app que hable protocolo OpenAI puede usar el modelo local apuntando a `localhost:11434`. Anécdota didáctica: el 3B respondió en italiano a un prompt ambiguo — modelos chicos derivan de idioma.
- **HECHO** — Entrada wiki [[3. Ollama - el runtime que ejecuta modelos locales]] escrita (inferencia vs entrenamiento, qué hace un runtime, cuantización GGUF/Q4, Ollama vs llama.cpp/LM Studio/vLLM, tradeoffs local vs nube).
- **PENDIENTE** — Servidor Ollama no arranca solo al boot (es nohup manual). Opciones: `systemd --user` unit o reinstalar con script oficial (sudo).
- **HECHO** — Repo satélite creado: `~/Escritorio/Desarrollo/myk` → `Nicolasmp92/myk` (privado, credencial embebida en remote como el resto de repos). Primer código: `myk.py` — CLI de chat sobre la API local (`/api/chat`, streaming, historial, comandos `/nuevo` `/salir`, solo stdlib). Smoke test OK — responde en español con su system prompt (2026-11-19).
- **HECHO** — **UI web propia**: `web/` en el repo — Angular 22 SSR + Tailwind 4 + signals (stack de la casa). Chat con streaming token a token vía `fetch`+`TextDecoderStream` (HttpClient no streamea), selector de modelo desde `/api/tags`, semáforo de estado del servidor, estado vacío/cargando/error con reintento, Enter/Shift+Enter, mobile-first, `afterNextRender` para no llamar la API en SSR. Puerto **4207**. Lint + 8/8 tests Vitest + build verdes; chunk del chat lazy 7 kB. Commit `c48ae02` (rama `feat/ui-angular-chat` mergeada). Skill desarrollo-aplicaciones aplicada (línea vertical primero) (2026-11-19).
