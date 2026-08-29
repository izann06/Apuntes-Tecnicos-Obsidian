# 06 — Técnicas de Adaptación de Foundation Models

**Tags:** #prompt-engineering #rag #fine-tuning #few-shot #chain-of-thought #ia
 #m3-genai
**Módulo:** [[00 - Índice Módulo 3]] | **Índice:** [[🏠 AWS AIF-C01 — Índice Maestro]]

> [!quote] El reto de la adaptación
> Los Foundation Models son generalistas. Para hacerlos útiles en contextos específicos de negocio, tenemos cuatro técnicas de adaptación con diferentes niveles de esfuerzo, coste y control. Elegir la correcta es una decisión de arquitectura crítica.

---

## 🏆 La Tabla Maestra — Esfuerzo / Coste / Caso de Uso

| Técnica | Esfuerzo | Coste | Tiempo | Modifica pesos | Lo que cambia | Caso de uso principal |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Prompt Engineering** | ⭐ Mínimo | 💰 Muy bajo | Horas | ❌ No | El input | Ajuste inmediato sin datos |
| **RAG** | ⭐⭐ Bajo | 💰💰 Bajo | Días | ❌ No | El contexto del prompt | Conocimiento actualizado/privado |
| **Fine-tuning** | ⭐⭐⭐ Alto | 💰💰💰 Alto | Semanas | ✅ Sí | Los pesos del modelo | Estilo específico, habilidades nuevas |
| **Pre-training from scratch** | ⭐⭐⭐⭐⭐ Extremo | 💰💰💰💰💰 Extremo | Meses | ✅ Todo | El modelo entero | Dominio completamente inédito |

---

## ✍️ Técnica 1: Prompt Engineering

> [!quote] Definición
> El arte de **diseñar los inputs (prompts)** para guiar al modelo hacia la respuesta deseada sin modificar ningún peso del modelo.

**Es siempre la primera técnica a probar.** Si funciona, no necesitas nada más.

---

### 🎯 Zero-shot Prompting

El modelo realiza la tarea **sin ningún ejemplo previo**, basándose únicamente en su conocimiento preentrenado.

```
Prompt:
"Clasifica el sentimiento de la siguiente reseña como Positivo, 
 Negativo o Neutro:

 Reseña: 'El envío llegó 3 días tarde y la caja estaba golpeada.'
 
 Sentimiento:"

Respuesta del modelo: "Negativo"
```

**Cuándo funciona:** Tareas simples y bien definidas que el modelo haya visto durante el preentrenamiento.

---

### 🎯 Few-shot Prompting

Se proporcionan **entre 2 y 5 ejemplos** de pares input→output en el propio prompt para que el modelo aprenda el patrón deseado.

```
Prompt:
"Clasifica el sentimiento:

Reseña: 'La comida estaba deliciosa y el servicio fue excelente.'
Sentimiento: Positivo

Reseña: 'Esperé 45 minutos y el pedido llegó frío y equivocado.'
Sentimiento: Negativo

Reseña: 'El local es amplio y tiene buena ubicación.'
Sentimiento: Neutro

Reseña: 'El precio es razonable pero la calidad podría mejorar.'
Sentimiento:"

Respuesta del modelo: "Neutro"
```

**Por qué funciona mejor que Zero-shot:**

- Los ejemplos **muestran el formato exacto** de respuesta esperado

- Definen implícitamente el **criterio de clasificación** de tu empresa

- El modelo puede aprender patrones muy específicos del dominio

> [!tip] Cuándo usar Few-shot vs Fine-tuning
> Si necesitas **personalizar el comportamiento** del modelo:
>
> - **¿Tienes < 100 ejemplos o no quieres coste de entrenamiento?** → Few-shot
>
> - **¿Tienes > 1.000 ejemplos y quieres consistencia permanente?** → Fine-tuning

---

### 🧠 Chain-of-Thought (CoT) Prompting

Técnica que le pide al modelo que **razone paso a paso** antes de dar la respuesta final. Mejora drásticamente el rendimiento en problemas de razonamiento multi-paso.

```
Prompt SIN Chain-of-Thought:
"Si Juan tiene 15 manzanas, da 1/3 a María y la mitad 
 de lo que queda a Pedro, ¿cuántas le quedan a Juan?"

Respuesta (incorrecta frecuentemente): "5"

---

Prompt CON Chain-of-Thought:
"Resuelve el siguiente problema razonando paso a paso:
 Si Juan tiene 15 manzanas, da 1/3 a María y la mitad 
 de lo que queda a Pedro, ¿cuántas le quedan a Juan?"

Respuesta:
"Paso 1: Juan tiene 15 manzanas.
 Paso 2: Da 1/3 a María → 15 × (1/3) = 5 manzanas para María.
 Le quedan a Juan: 15 - 5 = 10 manzanas.
 Paso 3: Da la mitad de lo que le queda a Pedro → 10 / 2 = 5 para Pedro.
 Le quedan a Juan: 10 - 5 = 5 manzanas.
 Respuesta final: Juan se queda con 5 manzanas."
```

