**Tags:** #aws #documentdb #neptune #aws-backup #mongodb #grafos #cloud-practitioner #cp-bases-de-datos

> [!summary] El Concepto Clave
> "No intentes meter un tornillo con un martillo". AWS tiene bases de datos diseñadas para estructuras de datos muy concretas. Si tienes documentos tipo JSON, usa **DocumentDB**. Si tienes redes sociales o relaciones complejas, usa **Neptune**. Y para proteger todo esto de forma centralizada, usa **AWS Backup**.

---

## 📄 1. Amazon DocumentDB (El hogar de MongoDB)

* **¿Qué es?** Una base de datos NoSQL especializada en gestionar **datos semiestructurados** (como archivos JSON).

* **El Problema:** Tienes una aplicación que ya usa **MongoDB** (una base de datos de documentos muy famosa) y quieres migrar a AWS sin tener que reescribir todo tu código.

* **La Solución:** DocumentDB está diseñado para ser **100% compatible con MongoDB**. Usas tus mismas herramientas y códigos, pero AWS administra el mantenimiento, la escalabilidad y las copias de seguridad.

* **Casos de Uso:** Sistemas de gestión de contenido (CMS), catálogos de productos donde cada producto tiene especificaciones diferentes, y perfiles de usuario.

---

## 🕸️ 2. Amazon Neptune (La Base de Datos de Grafos)

* **¿Qué es?** Una base de datos de **grafos** completamente administrada.

* **El Problema:** Imagina que quieres encontrar en una base de datos a "Los amigos de los amigos de Juan que también han comprado la zapatilla Nike X". En una base de datos relacional (SQL), hacer esos "cruces" de tablas es una pesadilla de rendimiento.

* **La Solución:** Neptune no guarda datos en tablas, guarda **Nodos (Personas/Cosas)** y **Bordes (Relaciones entre ellos)**. Es absurdamente rápido navegando por estas conexiones.

* **Casos de Uso:** * Redes Sociales (Sugerencias de "Personas que quizás conozcas").

 * Motores de Recomendación ("Los clientes que compraron esto también compraron...").

 * Detección de Fraude (Ver si una tarjeta de crédito está vinculada a 50 cuentas falsas).

---

## 🛡️ 3. AWS Backup (El Anillo Único de la Protección)

* **El Problema:** Tienes datos en discos EBS, en carpetas EFS, en bases de datos RDS y en tablas DynamoDB. Cada uno de esos servicios tiene su propio menú para configurar copias de seguridad. Si eres el jefe de seguridad, tienes que ir menú por menú revisando que las copias se están haciendo bien. Es un caos y propenso a errores humanos.

* **La Solución:** **AWS Backup** es un panel de control **centralizado**.

* **¿Qué hace?** Desde una única pantalla, creas una "Política de Copias de Seguridad" (ej. "Haz copia todos los días a las 3 AM y guárdala un mes") y se la aplicas de golpe a todos tus discos, carpetas y bases de datos, sin importar de qué tipo sean.

* **Beneficios Clave:**

 * Unifica todos los procesos de backup fragmentados.

 * Permite la **Copia entre Regiones** (puedes decirle que envíe automáticamente una copia de tus servidores de Madrid a Tokio en caso de desastre).

 * Te genera informes de auditoría instantáneos para demostrar a los reguladores que estás cumpliendo la ley.

---

## 📊 Chuleta Resumen: El "Quién es Quién" de las Bases de Datos

| Si necesitas guardar... | Usa este servicio de AWS |
| :--- | :--- |
| **Tablas relacionales** con SQL rígido (MySQL, Oracle). | **Amazon RDS** o **Amazon Aurora** |
| **Pares Clave-Valor** flexibles con respuesta en milisegundos. | **Amazon DynamoDB** |
| Respuestas en **memoria RAM** (microsegundos) para aliviar a la BD. | **Amazon ElastiCache** |
| **Documentos semiestructurados (JSON)** o compatibilidad con **MongoDB**. | **Amazon DocumentDB** |
| **Relaciones altamente conectadas** (Redes sociales, Fraude). | **Amazon Neptune** |

---

---
→ Volver al índice: [[📂Bases de Datos/00 - Índice Bases de Datos|🪐 Bases de Datos]]
