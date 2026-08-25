
> [!info] Navegación
> ◀ [[🐳 Índice - Guía Docker]] · ▶ [[Namespaces]]

---
## ¿Qué son los contenedores y por qué los necesitamos?

### El problema: "En mi máquina sí funciona" 🤷‍♂️

Si alguna vez has desarrollado software, esta frase te resultará dolorosamente familiar. Imagina este escenario:

> [!example] La pesadilla del desarrollador
> **Ana** desarrolla una aplicación web en su laptop con Windows. Usa **Node.js 18**, **PostgreSQL 15** y tiene configuradas ciertas variables de entorno. Todo funciona perfecto en su máquina.
> 
> Cuando **Carlos** (su compañero) clona el repositorio en su Mac, la aplicación no arranca. Carlos tiene **Node.js 16** y **PostgreSQL 14**. Cuando finalmente llega a producción (un servidor Linux), la app se rompe de nuevo porque el servidor tiene versiones diferentes de las librerías del sistema operativo.
> 
> **Resultado**: Tres entornos diferentes, tres resultados diferentes. Horas perdidas depurando problemas que no son del código.

Este problema existe porque **el software no vive aislado**. Depende de:

- La **versión del lenguaje** de programación (Python 3.8 vs 3.12).
- Las **librerías del sistema operativo** (openssl, libc, etc.).
- Las **variables de entorno** configuradas.
- Los **servicios externos** (bases de datos, caches, colas de mensajes).
- La **configuración del sistema operativo** en sí.

---

### La solución: Contenedores 📦

> [!tip] Analogía: La caja de mudanza estandarizada
> Imagina que te mudas de casa. Podrías llevar tus cosas sueltas en el maletero del coche: la lámpara se roza con los platos, los libros se mojan si llueve, y cada viaje es un caos diferente.
> 
> Ahora imagina que metes **TODO** lo que necesitas en una **caja de mudanza estandarizada**: los platos con su protección, los libros sellados, la lámpara bien envuelta. Esa caja funciona igual en cualquier camión, barco o avión. No importa el vehículo (la infraestructura), la caja siempre llega intacta.
> 
> **Un contenedor es esa caja estandarizada, pero para software.**

Un **contenedor** es una unidad de software que empaqueta:

1. **Tu código** (la aplicación).
2. **Todas sus dependencias** (librerías, frameworks, herramientas).
3. **La configuración** necesaria (variables de entorno, archivos de config).
4. **Un mini sistema de archivos** (basado en Linux) con todo lo que la app necesita para ejecutarse.

Todo esto se ejecuta de forma **aislada** del resto del sistema, pero compartiendo el **kernel** del sistema operativo anfitrión (host). Esto último es la clave que diferencia a los contenedores de las máquinas virtuales.

```
┌─────────────────────────────────────────────────┐
│              Máquina Anfitriona (Host)          │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Conten.1 │  │ Conten.2 │  │ Conten.3 │     │
│  │ Node.js  │  │ Python   │  │ Postgres │     │
│  │ App Web  │  │ API REST │  │ DB       │     │
│  └──────────┘  └──────────┘  └──────────┘     │
│         │            │             │            │
│  ┌──────────────────────────────────────┐      │
│  │          Docker Engine               │      │
│  └──────────────────────────────────────┘      │
│  ┌──────────────────────────────────────┐      │
│  │       Kernel del Sistema Operativo   │      │
│  └──────────────────────────────────────┘      │
│  ┌──────────────────────────────────────┐      │
│  │         Hardware (CPU, RAM, Disco)   │      │
│  └──────────────────────────────────────┘      │
└─────────────────────────────────────────────────┘
```

---

### ¿Qué papel juega Docker en todo esto?

**Docker no inventó los contenedores.** La tecnología de contenedores existe en Linux desde hace más de una década (LXC, chroot, etc.). Lo que Docker hizo fue **democratizar** y **estandarizar** el uso de contenedores, creando:

- Un **formato de imagen estándar** (la "receta" para crear contenedores).
- Una **CLI intuitiva** para gestionar contenedores.
- Un **ecosistema** ([[Registries y Etiquetado de Imágenes|Docker Hub]]) para compartir imágenes.
- Herramientas como **[[Docker Compose]]** para orquestar múltiples contenedores.

> [!info] Docker = Plataforma
> Docker no es solo "contenedores". Es una **plataforma completa** que incluye: el motor de contenedores (**Docker Engine**), la herramienta de escritorio (**Docker Desktop**), el registro de imágenes (**Docker Hub**), la orquestación local (**Docker Compose**) y más.

