**Tags:** #aws #aws-health #supervision #mantenimiento #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> **Amazon CloudWatch** vigila el rendimiento de *tus* recursos (ej. si tu servidor está al 90% de capacidad). **AWS Health** te avisa si *los servicios de infraestructura de AWS en sí* están fallando o van a sufrir cambios que te afecten (ej. "Un cable de fibra óptica se ha roto en la Región de París y tu base de datos podría ir lenta").

---
## 🩺 1. ¿Qué es AWS Health?

Es la fuente oficial y de referencia sobre el estado operativo de la nube de AWS. Te envía tres tipos de alertas principales para que puedas tomar medidas proactivas:

1. **Eventos de servicio (Incidentes):** Averías, interrupciones o problemas de rendimiento actuales en la infraestructura general de AWS.

2. **Cambios planificados (Mantenimiento):** Avisos con antelación de que Amazon va a realizar tareas de mantenimiento en el hardware físico donde se alojan tus máquinas, permitiéndote prepararte o migrar recursos temporalmente.

3. **Notificaciones de la cuenta:** Alertas específicas de seguridad, vulnerabilidades o problemas administrativos vinculados a tu cuenta.

---

## 🖥️ 2. AWS Health Dashboard (El Panel de Control)

Es la pantalla donde visualizas toda esta información. Su mayor ventaja es que te ofrece una vista **personalizada**: no te inunda con notificaciones de los cientos de servicios que tiene AWS, sino que filtra el ruido y *solo* te muestra los eventos que afectan a los recursos que tú tienes desplegados en ese momento.

* **La API de AWS Health (Dato de Examen):** Puedes consultar este panel mediante programación (API) para automatizar respuestas o enviar alertas directamente al sistema de tickets de tu empresa. *Ojo: el acceso a esta API solo está disponible si tienes contratado el plan **AWS Premium Support**.*

---

## 🎯 3. La Trampa del Examen: El Cuarteto de la Supervisión

Con este servicio completamos la familia de herramientas operativas. Si en el examen te preguntan qué usar, aplica esta tabla de asociación rápida:

| La pregunta que necesitas responder... | El servicio correcto es... |
| :--- | :--- |
| *¿Está consumiendo demasiada CPU mi servidor?* | **Amazon CloudWatch** |
| *¿Quién apagó mi servidor web ayer a las 3 AM?* | **AWS CloudTrail** |
| *¿Alguien modificó mi servidor dejándolo sin cifrar?* | **AWS Config** |
| *¿Hay alguna avería general de Amazon hoy que esté afectando a mi servidor?* | **AWS Health Dashboard** |

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
