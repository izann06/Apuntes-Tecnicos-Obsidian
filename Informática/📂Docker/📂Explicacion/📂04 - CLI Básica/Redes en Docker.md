# 🌐 Redes en Docker (Networks)

> [!info] Navegación
> ◀ [[Contenedores en Docker]] · ▶ [[Sistema de Archivos Efímero]]
> 📂 Sección: **04 - CLI Básica** · Ver también: [[Imágenes en Docker]] · [[Contenedores en Docker]]

---

## ¿Por qué necesitas entender las redes de Docker?

Las redes de Docker definen **cómo se comunican los contenedores entre sí** y con el mundo exterior. Cuando trabajas con múltiples contenedores (ej. una API + una base de datos + un cache Redis), necesitas que puedan "hablarse" entre sí de forma segura y controlada.

> [!tip] Analogía: Las redes como edificios y pisos
> Imagina que los contenedores son oficinas:
>
> - Si están en el **mismo edificio** (misma red Docker), pueden llamarse por teléfono interno (por nombre del contenedor).
>
> - Si están en **edificios diferentes** (redes diferentes), no se ven entre sí, a menos que establezcas una línea telefónica especial (conectar un contenedor a múltiples redes).
>
> - La **recepción del edificio** (el gateway de la red) gestiona las llamadas con el exterior (Internet, tu host).

---

## Tipos de redes en Docker

| Driver de red | Descripción | Aislamiento | Caso de uso |
|---|---|---|---|
| **bridge** (por defecto) | Red virtual privada donde los contenedores se comunican entre sí | Aislados del host, comunicación entre contenedores | **El más común.** Desarrollo y producción para apps de un solo host |
| **host** | El contenedor comparte la red del host directamente | Sin aislamiento de red | Máximo rendimiento de red o acceso directo a la interfaz del host |
| **none** | Sin red. El contenedor está completamente aislado | Aislamiento total | Contenedores que no necesitan red (procesamiento batch aislado) |
| **overlay** | Red que abarca múltiples hosts Docker (cluster) | Comunicación entre hosts | Docker Swarm / Kubernetes |
| **macvlan** | El contenedor obtiene una IP directamente en la red física | Aparece como un dispositivo físico en la LAN | Aplicaciones que necesitan IP dedicada en la red LAN |

---

## `docker network ls` — Listar redes

```bash
docker network ls

# Resultado:
# NETWORK ID NAME DRIVER SCOPE
# a1b2c3d4e5f6 bridge bridge local ← Red por defecto
# b2c3d4e5f6a7 host host local ← Red del host
# c3d4e5f6a7b8 none null local ← Sin red
```

Docker crea automáticamente tres redes al instalarse: `bridge`, `host` y `none`.

---

## Red bridge por defecto vs redes bridge personalizadas

> [!warning] Siempre crea redes personalizadas
> Docker crea una red `bridge` por defecto, pero tiene limitaciones importantes:
> 
> | Característica | Red bridge por defecto | Red bridge personalizada |
> |---|---|---|
> | **Resolución DNS por nombre** | ❌ No (solo por IP) | ✅ Sí (`ping mi-contenedor` funciona) |
> | **Aislamiento** | Todos los contenedores comparten la red | Solo los contenedores explícitamente conectados |
> | **Configuración** | No configurable | Personalizable (subred, gateway, etc.) |
> | **Comunicación automática** | Todos se ven entre sí | Solo los que estén en la misma red |
> 
> **Siempre crea redes personalizadas** para tus proyectos. La red por defecto es solo para pruebas rápidas.

---

## `docker network create` — Crear una red

```bash
# Crear una red bridge personalizada (lo más común)
docker network create mi-red

# Crear una red con configuración específica
docker network create \
 --driver bridge \
 --subnet 172.20.0.0/16 \
 --gateway 172.20.0.1 \
 --ip-range 172.20.240.0/20 \
 mi-red-configurada

# Crear una red con etiquetas
docker network create \
 --label environment=development \
 --label project=tienda \
 dev-network
```

---

## Ejecutar contenedores en una red

```bash
# Crear una red para nuestro proyecto
docker network create app-network

# Ejecutar contenedores directamente en esa red
docker run -d --name backend --network app-network node:20-alpine sleep infinity
docker run -d --name database --network app-network postgres:16-alpine

# 'backend' puede comunicarse con 'database' usando su NOMBRE:
docker exec backend ping database
# PING database (172.20.0.3): 56 data bytes
# 64 bytes from 172.20.0.3: seq=0 ttl=64 time=0.089 ms
```

---

## `docker network connect` / `disconnect` — Conectar y desconectar

```bash
# Conectar un contenedor EXISTENTE a una red
docker network connect app-network mi-contenedor

# Ahora el contenedor está en DOS redes simultáneamente
# Puede comunicarse con contenedores de ambas redes

# Desconectar un contenedor de una red
docker network disconnect app-network mi-contenedor

# Conectar con una IP estática específica
docker network connect --ip 172.20.0.100 app-network mi-contenedor
```

---

## `docker network inspect` — Examinar una red

