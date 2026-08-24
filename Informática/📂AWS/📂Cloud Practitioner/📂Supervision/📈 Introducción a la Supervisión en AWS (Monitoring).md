**Tags:** #aws #supervision #monitoreo #metricas #alarmas #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> La supervisión (Monitoring) es el proceso continuo de **recopilar, visualizar y rastrear** la salud y el rendimiento de tus recursos en AWS. Te permite saber qué está pasando en tu infraestructura en tiempo real sin tener que estar mirando una pantalla las 24 horas del día.

---
## ☕ La Analogía de la Cafetería

Imagina que eres la dueña de la cafetería. No puedes estar físicamente allí todo el día observando cada taza de café que se sirve. Necesitas un sistema que responda a estas preguntas automáticamente:

1. **Métricas:** ¿Cuántos cafés se han vendido hoy? ¿Cuál es el tiempo de espera promedio?

2. **Registro (Logs):** ¿A qué hora exacta se acabó la leche de avena?

3. **Alarmas:** ¡Avisarme inmediatamente al móvil si la cola de clientes supera las 15 personas para llamar a otro barista!

En AWS, tu cafetería son tus servidores (EC2), tus bases de datos (RDS) y tus redes.

---

## 🚀 ¿Por qué es fundamental la supervisión en la nube?

A diferencia de un centro de datos físico donde tienes un número fijo de ordenadores, la nube de AWS es **elástica**. Los recursos cambian de tamaño dinámicamente.

* **Tomar Decisiones Automáticas (Escalado):** Si no supervisas, no puedes autoescalar. Necesitas un sistema que lea la métrica *"Uso de CPU al 85%"* para que tome la decisión automática de decir *"Enciende otro servidor EC2 inmediatamente"*.

* **Prevención de Caídas:** Si una aplicación empieza a dar errores (ej. Error 500) a una tasa inusualmente alta, la supervisión te envía una alerta antes de que los clientes inunden tu centralita de quejas.

* **Optimización de Costes:** La supervisión te dice si tienes servidores encendidos que están al 1% de uso de CPU, permitiéndote apagarlos y ahorrar dinero.

---

## 🧩 Los Tres Pilares de la Observabilidad

Para supervisar de manera eficaz, las herramientas de AWS recopilan tres cosas principales:

1.  **Métricas:** Números a lo largo del tiempo (ej. % de CPU, Megabytes de RAM usados, número de visitantes).

2.  **Registros (Logs):** Archivos de texto detallados que registran eventos específicos (ej. "A las 14:02 el usuario Juan inició sesión con éxito").

3.  **Paneles (Dashboards):** Pantallas visuales con gráficos para que los humanos puedan entender las métricas de un solo vistazo.

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
