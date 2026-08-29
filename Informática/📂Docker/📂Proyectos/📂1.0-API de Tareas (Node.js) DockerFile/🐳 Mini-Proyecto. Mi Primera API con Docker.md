> [!info] Metadatos
> 
> **Fecha:** 2026-08-17
> 
> **Tecnologías:** Docker, Node.js
> 
> **Conceptos:** Dockerfile, Contenedores, Puertos, CLI
> 
> 

## 🎯 Objetivo del Proyecto

El objetivo de este miniproyecto es construir un servidor web minimalista utilizando Node.js puro (sin librerías externas ni `package.json`) y empaquetarlo dentro de un contenedor de Docker. Esto permite aislar la aplicación de nuestro sistema operativo principal, asegurando que funcione exactamente igual en cualquier otra máquina.

## 🧠 Conceptos Clave

Para entender el flujo de trabajo, hay que diferenciar tres elementos fundamentales:

1. **Dockerfile (La Receta):** Es un archivo de texto con instrucciones paso a paso. Define qué sistema operativo base usar, cómo copiar los archivos y qué comandos ejecutar. 
 
2. **Imagen (El Molde):** Es el resultado inmutable de compilar el Dockerfile (`docker build`). No consume RAM, es un empaquetado estático. 
 
3. **Contenedor (La App Viva):** Es la instancia en ejecución de la imagen (`docker run`). Es el proceso real que corre aislado en la máquina.
 
## 🛠️ Paso a Paso

### 1. El Código Fuente (`servidor.js`)

Este es el archivo principal de nuestra aplicación. Crea un servidor HTTP básico que responde con un texto.

```JavaScript
const http = require('http');

const server = http.createServer((req, res) => {
 res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
 res.end('¡Hola! Estoy corriendo en un contenedor creado SOLO con un Dockerfile.\n');
});

server.listen(3000, () => {
 console.log('Servidor funcionando en el puerto 3000');
});
```

### 2. El Manifiesto (`Dockerfile`)

Este archivo se debe llamar exactamente `Dockerfile` (sin extensión) y debe estar en la misma carpeta que `servidor.js`.

```Dockerfile
#1. Usar Node.js
FROM node:20-alpine

#2. Carpeta de Trabajo que se crea dentro del contenedor (aislado del PC)
# Sirve para no tirar nuestros archivos en la raíz del sistema operativo Linux.
WORKDIR /app

#3. Copiar solo nuestro archivo al contenedor, al ser uno ponemos su nombre
# Si hubiera más archivos, usaríamos COPY.. para copiarlos TODOS
COPY server.js.

#4. Abrir el puerto 3000 (Puerto del Contenedor)
# Luego con -p 3000:3000 lo "engancharemos" al PC
EXPOSE 3000

#5 Ejecutar el código
CMD ["node", "server.js"]
```

## 💡 Análisis de Dudas y Conceptos del Dockerfile

> [!question] ¿Dónde se crea la carpeta `/app` y para qué sirve?
> 
> El comando `WORKDIR /app` crea esta carpeta **dentro de la máquina virtual (el contenedor)**, no en tu PC. Sirve para mantener el orden y no mezclar nuestros archivos (`servidor.js`) con las carpetas del sistema operativo Linux (`/bin`, `/etc`, etc.). Todo lo que ocurra después de esta línea, se ejecutará dentro de esa carpeta.
> 
> 

> [!question] El puerto del `EXPOSE`, ¿es el de mi PC o el del contenedor?
> 
> Es **100% interno del contenedor**. `EXPOSE 3000` es solo una etiqueta informativa que le dice a Docker: _"El código por dentro está usando este puerto"_. No abre automáticamente ningún puerto en tu ordenador real. La conexión hacia fuera se hace más tarde con el comando de ejecución.
> 
> 

> [!question] ¿Qué se pone en el `CMD`? ¿Y si hay más archivos?
> 
> En el `CMD` va **el comando para arrancar tu programa**. Si tuvieras más archivos (ej. rutas, controladores), el `CMD` seguiría siendo el mismo: `["node", "servidor.js"]`, ya que este archivo principal se encargará de llamar a los demás.
> 
> _Nota:_ Para copiar múltiples archivos al contenedor, cambiaríamos la instrucción COPY a `COPY..` (Copia todo desde tu PC hacia el contenedor).
> 
> 

## 💻 Comandos y Ejecución

### 1. Construir la Imagen (Build)

Situados en la terminal dentro de la carpeta del proyecto, ejecutamos:

```Bash
docker build -t mi-primer-dockerfile.
```

_(El `-t` asigna un nombre a la imagen, y el `.` final indica que el Dockerfile está en la carpeta actual)._

### 2. Levantar el Contenedor (Run)

Para iniciar la aplicación liberando nuestra terminal y conectando los puertos:

```Bash
docker run -d -p 3000:3000 mi-primer-dockerfile
```

- **`-d` (Detached):** Ejecuta el contenedor en segundo plano, devolviéndote el control de la terminal inmediatamente. 
 
- **`-p 3000:3000` (Port):** Mapea el puerto `[Tu_PC]:[Contenedor]`. Conecta el puerto 3000 de tu ordenador local al puerto 3000 interno del contenedor. 
 
## ⚠️ Resolución de Problemas Comunes

> [!warning] Error: `port is already allocated` (Bind for 0.0.0.0:3000 failed)
> 
> Este error ocurre cuando intentas lanzar un contenedor, pero el puerto 3000 de tu ordenador ya está ocupado por un contenedor antiguo que se quedó corriendo en segundo plano.
> 
> 
> 
> **Solución:**
> 
> 
> 
> 1. Ejecuta `docker ps` para listar los contenedores activos.
> 
> ![[🐳 Mini-Proyecto. Mi Primera API con Docker.png]]
> 
> 2. Copia el **Container ID** del que está usando el puerto 3000.
> 
> 
> 
> 3. Ejecuta `docker stop <CONTAINER_ID>`.
> 
> 
> 
> 4. Vuelve a lanzar tu comando `docker run`.
> 
> 
> 

> [!faq] ¿Qué pasa si cambio algo en el código (`servidor.js`)?
> 
> Las imágenes de Docker son **inmutables** (como una fotografía). Si cambias tu código, el contenedor no se enterará. Debes seguir este flujo:
> 
> 
> 
> 1. **Apagar** el contenedor actual (`docker stop <ID>` o `Ctrl+C`).
> 
> 
> 
> 2. **Reconstruir** la imagen con los nuevos cambios (`docker build -t mi-primer-dockerfile.`).
> 
> 
> 
> 3. **Volver a ejecutar** el contenedor (`docker run -d -p 3000:3000 mi-primer-dockerfile`).
>