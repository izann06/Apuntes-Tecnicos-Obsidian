#github #gh-foundations #cli #referencia-rapida #gh

> [!info] Navegación
> ▶ [[🎓 Índice Maestro - GitHub Foundations]]

---

# GitHub CLI — Referencia Completa de Comandos `gh`

**GitHub CLI** (`gh`) es la herramienta oficial de GitHub para la terminal. Te permite hacer casi todo lo que harías en la web de GitHub sin salir de la línea de comandos.

> [!TIP] Instalar GitHub CLI
> Descarga desde [cli.github.com](https://cli.github.com). En Windows con winget: `winget install GitHub.cli`

---

## Autenticación

```bash
# Iniciar sesión en GitHub (abre el navegador para autorizar)
gh auth login

# Ver el estado de autenticación actual
gh auth status

# Cerrar sesión
gh auth logout
```

---

## Repositorios (`gh repo`)

```bash
# Clonar un repositorio
gh repo clone usuario/repo

# Crear un nuevo repo (te pregunta opciones interactivamente)
gh repo create

# Crear repo privado con nombre y descripción (no interactivo)
gh repo create mi-proyecto --private --description "Mi proyecto secreto"

# Crear repo público
gh repo create mi-proyecto --public

# Ver info de un repositorio
gh repo view usuario/repo

# Abrir el repositorio en el navegador
gh repo view --web

# Hacer fork de un repositorio
gh repo fork usuario/repo

# Listar tus repositorios
gh repo list

# Listar repos de una organización
gh repo list mi-organizacion
```

---

## Pull Requests (`gh pr`)

```bash
# Listar los PRs abiertos del repositorio actual
gh pr list

# Crear un PR (interactivo)
gh pr create

# Crear un PR con todos los parámetros (no interactivo)
gh pr create --title "Añade login" --body "Implementa autenticación JWT" --base main

# Crear un Draft PR (borrador)
gh pr create --draft --title "WIP: Añade login"

# Ver los detalles de un PR
gh pr view 42

# Abrir el PR en el navegador
gh pr view 42 --web

# Revisar (aprobar) un PR
gh pr review 42 --approve

# Pedir cambios en un PR
gh pr review 42 --request-changes --body "Falta manejar el caso de error"

# Fusionar un PR (merge commit por defecto)
gh pr merge 42

# Fusionar con Squash
gh pr merge 42 --squash

# Fusionar con Rebase
gh pr merge 42 --rebase

# Hacer checkout de la rama de un PR localmente para revisarlo
gh pr checkout 42

# Ver el estado de los checks de CI del PR
gh pr checks 42
```

---

## Issues (`gh issue`)

```bash
# Listar issues abiertos
gh issue list

# Listar issues cerrados
gh issue list --state closed

# Listar issues con un label específico
gh issue list --label "bug"

# Crear un issue (interactivo)
gh issue create

# Crear un issue con parámetros
gh issue create --title "Bug en el login" --body "Al pulsar enter el formulario no envía" --label bug

# Ver los detalles de un issue
gh issue view 15

# Abrir el issue en el navegador
gh issue view 15 --web

# Cerrar un issue
gh issue close 15

# Reabrir un issue cerrado
gh issue reopen 15

# Comentar en un issue
gh issue comment 15 --body "Investigando el problema..."
```

---

## GitHub Actions (`gh workflow` / `gh run`)

```bash
# Listar los workflows del repositorio
gh workflow list

# Ejecutar manualmente un workflow
gh workflow run "CI Build"

# Ver las ejecuciones recientes de workflows
gh run list

# Ver el detalle de una ejecución
gh run view 1234567890

# Ver los logs en tiempo real de una ejecución
gh run watch 1234567890
```

---

## GitHub Codespaces (`gh codespace`)

```bash
# Listar tus Codespaces
gh codespace list

# Crear un Codespace para el repo actual
gh codespace create

# Conectarse a un Codespace vía SSH
gh codespace ssh

# Abrir un Codespace en VS Code
gh codespace code

# Eliminar un Codespace
gh codespace delete --codespace NOMBRE
```

---

## Gists (`gh gist`)

```bash
# Crear un gist público desde un archivo
gh gist create mi_script.py

# Crear un gist secreto
gh gist create mi_script.py --secret

# Crear un gist con un título/descripción
gh gist create mi_script.py --desc "Script para automatizar backups"

# Listar tus gists
gh gist list

# Ver un gist
gh gist view GIST_ID

# Editar un gist
gh gist edit GIST_ID
```

---

## Comandos de utilidad

```bash
# Abrir la página principal de GitHub en el navegador
gh browse

# Abrir un archivo concreto del repo en el navegador
gh browse src/main.py

# Ver el estado general de los servicios de GitHub
gh api /meta | jq .

# Buscar repositorios en GitHub
gh search repos "machine learning" --language python

# Buscar issues en GitHub
gh search issues "login bug" --repo usuario/repo
```
