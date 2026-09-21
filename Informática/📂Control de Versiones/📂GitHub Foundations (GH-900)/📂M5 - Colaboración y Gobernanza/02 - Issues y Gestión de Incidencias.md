#github #gh-foundations #modulo-5 #issues #labels #milestones #templates

> [!info] Navegación
> ◀ [[01 - Repositorios y Documentación]] · ▶ [[03 - Fork vs Clone y Sincronización]]

---

# 02 — Issues y Gestión de Incidencias

> **Resumen ejecutivo:**
> 1. Los **Issues** son el sistema de tickets de GitHub: bugs, tareas, propuestas.
> 2. Se organizan con **Labels** (etiquetas), **Assignees** (responsables), **Milestones** (hitos).
> 3. Puedes cerrar issues automáticamente desde commits o PRs con keywords como `fixes #42`.

---

## 1. Crear y Gestionar Issues

Un **Issue** se crea desde la pestaña `Issues > New issue`. Incluye:

- **Título y descripción** (en Markdown).
- **Assignees:** Personas responsables de resolverlo (hasta 10).
- **Labels:** Etiquetas de color para categorizar.
- **Milestone:** Hito al que pertenece (ej. "Sprint 3", "v2.0").
- **Projects:** Proyecto de gestión al que se asocia.

### Diferencias: Issue vs. Discussion vs. Pull Request

| | Issue | Discussion | Pull Request |
| :--- | :--- | :--- | :--- |
| **¿Para qué?** | Bugs, tareas, peticiones concretas | Conversaciones abiertas, Q&A, ideas | Proponer cambios de código |
| **¿Tiene código adjunto?** | No necesariamente | No | Sí (siempre) |
| **¿Se puede cerrar/resolver?** | ✅ Sí | Se marca respuesta (Q&A) | ✅ Se fusiona o se rechaza |
| **¿Se puede convertir?** | — | ✅ Discussion → Issue | — |

---

## 2. Labels (Etiquetas)

Las **Labels** son etiquetas de color que categorizan issues y PRs.

**Labels por defecto en cada repositorio nuevo:**

| Label | Color | Uso |
| :--- | :--- | :--- |
| `bug` | 🔴 Rojo | Error en el código |
| `enhancement` | 🔵 Azul | Petición de nueva funcionalidad |
| `documentation` | 🟣 Morado | Mejora de documentación |
| `good first issue` | 🟢 Verde | Ideal para nuevos contribuidores |
| `help wanted` | 🟡 Amarillo | Se busca ayuda de la comunidad |
| `duplicate` | ⚪ Gris | Issue duplicado |
| `wontfix` | ⚪ Gris | No se va a solucionar |

> [!TIP] `good first issue` y `help wanted`
> Estas dos etiquetas aparecen en los exploradores de GitHub para atraer nuevos contribuidores a proyectos Open Source. Si mantienes un proyecto OSS, úsalas estratégicamente.

---

## 3. Milestones (Hitos)

Un **Milestone** agrupa issues y PRs bajo una meta común con fecha límite opcional.

- Muestra una **barra de progreso** (issues cerrados / total).
- Ejemplo: `v1.0.0 - Lanzamiento inicial` con fecha límite 30 de octubre.
- Se crean en `Issues > Milestones > New milestone`.

---

## 4. Keywords para Cerrar Issues Automáticamente

Al hacer un commit o fusionar un PR, si incluyes estas keywords seguidas del número de issue, GitHub lo cierra automáticamente:

| Keyword | Ejemplo | Efecto |
| :--- | :--- | :--- |
| `fixes` | `fixes #42` | Cierra el issue #42 al fusionar |
| `closes` | `closes #42` | Cierra el issue #42 al fusionar |
| `resolves` | `resolves #42` | Cierra el issue #42 al fusionar |

```bash
# En un mensaje de commit:
git commit -m "Corrige la validación del email. Fixes #42"

# En la descripción de un PR:
# "Este PR corrige el bug de login. Closes #42"
```

> [!IMPORTANT] Las keywords solo funcionan en la rama por defecto
> Si el commit o PR se fusiona en `main` (la rama por defecto), el issue se cierra automáticamente. Si se fusiona en otra rama, el issue NO se cierra.

---

## 5. Issue Templates vs. Issue Forms

### Issue Templates (Markdown)

Archivos `.md` en `.github/ISSUE_TEMPLATE/` que prerellenan el cuerpo del issue:

```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Bug Report
about: Reporta un error
labels: bug
---

## Descripción del bug
<!-- Describe claramente el problema -->

## Pasos para reproducir
1. 
2. 
3. 

## Comportamiento esperado
<!-- ¿Qué debería pasar? -->

## Capturas de pantalla
<!-- Si aplica -->
```

### Issue Forms (YAML — Más estructurados)

Formularios con campos controlados (dropdowns, checkboxes, campos obligatorios):

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: Reporta un error
labels: [bug]
body:
  - type: textarea
    attributes:
      label: Descripción
    validations:
      required: true
  - type: dropdown
    attributes:
      label: Severidad
      options:
        - Crítica
        - Alta
        - Media
        - Baja
```

> [!TIP] Exam Tip — Templates vs Forms
> **Templates** = Markdown libre. El usuario puede borrar o modificar la estructura.
> **Forms** = YAML con campos controlados. El usuario rellena un formulario y no puede saltarse campos obligatorios. Son más nuevos y más estrictos.

---

## 6. Crear una Rama desde un Issue

Dentro de un issue, en el panel derecho, hay la opción **"Create a branch"**. Esto crea una rama automáticamente con un nombre vinculado al issue (ej. `42-fix-login-bug`), facilitando el seguimiento.

---

## 7. Fijar Issues (Pin)

Los issues más importantes se pueden **fijar** en la parte superior de la lista. Admite hasta **3 issues fijados** por repositorio.