**Por qué funciona:** Fuerza al modelo a "pensar en voz alta", activando capacidades de razonamiento más profundas. Reduce errores en matemáticas, lógica y razonamiento causal.

> [!tip] Variante: Zero-shot CoT
> Simplemente añade al final del prompt: **"Piensa paso a paso:"** o **"Let's think step by step:"**
> Esta variante es sorprendentemente efectiva sin necesidad de ejemplos.

---

## 🔍 Técnica 2: RAG (Retrieval-Augmented Generation)

> [!quote] Definición AWS
> RAG es una técnica que **aumenta el prompt del LLM** con información relevante recuperada en tiempo real de una base de conocimiento externa, sin modificar los pesos del modelo.

### ¿Por Qué RAG en Lugar de Fine-tuning para Conocimiento?

| Criterio | RAG | Fine-tuning |
| :--- | :---: | :---: |
| **Conocimiento actualizable** | ✅ Solo actualizas la KB | ❌ Reentrenamiento necesario |
| **Datos privados/confidenciales** | ✅ Nunca salen de tu infraestructura | ⚠️ Se exponen durante el entrenamiento |
| **Citación de fuentes** | ✅ Puedes mostrar el chunk origen | ❌ No puede citar |
| **Reducción de alucinaciones** | ✅ El modelo se ancla a los datos | ❌ No garantizado |
| **Coste de implementación** | 💰 Medio | 💰💰💰 Alto |

### Flujo RAG Completo

```mermaid
sequenceDiagram
 participant U as 👤 Usuario
 participant O as 🔧 Orquestador
 participant V as 🗃️ Vector DB
 participant E as 🔢 Embedding Model
 participant L as 🧠 LLM

 U->>O: "¿Cuál es nuestra política de devoluciones?"
 O->>E: Convierte pregunta en embedding
 E->>O: Vector de la pregunta
 O->>V: Búsqueda ANN por similitud
 V->>O: Top-3 chunks relevantes del manual
 O->>O: Construye prompt aumentado:<br/>"Usando el siguiente contexto:<br/>[chunk1] [chunk2] [chunk3]<br/>Responde: ¿Cuál es la política...?"
 O->>L: Prompt aumentado
 L->>U: "Según nuestra política vigente,<br/>los clientes tienen 30 días para..."
```

### Cuándo Usar RAG (Regla de Oro)

> [!tip] RAG es la respuesta cuando...
>
> - El modelo necesita saber cosas que ocurrieron **después** de su fecha de corte de entrenamiento
>
> - Necesitas dar respuestas sobre **documentos internos privados** (manuales, políticas, contratos)
>
> - Quieres que el modelo **cite sus fuentes** (grounding)
>
> - Necesitas que el modelo **no invente** respuestas sobre datos factuales específicos
>
> - El conocimiento **cambia frecuentemente** (precios, normativas, inventario)

---

## 🏋️ Técnica 3: Fine-tuning

> [!quote] Definición
> Fine-tuning es el proceso de **continuar el entrenamiento** de un FM preentrenado con un dataset específico y más pequeño, **modificando los pesos del modelo** para especializarlo.

### Lo Que Cambia (y Lo Que No)

```
Foundation Model Original:
[Pesos W1, W2, W3,..., Wn] ← Resultado del pre-training masivo

Después del Fine-tuning con tus datos:
[Pesos W1', W2', W3',..., Wn'] ← Ligeramente modificados para tu dominio
```

**El fine-tuning modifica los pesos**, a diferencia de RAG y Prompt Engineering que solo cambian el input.

### Tipos de Fine-tuning

| Tipo | Descripción | Cuándo usarlo |
| :--- | :--- | :--- |
| **SFT (Supervised Fine-tuning)** | Entrenas con pares (prompt, respuesta ideal) | Tarea muy específica con ejemplos etiquetados |
| **RLHF** | Alinear con preferencias humanas via recompensa | Mejorar utilidad y seguridad del modelo |
| **LoRA / QLoRA (PEFT)** | Solo ajusta una pequeña fracción de los parámetros | Reducir coste: el 99% de los parámetros no cambia |

> [!tip] LoRA — Por Qué Es Importante para el Examen
> **LoRA (Low-Rank Adaptation)** es la técnica más popular de **PEFT (Parameter-Efficient Fine-tuning)**. En lugar de ajustar todos los pesos del modelo, añade pequeñas matrices de adaptación que se entrenan. El resultado: **80-95% menos de parámetros entrenables**, costes 10x menores, mismo rendimiento final. 
> 
> Amazon Bedrock soporta fine-tuning con estas técnicas de forma gestionada.

