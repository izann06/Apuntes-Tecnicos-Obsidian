**Tags:** #aws #s3 #almacenamiento #objetos #buckets #seguridad #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> Amazon S3 (Simple Storage Service) es un servicio de almacenamiento de *objetos*. No guardas archivos en carpetas tradicionales, sino que metes "Objetos" (archivos de cualquier tipo) en "Buckets" (cubos). Es infinitamente escalable, Serverless (sin servidor) y ofrece una durabilidad extrema.

---

## 📦 1. Conceptos Fundamentales (Objetos y Buckets)

### Los Buckets (Los Cubos)

* **¿Qué son?** El contenedor principal donde guardas cosas. (Como el directorio raíz).

* **Regla de Oro:** El nombre de un bucket debe ser **ÚNICO A NIVEL MUNDIAL** en todo AWS (como un nombre de dominio web). Nadie en el mundo puede tener un bucket llamado `mis-fotos` si tú ya lo has registrado.

* **Límite de Capacidad:** No hay límite. Puedes almacenar una cantidad prácticamente ilimitada de objetos en un bucket.

### Los Objetos (Los Archivos)

* **¿Qué son?** La unidad fundamental (una foto, un documento de texto, un vídeo de 4K, un archivo de Excel).

* **Composición:** Tienen los datos en sí, metadatos y una **Clave (Key)** que es el nombre único del archivo dentro del bucket.

* **Límite de Tamaño:** El tamaño de un solo objeto puede ser desde 0 bytes hasta **5 Terabytes**.

---

## 💎 2. Los Superpoderes de S3

### A. La Durabilidad de los 11 Nueves

AWS promete una durabilidad del **99,999999999%** para S3.

* *¿Qué significa?* Si guardas 10.000.000 de objetos en S3, estadísticamente solo perderías 1 objeto cada 10.000 años. 

* *¿Cómo lo logran?* S3 copia automáticamente tus archivos en múltiples instalaciones de hardware separadas dentro de una misma Región.

### B. Control de Versiones (Versioning)

Puedes activarlo para protegerte de **borrados accidentales**. Si un empleado sube un archivo nuevo que sobrescribe uno antiguo, S3 guarda ambas versiones, permitiéndote restaurar la antigua con un clic.

### C. URLs Pre-firmadas

Si quieres compartir un archivo privado con alguien temporalmente, puedes generar una URL pre-firmada que caduca en un tiempo determinado (ej. 15 minutos). Después de ese tiempo, el enlace deja de funcionar.

---

## 🛡️ 3. Seguridad: "Privado por Defecto"

Esta es la regla más estricta de S3: **Todo lo que subes es PRIVADO de forma predeterminada.** Solo el creador puede verlo. Si quieres que otros lo vean, debes configurar permisos.

### El Bloqueo de Acceso Público (Block Public Access - BPA)

Es un "botón de pánico" de seguridad. Si el Bloqueo de Acceso Público está activado a nivel de cuenta o de bucket, **nadie en Internet podrá ver tus archivos**, incluso si has configurado políticas que digan lo contrario. Es la causa número uno de problemas cuando la gente intenta hacer una web pública con S3.

### Políticas de Bucket (Bucket Policies)

Son documentos (en formato JSON) que se adjuntan al bucket para definir reglas estrictas de seguridad. 

* *Ejemplo:* "Permitir que cualquier persona del mundo lea las fotos, pero solo permitir que el departamento de finanzas borre archivos".

---

## 🎯 4. Casos de Uso (Para qué SÍ y para qué NO sirve S3)

| Casos Ideales (SÍ usar S3) | Casos Incorrectos (NO usar S3) |
| :--- | :--- |
| Guardar copias de seguridad masivas. | Alojar una base de datos relacional activa (usa RDS). |
| Alojar páginas web *estáticas* (HTML, CSS, Imágenes). | Alojar una web dinámica (PHP, Node.js) que requiere CPU (usa EC2). |
| Lagos de datos (Data Lakes) y análisis de Big Data. | Almacenar el disco de arranque de un sistema operativo (usa EBS). |
| Repositorio de medios (Netflix o Spotify guardando vídeos/música). | Archivos que cambian constantemente y necesitan latencia baja extrema. |

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
