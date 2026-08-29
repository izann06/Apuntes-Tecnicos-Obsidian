# 💾 Volume Mounts (Volúmenes gestionados por Docker)

> [!info] Navegación
> ◀ [[Sistema de Archivos Efímero]] · ▶ [[Bind Mounts]]
> 📂 Sección: **05 - Persistencia de Datos** · Ver también: [[Sistema de Archivos Efímero]] · [[Bind Mounts]]

---

## ¿Qué son los Volumes?

Los **volumes** (volúmenes) son el mecanismo **recomendado por Docker** para persistir datos. Docker crea y gestiona un directorio especial en el sistema de archivos del host (`/var/lib/docker/volumes/` en Linux) donde almacena los datos del volumen.

La clave de los volumes es que **Docker gestiona todo**. Tú solo le dices el nombre del volumen y la ruta dentro del contenedor donde quieres montarlo. Docker se encarga de crear el directorio, almacenarlo de forma segura y gestionarlo.

> [!tip] Analogía: La caja fuerte del hotel
> Si los contenedores son habitaciones de hotel, un **volume** es la **caja fuerte** del hotel. Guardas tus objetos de valor en la caja fuerte. Si cambias de habitación (recreas el contenedor), tus objetos siguen ahí. Si el hotel renueva la habitación (actualizas la imagen), tus objetos de valor están a salvo.
> 
> La clave: **tú no decides dónde está físicamente la caja fuerte** (Docker elige la ubicación en disco). Tú solo la usas con una llave (el nombre del volumen).

---

## Características clave

| Característica | Detalle |
|---|---|
| **Gestionados por Docker** | No necesitas saber dónde están en disco |
| **Persistencia** | Los datos sobreviven a `docker rm` |
| **Compartibles** | Múltiples contenedores pueden montar el mismo volumen |
| **Portabilidad** | Funcionan igual en Linux, Mac y Windows |
| **Drivers** | Soportan almacenamiento remoto (NFS, AWS EBS, etc.) |
| **Rendimiento** | Mejor que bind mounts en Docker Desktop (Mac/Windows) |
| **Backup** | Se pueden respaldar con comandos Docker |
| **Pre-población** | Si el volumen está vacío, Docker copia los datos de la imagen |

---

## Comandos para gestionar volúmenes

### Crear un volumen

```bash
docker volume create mis-datos
```

### Listar todos los volúmenes

```bash
docker volume ls

# DRIVER VOLUME NAME
# local mis-datos
# local pgdata
# local redis-cache
```

### Inspeccionar un volumen

```bash
docker volume inspect mis-datos

# [
# {
# "CreatedAt": "2024-01-15T10:30:00Z",
# "Driver": "local",
# "Labels": {},
# "Mountpoint": "/var/lib/docker/volumes/mis-datos/_data", ← Ubicación real
# "Name": "mis-datos",
# "Options": {},
# "Scope": "local"
# }
# ]
```

### Eliminar un volumen

```bash
# Eliminar un volumen específico (solo si no está en uso)
docker volume rm mis-datos

# Eliminar TODOS los volúmenes sin usar
docker volume prune

# Forzar sin confirmación
docker volume prune -f
```

---

## Montar volúmenes al crear contenedores

Hay dos sintaxis para montar volúmenes:

### Sintaxis corta (`-v`) — La más usada

```bash
# -v nombre_volumen:ruta_en_contenedor
docker run -d \
 --name mi-postgres \
 -v pgdata:/var/lib/postgresql/data \
 -e POSTGRES_PASSWORD=secreto \
 postgres:16-alpine
```

### Sintaxis larga (`--mount`) — Recomendada por Docker

```bash
docker run -d \
 --name mi-postgres \
 --mount type=volume,source=pgdata,target=/var/lib/postgresql/data \
 -e POSTGRES_PASSWORD=secreto \
 postgres:16-alpine
```

| Parámetro de `--mount` | Descripción |
|---|---|
| `type=volume` | Tipo de montaje (volume, bind, o tmpfs) |
| `source=pgdata` | Nombre del volumen (se crea automáticamente si no existe) |
| `target=/var/lib/...` | Ruta dentro del contenedor donde se monta |
| `readonly` | (Opcional) Monta en modo solo lectura |

