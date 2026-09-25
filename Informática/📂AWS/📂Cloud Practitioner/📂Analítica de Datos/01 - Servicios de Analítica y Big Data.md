#aws #cloud-practitioner #ai-practitioner #data #analytics

> [!info] Exámenes Relacionados
> Estos servicios son **fundamentales para ambas certificaciones**. 
> - En **Cloud Practitioner (CLF-C02)** se evalúan a nivel conceptual (para qué sirve cada uno).
> - En **AI Practitioner (AIF-C01)** son el núcleo de la fase de preparación de datos (Data Engineering). La IA necesita datos limpios para entrenar, y estos servicios son los encargados de recolectarlos, limpiarlos y analizarlos.

---

# 📊 Servicios de Analítica y Big Data en AWS

Para que cualquier modelo de Inteligencia Artificial (Machine Learning o Generativa) funcione correctamente, primero necesita ingerir, catalogar y consultar datos masivos. 

## 1. Amazon Athena
- **Qué es:** Es un servicio de consultas interactivo que te permite analizar datos almacenados directamente en **Amazon S3** utilizando lenguaje SQL estándar.
- **Enfoque de examen:**
  - **No tiene servidor (Serverless):** No necesitas aprovisionar ni configurar bases de datos.
  - **Pago por uso:** Solo pagas por la cantidad de datos escaneados al ejecutar la consulta.
- **Cloud Practitioner vs AI Practitioner:** En CP, se evalúa como la forma más rápida de consultar S3 sin mover los datos. En AIP, se usa en la fase de análisis exploratorio para ver qué datos útiles tenemos antes de entrenar un modelo.

## 2. AWS Glue (Data Catalog y Crawlers)
- **Qué es:** Un servicio de integración de datos sin servidor (Serverless ETL: Extract, Transform, Load). Prepara y transforma los datos para que puedan ser analizados.
- **Componentes clave para el examen:**
  - **Glue Data Catalog:** Un índice central (como un índice de biblioteca) que guarda la metadata de todos tus datos en AWS (dónde están, qué formato tienen, sus columnas).
  - **Glue Crawler (Rastreador):** Es un programa que escanea automáticamente tus buckets de S3, descubre el esquema de los datos y los añade al *Data Catalog*.
- **Cloud Practitioner vs AI Practitioner:** En CP, recuerda que es "Serverless ETL". En AIP, es **vital**: limpia datos ruidosos, los transforma y los cataloga para que SageMaker o Bedrock puedan consumirlos.

## 3. Amazon Kinesis (Streaming de Datos en Tiempo Real)
- **Qué es:** Es la familia de servicios para recopilar, procesar y analizar flujos masivos de datos (streaming) en **tiempo real** (ej. clics en una web, logs, telemetría de sensores IoT).
- **Diferencia clave para el examen:**
  - **Kinesis Data Streams:** *Procesa* los datos en tiempo real. Retiene los datos (hasta 365 días) y necesitas crear aplicaciones para consumir y procesar esa información instantáneamente.
  - **Kinesis Data Firehose (Amazon Data Firehose):** *Entrega* los datos (Load). Simplemente toma el flujo de datos y lo escupe (como una manguera de bomberos, *firehose*) directamente en un destino final como S3, Redshift o OpenSearch. No retiene los datos.
- **Cloud Practitioner vs AI Practitioner:** En CP es el servicio estrella para "Streaming" o "Tiempo Real". En AIP se usa para IA predictiva en vivo (ej. detectar fraudes en tarjetas de crédito en el momento en que ocurren).

## 4. Amazon QuickSight
- **Qué es:** Un servicio de inteligencia empresarial (Business Intelligence - BI) en la nube. Permite crear cuadros de mando (dashboards) interactivos, gráficos y visualizaciones.
- **Enfoque de examen:**
  - Se integra de forma nativa con los servicios de datos de AWS (S3, Athena, Redshift).
  - Incluye **QuickSight Q**: una función potenciada por Machine Learning que permite a los usuarios hacer preguntas sobre sus datos en lenguaje natural (ej. *"¿Cuáles fueron las ventas totales en España el mes pasado?"*).
- **Cloud Practitioner vs AI Practitioner:** En CP es la herramienta visual de BI por excelencia. En AIP, se enmarca en la fase de visualización de los resultados de Machine Learning para presentarlos a los directivos.
