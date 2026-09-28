# 🧩 Extensiones de VS Code — Setup

Extensiones recomendadas para el stack del vault (Angular front, Java/Spring Boot APIs). El archivo `.vscode/extensions.json` ya trae la lista — VS Code la detecta al abrir la carpeta y ofrece **"Install Recommended Extensions"**.

## ⚙️ Instalación

1. Abrir la carpeta del proyecto en VS Code.
2. Aceptar el toast *"Do you want to install the recommended extensions?"*
   — o manualmente: `Ctrl+Shift+X` → buscar `@recommended` → instalar todas.

## 📋 Extensiones

| Extensión | ID | Para qué |
|---|---|---|
| **Angular Language Service** ⭐ | `angular.ng-template` | **La más importante.** Autocompletado, errores y navegación dentro de templates `.html` (signals, `@if`, `input()`, pipes). Sin esto los templates quedan a ciegas |
| **Angular Essentials** | `johnpapa.angular-essentials` | Pack de John Papa: Language Service + snippets + utilidades Angular en una sola instalación |
| **Extension Pack for Java** | `vscjava.vscode-java-pack` | Pack completo Java: Language Support (Red Hat), Debugger, Test Runner, Maven, IntelliCode |
| **Spring Boot Extension Pack** | `vmware.vscode-boot-dev-pack` | Spring Boot Dashboard, soporte `application.properties`/`.yml`, Spring Initializr integrado — para las APIs REST |
| **ESLint** | `dbaeumer.vscode-eslint` | `ng lint` integrado al editor — requerido por [[Estándares Front-End - Angular]] |
| **Prettier** | `esbenp.prettier-vscode` | Formato al guardar (`printWidth: 100`, single quotes) — idem estándares |
| **Tailwind CSS IntelliSense** | `bradlc.vscode-tailwindcss` | Autocompletado de clases Tailwind 4 — idem estándares |

## 🔗 Relación con el vault

- Los estándares de estas extensiones están documentados en [[Estándares Front-End - Angular]] (lint, prettier, naming, workflow `npm`).
- Para el ecosistema del vault en sí: [[Plugins de Obsidian - Setup]].