```bash
docker network inspect app-network

# Resultado (resumido):
# [
# {
# "Name": "app-network",
# "Driver": "bridge",
# "IPAM": {
# "Config": [
# { "Subnet": "172.20.0.0/16", "Gateway": "172.20.0.1" }
# ]
# },
# "Containers": {
# "abc123": { "Name": "backend", "IPv4Address": "172.20.0.2/16" },
# "def456": { "Name": "database", "IPv4Address": "172.20.0.3/16" }
# }
# }
# ]
```

---

## DNS interno de Docker

> [!info] Cómo funciona el DNS interno
> Cuando creas una **red personalizada**, Docker activa un **servidor DNS interno** (embebido en el daemon) que permite a los contenedores **encontrarse entre sí por nombre**.
> 
> Esto es crucial porque las IPs de los contenedores **pueden cambiar** cada vez que se reinician. Usar nombres garantiza que la comunicación siempre funcione, independientemente de la IP asignada.

```
┌─────────────────────────────────────────┐
│ Red personalizada │
│ │
│ "api" ──────► DNS Docker ──────► "db" │
│ 172.20.0.2 resuelve nombre 172.20.0.3
│ │
│ La API se conecta a "db:5432" │
│ Docker traduce "db" → 172.20.0.3 │
└─────────────────────────────────────────┘
```

```bash
# La aplicación usa el NOMBRE del contenedor como hostname:
# postgresql://admin:secreto@database:5432/mi_app
# ^^^^^^^^
# Nombre del contenedor = hostname DNS
```

---

## Ejemplo práctico completo: Comunicación entre contenedores

> [!example] App web con base de datos
> ```bash
> # 1. Crear la red
> docker network create tienda-network
> 
> # 2. Ejecutar MySQL
> docker run -d \
> --name mysql-db \
> --network tienda-network \
> -e MYSQL_ROOT_PASSWORD=root123 \
> -e MYSQL_DATABASE=tienda \
> -v mysql-data:/var/lib/mysql \
> mysql:8.0
> 
> # 3. Ejecutar la API (conectándose a MySQL por NOMBRE)
> docker run -d \
> --name api-tienda \
> --network tienda-network \
> -p 3000:3000 \
> -e DB_HOST=mysql-db \
> -e DB_PORT=3306 \
> -e DB_NAME=tienda \
> -e DB_USER=root \
> -e DB_PASSWORD=root123 \
> mi-api-tienda:latest
> 
> # 4. Verificar la conexión desde la API
> docker exec api-tienda ping mysql-db
> # PING mysql-db (172.20.0.2): 56 data bytes
> # 64 bytes from 172.20.0.2: seq=0 ttl=64 time=0.089 ms
> 
> # 5. Verificar conectividad DNS
> docker exec api-tienda nslookup mysql-db
> # Server: 127.0.0.11 ← DNS interno de Docker
> # Address: 127.0.0.11#53
> # Name: mysql-db
> # Address: 172.20.0.2
> ```

---

## Red `host` — Sin aislamiento de red

```bash
# El contenedor comparte directamente la red del host
docker run -d --network host nginx

# No necesitas -p (publish) porque el contenedor USA los puertos del host
# nginx escucha directamente en el puerto 80 del host
# http://localhost:80 funciona directamente
```

> [!warning] Consideraciones de la red host
>
> - Solo funciona en **Linux**. En Docker Desktop (Mac/Windows), la red `host` se comporta como bridge porque Docker corre en una VM.
>
> - **Sin aislamiento de red**: El contenedor ve todas las interfaces de red del host.
>
> - **Sin mapeo de puertos**: Si la app escucha en el puerto 80, usa directamente el puerto 80 del host.
>
> - **Mejor rendimiento**: Elimina la capa de NAT (Network Address Translation).
>
> - **Riesgo**: El contenedor puede interferir con servicios del host.

---

## Red `none` — Aislamiento total

```bash
# Contenedor sin ninguna interfaz de red (excepto loopback)
docker run -d --network none mi-procesamiento-batch

# Solo tiene la interfaz lo (127.0.0.1)
docker exec mi-procesamiento-batch ip addr
# 1: lo: <LOOPBACK,UP,LOWER_UP>
# inet 127.0.0.1/8 scope host lo
```

Útil para contenedores que procesan datos locales y **no deben** tener acceso a la red por seguridad.

---

## Limpieza de redes

```bash
# Eliminar una red (solo si no tiene contenedores conectados)
docker network rm mi-red

# Eliminar todas las redes no usadas
docker network prune

# Forzar sin confirmación
docker network prune -f
```

---

## Tabla resumen de comandos de redes

| Comando | Descripción | Ejemplo |
|---|---|---|
| `docker network ls` | Listar redes | `docker network ls` |
| `docker network create` | Crear red | `docker network create mi-red` |
| `docker network rm` | Eliminar red | `docker network rm mi-red` |
| `docker network inspect` | Detalles de una red | `docker network inspect mi-red` |
| `docker network connect` | Conectar contenedor a red | `docker network connect mi-red cont` |
| `docker network disconnect` | Desconectar de red | `docker network disconnect mi-red cont` |
| `docker network prune` | Limpiar redes sin usar | `docker network prune` |

---

> [!info] Navegación
> ◀ [[Contenedores en Docker]] · ▶ [[Sistema de Archivos Efímero]]
