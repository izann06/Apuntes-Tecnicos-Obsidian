
**Tags:** #aws #migracion #migration-hub #dms #snow-family #cloud-practitioner #cp-migracion-de-la-nube

> [!summary] El Concepto Clave
> Migrar a la nube no es copiar y pegar archivos en una tarde; es un proyecto estratégico para mover activos digitales, servidores y bases de datos desde un entorno local (On-Premises) hacia AWS. Para asegurar el éxito, AWS divide este viaje en **tres fases secuenciales**.

---

## 🧭 Fase 1: Evaluación (Assess)

Antes de tocar ningún servidor, necesitas saber si tiene sentido financiero y operativo dar el salto a la nube.

* **¿Qué se hace?** Se evalúa el estado actual de la empresa, se definen los objetivos de negocio y se desarrolla un Caso de Negocio (Business Case) para justificar la migración.

* **Servicio de evaluación previa:**

    * **Evaluador de la migración (Migration Evaluator):** Te ayuda a crear un caso de negocio basado en datos. Analiza lo que gastas actualmente en tus servidores físicos y proyecta cuánto te costaría (y cuánto ahorrarías) ejecutando esas mismas cargas de trabajo en AWS.

---

## 🗺️ Fase 2: Traslado / Movilización (Mobilize)

Ya tienes la aprobación de la directiva. Ahora necesitas un mapa detallado de todo lo que tienes en tu edificio antes de empezar a empaquetarlo.

* **¿Qué se hace?** Se crea un plan de migración sólido. Es crítico descubrir las interdependencias ocultas (ej. "La web de ventas no se puede migrar antes que la base de datos de usuarios porque están conectadas").

* **Servicios de migración (Descubrimiento y Planificación):**

    * **AWS Application Discovery Service:** Instala agentes en tus servidores físicos para "descubrir" qué aplicaciones tienes instaladas, cuánto rendimiento consumen y cómo se comunican entre sí.
    
    * **AWS Migration Hub:** Es tu **panel central de control**. Te permite realizar un seguimiento del progreso de las migraciones en múltiples herramientas de AWS y de socios desde un único lugar.

---

## 🏗️ Fase 3: Migración y Modernización (Migrate & Modernize)

Es la hora de la verdad. Se ejecutan los planes y los bytes reales empiezan a viajar hacia los servidores de AWS.

* **¿Qué se hace?** Cada aplicación se diseña para la nube, se migra físicamente y se valida que funciona. Posteriormente, se puede "modernizar" (ej. pasar de usar un servidor clásico a usar funciones Serverless).

* **Servicios de migración (Ejecución):**

    * **AWS Application Migration Service:** Permite migrar aplicaciones y servidores enteros (sistemas operativos, bases de datos y aplicaciones) a AWS de forma automatizada y con un tiempo de inactividad casi nulo.
    
    * **AWS Database Migration Service (DMS):** Especializado en mover bases de datos. Su superpoder es que **la base de datos de origen sigue funcionando con normalidad** mientras se copian los datos a AWS, evitando paralizar la empresa.

* **Servicios de transferencia de datos:**

    * **AWS DataSync:** Un servicio de transferencia online que mueve grandes conjuntos de datos (Terabytes) a gran velocidad a través de Internet o Direct Connect hacia servicios como Amazon S3 o Amazon EFS.
    
    * **AWS Transfer Family:** Gestiona de forma segura la transferencia de archivos utilizando protocolos estándar de la industria (SFTP, FTPS, FTP) directamente hacia y desde Amazon S3.
    
    * **Familia AWS Snow:** Para migraciones "offline" (sin Internet). Si tienes Petabytes de datos que tardarían años en subirse por la red, AWS te envía dispositivos físicos (maletines blindados o camiones) para copiar los datos en tu oficina y llevarlos físicamente al centro de datos de Amazon.

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
