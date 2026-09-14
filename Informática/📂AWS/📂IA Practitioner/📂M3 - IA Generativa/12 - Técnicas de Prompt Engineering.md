**Tags:** #prompt-engineering #few-shot #ia #m3-genai
#m3-genai

> [!quote] Concepto fundamental
> El **Prompt Engineering** es el arte y la ciencia de dar instrucciones precisas a un modelo fundacional para obtener el resultado exacto deseado. Es la forma más barata y rápida de "programar" o ajustar el comportamiento de un LLM sin necesidad de reentrenarlo.

---

## 🎨 Técnicas Avanzadas de Prompt Engineering

En el examen AIF-C01 se evalúa el conocimiento de diferentes estrategias para controlar las salidas del modelo. Aquí están las más importantes:

### 1. Ajuste del Prompt (Prompt Tuning / Shaping)
- **Definición:** Controlar el tono, longitud, y formato de marca de la respuesta modificando directamente las instrucciones.
- **Caso de Uso:** Si un modelo responde de forma muy técnica a clientes inexpertos, en lugar de reentrenar al modelo, añades al prompt: *"Responde con un tono amable, usando vocabulario sencillo y limita tu respuesta a 3 párrafos"*.
- **Ventaja:** Cero coste adicional de infraestructura, resultados inmediatos.

### 2. Zero-Shot Prompting
- **Definición:** Pedir al modelo que realice una tarea sin darle ningún ejemplo previo. Confías enteramente en su entrenamiento previo.
- **Ejemplo:** *"Clasifica el siguiente texto como Positivo o Negativo: 'El servicio fue excelente'."*

### 3. Few-Shot Prompting
- **Definición:** Incluir **pares de ejemplos** (mensaje de entrada + respuesta correcta/intención) dentro del propio prompt para enseñar al modelo el patrón exacto que quieres.
- **Por qué funciona:** Los LLMs son excelentes "imitadores de patrones". Al ver 2 o 3 ejemplos, replican el formato a la perfección.
- **Ejemplo en el prompt:**
  ```text
  Convierte la fecha a formato ISO:
  Entrada: "5 de Mayo de 2023" -> Salida: "2023-05-05"
  Entrada: "14 de Febrero de 2021" -> Salida: "2021-02-14"
  Entrada: "1 de Enero de 2024" -> Salida:
  ```

### 4. Rol en el Contexto (Role-Prompting)
- **Definición:** Asignar un rol específico o *persona* al modelo al principio del prompt. Esto ayuda a adaptar el estilo, vocabulario y nivel de detalle según el perfil o edad del usuario.
- **Caso de Uso:** Adaptación según edad/perfil. *"Actúa como un profesor de primaria. Explica cómo funciona la fotosíntesis a un niño de 8 años."* vs *"Actúa como un biólogo molecular y explica la fotosíntesis."*

### 5. Chain of Thought (Cadena de Pensamiento)
- **Definición:** Pedirle al modelo que explique su razonamiento "paso a paso" antes de dar la respuesta final.
- **Ventaja:** Reduce drásticamente los errores en problemas matemáticos o lógicos, ya que obliga al modelo a "pensar" y calcular cada paso.
- **Ejemplo:** *"Resuelve este problema matemático y piensa paso a paso antes de dar la respuesta."*

---

> [!brain] Comparativa: Prompt Engineering vs Fine-Tuning
> Si en el examen te preguntan cómo cambiar el formato de salida de un LLM o enseñarle un tono específico de marca para 5 casos de uso de marketing: **Empieza siempre por Few-Shot Prompting o ajustes al Prompt**. El *Fine-Tuning* solo se recomienda cuando el Prompt Engineering ya no es suficiente, debido a su alto coste y complejidad.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
