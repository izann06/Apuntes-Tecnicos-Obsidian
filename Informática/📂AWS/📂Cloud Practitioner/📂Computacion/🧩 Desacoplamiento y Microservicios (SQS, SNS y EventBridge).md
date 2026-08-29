**Tags:** #aws #arquitectura #microservicios #sqs #sns #eventbridge #cloud-practitioner #cp-computacion

> [!summary] El Concepto Core: El Desacoplamiento
> El objetivo principal en la nube es evitar que el fallo de una pieza rompa todo el sistema. Para lograrlo, separamos la aplicación en piezas pequeñas (microservicios) y ponemos un "buffer" o intermediario entre ellas para que no dependan directamente la una de la otra.

---

## 1. El Problema: Acoplamiento Estrecho (Monolito)

* **¿Qué es?** El Componente A le manda datos directamente al Componente B.

* **El Riesgo:** Si el Componente B se apaga, se actualiza o se satura, el Componente A colapsa porque no sabe qué hacer con los datos que tiene en la mano. Todo el sistema se cae.

* **Analogía:** El cajero le da el ticket en mano al barista. Si el barista se va al baño, el cajero no puede atender a nadie más.

## 2. La Solución: Acoplamiento Débil (Microservicios)

* **¿Qué es?** Introducir un intermediario (como una cola de mensajes). El Componente A deja el mensaje ahí y se olvida. El Componente B lo recoge cuando está listo.

* **El Beneficio:** Si el Componente B falla, el Componente A sigue trabajando con normalidad. Los mensajes se guardan a salvo en el intermediario hasta que B vuelva a la vida.

* **Analogía:** El cajero cuelga los tickets en un corcho. Si el barista se va al baño, el cajero sigue atendiendo clientes y llenando el corcho. Cuando el barista vuelve, saca los tickets y empieza a hacer cafés.

---

## 🛠️ Los 3 Servicios de Comunicación en AWS

## 🏢 SQS vs SNS vs EventBridge (Ejemplo Práctico)

**Tags:** #aws #sqs #sns #eventbridge #arquitectura #casos-reales #cp-computacion

> [!abstract] El Resumen Callejero
>
> * **SQS (Cola):** El trabajador que apila tareas para hacerlas a su ritmo (PULL).
>
> * **SNS (Notificación):** El megáfono que grita una alerta a todos a la vez (PUSH).
>
> * **EventBridge (Enrutador):** El recepcionista inteligente que lee el contenido del mensaje y decide a qué departamento enviarlo (ROUTER).

---

## 🛒 El Escenario: Compras unas zapatillas en Amazon

Imagina que acabas de darle al botón de "Comprar" en una tienda online. Mira cómo actúa cada servicio en ese preciso instante:

### 1. Amazon EventBridge (El Cerebro / Recepcionista)

Nada más pulsar "Comprar", la página web emite un evento general al sistema que dice: *"¡Alerta! Se ha creado el Pedido #555. Contiene: Zapatillas Nike. Cliente VIP"*.

* **¿Qué hace en la práctica?** EventBridge recibe este mensaje, lo abre, lo lee y dice: *"Aja, como son zapatillas, envío este mensaje al Almacén de Ropa. Como es VIP, también mando copia al departamento de Atención al Cliente"*. 

* **En la vida real:** Es el sistema de reglas inteligente de la empresa que conecta decenas de departamentos diferentes según lo que pase.

### 2. Amazon SQS (El Buffer del Almacén)

EventBridge le ha mandado el mensaje de tus zapatillas al "Almacén de Ropa". Ese mensaje cae en una cola de SQS.

* **¿Qué hace en la práctica?** El mensaje se queda ahí guardado de forma segura. En el almacén hay 5 robots empacadores (Servidores EC2). Cuando un robot termina un paquete, va a la cola SQS, **coge (Pull)** el mensaje de tus zapatillas y empieza a empaquetarlas. Si de repente hay un pico por el Black Friday y entran 10.000 pedidos, la cola SQS se hace enorme, pero **ningún pedido se pierde**. Los robots irán sacando mensajes a su ritmo hasta vaciar la cola.

* **En la vida real:** Es la bandeja de entrada de tareas pendientes. Ideal para trabajos pesados que tardan un rato en hacerse (como procesar un pago o renderizar un vídeo).

### 3. Amazon SNS (Las Alertas Inmediatas)

El robot termina de empaquetar tus zapatillas y avisa al sistema: *"Paquete listo para envío"*. El sistema manda este aviso a un tema de SNS llamado "Avisos de Envío".

* **¿Qué hace en la práctica?** SNS coge ese mensaje y lo **dispara (Push)** instantáneamente a todos los que estén suscritos. Te manda un SMS a tu móvil, un correo electrónico a tu bandeja de entrada y una notificación a la app del transportista. ¡Pum! A los tres a la vez en un milisegundo. No guarda el mensaje; si tu móvil estaba apagado, no es su problema, él ya lo envió.

* **En la vida real:** Son las notificaciones push de tu móvil, alarmas o emails masivos donde se necesita inmediatez, no almacenamiento.

---

## 📊 La Chuleta Definitiva

| Característica | Amazon SQS (Cola) | Amazon SNS (Notificación) | Amazon EventBridge (Eventos) |
| :--- | :--- | :--- | :--- |
| **Acción Principal** | Almacenar (Buffer) | Difundir (Broadcast) | Enrutar (Filtrar y dirigir) |
| **¿Quién inicia la entrega?**| El receptor **tira** del mensaje (Pull). | AWS **empuja** el mensaje (Push). | AWS **empuja** basado en reglas. |
| **¿Se guardan los mensajes?**| SÍ (hasta 14 días). | NO (se envían y desaparecen). | NO (actúa en tiempo real). |
| **Destinatarios** | 1 mensaje = 1 trabajador. | 1 mensaje = Miles de suscriptores. | 1 evento = Reglas específicas. |

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
