**Tags:** #aws #analytics #data-pipeline #big-data #kinesis #glue #redshift #athena #cloud-practitioner #cp-ia

> [!summary] El Concepto Clave
> Una canalización de datos (Data Pipeline) es el camino automatizado que recorren los datos desde su origen hasta que se convierten en gráficos legibles. Automatizar este flujo evita el trabajo manual y los errores humanos, pasando por 5 fases esenciales: Ingesta, Almacenamiento, Catalogación, Procesamiento y Análisis/Visualización.

---
## 🏗️ La Analogía General: El Viaje del Agua

Para entender este ecosistema sin perderte en las siglas, imagina que los datos son **agua salvaje** que fluye de un río y tú quieres transformarla en **botellas de agua mineral etiquetadas** listas para vender en un supermercado:

1. **Ingesta:** Las bombas de extracción que sacan el agua del río (Kinesis o Firehose).

2. **Almacenamiento:** El gran embalse de agua bruta (S3) o el almacén de botellas ordenadas (Redshift).

3. **Catalogación:** El libro de inventario que registra de dónde vino el agua y qué contiene (Glue Data Catalog).

4. **Procesamiento:** La planta purificadora que filtra la arena y añade minerales (Glue o EMR).

5. **Análisis y Visualización:** El laboratorio de control de calidad (Athena) y las pantallas de ventas de la tienda (QuickSight).

---

## ⚡ Fase 1: Ingesta de Datos (¿Cómo entran?)

Mover los datos desde los sensores, aplicaciones o bases de datos hacia la nube. Puede ser en tiempo real o por lotes (con retardo).

* **Amazon Kinesis Data Streams (Tiempo Real Puro):** Captura de forma continua terabytes de datos por segundo con una latencia de milisegundos. Admite que múltiples aplicaciones consuman el mismo flujo a la vez.

    * *Caso de uso de examen:* Analizar las tendencias del mercado de valores al instante para tomar decisiones bancarias inmediatas.
    
* **Amazon Data Firehose (Casi Tiempo Real / ETL de transmisión):** Recopila los datos y los empaqueta automáticamente para enviarlos directamente a su destino (como S3 o Redshift) en cuestión de segundos. No requiere gestionar servidores.

    * *Caso de uso de examen:* Recopilar registros de miles de dispositivos domésticos inteligentes para guardarlos a largo plazo.

---

## 🛢️ Fase 2: Almacenamiento (¿Dónde se guardan?)

* **Amazon S3 (El Lago de Datos / Data Lake):** Almacena cantidades masivas de datos **sin procesar, estructurados o no estructurados** (imágenes, textos, vídeos). Es flexible, infinito y elástico.

* **Amazon Redshift (El Almacén de Datos / Data Warehouse):** Diseñado para datos **altamente estructurados o semiestructurados**. Escala a nivel de petabytes y está optimizado al 100% para Inteligencia de Negocios (BI) y analítica compleja de alto rendimiento.

---

## 📋 Fase 3: Catalogación (¿Cómo sabemos qué hay?)

* **Catálogo de Datos de AWS Glue (El Inventario):** Es un repositorio centralizado que guarda los **metadatos** (los datos sobre los datos: formato, fecha de creación, origen). Es como la etiqueta de una foto que te dice la hora y las coordenadas de dónde se tomó. Ayuda a que todas las herramientas de análisis sepan qué estructura tienen los datos antes de leerlos.

---

## 🧪 Fase 4: Procesamiento y Transformación (¿Cómo se limpian?)

Los datos brutos suelen venir "sucios" o desorganizados. Hay que hacerles un proceso **ETL** (Extraer, Transformar y Cargar).

* **AWS Glue (Serverless y Visual):** Un servicio completamente administrado para preparar y limpiar datos. Permite crear trabajos ETL de forma visual e incluso generar scripts sin picar código. Ideal para flujos de trabajo estándar y automatizados.

* **Amazon EMR (Elastic MapReduce - Big Data Masivo):** Diseñado para procesar datos a escala gigante utilizando marcos de trabajo de código abierto muy populares como **Apache Spark, Hadoop o Hive**. 

    * *Clave de examen:* Requiere que el equipo tenga experiencia previa en herramientas de Big Data y necesite configuraciones muy personalizadas de clústeres.

---

## 📊 Fase 5: Análisis y Visualización (¿Cómo se consumen?)

Una vez limpios, llega el momento de hacerles preguntas y ver los resultados.

* **Amazon Athena (Consultas Express en S3):** Un motor de consultas **Serverless** que te permite escribir código SQL clásico directamente sobre los archivos guardados en Amazon S3. No tienes que montar una base de datos; solo pagas por los gigabytes de datos que escanea cada consulta que ejecutas.

* **Amazon Redshift (Consultas Complejas y Corporativas):** Utiliza almacenamiento en columnas y procesamiento en paralelo para resolver consultas analíticas pesadas y recurrentes sobre tablas gigantescas.

* **Amazon QuickSight (Los Cuadros de Mando / BI):** La herramienta visual de inteligencia de negocios. Permite tanto a ingenieros como a directivos crear paneles gráficos interactivos y modernos. Además, integra **Amazon Q** para que puedas pedirle gráficos usando lenguaje natural (ej: *"Muéstrame las ventas de café de este mes comparadas con las de junio pasado"*).

* **Amazon OpenSearch Service (Búsqueda y Monitorización):** Especializado en la búsqueda de texto en tiempo real y el análisis de registros (logs), métricas de aplicaciones y observabilidad de sistemas.

---

## 🎯 Chuletas de Emparejamiento

### Kinesis Data Streams vs. Data Firehose

* **Kinesis Streams:** Tiempo real estricto, baja latencia, tú construyes la aplicación que consume el flujo
.
* **Firehose:** Casi tiempo real, automatizado, su función principal es "cargar" el dato directamente en S3, Redshift u OpenSearch.

### Amazon Athena vs. Amazon Redshift

* **Athena:** Consultas rápidas y ocasionales en SQL directamente sobre archivos sueltos de S3. Serverless.

* **Redshift:** Un almacén estructurado masivo corporativo (Data Warehouse) para analítica pesada y constante a gran escala.

### AWS Glue vs. Amazon EMR

* **Glue:** ETL Serverless, interfaces visuales, automatización de tareas sin gestionar clústeres.

* **EMR:** Big Data avanzado a gran escala basado en ecosistemas como **Spark** o **Hadoop** con control del clúster.

---

---
→ Volver al índice: [[📂IA/00 - Índice IA|🪐 IA]]
