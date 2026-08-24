**Tags:** #aws #arquitectura #data-pipeline #machine-learning #sagemaker #athena #cloud-practitioner #cp-ia

> [!summary] El Concepto Clave
> En una empresa real, los científicos de datos (Analítica) y los ingenieros de IA (Machine Learning) suelen necesitar los *mismos* datos. En lugar de hacer el trabajo dos veces, se construye una **Canalización de Datos Automatizada** que extrae la información de la base de datos de la app, la limpia y la deja en un Lago de Datos central (S3) para que todos puedan usarla.

---
## 🗺️ El Viaje de los Datos (Paso a Paso)

Imagina una aplicación de comercio electrónico que quiere recomendar productos a sus clientes en tiempo real. Así es como viaja la información desde que el usuario hace clic hasta que el modelo aprende:

### 📱 1. La Aplicación y 🗄️ 2. La Base de Datos (El Origen)

* **La Acción:** Los clientes usan la app para comprar.

* **El Almacenamiento (Amazon DynamoDB):** Todo ese historial de clics y compras se guarda en DynamoDB. 

* *¿Por qué no entrenar la IA directamente aquí?* DynamoDB es brutalmente rápido para leer el carrito de un solo usuario (baja latencia), pero es malísimo y carísimo para escanear *toda* la tabla de golpe para entrenar a una IA. Hay que sacar los datos de ahí.

### 🌪️ 3. La Ingesta (El Transporte)

* **El Problema:** Hay que sacar los datos de DynamoDB continuamente.

* **La Solución:** Se usa **Amazon Kinesis Data Streams** para capturar todos los cambios en la base de datos al instante. Kinesis le pasa ese flujo a **Amazon Data Firehose**, que se encarga de empaquetar los datos para enviarlos a su destino final.

### ⚙️ 4. El Procesamiento (La Limpieza)

* **El Problema:** Los datos salen de DynamoDB en formato `JSON`, pero los científicos de datos y los modelos de Machine Learning prefieren trabajar con tablas en formato `.csv` (valores separados por comas).

* **La Solución (AWS Lambda):** Mientras Firehose transporta los datos, invoca automáticamente a una función **Lambda** en el aire. Lambda actúa como una trituradora/conversora: coge el JSON, lo transforma en CSV sobre la marcha y se lo devuelve a Firehose.

### 🪣 5. La Entrega (El Lago de Datos)

* **El Destino (Amazon S3):** Firehose escupe todos esos archivos CSV limpios en un bucket de S3. Este es el gran almacén central y barato de la empresa.

### 📚 6. La Catalogación (El Índice)

* **El Inventario (AWS Glue Data Catalog):** S3 es solo un cajón desastre lleno de archivos CSV. Para que alguien pueda buscar en ellos, AWS Glue crea un catálogo virtual (metadatos) que dice: *"El archivo X tiene 3 columnas: Nombre, Fecha y Precio"*.

---

## 👥 Los Consumidores (El Destino Final)

Una vez que los datos están limpios en S3 y bien etiquetados en Glue, la canalización se divide en dos caminos para dos equipos diferentes:

### 🔎 7. El Científico de Datos (Analítica)

* **La Herramienta (Amazon Athena):** El científico quiere saber cuántas ventas hubo el martes. En lugar de descargar los CSV, usa **Athena** para lanzar una consulta SQL clásica directamente contra los archivos que están descansando en S3 (usando el esquema que le chivó Glue). Es rápido y Serverless.

### 🤖 8. El Ingeniero de Machine Learning (IA)

* **La Herramienta (Amazon SageMaker AI):** El ingeniero coge esos mismos archivos CSV de S3 y los usa para entrenar una nueva versión de su Modelo de Recomendaciones.

* **El Círculo se Cierra:** Una vez entrenado, el modelo de SageMaker se conecta a la aplicación inicial (Paso 1) para empezar a ofrecer recomendaciones en tiempo real mucho más precisas a los clientes.

---

## 💡 Lección para el Examen

La magia de esta arquitectura es que **es totalmente Serverless y Automática**. Nadie tiene que darle a un botón todos los días para exportar la base de datos a CSV. Los datos fluyen, se transforman solos y alimentan tanto los gráficos de la empresa como los cerebros de la Inteligencia Artificial de forma continua.



![[Sin título-4.png]]

1. **Hacer Recomendaciones**

	Una empresa de comercio electrónico utiliza un modelo de ML para hacer recomendaciones de productos.

2. **Almacenar los Datos de la Aplicación**

	Una base de datos de Amazon DynamoDB almacena los datos históricos de la clientela recopilados a través de la aplicación. Esto resulta útil para lecturas y escrituras de baja latencia, pero no es ideal para el entrenamiento de modelos de ML.
	
3. Ingerir Datos

	Kinesis Data Streams ingiere los datos de DynamoDB. Después, Amazon Data Firehose añade los datos.

4. **Procesar Datos**

	Los datos están en formato JSON, por lo que Firehose invoca una función de AWS Lambda que transforma los datos en formato.csv.

5. **Entregar Datos**

	A continuación, Firehose entrega los datos al lago de datos de Amazon S3 de la empresa, donde están disponibles para varios consumidores.

6. **Catalogar Datos**

	El catálogo de datos de AWS Glue sirve como repositorio de metadatos con tablas que describen el esquema y la ubicación de los datos de Amazon S3.

7. **Analizar Datos**

	Los científicos de datos utilizan Athena para recopilar información a través de consultas.
	
8. **Entrenar un Modelo**

	SageMaker AI lee el mismo conjunto de datos directamente desde Amazon S3. Los equipos de ingeniería de ML pueden entrenar nuevas versiones del modelo de recomendación utilizando la información más reciente.

---

---
→ Volver al índice: [[📂IA/00 - Índice IA|🪐 IA]]
