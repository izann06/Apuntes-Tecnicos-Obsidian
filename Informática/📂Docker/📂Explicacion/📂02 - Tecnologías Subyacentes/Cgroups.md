# ⚖️ Cgroups (Control Groups: CPU, RAM y más)

> [!info] Navegación
> ◀ [[Namespaces]] · ▶ [[Union Filesystems]]
> 📂 Sección: **02 - Tecnologías Subyacentes** · Ver también: [[Namespaces]] · [[Union Filesystems]]

---

## ¿Qué son los Cgroups?

Los **cgroups** (abreviatura de *Control Groups*) son una funcionalidad del kernel de Linux que permite **limitar, contabilizar y aislar el uso de recursos** (CPU, memoria, disco I/O, red) de un grupo de procesos.

Si los **[[Namespaces]]** controlan **qué puede ver** un contenedor, los **cgroups** controlan **cuánto puede usar**.

> [!tip] Analogía: El contrato de alquiler del hotel
> Volvamos al hotel de los [[Namespaces]]. Los namespaces te dan tu habitación privada (aislamiento). Pero, ¿qué pasa si un huésped decide ducharse con toda el agua caliente durante 3 horas? Los demás se quedan sin agua.
> 
> Los **cgroups** son como las **reglas del hotel**: "Cada habitación puede usar máximo X litros de agua caliente al día, consumir máximo Y kWh de electricidad". Así, ningún huésped acapara todos los recursos y el hotel funciona correctamente.
>
> Sin cgroups, un contenedor podría consumir **toda** la CPU o **toda** la RAM del servidor, causando que los demás contenedores (y el propio host) dejen de funcionar.

---

## ¿Qué recursos controlan los Cgroups?

| Recurso | Controlador cgroup | ¿Qué limita? | Flag de Docker |
|---|---|---|---|
| **CPU** | `cpu`, `cpuset` | Tiempo de CPU que puede usar el contenedor | `--cpus`, `--cpu-shares` |
| **Memoria RAM** | `memory` | Cantidad máxima de RAM (y swap) | `--memory`, `--memory-swap` |
| **Disco I/O** | `blkio` | Velocidad de lectura/escritura en disco | `--device-read-bps`, `--device-write-bps` |
| **Red** | `net_cls`, `net_prio` | Prioridad y clasificación del tráfico de red | (Menos común en Docker directamente) |
| **PIDs** | `pids` | Número máximo de procesos que puede crear | `--pids-limit` |

---

## Limitando CPU

Docker ofrece varias formas de limitar el uso de CPU:

### `--cpus` — Límite absoluto de CPUs

```bash
# El contenedor puede usar como máximo 1.5 CPUs
docker run -d --name app-cpu --cpus="1.5" nginx

# Solo media CPU
docker run -d --cpus="0.5" mi-app

# En una máquina de 8 CPUs, esto significa:
# --cpus="1.0"  → El contenedor usa como máximo el 12.5% del total
# --cpus="4.0"  → El contenedor usa como máximo el 50% del total
# --cpus="8.0"  → El contenedor puede usar toda la CPU disponible
```

### `--cpu-shares` — Prioridad relativa (peso)

```bash
# Por defecto, cada contenedor tiene 1024 shares
# Un contenedor con 2048 shares obtiene el DOBLE de CPU que uno con 1024
# PERO solo cuando hay contención (competición por CPU)

docker run -d --name alta-prioridad --cpu-shares=2048 mi-app-critica
docker run -d --name baja-prioridad --cpu-shares=512 mi-app-secundaria

# Si ambos necesitan CPU al mismo tiempo:
# alta-prioridad obtiene ~80% (2048 / 2560)
# baja-prioridad obtiene ~20% (512 / 2560)
# Si solo uno necesita CPU, obtiene el 100%
```

### `--cpuset-cpus` — Fijar a CPUs específicas

```bash
# El contenedor solo puede ejecutarse en los CPUs 0 y 1
docker run -d --cpuset-cpus="0,1" mi-app

# Rango de CPUs
docker run -d --cpuset-cpus="0-3" mi-app  # CPUs 0, 1, 2 y 3
```

---

## Limitando Memoria (RAM)

### `--memory` — Límite de RAM

```bash
# Máximo 512 MB de RAM
docker run -d --name app-limitada --memory="512m" nginx

# Otras unidades:
# --memory="1g"     → 1 GB
# --memory="256m"   → 256 MB
# --memory="100000k" → ~100 MB
```

### `--memory-swap` — Límite de RAM + Swap

```bash
# 512 MB de RAM, 1 GB total (RAM + swap)
# Esto significa: 512 MB RAM + 512 MB de swap
docker run -d --memory="512m" --memory-swap="1g" mi-app

# Deshabilitar swap completamente
docker run -d --memory="512m" --memory-swap="512m" mi-app

# Swap ilimitado (no recomendado)
docker run -d --memory="512m" --memory-swap=-1 mi-app
```

