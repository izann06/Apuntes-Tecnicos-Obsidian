**Tags:** #aws #cp-exploracion-de-los-servicios-de-computacion

En esta gráfica se puede observar la capacidad de escalado en levantar contenedores respecto al tiempo. Vemos que la peor de todas es combinar ECS con EC2 ya que es la que más tarda y si necesitas levantar muchos contenedores rápidamente, esta, no es la mejor opción. Luego tenemos ECS con Fargate que es muy rápida, barata...

Y la mejor de todas la más rápida es Lambda, puede ser muy interesante utilizarla para levantar contendedores, pero ojo con el `Cold Start` tienes que "calentar" la Lambda antes **(Investigar)**. También recuerda que Lambda solo dura 15 minutos, por lo que si quieres levantar contenedores para más minutos o horas lo suyo sería ECS con Fargate.

![[Sin título-3.png]]

---

---
→ Volver al índice: [[📂Exploracion de los servicios de computacion/00 - Índice Exploracion de los servicios de computacion|🪐 Exploracion de los servicios de computacion]]
