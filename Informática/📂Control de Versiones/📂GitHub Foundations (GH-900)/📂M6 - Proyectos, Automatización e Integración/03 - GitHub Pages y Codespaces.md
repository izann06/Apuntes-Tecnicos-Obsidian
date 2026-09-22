#github #gh-foundations #modulo-6 #pages #codespaces #github-dev

> [!info] Navegación
> ◀ [[02 - GitHub Actions (CI-CD)]] · ▶ [[🎓 Índice Maestro - GitHub Foundations]]

---

# 03 — GitHub Pages y Codespaces

> **Resumen ejecutivo:**
> 1. **GitHub Pages** aloja webs estáticas directamente desde un repositorio (gratis en repos públicos).
> 2. **github.dev** (tecla `.`) abre un editor ligero en el navegador. **Codespaces** es un entorno completo en la nube.
> 3. Los **Dev Containers** definen el entorno de un Codespace para que todos los desarrolladores trabajen igual.

---

## 1. GitHub Pages

**GitHub Pages** es un servicio de alojamiento web estático integrado en GitHub. Perfecto para documentación, portfolios o blogs.

### Configuración

Se publica desde:

- La rama `main` (raíz del repo).
- La carpeta `/docs` de la rama `main`.
- Una rama dedicada `gh-pages`.
- Un workflow de GitHub Actions (para generadores estáticos como Jekyll, Hugo o Quartz).

**URL por defecto:** `https://usuario.github.io/nombre-del-repositorio`

### Tipos de sitios Pages

| Tipo | URL | Repositorio |
| :--- | :--- | :--- |
| **Sitio de usuario** | `https://izanm.github.io` | Repo: `izanm/izanm.github.io` |
| **Sitio de proyecto** | `https://izanm.github.io/mi-proyecto` | Repo: `izanm/mi-proyecto` |
| **Sitio de organización** | `https://my-org.github.io` | Repo: `my-org/my-org.github.io` |

> [!TIP] Exam Tip — Pages es solo estático
> GitHub Pages solo sirve archivos estáticos (HTML, CSS, JS). No ejecuta código del lado del servidor (no Python, no Node.js, no PHP). Si necesitas backend, usa otro servicio.

### Dominio Personalizado

Puedes configurar un dominio propio (ej. `www.midominio.com`) en `Settings > Pages > Custom domain`. Requiere configurar registros DNS (CNAME o A records).

---

## 2. El Editor github.dev

Pulsa la tecla `.` en cualquier repositorio de GitHub y se abre un **editor VS Code ligero en el navegador**.

| Característica | github.dev |
| :--- | :--- |
| **Acceso** | Tecla `.` o cambia `github.com` por `github.dev` en la URL |
| **¿Ejecuta código?** | ❌ No tiene terminal ni puede ejecutar comandos |
| **¿Puede hacer commits?** | ✅ Sí, puede hacer commits y crear PRs |
| **Coste** | 🆓 Totalmente gratuito |
| **Uso ideal** | Ediciones rápidas de archivos, revisar PRs |

---

## 3. GitHub Codespaces

**Codespaces** es un entorno de desarrollo **completo** en la nube. Es como tener un VS Code con terminal, extensiones, Docker y todo lo necesario ejecutándose en un servidor remoto.

### Cómo iniciar un Codespace

1. En el repositorio → Botón `Code` → Pestaña `Codespaces` → `Create codespace on main`.
2. Desde la CLI: `gh codespace create`.
3. GitHub provisiona un contenedor de desarrollo en la nube en ~30 segundos.

### Ciclo de Vida

| Etapa | Descripción |
| :--- | :--- |
| **1. Asignación** | Se asigna una máquina virtual (VM) y el almacenamiento. |
| **2. Creación** | Se descarga y crea el contenedor basado en la imagen definida. |
| **3. Conexión** | El entorno se conecta al editor (web o local). |
| **4. Post-creación** | Se ejecutan los scripts de `postCreateCommand` (ej. `npm install`). |

