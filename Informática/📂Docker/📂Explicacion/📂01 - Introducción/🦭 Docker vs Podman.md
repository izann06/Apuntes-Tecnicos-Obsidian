#docker #podman #contenedores #devops #kubernetes

> [!info] Navegación
> ◀ [[🐳Introducción al Mundo Docker]] · ▶ [[⚖️ Cgroups (Control Groups. CPU, RAM y más)]]

---

# 🦭 Docker vs. Podman: ¿Cuál deberías elegir?

Aunque [[🐳Introducción al Mundo Docker|Docker]] es el rey indiscutible cuando hablamos de contenedores, **Podman** (desarrollado por Red Hat) ha ganado una tracción enorme como su principal alternativa. A continuación, desglosamos las diferencias técnicas clave.

## 1. Licenciamiento y Modelo Económico

- **Docker Desktop**: Requiere una **licencia de pago** para uso comercial en empresas de más de 250 empleados o con una facturación superior a 10 millones de dólares anuales.

- **Podman**: Es un proyecto *Open Source* liberado a la comunidad. Es **100% gratuito** sin importar el tamaño o facturación de la empresa.

---

## 2. Arquitectura y Compatibilidad OCI

La diferencia arquitectónica más grande está en cómo gestionan los procesos en el sistema operativo:

- **Motor con Demonio (Docker)**: Docker requiere un proceso en segundo plano (el demonio `dockerd`) para gestionar todo el ciclo de vida de los contenedores. Normalmente se ejecuta con altos privilegios.

- **Daemonless (Podman)**: Podman opera bajo un modelo **sin demonio**. Los contenedores se ejecutan como procesos hijos directos del usuario que lanza el comando. Esto favorece enormemente la seguridad (*rootless* por defecto).

Ambos motores son totalmente compatibles con la especificación **OCI (Open Container Initiative)**, lo que significa que un contenedor creado con Docker funcionará en Podman y viceversa.

### Experiencia de Usuario

- **CLI**: Podman fue diseñado para ser un reemplazo 1:1 de Docker en la terminal. Puedes crear un alias para no tener que reaprender comandos:

  ```bash
  alias docker=podman
  ```
  
  Los comandos son idénticos: `podman run`, `podman ps`, `podman build`.
  
- **Desktop**: Existe **Podman Desktop**, que ofrece un panel visual (Dashboard) muy similar a Docker Desktop para gestionar imágenes, volúmenes, extensiones y Pods de forma gráfica.

---

## 3. Construcción de Imágenes

- **Naming Convention**: La convención nativa en Podman es llamar al archivo `Containerfile`. Sin embargo, Podman reconoce y procesa automáticamente los archivos llamados `Dockerfile` sin que tengas que hacer modificaciones.

- **Sintaxis**: El comando de construcción utiliza los mismos parámetros que Docker:

  ```bash
  podman build -t mi-app:latest .
  ```

---

## 4. Orquestación Local: Podman Compose

Puedes desplegar tus archivos `docker-compose.yml` habituales utilizando la herramienta `podman-compose`.

```bash
podman-compose up -d
```

> [!IMPORTANT] Permisos de Volúmenes y el sufijo `:z`
> Si tu sistema Linux utiliza un control de acceso fuerte (como SELinux, muy común en entornos Red Hat), debes agregar el sufijo `:z` (o `:Z`) en el mapeo de tus volúmenes. 
> Esto le indica a Podman que debe reetiquetar el contexto de seguridad del directorio para que el contenedor no sufra bloqueos de escritura.
> ```bash
> # En la terminal (CLI)
> podman run -v /mi/ruta/local:/ruta/contenedor:z nginx
> 
> # En tu archivo docker-compose.yml
> volumes:
>   - /mi/ruta/local:/ruta/contenedor:z
> ```

*Nota*: Ciertas funcionalidades exclusivas y modernas de Docker Compose (como `develop.watch`) no producen un error en Podman, simplemente son ignoradas de manera silenciosa.

