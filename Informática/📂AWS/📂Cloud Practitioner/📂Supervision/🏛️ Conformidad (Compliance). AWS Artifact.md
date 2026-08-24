**Tags:** #aws #conformidad #compliance #artifact #auditoria #legal #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> La conformidad consiste en demostrar legalmente que cumples con las reglas de tu industria (ej. no sacar datos de ciudadanos europeos fuera de la UE para cumplir con el GDPR). Dado que tú no puedes meter a un auditor físico en los centros de datos de Amazon, AWS te da los certificados de aprobación oficiales ya hechos a través del servicio **AWS Artifact**.

---
## ⚖️ 1. La Herencia de Seguridad (El Modelo de Responsabilidad Compartida)

El mayor beneficio legal de usar AWS es la "Herencia". 
Si tú quieres montar un servidor para guardar historiales médicos (HIPAA) en el sótano de tu oficina, tienes que pagar a un auditor para que verifique que la cerradura de tu sótano es segura, que los cables no están expuestos y que el aire acondicionado funciona. 

Al usar AWS, **heredas los controles de infraestructura**. Como AWS ya ha sido auditado y aprobado por terceros para cumplir con HIPAA a nivel mundial, tú te saltas toda la auditoría del "Sótano y los Cables" y solo tienes que demostrar que has cifrado tus propios datos. Te ahorra muchísimo dinero y tiempo legal.

---

## 📜 2. AWS Artifact: El Portal Legal

Es el portal gratuito donde descargas la documentación legal de AWS. Se divide en dos partes:

### A. AWS Artifact Reports (Informes)

* **¿Qué es?** Es una biblioteca de informes de auditoría hechos por empresas externas (Terceros) que validan que AWS cumple con miles de normativas globales.

* **El Caso de Uso:** El regulador del gobierno te visita y te dice: *"Demuéstrame que la nube donde guardas tus datos cumple con el estándar de seguridad ISO 27001"*. Entras a Artifact, descargas el PDF del auditor externo que confirma que AWS es nivel ISO 27001, y se lo entregas.

### B. AWS Artifact Agreements (Acuerdos)

* **¿Qué es?** El lugar donde firmas contratos legales con AWS.

* **El Caso de Uso:** Eres un hospital. Según la ley HIPAA de EE. UU., si compartes datos médicos con un proveedor tecnológico (como AWS), debes firmar un "Acuerdo de Socio Comercial (BAA)". Entras a AWS Artifact Agreements, firmas el contrato digitalmente y ya estás cubierto legalmente. Si usas *AWS Organizations*, puedes firmar un acuerdo maestro que cubra todas las sub-cuentas de tu empresa.

---

## 🌍 3. Residencia de Datos y Conformidad

Un punto crítico legal es "Dónde están los datos". 

* **Tú eres el único dueño.**

* **AWS nunca moverá tus datos de la Región en la que los guardaste** (ej. si guardas datos en la región de París, no se replicarán automáticamente a la región de Tokio). Esto es vital para cumplir con leyes como el RGPD (GDPR) europeo.

---

## 📊 Chuleta Resumen: El Triángulo de la Gobernanza

Esta es la forma rápida de diferenciar los servicios de esta área en las preguntas del examen:

| Si la pregunta te pide... | Servicio correcto |
| :--- | :--- |
| **"Auditar llamadas a la API"** o "¿Quién encendió este servidor?" | **AWS CloudTrail** |
| **"Descargar informes de cumplimiento"** o "Firmar un acuerdo legal con AWS". | **AWS Artifact** |
| **"Supervisar el uso de CPU"** o "Crear alarmas si falla el rendimiento". | **Amazon CloudWatch** |

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
