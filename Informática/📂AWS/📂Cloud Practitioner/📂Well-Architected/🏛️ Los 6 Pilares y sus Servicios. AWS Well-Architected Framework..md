**Tags:** #aws #well-architected #arquitectura #servicios #cloud-practitioner #cp-well-architected

> [!summary] El Concepto Clave
> El **AWS Well-Architected Framework** es la guía oficial de buenas prácticas de Amazon. Proporciona un enfoque consistente para evaluar arquitecturas y asegurar que son seguras, rentables, rápidas y sostenibles. AWS proporciona herramientas específicas para cumplir con las reglas de cada uno de estos 6 pilares.

[Image of AWS Well-Architected Framework 6 pillars detailed]

---

## 🏛️ Los 6 Pilares de la Arquitectura (Estructura de Examen)

### 1. Excelencia Operativa (Operational Excellence)

* **¿De qué trata?** Ejecutar y supervisar sistemas para entregar valor empresarial, así como mejorar continuamente los procesos y procedimientos operativos diarios.

* **Conceptos Clave:** Automatización de cambios, despliegues frecuentes y pequeños, integración y entrega continuas (**CI/CD**), y anticiparse a los fallos respondiendo a eventos de forma automática (sin intervención humana).

* **Servicios AWS:**

 * **AWS CloudFormation:** Para desplegar infraestructura mediante código (Infrastructure as Code) y evitar errores manuales.

 * **AWS CodePipeline / CodeBuild:** Para automatizar las tuberías de entrega de software.

 * **Amazon CloudWatch:** Para supervisar la salud de las aplicaciones.

### 2. Seguridad (Security)

* **¿De qué trata?** Proteger la información, los sistemas y los activos, mitigando los riesgos mediante evaluaciones continuas y estrategias de defensa.

* **Conceptos Clave:** Principio de **privilegio mínimo** (dar solo el acceso estrictamente necesario), cifrado de datos (en tránsito y en reposo), trazabilidad completa (saber exactamente quién hizo qué y cuándo) y protección en todas las capas de red.

* **Servicios AWS:**

 * **AWS IAM:** Para gestionar usuarios, roles y políticas de permisos estrictas.

 * **AWS CloudTrail:** Para el registro de auditoría y la trazabilidad de llamadas a la API.

 * **AWS KMS:** Para la gestión de claves y cifrado de datos.

 * **AWS Shield / AWS WAF:** Para repeler ataques DDoS y amenazas web.

### 3. Fiabilidad (Reliability)

* **¿De qué trata?** La capacidad de un sistema para recuperarse de interrupciones en la infraestructura o interrupciones del servicio, garantizando que cumple su función cuando se le necesita.

* **Conceptos Clave:** Recuperación ante desastres (Disaster Recovery), tolerancia a fallos, escalar horizontalmente para aumentar la disponibilidad, y la capacidad de adaptarse a cambios dinámicos en la demanda sin caerse.

* **Servicios AWS:**

 * **Elastic Load Balancing (ELB):** Para distribuir el tráfico y evitar la saturación de un único servidor.

 * **AWS Auto Scaling:** Para añadir o quitar servidores automáticamente según la carga de trabajo.

 * **Amazon Route 53:** Para enrutar a los usuarios hacia infraestructuras de respaldo si el centro de datos principal falla.

### 4. Eficiencia del Rendimiento (Performance Efficiency)

* **¿De qué trata?** Utilizar los recursos informáticos y tecnológicos de forma eficiente para satisfacer los requisitos del sistema, y mantener esa eficiencia a medida que la tecnología evoluciona.

* **Conceptos Clave:** Democratizar tecnologías avanzadas, elegir el tipo de recurso adecuado (la máquina exacta para el trabajo), usar arquitecturas sin servidor (Serverless) y acercar los datos a los usuarios mediante cachés.

* **Servicios AWS:**

 * **Amazon CloudFront (CDN):** Para entregar contenido a nivel mundial con latencia ultrabaja.

 * **Amazon ElastiCache:** Para guardar datos en memoria y acelerar las consultas a bases de datos.

 * **AWS Compute Optimizer:** Para obtener recomendaciones sobre qué tamaño exacto de servidor necesitas.

### 5. Optimización de Costes (Cost Optimization)

* **¿De qué trata?** Evitar gastos innecesarios, comprender exactamente dónde se gasta el dinero y dimensionar correctamente los recursos para maximizar el retorno de la inversión (ROI).

* **Conceptos Clave:** Pagar solo por lo que se utiliza, medir la eficiencia general, aprovechar los modelos de precios con descuento (Spot, Savings Plans) y apagar los recursos inactivos o "huérfanos".

* **Servicios AWS:**

 * **AWS Cost Explorer / AWS Budgets:** Para analizar tendencias de gasto histórico y poner alertas proactivas.

 * **AWS Trusted Advisor:** Para recibir avisos automáticos sobre servidores encendidos que nadie usa.

 * **Amazon EC2 Spot Instances:** Para alquilar servidores sobrantes de AWS con hasta un 90% de descuento.

### 6. Sostenibilidad (Sustainability)

* **¿De qué trata?** Minimizar el impacto ambiental derivado del funcionamiento de las cargas de trabajo en la nube.

* **Conceptos Clave:** Comprender el impacto climático, maximizar la utilización para conseguir una mayor eficiencia energética, reducir el hardware inactivo y adoptar arquitecturas que consuman menos recursos físicos.

* **Servicios AWS:**

 * **AWS Customer Carbon Footprint Tool:** Para calcular las emisiones de carbono que generan tus proyectos.
 
 * **AWS Lambda (Serverless):** Al no tener servidores encendidos 24/7 de forma ociosa, solo consumes la energía exacta durante los milisegundos que dura tu código.

---

## 🛠️ La Herramienta de Evaluación Central

* **Herramienta de AWS Well-Architected:** Es el servicio gratuito en la consola de AWS donde auditas tu arquitectura. Respondes a preguntas clave de estos 6 pilares y el sistema te genera un **informe de estado** con recomendaciones accionables y paso a paso para tapar brechas de seguridad, ahorrar dinero o mejorar el rendimiento.

---

---
→ Volver al índice: [[📂Well-Architected/00 - Índice Well-Architected|🪐 Well-Architected]]
