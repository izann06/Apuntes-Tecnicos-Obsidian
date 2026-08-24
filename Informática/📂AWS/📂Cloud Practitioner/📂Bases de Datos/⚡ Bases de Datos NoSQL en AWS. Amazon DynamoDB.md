**Tags:** #aws #base-de-datos #dynamodb #nosql #serverless #cloud-practitioner #cp-bases-de-datos

> [!summary] El Concepto Clave
> Las bases de datos NoSQL abandonan la estructura rígida de filas y columnas. Permiten guardar datos en formato "Clave-Valor" (como un diccionario). **Amazon DynamoDB** es la base de datos NoSQL de AWS: es Serverless (no hay servidores que administrar), escala de forma infinita automáticamente y siempre responde en milisegundos.

---

## 🧩 1. ¿Qué es una Base de Datos NoSQL? (El Esquema Flexible)

* **El Problema del SQL Tradicional:** Si tienes una tabla de "Clientes" con Nombre, Dirección y Teléfono, y mañana quieres añadir el "Color Favorito" a un cliente nuevo, en SQL tienes que alterar la estructura de *toda* la tabla para todos los clientes (dejando el hueco en blanco para los que no tienen color favorito). Es rígido.

* **La Solución NoSQL (Clave-Valor):** No hay un esquema fijo. Cada registro (Elemento) es independiente.

    * *Elemento 1:* `{ID: 1, Nombre: "Juan", Teléfono: "555-1234"}`
    * *Elemento 2:* `{ID: 2, Nombre: "Ana", Edad: 30, Color_Favorito: "Azul", Mascotas: ["Perro", "Gato"]}`
    
    * *¡Fíjate!* El Elemento 2 tiene datos completamente diferentes al Elemento 1, y ambos viven felices en la misma base de datos.

---

## 🚀 2. Amazon DynamoDB: El Cohete de AWS

Amazon DynamoDB es un servicio de base de datos NoSQL *completamente administrado*.

### Los Superpoderes de DynamoDB

1.  **Rendimiento Inferior a 10 Milisegundos:** No importa si tu base de datos tiene 10 megabytes o 100 terabytes. DynamoDB está diseñado para que cualquier búsqueda tarde menos de 10 milisegundos (un solo dígito).

2.  **Serverless (Sin Servidor):** No hay máquinas EC2 que aprovisionar. No hay sistemas operativos que actualizar. Solo creas una tabla y empiezas a escupirle datos.

3.  **Escalado Infinito y Automático:** Configuras la *capacidad aprovisionada con escalado automático*. Si de repente tienes un pico de tráfico (como en el Amazon Prime Day, con 146 millones de peticiones *por segundo*), DynamoDB añade potencia por detrás de forma invisible para que la base de datos no se caiga.

4.  **Tablas Globales:** Con un par de clics, DynamoDB replica tu base de datos en múltiples Regiones de AWS en todo el mundo. Así, un usuario en Japón lee los datos desde Tokio y un usuario en España lee desde Madrid, logrando una latencia casi nula.

---

## 🎯 3. Casos de Uso 

DynamoDB es ideal para aplicaciones que necesitan escupir o leer datos masivos a la velocidad del rayo, sin importar cómo evolucionen esos datos en el futuro.

| Cuándo USAR DynamoDB (NoSQL) | Cuándo NO USAR DynamoDB (Usa RDS/SQL) |
| :--- | :--- |
| **Videojuegos Online:** Guardar puntuaciones, inventarios de jugadores o perfiles (donde cada jugador puede tener objetos distintos). | **Sistemas de Contabilidad / ERPs:** Donde necesitas transacciones complejas que afecten a 5 tablas diferentes a la vez (ej. Restar dinero, actualizar factura, actualizar stock). |
| **Carritos de la compra en E-commerce:** Guardar sesiones temporales a gran velocidad. | **Consultas complejas:** (ej. "Dime todos los usuarios mayores de 30 años que compraron un producto X en enero y viven en Madrid"). NoSQL es malo para esto. |
| **Aplicaciones Móviles o IoT:** Dispositivos (sensores, termostatos) enviando ráfagas constantes de datos no estructurados. | **Esquemas rígidos y definidos:** Si tus datos nunca cambian de formato y las relaciones entre ellos son vitales. |

---

---
→ Volver al índice: [[📂Bases de Datos/00 - Índice Bases de Datos|🪐 Bases de Datos]]
