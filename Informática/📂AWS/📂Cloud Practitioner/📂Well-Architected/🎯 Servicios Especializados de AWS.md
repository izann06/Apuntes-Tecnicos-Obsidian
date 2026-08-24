**Tags:** #aws #desarrollo #business-apps #euc #iot #ci-cd #cloud-practitioner #cp-well-architected

> [!summary] El Concepto Clave
> Además de la infraestructura básica (servidores, redes y almacenamiento), AWS ofrece un catálogo de herramientas diseñadas para nichos muy específicos de la industria. Se dividen en cuatro grandes bloques: herramientas de automatización y depuración para **desarrolladores**, aplicaciones de **gestión empresarial**, entornos de **trabajo remoto** para usuarios finales, y conectividad para **dispositivos inteligentes (IoT)**.

---

## 💻 1. Servicios de Desarrollo (Developer Tools)

Diseñados para optimizar la creación, despliegue y mantenimiento de código.

### A. AWS CodeBuild & AWS CodePipeline (El dúo de CI/CD)

* **AWS CodeBuild:** Un servicio de Integración Continua (CI) que compila el código fuente, ejecuta pruebas unitarias y genera paquetes listos para desplegar. Solo pagas por los minutos de computación que usas.

* **AWS CodePipeline:** Un servicio de Entrega Continua (CD) que automatiza las fases de compilación, prueba y despliegue del software cada vez que hay un cambio en el repositorio.

* *Diferencia rápida:* CodeBuild *hace el trabajo físico* (compilar/probar) y CodePipeline es el *director de orquesta* que mueve el código a través de las fases.

### B. AWS X-Ray (El Detective del Rendimiento)

* **¿Qué es?** Una herramienta de seguimiento (tracing) y depuración en entornos distribuidos.

* **¿Para qué sirve?** Te ayuda a **visualizar el comportamiento de la aplicación** en tiempo real. Si la web va lenta o da errores, X-Ray dibuja un mapa que rastrea las peticiones HTTP e identifica exactamente qué componente (base de datos, microservicio o API) está causando el cuello de botella.

### C. AWS AppSync & AWS Amplify

* **AWS AppSync:** Servicio administrado para crear APIs **GraphQL**. Permite interactuar, manipular y combinar datos de múltiples fuentes de AWS utilizando una única consulta.

* **AWS Amplify:** Un framework para desarrollar aplicaciones móviles y web *Full-Stack* de forma rapidísima. Te ayuda a configurar el Frontend y conectarlo con el Backend (autenticación, base de datos) con un esfuerzo mínimo de gestión de infraestructura.

---

## 🏛️ 2. Servicios de Aplicaciones Empresariales (Business Apps)

Soluciones empaquetadas listas para usar que resuelven necesidades de comunicación del día a día de un negocio.

* **Amazon Connect:** Un centro de contacto (call center) en la nube **potenciado por IA**. Ofrece de forma nativa enrutamiento automatizado de llamadas, grabación de conversaciones y analítica avanzada para el servicio al cliente.

* **Amazon Simple Email Service (Amazon SES):** Una plataforma de correo electrónico masiva, escalable y muy económica. Se integra en el código de tus apps para enviar correos transaccionales (ej. confirmaciones de compra) o de marketing (boletines).

---

## 🖥️ 3. Computación para el Usuario Final (End-User Computing)

Permiten a los departamentos de TI desplegar herramientas de trabajo remoto seguro sin gestionar hardware local costoso.

* **Amazon WorkSpaces:** Un servicio de **Escritorios Virtuales (VDI)** en la nube completamente administrado. El empleado puede acceder a su ordenador corporativo completo (con sus programas y archivos) desde cualquier dispositivo con Internet.

* **Amazon AppStream 2.0:** En lugar de transmitir todo el sistema operativo, **transmite aplicaciones de escritorio individuales** directamente a través de un navegador web, convirtiendo software tradicional en soluciones SaaS sin reescribir código.

* **Amazon WorkSpaces Secure Browser:** Un navegador web corporativo remoto y protegido. Ideal para que los empleados accedan de forma segura a webs privadas de la empresa o herramientas SaaS sin necesidad de una VPN compleja ni de instalar agentes en sus equipos personales.

---

## 🔌 4. Internet de las Cosas (IoT)

* **AWS IoT Core:** El servicio central que permite **conectar miles de millones de dispositivos físicos** (sensores, enchufes Wi-Fi, cámaras de seguridad, wearables) con las aplicaciones en la nube de AWS de forma totalmente segura.

* **Seguridad:** Utiliza autenticación mutua y cifrado de extremo a extremo (E2E) para que nadie pueda hackear o interceptar las señales de los dispositivos inteligentes.

---

## 📊 Chuleta Resumen para el Examen (Evita las trampas)

AWS suele mezclar estos nombres en las preguntas de opción múltiple para confundirte. Aplica esta tabla de asociación directa:

| Si la pregunta te pide... | El servicio exacto es... | 🚨 Cuidado con confundirlo con... |
| :--- | :--- | :--- |
| **Depurar, analizar rendimiento** y visualizar mapas de llamadas. | **AWS X-Ray** | *Amplify* (que es para construir el esqueleto de la app, no para depurar). |
| Centro de atención al cliente con **IA, llamadas y grabación**. | **Amazon Connect** | *SES* (que es exclusivamente para enviar emails masivos). |
| Transmitir **aplicaciones de escritorio sueltas** por el navegador. | **Amazon AppStream 2.0** | *WorkSpaces* (que te da el escritorio virtual/ordenador entero). |
| Conectar **sensores, enchufes inteligentes o wearables** físicos. | **AWS IoT Core** | *AppStream 2.0* (que es para software de usuario, no para cacharros físicos). |

---

---
→ Volver al índice: [[📂Well-Architected/00 - Índice Well-Architected|🪐 Well-Architected]]
