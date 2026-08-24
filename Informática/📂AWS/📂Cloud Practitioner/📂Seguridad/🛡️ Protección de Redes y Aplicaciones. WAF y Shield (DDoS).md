 **Tags:** #aws #seguridad #ddos #shield #waf #firewall #cloud-practitioner

> [!summary] El Concepto Clave
> En Internet, los atacantes no siempre intentan robar datos; a veces solo quieren colapsar tu servidor enviándole millones de peticiones basura para que los clientes reales no puedan entrar. AWS tiene una infraestructura masiva y servicios específicos (Shield y WAF) para absorber y bloquear estos ataques automáticamente.

---
## 🧟 1. Entendiendo la Amenaza: DoS vs. DDoS

Debes distinguir claramente entre estos dos conceptos:

* **Ataque DoS (Denegación de Servicio):** Un *solo* ordenador atacante inunda tu aplicación web con tráfico excesivo. Es fácil de bloquear porque solo tienes que prohibir la entrada a esa única dirección IP.

* **Ataque DDoS (Denegación de Servicio Distribuida):** El atacante infecta miles de ordenadores o dispositivos ajenos (creando un ejército de "bots zombies"). Estos ordenadores, sin que sus dueños lo sepan, atacan tu aplicación **todos a la vez desde miles de lugares diferentes**. Es devastador porque no puedes bloquear una sola IP.

---

## 🏰 2. La Primera Línea de Defensa: Infraestructura de AWS

Antes de contratar servicios extra, la propia arquitectura básica de AWS ya te protege enormemente:

* **Capacidad de las Regiones:** Un ataque DDoS intenta agotar el ancho de banda. La red de una Región entera de AWS es tan absurdamente gigante que es casi imposible que un ataque consiga saturarla.

* **Elastic Load Balancing (ELB):** En lugar de que el ataque golpee tu servidor EC2 directamente, golpea al Balanceador de Cargas. El ELB distribuye y absorbe el impacto.

* **Grupos de Seguridad (Security Groups):** Operan a nivel de red, no a nivel de sistema operativo. Si recibes una avalancha de peticiones por un puerto raro (ej. protocolo UDP que no usas), el Grupo de Seguridad las rechaza en la frontera antes de que lleguen a tocar tu EC2.

---

## 🦸‍♂️ 3. Los Servicios Especializados: Shield y WAF

Cuando la infraestructura básica no es suficiente, entran en juego los servicios de seguridad administrados:

### A. AWS Shield (El Escudo Antidisturbios)

Es un servicio diseñado *específicamente* para absorber y mitigar ataques DDoS. Tiene dos niveles:

* **AWS Shield Standard:** ¡Viene activado por defecto y es **GRATIS**! Protege todos tus recursos de AWS contra los ataques DDoS más comunes de la capa de red. Está integrado con Route 53, CloudFront y ELB.

* **AWS Shield Advanced:** Es la versión de pago (y muy cara). Te da protección contra ataques DDoS ultracomplejos, acceso a un equipo de respuesta rápida de humanos de AWS (DRT) y te reembolsa el dinero si el ataque hizo que tus servidores autoescalaran y te subiera la factura.

### B. AWS WAF (El Guardia de Seguridad Inteligente)

WAF significa *Web Application Firewall*. Mientras que Shield te protege de ataques de fuerza bruta (DDoS), WAF te protege de **ataques de piratas informáticos que intentan engañar a tu web**.

* **¿Cómo funciona?** Inspecciona el contenido de las peticiones HTTP/HTTPS que entran. 

* **Listas de Control de Acceso Web (Web ACLs):** Tú creas reglas. Por ejemplo: *"Bloquea cualquier petición que venga de este país"*, o *"Bloquea las peticiones que contengan código SQL malicioso intentando colarse en mi base de datos (SQL Injection)"*.

---

## 📊 Chuleta Resumen

| Servicio | ¿De qué me protege? | ¿Cuánto cuesta? | Caso de uso típico |
| :--- | :--- | :--- | :--- |
| **AWS Shield Standard** | Ataques DDoS comunes (Fuerza bruta a la red). | **Gratis** (Activado por defecto). | Protección base automática para todos. |
| **AWS Shield Advanced** | Ataques DDoS gigantes y sofisticados. | De pago. | Grandes corporaciones (Bancos, Tiendas enormes). |
| **AWS WAF** | Tráfico web malicioso (Hackers, inyecciones de código, bots). | De pago (Por reglas). | Filtrar IPs específicas, bloquear países o patrones de hackeo web. |

---

---
→ Volver al índice: [[📂Seguridad/00 - Índice Seguridad|🪐 Seguridad]]
