**Tags:** #vector-db #rag #opensearch #aurora #pgvector #neptune #ia #m3-genai

> [!quote] Contexto de Examen
> Para implementar la arquitectura RAG (Capa "Retrieve"), necesitas almacenar las "pegatinas matemáticas" (Embeddings). AWS ofrece varias opciones de bases de datos vectoriales. El examen probará tu capacidad para elegir la correcta según el caso de uso del cliente.

---

## 🗃️ Comparativa de Vector Stores en AWS

A la hora de guardar vectores y realizar búsquedas de similitud (*Nearest Neighbors*), usa esta tabla maestra de decisión:

| Servicio AWS | Cuándo usarlo (Palabras Clave de Examen) | Caso de Uso Ideal |
| :--- | :--- | :--- |
| **Amazon OpenSearch Service** | **Escala masiva**, búsqueda **híbrida** (texto exacto + similitud semántica), millones de documentos, concurrencia altísima. | Un e-commerce global que quiere añadir búsqueda semántica ("zapatos cómodos para correr") a su catálogo de 10 millones de productos. |
| **Amazon Aurora / RDS (con pgvector)** | **SQL**, base de datos relacional existente, sin necesidad de aprender nuevas herramientas, conveniencia. | Una empresa que ya usa PostgreSQL para su base de datos de usuarios y quiere añadir una columna vectorial a la misma tabla para evitar arquitecturas complejas. |
| **Amazon Neptune** | **Grafos**, **relaciones**, nodos interconectados. | Un sistema RAG legal o médico donde es vital entender cómo el "Documento A" referencia a la "Leyes B y C". Neptune Analytics mapea esas redes complejas. |
| **Amazon DocumentDB** | **JSON**, ecosistema **MongoDB**, datos no estructurados. | Una app moderna que guarda perfiles de usuario y logs en JSON y quiere añadirle capacidades vectoriales sin salir del ecosistema de documentos. |

> [!warning] La Trampa del Examen
> Si el caso del examen dice *"El equipo de desarrollo tiene muchísima experiencia en SQL y PostgreSQL y no tiene tiempo de aprender sistemas de búsqueda complejos"* ➔ La respuesta correcta **SIEMPRE** es Aurora/RDS con `pgvector`.
>
> Si el caso dice *"Se necesita búsqueda semántica pero el catálogo requiere una búsqueda exacta por nombre de marca (búsqueda híbrida) a una escala de petabytes"* ➔ La respuesta correcta es **OpenSearch**.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
