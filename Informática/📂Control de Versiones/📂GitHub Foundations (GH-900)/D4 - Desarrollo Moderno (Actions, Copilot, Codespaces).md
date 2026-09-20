#github #actions #copilot #codespaces #gh-foundations

> [!info] Navegación
> ◀ [[D3 - Colaboración (Issues, PRs y Discussions)]] · ▶ [[D5 - Gestión de Proyectos]]

---

# Dominio 4 — Desarrollo Moderno

## 4.1 GitHub Actions

**GitHub Actions** es la plataforma de automatización CI/CD integrada en GitHub. Permite ejecutar flujos de trabajo automatizados (workflows) en respuesta a eventos del repositorio.

### Conceptos Clave
- **Workflow:** Un proceso automatizado definido en un archivo YAML dentro de `.github/workflows/`.
- **Event (Evento):** Lo que dispara el workflow. Ejemplos:
  - `push` → Al subir código
  - `pull_request` → Al abrir un PR
  - `schedule` → En un horario (cron)
  - `workflow_dispatch` → Manualmente desde la UI
- **Job:** Un conjunto de pasos que se ejecutan en un runner.
- **Step:** Una tarea individual dentro de un job (ejecutar un comando o usar una Action).
- **Runner:** La máquina virtual donde se ejecuta el job (Ubuntu, Windows, macOS).
- **Action:** Un componente reutilizable (puede ser tuyo o de terceros).

```yaml
# Ejemplo básico: .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Instalar dependencias
        run: npm install
      - name: Ejecutar tests
        run: npm test
```

### ¿Dónde encontrar Actions existentes?
- **GitHub Marketplace:** [github.com/marketplace?type=actions](https://github.com/marketplace?type=actions). Miles de Actions creadas por la comunidad y empresas.
- En la pestaña **"Actions"** de cualquier repositorio puedes buscar y configurar workflows directamente.

---

## 4.2 GitHub Copilot

**GitHub Copilot** es un asistente de programación basado en IA (basado en modelos de OpenAI) que sugiere líneas de código o funciones completas en tiempo real dentro del editor.

### ¿Cómo funciona?
Analiza el código que has escrito, los comentarios y el contexto del archivo para generar sugerencias de código en línea. Se integra como extensión en VS Code, JetBrains, Vim, etc.

### Planes
| | GitHub Copilot Individual | GitHub Copilot Business |
| :--- | :--- | :--- |
| **Precio** | De pago (o gratis para estudiantes/OSS) | De pago por asiento |
| **Gestión** | Individual | Administrada por la organización |
| **Excluir archivos** | ❌ | ✅ Política de exclusión de archivos |
| **Logs de auditoría** | ❌ | ✅ |

> [!tip] Gratis para estudiantes
> Con el **GitHub Student Developer Pack**, obtienes acceso gratuito a GitHub Copilot Individual. Actívalo en [education.github.com](https://education.github.com).

### Cómo empezar
1. Activa Copilot en `Settings > GitHub Copilot`.
2. Instala la extensión en tu editor (VS Code: busca "GitHub Copilot").
3. Empieza a escribir código y acepta sugerencias con `Tab`.

---

## 4.3 GitHub Codespaces

**GitHub Codespaces** es un entorno de desarrollo en la nube (basado en VS Code) que se ejecuta directamente en los servidores de GitHub. Permite desarrollar sin instalar nada en tu máquina local.

### Cómo iniciar un Codespace
- En cualquier repositorio, haz clic en **"Code" → "Codespaces" → "Create codespace on main"**.
- También puedes crearlo desde la CLI: `gh codespace create`.

### Ciclo de Vida de un Codespace
1. **Creation:** Se crea el contenedor de desarrollo.
2. **Running:** Está activo y puedes trabajar.
3. **Stopped:** Se para por inactividad (por defecto tras 30 min). Los datos se conservan.
4. **Rebuild:** Recrea el contenedor (útil cuando cambias la configuración).
5. **Deleted:** Se elimina permanentemente junto con sus datos no guardados.

> [!warning] Los Codespaces tienen un coste
> GitHub Free incluye un límite mensual gratuito de horas de Codespace. Pasado ese límite, se cobra por hora de uso según el tipo de máquina.

### Personalización con Dev Containers
Un **Dev Container** es un archivo de configuración (`.devcontainer/devcontainer.json`) que define el entorno del Codespace: imagen de Docker a usar, extensiones de VS Code a instalar, variables de entorno, etc. Garantiza que todos los desarrolladores del equipo tengan el mismo entorno.

```json
// .devcontainer/devcontainer.json
{
  "name": "Node.js Dev",
  "image": "mcr.microsoft.com/devcontainers/node:18",
  "customizations": {
    "vscode": {
      "extensions": ["esbenp.prettier-vscode", "dbaeumer.vscode-eslint"]
    }
  }
}
```

### Compartir un Codespace (Deep Link)
Puedes compartir un enlace directo a un Codespace o al editor de un archivo específico para colaboración rápida.

### El editor github.dev (vs. Codespace)

| | github.dev | GitHub Codespace |
| :--- | :--- | :--- |
| **Acceso** | Pulsa `.` en cualquier repo | Desde el botón "Code" del repo |
| **¿Ejecuta código?** | ❌ Solo editor, no terminal | ✅ Terminal completa, puede ejecutar |
| **Entorno** | VS Code en el navegador (ligero) | Contenedor de desarrollo completo |
| **Coste** | Gratuito | Tiene coste (horas de cómputo) |
| **Uso ideal** | Editar archivos rápidamente | Desarrollo completo de una feature |
