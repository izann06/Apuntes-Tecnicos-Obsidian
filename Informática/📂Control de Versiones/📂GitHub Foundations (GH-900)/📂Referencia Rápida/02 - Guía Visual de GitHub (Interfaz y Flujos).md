#github #gh-foundations #cheatsheet #referencia #interfaz

> [!info] Navegación
> ◀ [[01 - Todos los Comandos de Git]] · ▶ [[🎓 Índice Maestro - GitHub Foundations]]

---

# 02 — Guía Visual de GitHub: Interfaz, Secciones y Flujos

> **Cómo usar este archivo:** Una guía de referencia de todo lo que puedes hacer dentro de un repositorio de GitHub, sección por sección. Perfecto para el examen y para la práctica real.

---

## 🏠 La Pantalla Principal de un Repositorio

Al entrar a cualquier repositorio en GitHub, verás una barra de pestañas en la parte superior. Cada pestaña es un "mundo" dentro del repositorio:

```
📁 Code | 🐛 Issues | 🔀 Pull Requests | ▶️ Actions | 📋 Projects | 📖 Wiki | 🔒 Security | 💡 Insights | ⚙️ Settings
```

---

## 📁 1. Pestaña CODE (El Corazón del Repositorio)

**¿Qué es?** La vista principal. Muestra todos los archivos del repositorio tal como están en la rama seleccionada.

**¿Qué puedes hacer aquí?**

| Elemento | Descripción |
| :--- | :--- |
| **Selector de rama** | Cambia entre ramas para ver su estado de archivos |
| **Botón `Code ▼`** | Obtén la URL para clonar (HTTPS, SSH, GitHub CLI) o descarga el ZIP |
| **Archivos y carpetas** | Navega por el código. Al hacer clic en un archivo, lo ves en el visor con syntax highlighting |
| **Vista de commits** | El número de commits junto a cada archivo indica cuándo fue modificado por última vez |
| **README.md** | Si existe, se renderiza automáticamente debajo de los archivos (es la "portada" del repo) |
| **Botón `+`** | Crea un archivo nuevo o sube archivos desde el navegador |
| **`.` (punto)** | Abre el repositorio en **github.dev** (VS Code en el navegador) |

### Archivos Clave que GitHub Reconoce Automáticamente

| Archivo | ¿Qué hace GitHub con él? |
| :--- | :--- |
| `README.md` | Lo renderiza como portada del repo / carpeta |
| `LICENSE` | Muestra el tipo de licencia en la sidebar |
| `.gitignore` | No hay magia extra, pero es recomendado tenerlo desde el principio |
| `CODEOWNERS` | Define automáticamente quién debe revisar qué archivos en los PRs |
| `CONTRIBUTING.md` | GitHub lo enlaza cuando alguien abre un Issue o PR |
| `SECURITY.md` | GitHub lo muestra en la pestaña Security |
| `.github/PULL_REQUEST_TEMPLATE.md` | Pre-rellena el cuerpo de cada nuevo Pull Request |
| `.github/ISSUE_TEMPLATE/` | Carpeta con plantillas para diferentes tipos de Issue |
| `.github/workflows/` | Carpeta donde viven los archivos YAML de GitHub Actions |

---

## 🐛 2. Pestaña ISSUES (Gestión de Tareas y Bugs)

**¿Qué es?** El sistema de seguimiento de tareas, bugs, peticiones de funcionalidades y discusiones del proyecto.

**¿Qué puedes hacer aquí?**

### Crear un Issue — Paso a Paso

1. Haz clic en **New Issue**.
2. Si hay plantillas configuradas, elige la que corresponda (Bug Report, Feature Request...).
3. Rellena:
   - **Title**: Título descriptivo (ej. "El botón de login no funciona en Firefox").
   - **Body**: Descripción detallada. Puedes usar Markdown, adjuntar imágenes (drag & drop) y mencionar código con backticks.
   - **Assignees** (sidebar derecho): Asigna el issue a una persona responsable.
   - **Labels** (sidebar derecho): Etiquetas como `bug`, `enhancement`, `documentation`, `good first issue`.
   - **Projects** (sidebar derecho): Asocia el issue a un GitHub Project.
   - **Milestone** (sidebar derecho): Asocia el issue a un hito/versión.
