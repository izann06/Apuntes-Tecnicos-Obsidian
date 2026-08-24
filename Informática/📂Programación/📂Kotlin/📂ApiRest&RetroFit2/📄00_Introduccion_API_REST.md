## 1. ¿Qué es una API REST?

API significa **Application Programming Interface**.

REST significa **Representational State Transfer**.

**Api Rest** es el **puente** o el **mensajero** que permite que dos sistemas informáticos (Front y Back) hablen entre sí, aunque estén programados en lenguajes diferentes.

> [!NOTE] Analogía del Restaurante 🍽️
> 
> - **Tu App (Cliente):** Eres tú sentado en la mesa. Tienes hambre (necesitas datos) pero no puedes entrar a la cocina.
>     
> - **La API (Camarero):** Es el intermediario. Toma tu pedido ("Solomillo con patatas y pimiento"), lo lleva a la cocina y te trae la comida.
>     
> - **El Servidor (Cocina):** Es donde se preparan y guardan los datos (Base de Datos). Tú nunca ves la cocina, solo recibes lo que el camarero te trae.
>     

---

## 2. ¿Cómo nos comunicamos? (Verbos HTTP)

Para hablar con la API, usamos el protocolo **HTTPS**. No podemos decir cualquier cosa, tenemos que usar unos "verbos" o acciones específicas:

|**Verbo**|**Acción (CRUD)**|**Descripción**|**Ejemplo**|
|---|---|---|---|
|**GET**|**Read** (Leer)|Pide información al servidor. No modifica nada.|_Dame la lista de usuarios._|
|**POST**|**Create** (Crear)|Envía datos nuevos al servidor para guardarlos.|_Publicar un nuevo tweet._|
|**PUT**|**Update** (Actualizar)|Reemplaza un registro existente por uno nuevo.|_Editar mi perfil completo._|
|**DELETE**|**Delete** (Borrar)|Elimina un registro de la base de datos.|_Borrar una foto._|

---

## 3. El Idioma: JSON

La API y tu App no hablan español ni inglés, hablan **JSON** (_JavaScript Object Notation_). Es un formato de texto ligero basado en **Clave-Valor**.

**Ejemplo de respuesta JSON:**

JSON

```
{
  "id": 1,
  "nombre": "Juan Pérez",
  "esEstudiante": true,
  "hobbies": ["Fútbol", "Programación"]
}
```

- **Claves:** Van entre comillas (`"nombre"`).
    
- **Valores:** Pueden ser números, texto, booleanos o listas (`[]`).
    

---

## 4. La Estructura de la URL

Para hacer una petición, necesitamos una dirección web exacta. Se compone de dos partes:

`https://jsonplaceholder.typicode.com/posts/1`

1. **Base URL:** `https://jsonplaceholder.typicode.com/`
    
    - Es la dirección del servidor (la casa).
        
    - Siempre termina en `/`.
        
2. **Endpoint:** `posts/1`
    
    - Es el recurso específico que queremos (la habitación).
    - En este caso le estamos diciendo que nos envie el post con id = 1.

---

## 5. Códigos de Estado (Status Codes)

Cuando la API responde, nos envía un número para decirnos cómo ha ido la operación.

- 🟢 **200 OK:** Todo salió bien. Aquí tienes tus datos.
    
- 🟢 **201 Created:** Todo bien, he creado lo que me pediste.
    
- 🔴 **400 Bad Request:** Tu petición está mal formulada (te falta un dato).
    
- 🔴 **401 Unauthorized:** No tienes permiso (te falta el token/login).
    
- 🔴 **404 Not Found:** Lo que buscas no existe (URL mal escrita o ID incorrecto).
    
- 🔥 **500 Internal Server Error:** Culpa del servidor (se rompió algo en el back).
    

---

### Resumen

Una **API REST** usa el protocolo **HTTP** para enviar y recibir **JSON**. Usamos **Retrofit** en Android para manejar esta comunicación sin tener que escribir todo el código de conexión a mano.