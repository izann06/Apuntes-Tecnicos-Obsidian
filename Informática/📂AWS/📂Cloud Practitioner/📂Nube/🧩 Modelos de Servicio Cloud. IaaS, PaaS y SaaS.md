**Tags:** #aws #modelos-servicio #iaas #paas #saas #conceptos-basicos #cp-nube
**Fecha:** 2026-04-29

> [!summary] El Concepto Core
> La nube te permite elegir tu nivel de "pereza" o control. Puedes alquilar desde los hierros vacíos hasta el programa ya hecho y listo para usar. 

---

## 🏗️ 1. IaaS (Infraestructura como Servicio)

Te alquilan los cimientos y las paredes vacías. Tú tienes que poner los muebles, la electricidad y pintar. Tienes el **máximo control**, pero también el **máximo trabajo de mantenimiento**.

* **En la Nube (AWS):** `Amazon EC2`. Te dan un servidor virtual en blanco. Tú tienes que instalar el Windows/Linux, actualizarlo, instalar el motor de base de datos y subir tu código.

* **🍕 Ejemplo del día a día (Pizza Congelada):** Vas al supermercado y compras una pizza congelada. El supermercado te da los ingredientes ya juntos (hardware), pero **tú** tienes que usar tu horno, pagar tu luz, hornearla y poner la mesa.

* **🚗 Otro ejemplo (Coche de alquiler):** Te dan el coche, pero tú tienes que conducir, echar gasolina y no chocarte.

* **Ejemplos Reales:** AWS(EC2), Azure, Google Cloud.

---

## 🛠️ 2. PaaS (Plataforma como Servicio)

Te alquilan el entorno listo para que tú solo te centres en tu trabajo principal (tu código o tus datos), sin preocuparte de lo que hay por debajo. El proveedor gestiona el sistema operativo y las actualizaciones.

* **En la Nube (AWS):** `Amazon RDS` (Base de datos) o `AWS Elastic Beanstalk`. Tú no ves el "Windows" que corre por debajo, solo ves la base de datos lista para que guardes información. Si hay que actualizar el sistema operativo, AWS lo hace solo.

* **🍕 Ejemplo del día a día (Pizza a Domicilio):** Llamas a la pizzería. Ellos ponen los ingredientes, el horno y te la cocinan. **Tú** solo tienes que preocuparte de poner la mesa en tu casa y comértela.

* **🚗 Otro ejemplo (Taxi / Uber):** Tú dices a dónde quieres ir (tu código/datos), pero el taxista (proveedor) conduce y se encarga de la gasolina y el mantenimiento del coche.

* **Ejemplos Reales:** GitHub, Shopify, Firebase, AWS (RDS, Lambda).

---

## 🚀 3. SaaS (Software como Servicio)

Te alquilan el producto final terminado. No gestionas ni los servidores, ni el sistema operativo, ni el código. Solo creas una cuenta, te logueas y lo usas. **Mínimo control, pero cero mantenimiento.**

* **En la Nube general:** `Gmail`, `Netflix`, `Zoom`, `Office 365`. (AWS tiene pocos SaaS puros, pero un ejemplo sería `Amazon WorkMail`).

* **🍕 Ejemplo del día a día (Restaurante):** Vas a una pizzería. Te sientas. Te traen la pizza hecha, te ponen la mesa, te sirven la bebida y luego ellos lavan los platos. Tú solo consumes y pagas.

* **🚗 Otro ejemplo (Autobús):** Tú no decides la ruta ni conduces. Simplemente te subes, pagas el billete y usas el servicio tal cual está diseñado.

* **Ejemplos Reales:** Gmail, Netflix,Spotify.

---

## 📊 Tabla Comparativa para el Examen

| Modelo | ¿Qué gestionas TÚ? | ¿Qué gestiona AWS? | Nivel de Control | Ejemplo AWS |
| :------- | :---------------------------------------- | :--------------------------------- | :--------------- | :-------------- |
| **IaaS** | SO, Datos, Aplicaciones, Red | Hardware, Servidores físicos | 🔴 Alto | EC2, S3 |
| **PaaS** | Datos, Aplicaciones | Hardware, SO, Entorno de ejecución | 🟡 Medio | RDS, Lambda |
| **SaaS** | ¡Nada! Solo la configuración de tu cuenta | Todo (Hardware, SO, App completa) | 🟢 Bajo | WorkMail, Gmail |

---

---
→ Volver al índice: [[📂Nube/00 - Índice Nube|🪐 Nube]]
