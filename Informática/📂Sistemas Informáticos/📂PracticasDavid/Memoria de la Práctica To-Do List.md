## 1. El Objetivo Principal

Lo que busco con esta práctica no es solo hacer una lista de tareas que funcione, sino **hacerla bien hecha a nivel de arquitectura**.

El objetivo es separar la lógica de la aplicación (es decir, tener por un lado los metodos, en otro lado los aplicamos...) de la base de datos.

 La explicación al porque es muy sencilla, porque en esta práctica guardamos los datos en la memoria RAM (una base temporal). El problema de tenerlo ahí es que al apagar el pc se borran todos los datos. La cosa es que la semana que viene podríamos querer poner una base de datos MySQL real y gracias a esta estructura, si hacemos ese cambio, no tendremos que tocar ni una sola línea de nuestra lógica de negocio, solo cambiaremos una línea en la configuración.




## 2. Estructura del Proyecto

El código está organizado en paquetes para que cada cosa esté en su sitio. Nada de tenerlo todo mezclado.

![[Memoria de la Práctica To-Do List-12.png]]
 
 `org.example.model` → Aquí van las clases con sus datos (Atributos,getters,setters,constructor).
 
 `org.example.repository` → Aquí va todo lo relacionado con guardar,leer,borrar.
 
 `org.example.service` → Aquí va la lógica y las decisiones(Aplica validaciones).
 
 `org.example.controller` → Aquí va la conexión con el mundo exterior (Web/HTTP).
 
 `org.example.App` → Conectamos Repository,Service y Controller,configuramos Javalin con su puerto y endpoints..



## 3. Explicación de las Clases (Paso a paso)

Aquí explico para qué sirve cada archivo que he creado y qué hace por dentro.

### A. `Task.java` (El Modelo)

![[Memoria de la Práctica To-Do List-2.png]]

Es una clase simple (POJO) que representa una Tarea. Es donde se guardan los datos.,no contiene lógica

- **Atributos** `id`, `title` y `description`.
 
- **Detalle importante:** Le hemos puesto un constructor vacío y los Getters/Setters. Esto es obligatorio porque usamos una librería llamada **Jackson**. Jackson necesita ese constructor vacío para poder crear el objeto cuando le llega un JSON desde el frontend.

### B. `ITaskRepository.java` (La Interfaz)

![[Memoria de la Práctica To-Do List-3.png]]

Este es el contrato. Aquí no hay código en los metodos, solo se DEFINEN para luego usarlos en una clase que implemente esta interfaz (guardar, buscar todos, borrar).

- **Para qué sirve:** Sirve para que el resto de la aplicación no sepa si estamos usando memoria RAM o SQL. Solo saben que existe un repositorio que cumple estas reglas.


### C. `InMemoryTaskRepository.java` (La Implementación)

![[Memoria de la Práctica To-Do List-17.png]]![[Memoria de la Práctica To-Do List-5.png]]
Esta es la base de datos temporal (RAM) que usamos hoy.

* Usa un map con clave (id) y valor (el objeto Tarea) para guardar las tareas en la memoria RAM del ordenador.

* Como no tenemos base de datos real, usamos un `AtomicLong` para ir generando los IDs (1, 2, 3...) manualmente cada vez que guardamos algo.


### D. `TaskService.java` (El Servicio / Lógica)

![[Memoria de la Práctica To-Do List-6.png]]

La clase donde está toda la lógica de negocio.

Le pasamos a su constructor un `ITaskRepository` (la interfaz), no la clase de `InMemoryTaskRepository`. Esto es lo que nos permite cambiar la base de datos en el futuro sin tocar esta clase.
 
Esta clase recibe órdenes, valida que los datos estén bien (ej: que el título no esté vacío ya que es obligatorio) esto es necesario ya que repository solo sabe guardar,mostrar,borrar y ya pero el service está atento y comprueba en esos métodos si son obligatorios si no se pueden añadir mas de 10 tareas,si se puede borrar una tarea...
 

### E. `TaskController.java` (El Controlador)

![[Memoria de la Práctica To-Do List-18.png]]
![[Memoria de la Práctica To-Do List-19.png]]![[Memoria de la Práctica To-Do List-20.png]]

Es el encargado de hablar con el Frontend usando **Javalin**.

- **GET `/api/tasks`:** Pide la lista al servicio y la convierte a JSON para enviarla.
 
- **POST `/api/tasks`:** Recibe un JSON, lo valida, lo convierte en un objeto `Task` y se lo pasa al servicio para crearlo.
 
- **DELETE `/api/tasks/{id}`:** Lee el ID de la URL y manda borrarlo.
 

### F. `App.java` (El Main)

![[Memoria de la Práctica To-Do List-13.png]]

Es donde conectamos todo.

1. Creamos el repositorio.
 
2. Creamos el servicio y le pasamos el repositorio.
 
3. Creamos el controlador y le pasamos el servicio.
 
4. Arrancamos Javalin en el puerto `8080` con el HTML dentro de la carpeta resources. 

![[Memoria de la Práctica To-Do List-14.png]]

Porque si abrimos el navegador desde el Intellij lo abre desde la biblioteca con la carpeta en que lo guarde y claro empieza a buscar /api/tasks desde el disco duro y no encuentra nada por eso me da este error.
![[Memoria de la Práctica To-Do List-15.png]]

Por eso el Javalin lo conectamos así ![[Memoria de la Práctica To-Do List-16.png]]
Porque con staticFiles funciona como un servidor para HTML,accede a resources/public y con Location.CLASSPATH le dice que no busque en la biblioteca si no que dentro del propio programa (resources).

Asi que el funcionamiento es el siguiente:
Escribimos `http://localhost:8080/index.html` en Chrome:

El navegador le dice servidor 8080 que le de el archivo `index.html`.
 
Javalin busca el HTML dentro de la carpeta resources/public porque se lo hemos indicado y ve que se encuentra el index.html y se lo pasa.
 
El navegador lee el HTML y ejecuta el Javascript de Vue, pero se da cuenta de que el script dice que pida datos a `/api/tasks`".
 
El navegador le pregunta ahora al servidor 8080 por la ruta `/api/tasks`.
 
Javalin le responde que eso no es un archivo, es un **Endpoint** que definió el usuario en el `Main`. Ejecuto `controller.getAll()` (por ejemplo).Después, le da los datos en formato JSON.



## 4. El Frontend y la Conexión

Para la parte visual hemos usado un archivo HTML sencillo con **Vue.js 3** y **Axios**.

- **Vue.js:** Se encarga de pintar la lista de tareas en la pantalla y de reaccionar cuando pulso botones (como el de borrar).
 
- **Axios:** Es el mensajero. Vue le dice que envie cierta tarea al servidor, y Axios hace la petición HTTP (POST, GET, DELETE) a nuestro backend en `http://localhost:8080/api/tasks`.
 

**Cómo probar que todo funciona:**

1. Arranco la `App.java` en IntelliJ.
 
2. Pongo `http://localhost:8080/index.html` en mi navegador.
 
3. Escribo "Estudiar Cloud" en el titulo y le doy a crear. Se aplica en el front y en el back.
 
4. Entramos a `http://localhost:8080/api/tasks` y verás algo la tarea en formato JSON. 

![[Memoria de la Práctica To-Do List-11.png]]

