**Tags:** #sagemaker #inference #async-inference #serverless #ia #m2-servicios
#m2-servicios

> [!quote] Concepto fundamental
> Después de entrenar un modelo en SageMaker, necesitas desplegarlo para que otras aplicaciones puedan consumirlo (hacer inferencias). SageMaker ofrece 4 opciones principales de despliegue según tus requisitos de latencia, tamaño de datos y presupuesto.

---

## 🚀 Tipos de Inferencia en Amazon SageMaker

Es **crucial para el examen AIF-C01** conocer cuándo elegir cada tipo de inferencia. La decisión se basa en la latencia, el tamaño del payload y si necesitas un punto de enlace (endpoint) persistente o no.

### 1. Real-Time Inference (Inferencia en Tiempo Real)
- **Casos de uso:** Baja latencia interactiva y continua, donde se necesita respuesta en milisegundos. (ej. recomendaciones de productos en la web al hacer clic, detección de fraude en pagos online).
- **Cómo funciona:** El modelo se aloja en una instancia EC2 dedicada que está **siempre encendida** esperando peticiones.
- **Payload máximo:** 6 MB.
- **Desventaja:** Pagas por la instancia encendida 24/7 aunque no haya peticiones (costo fijo).

### 2. Serverless Inference (Inferencia sin Servidor)
- **Casos de uso:** Tráfico intermitente, impredecible o modelos que no se usan constantemente pero necesitan estar disponibles al instante (ej. un chatbot de soporte que casi no se usa de madrugada).
- **Cómo funciona:** AWS gestiona la infraestructura subyacente. El endpoint se enciende, escala automáticamente según el tráfico y **se apaga a cero (scale-to-zero)** si no hay peticiones.
- **Desventaja:** Puede haber un "cold start" (latencia inicial al encender la instancia). No pagas tiempo de inactividad, pagas por invocación.

### 3. Asynchronous Inference (Inferencia Asíncrona)
- **Casos de uso:** Cuando el payload es grande (modelos pesados, imágenes de alta resolución) o el tiempo de procesamiento es largo, pero aún así necesitas una respuesta relativamente rápida una vez finalizado (ej. procesar un video de varios minutos).
- **Cómo funciona:** Coloca la petición en una cola interna.
- **Límites clave para el examen:** Soporta entrada masiva de datos de **hasta 1 GB** y tiempos de procesamiento largos de **hasta 1 hora**.
- **Ventaja:** Permite hacer *scale-to-zero* de la infraestructura y responde a una URL de S3 cuando termina.

### 4. Batch Transform (Transformación por Lotes)
- **Casos de uso:** Procesamiento diferido offline para archivos enormes sin necesidad inmediata. El usuario no está esperando la respuesta (ej. clasificar un mes entero de registros durante la madrugada).
- **Cómo funciona:** Apuntas el trabajo a un bucket S3 completo lleno de datos (puede ser de múltiples GBs). SageMaker levanta la infraestructura, procesa todo, guarda el resultado en otro bucket S3 y **apaga la infraestructura**.
- **Ventaja:** La forma más eficiente y barata de procesar datos masivos si no hay requisitos de tiempo real.

---

## 📊 Tabla Comparativa Definitiva

> [!brain] Tabla de Decisión Rápida para el Examen

| Tipo de Inferencia | Latencia Esperada | Tamaño Máx. Payload | Costo de Inactividad | ¿Escala a Cero? | Ideal Para |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Real-Time** | Milisegundos | 6 MB | Sí (Pagas 24/7) | ❌ No | Tráfico constante y crítico |
| **Serverless** | Segundos (cold start) | 6 MB | No | ✅ Sí | Tráfico impredecible o esporádico |
| **Asynchronous** | Minutos a 1 hora | **Hasta 1 GB** | No | ✅ Sí | Payloads grandes, visión artificial |
| **Batch Transform** | Horas / Diferido | Múltiples GBs | No | (No usa endpoints) | Análisis nocturno/histórico masivo |

---
→ Volver al índice: [[📂M2 - Servicios IA-ML AWS/00 - Índice Módulo 2|🪐 Módulo 2: Servicios IA-ML AWS]]
