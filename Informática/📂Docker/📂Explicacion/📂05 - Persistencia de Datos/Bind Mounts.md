# 📁 Bind Mounts (Carpetas locales mapeadas)

> [!info] Navegación
> ◀ [[Volume Mounts]] · ▶ [[Dockerfile - Anatomía Completa]]
> 📂 Sección: **05 - Persistencia de Datos** · Ver también: [[Sistema de Archivos Efímero]] · [[Volume Mounts]]

---

## ¿Qué son los Bind Mounts?

Los **Bind Mounts** montan un **directorio o archivo específico de tu máquina** directamente dentro del contenedor. A diferencia de los [[Volume Mounts|volumes]], **tú controlas exactamente dónde están los datos** en tu disco.

> [!tip] Analogía: El enchufe directo
> Si un **volume** es una caja fuerte gestionada por el hotel, un **bind mount** es como si conectaras un **enchufe directo** desde tu escritorio (tu máquina) hasta la habitación del hotel (contenedor). Todo lo que pongas en ese escritorio aparece instantáneamente en la habitación, y viceversa. Tú controlas dónde está el escritorio; el hotel no tiene ni idea.

---

## Características clave

| Característica | Detalle |
|---|---|
| **Control total** | Tú decides la ruta exacta en tu máquina |
| **Reflejo bidireccional** | Los cambios en el host aparecen en el contenedor y viceversa, **en tiempo real** |
| **Ideal para desarrollo** | Editas el código en VS Code y el contenedor lo ve instantáneamente |
| **Dependiente del host** | La ruta debe existir en tu máquina |
| **Rendimiento en Desktop** | ⚠️ Más lento que volumes en Docker Desktop (Mac/Windows) por la capa de sincronización |
| **Seguridad** | ⚠️ El contenedor accede directamente a tu sistema de archivos |

---

## Sintaxis

### Sintaxis corta (`-v`)

```bash
# -v /ruta/absoluta/en/host:/ruta/en/contenedor
docker run -d \
 -v /home/usuario/mi-proyecto:/app \
 node:20-alpine npm start

# En Windows (PowerShell):
docker run -d \
 -v ${PWD}:/app \
 node:20-alpine npm start

# En Linux/Mac:
docker run -d \
 -v $(pwd):/app \
 node:20-alpine npm start
```

### Sintaxis larga (`--mount`) — Más segura

```bash
docker run -d \
 --mount type=bind,source=/home/usuario/mi-proyecto,target=/app \
 node:20-alpine npm start

# En PowerShell:
docker run -d \
 --mount "type=bind,source=$(pwd),target=/app" \
 node:20-alpine npm start
```

> [!warning] Diferencia crucial entre `-v` y `--mount` con bind mounts
> Si la ruta del host **no existe**:
>
> - `-v` la **crea automáticamente** como un directorio vacío (lo que puede causar errores silenciosos difíciles de depurar).
>
> - `--mount` **falla con un error explícito** (más seguro, te avisa del problema).
> 
> Por esta razón, Docker recomienda usar `--mount` para bind mounts.

---

## ¿Cómo diferenciar un bind mount de un volume en la sintaxis `-v`?

```bash
# BIND MOUNT → empieza con / (ruta absoluta) o./ (ruta relativa)
docker run -v /home/user/code:/app... # Bind mount (ruta absoluta)
docker run -v $(pwd):/app... # Bind mount (pwd = ruta absoluta)
docker run -v./src:/app/src... # Bind mount (ruta relativa, Docker 23+)

# VOLUME → es solo un nombre (sin barras)
docker run -v mi-volumen:/app/data... # Volume (nombre sin /)
```

---

## Ejemplo práctico: Desarrollo con Bind Mount

> [!example] Entorno de desarrollo Node.js
> ```bash
> # Supongamos que tienes un proyecto en ~/mi-api/
> # Estructura:
> # ~/mi-api/
> # ├── package.json
> # ├── package-lock.json
> # ├── src/
> # │ └── index.js
> # └──.env
> 
> # Ejecutar el contenedor con tu código montado
> docker run -it \
> --name dev-api \
> -p 3000:3000 \
> -v $(pwd):/app \
> -w /app \
> node:20-alpine \
> sh -c "npm install && npm run dev"
> 
> # Ahora, si editas ~/mi-api/src/index.js en VS Code,
> # el cambio se refleja INSTANTÁNEAMENTE dentro del contenedor.
> # Si tu app usa hot-reloading (nodemon, vite, etc.),
> # se recargará automáticamente.
> ```
> 
> Ver más sobre este flujo de desarrollo en [[Hot Reloading y DX]].

---

## Bind Mounts de solo lectura

Puedes montar archivos o directorios como **solo lectura** para que el contenedor no pueda modificarlos:

```bash
# Montar configuración como solo lectura
docker run -d \
 --name web-server \
 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
 -v $(pwd)/html:/usr/share/nginx/html:ro \
 -p 80:80 \
 nginx

# Con --mount:
docker run -d \
 --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf,readonly \
 -p 80:80 \
 nginx

# El contenedor puede LEER los archivos pero NO modificarlos.
# Intentar escribir dará: "Read-only file system"
```

> [!tip] Cuándo usar solo lectura
>
> - **Archivos de configuración**: nginx.conf, my.cnf, etc.
>
> - **Certificados SSL**: Los certificados no deben ser modificables.
>
> - **Scripts de inicialización**: Scripts que se ejecutan al arrancar el contenedor.
>
> - **Código fuente en producción**: Si no necesitas que el contenedor modifique tu código.

---

## Montar archivos individuales

