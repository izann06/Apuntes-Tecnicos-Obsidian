# ⚙️ Instalación y Setup

> [!info] Navegación
> ◀ [[Union Filesystems]] · ▶ [[Imágenes en Docker]]
> 📂 Sección: **03 - Instalación**

---

## Docker Desktop vs Docker Engine: ¿Cuál necesitas?

Docker ofrece dos productos principales. Elegir el correcto depende de tu sistema operativo y tu caso de uso:

| Característica | 🖥️ Docker Desktop | ⚙️ Docker Engine |
|---|---|---|
| **¿Qué es?** | Una **aplicación gráfica** (GUI) que incluye Docker Engine, Docker Compose, Docker Scout, y herramientas adicionales | El **motor de contenedores** puro, solo línea de comandos (CLI) |
| **Plataformas** | ✅ Windows, ✅ macOS, ✅ Linux | ✅ Solo Linux (nativo) |
| **Interfaz gráfica** | ✅ Sí (dashboard visual con contenedores, imágenes, volúmenes) | ❌ No (solo CLI) |
| **¿Cómo funciona en Windows/Mac?** | Ejecuta una **VM ligera de Linux** en segundo plano (WSL2 en Windows, VZ en Mac) | N/A (no disponible sin VM) |
| **Rendimiento** | Muy bueno, pero ligeramente inferior al nativo por la capa de VM | **Máximo** (nativo en Linux) |
| **Docker Compose incluido** | ✅ Sí (integrado como `docker compose`) | ❌ Se instala por separado (como plugin) |
| **Licencia** | ⚠️ **Gratuito para uso personal y empresas pequeñas** (<250 empleados Y <$10M ingresos). De pago para empresas grandes | ✅ **Gratuito y open source** (Apache 2.0) |
| **Actualizaciones** | Automáticas con la app | Manuales (apt, yum, etc.) |
| **Ideal para** | Desarrolladores en **Windows, Mac o Linux** que quieren una experiencia integrada | Servidores de **producción en Linux**, CI/CD, entornos headless |

> [!warning] Cuidado con la licencia de Docker Desktop
> Desde 2021, Docker Desktop **requiere una suscripción de pago** para empresas con más de 250 empleados o más de $10 millones en ingresos anuales. Docker Engine sigue siendo completamente gratuito y open source. Si trabajas en una empresa grande, verifica la política de licencias. Alternativas gratuitas: **Podman Desktop** o **Rancher Desktop**.

---

## Instalación de Docker Desktop

### Windows (con WSL2)

> [!info] Prerequisito: WSL2
> Docker Desktop en Windows utiliza **WSL2** (Windows Subsystem for Linux 2) como backend. WSL2 ejecuta un kernel de Linux real dentro de Windows, lo que permite a Docker funcionar de forma nativa.

```powershell
# 1. Instalar WSL2 (si no lo tienes)
wsl --install

# 2. Reiniciar el equipo

# 3. Descargar Docker Desktop desde:
# https://www.docker.com/products/docker-desktop/

# 4. Ejecutar el instalador y seguir el asistente
# Asegúrate de marcar "Use WSL 2 instead of Hyper-V"

# 5. Verificar la instalación (abrir PowerShell o terminal WSL):
docker --version
# Docker version 27.x.x, build xxxxxxx

docker compose version
# Docker Compose version v2.x.x
```

### macOS

```bash
# Opción 1: Descarga directa
# Ir a https://www.docker.com/products/docker-desktop/
# Descargar el .dmg (Apple Silicon o Intel según tu Mac)

# Opción 2: Con Homebrew
brew install --cask docker

# Abrir Docker Desktop desde Applications
# Verificar:
docker --version
docker compose version
```

### Linux (Ubuntu/Debian) — Docker Desktop

```bash
# En Linux, Docker Desktop es OPCIONAL. Puedes instalar solo Docker Engine.
# Si quieres Docker Desktop (GUI):

# 1. Descargar el paquete .deb desde:
# https://docs.docker.com/desktop/install/linux/

# 2. Instalar:
sudo apt-get install ./docker-desktop-<version>-amd64.deb
```

