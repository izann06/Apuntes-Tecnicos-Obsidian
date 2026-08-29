# **Objetivo del proyecto

El objetivo es crear un **API RESTful simulada (mock)** usando **Javalin**. Esto sirve para:

Aprender a manejar rutas (`GET`, `POST`, `PUT`, `DELETE`) en Javalin.

Trabajar con **JSON** para enviar y recibir datos.

Practicar la lógica de un CRUD **sin base de datos**.

Simular la persistencia de datos para pruebas rápidas.

---

# Cómo funciona y por qué no se ve nada en el navegador

Javalin **no genera páginas web automáticamente**.
 
Si abres `http://localhost:7000/` en un navegador, no verás la lista de usuarios ni un formulario, porque tu servidor **solo responde JSON a peticiones HTTP**.
 
Para “ver” los datos debes hacer peticiones de la siguiente manera:

Tenemos 4 métodos que nos ayudan a hacer el CRUD para los datos, con esto podemos crear,obtener,actualizar y borrar.

GET(OBTENER) 
POST(CREAR)
PUT(ACTUALIZAR)
DELETE (BORRAR)

Ahora tenemos que poner una ruta basicamente la tabla a la que queremos acceder.
Si queremos acceder a la tabla 'users' haremos:

/users

Para put y para delete tenemos que acceder si o si con algun atributo lo mejor es el id ya que es unico,si lo hacemos por nombre puede haber duplicados y podemos equivocarnos.

|Método HTTP|Ruta|Función|
|---|---|---|
|POST|/users|Crear un nuevo usuario|
|GET|/users|Obtener todos los usuarios|
|GET|/users/{id}|Obtener un usuario por ID|
|PUT|/users/{id}|Actualizar un usuario por ID|
|DELETE|/users/{id}|Eliminar un usuario por ID|

> Nota: Esto **simula un CRUD**, no usa base de datos, los datos son “mock” o generados al vuelo.




## Clases del proyecto

## `User.java` – Modelo de datos

![[Rest.png]]

- Representa un usuario con `id`, `name` y `email`.

---

## `Main.java` – Servidor y endpoints

![[Rest-1.png]]

- **Gson**: Se utiliza para convertir entre **JSON y objetos Java**.
 
 - Ejemplo: `ctx.body()` devuelve un JSON, `gson.fromJson(...)` lo convierte en un objeto `User`.
 
- **Random**: Genera IDs aleatorios para simular la creación de usuarios.
 
- Es **la clase principal** que arranca el servidor y contiene todos los endpoints del CRUD.

- **Crea el servidor Javalin** en el puerto `7000`.
 
- Define **5 rutas** que corresponden a un CRUD completo de usuarios:




![[Rest-4.png]]

- Recibe el JSON del **body** de la petición POST y lo convierte a un objeto `User`.
 
- Genera un **ID aleatorio** para simular la creación.
 
- Devuelve un JSON con `status`, `usuario` y `idAsignado`.
 
- **No guarda el usuario** en memoria, solo simula la respuesta.





![[Rest-5.png]]

- Devuelve una **lista de usuarios simulados**.
 
- Cada GET siempre devuelve los mismos usuarios “mock” (`Ana` y `Luis`).
 
- Este método **no refleja los usuarios creados con POST**, porque no se guardan en memoria.






![[Rest-6.png]]

- Recoge el **ID** de la URL (`{id}`).
 
- Devuelve un **usuario simulado** usando ese ID.
 
- Siempre crea un usuario al vuelo con `name = "Usuario Simulado {id}"` y email similar.






![[Rest-7.png]]


- Recibe el **ID** en la URL y el JSON con el nuevo usuario.
 
- No modifica nada en memoria; solo devuelve un mensaje indicando el “nuevo nombre”.
 
- Simula un PUT sin persistencia real.






![[Rest-8.png]]

- Recibe el **ID** de la URL.
 
- Simula la eliminación devolviendo un JSON con `status` y `id`.
 
- **No elimina ningún usuario**, porque no hay almacenamiento real.
 

---

# Resumen de cómo probar en **==CMD==**

1. **Crear usuario:**
 

`curl -X POST http://localhost:7000/users -H "Content-Type: application/json" -d "{\"name\":\"Carlos\",\"email\":\"carlos@gmail.com\"}"`

**Resultado:**
![[Rest-9.png]]

2. **Ver todos los usuarios:**
 

`curl http://localhost:7000/users`

**Resultado:**
![[Rest-10.png]]

3. **Ver un usuario por ID:**
 

`curl http://localhost:7000/users/123`

**Resultado:**

![[Rest-11.png]]

4. **Actualizar usuario:**

`curl -X PUT http://localhost:7000/users/123 -H "Content-Type: application/json" -d "{\"name\":\"Nuevo Nombre\",\"email\":\"nuevo@mail.com\"}"`

**Resultado:**

![[Rest-12.png]]

5. **Eliminar usuario:**
 

`curl -X DELETE http://localhost:7000/users/123`


**Resultado:**

![[Rest-13.png]]