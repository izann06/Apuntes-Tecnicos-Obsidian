
> [!info] Metadatos 
> **Fecha:** 2026-08-17
> **Tecnologías:** Docker Compose, Node.js
> **Conceptos:** Orquestación, `docker-compose.yml`, Volúmenes (Bind Mounts), Mapeo de Puertos

## 🎯 Objetivo del Proyecto

Evolucionar nuestro contenedor individual para que sea gestionado por **Docker Compose**. Esto resuelve tres problemas principales:

1. Dejar de escribir comandos de terminal larguísimos y guardarlo todo en un archivo (`IaC`).
 
2. Sincronizar nuestro código en tiempo real usando **Volúmenes** (sin tener que reconstruir la imagen en cada cambio).
 
3. Entender y dominar la comunicación de red y los puertos entre el PC físico y el contenedor.
 

## 🛠️ Archivos Necesarios

Tu proyecto solo necesita estos 3 archivos en la misma carpeta:

### 1. El Código Fuente (`server.js`)

Un servidor HTTP básico en Node.js, esta vez configurado para escuchar en el puerto `3000.

```JavaScript
const http = require('http');

const server = http.createServer((req, res) => {
 res.writeHead(200, { 'Content-Type': 'text/plain' });
 res.end('En este proyecto estoy usando Docker Compose y sincroniza mi código en tiempo real.\n');
});

server.listen(3000, () => {
 console.log('Server running on port 3000');
});
```

### 2. El Manifiesto (`Dockerfile`)

Mantenemos la misma receta, pero actualizando el puerto expuesto para que coincida con el código.

```Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY server.js.
EXPOSE 3000
CMD ["node", "server.js"]
```

### 3. El Orquestador (`docker-compose.yml`)

Este archivo reemplaza al comando `docker run`. Aquí definimos los servicios, los puertos y los volúmenes.

```YAML
services: #Aquí se definen todos los contenedores que quieres usar

 mi-api-node: #Nombre inventado para este contenedor
 
 build:. #Le dice a docker que busque un Dockerfile en esta misma carpeta y construya la imagen
 
 ports: #Enlaza los puertos
 - "3001:3000" #Desde el 3001 de mi PC hasta el 3000 del contenedor
 
 volumes:
 -.:/app #Sincroniza mi carpeta actual con la del contenedor
 
 restart: always #Siempre que reinicie mi PC o Docker, se iniciará automáticamente
 
```

## 💡 Conceptos Clave (Resolución de Dudas)

> [!tip] La magia de los Volúmenes (`volumes: -.:/app`) 
> **¿Qué hace?** Crea un túnel directo entre la carpeta de nuestro PC (`.`) y la carpeta interna del contenedor (`/app`).
> 
> **¿Para qué sirve?** Si ahora modificas `server.js` y guardas, el archivo se actualiza mágicamente dentro del contenedor. Ya no necesitas hacer un `docker build` cada vez que programas algo nuevo.

> [!warning] La Regla de Oro de los Puertos (Izquierda vs Derecha) Cuando mapeamos puertos en Compose (`"3001:3000"`), siempre seguimos la regla: **`TU_PC : CONTENEDOR`**.
> 
> - **Derecha (Contenedor - 3000):** Es el puerto donde vive tu código. Siempre tiene que coincidir con el puerto que pusiste en el `server.js` (`server.listen(3000)`). Los puertos de los contenedores son reutilizables infinitas veces porque son cajas aisladas.
> 
> - **Izquierda (Tu PC - 3001):** Es la puerta real de tu ordenador por donde vas a entrar desde el navegador (`http://localhost:3001`). Puedes inventarte el número que quieras (8080, 4000, 9999), siempre que esté libre en tu PC.
> 

## 💻 Comandos del Día a Día

### 1. Levantar la infraestructura

Para arrancar el proyecto, construir la imagen y crear las redes y volúmenes:

```Bash
docker compose up -d
```

_(Si has cambiado cosas pesadas en el Dockerfile, añade `--build` al final para forzar la reconstrucción)._

### 2. Ver Logs en tiempo real

Para comprobar los `console.log` del contenedor mientras está en segundo plano:

```Bash
docker compose logs -f
```

_(Pulsa `Ctrl + C` para salir de la vista de logs; el contenedor no se apagará)._

### 3. Apagar y Limpiar

Cuando termines de trabajar, para detener los contenedores y destruir la red virtual:

```Bash
docker compose down
```


