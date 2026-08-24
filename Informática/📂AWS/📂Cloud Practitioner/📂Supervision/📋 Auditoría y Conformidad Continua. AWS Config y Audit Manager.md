**Tags:** #aws #config #audit-manager #auditoria #conformidad #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> Cumplir las normas no es algo que haces una vez y te olvidas. Necesitas un policía interno que vigile que nadie cambie las reglas de seguridad de tus servidores (**AWS Config**) y un asistente administrativo que recopile automáticamente las pruebas de que haces las cosas bien para enseñárselas a los inspectores externos (**AWS Audit Manager**).

---
## 📏 1. AWS Config (El Policía de las Configuraciones)

* **¿Qué es?** Es un servicio que registra y evalúa continuamente las configuraciones de tus recursos de AWS comparándolas con las "reglas" que tú le hayas marcado.

* **El Problema:** Creas una regla en tu empresa que dice: *"Ningún disco duro (EBS) puede estar sin cifrar"*. El lunes todos cumplen. El miércoles, un desarrollador crea un disco duro nuevo sin cifrar por las prisas.

* **La Solución:** AWS Config detecta ese cambio casi al instante. Marca ese recurso como "No conforme" (Non-compliant) y te envía una alerta.

* **El Superpoder (Remediación Automática):** No solo te avisa, sino que puedes configurarlo para que actúe. Si Config detecta un disco sin cifrar, puede lanzar una acción automática para cifrarlo inmediatamente sin intervención humana.

* **Palabras clave para el examen:** "Evaluar el estado deseado", "Inventario de configuraciones", "Remediación automática", "Auditoría continua de recursos".

---

## 🗂️ 2. AWS Audit Manager (El Recopilador de Pruebas)

* **¿Qué es?** Es un servicio diseñado específicamente para reducir el esfuerzo manual masivo que suponen las auditorías legales y de industria.

* **El Problema:** Cuando viene un auditor del gobierno a revisar tu empresa (ej. para la ley HIPAA de sanidad o el RGPD europeo), te pide *pruebas* de que los datos están seguros. Antes, los equipos informáticos pasaban semanas haciendo capturas de pantalla de las configuraciones y juntándolas en documentos de Word.

* **La Solución:** Audit Manager tiene "marcos de trabajo" (frameworks) preconfigurados con las leyes más famosas. **Recopila las evidencias de forma automática y continua** directamente desde tus cuentas de AWS y te genera un informe final formateado, inmutable y listo para entregar al auditor.

* **Palabras clave para el examen:** "Recopilación automatizada de pruebas", "Evaluación de riesgos continua", "Informes listos para auditoría", "Mapeo con normativas del sector".

---

## 🎯 Chuleta Definitiva: El Cuarteto de la Auditoría

En el examen intentarán confundirte entre estos 4 servicios. Si memorizas esto, no fallarás ninguna:

| Herramienta de AWS | ¿Qué pregunta responde o qué problema soluciona? |
| :--- | :--- |
| **AWS CloudTrail** | *¿Quién hizo qué y cuándo?* (Graba el historial de todas las llamadas a la API de los usuarios). |
| **AWS Config** | *¿Están mis recursos configurados como yo mandé?* (Vigila configuraciones técnicas, como puertos abiertos o discos sin cifrar). |
| **AWS Artifact** | *Necesito el certificado de que los centros de datos de Amazon son legales.* (Descarga de documentos PDF y contratos BAA). |
| **AWS Audit Manager** | *Necesito pruebas de mis propios servidores para dárselas a mi auditor.* (Automatiza la recolección de capturas/evidencias de tu uso de AWS). |

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
