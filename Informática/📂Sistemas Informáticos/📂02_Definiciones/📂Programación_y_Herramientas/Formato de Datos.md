# XML 

- **Qué es:** lenguaje de marcado para datos jerárquicos, muy estructurado.
 
- **Uso típico:** configuraciones complejas, sistemas empresariales, documentos (por ejemplo, archivos `.docx` usan XML internamente).
 

Ejemplo:

`<persona> 
	`<nombre>Izan</nombre> 
	`<edad>21</edad> 
`</persona>`

---

# JSON

- **Qué es:** formato de texto ligero para intercambio de datos (muy usado en APIs REST). Más simple y menos verboso que XML.
 
- **Ejemplo:**
 

`{ 
	`"nombre": "Izan", 
	`"edad": 21 
`}`

- **Uso típico:** respuestas de APIs, configuración, intercambio frontend-backend.
 

---

# BSON 

- **Qué es:** Binary JSON — JSON en forma binaria, con tipos adicionales (fechas, binarios, ObjectId).
 
- **Uso típico:** **MongoDB** lo usa internamente.
 
- **Ventaja:** más rápido y con tipos ricos. **Inconveniente:** no legible sin herramientas.
 

---

# GSON 

- **GSON** no es un formato: es **una librería de Google para Java/Kotlin** que convierte objetos a JSON y viceversa (serialización/deserialización).
 
- **Uso típico:** en Android y servicios Java para manejar JSON fácilmente.
 

Ejemplo (Kotlin):

`val usuario = Usuario("Izan", 21) 
`val json = Gson().toJson(usuario)`

---

# TOML 

- **Qué es:** formato de texto para **configuración**, diseñado para ser simple y legible.
 
- **Uso típico:** `pyproject.toml` (Python), `Cargo.toml` (Rust).
 

Ejemplo:

`[servidor] 
`puerto = 8080`

---

# MessagePack 

- **Qué es:** formato binario que representa estructuras similares a JSON pero más compactas.
 
- **Uso típico:** cuando necesitas alta velocidad y poco ancho de banda (IoT, microservicios de alto rendimiento).
 

---

# YAML

- **Qué es:** formato de texto legible, con indentación, usado para configuraciones (Docker Compose, Kubernetes manifestos).
 
- **Ejemplo:**
 

`persona:
	`Nombre: Izan
	`edad: 21`

- **Punto importante:** muy legible, pero la indentación puede provocar errores si no se tiene cuidado.
 

---

# CSV 

- **Qué es:** valores separados por comas; ideal para datos tabulares (hojas de cálculo).
 
- **Ejemplo:**
 

`nombre,edad 
`Izan,21 

- **Uso típico:** exportar/importar hojas de cálculo, cargas masivas simples.



# 🧭 **Resumen Comparativo — Cuándo usar cada uno**

| Formato / Librería | Tipo | Legible | Uso principal | Ejemplo real |
| ------------------ | ------------------------------ | ------- | ----------------------------------------------------- | ---------------------------- |
| **XML** | Texto estructurado | ✅ Sí | Intercambio formal de datos, configuraciones antiguas | Android, Office, SOAP |
| **JSON** | Texto estructurado | ✅ Sí | APIs REST, apps web, comunicación frontend-backend | Casi todas las APIs modernas |
| **BSON** | Binario | ❌ No | Almacenamiento eficiente | MongoDB |
| **GSON** | Librería (Java/Kotlin) | ✅ Sí | Convertir objetos ↔ JSON | Android, Retrofit |
| **TOML** | Texto (configuración) | ✅ Sí | Configuraciones legibles | Python, Rust |
| **YAML** | Texto (configuración avanzada) | ✅ Sí | DevOps, Docker, Kubernetes | docker-compose.yml |
| **MessagePack** | Binario | ❌ No | Comunicación rápida y comprimida | IoT, microservicios |
| **CSV** | Texto plano (tablas) | ✅ Sí | Datos tabulares simples | Excel, bases de datos |

---

## 💡 **Resumen final — cómo recordarlos fácilmente**

- 🧩 **XML** → “Etiquetas” — jerarquías complejas, usado en sistemas antiguos y documentos.
 
- ⚙️ **JSON** → “Ligero y universal” — APIs y datos en la web moderna.
 
- 💾 **BSON** → “JSON binario” — base de datos MongoDB.
 
- 🧮 **GSON** → “Librería de Java para JSON”.
 
- 🧰 **TOML** → “Configuración simple y clara”.
 
- 🧾 **YAML** → “Configuración humana” (Docker, Kubernetes).
 
- ⚡ **MessagePack** → “JSON comprimido binario, rápido y pequeño”.
 
- 📊 **CSV** → “Tablas de texto” (Excel, datos simples)