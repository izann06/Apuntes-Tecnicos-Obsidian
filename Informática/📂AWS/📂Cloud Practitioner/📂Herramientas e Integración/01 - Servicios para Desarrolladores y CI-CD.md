#aws #cloud-practitioner #devops #ci-cd

> [!info] Exámenes Relacionados
> Estos servicios pertenecen íntegramente al dominio del **Cloud Practitioner (CLF-C02)** y de DevOps. 
> Tienen poco o ningún peso en el examen de IA Practitioner (AIF-C01), ya que están enfocados puramente en el ciclo de vida del desarrollo de software clásico, integración de aplicaciones y marketing.

---

# 🛠️ Servicios para Desarrolladores, Integración y Móviles

El desarrollo moderno en la nube utiliza prácticas de Integración Continua y Despliegue Continuo (CI/CD). AWS ofrece herramientas nativas para automatizar todo este proceso, así como servicios para comunicar microservicios y conectar con clientes.

## 1. La Suite de CI/CD (Developer Tools)

Piensa en estos servicios como una cadena de montaje de una fábrica de coches (tu código fuente). Cada servicio se encarga de una fase:

- **AWS CodeBuild (Construcción):** Es el servicio que compila el código fuente, ejecuta las pruebas (tests unitarios) y crea paquetes de software listos para ser desplegados. Es totalmente administrado y escala automáticamente según el volumen de trabajo.
- **AWS CodeDeploy (Despliegue):** Es el encargado de coger ese paquete ya compilado y automatizar su instalación y despliegue en cualquier instancia de cómputo (EC2, Fargate, Lambda o incluso servidores On-Premise físicos).
- **AWS CodePipeline (El Orquestador):** Es el director de orquesta. Es un servicio de entrega continua que **automatiza y modela todo el proceso**. Cuando subes un código nuevo (a GitHub o CodeCommit), CodePipeline detecta el cambio, llama a CodeBuild para que lo compile, y luego llama a CodeDeploy para que lo lance a producción.

## 2. Pruebas de Aplicaciones Móviles

- **AWS Device Farm:**
  - **Qué es:** Es un servicio de pruebas de aplicaciones que te permite testear tus apps (iOS, Android y web) de forma simultánea en **miles de dispositivos móviles físicos reales** (no emuladores) alojados de forma segura en los centros de datos de AWS.
  - **Enfoque de examen:** Si la pregunta menciona "probar aplicaciones en dispositivos físicos reales en la nube", la respuesta es 100% Device Farm.

## 3. Integración y Orquestación de Microservicios

- **AWS Step Functions:**
  - **Qué es:** Es un orquestador visual de flujos de trabajo (workflows) sin servidor. Permite secuenciar funciones AWS Lambda y otros servicios de AWS en procesos de negocio complejos.
  - **Enfoque de examen:** Es la respuesta correcta cuando se necesita "orquestar múltiples microservicios", crear "flujos de trabajo visuales" o procesos con "estados y ramificaciones lógicas" (ej. un flujo de pago donde si la tarjeta falla va por la rama A, y si funciona va por la B).

## 4. Comunicación y Marketing

- **Amazon Pinpoint:**
  - **Qué es:** Es el servicio de comunicación de marketing bidireccional y análisis de clientes de AWS.
  - **Enfoque de examen:** Se usa para interactuar con clientes a través de múltiples canales (SMS, correo electrónico, notificaciones push móviles o notificaciones in-app). Si la pregunta menciona "campañas de marketing dirigidas", "segmentación de usuarios" o "notificaciones push para campañas", la respuesta correcta es Pinpoint. No confundir con SNS (que es más para notificaciones de sistema o de pub/sub técnico).
