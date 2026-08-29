# 📦 Contenedores en Docker

> [!info] Navegación
> ◀ [[Imágenes en Docker]] · ▶ [[Redes en Docker]]
> 📂 Sección: **04 - CLI Básica** · Ver también: [[Imágenes en Docker]] · [[Redes en Docker]]

---

## ¿Qué es un contenedor?

Un contenedor es una **instancia en ejecución** de una [[Imágenes en Docker|imagen]]. Si la imagen es la receta, el contenedor es el plato servido. Puedes crear múltiples contenedores a partir de la misma imagen, y cada uno tendrá su propio **estado**, su propia **capa de escritura** y su propio **aislamiento** (gracias a los [[Namespaces]] y [[Cgroups]]).

```
 docker run
IMAGEN ──────────────────────────────► CONTENEDOR
(inmutable) (en ejecución, con estado)
 docker run
 ──────────────────────────────► CONTENEDOR 2
 docker run (misma imagen, instancia diferente)
 ──────────────────────────────► CONTENEDOR 3
```

---

## `docker run` — El comando más importante de Docker

`docker run` es el comando que **crea y ejecuta** un contenedor a partir de una imagen. Es el comando que más usarás en tu vida con Docker.

```bash
# Sintaxis completa
docker run [OPCIONES] <imagen> [COMANDO] [ARGUMENTOS]
```

### Flags más importantes

| Flag | Forma larga | Descripción | Ejemplo |
|---|---|---|---|
| `-d` | `--detach` | Ejecutar en **segundo plano** (daemon mode) | `docker run -d nginx` |
| `-it` | `--interactive --tty` | Modo **interactivo** con terminal (para shells) | `docker run -it ubuntu bash` |
| `-p` | `--publish` | **Mapear puertos** host:contenedor | `docker run -p 8080:80 nginx` |
| `--name` | `--name` | Asignar un **nombre** al contenedor | `docker run --name mi-web nginx` |
| `-e` | `--env` | Establecer **variable de entorno** | `docker run -e DB_HOST=localhost nginx` |
| `--env-file` | `--env-file` | Cargar variables desde un **archivo** | `docker run --env-file.env nginx` |
| `-v` | `--volume` | Montar un **volumen** o bind mount | `docker run -v datos:/app/data nginx` |
| `--rm` | `--rm` | **Eliminar** el contenedor al detenerse | `docker run --rm nginx` |
| `--network` | `--network` | Conectar a una **red** específica | `docker run --network mi-red nginx` |
| `--restart` | `--restart` | **Política de reinicio** | `docker run --restart=unless-stopped nginx` |
| `-w` | `--workdir` | Establecer el **directorio de trabajo** | `docker run -w /app node` |
| `--memory` | `--memory` | **Limitar RAM** | `docker run --memory="256m" nginx` |
| `--cpus` | `--cpus` | **Limitar CPUs** | `docker run --cpus="0.5" nginx` |
| `--init` | `--init` | Usar **tini** como PID 1 (evita zombies) | `docker run --init mi-app` |
| `--hostname` | `--hostname` | Asignar **hostname** personalizado | `docker run --hostname web-1 nginx` |

---

### Ejemplos prácticos de `docker run`

#### 1. Servidor web nginx en segundo plano

```bash
docker run -d --name mi-nginx -p 8080:80 nginx
# Ahora abre http://localhost:8080 en tu navegador
```

#### 2. Contenedor interactivo de Ubuntu

```bash
docker run -it --rm ubuntu:22.04 bash
# Estás "dentro" del contenedor. Puedes instalar cosas, explorar.
# Al escribir 'exit', el contenedor se elimina automáticamente (--rm)
```

#### 3. Base de datos PostgreSQL con datos persistentes

```bash
docker run -d \
 --name mi-postgres \
 -p 5432:5432 \
 -e POSTGRES_USER=admin \
 -e POSTGRES_PASSWORD=secreto123 \
 -e POSTGRES_DB=mi_aplicacion \
 -v pgdata:/var/lib/postgresql/data \
 postgres:16-alpine
```

#### 4. Contenedor Node.js con bind mount para desarrollo