4. Haz clic en **Submit new issue**.

### Gestionar Issues

| Acción | Cómo |
| :--- | :--- |
| **Cerrar un issue** | Botón "Close issue" o escribir `Closes #42` en un commit/PR |
| **Reabrir** | Botón "Reopen issue" |
| **Filtrar** | Por label, assignee, milestone, estado (open/closed) |
| **Mencionar a alguien** | `@usuario` en cualquier comentario |
| **Mencionar otro issue** | `#número` (crea un enlace automático) |
| **Vincular un PR** | En el PR, escribir "Closes #42" cierra el issue al mergear |

### Labels (Etiquetas)

GitHub crea estas etiquetas por defecto:

| Label | Significado |
| :--- | :--- |
| `bug` | Algo no funciona como debería |
| `enhancement` | Petición de nueva funcionalidad |
| `documentation` | Mejoras en la documentación |
| `good first issue` | Ideal para nuevos contribuidores |
| `help wanted` | Se busca ayuda extra |
| `invalid` | El issue no es válido o relevante |
| `question` | Pregunta o duda |
| `wontfix` | El equipo ha decidido no corregir esto |
| `duplicate` | Ya existe otro issue igual |

---

## 🔀 3. Pestaña PULL REQUESTS (Revisión y Fusión de Código)

**¿Qué es?** El mecanismo central de colaboración en GitHub. Un PR es una solicitud formal para fusionar los cambios de una rama en otra. Incluye una discusión de revisión de código.

### Crear un Pull Request — Paso a Paso

1. Sube tu rama con cambios: `git push origin feature/mi-rama`.
2. GitHub mostrará un banner amarillo: **"Compare & pull request"** → haz clic.
3. Configura:
   - **Base branch**: La rama a la que quieres fusionar (normalmente `main`).
   - **Compare branch**: Tu rama con los cambios.
   - **Title**: Mensaje descriptivo del PR.
   - **Body**: Descripción de qué cambia, por qué, y cómo probar. Puedes usar `Closes #42` para vincular issues.
   - **Reviewers**: Solicita revisión a compañeros.
   - **Assignees**: Persona responsable del PR.
   - **Labels, Projects, Milestone**: Igual que en Issues.
4. Elige el tipo:
   - **"Create Pull Request"**: PR listo para revisión.
   - **"Create Draft Pull Request"**: PR en borrador (no listo para revisión, es de trabajo).
5. Haz clic en **Create pull request**.

### El Proceso de Code Review

| Paso | Acción |
| :--- | :--- |
| **Revisar archivos** | Pestaña "Files changed" para ver el diff completo |
| **Comentar líneas** | Clic en el `+` junto a una línea para añadir un comentario |
| **Sugerir cambios** | En el comentario de línea, clic en "Add a suggestion" (el autor puede aplicarla con 1 clic) |
| **Aprobar** | Review → "Approve" |
| **Solicitar cambios** | Review → "Request changes" (bloquea el merge hasta que se arreglen) |
| **Comentar solo** | Review → "Comment" (sin bloquear ni aprobar) |

### Hacer el Merge

Una vez aprobado el PR, el autor puede fusionarlo:

| Opción de Merge | Historial resultante | Cuándo usarla |
| :--- | :--- | :--- |
| **Merge commit** | Conserva todos los commits + crea uno de merge | Por defecto. Historial completo |
| **Squash and merge** | Aplana todos los commits en uno solo | Para PRs con commits de "trabajo en progreso" |
| **Rebase and merge** | Reaplica los commits linealmente (sin commit de merge) | Para mantener el historial limpio |

> [!TIP] Tras el merge, GitHub te ofrece borrar la rama automáticamente. ¡Hazlo para mantener el repo limpio!

---

## ▶️ 4. Pestaña ACTIONS (Automatización y CI/CD)

**¿Qué es?** El sistema de automatización de GitHub. Permite ejecutar tareas automáticamente (tests, despliegues, notificaciones) cuando ocurre un evento en el repositorio.

**Conceptos clave:**

