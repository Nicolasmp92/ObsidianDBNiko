**Tags:** #Git #Setup #Configuración  
**Anterior:** [[Git y GitHub: El Mapa Maestro]]

---

🧰 1. Instalar Git

Antes de empezar, necesitamos el motor de Git funcionando en tu sistema.

🪟 En Windows (Recomendado)

1. Descarga el instalador en git-scm.com.
2. **Importante:** Durante la instalación, marca la casilla **"Git Bash Here"**.
3. Al terminar, usa siempre **Git Bash** (clic derecho en cualquier carpeta > _Git Bash Here_).

🐧 En Linux / 🍎 macOS

bash

```
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install git

# macOS (Usando Homebrew)
brew install git
```

Usa el código con precaución.

> [!CHECK] Verificación  
> Abre tu terminal y escribe `git --version`. Si ves algo como `git version 2.x.x`, ¡estás listo!

---

👤 2. Configuración de Identidad (Primeros Pasos)

Git necesita saber quién eres para firmar tus cambios. Ejecuta estos comandos en tu terminal (solo una vez):

bash

```
# Configura tu nombre global
git config --global user.name "Tu Nombre"

# Configura tu correo (el mismo que usas en GitHub)
git config --global user.email "tu-correo@ejemplo.com"

# Opcional: Configura la rama principal por defecto como 'main'
git config --global init.defaultBranch main
```

Usa el código con precaución.

---

🐙 3. Creación y Conexión con GitHub

Ahora que Git sabe quién eres localmente, vamos a conectarlo con la nube.

A. Crear el Repositorio en la Web

1. Ve a github.com y crea un **New Repository**.
2. Dale un nombre (ej. `mi-proyecto`).
3. **⚠️ Tip Pro:** No marques "Add a README" si ya tienes código en tu carpeta local; esto evita conflictos de historial al inicio.

B. Vincular tu Proyecto Local

Si ya tienes una carpeta con archivos (como un proyecto de Laravel o Angular), sitúate en ella desde **Git Bash** y lanza este "combo" de comandos:

bash

```
git init                                     # Inicia Git localmente
git add .                                    # Prepara todos los archivos
git commit -m "feat: initial commit"         # Primer guardado
git branch -M main                           # Asegura que la rama se llame main
git remote add origin https://github.com
git push -u origin main                      # Sube todo y vincula las ramas
```

Usa el código con precaución.

> [!TIP] ¿Problemas de permisos?  
> Si el repo remoto ya tenía un README o archivos creados en la web, usa:  
> `git pull origin main --allow-unrelated-histories` para fusionar ambos historiales antes de subir el tuyo.

---

**¿Qué sigue?** Ahora que tienes todo conectado, es hora de aprender el flujo diario en:  
👉 **[[Comandos de Git y Flujo de Trabajo]]**

---