#git #gh-foundations #cheatsheet #referencia #comandos

> [!info] Navegación
> ◀ [[🎓 Índice Maestro - GitHub Foundations]] · ▶ [[02 - Guía Visual de GitHub (Interfaz y Flujos)]]

---

# 01 — Cheatsheet Completa: Todos los Comandos de Git

> **Cómo usar este archivo:** Es una referencia rápida. Cada comando tiene sus variantes más importantes. Para la explicación profunda de cada concepto, ve a los archivos de cada módulo.

---

## 🔧 Configuración (`git config`)

| Comando | Qué hace |
| :--- | :--- |
| `git config --global user.name "Izan"` | Define tu nombre para todos los repos |
| `git config --global user.email "tu@email.com"` | Define tu email para todos los repos |
| `git config --local user.email "trabajo@empresa.com"` | Sobreescribe el email solo en este repo |
| `git config --list` | Muestra toda la configuración activa |
| `git config --global core.editor "code --wait"` | Cambia el editor por defecto a VS Code |
| `git config --global alias.historial "log --oneline --graph --all"` | Crea un alias (atajo) personalizado |
| `git config --global alias.st "status"` | Alias corto: `git st` = `git status` |

---

## 🏗️ Inicialización (`git init` / `git clone`)

| Comando | Qué hace |
| :--- | :--- |
| `git init` | Crea un repositorio nuevo vacío en la carpeta actual |
| `git init nombre-proyecto` | Crea una carpeta nueva con un repo dentro |
| `git clone https://github.com/usuario/repo.git` | Descarga un repositorio de GitHub |
| `git clone https://...repo.git mi-carpeta` | Clona y guarda en una carpeta con nombre personalizado |
| `git clone --depth 1 https://...repo.git` | Clona solo el último commit (más rápido, historial incompleto) |

---

## 📋 Estado del Repositorio (`git status` / `git log`)

| Comando | Qué hace |
| :--- | :--- |
| `git status` | Muestra archivos modificados, preparados o sin seguimiento |
| `git status -s` | Versión compacta (una línea por archivo) |
| `git log` | Historial completo de commits (más reciente primero) |
| `git log --oneline` | Historial en formato compacto (una línea por commit) |
| `git log --oneline --graph --all` | Historial con árbol visual de ramas |
| `git log --oneline --graph --all --decorate` | Igual pero mostrando etiquetas y referencias |
| `git log -5` | Muestra solo los últimos 5 commits |
| `git log -5 --oneline` | Los últimos 5 en formato compacto |
| `git log -- archivo.js` | Historial de solo ese archivo |
| `git log -3 -- report.md` | Los últimos 3 commits que tocaron report.md |
| `git log --author="Izan"` | Commits solo de ese autor |
| `git log --since="2026-09-01"` | Commits desde esa fecha |
| `git log --until="2026-09-15"` | Commits hasta esa fecha |
| `git log --since="2026-09-01" --until="2026-09-15"` | Rango de fechas |
| `git log --since="2 weeks ago"` | Lenguaje natural |
| `git log --since="yesterday"` | Lenguaje natural |
| `git log --pretty=oneline` | Formato oneline con hash completo |
| `git log --pretty=format:"%h %an %s"` | Formato personalizado: hash corto, autor, mensaje |

---

## ➕ Preparación de Cambios (`git add`)

| Comando | Qué hace |
| :--- | :--- |
| `git add index.html` | Añade un archivo específico al staging |
| `git add .` | Añade **todos** los archivos modificados y nuevos |
| `git add -A` | Igual que `git add .` (incluyendo borrados) |
| `git add *.css` | Añade todos los archivos con extensión `.css` |
| `git add src/` | Añade todos los archivos dentro de la carpeta `src/` |
| `git add -p` | Modo interactivo: decide chunk a chunk qué añadir |

---

## 💾 Confirmar Cambios (`git commit`)

| Comando | Qué hace |
| :--- | :--- |
| `git commit -m "Mensaje aquí"` | Commit con mensaje directo (lo más habitual) |
| `git commit` | Abre el editor para escribir el mensaje |
| `git commit -am "Mensaje"` | `git add` + `git commit` en un paso (solo archivos ya trackeados) |
| `git commit --amend -m "Nuevo mensaje"` | Reemplaza el mensaje del ÚLTIMO commit |
| `git commit --amend --no-edit` | Añade los archivos del staging al ÚLTIMO commit sin cambiar el mensaje |

