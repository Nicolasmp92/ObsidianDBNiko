**Tags:** #Desarrollo #Git #Productividad  
**Relacionado:** [[Conventional Commits]] | [[GitFlow]]

---

📌 Resumen

Uso de **prefijos** para categorizar el trabajo en el repositorio. Ayuda a que el equipo sepa qué esperar de una rama antes de mirar el código.

🛠 Tipos de Ramas (Standard)

| Prefijo     | Uso                      | Ejemplo               |
| ----------- | ------------------------ | --------------------- |
| `feat/`     | Nuevas características   | `feat/login-social`   |
| `refactor/` | Mejorar código existente | `refactor/clean-api`  |
| `fix/`      | Corregir errores         | `fix/error-pago`      |
| `docs/`     | Solo documentación       | `docs/update-install` |
| `chore/`    | Mantenimiento/Config     | `chore/deps-update`   |
| `perf/`     | Mejora de rendimiento    | `perf/load-images`    |

---

🚀 Estrategias Populares

1. **GitFlow**: El modelo clásico. Usa `feature/`, `release/`, y `hotfix/`.
2. **GitHub Flow**: Ramas cortas y simples. Ideal para CI/CD.
3. **Trunk-based**: Pocas ramas, integración constante a `main`.

💡 Notas Adicionales

> [!TIP] Tip de Organización  
> Si usas el plugin **Dataview** en Obsidian, puedes etiquetar tus notas de proyectos con estos mismos prefijos para mantener una trazabilidad total entre tus notas y tu código.

---