### Cuándo Usar Fine-tuning (NO RAG)

> [!warning] Fine-tuning es para COMPORTAMIENTO, no para CONOCIMIENTO
>
> - ✅ **Sí usa fine-tuning cuando:** Quieres cambiar el **estilo o tono** (responder siempre en formato JSON, usar el tono de voz de tu marca)
>
> - ✅ **Sí usa fine-tuning cuando:** Quieres enseñar una **habilidad nueva** (clasificar tickets de soporte en categorías propias muy específicas)
>
> - ❌ **No uses fine-tuning para:** Darle al modelo información actualizada → usa **RAG**
>
> - ❌ **No uses fine-tuning para:** Proporcionar documentos contextuales → usa **RAG**

---

## 🏗️ Técnica 4: Pre-training from Scratch

> [!quote] Definición
> Entrenar un Foundation Model completamente nuevo desde cero, con billones de tokens de datos propios y miles de GPUs durante semanas o meses.

### La Realidad del Pre-training

| Recurso | Magnitud |
| :--- | :--- |
| **Datos** | > 1 billón de tokens (TB o PB de texto) |
| **Cómputo** | Miles de GPUs/TPUs durante semanas o meses |
| **Coste** | Decenas a cientos de millones de dólares |
| **Equipo** | Decenas de investigadores senior de ML |
| **Tiempo total** | 6-18 meses (datos + entrenamiento + evaluación + alineamiento) |

**¿Quién hace esto en la práctica?**

- Anthropic (Claude), Meta (Llama), Google (Gemini), Amazon (Titan), Mistral AI

**Para el 99.9% de empresas:** No tiene sentido económico. Siempre es mejor partir de un FM existente y adaptarlo.

> [!tip] Truco de examen — Pre-training CASI NUNCA es la respuesta correcta
> Si el examen te presenta un escenario de empresa buscando la solución más práctica, **pre-training from scratch prácticamente nunca es la respuesta correcta**. Solo es válido si el escenario específicamente menciona un dominio totalmente nuevo sin FMs disponibles (ej. "proteómica de organismos marinos no estudiados previamente").

---

## 🗺️ Árbol de Decisión — ¿Qué Técnica Elegir?

```mermaid
flowchart TD
 A["¿Qué necesitas?"] --> B{"¿El modelo necesita\nconocimiento actualizado\no de datos privados?"}
 B -->|"Sí"| C["✅ RAG\n(Knowledge Bases for Bedrock)"]
 B -->|"No"| D{"¿Las respuestas actuales\nson funcionales pero\nnecesitan mejorarse?"}
 D -->|"Sí"| E["✅ Prompt Engineering\n(Zero-shot, Few-shot, CoT)"]
 D -->|"No: el estilo/capacidad\nnecesita cambiar"| F{"¿Tienes >1.000 ejemplos\netiquetados y presupuesto?"}
 F -->|"No"| E
 F -->|"Sí"| G["✅ Fine-tuning\n(LoRA, SFT en Bedrock)"]
 G --> H{"¿Ningún FM existente\nse adapta al dominio?"}
 H -->|"No: hay FMs útiles"| G
 H -->|"Sí: dominio totalmente inédito"| I["⚠️ Pre-training\nfrom Scratch\n(casi nunca aplicable)"]

 style C fill:#0d3721,stroke:#4aed8a,color:#b8f5d0
 style E fill:#0d3721,stroke:#4aed8a,color:#b8f5d0
 style G fill:#0d3721,stroke:#4aed8a,color:#b8f5d0
 style I fill:#4a2a0d,stroke:#ed8a4a,color:#f5d0b8
```

---

## 🎯 Escenarios de Examen — Elige la Técnica

> [!example] Escenario A
> *"Una empresa quiere que su chatbot responda preguntas sobre el manual de procedimientos interno (actualizado mensualmente)."*
> → **RAG** con el manual como Knowledge Base. El conocimiento cambia frecuentemente y es privado.

> [!example] Escenario B
> *"Un desarrollador quiere mejorar la calidad de las respuestas de un LLM en problemas de razonamiento lógico sin coste adicional."*
> → **Chain-of-Thought Prompting**. Sin coste de entrenamiento, mejora inmediata.

> [!example] Escenario C
> *"Una empresa legal quiere que el modelo responda siempre en un formato JSON estructurado con campos específicos del sector legal."*
> → **Fine-tuning**. Necesita cambiar el comportamiento/estilo de forma permanente y consistente.

> [!example] Escenario D
> *"Una startup farmacéutica quiere un modelo que hable el idioma de sus científicos, usando miles de ejemplos de publicaciones internas."*
> → **Fine-tuning** con los papers internos. Habilidad nueva + estilo de dominio específico.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
