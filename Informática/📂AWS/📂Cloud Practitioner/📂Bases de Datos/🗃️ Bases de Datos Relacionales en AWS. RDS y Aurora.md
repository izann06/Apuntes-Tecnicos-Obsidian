**Tags:** #aws #base-de-datos #rds #aurora #sql #relacional #cloud-practitioner #cp-bases-de-datos

> [!summary] El Concepto Clave
> Las bases de datos relacionales organizan la información en tablas (filas y columnas) que se conectan entre sí (como un Excel avanzado). Hablan el lenguaje SQL. En AWS, puedes instalar tu base de datos a mano en un EC2, usar **Amazon RDS** para que AWS te la administre, o usar **Amazon Aurora** para conseguir un rendimiento brutal en la nube.

---

## 🏗️1. Tres formas de tener una Base de Datos SQL en AWS

Si tu empresa tiene una base de datos MySQL o SQL Server, y quiere llevarla a AWS, tiene 3 niveles de adopción:

### Nivel 1: EC2 (Hazlo tú mismo - Lift & Shift)

* **¿Qué es?** Alquilas un servidor virtual (EC2) vacío, instalas tú mismo el motor de la base de datos (ej. Oracle) y lo configuras.

* **Pros:** Tienes control absoluto sobre el sistema operativo y las configuraciones internas.

* **Contras:** Tú eres responsable de actualizar el antivirus, aplicar parches de seguridad, hacer las copias de seguridad a mano y configurar la alta disponibilidad.

### Nivel 2: Amazon RDS (Servicio Administrado)

* **¿Qué es?** Amazon Relational Database Service (RDS). Le dices a AWS: *"Quiero una base de datos PostgreSQL de tamaño X"*. AWS te la entrega lista para usar.

* **La Ventaja (Responsabilidad Compartida):** AWS gestiona la infraestructura subyacente, el sistema operativo, aplica los parches de software automáticamente y realiza copias de seguridad sin que tú hagas nada. Tú solo te preocupas de tus datos y de ponerles contraseñas.

* **Motores compatibles:** MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server y Amazon Aurora.

* **Alta Disponibilidad:** Tiene opción de **Despliegue Multi-AZ**. Si el servidor principal falla, AWS cambia automáticamente el tráfico a una copia de seguridad en otra Zona de Disponibilidad.

### Nivel 3: Amazon Aurora (El Ferrari de la Nube)

* **¿Qué es?** Es un motor de base de datos relacional creado por Amazon, diseñado *específicamente* para la nube.

* **La Ventaja (Rendimiento Extremo):** Es hasta **5 veces más rápido** que MySQL estándar y 3 veces más rápido que PostgreSQL, costando mucho menos que las bases de datos comerciales de gama alta (como Oracle).

* **El Superpoder de la Replicación:** Aurora guarda automáticamente **6 copias de tus datos** distribuidas en **3 Zonas de Disponibilidad** distintas (incluso si no se lo pides). Es prácticamente indestructible.

* **Almacenamiento Mágico:** El disco duro crece solo automáticamente (hasta 128 TB) a medida que metes datos. No tienes que preocuparte del espacio libre.

---

## 🛠️ Conceptos Clave de Amazon RDS

### Copias de Seguridad y Snapshots

RDS hace copias de seguridad automáticas (que puedes restaurar a cualquier minuto exacto de los últimos 35 días). Además, puedes hacer **Snapshots manuales** (fotografías completas de la base de datos) que duran para siempre.

### Réplicas de Lectura (Read Replicas)

* **El Problema:** Tienes una tienda online. Mientras unos pocos empleados están insertando productos nuevos (Escribiendo), miles de clientes están buscando y mirando el catálogo (Leyendo). El servidor se satura.

* **La Solución:** Creas una "Réplica de Lectura". Es una copia exacta de tu base de datos que se sincroniza en tiempo real, pero a la que **solo se le puede hacer preguntas (leer), no se puede escribir en ella**. Diriges a los miles de clientes hacia la réplica, aliviando la carga del servidor principal.

---

## 📊 Chuleta Resumen

| Característica | Base de Datos en EC2 | Amazon RDS | Amazon Aurora |
| :--- | :--- | :--- | :--- |
| **Administración** | Tú administras TODO (OS, parches, backups). | AWS administra el OS y los backups. | AWS administra todo con auto-escalado de disco. |
| **Motores disponibles** | Cualquier software del mundo. | 6 motores (MySQL, SQL Server, etc.). | Compatible con MySQL y PostgreSQL. |
| **Durabilidad de datos** | La configuras tú a mano. | Multi-AZ opcional (Tú lo activas). | 6 copias en 3 AZs por defecto. |
| **Rendimiento** | Depende del tamaño de EC2 y del disco. | Estándar de la industria. | Nivel empresarial (+5x velocidad). |

---

---
→ Volver al índice: [[📂Bases de Datos/00 - Índice Bases de Datos|🪐 Bases de Datos]]