> [!WARNING] `commit -am` no funciona con archivos nuevos (untracked). Para esos, siempre `git add` primero.

---

## ↩️ Deshacer y Restaurar (`git restore` / `git revert` / `git reset`)

| Comando | Qué hace |
| :--- | :--- |
| `git restore archivo.js` | Descarta cambios del Working Directory (destructivo) |
| `git restore .` | Descarta TODOS los cambios no preparados |
| `git restore --staged archivo.js` | Saca el archivo del Staging (sin borrar los cambios) |
| `git restore --staged .` | Saca TODOS los archivos del Staging |
| `git revert HEAD` | Crea un nuevo commit que deshace el último commit |
| `git revert HEAD --no-edit` | Revert sin abrir el editor (acepta mensaje por defecto) |
| `git revert 9f8e7d6` | Revierte un commit específico por su hash |
| `git revert HEAD -n` | Aplica el revert en staging sin hacer commit automático |
| `git reset --soft HEAD~1` | Deshace el último commit; los cambios quedan en Staging |
| `git reset HEAD~1` | Deshace el último commit; los cambios quedan sin preparar |
| `git reset --hard HEAD~1` | Deshace el último commit y borra los cambios (peligroso) |
| `git reset --hard <hash>` | Mueve HEAD al commit indicado (puede ser hacia adelante o atrás) |

---

## 🔍 Inspección y Comparación (`git show` / `git diff`)

| Comando | Qué hace |
| :--- | :--- |
| `git show a1b2c3d4` | Muestra los metadatos y el diff de un commit |
| `git show HEAD` | Muestra el último commit |
| `git show HEAD~2` | Muestra el commit de hace 2 posiciones |
| `git diff` | Cambios en Working Directory que NO están en Staging |
| `git diff --staged` | Cambios que YA están en Staging vs. último commit |
| `git diff app.js` | Diff de un archivo específico (no trackeados no aparecen) |
| `git diff --staged styles.css` | Diff en Staging de un archivo específico |
| `git diff 9f8e7d6 a1b2c3d` | Diferencias entre dos commits (el más antiguo primero) |
| `git diff HEAD~1 HEAD` | Diferencias entre el penúltimo y el último commit |
| `git diff main feature/login` | Diferencias entre dos ramas |

---

## 🌿 Gestión de Ramas (`git branch` / `git switch`)

| Comando | Qué hace |
| :--- | :--- |
| `git branch` | Lista todas las ramas locales |
| `git branch -a` | Lista ramas locales y remotas |
| `git branch -v` | Lista ramas con su último commit |
| `git branch feature/login` | Crea una rama nueva (sin moverte a ella) |
| `git switch feature/login` | Cambia a una rama existente |
| `git switch -c feature/login` | Crea una rama Y se mueve a ella (forma moderna) |
| `git checkout -b feature/login` | Crea una rama Y se mueve a ella (forma clásica) |
| `git branch -d feature/login` | Borra una rama fusionada (seguro) |
| `git branch -D feature/login` | Borra una rama aunque no esté fusionada (forzado) |
| `git branch -m nombre-viejo nombre-nuevo` | Renombra una rama |

---

## 🔀 Fusión (`git merge`)

| Comando | Qué hace |
| :--- | :--- |
| `git merge feature/login` | Fusiona la rama indicada en la rama actual |
| `git merge feature/login --no-ff` | Fuerza la creación de un Commit de Merge (aunque sea Fast-Forward) |
| `git merge feature/login --squash` | Aplana todos los commits de la rama en uno solo antes de fusionar |
| `git merge --continue` | Finaliza el merge tras resolver conflictos |
| `git merge --abort` | Cancela el merge en conflicto y vuelve al estado anterior |

---

## 🔁 Rebase (`git rebase`)

| Comando | Qué hace |
| :--- | :--- |
| `git rebase main` | Reaplica los commits de la rama actual sobre la punta de `main` |
| `git rebase --continue` | Continúa el rebase tras resolver un conflicto |
| `git rebase --abort` | Cancela el rebase y vuelve al estado anterior |
| `git rebase -i HEAD~3` | Rebase interactivo de los últimos 3 commits (reordenar, squash, editar...) |

---

## 🍒 Cherry-pick (`git cherry-pick`)

| Comando | Qué hace |
| :--- | :--- |
| `git cherry-pick e5f6g7h` | Copia un commit concreto a la rama actual |
| `git cherry-pick e5f6g7h a1b2c3d` | Copia varios commits a la vez |
| `git cherry-pick --no-commit e5f6g7h` | Aplica los cambios en Staging sin hacer commit automático |

