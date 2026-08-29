**Tags:** #aws #trusted-advisor #iam #access-analyzer #seguridad #optimizacion #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> Mantener una nube eficiente y segura es un trabajo constante. AWS te proporciona dos "consultores automáticos": **AWS Trusted Advisor**, que analiza toda tu cuenta en busca de formas de ahorrar dinero, mejorar el rendimiento o tapar agujeros de seguridad; e **IAM Access Analyzer**, que se enfoca quirúrgicamente en tus políticas de acceso para garantizar que nadie tenga más permisos de los necesarios (Mínimo Privilegio).

---

## 🤵 1. AWS Trusted Advisor (Tu Consultor Automatizado)

* **¿Qué es?** Un servicio de inspección automatizado que escanea tu infraestructura en tiempo real y la compara con las mejores prácticas recomendadas por Amazon.

* **¿Cómo funciona?** Te da un informe visual con un sistema de colores tipo semáforo:

 * 🔴 **Rojo:** Acción crítica requerida (ej. Tienes un agujero de seguridad grave).

 * 🟡 **Amarillo:** Recomendación de optimización (ej. Podrías ahorrar dinero aquí).

 * 🟢 **Verde:** Cumples con la mejor práctica.

### 📊 Las 6 Categorías de Inspección (¡Esencial conocerlas!)

1. **Optimización de Costes (Cost Optimization):** Te avisa si estás pagando de más. *(Ejemplo: Instancias EC2 infrautilizadas que deberías apagar, o discos EBS antiguos sueltos que sigues pagando pero nadie usa).*

2. **Seguridad (Security):** Busca debilidades que te expongan a ataques. *(Ejemplo: No tienes MFA activado en el usuario raíz, o tienes un puerto de base de datos abierto a todo Internet).*

3. **Rendimiento (Performance):** Revisa que tus servicios funcionen de la forma más fluida posible.

4. **Tolerancia a Fallos (Fault Tolerance):** Comprueba si tu sistema sobrevivirá a un desastre. *(Ejemplo: Te avisa si no has hecho copias de seguridad de tus discos EBS en mucho tiempo).*

5. **Límites de Servicio (Service Limits):** AWS limita cuántos recursos puedes crear por defecto para protegerte de gastos locos. Este check te avisa si estás al 80% de alcanzar el límite de servidores permitidos en tu cuenta.

6. **Excelente Operativa (Operational Excellence):** Evalúa procesos operativos y consistencia.

*Dato de examen:* Todos los clientes tienen acceso gratuito a unas cuantas reglas básicas. Los planes de soporte avanzados (**Business y Enterprise**) desbloquean el catálogo completo con cientos de verificaciones detalladas.

---

## 🔍 2. IAM Access Analyzer (El Guardián del Mínimo Privilegio)

Mientras Trusted Advisor mira la cuenta de forma general, el **Analizador de Acceso de IAM** se pone la lupa para auditar minuciosamente los accesos y los permisos.

* **El Propósito:** Ayudarte a cumplir de forma estricta el **Principio de Mínimo Privilegio**.

* **¿Qué problemas resuelve?**

 * **Análisis de Acceso Externo:** Te avisa inmediatamente si un recurso tuyo (como un bucket de S3) tiene una política que permite que alguien *fuera de tu empresa* pueda entrar a leer o escribir.
 
 * **Validación de Políticas:** Escanea tus políticas escritas en JSON mientras las creas para asegurarse de que no has cometido errores gramaticales o de seguridad informática.
 
 * **Limpieza de Permisos obsoletos:** Analiza los registros históricos y te dice: *"Le diste permiso a Juan para usar 20 servicios, pero en los últimos 90 días solo ha usado 2. Deberías quitarle los otros 18"*.

---

## 📊 Chuleta Resumen para el Examen

| Si la pregunta menciona... | El servicio correcto es... |
| :--- | :--- |
| Escanear la cuenta en busca de **servidores infrautilizados para ahorrar costes**. | **AWS Trusted Advisor** (Optimización de costes) |
| Verificar que el **usuario raíz tiene MFA activado**. | **AWS Trusted Advisor** (Seguridad) |
| Descubrir si un recurso tiene **acceso público o externo no deseado**. | **IAM Access Analyzer** |
| Validar que una **política de IAM cumpla con los estándares de seguridad**. | **IAM Access Analyzer** |

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
