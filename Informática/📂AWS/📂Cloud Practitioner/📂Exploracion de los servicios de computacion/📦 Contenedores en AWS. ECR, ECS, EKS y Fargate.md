**Tags:** #aws #contenedores #docker #ecs #eks #fargate #computacion #cloud-practitioner #cp-exploracion-de-los-servicios-de-computacion

> [!summary] El fin del "¡En mi máquina sí funciona!"
> Los contenedores resuelven el problema de la portabilidad empaquetando tu código, sus dependencias y la configuración en una sola "caja" sellada. Si funciona en tu portátil, funcionará exactamente igual en AWS.

---
## 1. ¿Qué es un Contenedor?

A diferencia de una Máquina Virtual (como EC2) que emula todo un ordenador entero (con su propio y pesado sistema operativo), un contenedor es ligero. Solo contiene:

* El código de la aplicación.

* El entorno de ejecución (ej. Node.js o Python).

* Las bibliotecas y dependencias necesarias.

* *Ventajas:* Tiempos de inicio ultra rápidos (segundos), mejor eficiencia de recursos y portabilidad total.

---
## 2. El Almacén: Amazon ECR (Elastic Container Registry)

Antes de ejecutar un contenedor, necesitas un lugar seguro donde guardar la imagen (el molde o archivo base de tu contenedor). Asi que si usas contenedores este servicio es más que **obligatorio**.

* **Función:** Es un registro de contenedores completamente gestionado por AWS.

* **Analogía:** Es como un catálogo de IKEA. Subes los "planos" de tu aplicación ahí, y luego los otros servicios van a ese catálogo para descargarlos y montarlos.

---

## 3. Los Directores de Orquesta: ECS vs. EKS

Gestionar docenas de contenedores a mano (vigilar que no se caigan, enrutarlos, escalarlos) es una pesadilla. Por eso usamos **Orquestadores**, que son los gerentes que automatizan el ciclo de vida de los contenedores.Tienes que elegir usar uno de estos dos:

| Orquestador | ¿Qué significa? | ¿Cuándo elegirlo? |
| :--- | :--- | :--- |
| **Amazon ECS** | Elastic Container Service | Quieres la opción **nativa de AWS**. Es más simple, fácil de configurar y se integra perfectamente con otros servicios de Amazon. |
| **Amazon EKS** | Elastic Kubernetes Service | Quieres usar **Kubernetes** (una tecnología de código abierto estándar en la industria). Ideal para arquitecturas gigantescas o si quieres poder llevarte tu sistema a otra nube (multicloud/híbrido) sin cambiar nada. |

---

## 4. El Motor (Compute): EC2 vs. AWS Fargate

Una vez que el orquestador (ECS o EKS) decide que hay que arrancar un contenedor, ¿en qué hardware físico se ejecuta? Tienes dos opciones de motor:

* **Opción A: Amazon EC2 (Control Total)**

 * Tú creas y gestionas las máquinas virtuales (instancias EC2).

 * El orquestador coloca los contenedores dentro de tus máquinas.

 * *El problema:* Sigues teniendo que administrar, parchear y escalar los servidores por debajo.

* **Opción B: AWS Fargate (Serverless)**

 * Es el motor de computación **sin servidor** para contenedores.

 * No hay máquinas que gestionar. AWS provisiona el hardware invisiblemente en milisegundos. Es una MV también pero tu no la ves como en EC2.

 * *La ventaja:* Tú solo le dices a AWS: *"Tengo este contenedor, ejecútalo"*. Pura eficiencia y comodidad.

---

## 🔄 El Flujo de Trabajo (Resumen Práctico)

1. **Construyes** tu contenedor en tu portátil y lo subes a **Amazon ECR**.

2. **Eliges a tu gerente** (el orquestador): ¿Quieres lo simple de Amazon (**ECS**) o el estándar abierto de la industria (**EKS**)?

3. **Eliges el hardware** (compute): ¿Quieres gestionar tú los servidores base (**EC2**) o prefieres que AWS haga el trabajo sucio sin servidores (**Fargate**)?

---

---
→ Volver al índice: [[📂Exploracion de los servicios de computacion/00 - Índice Exploracion de los servicios de computacion|🪐 Exploracion de los servicios de computacion]]