---

## 🗄️ Stash (`git stash`)

| Comando | Qué hace |
| :--- | :--- |
| `git stash` | Guarda todos los cambios sin commitear en la pila |
| `git stash save "Mensaje descriptivo"` | Guarda el stash con un mensaje personalizado |
| `git stash list` | Lista todos los stashes guardados |
| `git stash pop` | Recupera el último stash y lo borra de la pila |
| `git stash apply stash@{1}` | Recupera un stash específico sin borrarlo de la pila |
| `git stash drop stash@{0}` | Borra un stash específico |
| `git stash clear` | Borra TODOS los stashes |
| `git stash show` | Muestra un resumen del último stash guardado |

---

## 🌐 Repositorios Remotos (`git remote` / `git push` / `git pull`)

| Comando | Qué hace |
| :--- | :--- |
| `git remote -v` | Lista los remotos configurados con sus URLs |
| `git remote add origin https://...` | Asocia el repo local al remoto con nombre `origin` |
| `git remote remove origin` | Elimina el vínculo con el remoto |
| `git push origin main` | Sube la rama `main` al remoto |
| `git push -u origin main` | Sube y configura el tracking (solo la primera vez) |
| `git push origin feature/login` | Sube una rama nueva al remoto |
| `git push origin --delete feature/login` | Borra una rama en el remoto |
| `git push --tags` | Sube todos los tags al remoto |
| `git fetch origin` | Descarga los cambios del remoto SIN fusionarlos |
| `git pull origin main` | `fetch` + `merge` en un solo paso |
| `git pull --rebase origin main` | `fetch` + `rebase` en lugar de merge |

---

## 🏷️ Tags (`git tag`)

| Comando | Qué hace |
| :--- | :--- |
| `git tag` | Lista todos los tags |
| `git tag v1.0.0` | Crea un tag ligero en el commit actual |
| `git tag -a v1.0.0 -m "Primera versión"` | Crea un tag anotado (con mensaje, recomendado) |
| `git tag v1.0.0 9f8e7d6` | Crea un tag en un commit anterior |
| `git tag -d v1.0.0` | Borra un tag local |
| `git push origin v1.0.0` | Sube un tag al remoto |
| `git push origin --tags` | Sube todos los tags al remoto |

---

## 🧰 Historial Oculto (`git reflog`)

| Comando | Qué hace |
| :--- | :--- |
| `git reflog` | Muestra TODOS los movimientos de HEAD (incluso tras reset --hard) |
| `git reset --hard HEAD@{3}` | Vuelve al estado de hace 3 movimientos según el reflog |
| `git reset --hard 7a8b9c0` | Recupera un commit "borrado" usando su hash del reflog |

> [!TIP] El reflog retiene entradas durante 90 días por defecto. Tu red de seguridad definitiva.

---

## 📄 Ignorar Archivos (`.gitignore`)

```bash
# Archivo que no quieres que Git rastree nunca:
node_modules/      # Carpeta completa
.env               # Archivo de variables de entorno
*.log              # Todos los archivos .log
dist/              # Carpeta de build
!importante.log    # Excepción: este sí se rastrea aunque sea .log
**/temp            # Cualquier carpeta "temp" a cualquier profundidad
```

```bash
# Si ya añadiste algo por error y quieres dejar de rastrearlo:
git rm --cached archivo.txt    # Deja de rastrear sin borrar el archivo
git rm --cached -r carpeta/    # Ídem para una carpeta entera
```

---

## 🔑 Tabla Resumen: Los 10 Comandos que Más Usarás

| # | Comando | Situación |
| :---: | :--- | :--- |
| 1 | `git status` | Siempre, antes de hacer nada |
| 2 | `git add .` | Preparar todos los cambios |
| 3 | `git commit -m "mensaje"` | Guardar el estado |
| 4 | `git push origin main` | Subir a GitHub |
| 5 | `git pull origin main` | Actualizar desde GitHub |
| 6 | `git switch -c feature/nueva` | Empezar una funcionalidad |
| 7 | `git merge feature/nueva` | Fusionar cuando termines |
| 8 | `git log --oneline --graph` | Ver el historial visual |
| 9 | `git stash` / `git stash pop` | Guardar trabajo a medias |
| 10 | `git restore --staged .` | Sacar todo del staging |
