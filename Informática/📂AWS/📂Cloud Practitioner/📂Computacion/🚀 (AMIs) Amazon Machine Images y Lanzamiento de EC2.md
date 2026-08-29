**Tags:** #aws #ec2 #ami #user-data #ssh #cloud-practitioner #cp-computacion

> [!summary] El Proceso de Creación
> Lanzar un EC2 es como pedir un ordenador a la carta. Debes elegir el sistema operativo (AMI), el hardware (Tipo de instancia), la seguridad de acceso (Par de claves), las reglas de red (Security Groups) y el disco duro (Almacenamiento).

---

## 💿 1. Amazon Machine Images (AMI)

Una AMI es una **imagen de máquina virtual preconfigurada** que contiene el sistema operativo, el servidor de aplicaciones y las aplicaciones. Esto ayuda a iniciar instancias de EC2 rápidamente con el software y la configuración deseados.

**¿Qué incluye una AMI?**

* El Sistema Operativo (Linux, Windows, macOS).

* Software adicional preinstalado (ej. un servidor web Apache o bases de datos).

* Configuración base de almacenamiento y permisos.

### Las 3 Formas de obtener una AMI

1. **AMI de AWS (Quick Start):** Plantillas oficiales de Amazon (como *Amazon Linux 2*). Son seguras, gratuitas (solo pagas la instancia) y listas para usar.

2. **AMI Personalizadas (Custom AMIs):** Las creas tu. Esto sirve por si tienes ya una instancia creada con su web, base de datos, lógica... Y quieres clonarla para meterla en otro servidor, en vez de crear todo de nuevo simplemente vas a la consola de AWS, haces clic derecho sobre la instancia que quieres copiar y le das a **"Crear Imagen"**. AWS detiene el servidor un segundo, le hace una "fotocopia" a todo el disco duro tal y como lo dejaste, y guarda ese archivo mágico. 

3. **AWS Marketplace:** Si crear tu propia AMI te da pereza o necesitas un software súper complejo de nivel empresarial, usas el Marketplace. La tienda de apps. Empresas de terceros (como Cisco, Palo Alto o WordPress) venden AMIs con su software premium ya instalado y configurado para que tu puedas usarlo.

> [!important] El Superpoder de la AMI: Repetibilidad
> Si tienes una AMI personalizada de tu servidor web, puedes lanzar 1.000 instancias exactamente idénticas en 5 minutos. Esto garantiza que todos los servidores se comportan igual y no hay errores humanos de instalación.

---

## 🔑 2. El Par de Claves (Key Pair)

AWS no te da una contraseña normal para entrar a los servidores Linux por primera vez, usa criptografía asimétrica para mayor seguridad (SSH).

* **Clave Pública:** AWS la guarda y se la asigna a la instancia EC2 al crearla.

* **Clave Privada (archivo.pem o.ppk):** Te la descargas TÚ a tu ordenador y tienes que saber donde está. 

	* **Regla:** Solo el ordenador que tenga la Clave Privada podrá conectarse remotamente a esa instancia. *¡Si pierdes este archivo, puedes perder el acceso al servidor!*

Aunque hoy en día no es necesario usar **SSH** de hecho hay una alternativa mejor y más segura. Se trata del **Session Manager**.

El SSH y Session Manager son el cable invisible que conecta lo que escribo con el cerebro del servidor de AWS.

#### 🛡️ ¿Por qué el Session Manager es mejor que el SSH tradicional?

Session Manager resuelve los tres grandes dolores de cabeza de la seguridad en la nube:

1. **Sin Puertos Abiertos:** Con SSH, tienes que abrir el puerto 22 al mundo (o a tu IP) en el Security Group. Con Session Manager, puedes cerrar **todos** los puertos de entrada. La conexión se hace de forma interna a través de la red de AWS.
 
2. **Sin Gestión de Claves (.pem):** Ya no tienes que preocuparte por quién tiene el archivo de la llave privada o qué pasa si se pierde. El acceso se controla mediante **políticas de IAM** (tu usuario y contraseña de AWS).
 
3. **Auditoría Total:** Todo lo que escribes en la terminal queda registrado. Puedes guardar los logs (registros) en **Amazon S3** o **CloudWatch Logs** para saber exactamente qué comando ejecutó cada administrador.

Session Manager lo tienes para la consola web y para la terminal mediante un plugin, tendrás que investigar más adelante sobre esto.

## 📊 Comparativa de Experiencia

| **Si usas...** | **¿Dónde escribes?** | **¿Cómo se conecta?** | **¿Es profesional?** |
| ---------------------- | -------------------------- | --------------------------------- | -------------------------- |
| **SSH tradicional** | Tu terminal local | Por el puerto 22 con llave `.pem` | Sí, pero "vieja escuela". |
| **SSM (Vía Web)** | Navegador (Chrome/Firefox) | Interno de AWS (sin puertos) | Sí, para arreglos rápidos. |
| **SSM (Vía Terminal)** | Tu terminal local | Interno de AWS (sin puertos) | **El nivel experto.** |

---

## 📊 Repaso Rápido

| Si necesitas... | ¿Qué herramienta usas en el lanzamiento? |
| :----------------------------------------------- | :---------------------------------------- |
| Elegir que el servidor sea Windows o Linux | **La AMI** |
| Elegir que el servidor tenga 2 CPUs y 4GB de RAM | **El Tipo de Instancia** (ej. `t3.micro`) |
| Conectarte por SSH de forma segura | **El Par de Claves** (Key Pair) |
| Conectarte por Session Manager | Consola web o termina (Plugin) |

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
