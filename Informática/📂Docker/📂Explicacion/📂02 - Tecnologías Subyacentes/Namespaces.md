# 🔒 Namespaces (Aislamiento: Lo que el contenedor puede ver)

> [!info] Navegación
> ◀ [[Introducción al Mundo Docker]] · ▶ [[Cgroups]]
> 📂 Sección: **02 - Tecnologías Subyacentes** · Ver también: [[Cgroups]] · [[Union Filesystems]]

---

## ¿Qué son los Namespaces?

Los **Namespaces** son una funcionalidad del kernel de Linux que permite **particionar los recursos del sistema** de forma que cada proceso (o grupo de procesos) tenga su propia **vista aislada** de ciertos recursos del sistema.

Cuando Docker crea un contenedor, configura un conjunto de namespaces que le proporcionan al contenedor su propia **burbuja aislada**. Dentro de esa burbuja, el contenedor cree que tiene su propia máquina completa.

> [!tip] Analogía: Las habitaciones de un hotel
> Imagina un hotel. Cada huésped tiene su propia habitación con su propio número de puerta. Cuando estás dentro de tu habitación (namespace), **no ves** las habitaciones de los demás. Para ti, tu habitación es "tu mundo". Pero en realidad, todos comparten el mismo edificio (kernel), la misma fontanería (red) y la misma estructura eléctrica (hardware).
>
> Los namespaces hacen exactamente lo mismo: le dan a cada contenedor la **ilusión** de que tiene su propia máquina.

```
┌───────────────────────────────────────────────┐
│               CONTENEDOR DOCKER               │
│                                               │
│  ┌─────────────┐  ┌────────────┐             │
│  │  Tu App     │  │  Librerías │             │
│  └─────────────┘  └────────────┘             │
│                                               │
│  Aislado por NAMESPACES:                      │
│  ┌─────┐┌─────┐┌─────┐┌─────┐               │
│  │ PID ││ NET ││ MNT ││ UTS │               │
│  └─────┘└─────┘└─────┘└─────┘               │
│  ┌─────┐┌──────┐┌───────┐                    │
│  │ IPC ││ USER ││CGROUP │                    │
│  └─────┘└──────┘└───────┘                    │
└───────────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────┐
│            KERNEL DE LINUX                    │
└───────────────────────────────────────────────┘
```

---

## Los 7 tipos de Namespaces que usa Docker

Docker utiliza **todos** los namespaces disponibles en el kernel de Linux. Cada uno aísla un aspecto diferente del sistema:

| Namespace | ¿Qué aísla? | Efecto en el contenedor | Analogía |
|---|---|---|---|
| **PID** (Process ID) | Tabla de procesos | El contenedor ve sus procesos como PID 1, 2, 3... sin ver los del host | Cada hotel tiene su propia numeración de habitaciones |
| **NET** (Network) | Interfaces de red, IPs, puertos, tablas de ruteo | El contenedor tiene su propia IP, sus propios puertos. Puede usar el puerto 80 sin conflicto | Cada apartamento tiene su propio número de teléfono |
| **MNT** (Mount) | Puntos de montaje del sistema de archivos | El contenedor ve su propio sistema de archivos raíz (`/`) sin ver el del host | Cada inquilino tiene su propio armario |
| **UTS** (Unix Timesharing System) | Hostname y dominio | El contenedor puede tener su propio hostname (`web-server-1`) | Cada oficina tiene su propio nombre en la puerta |
| **IPC** (Inter-Process Communication) | Colas de mensajes, semáforos, memoria compartida | Los procesos de un contenedor solo pueden comunicarse entre sí | Cada departamento tiene su propio sistema de mensajería interno |
| **USER** | IDs de usuario y grupo | Un proceso puede ser root (UID 0) dentro del contenedor, pero mapeado a un usuario sin privilegios en el host | Puedes ser "el jefe" dentro de tu oficina, pero no del edificio entero |
| **CGROUP** | Vista de los cgroups | El contenedor solo ve sus propios límites de recursos | Cada inquilino ve solo su propio contrato de alquiler |

