**Tags:** #aws #gobernanza #control-tower #service-catalog #license-manager #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> A medida que una empresa crece, darle libertad total a los empleados para crear servidores es un caos de seguridad y facturación. La Gobernanza te permite establecer reglas predefinidas para automatizar la creación de cuentas, limitar qué servicios se pueden usar y controlar las licencias de software de terceros.

---
## 🗼 1. AWS Control Tower (El Alcalde de la Nube)

Si **AWS Organizations** es la estructura (las carpetas), **AWS Control Tower** es el servicio de automatización que te construye el edificio entero siguiendo los planos oficiales.

* **El Problema:** Tienes que crear 50 cuentas nuevas para 50 equipos distintos. Configurar a mano CloudTrail, IAM y AWS Config en cada una para que sean seguras es lento y propenso a errores.

* **La Solución:** Control Tower crea automáticamente un entorno de múltiples cuentas llamado **Landing Zone (Zona de Aterrizaje)** que ya viene configurado con las mejores prácticas de seguridad de AWS desde el minuto cero.

* **Los Guardarrailes (Guardrails / Controles):** Es su característica principal. Son reglas obligatorias. 

 * *Preventivos:* Evitan que hagas algo mal (ej. "Nadie puede apagar CloudTrail en ninguna cuenta").

 * *Detectivos:* Te avisan si algo se desconfigura (ej. "Avisar si alguien crea un disco sin cifrar").
 
* **Panel Central:** Te da un resumen visual para ver qué cuentas cumplen las reglas y cuáles no.

---
## 🛒 2. AWS Service Catalog (La Máquina Expendedora de TI)

* **El Problema:** Un desarrollador necesita un servidor EC2 para hacer pruebas, pero el equipo de seguridad no quiere darle permisos de Administrador para evitar que lance un servidor gigante que cueste 5.000€ al mes o que lo deje abierto a Internet.

* **La Solución:** El equipo de seguridad crea un "producto" (ej. un servidor EC2 pequeño, barato y con el antivirus ya instalado) y lo pone en el **Service Catalog**.

* **Cómo funciona:** El desarrollador entra a AWS, va al Service Catalog y ve una lista de recursos aprobados. Hace clic en "Desplegar" y AWS lanza el servidor por él.

* **Beneficio Clave (Examen):** Fomenta el **autoservicio ágil**. Los desarrolladores no tienen que abrir un ticket de soporte y esperar 3 días para tener un servidor, y la empresa se asegura de que todo lo que se lanza cumple las normas corporativas.

---

## 📜 3. AWS License Manager (El Auditor de Software)

Cuando usas software que no es de Amazon (como Windows Server, bases de datos Oracle o SAP), necesitas pagar licencias. 

* **El Modelo BYOL (Bring Your Own License):** AWS te permite "Traer Tu Propia Licencia" que ya compraste a Microsoft u Oracle y usarla en servidores de AWS (como EC2 Dedicated Hosts) para ahorrar mucho dinero.

* **El Problema:** Si tu contrato dice que solo puedes tener 100 servidores con Windows, y en AWS lanzas 105, estás incumpliendo el contrato y Microsoft puede ponerte una multa millonaria.

* **La Solución:** **AWS License Manager**.

* **¿Qué hace?** Le introduces las reglas de tu contrato legal. El servicio rastrea y administra el uso de esas licencias en todas tus cuentas de AWS.

* **El Superpoder:** Puedes configurarlo para aplicar **límites estrictos (hard limits)**. Si un empleado intenta lanzar el servidor Windows número 101, License Manager bloquea el lanzamiento para evitar que incumplas la ley.

---

## 📊 Chuleta Resumen: Herramientas de Gestión a Escala

| Servicio de AWS | Su función principal para el examen |
| :--- | :--- |
| **AWS Organizations** | Agrupar cuentas para **facturación consolidada** y aplicar SCPs. |
| **AWS Control Tower** | **Automatizar la creación** de un entorno multi-cuenta seguro con *guardarrailes*. |
| **AWS Service Catalog** | Catálogo de **recursos aprobados (autoservicio)** para estandarizar la infraestructura. |
| **AWS License Manager** | Administrar el modelo **BYOL** y evitar pasarte del límite de tus licencias. |

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
