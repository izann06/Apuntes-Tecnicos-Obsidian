#git #gh-foundations #modulo-1 #revert #reset #stash #reflog #tags

> [!info] Navegación
> ◀ [[03 - Historial y Comparación de Cambios]] · ▶ [[01 - Gestión de Ramas (Branching)]]

---

# 04 — Deshacer Cambios y Recuperación

> **Resumen ejecutivo:**
> 1. `git revert` deshace un commit creando uno nuevo (seguro para repos compartidos). `git reset` reescribe el historial (peligroso).
> 2. `git reflog` es la red de seguridad definitiva: registra TODOS los movimientos de HEAD, incluso tras un `reset --hard`.
> 3. `git stash` guarda temporalmente cambios sin commitear para cambiar de contexto rápidamente.

---

## 1. Restaurar Archivos en el Working Directory

Si has modificado un archivo y quieres **descartar esos cambios** (volver a la versión del último commit):

```bash
# Forma moderna (recomendada)
git restore app.js

# Forma clásica (equivalente)
git checkout -- app.js

# Salida: Git es silencioso. Confirma con git status:
# On branch main
# nothing to commit, working tree clean
```

> [!WARNING] `git restore` / `git checkout --` es destructivo
> Los cambios no commiteados que descartes con estos comandos **se pierden para siempre**. No hay undo. Asegúrate antes de ejecutarlo.

---

## 2. Revertir Confirmaciones (`git revert`)

`git revert` **no borra** el commit del historial. Crea un **nuevo commit** que deshace exactamente los cambios del commit indicado.

```bash
# Revertir el último commit
git revert HEAD

# Salida esperada:
# [main 7a8b9c0] Revert "Añade botón roto"
#  1 file changed, 0 insertions(+), 5 deletions(-)
```

```bash
# Revertir sin abrir el editor de texto (acepta el mensaje por defecto)
git revert HEAD --no-edit

# Aplicar la reversión en staging sin confirmar automáticamente
git revert HEAD -n
# (Útil para revisar los cambios antes de commitear tú mismo)
```

---

## 3. Reseteo del Historial (`git reset`)

`git reset` mueve el puntero HEAD hacia atrás, **reescribiendo el historial**. Tiene 3 modos:

| Modo | Comando | Working Directory | Staging Area | Historial |
| :--- | :--- | :---: | :---: | :---: |
| **`--soft`** | `git reset --soft HEAD~1` | ✅ Intacto | ✅ Conserva cambios | ❌ Borra commit |
| **`--mixed`** (por defecto) | `git reset HEAD~1` | ✅ Intacto | ❌ Desmarca cambios | ❌ Borra commit |
| **`--hard`** | `git reset --hard HEAD~1` | ❌ Borra cambios | ❌ Borra cambios | ❌ Borra commit |

```bash
# Ejemplo: Deshacer el último commit pero conservar los cambios en staging
git reset --soft HEAD~1

# Salida esperada (al hacer git status):
# Changes to be committed:
#   modified:   app.js
```

```bash
# Ejemplo: Deshacer el último commit y desmarcar los cambios
git reset HEAD~1

# Salida esperada:
# Unstaged changes after reset:
# M  app.js
```

```bash
# PELIGRO: Deshacer el último commit y BORRAR todo
git reset --hard HEAD~1

# Salida esperada:
# HEAD is now at 9f8e7d6 Configuración inicial
```

> [!IMPORTANT] Diferencia clave para el examen: `revert` vs `reset`
> - **`git revert`**: Crea un commit nuevo que deshace los cambios. El historial **crece**. ✅ Seguro para repos compartidos.
> - **`git reset`**: Borra commits del historial. El historial **retrocede**. ❌ Peligroso en repos compartidos (reescribe la historia de los compañeros).
> 
> **Regla de oro**: Si ya hiciste `git push`, usa `revert`. Si el commit solo existe en tu máquina local, puedes usar `reset`.

---

## 4. Red de Seguridad: `git reflog`

`git reflog` registra **absolutamente todos los movimientos de HEAD**: commits, resets, checkouts, merges, rebases... incluso los que un `git reset --hard` borró del historial visible.

```bash
git reflog

# Salida esperada:
# a1b2c3d (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
# 7a8b9c0 HEAD@{1}: commit: Añade botón roto
# 9f8e7d6 HEAD@{2}: commit: Configuración inicial
```

### Recuperar un commit "borrado"

Si hiciste `git reset --hard` por accidente y perdiste un commit:

```bash
# 1. Busca el hash del commit perdido en reflog
git reflog

# 2. Recupera el commit apuntando HEAD a ese hash
git reset --hard 7a8b9c0

# Salida esperada:
# HEAD is now at 7a8b9c0 Añade botón roto
# ¡Recuperado! El commit vuelve a existir.
```

> [!TIP] `reflog` es tu seguro de vida
> Mientras no pase mucho tiempo (por defecto Git retiene entradas en reflog durante 90 días), puedes recuperar cualquier cosa con `reflog`. Es la herramienta que te salva de los desastres con `reset --hard`.

---

## 5. Almacenamiento Temporal (`git stash`)

`git stash` guarda temporalmente tus cambios en una "pila" sin hacer commit, dejando el Working Directory limpio. Ideal para cambiar de rama sin perder tu trabajo en progreso.

```bash
# Guardar cambios temporalmente
git stash

# Salida esperada:
# Saved working directory and index state WIP on main: a1b2c3d Añade login
```

```bash
# Ver la lista de stashes guardados
git stash list

# Salida esperada:
# stash@{0}: WIP on main: a1b2c3d Añade login
# stash@{1}: WIP on feature: 9f8e7d6 Bug en CSS
```

```bash
# Recuperar el último stash y borrarlo de la pila
git stash pop

# Salida esperada:
# On branch main
# Changes not staged for commit:
#   modified:   app.js
# Dropped refs/stash@{0} (abc123...)
```

```bash
# Recuperar un stash sin borrarlo de la pila
git stash apply stash@{1}

# Borrar un stash específico
git stash drop stash@{0}

# Borrar TODOS los stashes
git stash clear
```

---

## 6. Etiquetado de Versiones (`git tag`)

Los **tags** marcan commits específicos como puntos importantes (normalmente versiones publicadas como `v1.0.0`).

```bash
# Crear un tag ligero
git tag v1.0.0

# Crear un tag anotado (con mensaje, recomendado)
git tag -a v1.0.0 -m "Primera versión estable"

# Listar todos los tags
git tag

# Salida esperada:
# v0.1.0
# v0.2.0
# v1.0.0
```

```bash
# Subir tags a GitHub
git push origin v1.0.0     # Un tag específico
git push origin --tags      # Todos los tags
```

> [!TIP] Tags y GitHub Releases
> En [[GitHub]], cuando subes un tag, puedes crear un **Release** asociado a él. Los Releases permiten adjuntar binarios descargables (como un `.zip` con el código compilado) y notas de la versión.