| Término | Qué es |
| :--- | :--- |
| **Workflow** | Un proceso automatizado definido en un archivo `.yml` dentro de `.github/workflows/` |
| **Trigger (on)** | El evento que dispara el workflow (push, pull_request, schedule...) |
| **Job** | Un conjunto de pasos que se ejecutan en una máquina virtual |
| **Step** | Una tarea individual dentro de un job (un comando o una Action) |
| **Action** | Una pieza de código reutilizable del Marketplace de GitHub |
| **Runner** | La máquina virtual donde se ejecutan los jobs |

### Estructura básica de un Workflow

```yaml
# .github/workflows/mi-workflow.yml
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4          # Descarga el código
      - name: Instalar dependencias
        run: npm install
      - name: Ejecutar tests
        run: npm test
```

### Ver los resultados en la pestaña Actions

1. Haz clic en cualquier ejecución de un workflow.
2. Verás los **jobs** con iconos de ✅ (éxito), ❌ (fallo) o 🟡 (en progreso).
3. Haz clic en un job para ver el log detallado paso a paso.

---

## 📋 5. Pestaña PROJECTS (Gestión de Proyectos)

**¿Qué es?** Tableros de gestión visual (como Trello o Jira) que agrupan Issues y PRs.

**Tipos de vista:**

| Vista | Descripción |
| :--- | :--- |
| **Board (Kanban)** | Columnas drag-and-drop (To Do / In Progress / Done) |
| **Table** | Vista en hoja de cálculo con campos personalizados |
| **Roadmap** | Vista temporal (línea del tiempo / Gantt) |

**Crear un Project:**
1. Ve a la pestaña **Projects** del repositorio o de tu perfil.
2. Clic en **New project**.
3. Elige plantilla o empieza vacío.
4. Añade Issues y PRs arrastrándolos o usando el campo `+`.

---

## 📖 6. Pestaña WIKI (Documentación Extendida)

**¿Qué es?** Un espacio de documentación separado del código, ideal para guías de usuario, arquitectura del sistema, FAQs, etc.

**¿Cuándo usarlo?** Cuando el README.md se queda pequeño.

**Crear una página de Wiki:**
1. Ve a **Wiki** → **Create the first page** (si es nuevo).
2. Escribe en Markdown.
3. Clic en **Save Page**.
4. Puedes crear más páginas desde **New Page** y enlazarlas entre sí.

> [!TIP] La Wiki también es un repositorio Git. Puedes clonarla y editarla localmente con tu editor habitual.

---

## 🔒 7. Pestaña SECURITY (Seguridad del Repositorio)

**¿Qué es?** Centro de control de seguridad del repositorio. Aquí se configura y visualiza todo lo relacionado con vulnerabilidades.

| Sección | Qué hace |
| :--- | :--- |
| **Security Policy** | Muestra el archivo `SECURITY.md` (instrucciones para reportar vulnerabilidades responsablemente) |
| **Security Advisories** | Publica avisos de vulnerabilidades de forma coordinada (sin revelar antes de tener el fix) |
| **Dependabot alerts** | Notificaciones automáticas cuando una dependencia tuya tiene una vulnerabilidad conocida (CVE) |
| **Dependabot security updates** | PRs automáticos que actualizan la dependencia vulnerable |
| **Code Scanning** | Análisis estático del código (SAST) con CodeQL para detectar bugs de seguridad |
| **Secret Scanning** | Detecta si accidentalmente has subido credenciales, API keys o tokens al repositorio |

---

## 💡 8. Pestaña INSIGHTS (Métricas y Estadísticas)

**¿Qué es?** Estadísticas de actividad del repositorio. Muy útil para gestores y contribuidores.

| Sección | Qué muestra |
| :--- | :--- |
| **Pulse** | Actividad reciente (PRs abiertos/cerrados, Issues, commits) |
| **Contributors** | Gráfico de contribuciones por autor a lo largo del tiempo |
| **Community Standards** | Checklist de salud del proyecto (README, LICENSE, CONTRIBUTING...) |
| **Traffic** | Visitas al repo, clones, páginas más vistas |
| **Network** | Visualización gráfica de los forks y sus ramas |
| **Forks** | Lista de todos los forks del repositorio |
| **Dependency graph** | Mapa de dependencias del proyecto |

