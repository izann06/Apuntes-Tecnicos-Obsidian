**Tags:** #mcp #configuracion #conexion #vscode #claude-desktop

> [!info] Navegación
> ◀ Anterior: [[📂MCP/03 - Primitivos de MCP Tools Resources y Prompts|Primitivos]] | Siguiente ▶: [[📂MCP/05 - Casos de Uso Reales y Proyecto Práctico|Casos de Uso]]

---

# 04 — Cómo Conectar y Utilizar Servidores MCP

> [!quote] Concepto Clave
> Conectar un servidor MCP a tu entorno de trabajo es sorprendentemente sencillo. En la mayoría de casos, es pegar un bloque JSON en un archivo de configuración. Esta nota cubre los dos escenarios principales: chatbots de escritorio e IDEs.

---

## 💬 Conexión desde un Chatbot (Claude Desktop)

Claude Desktop es el [[📂MCP/02 - Arquitectura Host Cliente y Servidor|Host]] más popular para MCP.

### Pasos para conectar un servidor MCP remoto (HTTP)

1. Abre **Settings → Connectors → Custom Connector**
2. Pega la URL del servidor MCP (proporcionada por el servicio, ej. Supabase)
3. Autoriza el acceso mediante **OAuth** (se abre una ventana de autorización del servicio)
4. Claude descubre automáticamente las [[📂MCP/03 - Primitivos de MCP Tools Resources y Prompts|herramientas disponibles]]

### Pasos para conectar un servidor MCP local (STDIO)

Edita el archivo de configuración de Claude Desktop:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/usuario/proyectos"],
      "env": {}
    }
  }
}
```

> [!tip] Qué pasa al guardar este archivo
> 1. Claude Desktop arranca automáticamente el proceso del servidor MCP
> 2. El servidor le presenta su catálogo de Tools, Resources y Prompts
> 3. Ya puedes pedirle a Claude: *"Lee el archivo README.md de mi proyecto"* y lo hará

---

## 💻 Conexión desde un IDE (VS Code / Cursor)

Los editores de código con IA integrada (VS Code con Copilot, Cursor, Windsurf) soportan MCP para dar a sus agentes acceso a herramientas externas.

### Paso a Paso en VS Code

1. Abre la **Paleta de Comandos** (`Ctrl + Shift + P`)
2. Escribe `MCP: Add Server` y selecciónalo
3. Elige el tipo de transporte: `STDIO` (local) o `HTTP` (remoto)
4. VS Code genera automáticamente el archivo de configuración

### Archivo `.vscode/mcp.json` (a nivel de workspace)

```json
{
  "servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_tu_token_secreto_aqui"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb"
      }
    }
  }
}
```

> [!warning] Buena práctica: Nivel de workspace, no global
> Instala los servidores MCP **a nivel de proyecto** (`.vscode/mcp.json`), NO de forma global. Si los instalas globalmente, el agente de IA cargará **todos** los servidores MCP en cada proyecto, consumiendo tokens innecesarios y ralentizando el descubrimiento de herramientas.

> [!tip] Seguridad de credenciales
> El token de GitHub (`ghp_...`) y la URL de la base de datos se guardan **solo en tu máquina local** dentro del archivo `mcp.json`. El LLM en la nube nunca ve estas credenciales. El [[📂MCP/02 - Arquitectura Host Cliente y Servidor|Servidor MCP local]] las usa para autenticarse con el servicio externo.
> 
> Aun así, **nunca subas `mcp.json` a un repositorio público**. Añádelo a tu `.gitignore`.

---

## 🗣️ Interacción Práctica desde el Chat

Una vez conectado, la interacción es completamente en **lenguaje natural**. No necesitas memorizar comandos ni nombres de funciones.

### Ejemplos de Prompts que Activan Tools MCP

| Lo que escribes | Tool MCP que se activa | Servidor |
| :--- | :--- | :--- |
| *"¿Qué issues abiertos hay en mi repo?"* | `listar_issues()` | GitHub |
| *"Crea una tabla 'productos' con id, nombre y precio"* | `ejecutar_query()` | PostgreSQL |
| *"Lee el archivo package.json de mi proyecto"* | `leer_archivo()` | Filesystem |
| *"Envía un mensaje al canal #dev de Slack diciendo que el deploy está listo"* | `enviar_mensaje()` | Slack |
| *"Muéstrame las estadísticas de mi newsletter de esta semana"* | `obtener_estadisticas()` | Beehiiv |

### Invocación Explícita vs Implícita

| Modo | Cómo funciona | Ejemplo |
| :--- | :--- | :--- |
| **Implícita** (recomendada) | Hablas en lenguaje natural y el LLM decide qué tool usar | *"¿Cuántos suscriptores tengo?"* |
| **Explícita** | Nombras directamente la herramienta o usas un Prompt Template | *"Usa la herramienta obtener_suscriptores del MCP de Beehiiv"* |

> [!example] Flujo real de una sesión
> ```
> 👤 Usuario: "Necesito saber qué PRs están pendientes de revisión en mi repo 
>              y crear un issue resumen con la lista"
> 
> 🧠 LLM (piensa): Necesito 2 tools:
>    1. listar_pull_requests(estado="abierto", repo="mi-repo")
>    2. crear_issue(titulo="PRs pendientes de revisión", cuerpo=<resultado>)
> 
> 🔌 Cliente MCP → Servidor GitHub: listar_pull_requests(...)
> 🐙 GitHub API → 3 PRs encontrados
> 🔌 Cliente MCP → Servidor GitHub: crear_issue(...)
> 🐙 GitHub API → Issue #45 creado
> 
> 🧠 LLM: "He encontrado 3 PRs pendientes y he creado el issue #45 
>          con el resumen. Aquí tienes el enlace: ..."
> ```

---

## 🔄 Descubrimiento Automático de Herramientas

Cuando un servidor MCP se conecta, el primer intercambio JSON-RPC es el **descubrimiento**: el servidor le dice al cliente qué herramientas, recursos y prompts tiene disponibles, incluyendo:

- **Nombre** de la herramienta
- **Descripción** en lenguaje natural (esto es lo que el LLM lee para saber cuándo usarla)
- **Esquema de parámetros** (JSON Schema: qué datos necesita)

> [!warning] La descripción de la Tool es CRÍTICA
> Si la descripción de una Tool es vaga o incorrecta, el LLM no sabrá cuándo invocarla. Ejemplo:
> - ❌ `"descripcion": "Hace cosas con issues"` → El LLM no sabe si crea, lista o borra issues.
> - ✅ `"descripcion": "Crea un nuevo issue en un repositorio de GitHub. Requiere título y cuerpo."` → El LLM sabe exactamente cuándo usarla.

---
→ Volver al índice: [[📂MCP/00 - MOC MCP|🔌 MOC MCP]]
