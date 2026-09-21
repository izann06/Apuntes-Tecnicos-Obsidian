#git #gh-foundations #modulo-2 #rebase #cherry-pick #github-flow #gitflow

> [!info] Navegación
> ◀ [[02 - Fusión y Resolución de Conflictos]] · ▶ [[01 - Ecosistema y Productos]]

---

# 03 — Flujos Avanzados (Rebase, Cherry-pick, Flows)

> **Resumen ejecutivo:**
> 1. `git rebase` reescribe el historial para hacerlo lineal. Es potente pero peligroso en repos compartidos.
> 2. `git cherry-pick` extrae un commit de una rama y lo aplica en otra quirúrgicamente.
> 3. **GitHub Flow** (simple, basado en PRs) vs **GitFlow** (complejo, con ramas `develop`, `release`, `hotfix`).

---

## 1. Rebase Interactivo (`git rebase`)

`git rebase` toma los commits de tu rama y los **reaplica** encima del último commit de otra rama, como si tu rama hubiese nacido más tarde. El resultado: un historial **lineal** sin commits de merge.

```
ANTES (dos ramas divergentes):
main:     A --- B --- E
                 \
feature:          C --- D

DESPUÉS de git rebase main (desde feature):
main:     A --- B --- E
                       \
feature:                C' --- D'   (commits re-creados sobre E)
```

```bash
# Desde la rama feature:
git switch feature/login
git rebase main

# Salida esperada:
# Successfully rebased and updated refs/heads/feature/login.
```

> [!WARNING] Regla de oro del Rebase
> **NUNCA hagas rebase de commits que ya hayas subido (`push`) a GitHub**. El rebase reescribe los hashes de los commits, lo que destruye el historial compartido y causa problemas graves a tus compañeros. Úsalo solo en ramas locales privadas.

| Operación | Historial | ¿Seguro en repos compartidos? | Uso ideal |
| :--- | :--- | :---: | :--- |
| `git merge` | No lineal (conserva la bifurcación) | ✅ Sí | Siempre seguro |
| `git rebase` | Lineal (limpio, sin bifurcaciones) | ❌ Solo en ramas locales | Limpiar historial antes de un PR |

---

## 2. Extracción Quirúrgica de Commits (`git cherry-pick`)

`git cherry-pick` copia un commit específico de cualquier rama y lo aplica en la rama actual, sin fusionar toda la rama.

```bash
# Desde main, aplica un commit específico de otra rama
git switch main
git cherry-pick e5f6g7h

# Salida esperada:
# [main 1a2b3c4] Fix critical bug in login
#  Date: Sun Sep 21 19:00:00 2026 +0200
#  1 file changed, 2 insertions(+), 2 deletions(-)
```

**Caso de uso real:** Un compañero ha corregido un bug crítico en la rama `feature/redesign` que aún no está lista para fusionar. Necesitas ese fix en `main` ahora. Haces `cherry-pick` solo de ese commit.

---

## 3. Flujos de Trabajo Organizacionales

### GitHub Flow (Recomendado para la mayoría de equipos)

Es el flujo que promueve [[GitHub]]. Es **simple y directo**:

```mermaid
graph LR
    A["1. Crea rama<br>desde main"] --> B["2. Haz commits<br>pequeños"]
    B --> C["3. Abre un<br>Pull Request"]
    C --> D["4. Code Review<br>y discusión"]
    D --> E["5. Merge a main"]
    E --> F["6. Despliega<br>desde main"]
```

**Reglas:**
- Solo existe la rama `main` como rama permanente.
- Para cada funcionalidad o fix, se crea una rama corta.
- Se abre un PR, se revisa, se fusiona y se borra la rama.

### GitFlow (Para proyectos con ciclos de release formales)

Es un flujo más complejo, ideal para software con versiones publicadas (apps móviles, etc.):

| Rama | Propósito | Permanente |
| :--- | :--- | :---: |
| `main` | Código en producción. Cada commit es una versión publicada. | ✅ |
| `develop` | Rama de integración donde se acumulan los cambios para la próxima versión. | ✅ |
| `feature/*` | Ramas de funcionalidad. Nacen de `develop`, se fusionan a `develop`. | ❌ |
| `release/*` | Preparación de una versión. Bug fixes de última hora antes de publicar. | ❌ |
| `hotfix/*` | Parches urgentes en producción. Nacen de `main`, se fusionan a `main` Y `develop`. | ❌ |

> [!TIP] Exam Tip — ¿Cuál pregunta el examen?
> El examen se centra en **GitHub Flow**, no en GitFlow. Debes saber los 6 pasos del GitHub Flow de memoria. GitFlow puede salir como comparación, pero no profundizan en él.
