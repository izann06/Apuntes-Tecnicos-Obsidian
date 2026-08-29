**Tags:** #aws #escalabilidad #elasticidad #auto-scaling #alta-disponibilidad #cloud-practitioner #cp-computacion

> [!danger] El Gran Malentendido
>
> * **Escalabilidad:** Es el *diseño*. ¿Puede mi sistema crecer si mi empresa tiene éxito?
>
> * **Elasticidad:** Es la *acción automática*. ¿Puede mi sistema estirarse y encogerse en tiempo real para no gastar dinero a lo tonto?

---

## 1. Conceptos de Crecimiento
#### 🏗️ Escalabilidad (Scalability)

La escalabilidad es la **capacidad arquitectónica** de tu sistema para manejar cargas de trabajo cada vez mayores. Se centra en el crecimiento a largo plazo.

* **La Analogía (El Estadio de Fútbol):** Construyes un estadio con 10.000 asientos. Pero el arquitecto lo diseña de tal forma que, si el equipo sube a primera división en 5 años, se puede construir fácilmente un segundo anillo para añadir 20.000 asientos más sin tener que derribar el estadio original. El estadio es **escalable**.

* **En AWS:** Significa que has construido tu aplicación de manera que, si pasas de 10 usuarios a 1 millón, el sistema no colapsará de forma irremediable, sino que aceptará que le añadas más potencia (vertical) o más servidores (horizontal).

#### 🧽 Elasticidad (Elasticity)

La elasticidad es la capacidad del sistema de **adaptarse dinámicamente y al instante** a los picos y caídas de demanda, encogiéndose y estirándose como una goma elástica. Se centra en la rentabilidad a corto plazo.

* **La Analogía (El Pantalón de Chándal):** Imagina unos pantalones mágicos. Si te comes un banquete de Navidad, la goma de la cintura se estira para que respires (Scale Out). Si al día siguiente te vas a correr y quemas las calorías, la goma se encoge automáticamente para que no se te caigan los pantalones (Scale In). **Eso es Elasticidad.**

* **En AWS:** Son las 10:00 AM y entran mil usuarios: AWS enciende 5 servidores al momento. Son las 3:00 AM y no hay nadie: AWS apaga 4 servidores para que no pagues por ellos.

---

## 2. El Desafío de la Capacidad

Planificar la capacidad en servidores locales (on-premises) es difícil. Tienes dos opciones malas:

1. **Planificar para el pico máximo:** Compras servidores para soportar el mayor pico de tráfico posible. *Problema:* Es muy caro y los servidores estarán inactivos la mayor parte del tiempo.

2. **Planificar para el promedio:** Compras servidores para el uso normal. *Problema:* Durante los picos de tráfico (ej. Black Friday), el sistema se satura y los clientes no pueden acceder al servicio.

**La Solución de AWS:** Aprovisionar la capacidad exacta necesaria en cada momento (Elasticidad).

---

## 3. Tipos de Escalado

### Escalado Vertical (Scale Up)

* **Concepto:** Añadir más potencia a las máquinas existentes.

* **En AWS:** Cambiar el tipo de instancia EC2 por uno más grande (ej. pasar de `t3.micro` a `t3.large`).

* **Analogía:** Cambiar el motor de un coche por uno más potente.

### Escalado Horizontal (Scale Out / Scale In)

* **Concepto:** Añadir más cantidad de máquinas para trabajar en paralelo.

* **En AWS:** Añadir más instancias EC2 idénticas.

* **Analogía:** Comprar más coches iguales. *Este es el método preferido para aplicaciones web y servicios distribuidos.*

---

## 4. Alta Disponibilidad y Redundancia

Para evitar un "punto único de falla" (Single Point of Failure), no dependas de una sola instancia.

* **Redundancia:** Crea copias de tus instancias. Si una falla, la otra puede tomar el relevo.

* **Zonas de Disponibilidad (AZs):** Despliega estas instancias redundantes en *múltiples* Zonas de Disponibilidad dentro de una región. Si hay un problema en un centro de datos, la aplicación sigue funcionando desde otro.

---

## 5. Amazon EC2 Auto Scaling

Es el servicio que automatiza el escalado horizontal (Añadir más máquinas).

* **¿Qué hace?:** Añade instancias EC2 (Scale Out) cuando la demanda sube y las elimina (Scale In) cuando la demanda baja, según las métricas que definas.

* **Integración:** Utiliza **Amazon CloudWatch** (el servicio de monitorización de AWS) para recopilar datos (como uso de CPU, tráfico de red) y decidir cuándo escalar.

* **Beneficio principal:** Pone a tu disposición una arquitectura rentable; solo pagas por lo que necesitas, cuando lo necesitas.

### Enfoques de Escalado Automático

1. **Escalado Dinámico:** Ajusta el número de instancias en tiempo real respondiendo a las fluctuaciones de la demanda.

2. **Escalado Predictivo:** Programa el escalado con anticipación basándose en patrones de uso históricos o previsiones.

### Grupos de Auto Scaling (Auto Scaling Groups - ASG)

Un grupo de Auto Scaling gestiona una colección de instancias EC2. Se configura con tres límites clave:

1. **Capacidad Mínima:** El número mínimo de instancias que siempre deben estar encendidas (para asegurar que la aplicación no se caiga).

	1. ![[Sin título.png]]

2. **Capacidad Deseada:** El número objetivo de instancias que el grupo intentará mantener en condiciones normales.

	2. ![[Sin título-1.png]]

3. **Capacidad Máxima:** El límite superior de instancias que el grupo puede crear durante un pico de demanda (para controlar los costes).

	3. ![[Sin título-2.png]]

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
