**Tags:** #Git #Comandos #Productividad  
**Anterior:** [[Instalación y Configuración Inicial]] | **Siguiente:** [[Convenciones de Nomenclatura de Ramas en Git]]

---

📌 El Ciclo de Vida del Código

Antes de ver los comandos, recuerda que en Git el código viaja por tres estados:

1. **Working Directory:** Donde escribes (tus archivos).
2. **Staging Area:** La "sala de espera" (`git add`).
3. **Local Repo:** El historial guardado (`git commit`).
4. **Remote Repo:** La nube (`git push`).

---

🛠️ Comandos Esenciales

🔹 Preparación y Guardado

| Acción          | Comando               | Nota                           |
| --------------- | --------------------- | ------------------------------ |
| **Ver estado**  | `git status`          | Hazlo siempre antes de seguir. |
| **Añadir todo** | `git add .`           | Prepara todos los archivos.    |
| **Guardar**     | `git commit -m "..."` | Usa [[Conventional Commits]].  |
| **Historial**   | `git log --oneline`   | Ver commits de forma resumida. |

🌿 Gestión de Ramas (Branches)

> [!TIP] Organización  
> Recuerda seguir la [[Convenciones de Nomenclatura de Ramas en Git|convención de nombres]] (`feat/`, `fix/`, etc.) para mantener el orden.

- `git branch`: Lista las ramas.
- `git checkout -b nueva-rama`: Crea una rama y se mueve a ella.
- `git merge rama-a-traer`: Fusiona otra rama en la que estás actualmente.
- `git branch -d nombre-rama`: Borra una rama local.

---

🔄 Conexión Remota (GitHub)

- `git remote -v`: Verifica a qué repositorio estás conectado.
- `git push origin main`: Sube tus cambios a la nube.
- `git pull origin main`: Baja los cambios nuevos antes de empezar a trabajar.

---

⚠️ Zona de Emergencia (Deshacer cambios)

A veces las cosas salen mal. Aquí tienes cómo volver atrás:

> [!WARNING] ¡Cuidado con el Reset Hard!  
> El comando `git reset --hard` borra todo tu trabajo no guardado de forma irreversible. Úsalo solo si estás seguro.

- **Sacar del Staging (deshacer `add`):** `git reset archivo.txt`
- **Revertir commit (manteniendo archivos):** `git reset --soft HEAD~1`
- **Borrar último commit y cambios:** `git reset --hard HEAD~1`
- **Guardado temporal (Pausa rápida):** `git stash` (guarda lo que estás haciendo sin hacer commit para limpiar la mesa de trabajo). Usa `git stash pop` para recuperarlo.

---

🧩 El archivo `.gitignore`

Es fundamental para no subir "basura" o archivos sensibles al repo. Crea un archivo llamado `.gitignore` en la raíz y añade:

bash

```
/node_modules
/vendor
.env
.DS_Store
/storage/*.key
```

Usa el código con precaución.

---

¡Entendido! Aquí tienes el flujo con el formato estándar de Markdown que usamos siempre, listo para que lo lleves a tu Obsidian:

## 🛠️ Git Workflow: Guía Rápida

### 1. Sincronizar Base

Antes de empezar, asegúrate de que tu rama `dev` tenga lo último del servidor.

- `git checkout dev`
    
- `git pull origin dev`
    

### 2. Crear Tarea (Feature)

Crea una rama específica para lo que vas a programar.

- `git checkout -b feat/nueva-tarea`
    

### 3. Ciclo de Desarrollo

Mientras trabajas, guarda tus avances localmente.

- `git add .`
    
- `git commit -m "feat: descripción de la mejora"`
    

### 4. Publicar y Revisar

Sube tu rama y abre el **Pull Request** en GitHub hacia la rama `dev`.

- `git push origin feat/nueva-tarea`
    

### 5. Limpieza Post-Merge

Una vez que el PR se acepta y se mezcla en GitHub, limpia tu entorno local.

- `git checkout dev`
    
- `git pull origin dev`
    
- `git branch -d feat/nueva-tarea`
    
- `git fetch -p`
    

---

> **Nota Pro:** Si la rama no se deja borrar con `-d` (minúscula), usa `git branch -D feat/nueva-tarea` para forzar la eliminación. El comando `fetch -p` se encargará de borrar las "ramas fantasma" de tu lista remota.

¿Te parece bien este formato para tu flujo de trabajo diario?