---

## 5. Características Únicas de Podman (Diferenciadores Clave)

Podman brilla especialmente por su integración nativa con conceptos de Kubernetes.

### Gestión Nativa de Pods

Podman permite crear y gestionar **Pods**. Un Pod es un concepto traído de Kubernetes: un grupo de uno o más contenedores que comparten la misma red, namespaces e IP (`localhost`).

```bash
# 1. Crear un Pod vacío exponiendo el puerto 8084 al host
podman pod create --name wordpress-pod -p 8084:80

# 2. Arrancar contenedores y asignarlos directamente a ese Pod
podman run -d --pod wordpress-pod --name mysql -e MYSQL_ROOT_PASSWORD=secreto mariadb
podman run -d --pod wordpress-pod --name wp -e WORDPRESS_DB_HOST=127.0.0.1 wordpress
```

> [!tip] Ejecución Directa de Manifiestos YAML (`play kube`)
> Podman permite ejecutar archivos YAML nativos de Kubernetes directamente en tu máquina local sin necesidad de instalar clústeres locales complejos como Minikube o Kind.
> ```bash
> podman play kube --port 8085:80 mi-manifiesto-k8s.yaml
> ```
> Esto hace que la transición de desarrollo local al despliegue en un clúster Kubernetes real sea mucho más natural.

---

## 6. Veredicto: ¿Cuándo usar cuál? (Ejemplos Reales)

La elección entre uno u otro depende del contexto de tu proyecto o empresa.
### ¿Cuándo elegir Docker?

- **Eres principiante o estás aprendiendo:** El 99% de los tutoriales de internet, foros (StackOverflow) y documentación oficial asumen que usas Docker. Si encuentras un error, será más fácil de solucionar.

- **Tu ecosistema depende mucho de Docker Compose:** Aunque Podman soporta Compose, si tu proyecto hace uso intensivo de características muy nuevas de Compose (como *watch* o *build hooks*), Docker es la apuesta segura.

- **Ejemplo Real:** Estás montando tu *Homelab* personal (servidores en casa) con aplicaciones como Immich, Nextcloud o n8n usando archivos `docker-compose.yml` que encontraste en GitHub. Sigue usando Docker, te ahorrará quebraderos de cabeza con los permisos (`:z`).

### ¿Cuándo elegir Podman?

- **Entornos empresariales restrictivos o de alta seguridad:** Si trabajas en un banco o una institución pública donde por seguridad informática está prohibido ejecutar procesos como administrador (*root*), Podman es la solución ideal gracias a su arquitectura *Daemonless* y *Rootless*.

- **Desarrollo orientado a Kubernetes:** Si tu objetivo final es desplegar la aplicación en un clúster de Kubernetes en producción, Podman te permite trabajar localmente con el mismo formato (Pods) y usar directamente los manifiestos YAML de K8s (`podman play kube`), acortando la brecha entre desarrollo y producción.

- **Ejemplo Real:** Trabajas en una gran consultora (más de 250 empleados) y el departamento legal no quiere pagar las licencias de Docker Desktop. Además, los servidores de producción utilizan Red Hat Enterprise Linux (RHEL). Podman es la opción lógica, gratuita y nativa para ese sistema.

---

## 📊 Tabla Comparativa Resumida

| Característica | 🐳 Docker | 🦭 Podman |
| :--- | :--- | :--- |
| **Licencia Comercial** | 💰 De pago (>250 emp. o >10M$ facturación) | 🆓 100% Gratuito (Open Source) |
| **Arquitectura** | Motor con Demonio (`dockerd`) | *Daemonless* (Sin demonio) |
| **Manejo de Pods** | ❌ No soportado nativamente | ✅ Soportado de forma nativa |
| **Compatibilidad K8s YAML** | ❌ Requiere herramientas extra | ✅ Nativo (`podman play kube`) |
| **Seguridad por defecto** | Requiere privilegios root | *Rootless* (Procesos de usuario normal) |

---


