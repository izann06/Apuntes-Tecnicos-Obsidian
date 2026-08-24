**Tags:** #aws #redes #vpn #privatelink #direct-connect #arquitectura #cloud-practitioner #cp-redes

> [!summary] El Concepto Clave
> A medida que tu empresa crece, necesitas conectar tu VPC con el exterior de forma segura. Dependiendo de **quién** se conecta, **qué nivel de seguridad** necesitas y **cuánto tráfico** mueves, elegirás una VPN tradicional, un enlace privado interno (PrivateLink) o un cable físico dedicado (Direct Connect).

---

## 🏢 1. AWS Site-to-Site VPN (VPN de Sitio a Sitio)

Ya hablamos de ella cuando explicamos el **VGW (Virtual Private Gateway)**. A diferencia del *Client VPN* (que es para un solo trabajador en su casa), esta VPN conecta **edificios enteros**.

* **¿Qué es?** Es una conexión cifrada (un túnel seguro) que viaja a través del Internet público y une el *router* de tu oficina física (Customer Gateway) con la puerta trasera de tu VPC en AWS (Virtual Private Gateway).

* **La Analogía:** Es un pasadizo blindado que conecta el edificio de tu empresa en Madrid directamente con tu restaurante en AWS. Cualquier empleado que esté dentro del edificio en Madrid puede cruzar el túnel automáticamente.

* **¿Cuándo usarlo?**
    * Tienes una oficina con 50 empleados y todos necesitan acceder a la base de datos de AWS. No vas a instalar *Client VPN* en 50 ordenadores individuales; configuras una *Site-to-Site VPN* en el router principal de la oficina y listo.
    * Necesitas una conexión segura rápida de configurar (se hace en minutos) y económica.
    * *Nota:* Como viaja por Internet, si hay mucho tráfico global, la conexión puede sufrir pequeñas ralentizaciones (latencia variable).

---

## 🚇 2. AWS PrivateLink (El enlace interno ultra-seguro)

Este concepto es nuevo, muy elegante y fundamental para la seguridad moderna.

* **¿Qué es?** Es un servicio que te permite conectar tu VPC de forma privada a otros servicios de AWS (como Amazon S3, DynamoDB o servicios de terceros) **sin que el tráfico salga a Internet**. 

* **El Problema que resuelve:** Imagina que tienes una base de datos ultrasecreta en una Subred Privada (sin Internet Gateway). Esa base de datos necesita guardar una copia de seguridad en Amazon S3. Normalmente, para llegar a S3, tendrías que salir al Internet público y volver a entrar. ¡Pero tu subred es privada, no tiene puerta a la calle!

* **La Solución:** PrivateLink crea una interfaz de red virtual (un enchufe especial) dentro de tu VPC. El tráfico fluye directamente hacia el servicio de AWS a través de la red troncal privada de Amazon, sin asomarse nunca a la calle pública.

* **La Analogía:** Es como un sistema de **tubos neumáticos de correos** interno del edificio. Si tu restaurante (VPC) necesita pedir servilletas al proveedor (Amazon S3), no abres la puerta principal, no sales a la calle ni usas furgonetas. Metes el pedido en el tubo neumático interno del edificio y llega al instante y de forma 100% privada.

* **¿Cuándo usarlo?**
    * Tienes una arquitectura con estrictas normas de seguridad (ej. sector bancario) donde está **prohibido** que los datos viajen por el Internet público.
    * Tienes recursos en subredes privadas que necesitan consumir otros servicios de AWS o aplicaciones SaaS (Software as a Service) de terceros.

---

## 🚀 3. AWS Direct Connect (El cable físico exclusivo)

Es el hermano mayor, rico y musculoso de la *Site-to-Site VPN*.

* **¿Qué es?** Es una conexión de red **física y dedicada** (un cable de fibra óptica real) que va desde tu centro de datos local corporativo hasta las instalaciones de AWS, eludiendo por completo el Internet público.

* **La Analogía:** Es construir una **autopista subterránea privada y asfaltada** que va desde tu sede hasta AWS. Solo tú tienes las llaves. No hay semáforos, no hay otros coches y la velocidad es bestial y siempre constante.

* **¿Cuándo usarlo?**
    * Trabajas con un volumen de datos gigantesco (ej. moviendo Terabytes de vídeos diarios o datos sísmicos) que colapsarían una conexión normal de Internet.
    * Necesitas una **latencia ultrabaja y constante**. En una VPN por Internet la velocidad varía según el día; con Direct Connect, siempre es la misma porque el cable es tuyo.
    * Quieres reducir los costes de transferencia de datos a largo plazo (AWS cobra menos por los datos que salen a través de Direct Connect que por los que salen a través de Internet).
    * *Nota:* Tarda semanas o meses en instalarse (hay que llamar a operarios de telecomunicaciones) y es costoso.

---

## 📊 Tabla Resumen para Exámenes

| Servicio | ¿Viaja por Internet? | ¿Para qué sirve? | Caso de uso principal |
| :--- | :--- | :--- | :--- |
| **Site-to-Site VPN** | **SÍ** (Pero cifrado/seguro) | Conectar toda la red de tu oficina física a AWS. | Rápido de configurar, económico, oficinas estándar. |
| **AWS PrivateLink** | **NO** (Usa la red privada de AWS) | Conectar tu VPC a servicios de AWS o terceros sin IGW. | Seguridad máxima sin exponer recursos al exterior (tubo interno). |
| **Direct Connect** | **NO** (Es un cable físico dedicado) | Conectar tu centro de datos masivo a AWS. | Altísimo ancho de banda, latencia constante, mover Terabytes. |

---

---
→ Volver al índice: [[📂Redes/00 - Índice Redes|🪐 Redes]]
