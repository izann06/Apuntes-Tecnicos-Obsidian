**Tags:** #aws #ec2 #tipos-instancias #cloud-practitioner #cp-computacion

> **Nota:** Precios basados en Linux On-Demand en N. Virginia (us-east-1).

> [!info] ¿Qué significan las siglas?
> - **vCPU:** Núcleos de procesador virtual.
> - **GiB:** Memoria RAM en Gigabytes.
> - **GPU:** Tarjeta Gráfica (solo en Computación Acelerada).
## 1. Propósito General / Uso General (General Purpose)

Son el equilibrio perfecto. Tienen una proporción balanceada de procesador (CPU), memoria (RAM) y red. Son las más comunes para empezar.

* **La Analogía:** Es un **coche todoterreno (SUV)**. Sirve para ir a trabajar, para llevar a los niños o para un viaje por el campo. No es el mejor en nada, pero cumple en todo.

* **Letras de la Familia:** **M** (Majority/Mayoría), **T** (Tiny/Burstable), **Mac** (para macOS).

* **Casos de uso:** Servidores web básicos, repositorios de código, blogs en WordPress, entornos de desarrollo o pruebas.

* **Precio:** Moderado/Barato. Las de la familia `T` (como la `t2.micro`) son súper baratas e incluso entran en la capa gratuita.

| Nivel      | Nombre de Instancia | Especificaciones | Coste por Hora ($) | Coste Mensual ($)* |
| :--------- | :------------------ | :--------------- | :----------------- | :----------------- |
| **Barata** | `t3.nano`           | 2 vCPU, 0.5 GiB  | **$0.0052**        | ~$3.70             |
| **Media**  | `m5.large`          | 2 vCPU, 8 GiB    | **$0.0960**        | ~$70.00            |
| **Alta**   | `m5.24xlarge`       | 96 vCPU, 384 GiB | **$4.6080**        | ~$3,363.00         |

---

## 2. Optimizadas para Computación (Compute Optimized)

Tienen procesadores de altísimo rendimiento. Tienen mucha CPU en proporción a la memoria RAM.

* **La Analogía:** Es un **Fórmula 1**. No tiene mucho maletero (RAM), pero su motor (CPU) hace cálculos a la velocidad de la luz.

* **Letra de la Familia:** **C** (Compute).

* **Casos de uso:** Servidores de videojuegos multijugador, renderizado de vídeo 3D, simulaciones científicas, modelos de machine learning clásicos, procesamiento de transacciones masivas.

* **Precio:** Pagas un "extra" por tener procesadores de última generación a máxima frecuencia.

| Nivel      | Nombre de Instancia | Especificaciones  | Coste por Hora ($) | Coste Mensual ($)* |
| :--------- | :------------------ | :---------------- | :----------------- | :----------------- |
| **Barata** | `c6g.medium`        | 1 vCPU, 2 GiB     | **$0.0340**        | ~$24.80            |
| **Media**  | `c6i.2xlarge`       | 8 vCPU, 16 GiB    | **$0.3400**        | ~$248.00           |
| **Alta**   | `c6i.32xlarge`      | 128 vCPU, 256 GiB | **$5.4400**        | ~$3,971.00         |

---

## 3. Optimizadas para Memoria (Memory Optimized)

Diseñadas para cargar muchísima información directamente en la memoria RAM para procesarla súper rápido sin tener que buscarla en un disco duro lento.

* **La Analogía:** Es un **estudiante empollón**. Tiene una memoria fotográfica gigante y puede recordar miles de datos de golpe en su cabeza (RAM) sin mirar los libros (Disco).

* **Letra de la Familia:** **R** (RAM), **X** (eXtreme memory).

* **Casos de uso:** Bases de datos gigantes y de alto rendimiento (como Amazon RDS o bases en memoria como Redis/Memcached), análisis de Big Data en tiempo real.

* **Precio:** Alto, porque los chips de memoria RAM de grado servidor son de los componentes más caros del hardware.