---

## Tabla Comparativa Definitiva: Bare Metal vs VMs vs Contenedores

### Las tres eras del despliegue

**Era 1 — Bare Metal (Servidores físicos):**
Cada aplicación se instalaba directamente en un servidor físico. Si necesitabas 5 aplicaciones, comprabas 5 servidores (o las metías todas en uno, rezando para que no colisionaran).

**Era 2 — Máquinas Virtuales (VMs):**
Con la **virtualización** (VMware, VirtualBox, Hyper-V), un solo servidor físico podía albergar múltiples "computadoras virtuales", cada una con su propio sistema operativo completo.

**Era 3 — Contenedores:**
Empaquetan solo la aplicación y sus dependencias, compartiendo el kernel del host. Son más ligeros, rápidos y eficientes.

> [!tip] Analogía: Los tres tipos de alojamiento
> - **Bare Metal** = Comprar una **casa entera** para cada inquilino. Máximo aislamiento, máximo desperdicio.
> - **VM** = Un **edificio de apartamentos** donde cada apartamento tiene su propia cocina, baño, instalación eléctrica y fontanería independientes. Buen aislamiento, pero mucha infraestructura duplicada.
> - **Contenedor** = Un **hotel** donde cada habitación es privada, pero todos comparten la estructura del edificio (fontanería, electricidad, recepción). Eficiente y rápido de "montar".

### La tabla comparativa

| Característica | 🖥️ Bare Metal | 🗄️ Máquina Virtual (VM) | 🐳 Contenedor |
|---|---|---|---|
| **¿Qué es?** | Aplicación corriendo directamente sobre el hardware físico | Un sistema operativo completo virtualizado sobre un hipervisor | Un proceso aislado que comparte el kernel del host |
| **Sistema operativo** | Uno solo, instalado en el hardware | Cada VM tiene su **propio SO completo** (kernel incluido) | Comparte el kernel del host; solo tiene las librerías necesarias |
| **Tamaño típico** | N/A (es el servidor completo) | **GBs** (una VM de Ubuntu pesa ~2-4 GB) | **MBs** (una imagen Alpine pesa ~5 MB) |
| **Tiempo de arranque** | Minutos (boot del servidor) | **30s - 2 min** (boot del SO completo) | **Milisegundos a segundos** |
| **Rendimiento** | Máximo (acceso directo al hardware) | **Overhead del 5-15%** por la capa de virtualización | **Casi nativo** (~1-3% de overhead) |
| **Aislamiento** | Nulo (todo comparte el mismo SO) | **Fuerte** (kernel separado por VM) | **Bueno** (aislamiento a nivel de proceso mediante [[Namespaces]]) |
| **Densidad** (cuántos caben en un host) | 1 SO por servidor | **~10-20 VMs** por servidor típico | **~100-1000 contenedores** por servidor |
| **Portabilidad** | Nula (atado al hardware) | Media (formato de VM varía entre hipervisores) | **Máxima** (misma imagen corre en cualquier host con Docker) |
| **Uso de recursos** | Eficiente pero inflexible | **Alto** (cada VM reserva CPU, RAM fija) | **Bajo** (comparte recursos del kernel dinámicamente) |
| **Seguridad** | Depende de la configuración del SO | **Alta** (aislamiento total del kernel) | **Media-Alta** (comparte kernel, pero tiene aislamiento con [[Namespaces]]/[[Cgroups]]) |
| **Caso de uso ideal** | Aplicaciones que necesitan rendimiento extremo (gaming, HPC) | Múltiples SO diferentes en un mismo servidor; máximo aislamiento | Microservicios, CI/CD, desarrollo local, escalado rápido |
| **Herramientas típicas** | Ansible, Chef, Puppet | VMware, VirtualBox, Hyper-V, KVM | Docker, Podman, containerd |

> [!warning] El aislamiento de los contenedores NO es perfecto
> Como los contenedores **comparten el kernel** del host, una vulnerabilidad a nivel de kernel podría permitir a un contenedor comprometido afectar al host o a otros contenedores. Las VMs, al tener su propio kernel, ofrecen un aislamiento más fuerte. Esto es especialmente relevante en entornos **multi-tenant** (donde diferentes clientes comparten infraestructura). Por eso existen soluciones como **gVisor** o **Kata Containers** que añaden capas extra de aislamiento. Más sobre esto en [[Seguridad en Docker]].

---

> [!info] Navegación
> ◀ [[🐳 Índice - Guía Docker]] · ▶ [[Namespaces]]
