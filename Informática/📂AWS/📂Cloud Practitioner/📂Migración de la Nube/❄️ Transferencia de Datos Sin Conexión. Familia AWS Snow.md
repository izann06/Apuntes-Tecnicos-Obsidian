**Tags:** #aws #snowball #snow-family #migracion #offline #edge-computing #cloud-practitioner #cp-migracion-de-la-nube

> [!summary] El Concepto Clave 
> A veces, la forma más rápida de mover Petabytes de datos a la nube no es a través de Internet, sino metiéndolos en un camión. Cuando el ancho de banda es limitado, la ubicación es remota (sin Internet) o el volumen de datos es colosal, AWS te envía a tu oficina dispositivos físicos ultra-resistentes para que copies los datos localmente y se los devuelvas por correo.

## 🚫 1. ¿Por qué usar transferencia sin conexión (Offline)?

En el examen te pondrán casos de uso donde las herramientas en línea (como AWS DataSync) no sirven. Debes elegir la Familia Snow si se cumple alguna de estas condiciones:

1. **Limitaciones extremas de red:** Tienes una conexión a Internet muy lenta y subir los datos tardaría meses o años.
 
2. **Ubicaciones remotas:** Estás en un barco, una plataforma petrolífera, una mina o un entorno militar donde no hay conexión a Internet o es intermitente.
 
3. **Escala masiva:** Tienes docenas de Petabytes o Exabytes de datos.

## 🧰 2. El Protagonista: AWS Snowball Edge (Storage Optimized)

Es el dispositivo físico de AWS más preguntado en el examen para migraciones offline estándar. Es como un disco duro externo gigante, blindado y con inteligencia propia.

- **¿Qué es?** Un dispositivo físico seguro y robusto (soporta golpes, agua y manipulaciones) que AWS te envía por paquetería.
 
- **Storage Optimized (Optimizado para almacenamiento):** Esta versión específica incluye unidades NVMe de altísimo rendimiento, lo que te permite transferir **Gigabytes de datos por segundo** desde tus servidores locales hacia el dispositivo.
 
- **Proceso de migración:**
 
 1. Lo pides desde la consola de AWS.
 
 2. Te llega por mensajería.
 
 3. Lo conectas a tu red local y copias los Petabytes de datos súper rápido.
 
 4. La etiqueta de envío de tinta electrónica se actualiza sola y se lo devuelves a AWS.
 
 5. AWS lo enchufa en su centro de datos y vuelca tu información en **Amazon S3**.
 

## 💻 3. El Superpoder Oculto: Computación Periférica (Edge Computing)

¡Ojo con esto para el examen! La palabra "Edge" (Borde/Periferia) en su nombre no es casualidad.

- **El Problema:** Tienes un barco de investigación en el Ártico grabando datos de los glaciares. No tienes Internet para procesar esos datos en los servidores de AWS.
 
- **La Solución:** Los dispositivos Snowball Edge **tienen capacidad de cómputo**. Puedes ejecutar pequeñas instancias de Amazon EC2 o funciones Lambda directamente _dentro_ de la caja física de Snowball mientras está en el barco. Filtra y procesa los datos en el lugar, y cuando el barco llega a puerto, envías el dispositivo a AWS con el trabajo ya hecho.
 

## 🎯 Chuleta Rápida para el Examen

|Si el enunciado menciona...|La respuesta correcta es...|
|---|---|
|Transferir Petabytes de datos **sin conexión a Internet** o con bajo ancho de banda.|**AWS Snowball Edge** / Familia AWS Snow|
|Dispositivo **robusto y seguro** para migración de datos local.|**AWS Snowball Edge Storage Optimized**|
|Ejecutar código (EC2/Lambda) en **ubicaciones remotas/periféricas** sin conexión.|**AWS Snowball Edge** (Edge Computing)|
|Mover datos muy rápido, pero **tengo buena conexión a Internet**.|**AWS DataSync** (¡No confundir con Snowball!)|

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
