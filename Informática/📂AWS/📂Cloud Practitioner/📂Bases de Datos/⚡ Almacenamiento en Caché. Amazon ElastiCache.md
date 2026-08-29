**Tags:** #aws #elasticache #caching #redis #memcached #base-de-datos #cloud-practitioner #cp-bases-de-datos

> [!summary] El Concepto Clave
> Ir a buscar un dato al disco duro de una base de datos lleva "tiempo" (milisegundos). Ir a buscar un dato a la memoria RAM lleva **microsegundos**. **Amazon ElastiCache** es una capa de memoria RAM superrápida **(caché)** que se coloca delante de tu base de datos para guardar las respuestas a las preguntas más frecuentes.

---
## 🧠 1. ¿Qué es una Caché en Memoria?

* **El Problema:** Imagina que eres un estudiante (la aplicación web) y le preguntas a tu profesor (la base de datos RDS) el resultado de `1234 * 5678`. El profesor saca una libreta, lo calcula (lee el disco duro) y te dice la respuesta. Si 1.000 estudiantes le preguntan lo mismo en el mismo minuto, el profesor se agobia y se bloquea (Cuello de botella).

* **La Solución (La Caché):** Pones un asistente (ElastiCache) en la puerta del aula. La primera vez que alguien pregunta, el asistente va al profesor, consigue la respuesta y **se la aprende de memoria**. A partir de ahí, a los siguientes 999 estudiantes se lo responde el asistente al instante (desde la memoria RAM), sin molestar al profesor.

---

## 🚀 2. Amazon ElastiCache (El Servicio de AWS)

Es un servicio *completamente administrado*. Tú no instalas el software; AWS te levanta los servidores de caché y los mantiene por ti.

### Motores Compatibles 

ElastiCache no inventa un software nuevo, sino que administra los dos motores de caché de código abierto más famosos del mundo:

1. **Redis (o Valkey):** Muy potente, admite estructuras de datos complejas (listas, conjuntos) y permite guardar los datos en disco si quieres que sobrevivan a un reinicio.

2. **Memcached:** Muy simple, puramente para guardar pares clave-valor temporales en memoria.

### El Flujo de Datos Típico (Lazy Loading)

1. El usuario (Cliente) pide ver el perfil de un jugador.

2. La Instancia EC2 (Aplicación) primero mira en **ElastiCache**.

3. *¿Está ahí? (Cache HIT):* EC2 se lo envía al cliente al instante.

4. *¿No está? (Cache MISS):* EC2 va a buscarlo a **Amazon RDS/DynamoDB**, se lo devuelve al cliente y, de paso, **guarda una copia en ElastiCache** para la próxima vez.

---

## 🎯 3. Casos de Uso Comunes

* **Tablas de clasificación de videojuegos (Leaderboards):** Todos quieren ver el Top 10 en tiempo real. Consultarlo en la base de datos cada segundo es muy costoso; se guarda en caché (Redis es el rey de esto).

* **Gestión de Datos de Sesión:** Cuando navegas por un E-commerce, el carrito de la compra temporal (que expira si cierras el navegador) se suele guardar en ElastiCache porque es rapidísimo.

* **Resultados de consultas de base de datos:** Para aliviar la carga de lectura de un RDS que sufre por tener demasiados visitantes.

---

## 🛡️ 4. Beneficios Clave

* **Velocidad Extrema:** Reduce la latencia a **microsegundos**.

* **Ahorro de Costes:** Al quitarle la carga de "lectura" a tu base de datos principal, puedes usar un servidor de base de datos más pequeño y barato.

* **Alta Disponibilidad:** Admite **Replicación Multi-AZ**. Si el servidor de caché principal cae, AWS promueve una réplica automáticamente para que la aplicación no sufra un bajón de rendimiento de golpe.

---

---
→ Volver al índice: [[📂Bases de Datos/00 - Índice Bases de Datos|🪐 Bases de Datos]]
