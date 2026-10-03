**Tags:** #mcp #python #sdk #fastmcp #servidor #desarrollo

> [!info] Navegación
> ◀ Anterior: [[📂MCP/05 - Casos de Uso Reales y Proyecto Práctico|Casos de Uso]] | Siguiente ▶: [[📂MCP/07 - Recursos Enlaces y Comunidad MCP|Recursos]]

---

# 06 — Cómo Crear un Servidor MCP en Python

> [!quote] Concepto Clave
> No necesitas depender de servidores MCP de terceros. Si tienes una API interna, una base de datos propia o una herramienta personalizada, puedes crear **tu propio servidor MCP** en pocas líneas de código usando los SDKs oficiales.

---

## 📦 SDKs Oficiales Disponibles

MCP tiene SDKs oficiales para los lenguajes más populares:

| Lenguaje | SDK | Estado |
| :--- | :--- | :--- |
| **Python** | `pip install mcp` | ✅ Estable (el más usado) |
| **TypeScript** | `npm install @modelcontextprotocol/sdk` | ✅ Estable |
| **Java** | Maven/Gradle | ✅ Estable |
| **C#** | NuGet | ✅ Estable |
| **Kotlin** | Maven/Gradle | ✅ Estable |
| **Rust** | Cargo | 🧪 Experimental |

> [!tip] ¿Cuál elegir?
> Para prototipos rápidos y aprendizaje → **Python** (es el que veremos aquí).
> Para producción en apps web → **TypeScript**.
> Para apps empresariales → **Java / C#** (conectar con los apuntes de [[📂Programación/📂Java|Java]] o [[📂Programación/📂CSharp|C#]]).

---

## 🐍 Paso a Paso: Servidor MCP Mínimo en Python

### 1. Crear y activar el entorno virtual

```bash
# Crear el directorio del proyecto
mkdir mi-servidor-mcp && cd mi-servidor-mcp

# Crear el entorno virtual de Python
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
```

### 2. Instalar el SDK de MCP

```bash
pip install mcp
```

### 3. Escribir el servidor

Crea un archivo `server.py`:

```python
from mcp.server.fastmcp import FastMCP

# Crear la instancia del servidor con un nombre descriptivo
mcp = FastMCP("Mi Servidor de Cálculos")


@mcp.tool()
def sumar(a: float, b: float) -> str:
    """Suma dos números y devuelve el resultado.
    
    Usa esta herramienta cuando el usuario quiera sumar, 
    calcular totales o hacer operaciones aritméticas básicas.
    """
    resultado = a + b
    return f"El resultado de {a} + {b} = {resultado}"


@mcp.tool()
def calcular_iva(precio: float, porcentaje_iva: float = 21.0) -> str:
    """Calcula el precio final con IVA incluido.
    
    Usa esta herramienta cuando el usuario pregunte por precios 
    con impuestos, IVA o necesite calcular el coste total de un 
    producto o servicio.
    
    Args:
        precio: El precio base sin IVA
        porcentaje_iva: El porcentaje de IVA a aplicar (por defecto 21%)
    """
    iva = precio * (porcentaje_iva / 100)
    total = precio + iva
    return f"Precio base: {precio}€ | IVA ({porcentaje_iva}%): {iva:.2f}€ | Total: {total:.2f}€"


@mcp.resource("config://version")
def obtener_version() -> str:
    """Devuelve la versión actual del servidor."""
    return "1.0.0"


if __name__ == "__main__":
    mcp.run()
```

> [!warning] La descripción del docstring es CRÍTICA
> El texto que escribes en el docstring de cada `@mcp.tool()` es lo que el LLM lee para decidir **cuándo** usar esa herramienta. Si la descripción es vaga, el modelo no sabrá cuándo invocarla.
> 
> - ❌ `"""Hace cosas con números"""` → El LLM no sabe si suma, resta, multiplica...
> - ✅ `"""Suma dos números y devuelve el resultado. Usa esta herramienta cuando el usuario quiera sumar..."""` → El LLM sabe exactamente cuándo usarla.

---

## 🔍 Paso 4: Depuración con MCP Inspector

Antes de conectar tu servidor al IDE, puedes probarlo en un **navegador de depuración**:

```bash
# Lanzar el MCP Inspector (herramienta de desarrollo oficial)
npx @modelcontextprotocol/inspector python server.py
```

Esto abre una interfaz web en `http://localhost:5173` donde puedes:
- Ver el catálogo de Tools, Resources y Prompts expuestos
- Ejecutar herramientas manualmente con parámetros de prueba
- Ver las peticiones/respuestas JSON-RPC en tiempo real
- Depurar errores antes de conectar con un LLM real

