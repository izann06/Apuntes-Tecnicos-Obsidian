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

## 2. Crear un Pull Request

### Desde GitHub Web

1. Haz push de tu rama a GitHub.
2. GitHub muestra un banner: **"Compare & pull request"**. Haz clic.
3. Rellena título, descripción, asigna reviewers, labels.
4. Clic en **"Create pull request"**.

### Desde la terminal (GitHub CLI)

```bash
gh pr create --title "Añade login" --body "Implementa autenticación JWT" --base main

# Salida esperada:
# Creating pull request for feature/login into main in izanm/mi-proyecto
# https://github.com/izanm/mi-proyecto/pull/5
```

---

## 3. Draft Pull Requests (Borradores)

Un **Draft PR** indica que el trabajo **no está listo para revisión**. No se puede fusionar hasta que lo marques como "Ready for review".

**Casos de uso:**

- Compartir trabajo en progreso para recibir feedback temprano.
- Ejecutar los checks de CI para validar que tu código compila.
- Comunicar al equipo en qué estás trabajando.

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

## 6. Estrategias de Merge en un PR

Al fusionar un PR, GitHub ofrece 3 opciones:

| Estrategia | ¿Qué hace? | Historial |
| :--- | :--- | :--- |
| **Create a merge commit** | Crea un commit de merge que une ambas ramas | Conserva toda la historia |
| **Squash and merge** | Aplasta todos los commits del PR en uno solo | Historial limpio |
| **Rebase and merge** | Reaplica los commits del PR sobre la rama base | Historial lineal sin merge commit |

> [!WARNING] Pregunta frecuente de examen
> Si el examen pregunta cuál es la estrategia de merge que **combina todos los commits en uno solo**, la respuesta es **Squash and merge**. Es útil cuando un PR tiene muchos commits pequeños ("fix typo", "oops", "ahora sí funciona") y quieres un historial limpio.

---

## 7. Referenciar Contenido en un PR

```
#42          → Issue o PR número 42
@izanm       → Mencionar a un usuario
@my-org/team → Mencionar a un equipo
SHA-hash     → Referencia a un commit específico
```
