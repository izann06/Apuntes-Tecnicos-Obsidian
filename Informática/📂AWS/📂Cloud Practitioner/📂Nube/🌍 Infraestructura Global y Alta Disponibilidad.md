**Tags:** #aws #infraestructura #regiones #zonas-disponibilidad #alta-disponibilidad #cloud-practitioner #cp-nube

> [!summary] El Concepto Core
> La nube no es un lugar etéreo; son edificios físicos llenos de cables y ordenadores. AWS organiza estos edificios de mayor a menor escala en: **Regiones > Zonas de Disponibilidad > Centros de Datos.**

[Regiones y zonas de disponibilidad de la infraestructura global](https://aws.amazon.com/es/about-aws/global-infrastructure/regions_az/)
---

## 1. Regiones de AWS (El País / La Ciudad)

Una **Región** es una ubicación geográfica física en el mundo donde AWS tiene infraestructura. Son totalmente independientes y están aisladas unas de otras.

* **Ejemplos:** España (`eu-south-2`), Norte de Virginia (`us-east-1`), Tokio (`ap-northeast-1`).
### ¿Cómo eliges en qué Región poner tu juego o aplicación?

Para el examen, siempre hay **4 factores para elegir una región**:

1. **Cumplimiento legal (Compliance):** Si la ley europea exige que los datos médicos no salgan de Europa, eliges una región europea (ej. España o Frankfurt).

2. **Latencia (Proximidad):** Eliges la región más cercana a tus usuarios para que el juego vaya rápido y sin *lag*.

3. **Disponibilidad de servicios:** No todos los servicios nuevos de AWS están en todas las regiones al mismo tiempo. A veces tienes que ir a Virginia (`us-east-1`) porque es la región principal.

4. **Precio:** La luz y los impuestos no cuestan lo mismo en España que en Estados Unidos o Brasil. Correr un EC2 en Virginia suele ser más barato que en São Paulo.

---

## 2. Zonas de Disponibilidad (Las "AZs")

Aquí es donde la gente se confunde: **Una Región NO es un solo edificio.** 
Dentro de cada Región, AWS construye múltiples **Zonas de Disponibilidad (Availability Zones o AZs)**. Cada región tiene un mínimo de 3 AZs.

* **¿Qué es una AZ?** Es un conjunto de uno o más **Centros de Datos discretos**. 

* **El Aislamiento (La magia):** Las AZs dentro de una región están separadas físicamente por varios kilómetros (para que un terremoto, inundación o corte de luz no afecte a todas a la vez), pero están conectadas entre sí mediante fibra óptica ultra-rápida y privada.

> [!warning] Regla de Oro
> Si cae un rayo y destruye la **AZ "A"** de Madrid, la **AZ "B"** de Madrid sigue funcionando perfectamente porque tiene su propia red eléctrica y conexión a internet independiente.

---

## 3. Alta Disponibilidad (High Availability - HA)

La Alta Disponibilidad no es un servicio que compras, es una **arquitectura (una forma de construir)**. Significa que tu aplicación sigue funcionando sin interrupciones, incluso si un servidor, una base de datos o un edificio entero (AZ) explota.

* **La regla de diseño:** "Nunca pongas todos los huevos en la misma cesta".

* **El Modelo Multi-AZ:** En lugar de comprar un servidor gigante (EC2) y ponerlo en la AZ "A", compras dos servidores medianos: pones uno en la AZ "A" y otro en la AZ "B". Delante de ellos pones un **Balanceador de Carga** (que reparte a los usuarios).

* Esta parte la puedes configurar tu o la puede configurar AWS.

## 🌡️ La Analogía del Termostato

Imagina el aire acondicionado de tu casa:
* **El fabricante (AWS)** construyó el aparato para que eche aire frío automáticamente.
* **Tú (El Cliente)** tienes que ir al panel y decirle: *"Si la temperatura sube de 25°C, enciéndete. Si baja a 22°C, apágate"*.

En AWS funciona exactamente igual.

---

## 🛠️ Cómo funciona en la vida real (Paso a Paso)

### 1. Lo que configuras TÚ (Las Reglas)

Cuando creas tu entorno para el juego, entras a la consola de AWS y creas un "Grupo de Auto Scaling". Ahí tú tienes que configurar tres cosas básicas

1. **La Plantilla:** Le dices a AWS, *"Cuando necesites crear un servidor nuevo, quiero que sea tamaño `t2.micro` y que tenga instalado mi juego"*.

2. **Los Límites:** *"Quiero tener un **Mínimo** de 2 servidores siempre encendidos, pero un **Máximo** de 10 (para no arruinarme

3. **El Disparador (Trigger):** *"Si ves que la CPU de mis servidores pasa del 80% durante 5 minutos, crea 2 servidores nuevos"*.

### 2. Lo que hace AWS (La Magia / La Ejecución)

Una vez que tú guardas esa configuración, te vas a dormir. Ahora es el turno de AWS:

1. **Vigilar (Amazon CloudWatch):** AWS está mirando tus servidores cada segundo.

2. **Crear:** De repente entra un <i>streamer</i> famoso a tu juego. La CPU sube al 90%. AWS se da cuenta de que la regla se ha cumplido. Sin pedirte permiso, AWS lanza 2 servidores nuevos y los conecta al juego en segundos.

3. **Destruir:** Son las 4:00 AM, los jugadores se van a dormir. La CPU baja al 10%. AWS se da cuenta, apaga esos servidores extra y los borra para que dejes de pagar por ellos.

---

### Ejemplo:

Si tu servidor en la AZ "A" se quema, el Balanceador de Carga (ELB) se da cuenta de que no responde, y empieza a enviar a todos los jugadores al servidor de la AZ "B". **Tus jugadores no notan la caída, el juego sigue online.** A esto se le llama ser **Altamente Disponible**.

---

## 📊 Resumen

| Concepto | Qué es físicamente | Nivel de Fallo que soporta |
| :--- | :--- | :--- |
| **Centro de Datos** | Un edificio lleno de servidores. | Fallo de hardware local. |
| **Zona de Disponibilidad (AZ)** | 1 o más Centros de Datos independientes. | Inundación, apagón en una zona de la ciudad. |
| **Región** | Un grupo de (mínimo 3) AZs conectadas. | Un desastre a nivel nacional. |
| **Alta Disponibilidad (HA)** | Distribuir tu app en al menos 2 AZs. | Sobrevive a la muerte de un Centro de Datos/AZ. |

---

---
→ Volver al índice: [[📂Nube/00 - Índice Nube|🪐 Nube]]
