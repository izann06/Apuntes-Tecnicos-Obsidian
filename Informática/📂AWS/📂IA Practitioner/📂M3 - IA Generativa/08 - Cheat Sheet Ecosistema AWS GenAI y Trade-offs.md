**Tags:** #ecosistema #bedrock #amazon-q #sagemaker #partyrock #trade-offs #ia #m3-genai

> [!quote] El Ecosistema AWS para IA Generativa
> Para el examen, debes ser capaz de mapear rápidamente una necesidad de negocio con el servicio correcto de AWS y entender las compensaciones (Trade-offs) al diseñar arquitecturas.

---

## 🗺️ Cheat Sheet: Ecosistema AWS GenAI

       ┌────────────────────────────────────────────────────────┐
       │               ECOSISTEMA GENERATIVO AWS                │
       └───────────────────────────┬────────────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
  [Amazon Bedrock]            [Amazon Q]          [SageMaker JumpStart]

  - Acceso vía API            - El asistente      - Mayor control técnico

  - Multi-proveedor           - Q Business        - Catálogo de modelos

  - Sin servidores            - Q Developer       - Cómputo administrado

### 1. Amazon Bedrock (La API Central)
Es el servicio principal y estrella para GenAI en AWS. Te da acceso a modelos ultra-potentes de múltiples proveedores (como Anthropic Claude, Meta Llama, Cohere, AI21 o Stable Diffusion) a través de una API unificada.

- **Ventaja:** Es serverless (no gestionas servidores) y pagas únicamente por token consumido.

- **Caso de uso de examen:** "Integrar modelos líderes en una app de empresa sin gestionar infraestructura".

- *Aprende más en: [[📂M4 - Bedrock y Amazon Q/01 - Amazon Bedrock - Qué es y Catálogo de Modelos|Módulo 4: Bedrock]]*

### 2. Amazon Q (Tu Asistente Experto)
Se ofrece en dos "sabores" principales:

- **Amazon Q Business:** Para responder preguntas complejas basándose en documentos y bases de datos privadas de tu propia organización (hace el RAG de forma automática).

- **Amazon Q Developer:** Para asistir a programadores con generación de código, depuración y soporte técnico directo en la consola de AWS o IDE.

- *Aprende más en: [[📂M4 - Bedrock y Amazon Q/05 - Amazon Q (Developer, Business, QuickSight)|Módulo 4: Amazon Q]]*

### 3. Amazon SageMaker JumpStart (Control Absoluto)
Un catálogo masivo de modelos de código abierto y comerciales para desarrolladores de Machine Learning que requieren un **control técnico total**.

- **Ventaja:** Te permite descargar el modelo, entrenarlo con tus propios datos (Fine-tuning profundo) y desplegarlo en tu propia infraestructura (instancias EC2 que tú controlas).

- **Caso de uso de examen:** "El equipo de Data Science necesita control absoluto sobre la infraestructura, hiperparámetros y el despliegue del modelo base".

### 4. Party Rock (Prototipado rápido y visual)
Un entorno interactivo de juegos (playground) impulsado por Amazon Bedrock.

- **Ventaja:** Sirve para crear prototipos rápidos de aplicaciones de IA de forma visual y **sin escribir una sola línea de código** (no-code). Ideal para aprender o para equipos de negocio.

---

## ⚖️ Trade-offs (Compensaciones Arquitectónicas)

Un Arquitecto AWS siempre tiene que equilibrar factores que compiten entre sí. En GenAI, los trade-offs más evaluados son:

### 1. Rendimiento / Capacidad de respuesta vs. Costo
Modelos con menor latencia y menor tamaño (ej. Claude Haiku) son mucho más rápidos y económicos, pero fallan en razonamiento complejo. Los modelos enormes (ej. Claude Opus) resuelven lógica profunda, pero consumen más tokens y son más lentos.

### 2. Disponibilidad Regional (Residencia de Datos)
No todos los modelos de Bedrock están disponibles en todas las regiones geográficas de AWS. 

- **El Trade-off:** Si las leyes de tu país te obligan a guardar los datos localmente (residencia de datos), quizás no puedas usar el último y más potente modelo si aún no ha sido desplegado en tu región local.

### 3. Rendimiento Aprovisionado vs. Bajo Demanda en Bedrock

- **Bajo Demanda (On-Demand):** Pagas exactamente por cada token consumido. Ideal para tráfico impredecible o bajo volumen. Es más caro por token, pero no hay compromiso mensual.

- **Rendimiento Aprovisionado (Provisioned Throughput):** Reservas y pagas por una capacidad dedicada de hardware mensualmente (un coste fijo alto). Ideal para empresas con volumen enorme y constante. Garantiza latencias predecibles.

### 4. Modelos Personalizados (Fine-tuning) vs. RAG

- **El Trade-off:** Si necesitas inyectar conocimiento nuevo, usar RAG (Knowledge Bases for Bedrock) es rápido y barato. Hacer un *Fine-tuning* para el mismo propósito es un error arquitectónico porque es caro, lento de actualizar y el modelo puede alucinar con los datos privados (memorización imperfecta).

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