---

## Instalación de Docker Engine (Servidores Linux)

Esta es la opción recomendada para **servidores de producción** y entornos donde no necesitas interfaz gráfica.

### Ubuntu / Debian

```bash
# ============================================
# Paso 1: Eliminar versiones antiguas
# ============================================
sudo apt-get remove docker docker-engine docker.io containerd runc

# ============================================
# Paso 2: Instalar dependencias
# ============================================
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# ============================================
# Paso 3: Añadir la clave GPG oficial de Docker
# ============================================
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# ============================================
# Paso 4: Configurar el repositorio
# ============================================
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# ============================================
# Paso 5: Instalar Docker Engine + Compose Plugin
# ============================================
sudo apt-get update
sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

# ============================================
# Paso 6: Verificar la instalación
# ============================================
sudo docker run hello-world
```

### CentOS / RHEL / Fedora

```bash
# Eliminar versiones antiguas
sudo yum remove docker docker-client docker-client-latest \
    docker-common docker-latest docker-latest-logrotate \
    docker-logrotate docker-engine

# Instalar utilidades
sudo yum install -y yum-utils

# Añadir repositorio de Docker
sudo yum-config-manager --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# Instalar Docker
sudo yum install -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin

# Iniciar y habilitar el servicio
sudo systemctl start docker
sudo systemctl enable docker

# Verificar
sudo docker run hello-world
```

---

## Post-instalación: Usar Docker sin `sudo`

> [!tip] Usar Docker sin `sudo`
> Por defecto, Docker requiere permisos de `root`. Para ejecutar comandos Docker sin `sudo`, añade tu usuario al grupo `docker`:
> ```bash
> # Añadir tu usuario al grupo docker
> sudo usermod -aG docker $USER
> 
> # Cerrar sesión y volver a iniciar (o ejecutar):
> newgrp docker
> 
> # Verificar que funciona sin sudo
> docker run hello-world
> ```

> [!warning] Nota de seguridad
> El grupo `docker` otorga privilegios equivalentes a `root`. Un usuario en el grupo `docker` puede montar cualquier directorio del host dentro de un contenedor. Solo añade usuarios de confianza.

---

## Verificación post-instalación

Independientemente del método de instalación, ejecuta estos comandos para verificar que todo funciona:

```bash
# Versión de Docker
docker --version
# Docker version 27.x.x, build xxxxxxx

# Información completa del sistema Docker
docker info
# Client: Docker Engine - Community
#  Version: 27.x.x
# Server:
#  Storage Driver: overlay2
#  Cgroup Driver: systemd
#  Cgroup Version: 2
#  ...

# Ejecutar el contenedor de prueba
docker run hello-world
# Hello from Docker!
# This message shows that your installation appears to be working correctly.

# Versión de Docker Compose
docker compose version
# Docker Compose version v2.x.x

# (Opcional) Ejecutar un contenedor interactivo
docker run -it --rm ubuntu bash
# Dentro del contenedor:
cat /etc/os-release   # Verás que estás en Ubuntu
exit                   # Salir del contenedor
```

---

## Componentes instalados

Después de la instalación, tendrás estos componentes:

| Componente | Descripción | Comando de verificación |
|---|---|---|
| **Docker Engine** (`dockerd`) | El daemon que gestiona contenedores | `docker info` |
| **Docker CLI** (`docker`) | La herramienta de línea de comandos | `docker --version` |
| **containerd** | Runtime de contenedores de bajo nivel | `containerd --version` |
| **runc** | Runtime OCI que realmente ejecuta los contenedores | `runc --version` |
| **Docker Buildx** | Plugin para builds avanzados (multi-plataforma) | `docker buildx version` |
| **Docker Compose** (plugin) | Orquestación de múltiples contenedores | `docker compose version` |

---

> [!info] Navegación
> ◀ [[Union Filesystems]] · ▶ [[Imágenes en Docker]]
