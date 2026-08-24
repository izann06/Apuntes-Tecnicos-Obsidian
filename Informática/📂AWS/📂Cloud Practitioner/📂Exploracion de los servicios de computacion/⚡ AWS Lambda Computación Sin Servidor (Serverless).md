**Tags:** #aws #lambda #serverless #computacion #event-driven #cloud-practitioner #cp-exploracion-de-los-servicios-de-computacion

> [!summary] El Concepto Core
> Lambda es un servicio de computación *Totalmente Administrado* y *Sin Servidor*. Ejecuta tu código en respuesta a eventos específicos (disparadores), escalando automáticamente y cobrándote **solo** por el tiempo de computación consumido, hasta el milisegundo.

---
## 1. ¿Qué significa "Sin Servidor" (Serverless)?

"Sin servidor" no significa que no haya servidores físicos en algún lugar de AWS. Significa que **tú no tienes que verlos, provisionarlos, ni administrarlos**.

*   **Lo que AWS hace:** Gestiona la ejecución, el escalado de los recursos, la disponibilidad, el parcheo del sistema operativo y la seguridad de la infraestructura.

*   **Lo que TÚ haces:** Escribes el código y le dices a Lambda cuánta memoria necesita tu función para ejecutarse.

## 2. ¿Cómo funciona Lambda? (Arquitectura Basada en Eventos)

Lambda no está encendido permanentemente esperando solicitudes. Se ejecuta a través de un flujo de trabajo:

1.  **El Disparador (Trigger):** Algo sucede en el entorno de AWS. Puede ser que alguien suba una imagen, se añada un mensaje a una cola SQS, un cambio de estado en un juego online, etc.

2.  **La Invocación:** El disparador "despierta" a Lambda y le pasa la información del evento.

3.  **La Ejecución:** Tu código se ejecuta para procesar el evento.

4.  **El Resultado:** Lambda completa la tarea (ej. guarda una imagen redimensionada o registra un mensaje de SQS) y vuelve a "dormirse".

## 3. Características Clave y Límites

*   **Escalado Automático:** Lambda escala automáticamente en función de las cargas o del tráfico de usuarios. Ya sea un evento o miles al mismo tiempo, Lambda crea instancias temporales de tu código para satisfacer la demanda.

*   **Cobro por uso:** Los costes aumentan con el uso. Solo se te cobra por el tiempo dedicado a procesar cada evento (medido en milisegundos). Si la función no se ejecuta, no pagas nada.

*   **Soporte de Lenguajes:** Admite varios lenguajes de forma predeterminada mediante el uso de entornos de ejecución, lenguajes como Java, Python y Node.js. También puedes crear tu propio entorno de ejecución personalizado.

*   **Límite de Tiempo:** La duración máxima de una función Lambda es de **15 minutos**. Si un proceso tarda más de 15 minutos (ej. procesar un vídeo de 4 horas), Lambda *no* es la herramienta adecuada; deberías usar EC2.

---

## 🛠️ Casos Prácticos de Lambda

*   **Procesamiento en tiempo real:** Cambiar el tamaño de la imagen, aplicar filtros y guardarla en un formato optimizado en el momento en que se sube.

*   **Sistemas Backend:** Recuperar datos, ejecutar la lógica de personalización y devolver contenido pertinente para un usuario en una app.

*   **Integración con SQS (Como en la demo):** Configurar Lambda para que lea automáticamente los mensajes de una cola SQS a medida que llegan y los procese (ej. registrar el ID y el texto de cada mensaje).

---

---
→ Volver al índice: [[📂Exploracion de los servicios de computacion/00 - Índice Exploracion de los servicios de computacion|🪐 Exploracion de los servicios de computacion]]
