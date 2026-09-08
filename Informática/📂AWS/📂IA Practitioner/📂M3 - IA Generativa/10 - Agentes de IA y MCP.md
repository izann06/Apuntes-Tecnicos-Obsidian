**Tags:** #agentes #mcp #apis #bedrock #ia #m3-genai

> [!quote] El Siguiente Nivel Evolutivo
> Hasta ahora, hemos visto modelos "pasivos" (RAG, Chatbots). Tú preguntas, ellos responden. Un **Agente** es el salto a la IA "activa": modelos capaces de tomar el control, planificar acciones y ejecutar tareas en el mundo real.

---

## 🤖 ¿Qué es un Agente de IA?

En el contexto de AWS (Bedrock Agents), un Agente es una arquitectura donde el LLM actúa como el **cerebro de un operario**. En lugar de solo generar texto, el Agente puede:

1. **Planificar:** Desglosar una petición compleja del usuario en pasos lógicos.

2. **Decidir:** Usar el razonamiento (Chain-of-Thought) para decidir qué herramienta necesita usar en cada paso.

3. **Llamar Herramientas (Action Groups):** Ejecutar código, llamar a APIs externas (AWS Lambda) o consultar bases de datos.

4. **Iterar:** Observar el resultado de la herramienta y decidir cuál es el siguiente paso hasta completar el objetivo.

> [!abstract] Analogía del Agente
> - **LLM normal:** Es un consejero experto atado a una silla. Le preguntas cómo hacer una pizza y te dicta la receta paso a paso.
> - **Agente de IA:** Es un chef en una cocina. Le dices "hazme una pizza", y él planifica la receta, **abre la nevera (llama a una API)**, saca los ingredientes, usa el horno y te entrega la pizza terminada.

### Ejemplo de Flujo de un Agente (Reserva de Vuelos):

1. **Usuario:** *"Cancela mi vuelo a Madrid y reserva uno para mañana a Barcelona."*

2. **Agente (Planificación):** Necesito 1) Buscar el vuelo de Madrid. 2) Cancelarlo. 3) Buscar vuelos a Barcelona para mañana. 4) Reservar.

3. **Agente (Acción):** Llama a la API de la aerolínea `obtenerVuelosUsuario(id)`.

4. **Agente (Acción):** Llama a `cancelarReserva(idVuelo)`.

5. **Agente (Acción):** Llama a `buscarVuelo(destino="BCN", fecha="mañana")`.

6. **Agente (Acción):** Llama a `reservarVuelo(...)` y le informa al usuario que todo está listo.

---

## 🔌 MCP (Model Context Protocol)

El gran problema de los Agentes hasta ahora era que, si querías que tu Agente leyera datos de GitHub, Google Drive, Slack o bases de datos locales, tenías que programar integraciones (APIs) complejas y personalizadas para cada una.

El **MCP (Model Context Protocol)** es un nuevo estándar abierto (creado originalmente por Anthropic, pero adoptado por toda la industria tecnológica) que resuelve este problema de raíz.

> [!abstract] La Analogía del Restaurante y el Camarero
> Imagina que el LLM es un cliente sentado en la mesa de un restaurante.
> 
> - **Sin MCP (Peligro):** Para que el cliente coma, le das las llaves de la cocina y de la despensa para que él mismo entre y cocine. Puede quemar la cocina, robar la receta secreta o manipular el gas.
> 
>
> - **Con MCP (Seguridad y Orden):** El cliente **nunca entra a la cocina**. En la mesa tiene una carta fija (el catálogo de herramientas de MCP). El cliente le dice al **Camarero (Servidor MCP)**: *"Por favor, tráeme el plato número 3"*. El camarero va a la cocina privada, valida la orden, usa sus propios permisos, coge únicamente ese plato y se lo sirve al cliente en la mesa.

