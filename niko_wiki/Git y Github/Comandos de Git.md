# 🧪 Comandos de Git: Guía Completa

## 📌 ¿Qué es Git?

**Git** es un sistema de control de versiones que permite llevar el seguimiento de los cambios realizados en un proyecto. Se utiliza principalmente en desarrollo de software y se integra fácilmente con GitHub, GitLab, etc.

---

## 🔹 Comandos básicos de configuración

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"
```
🔧 Configura tu identidad para los commits. Solo necesitas hacerlo una vez.

🔹 Crear o clonar un repositorio
```bash
git init
```
Crea un repositorio Git vacío en la carpeta actual.

```bash
git clone https://github.com/usuario/repositorio.git
```
Clona un repositorio remoto (GitHub, GitLab, etc.) a tu computadora.

🔹 Ver estado del repositorio
```bash
git status
```
Muestra los archivos modificados, nuevos o eliminados pendientes de confirmar.

🔹 Añadir archivos al área de preparación (staging)
```bash
git add archivo.txt
// Tambien puedes hacerlo para variso
git add archivo1.txt archivo2.php archivo3.blade.php
```
Añade un archivo especificado por su nombre.
```bash
git add .
```
Agrega todos los archivos modificados al staging.

🔹 Confirmar cambios (commit)
```bash
git commit -m "Mensaje claro de los cambios"
```
Registra los cambios preparados con un mensaje descriptivo.

🔹 Ver historial de commits
bash
Copiar
Editar
git log
Lista los commits realizados.

bash
Copiar
Editar
git log --oneline
Muestra los commits en formato resumido.

🔹 Ver diferencias (diff)
bash
Copiar
Editar
git diff
Muestra los cambios realizados en el código antes del commit.

bash
Copiar
Editar
git diff --staged
Muestra los cambios ya añadidos con git add.

🔹 Ramas (branches)
bash
Copiar
Editar
git branch
Muestra las ramas existentes.

bash
Copiar
Editar
git branch nombre_rama
Crea una nueva rama.

bash
Copiar
Editar
git checkout nombre_rama
Cambia a otra rama.

bash
Copiar
Editar
git checkout -b nueva_rama
Crea y cambia a una nueva rama en un solo paso.

🔹 Fusionar ramas (merge)
bash
Copiar
Editar
git merge nombre_rama
Fusiona la rama indicada con la rama actual.

🔹 Eliminar ramas
bash
Copiar
Editar
git branch -d nombre_rama
Elimina una rama local si ya fue fusionada.

bash
Copiar
Editar
git push origin --delete nombre_rama
Elimina una rama del repositorio remoto.

🔹 Trabajar con repositorio remoto (GitHub)
bash
Copiar
Editar
git remote -v
Muestra los repositorios remotos conectados.

bash
Copiar
Editar
git remote add origin https://github.com/usuario/repositorio.git
Conecta un repositorio local a uno remoto.

bash
Copiar
Editar
git push origin main
Envía tus commits al repositorio remoto (main es la rama).

bash
Copiar
Editar
git pull origin main
Descarga los últimos cambios del repositorio remoto.

🔹 Deshacer cambios
bash
Copiar
Editar
git checkout -- archivo.txt
Revierte los cambios en un archivo antes de hacer commit.

bash
Copiar
Editar
git reset archivo.txt
Saca un archivo del staging (git add).

bash
Copiar
Editar
git reset --soft HEAD~1
Revierte el último commit pero conserva los cambios en staging.

bash
Copiar
Editar
git reset --hard HEAD~1
Revierte el último commit y borra los cambios. ⚠️ ¡Irreversible!

🔹 Etiquetas (tags)
bash
Copiar
Editar
git tag v1.0
Crea una etiqueta simple.

bash
Copiar
Editar
git tag -a v1.0 -m "Versión estable"
Etiqueta con mensaje (anotada).

bash
Copiar
Editar
git push origin --tags
Sube las etiquetas al repositorio remoto.

🧠 Tips útiles
Comando	Qué hace
git show	Muestra información detallada de un commit
git stash	Guarda temporalmente cambios sin hacer commit
git stash pop	Recupera lo guardado en el stash
git clean -f	Borra archivos sin seguimiento (⚠️ cuidado)
git rm archivo.txt	Borra un archivo y lo marca para commit

🧭 Flujos de trabajo comunes
🔁 Ciclo básico
git pull origin main

Haces tus cambios...

git add .

git commit -m "Mensaje"

git push origin main

🧩 Bonus: Archivo .gitignore
Para evitar subir archivos o carpetas al repo (como /vendor, .env, etc.):

bash
Copiar
Editar
/vendor
/node_modules
.env
.DS_Store
📎 Recursos útiles
Git Cheat Sheet en español (GitHub)

Pro Git Book (oficial)

GitHub Docs

