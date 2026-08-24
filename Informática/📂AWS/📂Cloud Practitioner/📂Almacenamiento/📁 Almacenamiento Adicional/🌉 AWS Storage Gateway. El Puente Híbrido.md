**Tags:** #aws #storage-gateway #nube-hibrida #almacenamiento #backup #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> AWS Storage Gateway es el "puente" que conecta los servidores físicos de tu oficina (on-premises) con el almacenamiento infinito de AWS. Permite que tus aplicaciones locales sigan funcionando como siempre, pero guardando los datos (o las copias de seguridad) en la nube por detrás de las cámaras.

---
## 🏗️ ¿Por qué usar Storage Gateway? (Beneficios)

Si un sistema físico funciona, no lo rompas. Storage Gateway te permite modernizarte sin cambiar tu forma de trabajar:

1.  **Integración sin problemas:** Tus aplicaciones locales no notan la diferencia. Creen que están guardando archivos en un disco duro normal de la oficina.

2.  **Almacenamiento en caché local:** Guarda los archivos que más usas en el servidor de tu oficina (para que abran al instante), pero manda los archivos viejos y pesados a la nube para no ocupar espacio físico.

3.  **Optimización de costes:** Usas el almacenamiento barato de AWS (como S3 o Glacier) para archivos históricos o copias de seguridad, en lugar de comprar más discos duros físicos.

---

## 🗂️ Los 3 Tipos de Puertas de Enlace

Storage Gateway tiene 3 tipos dependiendo de lo que quieras guardar (Archivos, Bloques de disco o Cintas). 

### 1. Amazon S3 File Gateway (Para Archivos)

* **¿Qué hace?** Tus servidores locales lo ven como una carpeta de red compartida normal. Pero cuando metes un archivo ahí, **se sube automáticamente como un objeto a Amazon S3**.

* **El Truco:** Mantiene una "caché" local de los archivos recientes. Si abres un Excel de ayer, se abre rapidísimo desde el servidor físico. Si abres un Excel de hace 3 años, lo descarga de S3.

* **Caso de uso:** Compartir archivos locales respaldados en la nube.

### 2. Volume Gateway (Para Discos Duros / Bloques)

* **¿Qué hace?** Presenta discos duros virtuales (volúmenes iSCSI) a tus servidores locales. Los datos de estos discos se respaldan en AWS como **Instantáneas de Amazon EBS**.

* **Tiene 2 modos de funcionamiento:**

    * *Modo Caché (Cached Volumes):* Los datos reales viven en la nube. Tu oficina solo guarda una copia temporal de lo que más se usa. (Ahorras mucho espacio físico).
    
    * *Modo Almacenado (Stored Volumes):* TODO el disco vive en tu oficina físicamente, pero hace una copia de seguridad asíncrona hacia la nube. (Ideal si necesitas que todo el disco esté disponible sin Internet).

### 3. Tape Gateway (Para Cintas de Copia de Seguridad)

* **¿Qué hace?** Reemplaza las librerías de cintas magnéticas físicas (esas que se metían en cajas fuertes).

* **¿Cómo funciona?** Tu software de copias de seguridad antiguo (Veeam, Backup Exec) cree que está grabando en una cinta de plástico real, pero en realidad está grabando en una **"cinta virtual"** que se guarda en Amazon S3 y se archiva en S3 Glacier.

* **Caso de uso:** Eliminar el almacenamiento físico de cintas sin cambiar el software que lleva usando la empresa 15 años.

---

## 📊 Chuleta Rápida de Correspondencias

| Lo que usas en tu oficina local   | El tipo de Storage Gateway | Dónde termina en AWS              |
| :-------------------------------- | :------------------------- | :-------------------------------- |
| **Archivos y Carpetas (NFS/SMB)** | S3 File Gateway            | **Amazon S3** (Objetos)           |
| **Discos duros (iSCSI)**          | Volume Gateway             | **Amazon EBS** (Snapshots)        |
| **Software de Cintas magnéticas** | Tape Gateway               | **S3 Glacier** (Cintas Virtuales) |

## Explicación para ver la diferencia con usar S3 O EBS

Por que no usar S3 directamente Amazon S3 no funciona como una carpeta normal de tu ordenador. Funciona a traves de peticiones web o APIs. Si tu empresa tiene un programa de facturacion antiguo instalado en los ordenadores de la oficina, ese programa solo sabe guardar archivos en un disco duro normal o en una carpeta compartida de red. No tiene ni idea de como conectarse a internet para hacer una peticion API a Amazon S3.

Aqui es donde entra S3 File Gateway. Actua como un traductor simultaneo. Lo instalas en tu oficina y este servicio le dice a tu programa de facturacion que el es una carpeta compartida normal y corriente. El programa guarda la factura ahi sin quejarse. Entonces, el File Gateway coge esa factura, la traduce al idioma web de AWS y la sube a S3. Has conseguido usar el almacenamiento infinito de S3 sin tener que pagar a unos programadores para que reescriban tu programa de facturacion.

Por que no usar EBS directamente Amazon EBS es un disco duro virtual que vive de forma estricta dentro de los centros de datos de Amazon. Una regla fundamental de AWS es que un disco EBS solo se puede enchufar a un servidor EC2 que este exactamente en su misma zona de disponibilidad. Literalmente es imposible conectar un disco EBS a un servidor fisico que tienes en tu oficina. Estan demasiado lejos y la tecnologia no lo permite de forma directa.

Volume Gateway soluciona esta limitacion fisica. Crea un disco duro virtual local en la red de tu oficina. Tu servidor fisico se conecta a ese disco y funciona de maravilla a velocidad local. Por detras, Volume Gateway se encarga de tomar fotografias de ese disco y enviarlas de forma segura por internet hacia AWS, guardandolas con el formato de instantaneas de EBS.

En resumen, no usas S3 o EBS directamente porque tus servidores fisicos locales no hablan el mismo idioma que la nube o no estan en el mismo edificio que los equipos de Amazon. Storage Gateway es el cable adaptador que pones en medio para que tus equipos antiguos de la oficina puedan usar la nube moderna de AWS.

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