```bash
docker run -it \
 --name mi-node \
 -p 3000:3000 \
 -v $(pwd):/app \
 -w /app \
 node:20-alpine \
 npm start
```

#### 5. Contenedor con límites de recursos y política de reinicio

```bash
docker run -d \
 --name produccion \
 --restart=unless-stopped \
 --memory="512m" \
 --cpus="1.5" \
 -p 80:80 \
 mi-api:v2.0.0
```

---

### El flag `-p` (publish) explicado en detalle

> [!warning] Entender el mapeo de puertos
> El formato es `-p <PUERTO_HOST>:<PUERTO_CONTENEDOR>`:
> ```
> -p 8080:80
> │ │
> │ └── Puerto DENTRO del contenedor (donde la app escucha)
> └──────── Puerto en TU MÁQUINA (por donde accedes desde el navegador)
> ```
> 
> Si escribes `-p 8080:80`, significa:
>
> - La app dentro del contenedor escucha en el puerto **80**.
>
> - Tú accedes desde tu navegador en `http://localhost:8080`.
>
> - Docker **redirige** el tráfico del puerto 8080 de tu máquina al puerto 80 del contenedor.

```bash
# Mapear múltiples puertos
docker run -d -p 80:80 -p 443:443 nginx

# Mapear a una IP específica del host (no todas)
docker run -d -p 127.0.0.1:8080:80 nginx
# Solo accesible desde localhost, no desde otras máquinas

# Puerto aleatorio del host → puerto 80 del contenedor
docker run -d -p 80 nginx
# Docker elige un puerto aleatorio. Usa 'docker port' para verlo.
```

### Políticas de reinicio (`--restart`)

| Valor | Comportamiento |
|---|---|
| `no` (default) | No reiniciar nunca automáticamente |
| `on-failure` | Reiniciar solo si el contenedor sale con error (exit code ≠ 0) |
| `on-failure:5` | Reiniciar máximo 5 veces en caso de error |
| `always` | Reiniciar **siempre**, incluso al reiniciar el daemon Docker |
| `unless-stopped` | Reiniciar siempre, **excepto** si fue detenido manualmente con `docker stop` |

> [!tip] Recomendación para producción
> Usa `--restart=unless-stopped` para servicios en producción. Así se reiniciarán automáticamente si fallan o si el servidor se reinicia, pero no molestarán si los detuviste intencionalmente.

---

## `docker ps` — Ver contenedores

```bash
# Ver contenedores ACTIVOS (en ejecución)
docker ps

# Resultado:
# CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
# a1b2c3d4e5f6 nginx "/docker-entrypoint.…" 10 minutes ago Up 10 minutes 0.0.0.0:8080->80/tcp mi-nginx

# Ver TODOS los contenedores (incluidos los detenidos)
docker ps -a

# Ver solo los IDs
docker ps -q

# Ver todos los IDs (incluidos detenidos)
docker ps -aq

# Filtrar contenedores
docker ps --filter "name=mi-nginx" # Por nombre
docker ps --filter "status=exited" # Por estado
docker ps -a --filter "ancestor=nginx" # Por imagen base
docker ps --filter "label=environment=prod" # Por etiqueta

# Formato personalizado (útil para scripts)
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
# NAMES STATUS PORTS
# mi-nginx Up 10 minutes 0.0.0.0:8080->80/tcp
# mi-postgres Up 5 minutes 0.0.0.0:5432->5432/tcp

# Ver tamaño de disco de cada contenedor
docker ps -s
```

---

## `docker stop` y `docker start` — Ciclo de vida

```bash
# Detener un contenedor (envía SIGTERM, espera 10s, luego SIGKILL)
docker stop mi-nginx

# Detener con timeout personalizado (espera 30 segundos)
docker stop -t 30 mi-nginx

# Detener TODOS los contenedores en ejecución
docker stop $(docker ps -q)

# Arrancar un contenedor detenido (no crea uno nuevo)
docker start mi-nginx

# Reiniciar un contenedor
docker restart mi-nginx

# Matar un contenedor inmediatamente (SIGKILL, sin gracia)
docker kill mi-nginx
```

