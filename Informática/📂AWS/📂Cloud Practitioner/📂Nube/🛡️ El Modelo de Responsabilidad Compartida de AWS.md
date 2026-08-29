**Tags:** #aws #seguridad #responsabilidad-compartida #cloud-practitioner #examen #cp-nube

> [!summary] La Regla de Oro
>
> **AWS es responsable de la seguridad DE la nube.**
> **El Cliente es responsable de la seguridad EN la nube.**

---
## 🟢 1. Responsabilidad de AWS: Seguridad DE la nube (Capa Inferior)

AWS actúa como el dueño de un edificio de alquiler. Ellos se encargan de que el edificio no se caiga, de que nadie salte la valla perimetral y de que haya electricidad y agua.

Según el esquema, AWS se hace cargo de la parte física y de red base:

* **Infraestructura Global:** La seguridad física de las Regiones, Zonas de Disponibilidad (AZs) y Ubicaciones Perimetrales. (Tienen guardias, cámaras, control biométrico).

* **Hardware:** Que los discos duros físicos y los procesadores no fallen.

* **El Software Base:** El software que gestiona la Computación, Almacenamiento y Redes a nivel de hipervisor.

> **Ejemplo de examen:** Si un disco duro físico se rompe en un centro de datos de Amazon, es responsabilidad total de AWS cambiarlo y asegurarse de que tus datos no se pierdan.

---

## 🔵 2. Responsabilidad del Cliente: Seguridad EN la nube (Capa Superior)

Tú eres el inquilino del apartamento. Amazon te da una puerta blindada, pero **si tú dejas la llave puesta por fuera**, es tu culpa si te roban.

Según tu esquema, tú SIEMPRE eres responsable de:

* **Tus Datos:** Absolutamente todo lo que subes. (Los datos del cliente).

* **Cifrado del lado del cliente:** Si decides enviar datos cifrados o en texto plano.

* **Tus Contraseñas (IAM):** Quién tiene acceso a qué. 

> **Ejemplo de examen:** Si un hacker borra tus fotos porque tu contraseña de AWS era "123456", es culpa tuya. AWS no gestiona tus contraseñas.

---

## 🧊 3. La Zona Gris: "Varía según el servicio" (Capa Intermedia)

Aquí es donde el examen te pone las trampas. Esta capa cambia dependiendo de qué "tipo" de servicio de AWS estés alquilando. Fíjate en los elementos del medio: Configuración del Sistema Operativo, Plataforma, Red, Cifrado del Servidor...

### Caso A: Usas IaaS (Infraestructura como Servicio) - Ej. Amazon EC2
Si alquilas un servidor virtual "en blanco" (EC2):

* **TÚ** tienes que instalar las actualizaciones de Windows o Linux (Sistema Operativo).

* **TÚ** tienes que configurar el Firewall (Security Groups).

* *Es como alquilar un coche: tú echas la gasolina y tú lo conduces.*

### Caso B: Usas PaaS/SaaS (Servicios Gestionados) - Ej. Amazon RDS o S3
Si alquilas una base de datos ya montada (RDS):

* **AWS** se encarga de actualizar el sistema operativo por ti.

* **AWS** parchea el motor de la base de datos (Ej. actualizar MySQL a la última versión).

* Tú **SOLO** te encargas de tus datos y de quién puede entrar (IAM).

* *Es como ir en taxi: el taxista (AWS) conduce y le echa gasolina, tú solo le dices a dónde ir.*

---

## 📊 Chuleta Rápida para el Examen

| Si en el examen mencionan... | ¿De quién es la responsabilidad? |
| :--- | :--- |
| Guardias de seguridad física del Data Center | **AWS** |
| Configurar reglas de contraseñas de usuarios | **Cliente** |
| Actualizar el Windows de una instancia EC2 | **Cliente** |
| Proteger un Bucket de S3 para que no sea público | **Cliente** |
| Mantener la red eléctrica de una Región | **AWS** |

---

---
→ Volver al índice: [[📂Nube/00 - Índice Nube|🪐 Nube]]
