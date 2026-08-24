**Tags:** #aws #elb #load-balancer #escalabilidad #alta-disponibilidad #redes #cloud-practitioner #cp-computacion

> [!summary] El Director de Tráfico (El Anfitrión)
> Un Balanceador de Carga (ELB) es el servicio que recibe todo el tráfico de internet y lo reparte de forma inteligente y equitativa entre todos tus servidores EC2 para que ninguno se sature ni se quede inactivo.

---

## 1. El Problema que Resuelve el ELB

Imagina un restaurante con 5 cajeros (5 servidores EC2). Si los clientes (el tráfico) eligen la fila que quieren, algunos cajeros tendrán colas larguísimas y otros estarán cruzados de brazos.

*   **Problema sin ELB:** Tienes que decirle a cada cliente la IP exacta del servidor al que debe conectarse. Si añades un servidor nuevo, tienes que avisar a todo el mundo de que existe.

*   **Solución con ELB:** Pones a un Anfitrión en la puerta del restaurante. Los clientes solo hablan con el Anfitrión (tienen una única URL o IP). El Anfitrión mira qué cajero está más libre y envía al cliente allí de forma invisible.

---

## 2. Beneficios Clave del ELB

1.  **Punto de Contacto Único:** Oculta la complejidad de tu flota de servidores. El cliente solo ve el equilibrador de carga.

2.  **Alta Disponibilidad:** Si el ELB detecta que un servidor EC2 se ha "roto" (falla las comprobaciones de estado), deja de enviarle tráfico automáticamente y lo desvía a los servidores sanos.

3.  **Desacoplamiento (Decoupling):** Permite separar el *Front-End* (lo que ve el usuario) del *Back-End* (bases de datos/procesamiento). Cada nivel escala por su cuenta sin interrumpir al otro.
	1. MAL: ![[⚖️ Elastic Load Balancing (ELB).png]]
4. Porque cada Front-End(Azul) debe estar conectado a todos los backend y asi sucesivamente, es una locura a gran escala.
	1. BIEN: ![[⚖️ Elastic Load Balancing (ELB)-1.png]]
	2. De esta manera, conectamos todo a ELB y el se encarga de manejar que back está libre para conectarlo en ese momento con ese front.

---

## 3. ¿Cómo decide el ELB a quién enviarle el tráfico? (Métodos de Enrutamiento)

El ELB es inteligente y usa algoritmos para repartir la carga. Estas son las siguientes  estrategias:

*   **Round Robin (El Cíclico):** Reparte como barajando cartas: uno para el Servidor A, uno para el B, uno para el C, y vuelta al A.

*   **Conexión Mínima (Least Outstanding Requests):** Manda al nuevo cliente al servidor que tiene menos trabajo *activo* en ese momento.

*   **Tiempo de Respuesta Mínimo:** Manda al cliente al servidor que está contestando más rápido (el que tiene menor latencia).

*   **Hash de IP (Sticky Sessions / Sesiones Persistentes):** Se asegura de que el Usuario 1 vaya **siempre** al mismo servidor durante toda su visita. (Útil si tienes un "carrito de la compra" que no está guardado en una base de datos central).

### 🚦 ¿Cuándo elegir cada método de enrutamiento?

|**Método**|**¿Cuándo es el mejor?**|**Razón principal**|
|---|---|---|
|**Round robin**|Cuando todas las solicitudes son **iguales y rápidas**.|Distribuye el tráfico de forma cíclica y uniforme entre todos los servidores. Es el más sencillo.|
|**Conexión mínima**|Cuando algunas solicitudes son **más pesadas** que otras.|Dirige el tráfico al servidor con menos conexiones activas para evitar que uno se sature mientras otros están libres.|
|**Hash de IP**|Cuando necesitas que un usuario **vuelva siempre al mismo servidor**.|Usa la IP del cliente para enrutarlo siempre al mismo sitio. Es vital si tu app guarda datos temporales solo en la memoria de esa máquina.|
|**Tiempo de respuesta mínimo**|Cuando la **velocidad de carga** es tu prioridad absoluta.|Envía al usuario al servidor que responde más rápido, minimizando la latencia para el cliente.|

---

## 🤝 4. El Combo Ganador: ELB + Auto Scaling

| Servicio                         | ¿Cuál es su trabajo? | Acción                                                          |
| :------------------------------- | :------------------- | :-------------------------------------------------------------- |
| **Amazon EC2 Auto Scaling**      | El "Constructor".    | **Crea y destruye** servidores EC2 según la demanda.            |
| **Elastic Load Balancing (ELB)** | El "Repartidor".     | **Distribuye el tráfico** entre los servidores que estén vivos. |

*Ejemplo de funcionamiento conjunto:*

1.  Viene un pico de tráfico (Black Friday).
2.  **Auto Scaling** detecta la carga y enciende 3 servidores nuevos.
3.  Los servidores nuevos le dicen al **ELB**: *"¡Eh, ya estoy listo!"*
4.  El **ELB** empieza a mandarles clientes inmediatamente, sin que el usuario final note ningún corte.

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
