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

Imagina que tienes un proyecto público y alguien te abre un issue diciendo simplemente: *"El botón no funciona, arregladlo"*. 
No te dicen qué botón, en qué navegador, ni cómo reproducirlo. Para evitar este caos y perder el tiempo preguntando, GitHub permite crear "plantillas" para guiar (u obligar) al usuario a dar la información correcta desde el primer momento.

Hay dos formas de hacer esto. Ambas se guardan en la carpeta oculta `.github/ISSUE_TEMPLATE/` de tu repositorio:

### 📄 Issue Templates (El método clásico y flexible)

Son simples archivos de texto en formato **Markdown** (`.md`).

- **Cómo funciona:** Cuando el usuario va a crear un issue, el cuadro de texto ya le aparece pre-rellenado con un esqueleto (ej: apartados de "Pasos para reproducir", "Comportamiento esperado", etc.).
  
- **El problema (Caso de uso):** Como es solo texto libre en una caja grande, el usuario perezoso puede pulsar `Ctrl+A` (seleccionar todo), borrar tu preciosa plantilla y escribir *"El botón no funciona"* ignorando tus reglas por completo.
  
- **Formato:** Archivos `.md`.

```markdown
<!-- Ejemplo de Issue Template (.md) -->
---
name: Bug Report
about: Reporta un error
labels: bug
---

## Descripción del bug
<!-- Describe claramente el problema aquí -->

## Pasos para reproducir
1. Ve a '...'
2. Haz clic en '....'
```

### 📋 Issue Forms (El método moderno y estricto)

Son verdaderos **formularios interactivos** creados mediante código **YAML** (`.yml`). 

- **Cómo funciona:** En lugar de darle al usuario una caja de texto gigante, le presentas un formulario de web real: cajas de texto separadas, menús desplegables (dropdowns) y casillas de verificación (checkboxes)

- **La gran ventaja (Caso de uso):** Puedes marcar campos como **obligatorios** (`required: true`). El usuario **NO PUEDE** saltárselos ni borrar la estructura. Si pones un desplegable para que elija su navegador y lo marcas como obligatorio, no podrá enviar el issue si no lo selecciona. Es perfecto para equipos profesionales.
  
- **Formato:** Archivos `.yml`.

```yaml
# Ejemplo de Issue Form (.yml)
name: Bug Report
description: Reporta un error en la aplicación
labels: [bug]
body:
  - type: textarea
    attributes:
      label: Descripción detallada
    validations:
      required: true  # ¡Obligatorio, no puede borrarlo!
  - type: dropdown
    attributes:
      label: ¿Qué navegador usas?
      options:
        - Chrome
        - Firefox
        - Safari
```

> [!TIP] Exam Tip — Diferencia Clave para el Examen
> Si te preguntan en el examen por la diferencia principal:
> - **Templates (`.md`)** = Markdown libre. El usuario puede saltarse las normas y borrar el texto.
> - **Forms (`.yml`)** = Formulario estructurado. Soporta menús desplegables, checkboxes y lo más importante: **campos obligatorios**. Son mucho más estrictos.

---

## 6. Crear una Rama desde un Issue

Dentro de un issue, en el panel derecho, hay la opción **"Create a branch"**. Esto crea una rama automáticamente con un nombre vinculado al issue (ej. `42-fix-login-bug`), facilitando el seguimiento.

---

## 7. Fijar Issues (Pin)

Los issues más importantes se pueden **fijar** en la parte superior de la lista. Admite hasta **3 issues fijados** por repositorio.
