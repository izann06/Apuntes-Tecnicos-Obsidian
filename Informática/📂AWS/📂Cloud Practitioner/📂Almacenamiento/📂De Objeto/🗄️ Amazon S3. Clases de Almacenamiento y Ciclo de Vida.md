**Tags:** #aws #s3 #storage-classes #glacier #lifecycle #ahorro #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> No todos los archivos valen lo mismo. Una foto que acabas de subir a Instagram la ven miles de personas hoy, pero dentro de 3 años nadie la mirará. AWS te ofrece diferentes "estantes" (Clases de Almacenamiento) en S3: los estantes de acceso rápido son más caros, y los estantes del trastero (archivos fríos) son muy baratos.

---

## 📚 1. Las Clases de Almacenamiento (Los "Estantes")

Amazon S3 tiene diferentes niveles según la frecuencia con la que vayas a consultar los datos y la rapidez con la que necesites acceder a ellos.

### Los Estantes Diarios (Datos Calientes)

* **S3 Standard:** Es el nivel por defecto. Máxima velocidad de acceso, ideal para sitios web dinámicos, aplicaciones móviles y archivos que consultas a diario. *Coste de almacenamiento más alto.*

* **S3 Express One Zone:** 10 veces más rápido que el Standard. Ideal para aplicaciones críticas que necesitan latencia de menos de un milisegundo. Se guarda en una sola Zona de Disponibilidad.

### Los Estantes del Fondo (Acceso Poco Frecuente / IA)

* **S3 Standard-IA (Infrequent Access):** Para datos que no consultas mucho (ej. copias de seguridad mensuales), pero que cuando los necesitas, los necesitas **inmediatamente**. *El almacenamiento es más barato, pero AWS te cobra una pequeña tarifa cada vez que decides abrir o descargar el archivo.*

* **S3 One Zone-IA:** Igual que el anterior, pero en lugar de copiarse en 3 Zonas de Disponibilidad, solo se guarda en 1. *Más barato aún, pero si ese centro de datos arde, pierdes los datos.*

### El Trastero y el Congelador (Archivos Fríos / Amazon Glacier)

* **S3 Glacier Instant Retrieval:** Archivos que casi nunca tocas, pero si un día los piden, se descargan en milisegundos (ej. radiografías médicas antiguas).

* **S3 Glacier Flexible Retrieval:** Copias de seguridad anuales. *Tarda entre minutos y horas en sacar los datos del congelador.*

* **S3 Glacier Deep Archive:** El congelador más profundo y la opción más barata de todo Amazon. Ideal para cumplir leyes que te obligan a guardar recibos durante 10 años. *Tarda hasta 12 horas en devolverte el archivo.*

---

## 🤖 2. S3 Intelligent-Tiering (El Bibliotecario Mágico)

¿Qué pasa si tienes una montaña de datos y no tienes ni idea de qué archivos se usan mucho y cuáles no?

* **¿Qué hace?** Es una clase de almacenamiento con "piloto automático". Tú metes todo ahí y AWS analiza con qué frecuencia accedes a cada archivo. 

* **El Beneficio:** Si ve que no has tocado un archivo en 30 días, lo mueve automáticamente a un estante más barato. Si de repente vuelves a usarlo, lo devuelve al estante rápido. *Optimiza los costes sin que tú muevas un dedo.*

---

## ⏱️ 3. S3 Lifecycle Policies (El Ciclo de Vida)

Si no quieres pagar por el "bibliotecario mágico" (Intelligent-Tiering), puedes crear tus propias reglas automatizadas.

* **Acciones de Transición:** Mueven objetos a un estante más barato cuando pasa el tiempo. *(Ej: "A los 30 días, mover facturas a Standard-IA. A los 90 días, mover a Glacier").*

* **Acciones de Vencimiento:** El botón de autodestrucción. *(Ej: "A los 365 días, eliminar el archivo permanentemente").*

---

## 📊 Chuleta de Examen: ¿Qué estante elegir?

| Escenario / Patrón de Acceso | Clase de S3 Recomendada |
| :--- | :--- |
| Acceso muy frecuente, web activa o apps móviles. | **S3 Standard** |
| Acceso poco frecuente, pero si se pide, debe ser instantáneo. | **S3 Standard-IA** |
| Datos que se pueden recrear fácilmente si se pierden, acceso raro. | **S3 One Zone-IA** |
| "No sé cómo de frecuentemente se va a acceder a esto". | **S3 Intelligent-Tiering** |
| Guardar por ley datos durante 5 años, puedo esperar horas para verlos. | **S3 Glacier Deep Archive** |

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
