---
tipo: roadmap
proyecto: myk
actualizado: 2026-11-17
tags: [roadmap, ia-local]
---

# MYK — Roadmap de aprendizaje e implementación

Plan por fases. Nivel asumido: desde cero. Cada fase deja registro en `log.md` y destila lo aprendido a `04_Wiki/Inteligencia Artificial/`.

## Fase 0 — Fundamentos (en curso)

- [x] Crear el proyecto y la sección wiki `Inteligencia Artificial`
- [x] Entrada wiki: [[2. Las Tres Leyes de Asimov - de la ficción a la IA real]]
- [ ] Qué es un LLM, qué es inferencia vs entrenamiento, qué es cuantización → entrada wiki
- [ ] Panorama de modelos open-weight y licencias (Llama, Qwen, Mistral, Gemma…)

## Fase 1 — El equipo listo

- [x] Arreglar driver NVIDIA (ver [[MYK - Hardware del equipo]]) → `nvidia-smi` OK ✅ 2026-11-18
- [x] Decidir runtime: **Ollama** ✅ 2026-11-19 → entrada wiki [[3. Ollama - el runtime que ejecuta modelos locales]]

## Fase 2 — Primer modelo local

- [x] Instalar runtime y descargar primer modelo → Ollama 0.40.16 portable en `~/tools/ollama` + `llama3.2:3b` ✅ 2026-11-19
- [x] Primera conversación local + medir velocidad real → **84,8 tok/s, 100% GPU** ✅ 2026-11-19
- [x] Probar el endpoint local compatible con OpenAI → `/v1/models` + `/v1/chat/completions` OK en `http://localhost:11434` ✅ 2026-11-19
- [ ] Levantar el servidor de forma persistente (hoy: `~/tools/ollama/bin/ollama serve` manual; pendiente: servicio systemd de usuario o instalación oficial con sudo)

## Fase 3 — Uso real

- [ ] Definir primer caso de uso (ideas: asistente sobre las notas del vault con RAG, automatización de bitácoras, copiloto de código local)
- [ ] Evaluar límites: contexto, memoria, qué NO puede hacer un modelo local vs uno de nube

## Reglas del proyecto

- Documentar como para un principiante: el "yo" de dentro de 3 meses es el lector.
- Nada de servicios de nube para la inferencia: el objetivo es **local** (privacidad + aprendizaje).
- Toda decisión de adopción pasa por la skill `interrogatorio-adopcion` si implica dependencia pesada.
