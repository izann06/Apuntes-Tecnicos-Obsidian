**Tags:** #aws #alta-disponibilidad #multi-az #multi-region #cloudfront #route53 #cloud-practitioner #cp-infraestructura-global

> [!summary] El Concepto Clave
> Las cosas fallan, es un hecho. La clave en AWS es diseñar **arquitecturas redundantes** (tener copias de respaldo listas para entrar en acción) para que, si un centro de datos o una región entera se cae, tus usuarios ni se enteren.

---
## ⚖️ 1. Los 3 Pilares de la Infraestructura en la Nube

Para entender los beneficios de AWS, es vital diferenciar estos tres conceptos que suelen aparecer en el examen:

* **Alta Disponibilidad (High Availability):** La capacidad del sistema para funcionar de forma continua sin fallar. Si un componente se rompe, la aplicación sigue viva gestionando el error automáticamente (sin tiempo de inactividad significativo).

* **Agilidad:** La capacidad técnica de tu empresa para adaptarse rápidamente. Puedes modificar, experimentar y desplegar nuevos servicios en minutos en lugar de meses.

* **Elasticidad:** La capacidad del sistema para **escalar vertical u horizontalmente de forma automática** (crecer o encogerse) respondiendo en tiempo real a los cambios en la demanda.

---

## 🛡️ 2. Estrategias de Redundancia

Para lograr esa Alta Disponibilidad, desplegamos nuestros recursos en varios niveles:
### A. Despliegue Multi-AZ (Múltiples Zonas de Disponibilidad)

* **¿Qué es?** Desplegar tu aplicación en varios centros de datos distintos *dentro de la misma Región*. 

* **Ventaja:** Si una Zona de Disponibilidad (AZ) sufre un corte de luz o un desastre, el tráfico cambia automáticamente a tu AZ de respaldo. Los clientes no notan la diferencia.

* **Beneficios extra:** Recuperación rápida ante desastres y continuidad del negocio.

### B. Despliegue Multi-Región

* **¿Qué es?** El nivel máximo de paranoia (y seguridad). Replicas tu infraestructura en dos partes del mundo (ej. París y Tokio).

* **Ventaja:** Si todo un país/región entera se desconecta, tu sistema hace una conmutación por error (*failover*) a la otra región.

---

## ⚡ 3. La Red Periférica (Edge Network) y sus Servicios

Aparte de las Regiones y las AZ, AWS tiene miles de minicentros repartidos por el mundo llamados **Ubicaciones Periféricas (Edge Locations)**. No sirven para montar grandes servidores, sino para acelerar la entrega a los usuarios finales.

En estas ubicaciones viven servicios específicos de red:

### 🚀 Amazon CloudFront (La Red de Entrega de Contenido - CDN)

* **¿Qué hace?** Sirve contenido (imágenes, vídeos, datos, APIs) desde la ubicación periférica más cercana al usuario.

* **El Beneficio:** Reduce drásticamente la latencia. Si alguien en España pide un meme que está alojado en EE. UU., CloudFront guarda una copia en el punto de disponibilidad de Madrid para que los siguientes usuarios españoles lo descarguen instantáneamente.

* Ejemplo: 

	* **Petición:** Un usuario en Argentina pide una imagen de tu web (`foto.jpg`).
	 
	- **Miss (Fallo de caché):** CloudFront mira en su servidor de Buenos Aires y ve que no tiene la foto.
	 
	- **Búsqueda:** CloudFront viaja hasta tu servidor (en España), coge la foto y se la lleva a Buenos Aires.
	 
	- **Caché:** CloudFront le entrega la foto al usuario y **se guarda una copia** en el disco duro de Buenos Aires.
	 
	- **Hit (Acierto de caché):** Cuando otro usuario en Argentina pide la misma `foto.jpg`, CloudFront ya no viaja a España. Se la entrega directamente desde el caché local en **milisegundos**. 
	
- El tiempo que se queda en CloudeFront lo decides con un valor llamado TTL(Time to Live) y le asignas el tiempo que corresponda.

### 🗺️ Amazon Route 53

* **¿Qué es?** Es el servicio de **DNS** (Sistema de Nombres de Dominio) de AWS. 

* **¿Qué hace?** Traduce las URLs legibles por humanos (ej. `www.tu-cafeteria.com`) en las direcciones IP numéricas que entienden las máquinas (ej. `192.0.2.44`). También dirige el tráfico de forma inteligente hacia la región más sana o más cercana. Es decir, se encarga de que si eres de España te diriga a una región cercana y no a una que está en la otra punta del mundo.

---

## 📊 Chuleta

| Concepto AWS | Definición Simple |
| :--- | :--- |
| **Región** | Ubicación geográfica física (país/ciudad) que agrupa múltiples Zonas de Disponibilidad. |
| **Zona de Disponibilidad (AZ)** | Uno o varios centros de datos aislados dentro de una Región para evitar fallos en cadena. |
| **Ubicación Periférica (Edge)** | Minicentro diseñado para almacenar contenido en caché y reducir la latencia (CloudFront). |
| **Outposts** | La opción extrema: Llevar los servicios de AWS físicamente a tu propio centro de datos para latencia cero. |

---

---
→ Volver al índice: [[📂Infraestructura Global/00 - Índice Infraestructura Global|🪐 Infraestructura Global]]
