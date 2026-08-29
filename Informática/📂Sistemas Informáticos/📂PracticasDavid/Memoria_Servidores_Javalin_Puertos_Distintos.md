# Memoria de la Práctica: Servidores Javalin en Distintos Puertos

# **No he podido hacer las capturas desde la mv ya que tuve problemas para hacerlo.**

## 1. ¿Qué hemos hecho? (Objetivo)

El objetivo de esta práctica es aprender a ejecutar el mismo programa dos veces a la vez, pero haciendo que cada uno se comporte de forma diferente. Queremos lanzar **dos servidores**:

- Uno que diga "Soy el Servidor 1" y funcione en el puerto **7000**.
 
- Otro que diga "Soy el Servidor 2" y funcione en el puerto **7001**.
 

Lo importante es que **no hemos creado dos archivos de código distintos**. Usamos el mismo archivo `.jar` para los dos, pero le pasamos la configuración (puerto y nombre) desde la consola al iniciarlo.

## 2. El Código Java (La clase Main)


![[Práctica Conectar puertos mediante Javalin-16.png]]
![[Práctica Conectar puertos mediante Javalin-17.png]]

Mas abajo estan los metodos de crear borrar...

Para no tener que escribir el puerto "a fuego" dentro del código, hemos usado los **argumentos (`args`)**.

- **¿Cómo funciona?** Cuando ejecutamos el programa, el código mira si le hemos pasado datos extra.
 
 - El primer dato lo usa como **Puerto** (ej: 7000).
 
 - El segundo dato lo usa como **Nombre** (ej: "Servidor 1").
 
- Luego, arrancamos Javalin con ese puerto (`.start(port)`) y creamos una ruta llamada `/version` que devuelve un mensaje saludando con el nombre del servidor.
 

## 3. Configuración de Maven (El problema del.jar vacío)

Para generar el archivo ejecutable, usamos Maven. Aquí tuvimos que solucionar dos problemas importantes en el archivo `pom.xml`:

1. **El "Fat Jar":** Por defecto, cuando Maven crea el archivo `.jar`, solo mete nuestro código, pero se deja fuera las librerías de Javalin. Al intentar ejecutarlo, daba error porque no encontraba las clases.
 
 - **Solución:** Añadimos un plugin llamado `maven-shade-plugin`. Esto mete **todo** (nuestro código + Javalin) en un solo archivo "gordo" (Fat Jar) que ya funciona por sí solo.
 
2. **La versión de Java:** Tuvimos que ajustar la versión en el `pom.xml` a la 21 para que fuera compatible con la versión de Java que tenemos instalada en la terminal (21) y no diera errores de versión ya que el compilador estaba con la 24.

3. ![[Práctica Conectar puertos mediante Javalin-4.png]]

Aqui esta todo el maven completo:

![[Práctica Conectar puertos mediante Javalin-18.png]]
![[Práctica Conectar puertos mediante Javalin-3.png]]
 

## 4. Creando el ejecutable (Clean y Package)

Para crear el archivo final, fuimos al panel de **Maven** (a la derecha en IntelliJ)
![[Práctica Conectar puertos mediante Javalin-5.png]]


Tienes que hacer doble click:

1. **`clean`:** Para borrar la carpeta `target` vieja y limpiar errores pasados. ![[Práctica Conectar puertos mediante Javalin-6.png]]
 
2. **`package`:** Para compilar y crear el nuevo archivo `.jar`.
![[Práctica Conectar puertos mediante Javalin-7.png]]
 

**¿Cómo sabemos que está bien?** Fuimos a la carpeta `target` y vimos que se creó un archivo llamado `conectarPuertosJavalin-1.0-SNAPSHOT.jar`
Comprobamos que **pesa bastante (unos 5 MB)**. Si pesara poco (unos KB), significaría que está vacío y no funcionaría.
El otro archivo que crea pesa 5kb.

![[Práctica Conectar puertos mediante Javalin-8.png]]


## 5. Ejecución (Lanzando los dos servidores)

Para la demostración, abrimos **dos terminales.

- Es muy importante **no cerrar ninguna de las dos**, porque si las cerramos, los servidores se apagan.
 

**En el servidor 1:** Fuimos a la terminal del IntellIJ

Entramos a target y ponemos: 
 java -jar conectarPuertosJavalin-1.0-SNAPSHOT.jar 7000 "Servidor 1"

![[Práctica Conectar puertos mediante Javalin-10.png]]

Resultado:

![[Práctica Conectar puertos mediante Javalin-11.png]]

**En la Terminal 2:** Abrimos la terminal CMD

Entramos a target y ponemos: 
 java -jar conectarPuertosJavalin-1.0-SNAPSHOT.jar 7001 "Servidor 2"

![[Práctica Conectar puertos mediante Javalin-12.png]]

Resultado:

![[Práctica Conectar puertos mediante Javalin-13.png]]

## 6. Comprobación Final

Con las dos terminales abiertas (IMPORTANTE) y funcionando, fuimos al navegador para ver si era verdad que funcionaban por separado:

1. Entramos a `http://localhost:7000/version` y vemos el mensaje del **Servidor 1**.

![[Práctica Conectar puertos mediante Javalin-14.png]]
 
2. Entramos a `http://localhost:7001/version` y vemos el mensaje del **Servidor 2**.
![[Práctica Conectar puertos mediante Javalin-15.png]]
 