> [!info] ¿Cuándo se crea el volumen?
> Si usas un nombre de volumen que **no existe**, Docker lo **crea automáticamente**. No necesitas ejecutar `docker volume create` previamente (aunque puedes hacerlo si quieres).

---

## Ejemplo completo: Base de datos PostgreSQL con persistencia

> [!example] PostgreSQL con datos que sobreviven al contenedor
> ```bash
> # 1. Crear el volumen (opcional, docker run lo crea automáticamente)
> docker volume create pgdata
> 
> # 2. Ejecutar PostgreSQL con el volumen montado
> docker run -d \
> --name postgres-produccion \
> -p 5432:5432 \
> -e POSTGRES_USER=admin \
> -e POSTGRES_PASSWORD=super_secreto \
> -e POSTGRES_DB=mi_app_produccion \
> -v pgdata:/var/lib/postgresql/data \
> --restart=unless-stopped \
> postgres:16-alpine
> 
> # 3. Crear datos (conectarse y crear una tabla)
> docker exec -it postgres-produccion psql -U admin -d mi_app_produccion
> # CREATE TABLE usuarios (id SERIAL, nombre TEXT, email TEXT);
> # INSERT INTO usuarios (nombre, email) VALUES ('Ana', 'ana@email.com');
> # INSERT INTO usuarios (nombre, email) VALUES ('Carlos', 'carlos@email.com');
> # SELECT * FROM usuarios;
> # id | nombre | email
> # ----+--------+-----------------
> # 1 | Ana | ana@email.com
> # 2 | Carlos | carlos@email.com
> # \q
> 
> # 4. DESTRUIR el contenedor completamente
> docker rm -f postgres-produccion
> 
> # 5. Verificar que el volumen SIGUE existiendo
> docker volume ls
> # DRIVER VOLUME NAME
> # local pgdata ← ¡Sigue ahí!
> 
> # 6. Crear un NUEVO contenedor con el MISMO volumen
> docker run -d \
> --name postgres-nuevo \
> -p 5432:5432 \
> -e POSTGRES_USER=admin \
> -e POSTGRES_PASSWORD=super_secreto \
> -e POSTGRES_DB=mi_app_produccion \
> -v pgdata:/var/lib/postgresql/data \
> postgres:16-alpine
> 
> # 7. ¡Los datos siguen ahí!
> docker exec -it postgres-nuevo psql -U admin -d mi_app_produccion \
> -c "SELECT * FROM usuarios;"
> # id | nombre | email
> # ----+--------+-----------------
> # 1 | Ana | ana@email.com
> # 2 | Carlos | carlos@email.com
> # ✅ ¡DATOS PRESERVADOS!
> 
> # 8. Limpieza
> docker rm -f postgres-nuevo
> ```

---

## Compartir volúmenes entre contenedores

Un volumen puede ser montado por **múltiples contenedores** simultáneamente. Esto es útil para compartir datos:

```bash
# Crear un volumen compartido
docker volume create datos-compartidos

# Contenedor que ESCRIBE datos
docker run -d \
 --name escritor \
 -v datos-compartidos:/datos \
 ubuntu bash -c "while true; do date >> /datos/log.txt; sleep 5; done"

# Contenedor que LEE datos (modo solo lectura)
docker run -it --rm \
 -v datos-compartidos:/datos:ro \
 ubuntu tail -f /datos/log.txt
# Verás las fechas apareciendo cada 5 segundos

# Limpieza
docker rm -f escritor
```

> [!warning] Cuidado con la concurrencia
> Si dos contenedores escriben al mismo archivo dentro del volumen simultáneamente, pueden ocurrir **corrupciones de datos**. Esto es especialmente peligroso con bases de datos. **Nunca** montes el directorio de datos de una BD en dos contenedores de BD al mismo tiempo. Para compartir datos de forma segura, usa mecanismos de coordinación (colas de mensajes, APIs, etc.).

---

## Volúmenes de solo lectura

