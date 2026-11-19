---
tipo: nota-tecnica
actualizado: 2026-11-19
tags: [herramientas, transferencia, croc, cli]
---

# croc — transferir archivos entre equipos

> **Pregunta que responde esta nota:** ¿qué es croc y cómo se usa para pasar archivos entre mis PCs (ej. compu pega ↔ PC casa)?
>
> **Respuesta corta:** croc es un CLI que transfiere archivos/carpetas entre **dos computadores cualquiera** con cifrado extremo a extremo, sin servidor propio ni puertos abiertos: el emisor corre `croc send archivo`, recibe una frase-código, y el receptor corre `croc frase-código`. Instalado acá en `~/tools/croc` (v11.6.5, portable sin sudo) y verificado end-to-end el 2026-11-19. El detalle abajo.

## 1. Cómo funciona

```
PC A (envía)                          PC B (recibe)
────────────                          ────────────
croc send notas.zip        ──►  frase-código (ej. risk-stung-whiff)
        │                                    │
        └─── conexión P2P cifrada E2E ───────┘
             (relay solo si P2P no se logra;
             el relay nunca puede leer nada)
```

- La frase-código (palabras del diccionario EFF) alimenta un intercambio **PAKE**: de ella deriva la clave de cifrado E2E — el código ES el secreto, tratarlo como contraseña.
- Intenta conexión **directa P2P** (IPv6 primero, IPv4 de respaldo); si la red lo impide, cae al **relay** (por defecto el público de croc, también auto-hospedable).
- Multiarchivo, carpetas enteras, **reanudación** de transferencias cortadas, proxy/Tor, y versión web compatible en getcroc.com (sin instalar nada del otro lado).

## 2. Instalación en este equipo (sin sudo)

```bash
# tarball oficial → ~/tools (mismo patrón que ollama portable)
mkdir -p ~/tools/croc
curl -sL https://github.com/schollz/croc/releases/download/v11.6.5/croc_v11.6.5_Linux-64bit.tar.gz \
  | tar -xz -C ~/tools/croc
ln -sf ~/tools/croc/croc ~/.local/bin/croc   # ya está en PATH
```

Otras vías oficiales: `curl https://getcroc.com | bash` (instala a `~/.local/bin` con `-p`), brew/scoop/choco/apt(pkg.haus)/pacman/pkg, o `go install` con Go 1.27+. Para actualizar: `croc update` + `croc-update`.

## 3. Uso básico

```bash
# Emisor
croc send archivo.zip            # imprime: "On the other computer, run: croc <frase>"

# Receptor (interactivo: pregunta confirmar y sobreescritura)
croc frase-codigo-aqui

# Saltar confirmaciones (scripts / ya confías)
croc --yes frase-codigo-aqui
```

**⚠️ Gotcha real de v11 en Linux (lo vimos al instalar):**

1. Pasar el código por línea de comandos lo deja visible en la lista de procesos del sistema (CVE-2023-43621). croc v11 lo advierte: la primera vez pide habilitar el *classic mode* (`(y/N)`) — responder `y` una sola vez; queda `~/.config/croc/classic_enabled`.
2. La forma recomendada en Linux/macOS es por variable de entorno, sin que el secreto toque la línea de comandos:

   ```bash
   CROC_SECRET="frase-codigo" croc          # recibir
   croc send --code frase-codigo archivo    # fijar código propio al enviar
   ```

## 4. Features útiles para nosotros

| Uso | Comando |
|---|---|
| Enviar **texto** (no solo archivos) | `croc send --text "token o nota corta"` |
| Código propio/memorable | `croc send --code mi-frase archivo` |
| Carpeta completa | `croc send carpeta/` — incluye `.git`; **rechaza rutas `.ssh`/`.gnupg`** (protección) |
| Relay propio | `croc relay` en un servidor → `--relay "host:9009"` en ambos lados (puertos 9009-9013) |
| Almacenamiento cifrado temporal | modo "stored": sube al relay y el receptor baja después (no simultáneo) |
| Terminal compartida (v11) | `croc ssh` — invitaciones read/write y read-only; no abre un daemon SSH |
| Navegador sin instalar | getcroc.com — enviar/recibir entre web y CLI |

**Candidato natural:** el VPS NAMP podría hospedar `croc relay` propio si el público nos queda corto — el relay solo ve bytes cifrados, pero el nuestro elimina la dependencia externa.

## 5. Seguridad en una línea

Cifrado E2E derivado del código vía PAKE → el relay ni el ISP pueden leer el contenido. Lo único sensible es la frase-código: compártela por canal separado si el archivo importa (mismo criterio del `.7z` a Cristóbal: archivo por un lado, clave por otro). Curva por defecto moderna; `--curve p521` si se quiere la más fuerte.

## 6. Estado actual y prueba

- Instalado: **compu pega** (por el usuario) y **PC casa** (`~/tools/croc`, v11.6.5, symlink en `~/.local/bin`).
- Verificado 2026-11-19: loopback local `send`→`receive` con `risk-stung-whiff`, archivo íntegro. Falta la prueba real entre los dos PCs.

## Glosario mínimo

- **PAKE:** protocolo que deriva una clave compartida fuerte desde una frase débil (el código) sin enviarla nunca — base del E2E de croc.
- **Relay:** servidor que puentea cuando el P2P directo no conecta; ve tráfico cifrado solamente.
- **Frase-código / code phrase:** 3 palabras EFF que identifican la transferencia y derivan la clave — es a la vez dirección y contraseña.
- **Classic mode:** modo v11 que vuelve a permitir `croc <codigo>` por línea de comandos (menos seguro en sistemas multiusuario; ya habilitado acá).

## Fuentes consultadas (2026-11-19)

- GitHub schollz/croc — README oficial (uso, CROC_SECRET/CVE-2023-43621, `--code`, `--text`, `croc relay`, `croc ssh`, stored mode, updates): https://github.com/schollz/croc
- getcroc.com — versión web sin instalación: https://getcroc.com
