
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

**Conservar el contenedor pero evitar que arranque solo (anular `restart: always`)**

Si tienes un contenedor configurado para que se encienda automáticamente con tu PC, pero quieres apagarlo y evitar que vuelva a arrancar solo la próxima vez que enciendas tu PC, usa este comando. Sobrescribe la política de reinicio a "no" en caliente y luego apaga el contenedor de forma normal.

```Bash
docker update --restart=no <nombre_o_id>
docker stop <nombre_o_id>
```

> [!tip] ¿Cómo volver a activarlo para siempre?
> Si en el futuro quieres que vuelva a arrancar automáticamente con tu PC, solo tienes que volver a cambiar su política y encenderlo:
> ```bash
> docker update --restart=always <nombre_o_id>
> docker start <nombre_o_id>
> ```

> [!question] ¿Cómo auditar qué política tiene cada contenedor meses después?
> Imagina que tienes 10 contenedores y cambiaste la política de 4 contenedores y meses después no recuerdas cuáles fueron, tienes dos formas de averiguarlo:
> 
> **1. Por Terminal:**
> Puedes usar el comando `inspect` para preguntar a Docker cómo está configurado exactamente el arranque de todos tus contenedores.
> ```bash
> # Ejemplo 1: Ver la política de un contenedor que tiene el reinicio desactivado
> docker inspect -f "{{.HostConfig.RestartPolicy.Name}}" 20-apidetareasnodejspostgresqldockercompose-mi-api-node-1
> # Salida: no
> 
> # Ejemplo 2: Ver la política de un contenedor que arranca siempre
> docker inspect -f "{{.HostConfig.RestartPolicy.Name}}" immich_server
> # Salida: always
> 
> # Ejemplo 3: Ver la política de TODOS los contenedores a la vez (Auditoría completa)
> docker inspect -f "{{.Name}} - {{.HostConfig.RestartPolicy.Name}}" $(docker ps -aq)
> # /ServidorAws - no
> # /immich_server - always
> # /immich_machine_learning - always
> # /immich_postgres - always
> # /immich_redis - always
> # /60-homelab-automation-stack-homepage-1 - unless-stopped
> # /60-homelab-automation-stack-n8n-1 - unless-stopped
> # /60-homelab-automation-stack-postgres-1 - unless-stopped
> # /60-homelab-automation-stack-portainer-1 - unless-stopped
> 
> 
> 
> 
> 
>
> ```
> 
> > **Explicación del resultado:**
> > Fíjate cómo de un vistazo sabes exactamente qué pasa en tu equipo. Los contenedores de `immich` están en **always** (siempre arrancan). El stack `60-homelab` está en **unless-stopped** (arrancan siempre *a menos* que tú los hayas apagado manualmente). Y la gran mayoría de tus APIs de pruebas (`gestorfinanciero`, `apidetareas`, `ServidorAws`) están en **no**, por lo que se quedan apagados y no consumen recursos al encender el PC.
> 
> **2. Por Interfaz Gráfica (Sin tocar la terminal):**
> 
> - **Portainer:** Si usas Portainer (la web de gestión de Docker), simplemente haces clic en el contenedor y bajas hasta la sección que dice **"Restart policies"**. Ahí verás si 
>   está en *Always* o *Never*, y puedes cambiarlo con un solo clic.
> - **Docker Desktop:** Si usas la app de Windows, puedes hacer clic en el contenedor, ir a la pestaña **"Inspect"** y buscar la línea `RestartPolicy`.


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

> [!example] Ejemplo Real: Lanzar un servidor Nginx
> ```bash
> docker run --name web -d -p 8080:80 nginx
> ```
> *¿Qué hace esto?* 
> Descarga la imagen oficial de Nginx (si no la tienes), crea un contenedor llamado `web`, lo deja corriendo en segundo plano (`-d`) y conecta el puerto `80` del contenedor al puerto `8080` de tu PC. Si vas a `http://localhost:8080` verás la web de Nginx.

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

## 🧹 6. Limpieza Masiva (Síndrome de Diógenes de Docker)

Con el tiempo, Docker acumula basura al hacer pruebas o actualizar contenedores. 

- **Imágenes `<none>` (Dangling):** Son versiones antiguas de imágenes que actualizaste. Solo ocupan espacio.

