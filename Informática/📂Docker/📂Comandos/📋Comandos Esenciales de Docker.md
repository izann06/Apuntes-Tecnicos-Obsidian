
------------------------------------------------------------------
### 🛠️ 0. Inicialización

**Generar archivos Docker base para un proyecto** (Dockerfile, compose.yaml,.dockerignore) de forma automática.

```Bash
docker init
```

------------------------------------------------------------------
## 🚀 1. Gestión de Contenedores

**Listar contenedores activos**

```Bash
docker ps
```

**Listar todos los contenedores (incluidos apagados)**

```Bash
docker ps -a
```

**Detener contenedor**

```Bash
docker stop <id/nombre>
```

**Iniciar contenedor apagado**

```Bash
docker start <id/nombre>
```

**Reiniciar contenedor**

```Bash
docker restart <id/nombre>
```

**Crear y encender un contenedor personalizado desde una Imagen:

```Bash
docker run -d -p <host>:<cont> --name <nombre> <imagen>
```

> [!tip] Desglose de parámetros
> 
> 
> 
> - `--name <nombre>`: Nombre del Contenedor (Que vas a crear con ese comando)
> 
> 
> 
> - `<imagen>`: Nombre de la imagen (ya creada) o puede usar una imagen publica (DockerHub)
> 
> 
> 
> - `-d`: Modo segundo plano (_detached_).
> 
> 
> 
> - `-p`: Mapeo de puertos `PC:Contenedor`.
> 

------------------------------------------------------------------
## 🔍 2. Monitorización y Logs

**Ver logs en tiempo real**

```Bash
docker logs -f <id/nombre>
```

`Pulsa Ctrl + C para salir sin detener el proceso.`

**Ver últimas 50 líneas de log**

```Bash
docker logs --tail 50 <id/nombre>
```

**Entrar a la terminal interactiva dentro de un contenedor en ejecución**

```Bash
docker exec -it <id/nombre> sh
```

Ejemplo: **Puedes hacer por ejemplo `ls`, entrar a los archivos con `cat` main.py**


**Ver estadísticas de consumo (CPU/RAM)**

```
docker stats
```

------------------------------------------------------------------
## 📦 3. Gestión de Imágenes

**Listar todas las imágenes descargadas en tu equipo**

```Bash
docker images
```

**Construir imagen desde Dockerfile**

```Bash
docker build -t <nombreImagen>.
```

**Descargar imagen de Docker Hub**

```Bash
docker pull <imagen>:<tag>
```

_Ejemplo:_ `docker pull postgres:16-alpine`

------------------------------------------------------------------

### 🗄️ 4. Gestión de Volúmenes

**Listar todos los volúmenes creados**

```Bash
docker volume ls
```

**Crear un volumen manual**

```Bash
docker volume create <nombre_volumen>
```

**Inspeccionar la ruta física de un volumen en el host**

```Bash
docker volume inspect <nombre_volumen>
```

**Listar redes internas**

```Bash
docker network ls
```
------------------------------------------------------------------
## 🗑️ 5. Eliminación Individual

> [!warning] **Regla de Dependencia** 
> No se puede borrar una imagen si un contenedor (incluso parado) depende de ella, ni se puede borrar un volumen si está asociado a un contenedor. **El orden estricto de borrado es: 1º Contenedor ➔ 2º Imagen ➔ 3º Volumen.**

**Eliminar contenedor parado**

```Bash
docker rm <id/nombre>
```

**Forzar eliminación de contenedor activo**

```Bash
docker rm -f <id/nombre>
```

**Eliminar imagen**

```Bash
docker rmi <image_id/nombre>
```

**Eliminar volumen (debe estar desacoplado de todo contenedor)**

```Bash
docker volume rm <nombre_volumen>
```

------------------------------------------------------------------

## 🧹 6. Limpieza Masiva

**Eliminar todas las imágenes sin uso**

```Bash
docker image prune -a
```

**Eliminar todas las imágenes**

```Bash
docker rmi -f $(docker images -q)
```

**Detener todos los contenedores activos a la vez**

```Bash
docker stop $(docker ps -q)
```

**Eliminar los contenedores apagados**

```Bash
docker container prune -f
```

`-f: Es para saltarte la confirmación de y/n`

**Forzar eliminación de TODOS los contenedores (activos y parados)**

```Bash
docker rm -f $(docker ps -aq)
```

**Elimina TODAS las imágenes contenedores y volúmenes que no estén en uso**

```
docker system prune -a --volumes
```

------------------------------------------------------------------

## 🐙 7. Docker Compose

**Construir y levantar servicios en segundo plano**

```Bash
docker compose up -d --build
```

**Apagar contenedores y eliminar redes internas (mantiene volúmenes y datos intactos)**

```Bash
docker compose down
```

**Apagar y BORRAR volúmenes asociados (reset completo de bases de datos)**

```Bash
docker compose down -v
```

------------------------------------------------------------------

## 💻 8. Ejecución Interactiva y Comandos Internos (`run` y `exec`)

**Crear contenedor temporal interactivo** _(La bandera `--rm` hace que el contenedor se autodestruya al cerrarlo. Útil para pruebas de usar y tirar)_

```Bash
docker run -it --rm <imagen>
```

**Abrir la terminal (shell) dentro de un contenedor temporal**

```Bash
docker run -it --rm <imagen> sh
```

**Ejecutar un comando DENTRO de un contenedor que YA está encendido (Exec)** _(El comando `exec` entra a un contenedor vivo sin apagarlo para ejecutar instrucciones. Muy usado en bases de datos)._

```Bash
docker exec -it <nombre_contenedor> <comando>
```

> [!example] Ejemplos de uso con PostgreSQL (Desde la terminal host)
> 
> - **Crear tabla:** `docker exec -it <nombre_contenedor> psql -U postgres -c "CREATE TABLE usuarios (nombre text);"`
> 
> - **Insertar dato:** `docker exec -it <nombre_contenedor> psql -U postgres -c "INSERT INTO usuarios VALUES ('midudev');"`
> 
> - **Leer datos:** `docker exec -it <nombre_contenedor> psql -U postgres -c "SELECT * FROM usuarios;"`
>

### 🤖 9. Modelos de IA Locales (Docker AI / GenAI)

> [!info] **Nota** 
> Estos comandos interactúan con las nuevas herramientas de modelos de Inteligencia Artificial locales integradas en el ecosistema (funcionan de manera muy similar a Ollama).

**Descargar un modelo de IA local (ej: Gemma de Google)**

```Bash
docker model pull gemma
```

**Listar los modelos descargados localmente**

```Bash
docker model list
```

**Ejecutar un modelo y pasarle un prompt (pregunta)**

```Bash
docker model run gemma "what is docker"
```

**Preguntar a la IA (Gordon) de Docker**

```Bash
docker ai
```