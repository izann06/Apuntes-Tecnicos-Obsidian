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

El **MCP (Model Context Protocol)** es un nuevo estándar abierto (creado originalmente por Anthropic, pero adoptado por la industria) que resuelve este problema de raíz.

> [!brain] MCP = El estándar USB para la Inteligencia Artificial
> Imagina cuando antes cada teléfono móvil tenía un cargador distinto (Nokia, Sony, Motorola). Era un caos. Luego llegó el estándar USB-C y todos los teléfonos empezaron a usar el mismo cable.
> 
> **MCP es el USB-C de la IA.** Es un protocolo universal. Si una herramienta (ej. GitHub) soporta MCP, **cualquier** Agente o modelo de IA que soporte MCP podrá conectarse a ella instantáneamente, sin que los programadores tengan que escribir código de integración específico.

### Beneficios del MCP en la Empresa
1. **Seguridad Total:** Las integraciones ocurren a nivel local/servidor bajo tu control, sin exponer tus credenciales directamente al modelo de la nube.
2. **Velocidad de Desarrollo:** No hay que reinventar la rueda conectando APIs.
3. **Interoperabilidad:** Puedes cambiar de Claude a Llama o a Amazon Titan, y todas las herramientas seguirán conectadas porque usan el mismo estándar MCP.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
