# 🧩 Plugins de Obsidian — Setup del Vault

Extensiones de comunidad necesarias para este vault. El archivo `.obsidian/community-plugins.json` ya trae la lista precargada — solo falta instalarlas.

## ⚙️ Instalación (una sola vez)

1. Abrir el vault en Obsidian.
2. **Settings → Community plugins → Turn on community plugins** (desactivar *Restricted Mode*).
3. **Browse** y buscar cada plugin de la tabla → **Install** → **Enable**.
4. Recargar el vault si es necesario.

> [!NOTE] Nota sobre el config
> `community-plugins.json` marca los plugins como *habilitados*, pero Obsidian no los descarga solo: el paso de **Install** es manual por seguridad (los plugins ejecutan código).

## 📋 Plugins

| Plugin | ID | Para qué |
|---|---|---|
| **Kanban** | `obsidian-kanban` | Tableros kanban en markdown — **requerido por [[Desarrollo]]** y `Untitled Kanban.md` (frontmatter `kanban-plugin: board`) |
| **Advanced Tables** | `table-editor-obsidian` | Editar tablas markdown con Tab/Enter, auto-formato de columnas — la wiki está llena de tablas |
| **Sticky Notes** | `sticky-notes` | Ventanas flotantes tipo post-it (pin, colores) para notas rápidas |
| **Excalidraw** | `obsidian-excalidraw-plugin` | Diagramas y bocetos a mano alzada guardados en el vault (post-its visuales, mapas) |
| **Dataview** | `dataview` | Tablas/listas dinámicas por consulta (ej. "todas las notas con `status: En proceso`") — potencia los MOCs |

## 🗒️ Post-its sin plugins (nativo)

**Canvas** ya viene con Obsidian: crea tarjetas tipo post-it en un lienzo infinito (los `.canvas` del vault: `POSIT.canvas`, `Sin título*.canvas`). No necesita plugin — solo abrir el archivo. Si solo quieres tarjetas en lienzo, Canvas basta; el plugin Sticky Notes es para ventanas flotantes sobre la app.

## ✅ Verificación

Después de instalar:

- Abrir [[Desarrollo]] → debe renderizar como tablero, no como lista.
- En una tabla cualquiera, pulsar `Tab` → debe saltar de celda auto-formateando.
- Command palette (`Ctrl+P`) → "Sticky Notes" / "Excalidraw" deben aparecer.
