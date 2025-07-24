[🔙 Volver al índice](obsidian://open?vault=ObsidianDBNiko&file=niko_wiki%2FGit%20y%20Github%2FIndex%20Git)

---
# ⚙️ Instalar y Configurar Git (por primera vez)

Esta guía te ayudará a **instalar Git**, **configurarlo por primera vez** y aplicar una personalización básica para trabajar de forma más cómoda desde la terminal.

---
## 🧰 1. Instalar Git

### 🪟 En Windows

1. Ve a [https://git-scm.com](https://git-scm.com)
2. Descarga el instalador para Windows.
3. Ejecuta el instalador y sigue los pasos predeterminados.  
   > ⚠️ **Importante**: durante la instalación, asegúrate de marcar la opción **"Git Bash Here"** para que aparezca al hacer clic derecho sobre carpetas.
4. Al finalizar, abre **Git Bash** desde el menú inicio o con clic derecho en una carpeta → **"Git Bash Here"**.

> Si no ves la opción al hacer clic derecho, puedes reinstalar Git y asegurarte de activar esa casilla en el instalador.

---

### 🐧 En Linux

```bash
sudo apt update
sudo apt install git
```

🍎 En macOS
```bash
Copiar código
brew install git
```

🔍 2. Comprobar instalación
Después de instalar Git, abre una terminal y ejecuta el siguiente comando:
```bash
git --version
👀 Si Git está correctamente instalado, deberías ver una salida similar a:
```

``` nginx
git version 2.44.0.windows.1
```
La versión puede variar según tu sistema operativo y la fecha.

✅ ¡Listo! Ya tienes Git instalado correctamente. En la siguiente sección aprenderás a configurarlo con tu nombre, correo y ajustes útiles.

➡️ Siguiente: [[conf]]