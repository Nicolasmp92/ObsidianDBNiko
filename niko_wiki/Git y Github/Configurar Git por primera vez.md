[🔙 Volver al índice](index Git y Github)

# 🛠️ Configurar Git por primera vez

Una vez instalado Git, es fundamental hacer una **configuración inicial** para que tus cambios queden correctamente registrados con tu nombre y correo.  
También puedes personalizar algunos comportamientos para que tu experiencia sea más cómoda.

---

## 👤 1. Configurar tu identidad

Git necesita saber **quién eres**, para registrar tu autoría en cada cambio. Para eso debes indicarle:

- Tu nombre completo
- Tu correo electrónico

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

🆘 ¿Y de dónde saco esos datos?
Si ya creaste una cuenta en GitHub, usa el mismo nombre y correo que usaste para registrarte.
Esto permite que tus contribuciones se vinculen correctamente a tu perfil.

➡️ Si aún no tienes una cuenta o no sabes cómo verla, revisa la guía:
👉 [[Inicio en GitHub|Cómo crear y configurar tu cuenta en GitHub]]


## ⚙️ 2. Configuraciones recomendadas

|Descripción|Comando|
|---|---|
|Editor por defecto (VS Code)|`git config --global core.editor "code --wait"`|
|Alias para `git status`|`git config --global alias.s status`|
|Alias para `git commit -m`|`git config --global alias.c "commit -m"`|
|Mostrar cambios con color|`git config --global color.ui auto`|
|Codificación UTF-8|
## 🧪 3. Ver tu configuración actual

Para ver lo que ya configuraste:

 ```bash
git config --list
```
> Muestra tu nombre, correo, alias y otras opciones activas.

También puedes editar directamente el archivo donde se guarda todo esto:
```bash
git config --global --edit
```
---

✅ Con esto, Git ya está listo para usarse en cualquier proyecto de forma cómoda y personalizada.

➡️ Siguiente: 🐙 Crear un Repositorio en GitHub