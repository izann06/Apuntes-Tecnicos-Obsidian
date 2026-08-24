**Tags:** #aws #ec2 #precios #billing #finops #cloud-practitioner #cp-computacion

> [!summary] La Regla del Dinero en la Nube
> No existe un único precio para un servidor. AWS te cobra dependiendo de **cuánto tiempo te comprometas** a usarlo y de si puedes **tolerar que te lo apaguen** de repente.

---
## 1. Bajo Demanda (On-Demand)

Es la opción por defecto. Pagas exactamente por lo que usas (por hora o por segundo), sin ataduras.

* **Características:** Sin compromisos a largo plazo. Sin pagos por adelantado.

* **Casos de uso:** Aplicaciones nuevas donde no conoces el tráfico, pruebas, experimentación, o cargas de trabajo a corto plazo.

* **Ejemplo del día a día:** Es como dormir en un hotel. Pagas la noche que duermes y te vas cuando quieres, pero es la tarifa más cara.

---

## 2. Los Modelos de Compromiso (Ahorro del 72% al 75%)

Si sabes que vas a usar AWS durante años, Amazon te hace un descuento gigante a cambio de firmar un "contrato" de 1 o 3 años. Tienen 3 formas de pago: *Todo por adelantado, Pago parcial o Sin pago por adelantado*.

### A. Instancias Reservadas (RI)

* **Concepto:** Te comprometes a usar un tipo de instancia específico durante 1 o 3 años.

* **Casos de uso:** Cargas de trabajo de "estado estable" o uso predecible (ej. la base de datos principal de la empresa que nunca se apaga).

### B. Savings Plans (Planes de Ahorro)

* **Concepto:** Es la evolución moderna de las Reservadas. En lugar de comprometerte a una máquina específica, te comprometes a **gastar una cantidad fija de dólares por hora** (ej. "Prometo gastar 10$/hora durante 3 años").

* **La Ventaja:** Es súper flexible. El descuento se aplica aunque cambies de familia de instancia, de sistema operativo, de región, ¡e incluso sirve para servicios sin servidor como AWS Fargate o Lambda!

---

## 3. Instancias Spot (Las "Sobras" - Ahorro del 90%)

AWS tiene miles de servidores vacíos en sus centros de datos esperando a que alguien los alquile. Para no tenerlos apagados, los "subastan" a precios ridículos.

* **El Inconveniente:** Si un cliente que paga *Bajo Demanda* necesita tu servidor, AWS te lo quita. Solo te dan un **aviso de 2 minutos** para guardar tu trabajo antes de apagarlo.

* **Casos de uso:** Procesamiento por lotes (batch), análisis de datos masivos, renderizado de vídeo. (Cosas que, si se cortan a la mitad, no pasa nada porque pueden retomarse luego).

* **Para el examen:** Busca SIEMPRE las palabras **"tolerar interrupciones"** o **"trabajos en segundo plano"**.

---

## 4. Opciones Dedicadas (Aislamiento Físico)

Por defecto, EC2 usa *Tenencia Múltiple* (compartes la máquina física con otros clientes). Si por ley o por seguridad no puedes hacer esto, pagas un extra por el aislamiento.

* **Instancias Dedicadas:** Tu servidor virtual corre en un hardware físico que es exclusivo para tu cuenta de AWS. Amazon decide en qué máquina física se pone, pero nadie más entra ahí.

* **Hosts Dedicados:** Alquilas el **servidor físico completo**. Tienes control total sobre la ubicación de las instancias dentro de ese hierro. 

	* **Casos de uso:** Cumplimiento de normativas gubernamentales muy estrictas o **licencias de software (BYOL - Bring Your Own License)** como Windows Server o SQL Server que te obligan a asociar la licencia a un procesador físico concreto (sockets/cores).

![[💰 Modelos de Precios y Facturación de Amazon EC2-2.png]]

---

## 📊 ¿Qué modelo elegir?

| Escenario del Cliente (Palabras clave) | Modelo Ganador |
| :--- | :--- |
| "No conoce sus patrones de uso", "Quiere probar", "Sin compromisos" | **Bajo Demanda** |
| "Uso constante y predecible", "Se compromete a 1 o 3 años" | **Instancias Reservadas** |
| "Quiere un compromiso a largo plazo pero con máxima flexibilidad" | **Savings Plans** |
| "Puede tolerar interrupciones", "Procesamiento por lotes", "Costo mínimo" | **Instancias Spot** |
| "Regulaciones estrictas", "Control total del hardware", "Licencias propias"| **Hosts Dedicados** |

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
