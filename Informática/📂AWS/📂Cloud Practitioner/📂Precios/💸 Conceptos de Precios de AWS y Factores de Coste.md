**Tags:** #aws #precios #facturacion #savings-plans #cloud-practitioner #cp-precios

> [!summary] El Concepto Clave
> AWS funciona exactamente igual que la factura de la luz o el agua de tu casa. No compras la central eléctrica (el servidor), solo pagas por los vatios que consumes. Además, AWS premia la fidelidad (si prometes quedarte tiempo, te hacen descuento) y el volumen (si compras al por mayor, es más barato).

---
## 📐 1. Los Tres Principios Fundamentales de Precios

Si entiendes estas tres reglas, entenderás casi toda la facturación de la nube:

1. **Pago por uso (Pay-as-you-go):**

 * *El concepto:* Si enciendes un servidor durante 3 horas y 15 minutos, pagas exactamente 3 horas y 15 minutos. Si lo apagas, el coste de computación se detiene a cero inmediatamente.
 
 * *Beneficio:* Ideal para experimentar o para cargas de trabajo que suben y bajan de forma impredecible (elimina el riesgo de comprar servidores de sobra).

2. **Ahorro con el compromiso (Save when you commit):**

 * *El concepto:* Si tu negocio es estable y sabes que vas a necesitar servidores funcionando 24/7, puedes firmar un **Savings Plan (Plan de Ahorro)** o reservar instancias.
 
 * *El Trato:* Te comprometes a un nivel de gasto durante **1 o 3 años**, y a cambio, AWS te hace descuentos masivos (hasta un 72% más barato que el pago por uso normal).
 
3. **Menor pago al incrementar el uso (Descuentos por Volumen):**

 * *El concepto:* AWS tiene "precios por niveles".
 
 * *El Trato:* Cuanto más usas un servicio, más barato te sale el Gigabyte. Por ejemplo, en Amazon S3, los primeros 50 Terabytes te cuestan un precio "X" por GB. Si guardas 500 Terabytes, los GB adicionales te cuestan "X - 10%".

---

## 🧮 2. Los 3 Factores que Impulsan el Coste (Cost Drivers)

Cuando miras la factura de AWS, el 90% de tus gastos provendrán de estas tres categorías:

### A. Computación (Compute)

* **¿Qué te cobran?** El tiempo de procesamiento.

* **La Métrica:** Se cobra **por hora o por segundo** (dependiendo del sistema operativo y la instancia EC2). Empiezas a pagar cuando le das a "Iniciar" y dejas de pagar cuando le das a "Detener" (¡Ojo! Si la instancia está detenida no pagas computación, pero *sí* pagas el disco duro EBS que tiene asociado).

### B. Almacenamiento (Storage)

* **¿Qué te cobran?** El espacio ocupado.

* **La Métrica:** Se cobra **por Gigabyte (GB) mensual**. En servicios elásticos como S3, pagas exactamente por los GB de las fotos o archivos que subes.

### C. Transferencia de Datos (Data Transfer) 

AWS es como un club nocturno: entrar es gratis, pero sacar cosas te cuesta dinero.

* **Transferencia de Entrada (Data IN):** Mover datos desde Internet hacia AWS (ej. subir fotos a S3) es **SIEMPRE GRATIS**.

* **Transferencia de Salida (Data OUT):** Mover datos desde AWS hacia Internet (ej. tus usuarios descargando archivos de S3) **CUESTA DINERO** (se cobra por GB transferido).

* *Excepción interna:* Transferir datos entre servicios dentro de la *misma* Región suele ser gratis. Transferir datos entre dos Regiones distintas (ej. de París a Tokio) cuesta dinero.

---

## 📊 Chuleta Rápida de Facturación

| Componente | ¿Cómo se cobra principalmente? | ¿Se puede conseguir descuento? |
| :--- | :--- | :--- |
| **Computación (EC2)** | Por Hora / Segundo | Sí (Compromiso de 1 a 3 años) |
| **Almacenamiento (S3)** | Por Gigabyte (GB) al mes | Sí (Precios por niveles de volumen) |
| **Datos HACIA AWS (IN)** | **Es GRATIS ($0)** | N/A |
| **Datos DESDE AWS (OUT)** | Por Gigabyte (GB) saliente | Sí (Precios por niveles de volumen) |

---

---
→ Volver al índice: [[📂Precios/00 - Índice Precios|🪐 Precios]]
