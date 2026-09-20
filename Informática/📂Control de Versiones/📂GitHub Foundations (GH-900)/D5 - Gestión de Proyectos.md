#github #projects #gestion #gh-foundations

> [!info] Navegación
> ◀ [[D4 - Desarrollo Moderno (Actions, Copilot, Codespaces)]] · ▶ [[D6 - Seguridad y Administración]]

---

# Dominio 5 — Gestión de Proyectos

## 5.1 GitHub Projects

**GitHub Projects** es la herramienta de gestión de proyectos integrada en GitHub. Permite planificar y hacer seguimiento del trabajo usando vistas personalizadas y automatizaciones.

### Vistas (Layouts) Disponibles

| Vista | Descripción |
| :--- | :--- |
| **Table (Tabla)** | Hoja de cálculo para ver y editar campos de todos los items a la vez |
| **Board (Tablero)** | Estilo Kanban. Columnas con cards que representan issues/PRs |
| **Roadmap** | Vista de línea de tiempo para planificar sprints y releases |

### Configuración de Proyectos

- **Custom Fields:** Puedes añadir campos personalizados a los items (fecha, texto, número, selección, iteración).
- **Automatizaciones:** Reglas que mueven automáticamente los items (ej. "Cuando un PR se fusiona → mover a Done").
- **Insights:** Gráficas de quemado (burnup/burndown) para seguir el progreso.

### Projects vs. Projects Classic

| | **Projects (nuevo)** | **Projects Classic** |
| :--- | :--- | :--- |
| **Vistas** | Tabla, Tablero, Roadmap | Solo Tablero Kanban |
| **Campos personalizados** | ✅ Sí | ❌ No |
| **Automatizaciones** | ✅ Avanzadas | ⚠️ Básicas |
| **Vinculación** | Repositorios cruzados | Dentro del mismo repo/org |

---

## 5.2 Labels (Etiquetas)

Las **Labels** son etiquetas de color que se aplican a Issues y Pull Requests para categorizarlos.

GitHub crea etiquetas predeterminadas en cada repositorio: `bug`, `documentation`, `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, `wontfix`.

> [!tip] `good first issue` y `help wanted`
> Estas dos etiquetas son especialmente importantes para proyectos Open Source. La etiqueta `good first issue` aparece en el explorador de GitHub para atraer nuevos colaboradores que buscan por dónde empezar.

**Acciones con Labels:**

- Crear, editar y borrar desde `Issues > Labels`.
- Aplicar múltiples etiquetas a un mismo issue/PR.
- Filtrar issues/PRs por etiqueta.

---

## 5.3 Milestones (Hitos)

Un **Milestone** es un contenedor que agrupa un conjunto de issues y pull requests para representar una meta o versión del proyecto.

- Tiene una **fecha límite** opcional.
- Muestra una **barra de progreso** en base a los issues cerrados vs. abiertos dentro de él.
- Ejemplo: `v1.0.0 - Lanzamiento inicial`, `Sprint 3 - Septiembre`.

---

## 5.4 Plantillas de Issues y PRs

### Issue Templates

Archivos `.md` ubicados en `.github/ISSUE_TEMPLATE/` que predefinen la estructura del issue para facilitar que los colaboradores reporten bugs o pidan features con la información necesaria.

### Pull Request Templates

Un archivo `.github/PULL_REQUEST_TEMPLATE.md` que se carga automáticamente como descripción inicial al abrir un nuevo PR. Ideal para incluir una checklist de revisión estándar.

---

## 5.5 Saved Replies (Respuestas Guardadas)

Las **Saved Replies** son plantillas de texto que puedes guardar en tu cuenta de GitHub y reutilizar en cualquier comentario con el atajo `⌘.` (Mac) o `Ctrl+.` (Windows).

- **Crear:** `Settings > Saved replies > New saved reply`.
- **Usar:** En cualquier caja de comentario, haz clic en el ícono de flechas o usa el atajo de teclado.
- **Beneficio:** Estandarizar respuestas frecuentes como "Gracias por tu contribución, lo revisaré esta semana" o "Este issue ya ha sido reportado en #123".

---

## 5.6 Workflows de Proyectos e Insights

### Workflows

Los Projects tienen **automatizaciones integradas (Workflows)** que se pueden activar:

- **Auto-add to project:** Añade automáticamente los issues/PRs nuevos del repo al proyecto.
- **Item closed:** Cuando se cierra un issue/PR, moverlo a una columna específica.
- **Pull request merged:** Al fusionarse un PR, marcarlo como Done.

### Project Insights

La pestaña **Insights** de un proyecto genera gráficas automáticas:

- **Burn up chart:** Cuánto trabajo se ha completado vs. el total.
- **Burn down chart:** Cuánto trabajo queda por hacer en el tiempo.
- Permiten detectar si el equipo va a tiempo o si el sprint está en riesgo.

---

## 5.7 Assignees

Los **Assignees** son los usuarios asignados como responsables de resolver un issue o revisar un PR.

- Se pueden asignar hasta **10 personas** a un issue/PR.
- Se pueden asignar desde el panel lateral al crear o editar el issue/PR.
- Útil para que quede claro quién es responsable de cada tarea.
