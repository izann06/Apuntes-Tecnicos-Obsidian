**Tags:** #aws #cloudwatch #supervision #metricas #alarmas #logs #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> Amazon CloudWatch es el servicio principal de supervisión y observabilidad de AWS. Recopila datos de rendimiento de todos tus recursos (incluso los locales) en tiempo real, permitiéndote ver gráficos, investigar errores pasados y configurar alarmas que tomen decisiones automáticas si algo va mal.

---
## 🏗️ Los 4 Pilares de CloudWatch

CloudWatch no es una sola herramienta, es un conjunto de 4 características que trabajan juntas para darte visibilidad total:

### 1. Métricas (Los Signos Vitales)

* **¿Qué son?** Son las variables numéricas que CloudWatch recopila de tus recursos a lo largo del tiempo. 

* **Ejemplos por defecto:** Uso de CPU de una instancia EC2, tráfico de red entrante, cantidad de datos guardados en un bucket S3.

* **Métricas Personalizadas:** Tú también puedes enviar tus propios números desde tu aplicación (Ej. "Número de cafés vendidos" o "Usuarios registrados hoy").

### 2. Alarmas de CloudWatch (Los Avisos Automáticos)

* **¿Qué son?** Son reglas que tú creas evaluando una métrica. Le pones un "umbral" (un límite).

* **Las Acciones:** Lo verdaderamente poderoso de las alarmas es lo que hacen cuando se disparan. Pueden:

    * Enviar un correo o SMS al administrador usando **Amazon SNS**.
    
    * Activar **Amazon EC2 Auto Scaling** (ej. *"Si la CPU supera el 80% durante 5 minutos, enciende dos servidores nuevos"*).
    
    * Reiniciar o recuperar una instancia EC2 bloqueada.

### 3. Paneles (Dashboards)

* **¿Qué son?** Son pantallas visuales personalizables donde puedes agrupar gráficos de tus métricas más importantes.

* **Beneficio:** Te permiten tener una "vista unificada" de la salud de todo tu sistema en tiempo casi real sin tener que actualizar la página de tu navegador.

### 4. Registros de CloudWatch (CloudWatch Logs)

* **¿Qué son?** Mientras las métricas son números, los registros (logs) son **archivos de texto**. Es el historial escrito de todo lo que hace tu aplicación.

* **Beneficio:** Centraliza todos los registros dispersos de tus servidores en un solo lugar. Si tu aplicación falla a las 3:00 AM, el desarrollador entra a *CloudWatch Logs*, filtra por la palabra "Error" o "Exception" y descubre exactamente qué línea de código falló.

---

## 🚀 La Sinergia

En el examen rara vez te preguntan por CloudWatch de forma aislada. Te lo preguntan en una "cadena de eventos" automatizada. Así es como debes visualizarlo:

1. **Recopilación:** Un servidor (Amazon EC2) está procesando compras y envía su métrica de CPU a **CloudWatch**.

2. **El Problema:** Llega el Black Friday. El uso de CPU sube al 95%.

3. **La Detección:** Una **Alarma de CloudWatch** detecta que se ha superado el umbral del 80%.

4. **La Reacción (Acción Automática):** La alarma avisa a **Amazon SNS** para que envíe un SMS al móvil del gerente.

    * La alarma avisa a **EC2 Auto Scaling** para que lance 3 servidores nuevos inmediatamente para ayudar a soportar el tráfico.

---

## 🎯 Beneficios Directos

* **Reduce el MTTR (Mean Time To Resolution):** Al tener todas las métricas y logs centralizados, los informáticos tardan minutos en encontrar y arreglar un problema, en lugar de horas.

* **Optimiza Recursos (Ahorro):** Si ves en tu panel que un servidor siempre está al 5% de uso, puedes decidir apagarlo o cambiarlo por uno más barato.

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
