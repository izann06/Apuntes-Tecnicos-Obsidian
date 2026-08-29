**Tags:** #aws #fsx #almacenamiento #windows #lustre #hpc #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> Si Amazon EFS es la "carpeta compartida" exclusiva para servidores Linux, **Amazon FSx** es la familia de sistemas de archivos compartidos para *todo lo demás*. Te permite lanzar sistemas de archivos de alto rendimiento compatibles con plataformas específicas que ya usas en tu empresa (como Windows) sin tener que administrar los servidores físicos.

---

## 🆚 ¿Por qué existe FSx si ya tenemos EFS?

El problema de EFS es que habla un idioma que Windows no entiende bien de forma nativa (el protocolo NFS para Linux). Si una empresa lleva 20 años usando servidores de archivos de Windows y decide migrar a AWS, reescribir todo para que funcione en Linux sería una pesadilla. 

**FSx resuelve esto.** AWS te dice: *"No cambies tu código. Dime qué sistema de archivos usabas en tu oficina y yo te monto uno igualito en la nube, pero 100% administrado por mí"*.

---

## 🗂️ Los 4 Sabores de Amazon FSx

Amazon FSx no es un solo sistema, es un "paraguas" que cubre 4 opciones diferentes. En el examen, **cada opción tiene unas palabras clave (triggers) muy claras**:

### 1. Amazon FSx para Windows File Server

* **¿Qué es?** Un servidor de archivos compartido nativo de Windows.

* **Palabras Clave en Examen:** "Migrar cargas de trabajo de Windows", "SQL Server", "Escritorios virtuales de Windows", "Protocolo SMB".

### 2. Amazon FSx para Lustre

* **¿Qué es?** (Lustre viene de *Linux + Cluster*). Es un sistema de archivos diseñado para una **velocidad bruta y masiva**. Se usa cuando los ordenadores tienen que procesar millones de datos por segundo.

* **Palabras Clave en Examen:** "Machine Learning (ML)", "Computación de Alto Rendimiento (HPC)", "Procesamiento de vídeo/multimedia", "Análisis de Big Data".

### 3. Amazon FSx para NetApp ONTAP

* **¿Qué es?** NetApp es una marca muy famosa de almacenamiento en el mundo empresarial. Esta opción te da un entorno ONTAP en la nube.

* **Palabras Clave en Examen:** "Migrar cargas de trabajo de NetApp", "Continuidad de negocio con ONTAP".

### 4. Amazon FSx para OpenZFS

* **¿Qué es?** Un sistema de archivos avanzado que ofrece un rendimiento altísimo y se accede mediante el protocolo NFS (como EFS, pero más rápido y con características del sistema ZFS).

* **Palabras Clave en Examen:** "Migrar cargas de trabajo de ZFS", "Pruebas de desarrollo rápidas".

---

## 🌟 Beneficios Generales

1. **Infraestructura Administrada:** Tú no instalas Windows ni actualizas el antivirus del servidor; AWS gestiona los parches y las copias de seguridad por debajo.

2. **Integración Transparente:** Las aplicaciones de tu empresa no notan que están en la nube; para ellas, es exactamente el mismo disco duro que tenían en la oficina física.

3. **Rentable:** Tiene opciones de organización por niveles (mueve los archivos que no usas a "estantes" más baratos automáticamente, como hace S3).

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
