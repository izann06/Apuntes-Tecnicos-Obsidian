#ia #opencode #programacion #cli #herramientas

> [!abstract] 🤖 ¿Qué es OpenCode?
> **OpenCode** (https://opencode.ai) es un asistente de programación impulsado por Inteligencia Artificial que se ejecuta directamente en la terminal (CLI). 
> A diferencia de los asistentes integrados en editores (como GitHub Copilot o el chat de VS Code), OpenCode funciona como un agente independiente en tu consola, capaz de leer tu código, entender el contexto del proyecto y aplicar los cambios (diffs) directamente en tus archivos.

---

## 💡 ¿Para qué se usa y Casos Reales?

OpenCode está diseñado para el **desarrollo de software asistido por IA (Agentic Coding)** sin tener que salir de la terminal.

**Casos de uso reales:**

- **Refactorización masiva:** Pedirle a la IA que cambie la estructura de varios archivos a la vez sin tener que ir copiando y pegando en el IDE.
  
- **Creación de proyectos desde cero:** Generar el esqueleto, la configuración y el código base iterando con comandos rápidos.
  
- **Depuración (Debugging) avanzado:** Entregarle un error crudo de la terminal para que analice el código fuente y lo arregle.
  
- **Generación de Tests:** Pedirle que lea un archivo y genere automáticamente las pruebas unitarias correspondientes.

**Diferencias principales con otros asistentes:**

1. **Independencia del IDE:** Funciona en cualquier terminal (Bash, ZSH, Warp), no requiere VS Code, IntelliJ ni Cursor.
   
2. **Agnóstico del proveedor:** Te permite conectar tu propia API Key del proveedor que prefieras (OpenAI, Anthropic, Google) en lugar de atarte a un único modelo de pago.
   
3. **Modo Shell y Diferencias:** Puede ejecutar comandos de terminal por ti y mostrarte los `diffs` (diferencias de código exactas) antes de confirmarlos.

---

## 🛠️ Instalación (Visión General)

Al ser una herramienta de línea de comandos, normalmente se instala utilizando un gestor de paquetes.

```bash
paru -S warp-terminal-bin
```

*(Asegúrate de consultar la documentación oficial en `opencode.ai` para obtener el comando exacto de instalación de la última versión).*

---

## ⌨️ Comandos Oficiales de OpenCode

OpenCode se controla mediante comandos que empiezan por `/` (barra diagonal) o caracteres especiales. Según su especificación, esta es la lista de herramientas a tu disposición:

### 1. Conexión y Modelos

- `/connect` : **Conectar un proveedor** (Ej: configurar tu API Key de Anthropic u OpenAI para que OpenCode pueda comunicarse con los servidores de IA).
- `/models` : **Seleccionar un modelo** (Cambiar entre Claude 3.5 Sonnet, GPT-4o, etc. dependiendo de la tarea).
- `/variants` : **Seleccionar el esfuerzo del modelo** (Configurar si quieres respuestas rápidas/ligeras o análisis profundos).

### 2. Gestión de Sesiones

- `/new` : **Nueva sesión** (Limpia el contexto de la memoria y empieza de cero para no confundir al modelo con temas pasados).
- `/sessions` : **Navegar entre sesiones** (Ver tu historial de conversaciones anteriores y retomarlas donde las dejaste).
- `/compact` : **Compacta la sesión** (Reduce el historial de chat para ahorrar tokens de contexto y abaratar costes de la API).
- `/exit` : **Salir** (Cierra la herramienta de forma segura).

### 3. Interacción y Código

- `/undo` : **Deshace un mensaje** (Si la IA se ha equivocado o alucinó una respuesta mala, echas hacia atrás la conversación).
- `/redo` : **Rehace un mensaje** (Vuelve a aplicar un mensaje que habías deshecho).
- `/diff` : **Muestra las diferencias** (Visualiza en rojo y verde qué líneas de código se van a añadir o borrar antes de aplicar los cambios a tus archivos).

### 4. Accesos Directos (Shortcuts)

- `@` : **Referencias** (Usa este símbolo para mencionar archivos específicos de tu proyecto y obligar a la IA a que los lea. Ej: `@src/main.py`).
- `!` : **Modo Shell** (Ejecuta comandos directamente en tu terminal de Linux desde dentro de OpenCode. Ej: `!npm run test`).
