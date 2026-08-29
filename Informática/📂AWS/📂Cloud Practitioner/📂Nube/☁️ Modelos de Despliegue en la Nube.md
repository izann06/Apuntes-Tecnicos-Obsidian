
**Tags:** #aws #cloud-practitioner #conceptos-basicos #infraestructura #cp-nube

> [!summary] Concepto Clave
> En el mundo de la computación, un "Modelo de Despliegue" simplemente responde a la pregunta: **¿De quién son los servidores físicos y dónde están ubicados?** AWS define tres modelos principales.

---

## 1. Nube Pública (Public Cloud)

La infraestructura pertenece a un proveedor de nube (como AWS, Google Cloud o Microsoft Azure) y se ofrece a través de Internet. Los recursos (servidores, bases de datos) se comparten entre miles de clientes, aunque los datos de cada cliente están estrictamente aislados.

* **La Analogía:** Es como **vivir en un edificio de apartamentos de alquiler**. No eres dueño del edificio, compartes la electricidad y el agua (red y servidores físicos) con tus vecinos, pero tu apartamento tiene llave y nadie más puede entrar. El dueño del edificio (AWS) se encarga de reparar el ascensor y la seguridad del lobby.

* **Características Principales:**

	* **Cero inversión inicial:** No compras hardware. Pagas por lo que usas (Pay-as-you-go).

	* **Escalabilidad masiva:** Si necesitas 1,000 servidores en 5 minutos, los tienes.

	* **Mantenimiento:** El proveedor se encarga del "trabajo pesado" (hardware, refrigeración, seguridad física).
	
* **Ejemplo en AWS:** Todo lo que usas directamente en Amazon Web Services (EC2, S3, RDS).

## 2. Nube Privada / Local (On-Premises / Private Cloud)

La infraestructura existe únicamente para una sola organización. Los servidores suelen estar en un centro de datos físico dentro del propio edificio de la empresa (por eso se llama "On-Premises" o "en las instalaciones").

* **La Analogía:** Es como **construir y ser dueño de tu propia casa**. Tú compras el terreno, pones los ladrillos y, si se rompe una tubería a las 3 de la mañana, es tu problema arreglarla. Sin embargo, tienes control absoluto sobre cada rincón de la casa.

* **Características Principales:**

	* **Control total:** Tú decides qué hardware comprar y cómo configurarlo a bajo nivel.

	* **Seguridad y Cumplimiento:** Algunas empresas (como bancos o gobiernos) la usan por leyes estrictas que prohíben que los datos salgan de sus edificios.

	* **Alto coste inicial (CapEx):** Tienes que comprar los servidores por adelantado, pagar la electricidad, el aire acondicionado y contratar personal para mantenerlos.

## 3. Nube Híbrida (Hybrid Cloud)

Es la combinación de las dos anteriores. La empresa mantiene algunos servidores en su propio centro de datos (Local) y, al mismo tiempo, conecta esa red a la Nube Pública (AWS) para usar sus servicios.

* **La Analogía:** Tienes tu **casa propia (Local)**, pero cuando vienen 20 familiares de visita por Navidad y no caben, **alquilas habitaciones en el hotel de enfrente (Nube Pública)** para que duerman allí. Todo funciona como una sola familia.

* **Características Principales:**

	* **Transición:** Es el modelo más usado por grandes empresas que tienen sistemas antiguos de hace 20 años que no pueden mover a AWS, pero quieren crear sus nuevas aplicaciones en la nube.

	* **Flexibilidad:** Puedes guardar los datos ultrasecretos en tu nube privada, y usar la nube pública para la página web que recibe millones de visitas.
	
* **Ejemplo en AWS:** Usar **AWS Direct Connect** (un cable privado dedicado) para conectar el centro de datos de la empresa directamente con los servidores de AWS.

---

## 📊 Tabla Comparativa

