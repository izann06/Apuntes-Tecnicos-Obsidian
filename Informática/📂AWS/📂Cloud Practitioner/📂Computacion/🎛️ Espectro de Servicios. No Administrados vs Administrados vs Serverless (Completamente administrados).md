**Tags:** #aws #ec2 #serverless #lambda #arquitectura #responsabilidad-compartida #cloud-practitioner #cp-computacion

> [!summary] El Gran Intercambio (Trade-off)
> En la nube, siempre estás intercambiando **Control** por **Comodidad**. Cuanto más administre AWS por ti, menos control tendrás sobre la máquina física/virtual, pero más tiempo tendrás para centrarte en tu negocio real.

---
## 1. Servicios No Administrados (Control Total)

Tú eres el administrador de sistemas. AWS te da una "caja vacía" con conexión a internet y electricidad.

*   **Tus tareas:** Instalar el sistema operativo, aplicar parches de seguridad, configurar el firewall interno, instalar el software, programar las copias de seguridad y configurar el Auto Scaling.

*   **Ejemplo AWS:** Amazon EC2.

*   **La Analogía:** La máquina de espresso profesional. Tienes que moler el grano, medir la presión, limpiar los filtros y espumar la leche. El café sale exactamente como tú quieres, pero da mucho trabajo.

* ![[🎛️ Espectro de Servicios. No Administrados vs Administrados vs Serverless (Completamente administrados).png]]

## 2. Servicios Administrados (Comodidad y Configuración)

AWS se encarga de que el "motor" subyacente funcione, no se rompa y esté actualizado. Tú solo configuras las reglas de negocio.

*   **Tus tareas:** Configurar el servicio (ej. decir a qué instancias debe apuntar el tráfico o quién puede leer los mensajes). No ves el sistema operativo ni instalas parches.

*   **Ejemplos AWS:** Elastic Load Balancing (ELB), Amazon SQS, Amazon SNS.

*   **La Analogía:** La cafetera de cápsulas. AWS pone la máquina y el mantenimiento; tú solo metes la cápsula que quieres, pulsas el botón y te olvidas.

## 3. Totalmente Administrados / Sin Servidor (Serverless)

> [!warning] OJO
>  Todos lo serverless son totalmente administrados, pero no todos los totalmente administrados son serverless.

*   **Tus tareas:** Escribir el código de tu aplicación o subir tus datos. NADA MÁS. AWS escala de cero a infinito y te cobra solo por los milisegundos que tu código está en ejecución.

*   **Ejemplo AWS:** AWS Lambda (lo verás en detalle más adelante).

*   **La Analogía:** Ir a una cafetería de especialidad y pedir un café. No te importa qué máquina usan, ni quién limpia los filtros, ni si el barista está parcheado a la última versión. Solo quieres tu café y pagas por él.

---

## ⚖️ El Modelo de Responsabilidad Compartida aquí

La línea de lo que "es tu culpa" y lo que "es culpa de AWS" se mueve dependiendo de lo que elijas:

| Tipo de Servicio | ¿AWS gestiona el Hardware? | ¿AWS parchea el Sistema Operativo? | ¿Tú gestionas el Código/Datos? |
| :--- | :---: | :---: | :---: |
| **No Administrado (EC2)** | ✅ Sí | ❌ No (Es tu responsabilidad) | ✅ Sí |
| **Administrado (ELB/SQS)**| ✅ Sí | ✅ Sí | ✅ Sí |
| **Serverless (Lambda)** | ✅ Sí | ✅ Sí | ✅ Sí |

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
