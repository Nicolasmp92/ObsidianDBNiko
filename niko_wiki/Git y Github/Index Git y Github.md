volver [[index niko_wiki]]

# 🧠 Git y GitHub: Control de versiones

## 1. Introducción: ¿Qué son Git y GitHub?

- **Git** es un programa que instalas en tu computador para guardar el historial de tus archivos. Permite controlar versiones, crear ramas y trabajar en equipo.
- **GitHub** es una plataforma web donde puedes guardar tus proyectos Git, colaborar con otros y mantener tus repos en la nube.

## 2. Diferencias clave entre Git y GitHub

| Git                   | GitHub                                     |
| --------------------- | ------------------------------------------ |
| Se instala local      | Es una plataforma web                      |
| Controla versiones    | Almacena proyectos online                  |
| Funciona sin internet | Necesita internet para subir/bajar cambios |
| Comandos CLI (`git`)  | Interfaz web + remoto (`github.com`)       |

> 🧠 Git es la herramienta, GitHub es el lugar donde guardas tu trabajo.

# 🖥️ Git, terminales y comandos más usados

**Git** se instala de manera **local** en tu computador. Para interactuar con él, usamos algo llamado **terminal** o línea de comandos.

---

## ⚙️ ¿Qué es una terminal?

Una **terminal** es una ventana donde puedes escribir instrucciones que ejecuta el sistema.

### Algunas terminales populares:

| Terminal             | Sistema         | Descripción breve |
|----------------------|------------------|-------------------|
| **CMD**              | Windows          | Terminal clásica de Windows, básica. |
| **PowerShell**       | Windows          | Más moderna, permite scripts avanzados. |
| **Git Bash**         | Windows (con Git) | Terminal que emula Linux para usar comandos Unix con Git. |
| **Terminal de Linux**| Linux            | Consola nativa, muy poderosa. |
| **Terminal de macOS**| macOS            | Basada en Unix, similar a Linux. |
| **Terminal de VS Code**| Todas           | Se integra al editor para trabajar sin salir del entorno. |

---

## 💡 ¿Qué se puede hacer desde la terminal?

Al instalar Git, puedes usar comandos para:

- Iniciar el seguimiento de un proyecto
- Guardar cambios
- Subirlos al repositorio remoto
- Cambiar entre versiones
- Ver historial, ramas, y más

---

## 🧾 Comandos esenciales de Git

| Acción                             | Comando                              |
|------------------------------------|--------------------------------------|
| Iniciar Git en una carpeta         | `git init`                           |
| Ver estado de los archivos         | `git status`                         |
| Agregar archivos para guardar      | `git add .`                          |
| Guardar cambios con mensaje        | `git commit -m "mensaje"`            |
| Ver historial de cambios           | `git log`                            |
| Subir cambios a GitHub             | `git push`                           |
| Traer cambios de GitHub            | `git pull`                           |
| Clonar un proyecto desde GitHub    | `git clone URL-del-repo`             |
| Crear nueva rama                   | `git branch nombre-rama`             |
| Cambiar de rama                    | `git checkout nombre-rama`           |
| Ver ramas existentes               | `git branch`                         |

>📌 **Todos estos comandos se escriben desde la terminal que prefieras** (recomendado: Git Bash o la terminal integrada de VS Code).

> **¡Importante!** Si eres principiante, por experiencia personal te sugiero comenzar utilizando la terminal **Git Bash** para trabajar con Git.  
> Aunque más adelante mencionaremos un entorno gráfico llamado **GitHub Desktop**, te recomiendo ignorarlo por ahora, ya que puede dificultarte el aprendizaje.  
> De hecho, yo no lo utilizo: cuando lo probé, me generó varios problemas.


✅ Con esto, ya sabes cómo usar Git desde la terminal, cuáles son los comandos más importantes.

---


# 🚀 Evolución de GitHub y Herramientas Inteligentes

## 🌐 ¿Solo existe GitHub?

No. Aunque **GitHub** es la plataforma más popular, existen otras opciones para alojar repositorios:

| Plataforma      | Enlace                    | Notas                   |
|------------------|----------------------------|--------------------------|
| **GitHub**        | [github.com](https://github.com) | La más usada y con mejores integraciones |
| **GitLab**        | [gitlab.com](https://gitlab.com) | Excelente para proyectos privados |
| **Bitbucket**     | [bitbucket.org](https://bitbucket.org) | Popular en empresas (integración con Jira) |

> 💬 **Yo me quedo con GitHub** por su facilidad de uso, comunidad, y herramientas como Copilot y GitHub Desktop.

---

Con el tiempo, GitHub ha dejado de ser solo “el lugar donde se guarda el trabajo” para convertirse en un **centro completo de desarrollo colaborativo**. Se han agregado muchas funciones nuevas que ayudan a programar más rápido, organizar mejor el código y trabajar en equipo sin enredos.

---

## 🤖 GitHub Copilot

Una de las funciones más revolucionarias es **[GitHub Copilot](https://github.com/features/copilot)**, una extensión con inteligencia artificial integrada con ChatGPT que te **sugiere líneas de código** mientras escribes.

> Es como tener un programador ayudante al lado. Funciona en VS Code, Neovim, JetBrains, etc.

Te permite:
- Autocompletar funciones completas
- Sugerir nombres de variables, estructuras, bucles, etc.
- Traducir comentarios en código
- Evitar escribir código repetitivo

---

## 💻 GitHub Desktop

Para quienes prefieren no usar la terminal, **[GitHub Desktop](https://desktop.github.com/)** es una interfaz gráfica que te permite:

- Hacer commits fácilmente
- Realizar `push` y `pull` con un clic
- Resolver conflictos visualmente
- Cambiar entre ramas (branches)
- Ver historial de cambios

> Muy útil para comenzar con Git sin miedo. Ideal para proyectos personales, educativos o colaborativos.

---

## 🧭 Comandos importantes de Git (que GitHub Desktop automatiza)

| Acción                   | Comando Git                  |
|--------------------------|------------------------------|
| Iniciar proyecto         | `git init`                   |
| Ver estado del repo      | `git status`                 |
| Agregar archivos         | `git add .` o `git add archivo` |
| Guardar cambios (commit) | `git commit -m "mensaje"`    |
| Subir al repositorio     | `git push`                   |
| Traer cambios nuevos     | `git pull`                   |
| Clonar proyecto          | `git clone URL`              |
| Cambiar de rama          | `git checkout nombre-rama`   |
| Crear nueva rama         | `git branch nueva-rama`      |
| Ver historial            | `git log`                    |

---

✅ Con estas herramientas, Git y GitHub ya no son solo para expertos. Gracias a interfaces como GitHub Desktop y asistentes como Copilot, cualquiera puede llevar el control de versiones de forma ordenada y profesional.

Ahora ya sabes todo lo importante sobre estas herramientas, ¡hora de instalarlas!  
👉 Comienza con la [[instalación Git|instalación de Git]] y luego sigue con el [[Inicio en GitHub|inicio en GitHub]].
