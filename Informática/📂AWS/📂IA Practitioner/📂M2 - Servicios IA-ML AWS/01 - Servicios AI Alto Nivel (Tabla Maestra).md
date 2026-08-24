**Tags:** #servicios-aws #ai #rekognition #comprehend #lex #polly #transcribe #ia #m2-servicios

> [!quote] Concepto clave
> Los servicios de IA de alto nivel de AWS son **APIs pre-construidas** que añaden capacidades de inteligencia artificial a cualquier aplicación sin necesidad de entrenar modelos. Solo consumes el servicio y recibes resultados.

---

## 🗺️ Mapa Visual de Servicios

```mermaid
flowchart LR
    subgraph V ["👁️ Visión"]
        direction TB
        V1["Rekognition"] --> V1a["Imágenes y vídeos"]
        V1 --> V1b["Caras, objetos, texto"]
        V2["Textract"] --> V2a["Documentos, PDFs"]
        V2 --> V2b["Tablas y formularios"]
    end

    subgraph L ["🗣️ Voz y Lenguaje"]
        direction TB
        L1["Transcribe"] --> L1a["Audio → Texto"]
        L1 --> L1b["Speech-to-Text"]
        L2["Polly"] --> L2a["Texto → Audio"]
        L2 --> L2b["Text-to-Speech"]
        L3["Translate"] --> L3a["Idioma A → Idioma B"]
        L3 --> L3b["NMT"]
    end

    subgraph C ["🧠 Comprensión de Texto"]
        direction TB
        C1["Comprehend"] --> C1a["NLP, sentimiento"]
        C1 --> C1b["Entidades, PII"]
        C2["Lex"] --> C2a["Chatbots, intenciones"]
        C2 --> C2b["Slots y fulfillment"]
        C3["Kendra"] --> C3a["Búsqueda semántica"]
        C3 --> C3b["Enterprise search"]
    end

    subgraph P ["🔮 Predicción"]
        direction TB
        P1["Personalize"] --> P1a["Recomendaciones"]
        P1 --> P1b["Similar a Netflix/Amazon"]
        P2["Forecast"] --> P2a["Series temporales"]
        P2 --> P2b["Predicción de demanda"]
    end

    classDef cat1 fill:#0d2137,stroke:#4a9eda,color:#b8d9f5
    classDef cat2 fill:#0d3721,stroke:#4aed8a,color:#b8f5d0
    classDef cat3 fill:#372d0d,stroke:#edba4a,color:#f5e8b8
    classDef cat4 fill:#2d0d37,stroke:#b04aed,color:#e8b8f5
    
    classDef sub1 fill:none,stroke:#4a9eda,color:#b8d9f5,stroke-dasharray: 5 5,stroke-width:2px
    classDef sub2 fill:none,stroke:#4aed8a,color:#b8f5d0,stroke-dasharray: 5 5,stroke-width:2px
    classDef sub3 fill:none,stroke:#edba4a,color:#f5e8b8,stroke-dasharray: 5 5,stroke-width:2px
    classDef sub4 fill:none,stroke:#b04aed,color:#e8b8f5,stroke-dasharray: 5 5,stroke-width:2px

    class V sub1
    class L sub2
    class C sub3
    class P sub4

    class V1,V1a,V1b,V2,V2a,V2b cat1
    class L1,L1a,L1b,L2,L2a,L2b,L3,L3a,L3b cat2
    class C1,C1a,C1b,C2,C2a,C2b,C3,C3a,C3b cat3
    class P1,P1a,P1b,P2,P2a,P2b cat4
```

---

## 📊 Tabla Maestra Comparativa

