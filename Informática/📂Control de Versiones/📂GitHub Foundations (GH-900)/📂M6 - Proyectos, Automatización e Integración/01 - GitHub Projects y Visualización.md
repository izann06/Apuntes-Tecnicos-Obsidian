#github #gh-foundations #modulo-6 #projects #kanban #roadmap

> [!info] Navegación
> ◀ [[05 - Branch Protection e InnerSource]] · ▶ [[02 - GitHub Actions (CI-CD)]]

---

# 01 — GitHub Projects y Visualización

> **Resumen ejecutivo:**
> 1. **GitHub Projects** es la herramienta de gestión de proyectos integrada. Tiene vistas Table, Board y Roadmap.
> 2. Projects (nuevo) es más flexible que Projects Classic: campos personalizados, múltiples vistas, automatizaciones.
> 3. Los **Insights** generan gráficas de progreso (burn up/down) para seguir el avance del sprint.

---

## 1. GitHub Projects vs. Projects Classic

| Característica | **Projects (nuevo)** | **Projects Classic** |
| :--- | :--- | :--- |
| **Vistas** | Table, Board, Roadmap | Solo Board (Kanban) |
| **Campos personalizados** | ✅ Texto, número, fecha, selección, iteración | ❌ No |
| **Automatizaciones** | ✅ Avanzadas (Built-in + Actions) | ⚠️ Básicas |
| **Ámbito** | A nivel de usuario u organización (cross-repo) | Vinculado a un repo |
| **Filtros y agrupaciones** | ✅ Avanzados | ⚠️ Básicos |
| **Insights (gráficas)** | ✅ Burn up / Burn down | ❌ No |

> [!WARNING] Pregunta frecuente de examen
> El examen puede preguntar la diferencia entre Projects y Projects Classic. La clave: **Projects** es la versión moderna, independiente del repositorio y con campos personalizados. **Classic** está atado a un repo y solo tiene tablero Kanban.

---

## 2. Vistas (Layouts)

### Table (Tabla)

Vista tipo hoja de cálculo. Permite ver y editar todos los campos de los items en una tabla.

- Ideal para **gestión masiva**: editar asignados, labels, fechas de muchos items a la vez.
- Soporta filtros, ordenación y agrupación por cualquier campo.

### Board (Tablero Kanban)

Vista de columnas tipo Trello/Jira. Los items se mueven entre columnas arrastrando.

- Columnas típicas: `Todo`, `In Progress`, `In Review`, `Done`.
- Ideal para visualizar el **flujo de trabajo** del equipo.

### Roadmap (Hoja de Ruta)

Vista de línea de tiempo tipo Gantt. Cada item tiene una fecha de inicio y fin.

- Ideal para **planificación de releases** y sprints a largo plazo.
- Requiere campos de fecha configurados en el proyecto.

---

## 3. Campos Personalizados

Puedes añadir campos a los items del proyecto:

| Tipo de campo | Ejemplo |
| :--- | :--- |
| **Text** | Notas, URLs, descripciones cortas |
| **Number** | Story Points, prioridad numérica |
| **Date** | Fecha de entrega |
| **Single Select** | Estado: `Todo` / `In Progress` / `Done` |
| **Iteration** | Sprint 1, Sprint 2... (con fechas de inicio y fin) |

---

## 4. Automatizaciones

### Built-in Automations

Automatizaciones predefinidas que se activan con un clic:

| Automatización | Efecto |
| :--- | :--- |
| **Auto-add to project** | Los issues/PRs nuevos del repo se añaden automáticamente al proyecto |
| **Item closed** | Cuando un issue se cierra → Mover a columna "Done" |
| **Pull request merged** | Cuando un PR se fusiona → Marcar como completado |
| **Item reopened** | Cuando se reabre un issue → Mover de vuelta a "Todo" |

### Automatización con GitHub Actions

Para lógica más compleja, se pueden crear workflows de Actions que actualicen el proyecto. Ejemplo: que tu código se suba a un servidor en el cloud.

---

## 5. Insights del Proyecto

La pestaña **Insights** genera gráficas automáticas:

| Gráfica | ¿Qué muestra? |
| :--- | :--- |
| **Burn up** | Cuánto trabajo se ha completado vs. el total a lo largo del tiempo |
| **Burn down** | Cuánto trabajo queda por hacer. Detecta si el sprint está en riesgo. |
| **Custom charts** | Gráficas personalizadas filtrando por campo, assignee, label, etc. |