---

## Namespaces en detalle

### PID Namespace (Procesos)

El namespace PID es quizás el más fácil de entender. Le da a cada contenedor su **propia tabla de procesos**, comenzando desde PID 1.

**¿Por qué importa PID 1?**
En Linux, el proceso con **PID 1** es el proceso `init`, el "padre de todos los procesos". Es el primer proceso que arranca y el último que termina. Dentro de un contenedor, **tu aplicación** (o el ENTRYPOINT/CMD) se convierte en PID 1. Esto tiene implicaciones importantes:

- PID 1 debe manejar **señales** correctamente (SIGTERM para graceful shutdown).
- Si PID 1 muere, **el contenedor entero se detiene**.
- PID 1 es responsable de "adoptar" procesos huérfanos (reaping zombies).

> [!example] Demostración del namespace PID
> ```bash
> # Ejecutar un contenedor nginx
> docker run -d --name mi-nginx nginx
> 
> # Ver procesos DENTRO del contenedor
> docker exec mi-nginx ps aux
> # PID   USER   COMMAND
> # 1     root   nginx: master process    ← PID 1 dentro del contenedor
> # 29    nginx  nginx: worker process
> # 30    nginx  nginx: worker process
> 
> # Ver el MISMO proceso DESDE el host (Linux)
> ps aux | grep nginx
> # root  34521  nginx: master process    ← PID 34521 en el host
> # nginx 34556  nginx: worker process
> # nginx 34557  nginx: worker process
> ```
> 
> El proceso `nginx` es **PID 1** dentro del contenedor (cree que es el proceso principal del "sistema"), pero es **PID 34521** en el host. Esto es el namespace PID en acción.

> [!warning] El problema de los procesos zombie
> Si tu aplicación (PID 1) crea procesos hijos y no los "recoge" (reap) correctamente cuando terminan, se convierten en **procesos zombie**. En un sistema Linux normal, `init` se encarga de esto. Pero dentro de un contenedor, **tu app es PID 1** y debe hacerlo ella misma.
> 
> Solución: Usa `--init` en `docker run`:
> ```bash
> docker run --init -d mi-app
> ```
> Esto inyecta un proceso `tini` como PID 1 que se encarga de recoger zombies y reenviar señales a tu app.

---

### NET Namespace (Red)

El namespace de red es especialmente importante porque define cómo se comunican los contenedores. Cada contenedor obtiene:

- Su propia **interfaz de red** (`eth0`).
- Su propia **dirección IP**.
- Su propia **tabla de enrutamiento**.
- Su propio rango de **puertos** (cada contenedor puede usar el puerto 80 sin conflicto).

```bash
# Cada contenedor tiene su propia interfaz de red
docker exec mi-nginx ip addr
# Verás una interfaz eth0 con una IP interna (ej. 172.17.0.2)

# El host tiene una interfaz 'docker0' que actúa como puente (bridge)
ip addr show docker0
# Verás la IP del gateway (ej. 172.17.0.1)
```

#### Diagrama de red

```
┌────────────────────────────────────────────────────┐
│                   HOST                             │
│                                                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │ Cont. A  │  │ Cont. B  │  │ Cont. C  │        │
│  │ eth0     │  │ eth0     │  │ eth0     │        │
│  │172.17.0.2│  │172.17.0.3│  │172.17.0.4│        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │              │              │              │
│  ┌────┴──────────────┴──────────────┴────┐        │
│  │          docker0 (Bridge)             │        │
│  │          172.17.0.1                   │        │
│  └───────────────────┬───────────────────┘        │
│                      │                             │
│  ┌───────────────────┴───────────────────┐        │
│  │          eth0 (Host NIC)              │        │
│  │          192.168.1.100                │        │
│  └───────────────────────────────────────┘        │
└────────────────────────────────────────────────────┘
```

