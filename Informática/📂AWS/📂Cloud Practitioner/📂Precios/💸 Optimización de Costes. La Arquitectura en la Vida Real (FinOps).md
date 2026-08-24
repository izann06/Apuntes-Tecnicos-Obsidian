**Tags:** #aws #optimizacion #costes #finops #arquitectura #cloud-practitioner #cp-precios

> [!summary] El Concepto Clave
> La optimización de costes no significa elegir siempre el servidor más lento y barato. Significa pagar *exactamente* por lo que necesitas, cuando lo necesitas, y no desperdiciar ni un céntimo en recursos encendidos que nadie está utilizando. Es el equilibrio entre rendimiento y eficiencia financiera.

---

## 🛠️ 1. Optimizando la Computación (Amazon EC2)

El poder de cómputo suele ser la parte más cara de cualquier factura en la nube. Aquí aplicamos estas técnicas:

* **Dimensionamiento Óptimo (Right-Sizing):** Es el paso uno. Consiste en analizar tu servidor y bajarle la talla si le sobra potencia. *Herramienta clave:* **AWS Compute Optimizer** (utiliza Machine Learning para decirte: "Oye, este servidor gigante de 8 núcleos solo usa el 10% de su CPU, bájalo a uno de 2 núcleos").

* **Instancias de Spot (Descuentos del 90%):** Si tienes procesos flexibles que pueden interrumpirse (como un pipeline de CI/CD, procesamiento de datos en segundo plano o renderizado de imágenes), usa instancias Spot. Alquilas la capacidad sobrante de AWS a precio de saldo.

* **Auto Scaling (Dimensionamiento Automático):** Apagar servidores por la noche o los fines de semana cuando no hay tráfico.

* **Limpieza de "Basura Digital":** Borrar volúmenes de discos duros (Amazon EBS) o instantáneas (Snapshots) que pertenecen a servidores EC2 que ya fueron eliminados hace meses. ¡Un disco suelto te sigue cobrando cada mes!

---

## 🗄️ 2. Optimizando Bases de Datos (Amazon RDS)

No intentes resolver un problema de lentitud en la base de datos simplemente comprando una máquina más grande y cara.

* **Réplicas de Lectura (Read Replicas):** Si tu aplicación (como un juego o un blog) tiene 10.000 personas leyendo datos y solo 10 escribiendo, no escales la base de datos principal de forma vertical. Crea réplicas de lectura más baratas para distribuir el tráfico de los que solo están "mirando".

* **Caché (Amazon ElastiCache):** Si todo el mundo consulta siempre el mismo dato (ej. el ranking de puntuaciones de tu proyecto), guárdalo en la memoria caché. Es mil veces más rápido y le quita el estrés (y el coste) a la base de datos RDS principal.

* **Dimensionamiento Óptimo y Apagado:** Al igual que EC2, evalúa si la base de datos está sobredimensionada. Si es un entorno de desarrollo, apágala cuando el equipo termine de trabajar.

---

## 📦 3. Optimizando el Almacenamiento (Amazon S3)

Acumular datos sin control puede disparar la factura silenciosamente.

* **S3 Intelligent-Tiering:** Si tienes datos pero no sabes si la gente los va a descargar mucho o poco, usa esta clase de almacenamiento. AWS mueve automáticamente los archivos a capas más baratas si ve que nadie los toca durante 30 o 90 días.

* **Políticas de Ciclo de Vida (Lifecycle Policies):** Reglas automáticas. *Ejemplo:* "Mover las copias de seguridad de S3 Standard a S3 Glacier (archivo súper barato) a los 30 días, y borrarlas permanentemente a los 3 años".

* **Compresión:** Si vas a guardar logs masivos o datos de texto, usa una función de **AWS Lambda** para comprimirlos en un archivo `.zip` o `.gz` antes de subirlos a S3. Pagarás por muchos menos Gigabytes.

---

## 🌐 4. Optimizando la Red y Transferencia de Datos

Recuerda: la transferencia de AWS (hacia Internet) cuesta dinero.

* **Tráfico cruzado:** Minimiza el tráfico de datos entre diferentes Zonas de Disponibilidad (AZ) si no es estrictamente necesario, ya que AWS cobra una pequeña tarifa por cruzar zonas.

* **VPC Endpoints (Puntos de enlace de la VPC):** ¡Pregunta de examen muy común! Si tu servidor EC2 privado necesita guardar un archivo en Amazon S3, por defecto, esos datos viajan por el Internet público, y AWS te cobra transferencia de salida. **Un VPC Endpoint crea un túnel privado y directo** entre tu red y S3. Es más seguro, más rápido y te ahorra enormes costes de red.

---

---
→ Volver al índice: [[📂Precios/00 - Índice Precios|🪐 Precios]]
