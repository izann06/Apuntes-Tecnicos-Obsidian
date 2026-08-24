**Tags:** #aws #compute #elastic-beanstalk #batch #lightsail #outposts #cloud-practitioner #cp-exploracion-de-los-servicios-de-computacion

> [!summary] El Concepto Clave
> No siempre tienes que construir desde cero con EC2. AWS ofrece servicios especializados que automatizan tareas muy concretas, como alojar un blog simple, procesar cálculos masivos, o incluso llevar la nube de AWS a tu propia oficina.

---
## 🌱 1. AWS Elastic Beanstalk (El Desplegador Automático)

Imagina que eres desarrollador, tienes el código de tu aplicación web listo y no quieres perder tiempo configurando redes, Auto Scaling o Balanceadores de Carga a mano. 

*   **¿Qué hace?** Es un servicio completamente administrado. Tú subes el código y le dices a Elastic Beanstalk qué esperas a alto nivel. El servicio coge esa información y construye automáticamente todo el entorno por ti (aprovisionamiento, escalado, equilibrio de carga y supervisión).

*   **La Ventaja:** Aunque automatiza todo, **mantienes el control total**. Si quieres entrar a ver o modificar las instancias EC2 que ha creado por debajo, puedes hacerlo.

*   **Lenguajes compatibles:** Java, .NET, Python, Node.js, Docker, etc.

*   **Ideal para:** Desplegar aplicaciones web, API RESTful y arquitecturas de microservicios sin administrar infraestructura.

---

## 🚜 2. AWS Batch (El Trabajador Pesado)

A veces no tienes una web que recibe visitas, sino un trabajo informático gigantesco que hacer (como renderizar una película o calcular riesgos financieros).

*   **¿Qué hace?** Es un servicio completamente administrado para cargas de trabajo de computación por lotes (batch) Los lotes son básicamente tareas iguales que vas almacenando para hacerlas todas de golpe. 

*   **¿Cómo funciona?** Tú le pasas los trabajos y AWS Batch programa, administra y escala automáticamente una flota de recursos (instancias EC2) para procesar todo de la forma más rápida y óptima posible.

*   **Ideal para:** Computación científica, procesamiento de big data, entrenamiento de machine learning, investigación genómica y transcodificación de archivos multimedia.

* Analogía: Vas guardando la ropa en un cesto y cuando ya está llena lo metes en la lavadora, para lavarlo todo de golpe, no vas lavando uno por uno o cuando tienes algun conjunto sucio, si no que te esperás hasta tener una cantidad razonable.

---

## ⛵ 3. Amazon Lightsail (El VPS Sencillo)

Si AWS te parece demasiado complejo y solo quieres un servidor simple para un proyecto pequeño, esta es tu opción.

*   **¿Qué hace?** Ofrece servidores privados virtuales (VPS), almacenamiento, bases de datos y redes de la forma más simplificada posible.

>[!WARNING] OJO. 
>Que sea privado no significa que no sea, cara al público, significa que el servidor es tuyo.

*   **La Ventaja:** Tiene un **precio mensual predecible**. Te aleja de la complejidad de la consola completa de AWS para que tengas algo rápido y fácil de gestionar.
*   **Ideal para:** Pequeñas empresas, blogs, sitios web con poco tráfico, entornos de pruebas y desarrollo.

**Por qué existe Lightsail si ya tengo EC2?** 
EC2 es para ingenieros. Si quieres un servidor web en EC2, tienes que configurar la red, el firewall, la IP pública, el disco duro y el sistema operativo por separado, y el precio varía cada mes según el uso. **Lightsail es un "todo incluido" para principiantes**. Te dan el servidor, la IP, el disco duro y el sistema operativo ya montado por un precio fijo (ej. 5$ al mes). Es la versión "IKEA" de EC2: barato, predecible y fácil de montar.

---

## 🏢 4. AWS Outposts (La Nube Híbrida)

¿Qué pasa si por leyes de tu país o por temas de extrema seguridad **no puedes** subir tus datos a los servidores de Amazon, pero quieres usar sus herramientas? 

*   **¿Qué hace?** Extiende la infraestructura y los servicios de AWS directamente a **tu centro de datos local (on-premises)**. Amazon literalmente te envía hardware para que lo instales en tu edificio. Puedes elegir **Outposts racks** que son más grande,con muchos servidores o los **Outposts Servers** que son más pequeños.

* ¿Cuánto cuesta? Outposts **no se paga por horas**, normalmente te exigen firmar un contrato de **3 años**. 

* **Los Outposts Servers (Pequeños):**  Rondan entre **$400 y $900 al mes** por cada servidor. No es una locura, pero tienes que comprometerte a 3 años. 
* **Los Outposts Racks (Los Gigantes):**  La configuración más barata (un armario con pocos servidores) suele empezar alrededor de los **$5.000 a $6.000 al mes**. * Si pides un armario lleno hasta arriba de servidores potentes y muchísima memoria, puede costar **más de $20.000 AL MES** (estamos hablando de contratos que se acercan al millón de dólares por los 3 años).

*   **La Ventaja:** Tienes una experiencia de nube híbrida consistente. Usas las mismas APIs y herramientas que en la nube pública, pero los datos no salen de tu oficina.

*   **Ideal para:** Aplicaciones que requieren latencia ultrabaja, cumplimiento normativo estricto, requisitos de residencia de datos o modernización de sistemas locales heredados.

---

## 📊 ¿Qué servicio elegir?

| Escenario / Palabras Clave | Servicio Ganador |
| :--- | :--- |
| "Solo quiero subir mi código y que AWS haga el resto para mi web", "Sin administrar infraestructura" | **AWS Elastic Beanstalk** |
| "Procesamiento paralelo", "Cálculos científicos masivos", "Trabajos en segundo plano" | **AWS Batch** |
| "Solución sencilla", "Precio predecible mensual", "Hosting básico para un blog" | **Amazon Lightsail** |
| "En las instalaciones", "Nube híbrida", "Estrictos requisitos de conformidad y residencia" | **AWS Outposts** |

---

---
→ Volver al índice: [[📂Exploracion de los servicios de computacion/00 - Índice Exploracion de los servicios de computacion|🪐 Exploracion de los servicios de computacion]]
