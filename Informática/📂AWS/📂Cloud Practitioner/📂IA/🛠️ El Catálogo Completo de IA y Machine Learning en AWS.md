**Tags:** #aws #ia #machine-learning #sagemaker #comprehend #polly #lex #rekognition #cloud-practitioner #cp-ia

> [!summary] El Concepto Clave
> AWS divide su oferta de IA/ML en tres niveles de abstracción. El **Nivel 1** te da herramientas listas para usar (solo llamas a una API); el **Nivel 2** te da la plataforma para construir tus propios modelos (**SageMaker AI**); y el **Nivel 3** te da los ladrillos puros (servidores avanzados y librerías de código) si eres un experto de bajo nivel.

---

## 🥞 Nivel 1: Servicios de IA Prediseñados (Modelos Listos para Usar)

No necesitas saber matemáticas ni saber entrenar un modelo. AWS ya lo ha hecho por ti. Estos servicios se dividen en tres grandes familias según lo que procesan:

### A. Servicios Lingüísticos (Texto y Voz)

* **Amazon Comprehend (El Analizador de Sentimientos):** Utiliza procesamiento de lenguaje natural (NLP) para leer textos (como correos o reseñas de clientes) y descubrir si la gente está contenta, enfadada o neutra. También extrae frases clave.

* **Amazon Polly (Texto a Voz):** Convierte texto escrito en archivos de audio con voces humanas increíblemente realistas, soportando múltiples idiomas y acentos.
 
* **Amazon Transcribe (Voz a Texto):** Lo contrario a Polly. Escucha un archivo de audio o voz en tiempo real y lo convierte en texto escrito.
 
* **Amazon Translate (El Traductor):** Traduce grandes volúmenes de texto a diferentes idiomas en tiempo real o por lotes.

### B. Visión Artificial y Búsqueda Inteligente

* **Amazon Rekognition (El Ojo Digital):** Analiza imágenes y vídeos guardados en Amazon S3. Puede identificar objetos, personas, texto e incluso detectar contenido inapropiado (moderación).
 
* **Amazon Textract (El Extractor de Formularios):** Va un paso más allí del reconocimiento de texto simple (OCR). Sabe leer tablas y formularios escaneados, identificando qué dato corresponde a cada casilla.
 
* **Amazon Kendra (El Buscador Inteligente):** Un motor de búsqueda para empresas que entiende el contexto de la pregunta en lenguaje natural, en lugar de buscar simples palabras clave en un documento.

### C. Personalización e IA Conversacional

* **Amazon Lex (El Constructor de Chatbots):** Es la tecnología que utiliza internamente Alexa. Permite añadir interfaces de conversación (de texto o voz) a tus aplicaciones.
 
* **Amazon Personalize (El Recomendador estilo Amazon.com):** Examina el historial de tus clientes y crea recomendaciones de productos o contenido totalmente adaptadas a sus gustos personales.

---

## 🧪 Nivel 2: Servicios de Machine Learning (Control sin Infraestructura)

Si los servicios del Nivel 1 se te quedan cortos porque necesitas un modelo único para tu negocio, pasas al Nivel 2.

### Amazon SageMaker AI

Es la plataforma estrella de AWS para proyectos de ML personalizados. Te permite **desarrollar, entrenar e implementar tus propios modelos** sin tener que configurar los servidores que corren por debajo.

* **Para todos los perfiles:** Tiene un entorno de desarrollo (IDE) avanzado para los científicos de datos avanzados y una interfaz visual *sin código* para los analistas de negocio.

* **Flujos Repetibles (MLOps):** Permite automatizar todo el proceso, realizar un seguimiento de los experimentos de entrenamiento y auditar los datos de forma transparente.

---

## 🏗️ Nivel 3: Marcos de Trabajo (Frameworks) e Infraestructura de ML

Diseñado exclusivamente para ingenieros expertos o centros de investigación que exigen un control total y absoluto sobre el silicio y el código.

* **Marcos de Trabajo (Frameworks):** Son las bibliotecas de software de código abierto más famosas de la industria para programar IA, como **PyTorch** y **TensorFlow**. AWS está optimizado para ejecutarlas al máximo rendimiento.

* **Infraestructura de ML:** Instancias de **Amazon EC2 especializadas** (con las tarjetas gráficas más potentes del mercado) y clústeres de computación masiva como Amazon EMR o ECS para procesar algoritmos altamente complejos.

---

## 🎯 Tabla de Emparejamiento Rápido para el Examen

| Si la pregunta te pide... | El servicio exacto es... |
| :--- | :--- |
| Analizar el **sentimiento** de unos textos. | **Amazon Comprehend** |
| Convertir guiones de texto a **voz realista**. | **Amazon Polly** |
| Crear un **Chatbot** de atención al cliente. | **Amazon Lex** |
| Extraer datos de **tablas y formularios** escaneados. | **Amazon Textract** |
| **Entrenar un modelo propio** sin gestionar servidores. | **Amazon SageMaker AI** |
| Usar **PyTorch** o **TensorFlow** con control total del hardware. | **Marcos de trabajo e Infraestructura de ML (Nivel 3)** |

---

---
→ Volver al índice: [[📂IA/00 - Índice IA|🪐 IA]]
