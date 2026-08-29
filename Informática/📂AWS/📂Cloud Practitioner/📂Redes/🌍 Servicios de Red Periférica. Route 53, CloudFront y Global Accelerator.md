**Tags:** #aws #redes #edge-locations #route53 #cloudfront #global-accelerator #dns #cdn #cloud-practitioner #cp-redes

> [!summary] El Concepto Clave
> Los usuarios odian esperar. Para que tu aplicación sea rápida a nivel mundial, necesitas una "guía telefónica" inteligente (Route 53), camiones de reparto locales que guarden copias de tus archivos (CloudFront) y carriles VIP en la autopista de Internet para evitar atascos (Global Accelerator).

---

## 📖 1. Amazon Route 53 (El Listín Telefónico / Recepcionista)

Las ordenadores no entienden de palabras, solo de números (Direcciones IP como `192.0.2.44`). Los humanos somos malísimos recordando números, así que usamos nombres (Dominios como `www.cafeteria.com`).

* **¿Qué es?** Es un servicio de **DNS (Sistema de Nombres de Dominio)** altamente disponible y escalable. 

* **¿Qué hace?** Traduce el nombre de la web que escribe el cliente en la dirección IP del servidor de AWS donde está alojada tu página. Además, te permite **comprar y registrar dominios nuevos**.

* **Su Superpoder (Enrutamiento Inteligente):** No solo traduce, sino que es un recepcionista muy listo. 

 * *Geolocalización:* Si detecta que el cliente teclea desde España, le da la IP del servidor de Madrid. Si teclea desde México, le da la IP del servidor de EE.UU. ¡Todo automáticamente!

---

## 🚚 2. Amazon CloudFront (La Red de Entrega - CDN)

Imagina que tu servidor principal (el almacén) está en EE.UU. Un cliente en Japón pide ver el catálogo de cafés (imágenes pesadas). Si esas fotos tienen que cruzar el océano Pacífico, la web cargará lento.

* **¿Qué es?** Es una **Red de Entrega de Contenido (CDN)**.

* **¿Cómo funciona?** Utiliza las **Ubicaciones Periféricas (Edge Locations)** de las que hablamos antes. La primera vez que el cliente japonés pide la foto, CloudFront va hasta EE.UU., trae la foto, se la da al cliente, **pero guarda una copia (Caché)** en el minicentro de Japón.

* **El Beneficio:** Cuando el *siguiente* cliente japonés pida la misma foto, CloudFront se la entrega directamente desde el minicentro de Japón en milisegundos. Ahorras dinero y mejoras la velocidad brutalmente.

* **Casos de uso:** Archivos estáticos pesados: Imágenes de tiendas online, vídeos de streaming (Netflix usa CDNs), mapas para apps móviles.

---

## 🏎️ 3. AWS Global Accelerator (El Carril VIP de Internet)

A veces, CloudFront no sirve. Si tienes un videojuego multijugador online o una app de transacciones bancarias, los datos cambian cada milisegundo. No puedes "guardar en caché" un disparo en un videojuego o el saldo de una cuenta. 

* **¿Qué es?** Es un servicio de red que utiliza la infraestructura global **privada** de AWS.

* **El Problema:** El Internet público está lleno de atascos y rutas ineficientes. Si envías un dato desde Londres a Tokio por el Internet normal, puede dar muchos saltos y sufrir "lag" (retraso).

* **La Solución:** Global Accelerator coge a tu usuario en Londres, lo mete inmediatamente en la red de fibra óptica privada de Amazon (donde no hay atascos externos), y lo lleva a Tokio por la ruta más rápida y estable posible.

* **Casos de uso:** Juegos online (reduce el lag), aplicaciones financieras en tiempo real, o cualquier app que necesite latencia ultra-estable para contenido que no se puede cachear.

---

## 📊 Chuleta de Examen: ¿Cuál elegir?

| Situación | Servicio a elegir | Palabra Clave en Examen |
| :--- | :--- | :--- |
| Quiero registrar un dominio (`.com`) o traducir nombres a IPs. | **Amazon Route 53** | "DNS", "Registrar dominio", "Enrutamiento geográfico" |
| Mi web carga lento por culpa de imágenes, PDFs o vídeos. | **Amazon CloudFront** | "CDN", "Caché", "Contenido estático", "Baja latencia global" |
| Mi juego online tiene lag o mi app bancaria va a tirones. | **AWS Global Accelerator** | "Contenido dinámico", "Red privada de AWS", "TCP/UDP", "Rendimiento constante" |

---

---
→ Volver al índice: [[📂Redes/00 - Índice Redes|🪐 Redes]]