No solo puedes montar directorios completos, también puedes montar **archivos individuales**:

```bash
# Montar un solo archivo de configuración
docker run -d \
 -v $(pwd)/mi-config.json:/app/config/settings.json:ro \
 mi-app

# Montar el socket de Docker (para Docker-in-Docker o herramientas de gestión)
docker run -d \
 -v /var/run/docker.sock:/var/run/docker.sock \
 portainer/portainer-ce

# Montar el archivo /etc/hosts
docker run -d \
 -v /etc/hosts:/etc/hosts:ro \
 mi-app
```

> [!warning] Montar archivos individuales: Cuidado
> Si montas un archivo individual y la aplicación lo **reemplaza** (en lugar de modificarlo in-place), el bind mount puede romperse. Esto ocurre porque algunos editores crean un archivo nuevo y borran el antiguo en lugar de modificar el mismo inodo. En estos casos, monta el **directorio padre** en su lugar.

---

## Problemas comunes con Bind Mounts

### 1. Permisos de archivos (Linux)

```bash
# Problema: El contenedor corre como root, los archivos creados son de root
docker run -v $(pwd):/app node:20-alpine touch /app/nuevo-archivo.txt
ls -la nuevo-archivo.txt
# -rw-r--r-- 1 root root 0 Jan 15 10:00 nuevo-archivo.txt
# ¡El archivo es de root en tu máquina!

# Solución 1: Ejecutar el contenedor con tu usuario
docker run -u $(id -u):$(id -g) -v $(pwd):/app node:20-alpine touch /app/archivo.txt

# Solución 2: En el Dockerfile, crear un usuario con el mismo UID
```

### 2. Rendimiento en Docker Desktop (Mac/Windows)

```bash
# En Mac/Windows, los bind mounts pasan por una capa de sincronización
# entre el SO host y la VM de Linux donde corre Docker.
# Esto puede ser LENTO para proyectos grandes (node_modules, vendor, etc.)

# Solución: Excluir directorios pesados usando volúmenes anónimos
docker run -d \
 -v $(pwd):/app \
 -v /app/node_modules \
 node:20-alpine npm start

# El truco: -v /app/node_modules (sin ruta host) crea un volumen anónimo
# que "oculta" el node_modules del bind mount, evitando la sincronización
# de miles de archivos.
```

### 3. El bind mount oculta el contenido original

```bash
# Si la imagen tiene archivos en /app/data y montas un bind mount ahí,
# los archivos originales DESAPARECEN y solo se ve el contenido del host.

# Ejemplo: La imagen nginx tiene archivos en /usr/share/nginx/html
docker run -d -v $(pwd)/mi-html:/usr/share/nginx/html nginx
# Solo se verán los archivos de./mi-html, no los que traía la imagen
```

> [!info] Diferencia con Volumes
> Los [[Volume Mounts]] tienen un comportamiento diferente: si el volumen está **vacío**, Docker **copia** los datos de la imagen al volumen (pre-población). Los bind mounts **nunca** hacen esto.

---

## Tabla comparativa definitiva: Volume Mounts vs Bind Mounts

| Característica | 📦 Volume Mounts | 📁 Bind Mounts |
|---|---|---|
| **¿Quién gestiona la ubicación?** | **Docker** (`/var/lib/docker/volumes/`) | **Tú** (cualquier ruta de tu sistema) |
| **Portabilidad** | ✅ Alta (funciona igual en Linux, Mac, Windows) | ⚠️ Baja (depende de rutas del host) |
| **Rendimiento en Docker Desktop** | ✅ **Mejor** (almacenamiento nativo en la VM) | ⚠️ **Peor** (sincronización host ↔ VM) |
| **Acceso desde el host** | ⚠️ Difícil (la ruta real está oculta) | ✅ Fácil (es un directorio normal) |
| **Ideal para...** | Bases de datos, datos de producción, datos compartidos | **Desarrollo** (código fuente), archivos de configuración |
| **Persistencia** | ✅ Persiste tras `docker rm` | ✅ Persiste (son archivos de tu disco) |
| **Backup** | Con comandos Docker | Backup normal del directorio |
| **Drivers remotos** | ✅ Soporta NFS, AWS EBS, etc. | ❌ Solo local |
| **Sintaxis `-v`** | `-v nombre:/ruta` | `-v /ruta/host:/ruta` |
| **Pre-población** | ✅ Si vacío, copia datos de la imagen | ❌ Siempre **oculta** el contenido original |
| **Seguridad** | ✅ Aislado del host | ⚠️ Acceso directo al filesystem del host |
| **Gestión** | `docker volume ls/create/rm` | Herramientas del SO (`ls`, `rm`, `cp`) |

---

## Reglas de oro para elegir

> [!tip] ¿Volume o Bind Mount?
> 
> | Situación | Recomendación |
> |---|---|
> | **Datos de base de datos** | 📦 **Volume** |
> | **Código fuente en desarrollo** | 📁 **Bind Mount** |
> | **Archivos subidos por usuarios** | 📦 **Volume** |
> | **Archivos de configuración** | 📁 **Bind Mount** (`:ro`) |
> | **Compartir datos entre contenedores** | 📦 **Volume** |
> | **Datos sensibles temporales** | 🔒 **tmpfs** |
> | **Logs que necesitas analizar desde el host** | 📁 **Bind Mount** o log driver |
> | **Producción en general** | 📦 **Volume** |
> | **Desarrollo local** | 📁 **Bind Mount** + 📦 **Volume** (para `node_modules`, etc.) |

---

> [!info] Navegación
> ◀ [[Volume Mounts]] · ▶ [[Dockerfile - Anatomía Completa]]