---

## 🔌 Paso 5: Conectar al IDE

Una vez probado, conecta tu servidor al IDE creando el archivo `.vscode/mcp.json` (o equivalente en Cursor):

```json
{
  "servers": {
    "mi-calculadora": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/ruta/a/mi-servidor-mcp",
      "env": {
        "VIRTUAL_ENV": "/ruta/a/mi-servidor-mcp/venv"
      }
    }
  }
}
```

Ahora puedes escribir en el chat del IDE:

> *"¿Cuánto costaría un producto de 150€ con el IVA incluido?"*

Y el agente ejecutará automáticamente `calcular_iva(precio=150)` y te responderá:

> *"Precio base: 150€ | IVA (21%): 31.50€ | Total: 181.50€"*

---

## 🏗️ Ejemplo Avanzado: Servidor MCP para Tu Base de Datos

```python
import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Servidor BD Productos")

DB_PATH = "productos.db"


@mcp.tool()
def buscar_producto(nombre: str) -> str:
    """Busca un producto en la base de datos por nombre parcial.
    
    Usa esta herramienta cuando el usuario pregunte por un producto,
    quiera saber el precio de algo, o busque información de inventario.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre, precio, stock FROM productos WHERE nombre LIKE ?",
        (f"%{nombre}%",)
    )
    resultados = cursor.fetchall()
    conn.close()
    
    if not resultados:
        return f"No se encontraron productos con el nombre '{nombre}'"
    
    respuesta = "Productos encontrados:\n"
    for nombre, precio, stock in resultados:
        respuesta += f"- {nombre}: {precio}€ (Stock: {stock} uds)\n"
    return respuesta


@mcp.tool()
def productos_bajo_stock(limite: int = 10) -> str:
    """Lista los productos con stock por debajo del límite indicado.
    
    Usa esta herramienta cuando el usuario pregunte por productos 
    que se están agotando, inventario bajo o necesiten reposición.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre, stock FROM productos WHERE stock < ? ORDER BY stock ASC",
        (limite,)
    )
    resultados = cursor.fetchall()
    conn.close()
    
    if not resultados:
        return f"Todos los productos tienen stock >= {limite}"
    
    respuesta = f"⚠️ Productos con stock < {limite}:\n"
    for nombre, stock in resultados:
        respuesta += f"- {nombre}: {stock} unidades\n"
    return respuesta


@mcp.resource("db://productos/esquema")
def esquema_bd() -> str:
    """Devuelve el esquema de la base de datos de productos."""
    return """
    Tabla: productos
    - id (INTEGER, PRIMARY KEY)
    - nombre (TEXT, NOT NULL)
    - precio (REAL, NOT NULL)
    - stock (INTEGER, DEFAULT 0)
    - categoria (TEXT)
    - created_at (TIMESTAMP)
    """


if __name__ == "__main__":
    mcp.run()
```

> [!example] Interacción real con este servidor
> ```
> 👤 "¿Tenemos auriculares en stock?"
> 🧠 → buscar_producto(nombre="auriculares")
> 🤖 "Sí, encontré: Auriculares Bluetooth Pro: 45€ (Stock: 23 uds)"
> 
> 👤 "¿Qué productos necesitan reposición?"
> 🧠 → productos_bajo_stock(limite=5)
> 🤖 "⚠️ Productos con stock < 5:
>      - Cable HDMI 2.1: 2 unidades
>      - Ratón inalámbrico: 3 unidades"
> ```

---

## 📝 Resumen de la Estructura de un Servidor MCP

| Elemento | Decorador | Función |
| :--- | :--- | :--- |
| **Tool** | `@mcp.tool()` | Función que el LLM puede ejecutar (verbo/acción) |
| **Resource** | `@mcp.resource("uri://...")` | Dato de solo lectura que aporta contexto |
| **Prompt** | `@mcp.prompt()` | Plantilla de prompt reutilizable |

```python
# Estructura mínima de un servidor MCP
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Nombre del Servidor")

@mcp.tool()
def mi_herramienta(parametro: str) -> str:
    """Descripción clara de cuándo usar esta herramienta."""
    return f"Resultado: {parametro}"

@mcp.resource("datos://info")
def mi_recurso() -> str:
    """Datos de contexto para el modelo."""
    return "Información relevante..."

if __name__ == "__main__":
    mcp.run()
```

---
→ Volver al índice: [[📂MCP/00 - MOC MCP|🔌 MOC MCP]]