---

## ⚙️ 9. Pestaña SETTINGS (Configuración del Repositorio)

**¿Qué es?** El panel de administración del repositorio. Solo lo ven los que tienen rol de Admin.

### Secciones Principales de Settings

#### General
- **Renombrar el repositorio**
- **Cambiar la visibilidad** (Public / Private / Internal)
- **Funcionalidades**: Activar/desactivar Issues, Projects, Wiki, Discussions, Sponsorships
- **Merge options**: Elegir qué tipos de merge están permitidos en los PRs
- **Archivar el repositorio** (solo lectura, no se puede borrar código)
- **Borrar el repositorio** (acción irreversible)

#### Collaborators & Teams
- Añadir personas directamente al repositorio
- Asignar roles: **Read**, **Triage**, **Write**, **Maintain**, **Admin**

#### Branches (Branch Protection Rules)
- Proteger ramas importantes (ej. `main`) para evitar pushes directos
- Configurar:
  - Requerir Pull Request antes de mergear
  - Requerir N aprobaciones de revisores
  - Requerir que pasen los CI checks (Actions)
  - Bloquear el historial reescrito (rebase/amend en commits subidos)
  - Requerir que la rama esté actualizada antes de mergear

#### Secrets and Variables
- **Secrets**: Variables cifradas (API keys, tokens) que los workflows de Actions usan pero que nadie puede leer
- **Variables**: Variables no secretas reutilizables en Actions

#### Webhooks
- Enviar notificaciones automáticas a URLs externas cuando ocurren eventos (push, PR, etc.)

#### GitHub Pages
- Activar la publicación del repositorio como página web estática
- Configurar la rama y carpeta de origen (`/root` o `/docs`)

---

## 🔄 Flujos de Trabajo Completos

### Flujo para Contribuir (GitHub Flow)

```
1. Sincronizar local          →  git pull origin main
2. Crear rama nueva           →  git switch -c feature/mi-funcionalidad
3. Hacer cambios y commits    →  git commit -am "Añade X"
4. Subir la rama              →  git push origin feature/mi-funcionalidad
5. Abrir Pull Request         →  GitHub UI → "Compare & pull request"
6. Pasar Code Review          →  Revisor aprueba o pide cambios
7. Hacer Merge                →  GitHub UI → "Merge pull request"
8. Borrar la rama             →  GitHub UI → "Delete branch"
9. Limpiar local              →  git switch main → git pull → git branch -d feature/mi-funcionalidad
```

### Flujo para Resolver un Bug Urgente (Hotfix)

```
1. Desde main                 →  git switch main && git pull
2. Rama de hotfix             →  git switch -c hotfix/login-crash
3. Corregir y commitear       →  git commit -am "Fix: login crash on mobile"
4. Subir y abrir PR urgente   →  git push origin hotfix/login-crash
5. Revisión rápida y Merge    →  GitHub UI
6. Etiquetar la versión       →  git tag -a v1.0.1 -m "Hotfix login" && git push --tags
```

### Flujo para Sincronizar un Fork

```
1. Añadir remoto upstream     →  git remote add upstream https://github.com/original/repo.git
2. Traer cambios del original →  git fetch upstream
3. Fusionar en tu local       →  git merge upstream/main
4. Subir a tu fork            →  git push origin main
```

---

## 📌 Atajos de Teclado en GitHub (Los más útiles)

| Atajo | Acción |
| :--- | :--- |
| `?` | Abre el menú de todos los atajos de teclado |
| `.` | Abre el repositorio en github.dev (VS Code en navegador) |
| `T` | Activa el buscador de archivos del repositorio |
| `L` | Salta a una línea específica en un archivo |
| `W` | Cambia entre ramas y tags |
| `S` / `/` | Activa la barra de búsqueda |
| `G + C` | Va a la pestaña Code |
| `G + I` | Va a la pestaña Issues |
| `G + P` | Va a la pestaña Pull Requests |
| `G + A` | Va a la pestaña Actions |