> [!brain] La Analogía Tecnológica: El USB-C de la Inteligencia Artificial
> Antes, cada marca de móvil tenía su propio cargador propietario (Nokia, Sony Ericsson, iPhone de 30 pines).
> 
> Si cambiabas de móvil, tenías que tirar todos tus cables a la basura.
> 
> Luego llegó el **USB-C**: un estándar universal donde cualquier cable sirve para cualquier dispositivo.
> 
> **MCP es el USB-C de los Agentes de IA.** Permite que cualquier modelo (Claude, GPT, Llama, Amazon Titan) se conecte a cualquier herramienta o base de datos sin escribir código a medida.

---

### 🏗️ Arquitectura de MCP: Las 3 Piezas Clave

MCP funciona bajo una arquitectura cliente-servidor muy bien delimitada:

1. **El Host (La Aplicación):** Es el entorno donde trabaja el usuario (por ejemplo: el IDE, Claude Desktop o una consola en AWS Bedrock). Aquí es donde reside el LLM.

2. **El Cliente MCP:** Es el componente dentro del Host que se encarga de hablar el protocolo estándar.

3. **El Servidor MCP:** Es un programa independiente y ligero que se ejecuta en tu máquina local o en tu red privada (VPC). Este servidor es el **único** que tiene acceso real a la herramienta (tus archivos locales, tu base de datos PostgreSQL, tu Slack o tu cuenta de GitHub).

---

### 🛡️ La Gran Pregunta: ¿Por qué MCP aporta Seguridad si a simple vista parece todo lo contrario?

A primera vista, tu intuición es totalmente lógica: *"¿Cómo va a ser seguro darle a una IA acceso a mis archivos o a mi base de datos? ¡Darle herramientas a un modelo parece un peligro enorme!"*

El secreto está en **contra qué lo estás comparando**.

Antes de MCP, para que una IA pudiera interactuar con herramientas o datos privados, se utilizaban métodos muy inseguros:

- Pegar contraseñas y claves API maestras dentro del propio prompt del sistema para que el modelo las utilizara.

- Subir volcados enteros de bases de datos confidenciales a nubes de terceros.

- Darle al modelo acceso a una consola bash abierta para que ejecutara comandos arbitrarios sin supervisión.

MCP nació precisamente para **blindar y aislar** ese proceso mediante 5 pilares de seguridad:

#### 1. Aislamiento Absoluto de Credenciales (Zero Knowledge)

El modelo de IA **nunca ve ni toca tus contraseñas, tokens de API ni cadenas de conexión**.

Las credenciales sensibles se guardan exclusivamente en el Servidor MCP (en tu entorno local o servidor seguro).

El modelo solo ve una firma abstracta: `buscar_factura(id_cliente)`.

Cuando el modelo quiere usarla, le solicita al Servidor MCP que la ejecute; el servidor valida la llamada, usa sus credenciales locales y solo le devuelve al modelo los datos resultantes.

Si el modelo sufre una fuga de información o un ataque de Prompt Injection, tus contraseñas maestras jamás se filtrarán porque nunca salieron de tu máquina.

#### 2. Principio de Mínimo Privilegio (Catálogo Cerrado)

El modelo no tiene acceso libre al sistema operativo ni a tu base de datos.

Solo puede ejecutar las funciones específicas que tú hayas expuesto en el Servidor MCP.

Por ejemplo: puedes configurar un servidor MCP que solo contenga la función `consultar_saldo()` y **ninguna** función para `transferir_fondos()`.

El modelo físicamente no puede realizar ninguna acción que no esté en esa lista blanca (*whitelist*), por mucho que un atacante intente convencerlo en el chat.

#### 3. El Guardián Humano (Human-in-the-Loop)

El estándar MCP permite implementar puertas de enlace y aprobación humana obligatoria.

Cada vez que el modelo intenta ejecutar una acción que modifica datos, escribe en el disco o ejecuta un comando sensible, la aplicación puede detenerse y solicitar tu visto bueno:

> *"El agente quiere ejecutar: `eliminar_archivo('config.json')`. ¿Deseas autorizar esta acción? [Aprobar / Denegar]"*

Tú mantienes la última palabra en todo momento.

#### 4. Tipado Estricto contra Inyecciones (JSON Schema)

Todas las herramientas en MCP se definen mediante esquemas JSON fuertemente tipados.

