**Tags:** #aws #datasync #transfer-family #direct-connect #migracion #redes #cloud-practitioner #cp-migracion-de-la-nube

> [!summary] El Concepto Clave
> Mover Terabytes de datos a través de la red de forma manual es lento, inseguro e inestable. AWS te proporciona servicios administrados para automatizar la transferencia de archivos, validar que no se ha corrompido ningún byte por el camino y asegurar que la mudanza digital se haga a máxima velocidad.

---

## 🚀 1. AWS DataSync (El Motor de Migración de Datos masivo)

Si tienes una cantidad gigantesca de datos en tu centro local (o en otra nube) y necesitas pasarlos a Amazon S3 o Amazon EFS, DataSync es tu herramienta.

* **¿Qué hace?** Automatiza y acelera la transferencia de grandes volúmenes de datos. Se encarga del trabajo sucio que normalmente tendrías que programar tú a mano.

* **Características Clave para el examen

    * **Validación de datos:** Comprueba automáticamente que el archivo que llegó a AWS es exactamente idéntico al que salió de tu servidor (integridad).
    * **Limitación de ancho de banda (Bandwidth limiting):** Puedes programarlo para que copie datos despacio durante el día (para no saturar el Wi-Fi de la oficina) y a máxima velocidad por la noche.
    * **Cifrado automático:** Protege los datos mientras viajan por la red.
    
* **Casos de Uso:** Migrar archivos de la empresa, archivar datos fríos en S3 Glacier o replicar datos para copias de seguridad rápidas.

---

## 🗄️ 2. AWS Transfer Family (El Servidor FTP/SFTP Administrado)

Muchas empresas, bancos y sistemas B2B (Business to Business) tradicionales se intercambian archivos todos los días utilizando protocolos antiguos pero muy seguros como **FTP, SFTP o FTPS**. 

* **El Problema:** Mantener un servidor FTP físico encendido y parcheado para que tus clientes te envíen archivos es un dolor de cabeza.

* **La Solución:** **AWS Transfer Family**. Es un servicio completamente administrado.

* **¿Cómo funciona?** Tú creas un servidor SFTP virtual en un par de clics. Tus clientes se conectan a él usando sus programas de siempre (como FileZilla), pero los archivos que suben caen *directamente* en un bucket de **Amazon S3** o en **Amazon EFS**.

* **Palabras clave para el examen:** "Intercambio de archivos con socios", "SFTP", "FTPS", "FTP", "Modernizar transferencia de archivos B2B".

---

## 🔌 3. AWS Direct Connect (El Cable Privado)

* **¿Qué es?** Una conexión de red física y dedicada entre el centro de datos de tu oficina y los centros de datos de AWS.

* **Beneficios para la migración:**
    * **Bypass de Internet:** Tus datos *no* viajan por el Internet público. Es la forma más privada y segura de mover información corporativa confidencial.
    
    * **Ancho de banda estable:** Al ser tu propio cable privado, la velocidad no fluctúa (puedes contratar líneas de 1 Gbps, 10 Gbps o 100 Gbps).
    
    * **Ahorro a gran escala:** Reduce drásticamente los costes de transferencia de red si vas a mover cantidades masivas de datos continuamente.

---

## 🎯 Chuleta Rápida para el Examen

| Si el enunciado menciona... | El servicio correcto es... |
| :--- | :--- |
| Mover terabytes de archivos, **programar la velocidad de red** y validar datos. | **AWS DataSync** |
| Usar protocolos **SFTP, FTPS o FTP** para compartir archivos con clientes. | **AWS Transfer Family** |
| Establecer una **conexión de red privada** que evite el Internet público. | **AWS Direct Connect** |

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
