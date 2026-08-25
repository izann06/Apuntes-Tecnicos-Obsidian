# 🖼️ Imágenes en Docker

> [!info] Navegación
> ◀ [[Instalación y Setup]] · ▶ [[Contenedores en Docker]]
> 📂 Sección: **04 - CLI Básica** · Ver también: [[Contenedores en Docker]] · [[Redes en Docker]]

---

## La relación entre Imagen y Contenedor

Antes de entrar en los comandos, es crucial entender la diferencia entre estos dos conceptos:

- Una **Imagen** es como la **receta de un plato**: contiene todas las instrucciones y los ingredientes necesarios. Es **inmutable** (no cambia). Puedes compartirla, distribuirla y almacenarla.
- Un **Contenedor** es el **plato preparado**: es una instancia en ejecución de una imagen. Puedes crear múltiples platos (contenedores) a partir de la misma receta (imagen), y cada uno puede tener su propio estado.

```
IMAGEN (Receta)                CONTENEDOR (Plato preparado)
┌─────────────────┐           ┌─────────────────┐
│ - Inmutable      │    ──►   │ - En ejecución   │
│ - Compartible    │   run    │ - Con estado      │
│ - Plantilla      │          │ - Efímero         │
│ - Capas de solo  │          │ - Capa de         │
│   lectura        │          │   escritura       │
└─────────────────┘           └─────────────────┘
```

---

## `docker pull` — Descargar una imagen

Descarga una imagen desde un **registry** (por defecto, [[Registries y Etiquetado de Imágenes|Docker Hub]]).

```bash
# Sintaxis básica
docker pull <nombre_imagen>:<tag>

# Descargar la última versión de nginx
docker pull nginx
# Equivalente a: docker pull nginx:latest

# Descargar una versión específica
docker pull nginx:1.25-alpine
# ":1.25-alpine" es el TAG → versión 1.25 basada en Alpine Linux (más ligera)

# Descargar una imagen de Python
docker pull python:3.12-slim
# "slim" es una variante reducida de la imagen oficial

# Descargar desde un registry diferente a Docker Hub
docker pull ghcr.io/mi-usuario/mi-app:v2.0.0
# ghcr.io = GitHub Container Registry
```

> [!warning] Nunca uses `:latest` en producción
> El tag `latest` cambia con cada nueva publicación, lo que puede romper tu aplicación sin previo aviso. Siempre especifica una versión concreta:
> ```bash
> # ❌ Malo (en producción)
> docker pull node:latest
> 
> # ✅ Bueno
> docker pull node:20.11-alpine3.19
> ```
> Más sobre estrategias de etiquetado en [[Registries y Etiquetado de Imágenes]].

---

## Variantes comunes de imágenes

| Sufijo del tag | Significado | Tamaño típico | Caso de uso |
|---|---|---|---|
| *(sin sufijo)* | Imagen completa basada en Debian | Grande (~300-900 MB) | Desarrollo, cuando necesitas todas las herramientas |
| `-slim` | Debian con paquetes mínimos | Medio (~50-200 MB) | Producción cuando necesitas compatibilidad Debian |
| `-alpine` | Basada en Alpine Linux (musl libc) | Pequeño (~5-50 MB) | Producción optimizada para tamaño |
| `-bookworm`, `-bullseye` | Versión específica de Debian | Grande | Cuando necesitas una versión exacta de Debian |
| `-windowsservercore` | Basada en Windows Server | Muy grande (~5 GB) | Aplicaciones .NET legacy |

> [!tip] ¿Cuándo usar Alpine?
> Las imágenes **Alpine** son muy populares por su tamaño reducido (~5 MB la base). Sin embargo, usan **musl libc** en lugar de **glibc**, lo que puede causar incompatibilidades con algunas librerías nativas de C/C++. Si tienes problemas con dependencias en Alpine, prueba con `-slim` (basada en Debian con glibc).

---

## `docker build` — Construir una imagen personalizada

Construye una imagen a partir de un **[[Dockerfile - Anatomía Completa|Dockerfile]]**.

```bash
# Sintaxis básica (el punto "." indica el directorio actual como contexto de build)
docker build -t <nombre>:<tag> .

# Construir una imagen con nombre y tag
docker build -t mi-api:v1.0.0 .

# Construir con un Dockerfile en una ubicación diferente
docker build -t mi-api:v1.0.0 -f ./docker/Dockerfile.prod .

# Construir sin usar caché (reconstruir todo desde cero)
docker build --no-cache -t mi-api:v1.0.0 .

# Construir pasando argumentos de build (build args)
docker build --build-arg NODE_ENV=production -t mi-api:prod .

# Construir para múltiples plataformas (requiere buildx)
docker buildx build --platform linux/amd64,linux/arm64 -t mi-api:v1.0.0 .
```

> [!info] Más sobre Dockerfiles
> Los detalles sobre cómo escribir un `Dockerfile` se cubren en profundidad en [[Dockerfile - Anatomía Completa]] y [[Caché de Capas y Optimización]].

---

## `docker images` — Listar imágenes locales