> [!info] SIGTERM vs SIGKILL
>
> - `docker stop` envía primero **SIGTERM** (señal educada: "por favor, termina"). La aplicación puede capturar esta señal y hacer un **graceful shutdown** (cerrar conexiones, guardar datos, etc.). Si no termina en el timeout (default 10s), Docker envía **SIGKILL** (muerte instantánea).
>
> - `docker kill` envía **SIGKILL** directamente, sin dar oportunidad de limpieza.
> 
> **Siempre usa `docker stop`** excepto cuando el contenedor está totalmente colgado.

---

## `docker rm` — Eliminar contenedores

```bash
# Eliminar un contenedor detenido
docker rm mi-nginx

# Forzar la eliminación de un contenedor en ejecución
docker rm -f mi-nginx
# Equivalente a: docker kill + docker rm

# Eliminar un contenedor y sus volúmenes anónimos asociados
docker rm -v mi-nginx

# Eliminar TODOS los contenedores detenidos
docker container prune

# Alternativa manual
docker rm $(docker ps -aq --filter "status=exited")
```

---

## `docker exec` — Ejecutar comandos dentro de un contenedor

Este comando es **fundamental** para depuración y administración. Te permite "entrar" en un contenedor que ya está corriendo.

```bash
# Sintaxis
docker exec [OPCIONES] <contenedor> <comando>

# Abrir una shell interactiva dentro del contenedor
docker exec -it mi-nginx bash
# Si la imagen no tiene bash (ej. Alpine), usa sh:
docker exec -it mi-nginx sh

# Ejecutar un comando específico sin entrar al contenedor
docker exec mi-nginx cat /etc/nginx/nginx.conf

# Ver los procesos dentro del contenedor
docker exec mi-nginx ps aux

# Ejecutar como un usuario específico
docker exec -u www-data mi-nginx whoami
# www-data

# Establecer variables de entorno para el comando
docker exec -e MI_VAR="valor" mi-nginx env | grep MI_VAR

# Ejecutar un comando en segundo plano (detached)
docker exec -d mi-nginx touch /tmp/archivo-creado
```

> [!example] Caso de uso real: Depurar una base de datos
> ```bash
> # Tienes un contenedor PostgreSQL corriendo
> docker run -d --name mi-db -e POSTGRES_PASSWORD=secreto postgres:16-alpine
> 
> # Conectarte a la consola de PostgreSQL
> docker exec -it mi-db psql -U postgres
> 
> # Ahora estás en psql:
> postgres=# \l -- Listar bases de datos
> postgres=# \dt -- Listar tablas
> postgres=# SELECT * FROM usuarios LIMIT 10;
> postgres=# \q -- Salir
> ```

---

## `docker logs` — Ver los registros del contenedor

```bash
# Ver todos los logs del contenedor
docker logs mi-nginx

# Seguir los logs en tiempo real (como tail -f)
docker logs -f mi-nginx

# Ver los últimos 50 registros
docker logs --tail 50 mi-nginx

# Ver logs con timestamps
docker logs -t mi-nginx
# 2024-01-15T10:23:45.123456789Z 172.17.0.1 - - "GET / HTTP/1.1" 200

# Ver logs desde una fecha/hora específica
docker logs --since "2024-01-15T10:00:00" mi-nginx
docker logs --since "30m" mi-nginx # Últimos 30 minutos

# Hasta una fecha/hora específica
docker logs --until "2024-01-15T11:00:00" mi-nginx

# Combinar: últimos 100 logs en tiempo real con timestamps
docker logs -f -t --tail 100 mi-nginx
```

> [!tip] Buena práctica: Logs a stdout
> Los contenedores Docker capturan todo lo que la aplicación escribe en **stdout** (salida estándar) y **stderr** (salida de errores). Por eso es una buena práctica que tus aplicaciones escriban sus logs a stdout/stderr en lugar de a archivos. Esto permite que Docker (y herramientas como ELK, Loki o Fluentd) gestionen los logs de forma centralizada.

---

## Otros comandos útiles