### `--memory-reservation` — Límite blando (soft limit)

```bash
# Reserva blanda: Docker intentará que el contenedor no exceda 256 MB
# pero puede hacerlo temporalmente si hay memoria disponible
docker run -d --memory="512m" --memory-reservation="256m" mi-app
```

---

## Ejemplo práctico: Limitando recursos

```bash
# Ejecutar un contenedor con máximo 512 MB de RAM y 1 CPU
docker run -d \
  --name app-limitada \
  --memory="512m" \
  --cpus="1.0" \
  nginx

# Ver los límites aplicados en tiempo real
docker stats app-limitada
# CONTAINER ID   NAME           CPU %   MEM USAGE / LIMIT   MEM %
# a1b2c3d4       app-limitada   0.00%   5.2MiB / 512MiB     1.02%
```

---

## ¿Qué pasa si un contenedor excede sus límites?

> [!warning] Comportamiento al exceder límites
> - **Si excede la RAM**: El kernel de Linux activa el **OOM Killer** (Out Of Memory Killer) y **mata el contenedor**. Verás un exit code `137` (128 + señal 9 SIGKILL).
> - **Si excede la CPU**: El contenedor simplemente se **ralentiza** (throttling). No se mata, pero sus procesos se ejecutan más lento.

### Detectar un OOM Kill

```bash
# Verificar si un contenedor murió por OOM
docker inspect app-limitada --format='{{.State.OOMKilled}}'
# true  ← El OOM Killer lo mató

# El exit code será 137
docker inspect app-limitada --format='{{.State.ExitCode}}'
# 137  ← 128 + 9 (SIGKILL)
```

### Simulación: Contenedor hambriento de recursos

```bash
# Crear un contenedor que intenta consumir 1 GB de RAM, pero limitado a 256 MB
docker run -d \
  --name stress-test \
  --memory="256m" \
  polinux/stress \
  stress --vm 1 --vm-bytes 1G --timeout 60s

# Observar en tiempo real cómo Docker lo gestiona
docker stats stress-test

# El contenedor será MATADO por el OOM Killer
docker inspect stress-test --format='{{.State.ExitCode}}'
# 137  ← Código de salida = 128 + 9 (SIGKILL por OOM)
```

---

## Limitando Disco I/O

```bash
# Limitar velocidad de escritura a 10 MB/s en el dispositivo /dev/sda
docker run -d \
  --device-write-bps /dev/sda:10mb \
  --device-read-bps /dev/sda:10mb \
  mi-app

# Limitar IOPS (operaciones de I/O por segundo)
docker run -d \
  --device-write-iops /dev/sda:100 \
  --device-read-iops /dev/sda:100 \
  mi-app
```

---

## Limitando el número de procesos

```bash
# Máximo 100 procesos dentro del contenedor
# Previene fork bombs y procesos descontrolados
docker run -d --pids-limit=100 mi-app
```

> [!tip] Buena práctica: Siempre limita los recursos en producción
> **Nunca** ejecutes contenedores en producción sin límites de recursos. Un contenedor sin límites puede consumir toda la RAM o CPU del servidor, afectando a todos los demás contenedores y al propio sistema operativo.
> 
> ```bash
> # ❌ Malo (sin límites — ¡peligroso en producción!)
> docker run -d mi-app
> 
> # ✅ Bueno (con límites definidos)
> docker run -d \
>   --memory="512m" \
>   --cpus="1.0" \
>   --pids-limit=100 \
>   --restart=unless-stopped \
>   mi-app
> ```

---

## cgroups v1 vs cgroups v2

| Característica | cgroups v1 | cgroups v2 |
|---|---|---|
| **Arquitectura** | Múltiples jerarquías (una por controlador) | **Una única jerarquía** unificada |
| **Gestión** | Cada recurso (cpu, memory) se gestiona por separado | Todos los recursos se gestionan juntos |
| **Adopción** | Legacy, pero aún soportado | **Estándar moderno** (default en kernels recientes) |
| **Docker** | Soportado | Soportado (Docker 20.10+) |
| **Distribuciones** | Ubuntu <21.10, CentOS 7 | Ubuntu 21.10+, Fedora 31+, Debian 11+ |

```bash
# Verificar qué versión de cgroups usa tu sistema
stat -fc %T /sys/fs/cgroup/
# cgroup2fs  → cgroups v2
# tmpfs      → cgroups v1

# Verificar en Docker
docker info | grep "Cgroup"
# Cgroup Driver: systemd
# Cgroup Version: 2
```

---

> [!info] Navegación
> ◀ [[Namespaces]] · ▶ [[Union Filesystems]]
