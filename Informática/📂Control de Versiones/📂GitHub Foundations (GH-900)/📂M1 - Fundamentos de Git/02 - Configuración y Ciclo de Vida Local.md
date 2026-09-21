#git #gh-foundations #modulo-1 #configuracion #gitignore

> [!info] Navegación
> ◀ [[01 - Arquitectura Interna y Estados]] · ▶ [[03 - Historial y Comparación de Cambios]]

---

# 02 — Configuración Inicial y Ciclo de Vida Local

> **Resumen ejecutivo:**
> 1. Antes de usar [[Git]], debes configurar tu **identidad** (`user.name` y `user.email`).
> 2. El ciclo básico es: Editar → `git add` → `git commit`. El archivo `.gitignore` excluye archivos no deseados.
> 3. Puedes corregir el último commit con `git commit --amend` sin crear uno nuevo.

---

## 1. Configuración Global y Local

Antes de tu primer commit, Git necesita saber quién eres:

```bash
# Configurar tu nombre (aparece en cada commit)
git config --global user.name "Izan"

# Configurar tu email (debe coincidir con el de tu cuenta de GitHub)
git config --global user.email "izan@email.com"

# Verificar la configuración actual
git config --list

# Salida esperada:
# user.name=Izan
# user.email=izan@email.com
# core.autocrlf=true
# [...otras configuraciones]
```

| Alcance | Flag | ¿Dónde se guarda? | ¿A qué afecta? |
| :--- | :--- | :--- | :--- |
| **Global** | `--global` | `~/.gitconfig` | A todos los repositorios del usuario |
| **Local** | `--local` (o sin flag) | `.git/config` del repo | Solo a ese repositorio |
| **Sistema** | `--system` | `/etc/gitconfig` | A todos los usuarios de la máquina |

> [!TIP] Prioridad de configuración
> La configuración **local** tiene prioridad sobre la **global**, que tiene prioridad sobre la de **sistema**. Esto te permite usar un email personal para tus repos personales y un email de empresa para los repos del trabajo.

---

## 2. Inicialización y Estado

```bash
# Crear un nuevo repositorio vacío en la carpeta actual
git init

# Salida esperada:
# Initialized empty Git repository in /home/izan/mi-proyecto/.git/
```

```bash
# Ver el estado actual del repositorio
git status

# Salida esperada (sin cambios):
# On branch main
# nothing to commit, working tree clean

# Salida esperada (con cambios sin preparar):
# On branch main
# Changes not staged for commit:
#   modified:   index.html
#
# Untracked files:
#   styles.css
```

---

## 3. Preparación de Cambios (`git add`)

El comando `git add` mueve archivos del **Working Directory** a la **Staging Area**:

```bash
# Añadir un archivo específico al staging
git add index.html

# Añadir todos los archivos modificados y nuevos
git add .

# Añadir todos los archivos con una extensión específica
git add *.css
```

Para **desmarcar** un archivo del staging (sin perder tus cambios en el código):

```bash
git restore --staged index.html

# Salida esperada (al hacer git status después):
# Changes not staged for commit:
#   modified:   index.html
```

---

## 4. Confirmación de Cambios (`git commit`)

```bash
# Crear un commit con un mensaje descriptivo
git commit -m "Añade formulario de login"

# Salida esperada:
# [main a1b2c3d] Añade formulario de login
#  2 files changed, 45 insertions(+), 3 deletions(-)
```

```bash
# Añadir al staging y hacer commit en un solo paso (solo archivos ya trackeados)
git commit -am "Corrige bug en la validación"
```

> [!WARNING] Pregunta frecuente de examen
> `git commit -am` **NO incluye archivos nuevos** (untracked). Solo añade automáticamente los archivos que Git ya conoce (que ya fueron añadidos al menos una vez con `git add`). Para archivos nuevos, siempre debes hacer `git add` primero.

### Corregir el Último Commit (`--amend`)

Si cometiste un error en el mensaje o se te olvidó incluir un archivo:

```bash
# Corregir solo el mensaje del último commit
git commit --amend -m "Mensaje corregido"

# Añadir un archivo olvidado al último commit
git add archivo_olvidado.js
git commit --amend --no-edit
# (--no-edit mantiene el mensaje original)

# Salida esperada:
# [main 9f8e7d6] Mensaje corregido
#  Date: Sun Sep 21 19:00:00 2026 +0200
#  3 files changed, 50 insertions(+)
```

> [!WARNING] Cuidado con `--amend` en commits subidos
> Nunca uses `--amend` en un commit que **ya hayas subido** a GitHub (`git push`). Reescribe el historial y causará conflictos a tus compañeros de equipo. Úsalo solo para commits que aún están en tu máquina local.

---

## 5. El Archivo `.gitignore`

El archivo `.gitignore` le dice a Git qué archivos o carpetas debe **ignorar completamente** (no trackear, no añadir, no commitear).

```bash
# Ejemplo de .gitignore típico:

# Dependencias de Node.js
node_modules/

# Variables de entorno (NUNCA subir credenciales)
.env
.env.local

# Archivos del sistema operativo
.DS_Store
Thumbs.db

# Archivos compilados o de build
dist/
build/
*.log

# Archivos del IDE
.vscode/
.idea/
```

**Reglas de sintaxis:**

| Patrón | Efecto |
| :--- | :--- |
| `archivo.txt` | Ignora ese archivo en cualquier carpeta |
| `carpeta/` | Ignora toda la carpeta y su contenido |
| `*.log` | Ignora todos los archivos con extensión `.log` |
| `!importante.log` | Excepción: NO ignora ese archivo aunque coincida con `*.log` |
| `**/temp` | Ignora cualquier carpeta llamada `temp` a cualquier profundidad |

> [!TIP] Exam Tip — `.gitignore` se debe crear al inicio
> La buena práctica es crear el `.gitignore` al inicio del proyecto, antes del primer commit. Si olvidas incluir algo y ya fue commiteado, Git seguirá trackeándolo incluso después de añadirlo al `.gitignore`. Para dejar de trackearlo: `git rm --cached <archivo>`.
