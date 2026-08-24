**Tags:** #aws #seguridad #inspector #guardduty #detective #security-hub #soc #cloud-practitioner #cp-seguridad

> [!summary] El Concepto Clave
> La seguridad no termina al poner una contraseña. Debes auditar constantemente tus servidores en busca de software desactualizado (Inspector), vigilar la red en busca de intrusos activos (GuardDuty), investigar cómo entraron si ocurre un ataque (Detective) y tener un panel central para ver todo este caos de forma ordenada (Security Hub).

---

## 🔍 1. Amazon Inspector (El Auditor Preventivo)

* **¿Qué hace?** Es un servicio de evaluación de vulnerabilidades automatizado.

* **La Analogía:** Es un inspector de edificios que va por tu cafetería comprobando si alguna ventana se quedó sin pestillo o si la puerta trasera tiene la madera podrida.

* **¿Cómo funciona?** Escanea continuamente tus **Instancias EC2, Contenedores y Funciones Lambda** buscando debilidades conocidas (por ejemplo, si tienes instalado un Windows antiguo que tiene un fallo de seguridad público). 

* **El Resultado:** Te da una lista de problemas priorizados por gravedad y te dice exactamente cómo arreglarlos *antes* de que te ataquen.

---

## 🐕 2. Amazon GuardDuty (El Perro Guardián / La Alarma)

* **¿Qué hace?** Es un servicio inteligente de detección de amenazas activas.

* **La Analogía:** Es el perro guardián y el sensor de movimiento. No busca puertas rotas, busca al ladrón *moviéndose* dentro del edificio.

* **¿Cómo funciona?** Utiliza **Machine Learning** e inteligencia de amenazas de AWS (listas negras globales de IPs de hackers). Analiza de forma invisible los registros (logs) de tu cuenta y la actividad de la red.

* **Casos de Uso:** Te avisa si un servidor tuyo de repente empieza a minar criptomonedas, si alguien intenta iniciar sesión desde un país donde no tienes empleados, o si tu servidor se comunica con una IP catalogada como maliciosa.

---

## 🕵️‍♂️ 3. Amazon Detective (El Investigador Forense)

* **¿Qué hace?** Analiza la causa raíz de un incidente de seguridad para que sepas qué pasó exactamente.

* **La Analogía:** La alarma (GuardDuty) sonó y atrapaste al ladrón. Ahora contratas a un detective con una lupa para que trace la línea temporal: por qué ventana entró, qué cajones abrió y con quién hablaba por teléfono.

* **¿Cómo funciona?** Recopila terabytes de registros automáticamente y utiliza machine learning para crear **gráficos visuales e interactivos**. Te permite ver la historia completa de un ataque para que puedas tapar el agujero y asegurarte de que no vuelva a pasar.

---

## 🎛️ 4. AWS Security Hub (El Centro de Mando Unificado)

* **El Problema:** Tienes a Macie (buscando tarjetas de crédito en S3), a Inspector (buscando software viejo), a IAM Access Analyzer y a GuardDuty lanzando alertas. Si tienes que abrir 4 pestañas diferentes para ver las alertas, te vas a volver loco.

* **La Solución:** **AWS Security Hub** centraliza todo en un único panel de control.

* **¿Qué hace?** Agrega (junta) todas las alertas (llamadas "hallazgos") de los diferentes servicios de seguridad de AWS (y de herramientas de terceros) en una sola vista. Además, evalúa continuamente si tu cuenta cumple con los estándares de seguridad de la industria.

---

## 📊 Chuleta Resumen: "El Ciclo del Incidente"

Para el examen, asocia cada servicio con su verbo principal:

| Servicio de AWS | Su función principal (Verbo) | Palabra clave en el examen |
| :--- | :--- | :--- |
| **Amazon Inspector** | **Evaluar** / Prevenir | "Vulnerabilidades de software", "EC2, Contenedores y Lambda". |
| **Amazon GuardDuty** | **Detectar** (en tiempo real) | "Amenazas activas", "Machine Learning", "IPs maliciosas". |
| **Amazon Detective** | **Investigar** / Analizar | "Causa raíz", "Gráficos interactivos", "Línea temporal". |
| **AWS Security Hub** | **Centralizar** / Consolidar | "Panel único", "Estado de cumplimiento", "Agregar hallazgos". |

---

---
→ Volver al índice: [[📂Seguridad/00 - Índice Seguridad|🪐 Seguridad]]
