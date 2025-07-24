[🔙 Volver al índice](obsidian://open?vault=ObsidianDBNiko&file=niko_wiki%2FGit%20y%20Github%2FIndex%20Git)

---


# 🐙 Cómo Crear un Repositorio en GitHub.

1. Ve a [https://github.com](https://github.com)
2. Inicia sesión con tu cuenta (o regístrate si no tienes una).
3. Haz clic en el botón **➕ New repository** (arriba a la derecha).
4. Completa los siguientes campos:
   - **Repository name:** (ej. `mi-proyecto`)
   - **Description:** (opcional, pero recomendable)
   - **Visibility:** elige `Public` o `Private`
5. 🔁 **NO marques** "Add a README" si vas a conectar un proyecto local ya existente (Laravel, Angular, etc.).
6. Haz clic en **Create repository**

---

## 🔗 2. Conectar el repositorio con tu proyecto local (Laravel, Angular, etc.)

Una vez creado el repositorio en GitHub, verás una URL como esta:

https://github.com/tuusuario/mi-proyecto.git

Ojo en alguna parte de tu repo encontraras la opción de copiar esta url, también se puede utilizar para SSH

Ahora en tu proyecto local:

```bash
git init                         # Inicia Git en tu carpeta local
git add .                        # Agrega todos los archivos al seguimiento
git commit -m "Primer commit"   # Guarda la versión inicial
git branch -M main              # Establece el nombre de la rama principal
git remote add origin https://github.com/tuusuario/mi-proyecto.git
git push -u origin main         # Sube todo al repo en GitHub
🧠 Si el repo remoto ya tenía archivos (como un README), haz primero:

git pull origin main --allow-unrelated-histories
