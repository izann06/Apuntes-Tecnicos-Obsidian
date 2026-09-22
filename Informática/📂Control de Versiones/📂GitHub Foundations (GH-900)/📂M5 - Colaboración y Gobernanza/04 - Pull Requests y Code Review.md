#github #gh-foundations #modulo-5 #pull-requests #code-review #draft-pr

> [!info] Navegación
> ◀ [[03 - Fork vs Clone y Sincronización]] · ▶ [[05 - Branch Protection e InnerSource]]

---

# 04 — Pull Requests y Code Review

> **Resumen ejecutivo:**
> 1. Un **PR** es una propuesta formal para fusionar cambios de una rama a otra. Tiene ramas *base* y *compare*.
> 2. Los **Draft PRs** comunican "trabajo en progreso" sin pedir revisión.
> 3. Las revisiones pueden ser: **Comment**, **Approve** o **Request Changes**, con sugerencias de código directas.

---

## 1. Anatomía de un Pull Request

| Concepto | Descripción |
| :--- | :--- |
| **Base branch** | La rama de destino (normalmente `main`). Donde quieres fusionar. |
| **Compare branch** | La rama con tus cambios (ej. `feature/login`). Lo que quieres fusionar. |

### Pestañas de un PR

| Pestaña | Contenido |
| :--- | :--- |
| **Conversation** | Comentarios generales, historial de revisiones, actividad |
| **Commits** | Lista de todos los commits incluidos en el PR |
| **Checks** | Resultados de CI/CD (GitHub Actions, tests automáticos) |
| **Files changed** | Diff completo de todos los archivos modificados |

---

## 2. Crear un Pull Request (Normal o Borrador)

### Desde GitHub Web

1. Haz push de tu rama a GitHub.
2. GitHub muestra un banner verde: **"Compare & pull request"**. Haz clic.
3. Rellena título, descripción, y opcionalmente asigna reviewers o labels.
4. **¿Normal o Borrador?**
   - **Para un PR Normal:** Haz clic en el botón verde gigante **"Create pull request"**.
   - **Para un Draft PR:** Haz clic en la **flechita hacia abajo** que hay justo a la derecha de ese botón verde. Se abrirá un menú. Elige **"Create draft pull request"** y luego dale al botón.

### Desde la terminal (GitHub CLI)

```bash
# Para crear un PR normal:
gh pr create --title "Añade login" --body "Implementa autenticación JWT" --base main

# Para crear un Draft PR (borrador), simplemente añade el flag --draft:
gh pr create --draft --title "Añade login" --body "Implementa autenticación JWT" --base main
```

---

## 3. Draft Pull Requests (Borradores)

Imagina que estás escribiendo un libro. Llevas solo 3 capítulos y sabes que tienen faltas de ortografía, pero quieres enseñarle el esquema a tu editor para saber si vas por buen camino. Sin embargo, **no quieres que lo mande a la imprenta todavía bajo ningún concepto**.

Eso es un **Draft PR** (Pull Request en Borrador). Es una forma de decirle a tu equipo: *"Eh, mirad en lo que estoy trabajando. Podéis echarle un ojo y darme ideas, pero todavía no he terminado, así que no lo fusionéis"*.

**Características principales:**

- **Es inofensivo:** El botón verde de "Merge" está bloqueado. Es literalmente imposible que alguien lo fusione por accidente con el código principal.
- **No molesta:** No manda notificaciones urgentes a tus compañeros pidiendo que revisen tu código. Hasta que no pulses el botón "Ready for review" (Listo para revisión), se entiende que sigues trabajando en ello.

**¿Para qué se usa en la vida real?**

1. **Feedback temprano:** *"Chicos, he empezado a hacer la nueva pantalla de Login. Mirad el código que llevo. ¿Os gusta esta estructura antes de que me tire 4 horas terminándolo?"*
2. **Aprovechar los robots (CI):** A veces quieres subir tu código a medias solo para que los tests automáticos de GitHub comprueben si compila bien, sin pedir a ningún humano que lo mire todavía.
3. **Visibilidad:** Dejar constancia pública de que tú te estás encargando de esa tarea para que otro compañero no empiece a hacer lo mismo sin darse cuenta.