| Estado/Políticas | Descripción |
| :--- | :--- |
| **Stopped (Inactividad)** | Se detiene automáticamente tras 30 minutos sin uso (configurable). Los datos se conservan. |
| **Deleted (Retención)** | Se elimina permanentemente tras 30 días de inactividad por defecto. |
| **Prebuilds** | Permiten precompilar el contenedor de forma automática. Cuando un desarrollador inicia un Codespace, arranca casi al instante. |

> [!WARNING] Codespaces tiene coste
> GitHub Free incluye **120 horas core/mes** gratuitas. Pasado el límite, se cobra por hora de uso. Los Codespaces con más CPU/RAM cuestan más. Configura el **spending limit** para no llevarte sorpresas.

### github.dev vs. Codespace

| | github.dev | Codespace |
| :--- | :--- | :--- |
| **Acceso** | Tecla `.` | Botón "Code" > Codespaces |
| **¿Ejecuta código?** | ❌ Solo editor | ✅ Terminal completa |
| **¿Tiene Docker?** | ❌ | ✅ |
| **¿Tiene extensiones?** | ⚠️ Limitadas (solo web) | ✅ Todas |
| **Coste** | Gratuito | Horas de cómputo |
| **Uso ideal** | Editar un archivo rápido | Desarrollo completo |

---

## 4. Personalización Avanzada y Dev Containers

### Dotfiles y Settings Sync

- **Dotfiles:** Puedes enlazar tu repositorio público de dotfiles (ej. `github.com/izanm/dotfiles`) en la configuración de GitHub. Codespaces los clonará automáticamente y aplicará tus configuraciones de bash/zsh, git, etc.
  
- **Settings Sync:** Activa la sincronización de configuración (VS Code) para que tus atajos de teclado, temas y snippets se apliquen a cualquier Codespace nuevo.
  
- **Tipo de máquina:** Puedes cambiar la CPU/RAM del Codespace incluso después de crearlo, pero requiere detener y reiniciar el entorno.

### Dev Containers

Un **Dev Container** es un archivo de configuración que define el entorno base de un Codespace. Garantiza que todos los desarrolladores del proyecto trabajen con las mismas herramientas y dependencias.

```json
// .devcontainer/devcontainer.json
{
  "name": "Node.js Development",
  "image": "mcr.microsoft.com/devcontainers/node:20",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "esbenp.prettier-vscode",
        "dbaeumer.vscode-eslint",
        "GitHub.copilot"
      ],
      "settings": {
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "npm install",
  "forwardPorts": [3000]
}
```

| Campo | Descripción |
| :--- | :--- |
| `image` | Imagen Docker base del contenedor |
| `features` | Herramientas adicionales a instalar (Docker, AWS CLI, etc.) |
| `customizations.vscode.extensions` | Extensiones de VS Code a instalar automáticamente |
| `postCreateCommand` | Comando que se ejecuta al crear el Codespace (ej. `npm install`) |
| `forwardPorts` | Puertos del contenedor que se exponen al navegador |

> [!TIP] Exam Tip — Deep Link
> Puedes compartir un enlace directo a un Codespace preconfigurado. Esto permite que cualquier persona lance un entorno de desarrollo listo para trabajar con un solo clic. Ideal para onboarding de nuevos desarrolladores.

---

## 5. Gists, Wikis, Discussions y Marketplace

### GitHub Gist

Mini-repositorios para compartir fragmentos de código. **Público** (aparece en búsquedas) o **Secreto** (solo con enlace). Se crea en [gist.github.com](https://gist.github.com).

### GitHub Wiki

Sistema de documentación colaborativa integrado en cada repositorio. Páginas en Markdown que cualquier colaborador puede editar.

> [!WARNING] El Wiki de un repo público siempre es público
> No existe la opción de hacer el Wiki privado dentro de un repo público.

### GitHub Discussions

Foro integrado para conversaciones abiertas: Q&A, anuncios, ideas, encuestas, show & tell. Se puede marcar una respuesta como correcta (Q&A) y convertir una discussion en issue.

### GitHub Marketplace

Tienda de herramientas y servicios de terceros que se integran con GitHub: CI/CD, monitorización, seguridad, gestión de proyectos. Algunas gratuitas, otras de pago.

### GitHub Sponsors

Programa para **financiar económicamente** a desarrolladores Open Source. Los sponsors pagan mensualmente. GitHub no cobra comisión en el primer año.