- **Volúmenes anónimos (ej. `f8a9b...`):** Creados automáticamente por algunos contenedores si no les das nombre. Quedan huérfanos al borrar el contenedor.

> [!tip] La Limpieza Segura (Recomendada)
> Este comando borra imágenes `<none>`, redes sin uso y contenedores parados. **Es muy seguro**, no borrará nada que esté encendido ni tocará los volúmenes de datos.
> ```bash
> docker system prune
> ```
> Para limpiar también los **volúmenes huérfanos** (desconectados de cualquier contenedor):
> ```bash
> docker volume prune
> ```

**¿Cómo investigar a los contenedores imágenes y volúmenes restantes?**

Si te quedan cosas raras y no sabes qué son antes de borrarlas:

- Contenedores parados: `docker inspect <id o nombre>` (mira `"Env"` o `"Image"` para saber qué programa era).

- Volúmenes: `docker volume inspect <nombre_largo>` (mira `Labels` o la ruta de montaje para buscar pistas `Mountpoint`).

---

> [!danger] Limpiezas Nucleares
> Úsalas solo si sabes lo que haces o quieres dejar Docker de fábrica.
> 
> **Eliminar TODAS las imágenes sin uso (incluidas las que tienen nombre pero no están en un contenedor activo):**
> ```bash
> docker image prune -a
> ```
> **Eliminar TODOS los contenedores apagados (saltando confirmación):**
> ```bash
> docker container prune -f
> ```
> **Eliminar TODOS los contenedores apagados Y SUS VOLÚMENES asociados:**
> Si un contenedor está apagado y ya no lo quieres, esto lo borra a él y también destruye el volumen de datos que tenía enganchado.
> ```bash
> docker rm -v $(docker ps -aq -f status=exited)
> ```
> **Forzar eliminación de TODOS los contenedores (activos y parados):**
> ```bash
> docker rm -f $(docker ps -aq)
> ```
> **💣 El botón rojo (Borra TODO lo que no esté encendido AHORA MISMO):**
> Elimina imágenes, contenedores parados, redes y volúmenes huérfanos.
> ```bash
> docker system prune -a --volumes
> ```

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

**Ver logs en tiempo real de todos los servicios a la vez**

```Bash
docker compose logs -f
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

**Ejecutar un comando DENTRO de un contenedor que YA está encendido (Exec)**

_(El comando `exec` entra a un contenedor vivo sin apagarlo para ejecutar instrucciones. Muy usado en bases de datos)._

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

**Copiar archivos entre tu PC y un contenedor (`docker cp`)**
_(Súper útil para sacar backups o meter archivos de configuración)._

```Bash
# Sintaxis general:
# docker cp [ORIGEN] [DESTINO]
```

> [!example] Ejemplo Real: Sacar un backup de base de datos a tu PC
> Imagina que has hecho un backup dentro de tu contenedor `immich_postgres` y ahora quieres sacarlo a tu Escritorio de Windows.
> **Comando:**
> ```bash
> docker cp immich_postgres:/var/lib/postgresql/data/backup.sql C:\Users\izanm\Desktop\backup.sql
> ```
> *¿De dónde sale cada cosa?*
> 1. `immich_postgres:` -> Nombre exacto de tu contenedor (seguido de dos puntos `:`).
> 2. `/var/lib/postgresql/data/backup.sql` -> La ruta absoluta de Linux DENTRO del contenedor donde está el archivo.
> 3. `C:\Users\izanm\Desktop\backup.sql` -> La ruta de tu Windows donde quieres guardarlo.

> [!example] Ejemplo Real: Meter una foto o archivo desde tu PC al contenedor
> Imagina que quieres subir una foto de prueba desde tu PC al servidor de `immich_server`.
> **Comando:**
> ```bash
> docker cp C:\Users\izanm\Desktop\prueba.jpg immich_server:/usr/src/app/upload/prueba.jpg
> ```
> *¿De dónde sale cada cosa?*
> 1. `C:\Users\izanm\Desktop\prueba.jpg` -> El archivo en tu disco duro de Windows.
> 2. `immich_server:` -> El contenedor de destino.
> 3. `/usr/src/app/upload/prueba.jpg` -> La carpeta dentro de Linux del contenedor donde lo quieres soltar.

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