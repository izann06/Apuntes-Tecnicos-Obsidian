**Tags:** #aws #dms #sct #bases-de-datos #migracion #cloud-practitioner #cp-migracion-de-la-nube

> [!summary] El Concepto Clave
> Mover una base de datos requiere precisión. AWS proporciona **AWS Database Migration Service (DMS)** para transportar los datos de forma segura sin apagar el sistema original, y la **Herramienta de conversión de esquemas (AWS SCT)** para traducir el formato de los datos si decides cambiar de marca de base de datos durante el viaje.

---

## 🚚 1. AWS Database Migration Service (AWS DMS)

Es el motor principal de la mudanza. Esencialmente, es un servidor de replicación que se coloca entre tu base de datos antigua y la nueva.

* **El Superpoder:** La base de datos de origen **permanece completamente operativa** durante la migración. DMS copia los datos en segundo plano y sincroniza cualquier cambio nuevo que ocurra durante el proceso, garantizando un tiempo de inactividad (downtime) casi nulo

* **Casos de uso:** Mover una base de datos local a Amazon RDS o Amazon Aurora.
    * Replicación continua de datos (mantener dos bases de datos sincronizadas).
    * Migrar bases de datos del tamaño de un Terabyte a un coste muy bajo.

---

## 🔄 2. Tipos de Migración de Bases de Datos

Para el examen, debes tener clarísima la diferencia entre estos dos escenarios:

### A. Migración Homogénea (Mismo Motor)

* **¿Qué es?** Migrar de una base de datos a otra de la **misma marca o tipo**.

* **Ejemplo:** De un servidor *Oracle* local a un *Amazon RDS for Oracle* en la nube; o de un *MySQL* local a un *Amazon RDS for MySQL*.

* **Herramienta necesaria:** Solo necesitas **AWS DMS**.

### B. Migración Heterogénea (Distinto Motor)

* **¿Qué es?** Migrar cambiando la marca o el tipo de base de datos (generalmente para ahorrar costes de licencias comerciales).

* **Ejemplo:** Pasar de una base de datos comercial cara como *Oracle* o *Microsoft SQL Server* hacia una base de datos de código abierto en la nube como *Amazon Aurora* o *PostgreSQL*.

* **El Problema:** Como son motores distintos, hablan idiomas distintos. Tienen estructuras de tablas (esquemas) y tipos de datos incompatibles.

* **Herramientas necesarias:** Necesitas **AWS SCT** (para traducir la estructura) + **AWS DMS** (para mover los datos).

---

## 🗣️ 3. Herramienta de Conversión de Esquemas de AWS (AWS SCT)

Si decides hacer una migración heterogénea (cambiar de motor), AWS SCT entra en juego *antes* que DMS.

* **¿Qué es un esquema?** Es el plano arquitectónico de tu base de datos (cómo se estructuran las tablas, los tipos de campos y las reglas).

* **¿Qué hace AWS SCT?** Automatiza la traducción del esquema y del código de la base de datos de origen (ej. un procedimiento almacenado en Oracle) a un formato compatible con el motor de destino (ej. Amazon Aurora). 

* **El Informe de Viabilidad:** SCT no solo traduce, sino que te genera un informe estimando cuánto esfuerzo manual requerirá la conversión de aquellas partes del código que son demasiado complejas para traducirse automáticamente.

---

## 🎯 Chuleta Rápida

| Escenario del Cliente | Solución AWS Requerida |
| :--- | :--- |
| Quiero mover mi base de datos Oracle a AWS **sin tiempo de inactividad**. | **AWS DMS** |
| Quiero migrar de MySQL local a MySQL en AWS. | **Migración Homogénea -> Solo AWS DMS** |
| Quiero migrar de Microsoft SQL Server (Comercial) a Amazon Aurora (Open Source). | **Migración Heterogénea -> AWS SCT + AWS DMS** |
| Necesito **convertir mis tablas, vistas y funciones** a un nuevo motor. | **AWS SCT** |

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
