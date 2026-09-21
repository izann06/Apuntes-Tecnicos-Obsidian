#github #gh-foundations #modulo-5 #markdown #search #busqueda

> [!info] Navegación
> ◀ [[05 - Branch Protection e InnerSource]] · ▶ [[01 - GitHub Projects y Visualización]]

---

# 06 — Markdown y Búsqueda Avanzada

> **Resumen ejecutivo:**
> 1. GitHub utiliza **GFM (GitHub Flavored Markdown)**, que extiende la sintaxis tradicional (tablas, alertas, checklists).
> 2. La barra de búsqueda soporta **filtros avanzados** (`user:`, `repo:`, `extension:`, `path:`).
> 3. Encontrar y documentar información de forma precisa es clave para colaborar en repositorios grandes.

---

## 1. GitHub Flavored Markdown (GFM)

GitHub utiliza una versión enriquecida de Markdown que permite dar formato a `README.md`, issues, PRs y comentarios.

### Sintaxis Básica y Extendida

| Elemento | Sintaxis | Ejemplo de Salida |
| :--- | :--- | :--- |
| **Negrita** | `**texto**` | **texto** |
| **Cursiva** | `*texto*` | *texto* |
| **Tachado** | `~~texto~~` | ~~texto~~ |
| **Código inline** | `` `var x = 1` `` | `var x = 1` |
| **Bloque de código** | ` ```javascript ` | (Con resaltado de sintaxis) |
| **Listas de tareas** | `- [ ] Tarea 1`<br>`- [x] Tarea 2` | 🔲 Tarea 1<br>✅ Tarea 2 (interactivo) |
| **Menciones** | `@usuario` | Notifica al usuario |
| **Referencias** | `#123` | Enlaza al issue o PR #123 automáticamente |
| **Emojis** | `:rocket:` | 🚀 |

### Alertas (Callouts)

GitHub introdujo recientemente alertas nativas con colores e iconos:

```markdown
> [!NOTE]
> Información útil que los usuarios deben saber, incluso leyendo por encima.

> [!WARNING]
> Contenido urgente o crítico que exige la atención inmediata del usuario.
```

---

## 2. Búsqueda Avanzada en GitHub

La barra de búsqueda global (arriba a la izquierda, atajo `/`) no solo busca palabras clave, sino que admite modificadores muy potentes.

### Filtros de Búsqueda Clave

| Filtro | Ejemplo | ¿Qué hace? |
| :--- | :--- | :--- |
| `user:` / `org:` | `org:github` | Limita la búsqueda a repositorios de esa organización |
| `repo:` | `repo:izanm/proyecto` | Limita la búsqueda a un repositorio específico |
| `path:` | `path:/src/app` | Busca solo dentro de una carpeta concreta |
| `extension:` | `extension:js` | Busca solo en archivos de esa extensión |
| `filename:` | `filename:package.json` | Busca un archivo con ese nombre exacto |
| `author:` | `author:izanm` | Busca commits o código escrito por ese autor |
| `is:` | `is:issue is:open` | Busca issues que están abiertos |

### Ejemplos Combinados de Examen

**"Buscar la palabra 'password' en todos los archivos `.env` de mi organización:"**
`org:mi-empresa password extension:env`

**"Encontrar todos los issues abiertos en los que me han mencionado:"**
`is:issue is:open mentions:@izanm`

**"Buscar funciones de React en archivos `.jsx` dentro de la carpeta `/components`:"**
`repo:mi-empresa/frontend path:/components extension:jsx function`

> [!TIP] Exam Tip — Búsqueda
> El examen puede presentarte un escenario (ej. "quieres buscar un error de log en archivos de Python"). La respuesta correcta será el filtro adecuado: `error extension:py`. Memoriza especialmente `extension:`, `path:` y `repo:`.