> [!TIP] Exam Tip — Assignee vs Reviewer
> - **Assignee:** La persona **responsable de completar** el trabajo del PR (normalmente el autor). Puede haber hasta 10.
> - **Reviewer:** La persona que **revisa el código** y aprueba o pide cambios. Es solicitada por el autor o automáticamente por `CODEOWNERS`.

---

## 4. Proceso de Code Review

### Estados de revisión

| Estado | Significado | ¿El PR se puede fusionar? |
| :--- | :--- | :---: |
| **Comment** | El revisor deja comentarios sin aprobar ni rechazar | Depende de las reglas |
| **Approve** | El revisor aprueba los cambios | ✅ Si cumple los requisitos |
| **Request Changes** | El revisor rechaza hasta que se corrijan los problemas | ❌ No, hasta que apruebe |

### Sugerencias de Código (Suggested Changes)

El revisor puede proponer cambios directamente en el diff, y el autor puede aceptarlos con un clic ("Apply suggestion"). Git crea un commit automáticamente.

```suggestion
const MAX_RETRIES = 5; // Mejor usar una constante
```

### Comentar en líneas específicas

En la pestaña "Files changed", puedes hacer clic en el número de línea para abrir un cuadro de comentario contextual. Puedes seleccionar un rango de líneas para comentar sobre un bloque completo.

---

## 5. Estados de un Pull Request

| Estado | Descripción |
| :--- | :--- |
| **Open (Draft)** | Borrador. Trabajo en progreso. |
| **Open (Ready)** | Listo para revisión y fusión. |
| **Merged** | Fusionado con la rama base. **Irreversible.** |
| **Closed** | Cerrado sin fusionar (descartado). Se puede reabrir. |

---

## 6. Estrategias de Merge en un PR (Cómo juntar el código)

Cuando tu Pull Request está aprobado y vas a pulsar el botón verde para fusionarlo con la rama `main`, GitHub te ofrece 3 opciones de cómo quieres que se unan.

Imagina que mientras trabajabas en tu rama, hiciste estos 3 commits:

1. `"Crea la pantalla de login"`
2. `"Arregla un bug en el botón"`
3. `"Oops, se me olvidó un punto y coma"`

¿Cómo quieres que se vean estos cambios cuando lleguen a la rama principal (`main`)?

### 1. Create a merge commit (El tradicional)

- **Qué hace:** Coge tus 3 commits y los mete **tal cual** en la rama `main`. Además, añade un 4º commit automático que sirve como pegamento: *"Merge branch feature/login"*.
  
- **Resultado:** Se conserva la historia exacta. Se ve la bifurcación de tu rama y cómo vuelve a unirse.
  
- **El problema:** Si tienes a 10 personas trabajando a la vez, el historial gráfico de Git se vuelve una tela de araña ilegible llena de commits basura como el del "punto y coma".

### 2. Squash and merge (La "Aplastadora")

- **Qué hace:** Coge tus 3 commits, los "aplasta" (*squash*) y los fusiona creando **un solo commit nuevo y limpio**.
  
- **Resultado en main:** En la rama principal solo aparecerá 1 commit (ej. *"Añade funcionalidad de Login completa"*). Nadie verá que te equivocaste con el punto y coma.
  
- **Cuándo usarlo:** Es la opción favorita en el 90% de las empresas hoy en día. Mantiene el historial de la rama `main` impoluto: cada commit es una funcionalidad entera terminada, sin ruido.

> [!WARNING] Pregunta frecuente de examen
> Si el examen pregunta cuál es la estrategia de merge que **combina todos los commits en uno solo**, la respuesta es **Squash and merge**. Es útil cuando un PR tiene muchos minicommits y quieres un historial limpio.

### 3. Rebase and merge (El perfeccionista lineal)

- **Qué hace:** Coge tus 3 commits originales y los recorta y pega justo en la punta de `main`, pero **sin crear el commit de pegamento (merge commit)**.
  
- **Resultado en main:** Aparecerán tus 3 commits originales, pero dibujando una línea completamente recta, como si nunca te hubieras ido a una rama paralela.
  
- **Cuándo usarlo:** Cuando el equipo odia la "tela de araña" pero quiere conservar absolutamente todos los pasos intermedios de los programadores.

---

## 7. Referenciar Contenido en un PR

```
#42          → Issue o PR número 42
@izanm       → Mencionar a un usuario
@my-org/team → Mencionar a un equipo
SHA-hash     → Referencia a un commit específico
```
