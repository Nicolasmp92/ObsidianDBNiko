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

- [ ] Arreglar driver NVIDIA (ver [[MYK - Hardware del equipo]]) → `nvidia-smi` OK
- [ ] Decidir runtime: Ollama (DX simple) vs llama.cpp (control) → entrada wiki comparativa

## Fase 2 — Primer modelo local

- [ ] Instalar runtime y descargar primer modelo (candidato ~3B–8B Q4 según GPU/CPU)
- [ ] Primera conversación local + medir velocidad real (tokens/seg) en este hardware
- [ ] Probar el endpoint local compatible con OpenAI (`http://localhost:11434` en Ollama)

## Fase 3 — Uso real

- [ ] Definir primer caso de uso (ideas: asistente sobre las notas del vault con RAG, automatización de bitácoras, copiloto de código local)
- [ ] Evaluar límites: contexto, memoria, qué NO puede hacer un modelo local vs uno de nube

## Reglas del proyecto

- Documentar como para un principiante: el "yo" de dentro de 3 meses es el lector.
- Nada de servicios de nube para la inferencia: el objetivo es **local** (privacidad + aprendizaje).
- Toda decisión de adopción pasa por la skill `interrogatorio-adopcion` si implica dependencia pesada.