| Servicio | Entrada | Salida | Superpoder | Palabras clave del examen |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon Rekognition** | 🖼️ Imagen / 🎥 Vídeo | Etiquetas, caras, texto, objetos, emociones | Visión por computadora en imágenes y vídeo en tiempo real | `análisis de imágenes`, `verificación identidad`, `content moderation`, `PPE detection` |
| **Amazon Transcribe** | 🎤 Audio (.mp3, .wav, etc.) | 📝 Texto transcrito | Speech-to-Text con identificación de hablantes y redacción de PII | `transcripción`, `subtítulos`, `call center`, `speaker diarization` |
| **Amazon Translate** | 📝 Texto (idioma origen) | 📝 Texto (idioma destino) | Traducción neuronal fluida entre 75+ idiomas | `traducción automática`, `localización`, `NMT` |
| **Amazon Comprehend** | 📝 Texto no estructurado | Sentimiento, entidades, idioma, PII, temas | NLP: analiza y extrae insights de texto | `análisis de sentimiento`, `NER`, `detección PII`, `NLP` |
| **Amazon Polly** | 📝 Texto | 🔊 Audio (voz sintética) | Text-to-Speech con voces neurales hiperrealistas | `síntesis de voz`, `text-to-speech`, `narración`, `accesibilidad` |
| **Amazon Textract** | 📄 PDF, imagen de documento | Texto, tablas y formularios estructurados | OCR avanzado que entiende la estructura de documentos | `OCR`, `facturas`, `formularios`, `tablas`, `IDP` |
| **Amazon Lex** | 🎤 Voz / 📝 Texto | Intents detectados + Slots extraídos | Chatbots y asistentes de voz (tecnología de Alexa) | `chatbot`, `bot conversacional`, `Alexa`, `intent`, `slot` |
| **Amazon Personalize** | 📊 Historial de interacciones | 🎯 Lista de ítems recomendados | Motor de recomendaciones en tiempo real | `recomendaciones`, `personalización`, `similar a Amazon/Netflix` |
| **Amazon Forecast** | 📈 Serie temporal histórica | 📊 Predicciones futuras con intervalos | Predicción de series temporales con variables externas | `predicción demanda`, `forecasting`, `serie temporal`, `stock` |
| **Amazon Kendra** | 📚 Repositorios de documentos | Respuesta en lenguaje natural | Búsqueda semántica empresarial con comprensión de contexto | `búsqueda inteligente`, `enterprise search`, `FAQ` |

---

## ⚡ Tabla de Decisión Rápida — Elige el Servicio

| Si el escenario dice... | El servicio es... |
| :--- | :--- |
| "Detectar objetos/caras en fotos o vídeo" | **Amazon Rekognition** |
| "Convertir grabaciones de audio a texto" | **Amazon Transcribe** |
| "Traducir contenido a otro idioma" | **Amazon Translate** |
| "Analizar el sentimiento de reseñas de clientes" | **Amazon Comprehend** |
| "Generar narración de audio desde texto" | **Amazon Polly** |
| "Extraer datos de facturas o formularios PDF" | **Amazon Textract** |
| "Construir un chatbot de atención al cliente" | **Amazon Lex** |
| "Recomendar productos a usuarios individuales" | **Amazon Personalize** |
| "Predecir ventas para el próximo mes" | **Amazon Forecast** |
| "Buscar información en documentos internos de la empresa" | **Amazon Kendra** |

---

## 🔀 Confusiones Habituales en el Examen

> [!warning] Rekognition vs Textract
> - **Rekognition:** Lee texto en **imágenes naturales** (señales de tráfico, matrículas, rótulos en fotos). Pensado para "ver" el mundo.
> - **Textract:** Extrae texto **estructurado de documentos** (tablas, formularios, PDFs). Pensado para IDP (Intelligent Document Processing) empresarial.
>
> *Pista: Si el escenario habla de "facturas", "formularios" o "documentos" → Textract. Si habla de "fotos", "vídeo" o "imágenes" → Rekognition.*

> [!warning] Comprehend vs Lex
> - **Comprehend:** **ANALIZA** texto pasivamente. ¿Qué dice? ¿Qué siente? ¿Qué entidades menciona? No hay conversación.
> - **Lex:** **COMPRENDE INTENCIONES** en un contexto conversacional. El usuario dice algo → Lex identifica qué quiere hacer (intent) y qué datos necesita (slots) → ejecuta una acción.
>
> *Pista: "Chatbot" → Lex. "Analizar texto" → Comprehend.*

> [!warning] Transcribe vs Polly — Son OPUESTOS
> - **Transcribe:** Audio → Texto (escucha y transcribe)
> - **Polly:** Texto → Audio (lee en voz alta)
>
> *Mnemotécnico: **Polly** habla como un **loro** (polly = loro en inglés). Transcribe transcribe.*

> [!warning] Personalize vs Forecast
> - **Personalize:** "¿Qué ítems le gustarán a ESTE usuario?" → Recomendaciones 1:1
> - **Forecast:** "¿Cuántas unidades venderemos MAÑANA?" → Predicción de cantidades futuras

---
→ Volver al índice: [[📂M2 - Servicios IA-ML AWS/00 - Índice Módulo 2|🪐 Módulo 2: Servicios IA-ML AWS]]
