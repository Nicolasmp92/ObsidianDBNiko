**Tags:** #Git #Estándares #Productividad

# Conventional Commits

Estándar para escribir mensajes de commit legibles por humanos y por máquinas. El formato base es:

```
<tipo>[scope opcional]: <descripción>
```

## Tipos principales

| Tipo | Uso | Impacto semver |
|---|---|---|
| `feat:` | Nueva funcionalidad | MINOR |
| `fix:` | Corrección de bug | PATCH |
| `docs:` | Solo documentación | — |
| `style:` | Formato (sin cambio de lógica) | — |
| `refactor:` | Cambio interno sin fix ni feature | — |
| `test:` | Agregar o corregir tests | — |
| `chore:` | Mantenimiento, tooling, deps | — |

Un `!` tras el tipo (`feat!:`) o el footer `BREAKING CHANGE:` marca un cambio incompatible → MAJOR.

## Ejemplos

```bash
git commit -m "feat(auth): agregar login con 2FA"
git commit -m "fix(rutinas): evitar duplicados al guardar rutina"
git commit -m "chore(deps): actualizar spatie/laravel-permission"
```

## Por qué usarlo

- Historial legible y escaneable (`git log --oneline` cuenta la historia).
- Permite generar CHANGELOGs automáticos.
- Combina bien con [[Convenciones de Nomenclatura de Ramas en Git]]: la rama `feat/xyz` produce commits `feat: xyz`.

---
**Relacionado:** [[GitFlow vs GitHub Flow]] | [[1 Index Git y Github]]
