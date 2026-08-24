**Tags:** #aws #ia-generativa #deep-learning #bedrock #amazon-q #sagemaker-jumpstart #cloud-practitioner #cp-ia

> [!summary] El Concepto Clave
> La IA Generativa es la evolución más reciente del Aprendizaje Profundo (*Deep Learning*). En lugar de limitarse a clasificar o predecir datos existentes, es capaz de **crear contenido nuevo** (texto, imágenes, código, música). AWS proporciona herramientas para consumirla e integrarla de forma masiva sin necesidad de que configures servidores o seas un experto matemático.

---
## 🪆 1. La "Matrioshka" Tecnológica: Del ML a la IA Generativa

Para no perderte en el examen, visualiza la Inteligencia Artificial como un juego de muñecas rusas donde cada concepto está metido dentro de otro:

1.  **Inteligencia Artificial (IA):** El concepto general (máquinas imitando tareas humanas).

2.  **Machine Learning (ML):** El subconjunto donde las máquinas encuentran patrones en datos históricos de forma matemática.

3.  **Deep Learning (DL / Aprendizaje Profundo):** Un subconjunto avanzado del ML. Aquí los modelos se entrenan utilizando **Redes Neuronales Artificiales** que imitan el cerebro humano. Los datos pasan por múltiples capas de funciones matemáticas secuenciales hasta generar el modelo final. Permite resolver problemas hipercomplejos como la visión artificial.

4.  **IA Generativa:** Un tipo específico de *Deep Learning* enfocado puramente en la creación de nuevo contenido.

---

## 🏗️ 2. Los Modelos Fundacionales (FMs) y LLMs

La IA Generativa no empieza desde cero cada vez que le haces una pregunta. Se apoya en motores preentrenados colosales:

* **Modelos Fundacionales (Foundational Models - FMs):** Son modelos de ML extremadamente gigantescos que han sido entrenados previamente (*pre-trained*) con colecciones masivas de datos de todo el planeta. A diferencia del ML tradicional (que solo sirve para una tarea concreta), un FM es flexible y **puede adaptarse a múltiples tareas distintas**.

* **LLMs (Large Language Models):** Son un tipo específico de Modelo Fundacional que ha sido entrenado de forma masiva con texto escrito para comprender, procesar y generar lenguaje humano perfectamente.

* #### Ejemplos de LLMs

- ChatGPT (basado en los modelos GPT de [OpenAI](https://openai.com?utm_source=chatgpt.com))
- [Gemini](https://gemini.google.com?utm_source=chatgpt.com) de [Google](https://google.com?utm_source=chatgpt.com)
- [Claude](https://claude.ai?utm_source=chatgpt.com) de [Anthropic](https://www.anthropic.com?utm_source=chatgpt.com)
- [Llama](https://www.llama.com?utm_source=chatgpt.com) de [Meta](https://about.meta.com?utm_source=chatgpt.com)

### Ejemplos de Modelos Fundacionales (no solo texto)

- [GPT-5 series (OpenAI)](https://openai.com?utm_source=chatgpt.com) – texto, imágenes y otras modalidades.
- [Gemini 2.x](https://gemini.google.com?utm_source=chatgpt.com) – multimodal (texto, imágenes, audio, vídeo).
- [Claude models](https://www.anthropic.com?utm_source=chatgpt.com) – principalmente lenguaje y análisis de documentos.
- [Stable Diffusion](https://stability.ai?utm_source=chatgpt.com) – generación de imágenes.
- [DALL·E](https://openai.com?utm_source=chatgpt.com) – generación de imágenes a partir de texto.

---

## 🛠️ 3. Las Soluciones de IA Generativa de AWS

Amazon ofrece tres grandes servicios para implementar IA Generativa en proyectos empresariales según el caso de uso exacto:

### A. Amazon Bedrock (La API Unificada)

* **¿Qué es?** Es un servicio **completamente administrado (Serverless)** que te da acceso a los Modelos Fundacionales más potentes del mercado (tanto de Amazon como de otras empresas líderes de IA, como **Claude** o **Stable Diffusion**).

* **El Superpoder:** Te conectas a múltiples modelos diferentes usando **una única API unificada**. Puedes experimentar con ellos, personalizarlos de forma privada con los datos confidenciales de tu empresa sin que estos salgan a internet, y desplegarlos sin tocar un solo servidor.

* **Caso de uso:** Crear aplicaciones multimodales corporativas de nivel empresarial (generación de texto, imágenes, agentes avanzados).

### B. Amazon SageMaker JumpStart (El Catálogo de Modelos)

* **¿Qué es?** Un "hub" o centro de recursos dentro de la plataforma *SageMaker AI*. 

* **¿Cómo funciona?** Es una biblioteca de soluciones de ML prediseñadas y modelos fundacionales de código abierto listos para usar. Te permite examinar el catálogo, elegir un modelo entrenado previamente, **ajustarlo con tus propios datos específicos (*fine-tuning*)** e implementarlo en tu entorno con un par de clics.

* **Caso de uso:** Equipos que ya trabajan en SageMaker y quieren experimentar o prototipar rápidamente soluciones de NLP o visión artificial antes de casarse con una arquitectura definitiva.

### C. Amazon Q (Tu Asistente de IA Inteligente)

Es un asistente conversacional interactivo diseñado para el entorno laboral que se divide en dos productos radicalmente distintos para el examen:

* **1. Amazon Q Business:** Se conecta de forma segura a los repositorios de información internos de tu empresa (wikis, documentos de SharePoint, carpetas de archivos). Los empleados pueden chatear con él para buscar información corporativa interna, automatizar flujos de trabajo o resumir datos confidenciales de la compañía con total seguridad de accesos.

* **2. Amazon Q Developer:** El mejor amigo del programador. Se integra directamente en los entornos de desarrollo (IDEs) y **ofrece recomendaciones y bloques de código completos en tiempo real** para lenguajes como Python, Java, JavaScript, C# y TypeScript, agilizando el desarrollo y realizando revisiones automáticas.

---

## 📊 Chuleta de Examen: El "Trigger" del Éxito

| Si la pregunta menciona... | El servicio correcto es... | Palabra clave secreta |
| :--- | :--- | :--- |
| Generación de contenido multimodal (texto e imágenes) a gran escala, nivel empresarial, usando **una única API**. | **Amazon Bedrock** | "Single API", "Claude / Stable Diffusion", "Fully Managed" |
| Un centro dentro de SageMaker para desplegar rápidamente soluciones prediseñadas con **pocos clics**. | **Amazon SageMaker JumpStart** | "Hub de ML", "Modelos preentrenados", "Prototipos" |
| Buscar respuestas urgentes o resumir informes utilizando los **repositorios de información de mi empresa**. | **Amazon Q Business** | "Repositorios empresariales", "Productividad del personal" |
| Escribir código más rápido en lenguajes como Python, Java o C# integrado en el IDE. | **Amazon Q Developer** | "Recomendaciones de código", "Bloques lógicos", "Escribir código rápido" |

---

---
→ Volver al índice: [[📂IA/00 - Índice IA|🪐 IA]]
