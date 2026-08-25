# ⏳ Sistema de Archivos Efímero (Ephemeral Filesystem)

> [!info] Navegación
> ◀ [[Redes en Docker]] · ▶ [[Volume Mounts]]
> 📂 Sección: **05 - Persistencia de Datos** · Ver también: [[Volume Mounts]] · [[Bind Mounts]]

---

## El problema: Los datos mueren con el contenedor

> [!warning] Dato crucial
> **Cuando un contenedor se elimina, TODOS los datos escritos dentro de él se pierden.** Esto es por diseño: los contenedores están pensados para ser **efímeros** (temporales, desechables). Puedes destruirlos y recrearlos sin miedo, porque la "receta" (imagen) siempre está ahí para crear uno nuevo.

---

## ¿Por qué es efímero?

Recuerda la sección de [[Union Filesystems]]: cada contenedor tiene una **capa de escritura** (thin writable layer) encima de las capas de solo lectura de la imagen. Todos los cambios que hagas durante la ejecución — archivos creados, modificados, datos guardados — se almacenan **únicamente** en esa capa de escritura.

```
┌──────────────────────────────────────┐
│  Capa de escritura del contenedor    │ ← Aquí se guardan tus cambios
│  (SE ELIMINA cuando haces docker rm)│ ← ¡¡EFÍMERA!!
├──────────────────────────────────────┤
│  Capas de la imagen (solo lectura)   │ ← Estas SIEMPRE están
└──────────────────────────────────────┘
```

Cuando ejecutas `docker rm mi-contenedor`, esa capa de escritura **se elimina permanentemente**. Los datos que había dentro desaparecen para siempre.

> [!tip] Analogía: La pizarra del hotel
> Imagina que la habitación del hotel (contenedor) tiene una **pizarra blanca**. Puedes escribir lo que quieras en ella durante tu estancia. Pero cuando haces checkout (docker rm), el personal del hotel **borra la pizarra** completamente para el siguiente huésped. Si necesitas conservar lo que escribiste, debes **copiarlo a tu cuaderno** (volumen externo) antes de salir.

---

## Demostración práctica del problema

```bash
# 1. Crear un contenedor y escribir datos dentro
docker run -it --name demo ubuntu bash
echo "Datos super importantes" > /datos.txt
echo "Configuración vital" > /config.txt
cat /datos.txt
# Datos super importantes
exit

# 2. El contenedor se detuvo, pero NO se eliminó.
#    Los datos AÚN existen en la capa de escritura.
docker start demo
docker exec demo cat /datos.txt
# Datos super importantes  ← ¡Siguen ahí!

# 3. Ahora ELIMINAMOS el contenedor
docker rm -f demo

# 4. Crear un NUEVO contenedor con la misma imagen
docker run -it --name demo ubuntu bash
cat /datos.txt
# cat: /datos.txt: No such file or directory
# ¡¡DATOS PERDIDOS PARA SIEMPRE!!
exit
docker rm demo
```

> [!warning] Detener ≠ Eliminar
> - `docker stop` → El contenedor se **detiene** pero sigue existiendo. Sus datos en la capa de escritura se conservan. Puedes reiniciarlo con `docker start`.
> - `docker rm` → El contenedor se **elimina**. La capa de escritura se destruye. Los datos se pierden irrecuperablemente.

---

## ¿Cuándo necesitas persistencia?