> [!info] Más sobre redes
> El funcionamiento completo de las redes Docker, tipos de drivers y comunicación entre contenedores se explica en detalle en [[Redes en Docker]].

---

### MNT Namespace (Sistema de Archivos)

El namespace MNT da a cada contenedor su propio **árbol de sistema de archivos**. Cuando un contenedor ve `/`, no es el `/` del host, sino su propio directorio raíz aislado, construido a partir de las capas de la imagen Docker (ver [[Union Filesystems]]).

```bash
# Dentro del contenedor, el sistema de archivos es completamente diferente al del host
docker exec mi-nginx ls /
# bin  boot  dev  docker-entrypoint.d  etc  home  lib  ...

# Este "/" NO es el "/" de tu máquina host
```

---

### USER Namespace (Usuarios)

El namespace USER permite que los IDs de usuario y grupo sean **diferentes dentro y fuera del contenedor**. Esto es una medida de seguridad crucial:

```bash
# Sin user namespace remapping: root en contenedor = root en host (¡peligroso!)
docker run --rm ubuntu id
# uid=0(root) gid=0(root)   ← El proceso es root

# Con user namespace remapping (configuración avanzada):
# root dentro del contenedor → usuario sin privilegios en el host
# uid=0(root) dentro → uid=100000 fuera
```

> [!warning] ¿Root dentro del contenedor es peligroso?
> Por defecto, si tu contenedor corre como `root` (UID 0), ese proceso tiene privilegios de `root` **en el host** también (limitados por otros mecanismos como capabilities y seccomp, pero aún así peligroso). Es una buena práctica ejecutar contenedores con un **usuario no root**. Más sobre esto en [[Seguridad en Docker]].

---

### UTS Namespace (Hostname)

Cada contenedor tiene su propio **hostname**, independiente del host:

```bash
# Ver el hostname del host
hostname
# mi-laptop

# Ver el hostname del contenedor (es su Container ID por defecto)
docker exec mi-nginx hostname
# a1b2c3d4e5f6

# Asignar un hostname personalizado
docker run -d --hostname web-server-1 nginx
docker exec $(docker ps -q -l) hostname
# web-server-1
```

---

### IPC Namespace (Comunicación Entre Procesos)

Aísla los mecanismos de comunicación entre procesos (colas de mensajes POSIX, semáforos, memoria compartida). Los procesos de un contenedor **no pueden** comunicarse mediante IPC con procesos de otro contenedor, a menos que compartan el mismo namespace IPC.

```bash
# Compartir IPC namespace entre dos contenedores (raro, pero posible)
docker run -d --name productor --ipc=shareable mi-app
docker run -d --name consumidor --ipc=container:productor mi-worker
```

---

### CGROUP Namespace

Limita la **visibilidad** que tiene el contenedor sobre la jerarquía de [[Cgroups]]. El contenedor solo ve sus propios cgroups, no los del host ni los de otros contenedores.

---

## Verificar los namespaces de un contenedor

En un sistema Linux, puedes inspeccionar los namespaces reales de un contenedor:

```bash
# Obtener el PID del proceso principal del contenedor en el host
PID=$(docker inspect --format '{{.State.Pid}}' mi-nginx)

# Ver los namespaces del proceso
ls -la /proc/$PID/ns/
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 cgroup -> 'cgroup:[4026532516]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 ipc -> 'ipc:[4026532450]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 mnt -> 'mnt:[4026532448]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 net -> 'net:[4026532453]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 pid -> 'pid:[4026532451]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 user -> 'user:[4026531837]'
# lrwxrwxrwx 1 root root 0 Jan 15 10:00 uts -> 'uts:[4026532449]'

# Los números entre corchetes son IDs únicos de namespace.
# Contenedores diferentes tendrán IDs diferentes → están aislados.
```

---

> [!info] Navegación
> ◀ [[Introducción al Mundo Docker]] · ▶ [[Cgroups]]
