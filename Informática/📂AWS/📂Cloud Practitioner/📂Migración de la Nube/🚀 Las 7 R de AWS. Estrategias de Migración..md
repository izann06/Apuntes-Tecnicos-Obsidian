
**Tags:** #aws #migracion #7-rs #arquitectura #cloud-practitioner #finops #cp-migracion-de-la-nube

> [!summary] El Concepto Clave
> Cuando una empresa decide migrar a la nube, no tiene por qué tratar a todas sus aplicaciones de la misma manera. Cada componente o sistema de software de la cartera de TI tiene un camino óptimo de migración. Las **7 R** representan el marco estratégico oficial de AWS para decidir el destino de cada aplicación evaluando el equilibrio entre el esfuerzo humano y los beneficios a largo plazo.

---
## 🏎️ 1. Migraciones Rápidas (Poco o ningún cambio de código)

### A. Reubicar (Relocate)

* **¿Qué es?** Mover instancias a nivel de hipervisor (como máquinas virtuales o contenedores) directamente a la nube sin cambiar el formato ni modificar la configuración operativa.

* **Caso de uso:** Aplicaciones que ya corren en entornos virtualizados u orquestados localmente y solo necesitan un cambio de dirección de alojamiento hacia AWS.

### B. Realojar (Rehost / "Lift and Shift")

* **¿Qué es?** Levantar la aplicación tal como está en el servidor local y moverla a una instancia **Amazon EC2** en la nube, sin realizar ningún tipo de optimización ni cambio arquitectónico.

* **Caso de uso:** Ideal para grandes migraciones heredadas donde la prioridad absoluta de la empresa es la velocidad y escalar rápido para cumplir con un plazo estricto. Puede ahorrar hasta un 30% de costes iniciales por el simple hecho de apagar el hierro local.

### C. Redefinir la Plataforma (Replatform / "Lift, Tinker and Shift")

* **¿Qué es?** Levantar la aplicación, realizar unos pequeños ajustes u optimizaciones para aprovechar ventajas tangibles de la nube, pero **sin modificar el código central** ni la arquitectura del programa.

* **Caso de uso:** Mover una base de datos MySQL autogestionada en un servidor local directamente hacia un servicio administrado como **Amazon RDS** o **Amazon Aurora**. El equipo se quita el trabajo de mantenimiento de encima sin picar código nuevo.

---

## 🛠️ 2. Transformación Radical (Cambio de producto o arquitectura)

### D. Refactorizar / Rearquitecturar (Refactor / Re-architect)

* **¿Qué es?** Volver a imaginar y escribir el código de la aplicación desde cero utilizando servicios nativos de la nube (como pasar de un monolito a microservicios con **AWS Lambda** o contenedores).

* **El Balance:** Tiene el coste inicial de planificación y esfuerzo humano más alto de todos, pero ofrece el mayor rendimiento, escalabilidad y beneficio de la nube a largo plazo.

### E. Recomprar (Repurchase / "Drop and Shop")

* **¿Qué es?** Abandonar el software o la licencia tradicional actual y cambiarlo por completo adquiriendo un modelo de **Software como Servicio (SaaS)** disponible en la nube.

* **Caso de uso:** Migrar un sistema antiguo de gestión de clientes (CRM) local hacia una solución SaaS moderna en la nube.

---

## 🛑 3. Sin Migración Real (El portfolio estático)

### F. Retener (Retain)

* **¿Qué es?** Mantener la aplicación funcionando exactamente donde está (en el centro de datos local). No se migra nada por ahora.

* **Caso de uso:** Aplicaciones esenciales para el negocio que requerirían un esfuerzo de refactorización inviable en este momento, o sistemas que van a ser deprecados en pocos meses y no merece la pena el gasto de moverlos.

### G. Retirar (Retire)

* **¿Qué es?** Identificar aplicaciones muertas o redundantes y apagarlas definitivamente.

* **Dato curioso:** No es raro que las corporaciones descubran que más del 10% de sus sistemas activos en los servidores de la oficina ya no son utilizados por ningún empleado. Identificarlos durante el plan de migración ahorra costes inmediatos.

---

## 📊 Chuleta Resumen (Estrategia vs. Código)

| Estrategia (R) | Nombre técnico común | ¿Se toca el código de la app? | Esfuerzo | Beneficio en la nube |
| :--- | :--- | :--- | :--- | :--- |
| **Refactor** | Rearquitecturar | **Sí (Cambio total)** | 🔴 Máximo | 🍏 Máximo |
| **Replatform** | *Lift, tinker and shift* | No (Solo el entorno) | 🟡 Medio | 🍏 Medio-Alto |
| **Rehost** | *Lift and shift* | No (Copia exacta) | 🟢 Bajo | 🍏 Medio-Bajo |
| **Repurchase** | *Drop and shop* | No (Se compra otro) | 🟡 Variable | 🍏 Alto (SaaS) |

---

---
→ Volver al índice: [[📂Migración de la Nube/00 - Índice Migración de la Nube|🪐 Migración de la Nube]]