| Nivel      | Nombre de Instancia | Especificaciones    | Coste por Hora ($) | Coste Mensual ($)* |
| :--------- | :------------------ | :------------------ | :----------------- | :----------------- |
| **Barata** | `r6g.medium`        | 1 vCPU, 8 GiB       | **$0.0504**        | ~$36.70            |
| **Media**  | `r6i.4xlarge`       | 16 vCPU, 128 GiB    | **$1.0080**        | ~$735.00           |
| **Alta**   | `r6i.32xlarge`      | 128 vCPU, 1.024 GiB | **$8.0640**        | ~$5,886.00         |

---

## 4. Optimizadas para Almacenamiento (Storage Optimized)

Diseñadas para acceder a miles de archivos en el disco duro a una velocidad vertiginosa. Tienen operaciones de lectura/escritura (IOPS) masivas.

* **La Analogía:** Es un **almacén gigante de logística (Amazon Fulfillment Center)**. Tiene cientos de puertas para que entren y salgan camiones (datos) constantemente sin atascos.

* **Letras de la Familia:** **I** (IOPS - Input/Output), **D** (Dense storage).

* **Casos de uso:** Bases de datos NoSQL gigantes, sistemas de archivos distribuidos, sistemas que guardan "logs" de millones de usuarios por segundo.

* **Precio:** Varía mucho según si usa discos SSD ultrarrápidos (Familia I) o discos duros mecánicos gigantes (Familia D).

| Nivel      | Nombre de Instancia | Especificaciones                | Coste por Hora ($) | Coste Mensual ($)* |
| :--------- | :------------------ | :------------------------------ | :----------------- | :----------------- |
| **Barata** | `i3.large`          | 2 vCPU, 15 GiB, 475 GB NVMe     | **$0.1560**        | ~$113.00           |
| **Media**  | `i4i.4xlarge`       | 16 vCPU, 128 GiB, 3.7 TB NVMe   | **$1.3840**        | ~$1,010.00         |
| **Alta**   | `i4i.32xlarge`      | 128 vCPU, 1.024 GiB, 30 TB NVMe | **$11.0720**       | ~$8,082.00         |

---

## 5. Computación Acelerada (Accelerated Computing)

Estas son las "bestias" de AWS. En lugar de usar solo CPUs tradicionales, usan coprocesadores de hardware físico súper potentes (como Tarjetas Gráficas - GPUs).

* **La Analogía:** Es una **planta de ensamblaje robótica**. Mientras un humano (CPU) hace una tarea a la vez, los robots (GPUs) pueden hacer miles de tareas diminutas y repetitivas exactamente al mismo tiempo.

* **Letras de la Familia:** **P** (Pictures/Gráficos), **G** (Graphics).

* **Casos de uso:** Entrenamiento de Inteligencia Artificial (ChatGPT se entrenó en cosas similares), Deep Learning, procesamiento de imágenes médicas, minería de criptomonedas, vehículos autónomos.

* **Precio:** **Altísimo**. Una instancia como la `p4d.24xlarge` puede costar más de $30 dólares... ¡por hora!

| Nivel      | Nombre de Instancia | Especificaciones                | Coste por Hora ($) | Coste Mensual ($)* |
| :--------- | :------------------ | :------------------------------ | :----------------- | :----------------- |
| **Barata** | `g4dn.xlarge`       | 4 vCPU, 16 GiB, 1x GPU T4       | **$0.5260**        | ~$383.00           |
| **Media**  | `p3.2xlarge`        | 8 vCPU, 61 GiB, 1x GPU V100     | **$3.0600**        | ~$2,233.00         |
| **Alta**   | `p4d.24xlarge`      | 96 vCPU, 1.152 GiB, 8x GPU A100 | **$32.7726**       | **~$23,924.00**    |

---

## 💡 Resumen de Familias
* **M** = **M**ayoría de las cosas (General)
* **C** = **C**omputación (CPU)
* **R** = **R**AM (Memoria)
* **I** / **D** = **I**OPS / **D**isco (Almacenamiento)
* **P** / **G** = **P**ictures / **G**raphics (Acelerada/GPU)

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
