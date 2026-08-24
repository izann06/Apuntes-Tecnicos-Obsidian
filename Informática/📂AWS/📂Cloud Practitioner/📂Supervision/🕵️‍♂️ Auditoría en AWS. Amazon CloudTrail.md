**Tags:** #aws #cloudtrail #auditoria #conformidad #api #trazabilidad #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> En AWS, absolutamente todo lo que haces (hacer clic en un botón de la consola, usar la terminal, o que un servicio hable con otro) es, por debajo, una **llamada a la API**. **AWS CloudTrail** es el servicio que graba un registro inmutable de *todas* esas llamadas. Responde a la pregunta fundamental de cualquier auditoría: **¿Quién hizo qué, cuándo y desde dónde?**

---
## 📖 1. El Historial de Eventos (La Caja Negra)

Cuando ocurre un desastre (por ejemplo, alguien borró la base de datos de producción), CloudTrail es el primer lugar al que acudes para buscar al culpable o entender el error.

Cada evento registrado en CloudTrail te da esta información detallada:

* **¿Quién?** (El usuario IAM o el Rol exacto que ejecutó la acción).
* **¿Qué?** (La acción de la API, ej. `TerminateInstances` o `DeleteTable`).
* **¿Cuándo?** (La marca de tiempo exacta).
* **¿Desde dónde?** (La dirección IP de origen).
* **¿Cuál fue el resultado?** (¿Se permitió la acción o se denegó por falta de permisos?).

*Dato:* CloudTrail guarda automáticamente los últimos **90 días** de eventos de administración de forma totalmente **gratuita** en la consola.

---

## 🗄️ 2. Registros y Seguridad (Para la Conformidad)

Si tu empresa maneja tarjetas de crédito (PCI) o datos médicos (HIPAA), la ley te obliga a guardar registros de auditoría durante años, no solo 90 días.

* **El Destino:** Puedes configurar CloudTrail para que empaquete todos esos registros y los envíe de forma continua a un bucket de **Amazon S3** para almacenamiento a largo plazo.

* **Validación de Integridad:** Para demostrar a un juez o auditor que nadie ha manipulado o borrado un registro para ocultar sus huellas, CloudTrail incluye una función matemática que crea un "sello a prueba de manipulaciones" en los archivos de registro.

---

## 🧠 3. CloudTrail Insights (El Detective Automático)

* **¿Qué es?** Es una función avanzada que utiliza Machine Learning para analizar tus registros.

* **El Problema:** Generas millones de registros al día. Un humano no puede leerlos todos para encontrar algo raro.

* **La Solución:** Insights aprende cuál es tu "comportamiento normal" (ej. normalmente enciendes 5 servidores al día). Si de repente un usuario intenta encender 500 servidores en un minuto o la tasa de errores de API se dispara, Insights genera una alerta de comportamiento anómalo.

---
## 🥊 4. La Trampa Clásica del Examen: CloudWatch vs. CloudTrail

AWS siempre intenta confundirte en el examen poniendo estas dos opciones juntas. Esta es la regla de oro para no fallar nunca:

| Si la pregunta menciona... | La respuesta es... |
| :--- | :--- |
| **Rendimiento**, métricas, uso de CPU, estado del sistema o crear **alarmas automáticas**. | **Amazon CloudWatch** ("Watch" = Vigilar la salud) |
| **Auditoría**, llamadas a la API, historial de la cuenta, trazabilidad, "quién hizo este cambio", conformidad legal. | **AWS CloudTrail** ("Trail" = Seguir el rastro/huellas) |

### CloudTrail Simulator

![[🕵️‍♂️ Auditoría en AWS. Amazon CloudTrail.png]]

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
