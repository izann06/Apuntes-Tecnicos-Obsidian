**Tags:** #aws #facturacion #budgets #cost-explorer #pricing-calculator #cloud-practitioner #cp-precios

> [!summary] El Concepto Clave
> La nube es elástica, lo que significa que los costes también lo son. AWS proporciona herramientas específicas para **estimar** cuánto vas a gastar antes de comprar, **supervisar** cuánto estás gastando ahora, **analizar** en qué te lo has gastado en el pasado, y poner **alertas** para no pasarte del presupuesto.

---

## 🏢 1. Facturación Consolidada (AWS Organizations)

Como vimos en el módulo de gobernanza, **AWS Organizations** tiene un superpoder financiero:

* **Una sola factura:** Unifica todas las subcuentas de tu empresa bajo una única cuenta de pago principal. 

* **Beneficio clave:** Facilita la vida al equipo de finanzas y permite alcanzar los **descuentos por volumen** mucho más rápido al sumar el consumo de todos los departamentos.

---

## 🛠️ 2. El Cuarteto de Gestión de Costes

### A. Calculadora de Precios de AWS (AWS Pricing Calculator)

* **¿Cuándo se usa?** *ANTES* de crear nada.

* **¿Qué hace?** Es una herramienta web donde simulas tu arquitectura (ej. "Quiero 3 servidores EC2 y 500GB en S3"). Te genera un presupuesto estimado mensual o anual. 
### B. Panel de Facturación (Billing Dashboard)

* **¿Cuándo se usa?** Para ver el estado *ACTUAL*.

* **¿Qué hace?** Es la pantalla principal donde ves tu gasto en lo que va de mes, tu previsión de cierre de mes y donde gestionas tus tarjetas de crédito o métodos de pago.

### C. AWS Budgets (Los Presupuestos y las Alertas)

* **¿Cuándo se usa?** Para *PREVENIR* sustos.

* **¿Qué hace?** Te permite establecer límites de dinero personalizados (ej. "Mi presupuesto son 1.000€ al mes"). 

* **El Superpoder:** Las **Alertas Automáticas**. Si a día 15 del mes AWS detecta que vas a superar los 1.000€ según tu ritmo de gasto actual, te envía un correo electrónico al instante para que puedas detener los servidores antes de arruinarte.

### D. AWS Cost Explorer (El Explorador de Costes)

* **¿Cuándo se usa?** Para *ANALIZAR* el pasado y encontrar tendencias.

* **¿Qué hace?** Es una herramienta analítica con gráficos visuales interactivos. Te permite ver en qué te has gastado el dinero en los últimos meses.

* **El Poder de las Etiquetas (Tags):** Si a cada recurso de AWS le pones una etiqueta (ej. `Departamento: Marketing`), en Cost Explorer puedes filtrar el gráfico para ver exactamente cuánto dinero está gastando el departamento de marketing frente al de ventas.

---

## 📊 Chuleta Resumen para el Examen

Si tienes dudas entre Budgets y Cost Explorer (la trampa más común), recuerda esta regla:

| Si la pregunta dice... | El servicio que buscas es... |
| :--- | :--- |
| Necesito **estimar** cuánto me costará un proyecto nuevo. | **Calculadora de precios de AWS** |
| Quiero recibir una **alerta/notificación** si el gasto supera los $500. | **AWS Budgets** |
| Necesito **analizar gráficos** de los últimos 6 meses agrupados por **etiquetas**. | **AWS Cost Explorer** |
| Quiero **unificar el pago** de las cuentas de mis 5 departamentos. | **AWS Organizations** |

---

---
→ Volver al índice: [[📂Precios/00 - Índice Precios|🪐 Precios]]