Si una herramienta espera un parámetro de tipo entero `id: 42`, el protocolo rechaza de inmediato cualquier intento de inyectar código malicioso o sentencias SQL destructivas (`DROP TABLE users;`).

Los datos se validan y sanean en la frontera antes de que lleguen a interactuar con tus sistemas internos.

#### 5. Soberanía y Privacidad del Dato (Tus datos no salen de tu red)

El Servidor MCP se ejecuta dentro de tu perímetro (tu ordenador local o tu nube privada VPC).

No necesitas subir gigabytes de información confidencial a los servidores de OpenAI, Anthropic o AWS.

El servidor MCP ejecuta la consulta en local, extrae únicamente la respuesta necesaria y envía a la IA solo ese pequeño fragmento de texto para que formule su respuesta.

---

### 🚀 Otros Beneficios Clave de MCP

1. **Interoperabilidad Total:** Si hoy utilizas Claude en AWS Bedrock conectado a tus herramientas mediante MCP, y mañana decides cambiar a Amazon Titan, GPT o Llama 3, **no tienes que reprogramar ninguna integración**. Todas tus herramientas seguirán funcionando al instante.

2. **Modularidad (Plugins Desacoplados):** Conectar una nueva fuente de datos a tu IA es tan fácil como añadir una línea a un archivo de configuración (`mcp_config.json`). Puedes activar, pausar o desinstalar servidores MCP como si fueran extensiones del navegador.

3. **Ecosistema Abierto y Reutilizable:** No necesitas reinventar la rueda. La comunidad y las grandes empresas ya publican servidores MCP oficiales y auditados para GitHub, Docker, Google Drive, PostgreSQL, Slack, terminales de comandos y cientos de servicios más.

---

### ⚙️ En la Práctica: ¿Cómo se Usa y se Configura MCP?

Una duda muy habitual cuando se estudia MCP es: *«¿Tengo que programar o configurar algo para utilizarlo?»*.

La respuesta depende de lo que quieras hacer:

#### 1. En el Uso Cotidiano (Herramientas por Defecto): Cero Configuración

Para las tareas habituales dentro de un asistente o entorno de desarrollo (como leer archivos de tu proyecto, editarlos o ejecutar comandos locales), **no tienes que configurar absolutamente nada**.

La aplicación ya viene de fábrica con esas capacidades integradas y listas para funcionar desde el primer segundo.

#### 2. Para Conectar Servicios Externos (Superpoderes Nuevos): Un Archivo JSON

Solo tienes que configurar algo cuando deseas conectar una **aplicación o servicio externo** que no viene incluido por defecto (por ejemplo: tu cuenta privada de **GitHub**, tu gestor de tareas en **Jira/Notion**, o tu base de datos **PostgreSQL**).

Lo mejor de este sistema es que **no tienes que picar ni una sola línea de código**.

La configuración consiste únicamente en pegar un bloque de texto descriptivo en un archivo de configuración (normalmente llamado `mcp_config.json` o a través de los menús gráficos de la aplicación).

#### Ejemplo Real: Conectar un Servidor MCP de GitHub

Si quieres que tu agente pueda interactuar directamente con tus repositorios de GitHub, solo tienes que añadir estas líneas:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_tu_token_secreto_aqui"
      }
    }
  }
}
```

¿Qué ocurre entre bastidores en cuanto guardas ese archivo?

1. **Arranque Automático:** El entorno ejecuta el paquete oficial del servidor MCP de GitHub.

2. **Catálogo Inmediato:** El servidor MCP le presenta a la IA su lista de herramientas disponibles: `crear_issue()`, `buscar_codigo()`, `abrir_pull_request()`.

3. **Interacción Natural:** A partir de ese instante, ya puedes pedirle en el chat: *«Revisa los issues abiertos en mi repositorio y dime cuáles son urgentes»*.

4. **Seguridad Preservada:** Tu token de acceso (`GITHUB_PERSONAL_ACCESS_TOKEN`) se queda guardado localmente en tu máquina; el modelo de IA en la nube jamás ve tu contraseña.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