```bash
# Listar todas las imágenes descargadas
docker images

# Resultado:
# REPOSITORY   TAG             IMAGE ID       CREATED        SIZE
# nginx        latest          a1b2c3d4e5f6   2 weeks ago    187MB
# nginx        1.25-alpine     b2c3d4e5f6a7   2 weeks ago    43.2MB
# python       3.12-slim       c3d4e5f6a7b8   3 days ago     131MB
# hello-world  latest          d4e5f6a7b8c9   3 months ago   13.3kB

# Filtrar imágenes por nombre
docker images nginx
# Solo muestra las imágenes de nginx

# Mostrar también imágenes intermedias (capas huérfanas)
docker images -a

# Mostrar solo los IDs de las imágenes
docker images -q

# Filtrar por imágenes "colgantes" (dangling — sin tag ni nombre)
docker images --filter "dangling=true"

# Ver el tamaño real en disco (las capas compartidas no se cuentan doble)
docker system df
# TYPE          TOTAL   ACTIVE  SIZE      RECLAIMABLE
# Images        4       2       350.2MB   187MB (53%)
# Containers    3       1       12.5kB    10kB (80%)
# Volumes       2       2       256MB     0B (0%)
```

---

## `docker inspect` — Radiografía completa de una imagen

El comando `inspect` es tu **herramienta de diagnóstico** principal. Devuelve un JSON detallado con toda la información del objeto Docker.

```bash
# Inspeccionar una imagen (devuelve JSON enorme)
docker inspect nginx:latest

# Usar --format para filtrar información específica:

# Arquitectura de la imagen
docker inspect nginx:latest --format='{{.Architecture}}'
# amd64

# Variables de entorno configuradas
docker inspect nginx:latest --format='{{json .Config.Env}}' | python3 -m json.tool
# [
#     "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
#     "NGINX_VERSION=1.25.3",
#     "NJS_VERSION=0.8.2"
# ]

# Puertos expuestos
docker inspect nginx:latest --format='{{json .Config.ExposedPorts}}'
# {"80/tcp":{}}

# Comando por defecto
docker inspect nginx:latest --format='{{json .Config.Cmd}}'
# ["nginx","-g","daemon off;"]

# Capas del sistema de archivos
docker inspect nginx:latest --format='{{json .RootFS.Layers}}' | python3 -m json.tool

# Directorio de trabajo
docker inspect nginx:latest --format='{{.Config.WorkingDir}}'
```

---

## `docker history` — Historial de capas

Muestra cada capa de la imagen y la instrucción del Dockerfile que la creó:

```bash
docker history nginx:latest

# IMAGE          CREATED       CREATED BY                                      SIZE
# a1b2c3d4e5f6   2 weeks ago   CMD ["nginx" "-g" "daemon off;"]                0B
# <missing>      2 weeks ago   EXPOSE map[80/tcp:{}]                           0B
# <missing>      2 weeks ago   COPY file:xxx in /etc/nginx/nginx.conf          1.23kB
# <missing>      2 weeks ago   RUN /bin/sh -c apt-get update && apt-get...     56.3MB
# <missing>      2 weeks ago   /bin/sh -c #(nop) FROM debian:bookworm-slim     74.8MB

# Sin truncar los comandos
docker history --no-trunc nginx:latest
```

---

## Otros comandos útiles para imágenes

### Eliminar imágenes

```bash
# Eliminar una imagen específica
docker rmi nginx:latest
# o por ID
docker rmi a1b2c3d4e5f6

# Forzar eliminación (incluso si hay contenedores detenidos)
docker rmi -f nginx:latest

# Eliminar TODAS las imágenes no usadas por contenedores activos
docker image prune -a
# Añade --force para no pedir confirmación

# Eliminar solo imágenes "dangling" (sin tag)
docker image prune
```

### Etiquetar imágenes

```bash
# Etiquetar una imagen existente con otro nombre/tag
docker tag nginx:latest mi-registro.com/nginx:v1.0.0

# Etiquetar para subir a Docker Hub
docker tag mi-api:latest miusuario/mi-api:v2.0.0

# Etiquetar para subir a GitHub Container Registry
docker tag mi-api:latest ghcr.io/miusuario/mi-api:v2.0.0
```

### Exportar e importar imágenes

```bash
# Guardar una imagen como archivo tar (para transferir sin registry)
docker save nginx:latest -o nginx-backup.tar

# Guardar múltiples imágenes
docker save nginx:latest postgres:16-alpine -o imagenes.tar

# Comprimir al guardar
docker save nginx:latest | gzip > nginx-backup.tar.gz

# Cargar una imagen desde un archivo tar
docker load -i nginx-backup.tar

# Cargar desde archivo comprimido
docker load < nginx-backup.tar.gz
```

> [!tip] ¿Cuándo usar save/load?
> - Cuando necesitas transferir imágenes a un servidor **sin acceso a Internet**.
> - Para **backups** de imágenes personalizadas.
> - En entornos **air-gapped** (sin conexión externa) como redes militares o bancarias.

---

## Tabla resumen de comandos de imágenes

| Comando | Descripción | Ejemplo |
|---|---|---|
| `docker pull` | Descargar imagen | `docker pull nginx:1.25-alpine` |
| `docker build` | Construir imagen desde Dockerfile | `docker build -t mi-app:v1 .` |
| `docker images` | Listar imágenes locales | `docker images` |
| `docker inspect` | Información detallada (JSON) | `docker inspect nginx:latest` |
| `docker history` | Ver capas de la imagen | `docker history nginx:latest` |
| `docker rmi` | Eliminar imagen | `docker rmi nginx:latest` |
| `docker tag` | Re-etiquetar imagen | `docker tag nginx mi-reg/nginx:v1` |
| `docker save` | Exportar imagen a tar | `docker save nginx -o backup.tar` |
| `docker load` | Importar imagen desde tar | `docker load -i backup.tar` |
| `docker image prune` | Limpiar imágenes sin usar | `docker image prune -a` |

---

> [!info] Navegación
> ◀ [[Instalación y Setup]] · ▶ [[Contenedores en Docker]]
