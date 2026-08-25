# 📦 Union Filesystems (Sistema de archivos por capas)

> [!info] Navegación
> ◀ [[Cgroups]] · ▶ [[Instalación y Setup]]
> 📂 Sección: **02 - Tecnologías Subyacentes** · Ver también: [[Namespaces]] · [[Cgroups]]

---

## ¿Qué son los Union Filesystems?

Los **Union Filesystems** (también llamados **UnionFS** o **overlay filesystems**) son sistemas de archivos que permiten **superponer múltiples capas de archivos** en una sola vista unificada. Piensa en ellos como transparencias apiladas: cada transparencia tiene contenido diferente, pero cuando las miras todas juntas, ves una imagen completa.

Docker utiliza principalmente **OverlayFS** (en su versión `overlay2`) como su sistema de archivos por defecto.

> [!tip] Analogía: Las capas de un pastel
> Imagina que estás haciendo un pastel por capas:
> 
> 1. **Capa 1 (base)**: La masa del bizcocho (el sistema operativo base, como Ubuntu o Alpine).
> 2. **Capa 2**: La crema de chocolate (instalar Node.js).
> 3. **Capa 3**: Las fresas encima (copiar tu código).
> 4. **Capa 4**: La decoración final (configuración y CMD).
> 
> Cada capa se construye **encima de la anterior**. Si mañana quieres cambiar las fresas por arándanos (actualizar tu código), solo reemplazas la **capa 3**. No necesitas volver a hacer el bizcocho ni la crema. **Esto es exactamente cómo funcionan las imágenes Docker.**

---

## ¿Cómo funciona en la práctica?

Cada instrucción en un **[[Dockerfile - Anatomía Completa|Dockerfile]]** crea una **nueva capa** de solo lectura:

```dockerfile
FROM ubuntu:22.04          # Capa 1: Sistema operativo base (~77 MB)
RUN apt-get update         # Capa 2: Actualizar paquetes (~30 MB)
RUN apt-get install -y \   # Capa 3: Instalar dependencias (~50 MB)
    python3 python3-pip
COPY . /app                # Capa 4: Tu código (~5 MB)
CMD ["python3", "app.py"]  # Capa 5: Metadatos (0 MB, no crea capa real)
```

### Diagrama de capas

```
┌──────────────────────────────────────────────┐
│    Capa de Escritura (Container Layer)       │  ← Solo esta capa es
│    Archivos modificados en runtime           │     de lectura/escritura
├──────────────────────────────────────────────┤
│    Capa 4: COPY . /app (solo lectura)        │
├──────────────────────────────────────────────┤
│    Capa 3: RUN apt-get install (solo lectura)│
├──────────────────────────────────────────────┤
│    Capa 2: RUN apt-get update (solo lectura) │
├──────────────────────────────────────────────┤
│    Capa 1: FROM ubuntu:22.04 (solo lectura)  │
└──────────────────────────────────────────────┘
        IMAGEN (inmutable, compartible)
```

Cuando ejecutas un contenedor a partir de esta imagen, Docker añade una **capa de escritura** (thin writable layer) encima de todas las capas de solo lectura. Esta es la única capa donde el contenedor puede crear, modificar o eliminar archivos.

> [!warning] La capa de escritura es efímera
> Cuando el contenedor se elimina (`docker rm`), **la capa de escritura se destruye** junto con todos los datos que contenía. Por eso necesitas [[Volume Mounts]] o [[Bind Mounts]] para persistir datos.

---

## Las ventajas clave del sistema de capas

### 1. Caché de construcción (Build Cache) ⚡

Si cambias tu código pero no tus dependencias, Docker solo reconstruye la capa del código. Las capas anteriores se **reutilizan desde la caché**. Esto hace que las builds subsiguientes sean extremadamente rápidas.

```dockerfile
# Ejemplo optimizado para aprovechar la caché:
FROM node:20-alpine                # Capa 1 (cacheada)
WORKDIR /app                       # Capa 2 (cacheada)
COPY package*.json ./              # Capa 3 (cacheada si package.json no cambió)
RUN npm ci                         # Capa 4 (cacheada si la anterior no cambió)
COPY . .                           # Capa 5 ← SOLO ESTA se reconstruye
CMD ["node", "src/index.js"]       # Metadatos
```

> [!info] Más detalles
> La optimización de la caché de capas se explica a fondo en [[Caché de Capas y Optimización]].

### 2. Compartición de capas entre contenedores 💾

Si 10 contenedores usan la misma imagen base `ubuntu:22.04`, esa capa base solo existe **una vez** en disco. Los 10 contenedores la comparten. Solo se almacenan las diferencias.

```
Contenedor A (nginx)    Contenedor B (nginx)    Contenedor C (nginx)
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Capa escritura A │    │ Capa escritura B │    │ Capa escritura C │
├──────────────────┴────┴──────────────────┴────┴──────────────────┤
│                                                                  │
│   CAPAS DE LA IMAGEN nginx (COMPARTIDAS, solo lectura)           │
│   Solo existen UNA VEZ en disco                                  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

Esto es enormemente eficiente. Si tienes 100 contenedores basados en `node:20-alpine`, la imagen base de ~180 MB solo ocupa espacio una vez, no 100 veces.

### 3. Copy-on-Write (CoW) ✏️

¿Qué pasa cuando un contenedor necesita **modificar** un archivo que vive en una capa de solo lectura?

El sistema **copia** ese archivo a la capa de escritura del contenedor y ahí lo modifica. El archivo original en la capa de lectura **permanece intacto**. Esto se llama **Copy-on-Write (CoW)**.

```
ANTES de la modificación:

Capa escritura: (vacía)
Capa lectura:   /etc/config.txt → "valor original"

El contenedor ejecuta: echo "nuevo valor" > /etc/config.txt

DESPUÉS de la modificación:

Capa escritura: /etc/config.txt → "nuevo valor"     ← COPIA modificada
Capa lectura:   /etc/config.txt → "valor original"  ← INTACTO
```

El contenedor ve "nuevo valor" (la capa de escritura tiene prioridad). Otros contenedores basados en la misma imagen siguen viendo "valor original".

> [!tip] ¿Por qué importa CoW?
> - **Eficiencia**: No se duplican archivos innecesariamente. Solo los archivos modificados se copian.
> - **Velocidad**: Crear un contenedor es instantáneo porque no necesita copiar toda la imagen.
> - **Seguridad**: Las capas de la imagen nunca se modifican, garantizando consistencia.

---

## Inspeccionar las capas de una imagen

```bash
# Ver las capas de una imagen con docker history
docker history nginx:latest

# Resultado típico:
# IMAGE          CREATED       CREATED BY                                      SIZE
# a1b2c3d4e5f6   2 weeks ago   CMD ["nginx" "-g" "daemon off;"]                0B
# <missing>      2 weeks ago   EXPOSE map[80/tcp:{}]                           0B
# <missing>      2 weeks ago   COPY file:xxx in /etc/nginx/nginx.conf          1.23kB
# <missing>      2 weeks ago   RUN /bin/sh -c apt-get update && apt-get...     56.3MB
# <missing>      2 weeks ago   /bin/sh -c #(nop) FROM debian:bookworm-slim     74.8MB

# Inspeccionar los hashes SHA256 de cada capa
docker inspect nginx:latest --format='{{json .RootFS.Layers}}' | python3 -m json.tool
# [
#     "sha256:a1b2c3d4...",  ← Capa 1
#     "sha256:e5f6a7b8...",  ← Capa 2
#     "sha256:c9d0e1f2...",  ← Capa 3
#     ...
# ]

# Ver el tamaño total de las imágenes vs espacio real en disco
docker system df -v
```

---

## OverlayFS: El driver por defecto

Docker utiliza **OverlayFS** (específicamente `overlay2`) como su storage driver por defecto en la mayoría de distribuciones Linux modernas.

```bash
# Verificar el driver de almacenamiento
docker info | grep "Storage Driver"
# Storage Driver: overlay2
```

### ¿Cómo funciona OverlayFS?

OverlayFS combina dos directorios en una vista unificada:

| Directorio | Nombre en OverlayFS | Descripción |
|---|---|---|
| **Lower** | `lowerdir` | Las capas de solo lectura de la imagen (apiladas) |
| **Upper** | `upperdir` | La capa de escritura del contenedor |
| **Merged** | `merged` | La vista unificada que el contenedor ve como su `/` |
| **Work** | `workdir` | Directorio temporal que OverlayFS usa internamente |

```bash
# Ver los directorios OverlayFS de un contenedor
docker inspect mi-nginx --format='{{json .GraphDriver.Data}}' | python3 -m json.tool
# {
#     "LowerDir": "/var/lib/docker/overlay2/abc123/diff:...",
#     "MergedDir": "/var/lib/docker/overlay2/xyz789/merged",
#     "UpperDir": "/var/lib/docker/overlay2/xyz789/diff",
#     "WorkDir": "/var/lib/docker/overlay2/xyz789/work"
# }
```

### Otros storage drivers (históricos)

| Driver | Estado | Notas |
|---|---|---|
| **overlay2** | ✅ **Recomendado y por defecto** | Mejor rendimiento y estabilidad |
| `overlay` | ⚠️ Deprecado | Versión anterior de overlay2 |
| `aufs` | ⚠️ Deprecado | Fue el primer driver de Docker, ya no se recomienda |
| `devicemapper` | ⚠️ Deprecado | Usado en CentOS/RHEL antiguas |
| `btrfs` | ⚠️ Nicho | Solo si usas el filesystem btrfs |
| `zfs` | ⚠️ Nicho | Solo si usas ZFS |

---

## Resumen: ¿Por qué importan las capas?

| Beneficio | Explicación |
|---|---|
| **Builds rápidos** | Solo se reconstruyen las capas que cambiaron (caché) |
| **Almacenamiento eficiente** | Las capas se comparten entre imágenes y contenedores |
| **Arranque instantáneo** | No hay que copiar la imagen completa, solo añadir una capa de escritura |
| **Inmutabilidad** | Las capas de la imagen nunca cambian, garantizando reproducibilidad |
| **Distribución eficiente** | Al hacer `push`/`pull`, solo se transfieren las capas que faltan |

---

> [!info] Navegación
> ◀ [[Cgroups]] · ▶ [[Instalación y Setup]]