| Característica | Nube Pública (AWS) | Nube Privada (Local/On-Prem) | Nube Híbrida |
| :--- | :--- | :--- | :--- |
| **Dueño del Hardware** | Proveedor (AWS) | La empresa | Ambos |
| **Gasto principal** | Operativo (OpEx) - Mensual | Capital (CapEx) - Inicial | Combinado |
| **Mantenimiento** | Lo hace el proveedor | Lo hace tu equipo de TI | Compartido |
| **Escalabilidad** | Prácticamente ilimitada | Limitada a lo que hayas comprado | Alta (usando la parte pública) |

---
# 🌍 Ejemplos Reales: Modelos de Despliegue

> [!example] 1. Caso Nube Pública: "Epic Games" (Fortnite) o "Netflix"
> **Empresas que nacieron en la era digital o que necesitan estar en todo el mundo al mismo tiempo.**
> 
> * **La Situación:** Fortnite tiene picos locos de jugadores (ejemplo: un evento en vivo donde entran millones de golpe) y luego vuelve a la normalidad.
>
> * **¿Por qué Nube Pública?** Sería una locura económica comprar 100,000 servidores físicos solo para un evento de 15 minutos y luego tenerlos apagados. Usan AWS para encender y apagar recursos bajo demanda.
>
> * **Servicios AWS que usan:**
> 	
> 	* **Amazon EC2 / AWS Fargate:** Para alojar los servidores de las partidas multijugador que se crean y destruyen en minutos.
> 	
> 	* **Amazon S3:** Para guardar los parches del juego, las skins y los videos que los jugadores descargan.
> 	
> 	* **Amazon DynamoDB:** Una base de datos ultrarrápida (NoSQL) para guardar el inventario y progreso de millones de jugadores en milisegundos.

---

> [!example] 2. Caso Nube Privada (Local): "Hospital General" o "Ministerio de Defensa"
> **Instituciones tradicionales o con leyes de privacidad de datos extremas.**
> 
> * **La Situación:** Un hospital regional maneja historiales médicos. Por la ley de su país, los datos de los pacientes no pueden salir del edificio bajo ninguna circunstancia.
>
> * **¿Por qué Nube Privada?** Porque la ley no les deja otra opción, o porque las máquinas de resonancia magnética necesitan latencia cero absoluta con el servidor del pasillo de al lado.
>
> * **¿Qué usan aquí?**
> 	
> 	* Hardware tradicional: Compran servidores físicos (marcas como Dell o HP) y usan software como VMware.
> 	
> 	* **El toque AWS (AWS Outposts):** Si el hospital quiere usar la tecnología de AWS, Amazon tiene un servicio llamado *Outposts*. Literalmente, Amazon mete un armario físico (un rack) con servidores de AWS *dentro* del hospital. Es la única forma de tener "AWS" 100% en local.

---

> [!example] 3. Caso Nube Híbrida: "Banco Tradicional" o "Aerolínea"
> **Empresas gigantes con 40 años de historia que están en plena "transformación digital".**
> 
> * **La Situación:** Un banco como Santander o BBVA tiene un ordenador central gigante (Mainframe) en su sótano con los saldos de todas las cuentas desde 1980. Es muy frágil y no lo pueden subir a la nube. Pero a la vez, quieren lanzar una App móvil súper moderna y rápida.
>
> * **¿Por qué Nube Híbrida?** Mantienen el sótano para lo viejo e intocable, y usan AWS para la App nueva.
>
> * **Servicios AWS que usan para "unir" los dos mundos:**
> 	
> 	* **AWS Direct Connect:** Contratan un cable de fibra óptica físico y privado que va desde una sede central de BBVA hasta el centro de datos de Amazon. No usan el internet público para que nadie pueda interceptar los datos bancarios.
> 	
> 	* **AWS Storage Gateway:** Un servicio que "engaña" a los servidores locales del banco haciéndoles creer que están guardando copias de seguridad en un disco duro local, pero en realidad se están enviando a un **Amazon S3** gigante en la nube.

---

---
→ Volver al índice: [[📂Nube/00 - Índice Nube|🪐 Nube]]