```bash
# Ver estadísticas de recursos en TIEMPO REAL
docker stats
# CONTAINER ID NAME CPU % MEM USAGE / LIMIT MEM % NET I/O
# a1b2c3d4 mi-nginx 0.01% 5.2MiB / 7.77GiB 0.07% 1.45kB / 0B
# b2c3d4e5 mi-postgres 0.15% 42.1MiB / 7.77GiB 0.53% 2.3kB / 1.1kB

# Estadísticas de un solo contenedor (sin streaming)
docker stats --no-stream mi-nginx

# Ver cambios en el sistema de archivos del contenedor
docker diff mi-nginx
# C /var ← Changed (modificado)
# A /var/log/nginx/access.log ← Added (añadido)
# D /tmp/file ← Deleted (eliminado)

# Copiar archivos entre host y contenedor
docker cp mi-nginx:/etc/nginx/nginx.conf./nginx.conf # Contenedor → Host
docker cp./mi-config.conf mi-nginx:/etc/nginx/conf.d/ # Host → Contenedor

# Ver los puertos mapeados
docker port mi-nginx
# 80/tcp -> 0.0.0.0:8080

# Pausar y reanudar un contenedor (congela los procesos)
docker pause mi-nginx
docker unpause mi-nginx

# Renombrar un contenedor
docker rename mi-nginx web-server

# Ver procesos dentro del contenedor (sin exec)
docker top mi-nginx

# Esperar a que un contenedor termine y obtener su exit code
docker wait mi-trabajo-batch
# 0 ← Exit code (0 = éxito)

# Inspeccionar un contenedor (JSON con toda la información)
docker inspect mi-nginx

# Ver solo la IP del contenedor
docker inspect mi-nginx --format='{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
# 172.17.0.2

# Ver el estado actual
docker inspect mi-nginx --format='{{.State.Status}}'
# running
```

---

## Ciclo de vida completo de un contenedor

```
 docker create docker start docker stop docker rm
 (crear sin (arrancar) (detener) (eliminar)
 ejecutar)
 │ │ │ │
 ▼ ▼ ▼ ▼
 ┌────────┐ ┌─────────┐ ┌─────────┐ ┌────────┐
 │CREATED │ ──────► │ RUNNING │ ──────► │ STOPPED │ ────► │REMOVED │
 └────────┘ └─────────┘ └─────────┘ └────────┘
 │ ▲
 │ docker restart │
 └────────────────────┘

 docker run = docker create + docker start (todo en uno)
```

---

## Limpieza total de contenedores

```bash
# Eliminar todos los contenedores detenidos
docker container prune

# Eliminar TODOS los contenedores (incluidos los activos)
docker rm -f $(docker ps -aq)

# Limpieza total del sistema Docker
docker system prune -a --volumes
# ⚠️ Elimina: contenedores, imágenes, redes, volúmenes y caché
```

---

## Tabla resumen de comandos de contenedores

| Comando | Descripción | Ejemplo |
|---|---|---|
| `docker run` | Crear y ejecutar contenedor | `docker run -d -p 80:80 nginx` |
| `docker ps` | Listar contenedores | `docker ps -a` |
| `docker stop` | Detener contenedor (graceful) | `docker stop mi-nginx` |
| `docker start` | Arrancar contenedor detenido | `docker start mi-nginx` |
| `docker restart` | Reiniciar contenedor | `docker restart mi-nginx` |
| `docker rm` | Eliminar contenedor | `docker rm -f mi-nginx` |
| `docker exec` | Ejecutar comando dentro | `docker exec -it mi-nginx bash` |
| `docker logs` | Ver registros | `docker logs -f --tail 100 mi-nginx` |
| `docker stats` | Monitorear recursos | `docker stats` |
| `docker inspect` | Información detallada | `docker inspect mi-nginx` |
| `docker cp` | Copiar archivos | `docker cp cont:/path./local` |
| `docker diff` | Ver cambios en filesystem | `docker diff mi-nginx` |
| `docker top` | Ver procesos | `docker top mi-nginx` |

---

> [!info] Navegación
> ◀ [[Imágenes en Docker]] · ▶ [[Redes en Docker]]