| Caso de uso | ¿Necesita persistencia? | ¿Por qué? | Solución recomendada |
|---|---|---|---|
| Base de datos (PostgreSQL, MySQL, MongoDB) | ✅ **Siempre** | Los datos deben sobrevivir reinicios y actualizaciones | [[Volume Mounts]] |
| Archivos subidos por usuarios (fotos, PDFs) | ✅ **Siempre** | Son datos generados por el usuario, irreemplazables | [[Volume Mounts]] |
| Logs de aplicación | ✅ A menudo | Para análisis posterior, debugging, auditoría | [[Volume Mounts]] o log driver |
| Caché (Redis) | ⚠️ Depende | Si es caché regenerable, puede ser efímera. Si es cola de tareas, necesita persistencia | [[Volume Mounts]] si persistente |
| Código fuente en desarrollo | ✅ **Siempre** | Tu código no vive dentro del contenedor | [[Bind Mounts]] |
| Configuración personalizada | ✅ A menudo | Archivos de config que no están en la imagen | [[Bind Mounts]] (readonly) |
| Servidor web con archivos estáticos | ❌ Normalmente no | Los archivos están en la imagen, se recrean con cada build | Imagen |
| Datos temporales sensibles (tokens, secretos) | ⚠️ Especial | No deben escribirse en disco | tmpfs mount |

---

## Las soluciones de Docker para persistencia

Docker ofrece **tres mecanismos** para que los datos sobrevivan al ciclo de vida del contenedor:

```
           ┌────────────────────────────────────────┐
           │          CONTENEDOR DOCKER             │
           │                                        │
           │   /app/data  ←──┐     /app/code ←──┐  │
           │                 │                   │  │
           │   /app/secrets ←┼───┐               │  │
           └─────────────────┼───┼───────────────┼──┘
                             │   │               │
                    ┌────────┴───┴──┐   ┌────────┴───────┐
                    │  1. VOLUME    │   │  2. BIND MOUNT │
                    │  MOUNT        │   │                │
                    │               │   │  TÚ gestionas  │
                    │  Docker       │   │  la ubicación  │
                    │  gestiona     │   │                │
                    │  la ubicación │   │  ~/mi-proyecto │
                    │               │   │  /src/...      │
                    │  /var/lib/    │   └────────────────┘
                    │  docker/     │
                    │  volumes/    │   ┌────────────────┐
                    └──────────────┘   │  3. TMPFS      │
                                      │  MOUNT          │
                                      │                 │
                                      │  En RAM         │
                                      │  (no persiste)  │
                                      └─────────────────┘
```

| Tipo | ¿Dónde se almacena? | ¿Persiste? | Ideal para |
|---|---|---|---|
| **[[Volume Mounts]]** | Docker gestiona la ubicación (`/var/lib/docker/volumes/`) | ✅ Sí | Bases de datos, datos de producción |
| **[[Bind Mounts]]** | Una ruta específica de tu máquina | ✅ Sí | Código fuente en desarrollo, configuración |
| **tmpfs** | En **RAM** (memoria del host) | ❌ No | Datos sensibles temporales |

---

## tmpfs Mounts (Bonus: Datos en memoria)

Los tmpfs mounts no persisten datos, pero son útiles para información **sensible** que no debe escribirse en disco:

```bash
# Montar un directorio en RAM
docker run -d \
  --name app-segura \
  --tmpfs /app/secrets:rw,size=64m \
  mi-app:latest

# O con --mount (más explícito):
docker run -d \
  --mount type=tmpfs,target=/app/secrets,tmpfs-size=67108864 \
  mi-app:latest
```

| Característica | tmpfs Mount |
|---|---|
| **¿Dónde se almacena?** | En **RAM** (memoria del host) |
| **¿Persiste tras reinicio?** | ❌ No |
| **¿Persiste tras `docker rm`?** | ❌ No |
| **Caso de uso** | Datos sensibles temporales (tokens, secretos) que no deben escribirse en disco |
| **Plataforma** | Solo Linux (no funciona en Docker Desktop Mac/Windows) |
| **Rendimiento** | Extremadamente rápido (es RAM) |

---

> [!info] Siguiente paso
> Ahora que entiendes el problema, vamos a ver las dos soluciones principales en detalle:
> - [[Volume Mounts]] — La solución recomendada para datos persistentes (bases de datos, uploads, etc.)
> - [[Bind Mounts]] — La solución ideal para desarrollo (código fuente, configuración)

---

> [!info] Navegación
> ◀ [[Redes en Docker]] · ▶ [[Volume Mounts]]
