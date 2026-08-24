**Tags:** #aws #migracion #migration-hub #application-migration #discovery-service #cloud-practitioner #cp-migracion-de-la-nube

> [!summary] El Concepto Clave
> Mudarse a la nube requiere herramientas especializadas para cada etapa del camino. AWS proporciona utilidades para calcular los costes financieros (**Migration Evaluator**), mapear la infraestructura oculta (**Application Discovery Service**), centralizar el control estratégico (**Migration Hub**) y ejecutar el traslado automatizado de los servidores (**Application Migration Service**).


---

## 🧭 1. Fase de Evaluación (Assess): El Consultor Financiero

### 📊 Migration Evaluator (Evaluador de la Migración)

* **¿Qué es?** Un servicio de evaluación guiado por datos que ayuda a construir el **Caso de Negocio** inicial antes de gastar un solo euro en la nube.

* **Función Principal:** Analiza el inventario local actual (hardware y licencias de software) y proyecta estimaciones de costes detalladas y realistas en AWS.

* **Beneficios Clave:**
    * Elimina las conjeturas mostrando múltiples escenarios de migración optimizados para reducir costes.
    * Identifica oportunidades para reutilizar licencias de software existentes (**BYOL**), disminuyendo el gasto total de adquisición.

---

## 🗺️ 2. Fase de Traslado (Mobilize): El Plan de Ataque

### 🕵️‍♂️ AWS Application Discovery Service

* **¿Qué es?** El detective de la infraestructura. Se encarga de descubrir de forma automatizada qué hay dentro de los servidores del centro de datos local

* **Función Principal:** Recopila datos de configuración, rendimiento histórico y, lo más importante, **mapea las conexiones y dependencias** entre servidores y bases de datos.

* **Caso de Uso:** Saber exactamente qué servidores hablan con cuáles para diseñar un plan de migración seguro, evitando romper aplicaciones por el camino. Se integra nativamente con *Migration Hub*.

### 🕹️ AWS Migration Hub (El Centro de Mando)

* **¿Qué es?** Un portal centralizado y único que permite realizar el seguimiento integral de todo el proceso de migración.

* **Función Principal:** Proporciona una **vista unificada** del progreso desde la fase de descubrimiento hasta la ejecución final, sin importar qué herramientas específicas de AWS o de socios de la APN se estén utilizando.

* **Beneficio Clave:** Su uso es **completamente gratuito**; solo se paga por los recursos de infraestructura individuales que se lancen en AWS.

---

## 🏗️ 3. Fase de Migración y Modernización: La Mudanza Real

### 🚚 AWS Application Migration Service (AWS MGN)

* **¿Qué es?** El servicio técnico principal de mudanza automatizada para trasladar servidores físicos, virtuales o basados en otras nubes hacia AWS.

* **Función Principal:** Realiza una replicación continua de los servidores a nivel de bloque. Permite que las operaciones de la empresa sigan funcionando con total normalidad durante la copia.

* **Beneficios Clave:**
    * **Tiempo mínimo de inactividad (Downtime):** El corte final para pasar a la nube se realiza en cuestión de minutos.
    * **Modernización en vuelo:** Permite aplicar optimizaciones automáticas a las aplicaciones durante el proceso de migración.

---

## 🎯 Chuleta de Examen: Emparejamientos Rápidos

| Si la pregunta busca... | La herramienta exacta es... | Analogía de Mudanza |
| :--- | :--- | :--- |
| Crear el **caso de negocio financiero** y optimizar licencias. | **Migration Evaluator** | El perito que calcula el presupuesto del camión y cajas. |
| Descubrir inventario local y **mapear dependencias** de red. | **AWS Application Discovery Service** | El inspector que etiqueta qué cables van conectados a cada caja. |
| **Rastrear el progreso** de múltiples herramientas en un solo panel. | **AWS Migration Hub** | El jefe de obra con la lista de tareas verificando qué está hecho. |
| Migrar servidores enteros con **mínimo tiempo de inactividad**. | **AWS Application Migration Service** | Los operarios que cargan, transportan y colocan los muebles de forma automatizada. |

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