```bash
# Montar un volumen como solo lectura
docker run -d \
 --name lector \
 -v config-data:/app/config:ro \
 mi-app

# Con --mount
docker run -d \
 --mount type=volume,source=config-data,target=/app/config,readonly \
 mi-app

# El contenedor puede LEER los datos pero NO modificarlos
# Intentar escribir dará error: "Read-only file system"
```

---

## Volúmenes anónimos

Si montas una ruta del contenedor **sin dar un nombre**, Docker crea un **volumen anónimo** con un hash como nombre:

```bash
# Volumen anónimo (Docker genera un nombre aleatorio)
docker run -d -v /var/lib/datos mi-app

docker volume ls
# DRIVER VOLUME NAME
# local a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2

# Difícil de gestionar → Usa SIEMPRE volúmenes con nombre
```

> [!tip] Evita volúmenes anónimos
> Los volúmenes anónimos son difíciles de identificar y gestionar. Siempre usa **volúmenes con nombre** (`-v mi-nombre:/ruta`) para poder rastrearlos, respaldarlos y limpiarlos fácilmente.

---

## Respaldar y restaurar volúmenes

### Respaldar un volumen a un archivo tar

```bash
# Estrategia: Crear un contenedor temporal que monte el volumen
# y lo comprima en un archivo tar

docker run --rm \
 -v pgdata:/source:ro \
 -v $(pwd):/backup \
 ubuntu tar czf /backup/pgdata-backup-$(date +%Y%m%d).tar.gz -C /source.

# Resultado: pgdata-backup-20240115.tar.gz en tu directorio actual
```

### Restaurar un volumen desde un archivo tar

```bash
# Crear un nuevo volumen
docker volume create pgdata-restored

# Restaurar los datos
docker run --rm \
 -v pgdata-restored:/target \
 -v $(pwd):/backup:ro \
 ubuntu tar xzf /backup/pgdata-backup-20240115.tar.gz -C /target

# Ahora puedes usar 'pgdata-restored' en un nuevo contenedor
```

### Copiar datos entre volúmenes

```bash
# Copiar todo el contenido de un volumen a otro
docker run --rm \
 -v volumen-origen:/from:ro \
 -v volumen-destino:/to \
 ubuntu cp -a /from/. /to/
```

---

## Drivers de volumen (almacenamiento remoto)

Por defecto, los volúmenes usan el driver `local` (almacenamiento en disco local). Pero Docker soporta **plugins de volumen** para almacenar datos en servicios remotos:

| Plugin / Driver | Almacenamiento | Caso de uso |
|---|---|---|
| `local` (default) | Disco local del host | Desarrollo, producción simple |
| `nfs` | Network File System (NFS) | Compartir volúmenes entre múltiples hosts |
| `aws/ebs` (REX-Ray) | Amazon EBS | Producción en AWS |
| `azure/file` | Azure File Storage | Producción en Azure |
| `gce/pd` | Google Persistent Disk | Producción en GCP |
| `convoy` | Diversos backends | Snapshots y backups avanzados |

```bash
# Ejemplo: Crear un volumen NFS
docker volume create \
 --driver local \
 --opt type=nfs \
 --opt o=addr=192.168.1.100,rw \
 --opt device=:/path/to/share \
 nfs-volume
```

---

## Tabla resumen de comandos de volúmenes

| Comando | Descripción | Ejemplo |
|---|---|---|
| `docker volume create` | Crear volumen | `docker volume create pgdata` |
| `docker volume ls` | Listar volúmenes | `docker volume ls` |
| `docker volume inspect` | Información detallada | `docker volume inspect pgdata` |
| `docker volume rm` | Eliminar volumen | `docker volume rm pgdata` |
| `docker volume prune` | Limpiar sin usar | `docker volume prune` |
| `-v nombre:/ruta` | Montar al crear contenedor | `docker run -v pgdata:/data...` |
| `-v nombre:/ruta:ro` | Montar solo lectura | `docker run -v config:/app:ro...` |

---

> [!info] Navegación
> ◀ [[Sistema de Archivos Efímero]] · ▶ [[Bind Mounts]]
