#git #gh-foundations #modulo-2 #merge #conflictos

> [!info] Navegación
> ◀ [[01 - Gestión de Ramas (Branching)]] · ▶ [[03 - Flujos Avanzados (Rebase, Cherry-pick, Flows)]]

---

# 02 — Fusión y Resolución de Conflictos

> **Resumen ejecutivo:**
> 1. `git merge` fusiona una rama en otra. Hay dos estrategias: **Fast-Forward** (sin commit nuevo) y **3-Way Merge** (con commit de merge).
> 2. Los conflictos ocurren cuando ambas ramas modifican las mismas líneas. Se resuelven manualmente editando los marcadores `<<<<<<<`.
> 3. `git merge --abort` cancela una fusión en conflicto y vuelve al estado anterior.

---

## 1. Concepto de Merge

Fusionar (*merge*) significa integrar los cambios de una rama (**source/origen**) en otra (**destination/destino**).

```bash
# Paso 1: Cambia a la rama destino (normalmente main)
git switch main

# Paso 2: Fusiona la rama origen
git merge feature/login

# Salida esperada:
# Updating 9f8e7d6..a1b2c3d
# Fast-forward
#  login.html | 10 ++++++++++
#  1 file changed, 10 insertions(+)
```

---

## 2. Estrategias de Fusión

### Fast-Forward (Avance Rápido)

Ocurre cuando la rama destino (`main`) **no tiene commits nuevos** desde que se creó la rama origen. Git simplemente "avanza" el puntero de `main`:

```
ANTES:
main:     A --- B
                 \
feature:          C --- D     (HEAD → feature)

DESPUÉS (Fast-Forward):
main:     A --- B --- C --- D     (HEAD → main)
```

No se crea un commit de merge. El historial queda lineal y limpio.

### 3-Way Merge (Merge Commit)

Ocurre cuando **ambas ramas tienen commits nuevos** que divergen. Git crea un **commit de merge** que une ambas líneas:

```
ANTES:
main:     A --- B --- E
                 \
feature:          C --- D

DESPUÉS (3-Way Merge):
main:     A --- B --- E --- M     (M = merge commit)
                 \         /
feature:          C --- D
```

```bash
# Salida esperada de un 3-way merge:
# Merge made by the 'ort' strategy.
#  login.html | 10 ++++++++++
#  styles.css |  5 +++++
#  2 files changed, 15 insertions(+)
```

| Estrategia | ¿Cuándo ocurre? | ¿Crea commit de merge? | Historial |
| :--- | :--- | :---: | :--- |
| **Fast-Forward** | `main` no tiene commits nuevos | ❌ No | Lineal y limpio |
| **3-Way Merge** | Ambas ramas tienen commits nuevos | ✅ Sí | Muestra bifurcación |

---

## 3. Conflictos de Fusión

Los conflictos ocurren cuando **ambas ramas han modificado las mismas líneas** del mismo archivo. Git no puede decidir automáticamente cuál versión conservar.

### Marcadores de conflicto

Al intentar el merge, Git marca los archivos conflictivos con esta estructura:

```
<<<<<<< HEAD
<p>Versión en main: Precio 10€</p>
=======
<p>Versión en feature: Precio 15€</p>
>>>>>>> feature/precios
```

| Marcador | Significado |
| :--- | :--- |
| `<<<<<<< HEAD` | Inicio del bloque con **tu versión** (la rama actual, destino) |
| `=======` | Separador entre ambas versiones |
| `>>>>>>> feature/precios` | Fin del bloque con la **versión de la otra rama** (origen) |

### Flujo de resolución manual

```bash
# 1. Intenta el merge
git merge feature/precios

# Salida esperada (conflicto):
# Auto-merging index.html
# CONFLICT (content): Merge conflict in index.html
# Automatic merge failed; fix conflicts and then commit the result.
```

```bash
# 2. Abre el archivo conflictivo y edita manualmente.
#    Elige la versión correcta y borra los marcadores:

# ANTES (conflicto):
<<<<<<< HEAD
<p>Precio 10€</p>
=======
<p>Precio 15€</p>
>>>>>>> feature/precios

# DESPUÉS (resuelto):
<p>Precio 15€</p>
```

```bash
# 3. Marca el conflicto como resuelto
git add index.html

# 4. Completa el merge
git commit
# (Git abrirá el editor con un mensaje de merge predeterminado)

# Alternativa:
git merge --continue
```

### Cancelar un merge en conflicto

Si te agobias o quieres empezar de cero:

```bash
git merge --abort

# Salida: Git vuelve al estado exacto anterior al intento de merge.
```

> [!IMPORTANT] Exam Tip — Resolución de conflictos
> El examen puede preguntar cuál es el flujo correcto para resolver un conflicto:
> 1. Editar el archivo eliminando los marcadores `<<<<<<<`, `=======`, `>>>>>>>`
> 2. `git add <archivo>` para marcar como resuelto
> 3. `git commit` o `git merge --continue` para finalizar
