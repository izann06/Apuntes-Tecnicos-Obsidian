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

### Deshacer la preparación (`git restore --staged`)

Imagina que la *Staging Area* es una caja donde estás metiendo cosas para enviar. Si metes un archivo por error, puedes **sacarlo de la caja sin perder tus modificaciones** usando `--staged`.

```bash
# 1. Sacar el archivo de la Staging Area (vuelve al Working Directory)
git restore --staged index.html

# 2. Descartar los cambios por completo (PELIGRO: borra lo que has escrito)
git restore index.html
```

- **Con `--staged`:** Tus líneas de código están a salvo, solo le dices a Git "no incluyas esto en el próximo commit todavía".
- **Sin `--staged`:** Git borra tus modificaciones y devuelve el archivo a como estaba en el último commit. ¡No hay botón de deshacer para esto!

---

## 4. Confirmación de Cambios (`git commit`)

```bash
# Crear un commit con un mensaje descriptivo
git commit -m "Añade formulario de login"

# Salida esperada:
# [main a1b2c3d] Añade formulario de login
#  2 files changed, 45 insertions(+), 3 deletions(-)
```

### Atajo: El comando `git commit -am`

Este comando combina dos banderas (flags) para saltarse el paso de `git add`:

- **`-a` (all):** Añade a la Staging Area todos los archivos modificados o borrados que Git **ya conoce** (trackeados).
- **`-m` (message):** Permite escribir el mensaje del commit.

```bash
git commit -am "Corrige bug en la validación"
```

> [!WARNING] Pregunta frecuente de examen: El peligro del `-am`
> El flag `-a` **NO incluye archivos nuevos** (untracked). 
> **Ejemplo:** Si modificas `app.js` (ya trackeado) y creas `nuevo.js` (no trackeado), y ejecutas `git commit -am "fix"`, **solo se guardará `app.js`**. El archivo `nuevo.js` se quedará fuera porque Git aún no lo conoce. Para archivos nuevos, siempre debes usar `git add` primero.

### Corregir el Último Commit (`--amend`)

En lugar de crear un commit nuevo que diga "Ups, me olvidé de este archivo", Git te permite **abrir el último commit, meterle más cosas o cambiarle el mensaje, y volverlo a cerrar**. A esto se le llama "enmendar" (*amend*).

**Caso 1: Me equivoqué en el mensaje**

```bash
git commit --amend -m "Mensaje corregido y sin faltas de ortografía"
```

**Caso 2: Me olvidé de añadir un archivo importante**

```bash
# 1. Preparas el archivo olvidado en la Staging Area
git add estilo_olvidado.css

# 2. Lo fusionas dentro del ÚLTIMO commit (sin cambiar el mensaje)
git commit --amend --no-edit
```

*(El flag `--no-edit` le dice a Git: "usa el mismo mensaje que ya tenía el commit, solo mételo dentro").*

> [!WARNING] Cuidado con `--amend` en commits subidos
> Al usar `--amend`, Git borra el commit original y crea uno **totalmente nuevo** (con un hash diferente) en su lugar. Por tanto, **nunca uses `--amend` en un commit que ya hayas subido a GitHub** (`git push`), porque reescribirás la historia y romperás el código de tus compañeros. Úsalo solo localmente.

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

---

## 6. Remotos, `origin` y el Misterio del `-u`

Esta sección explica el tropiezo más habitual de todo el mundo con Git. Lo entiendes una vez y no te vuelve a dar problemas nunca más.

### ¿Qué es un "remoto" y qué es `origin`?

Cuando haces `git init`, tu repositorio existe **solo en tu ordenador**. Un **remoto** es simplemente la dirección de ese mismo repositorio alojado en un servidor externo (GitHub).

`origin` **no es nada especial ni técnico**. Es solo un **apodo** (alias) que se le da por convenio mundial a la URL del servidor principal. En vez de escribir la URL entera cada vez, le pones un nombre corto.

```bash
# Asociar tu repo local a GitHub (darle el alias "origin" a esa URL)
git remote add origin git@github.com:izann06/mi-proyecto.git

# Ver qué remotos tienes configurados (y sus URLs reales)
git remote -v

# Salida:
# origin  git@github.com:izann06/mi-proyecto.git (fetch)
# origin  git@github.com:izann06/mi-proyecto.git (push)
```

> [!TIP] ¿Por qué aparece dos veces (fetch y push)?
> Git permite configurar URLs diferentes para descargar (fetch) y para subir (push). Normalmente son la misma. Por eso aparece dos líneas con el mismo valor.

**Comandos para gestionar remotos:**

```bash
# Ver los remotos configurados
git remote -v

# Añadir un remoto
git remote add origin git@github.com:izann06/repo.git

# Cambiar la URL de un remoto (ej: de HTTPS a SSH)
git remote set-url origin git@github.com:izann06/repo.git

# Eliminar un remoto (no borra el repo en GitHub, solo el alias local)
git remote remove origin

# Renombrar un remoto
git remote rename origin nuevo-nombre
```

---

### ¿Qué hace el `-u` en `git push -u origin main`?

Tu rama local se llama `main`. La rama en GitHub también se llama `main`. Pero Git **no las empareja automáticamente**. Son dos cosas independientes hasta que tú lo configures.

La primera vez que subes código, tienes que decirle a Git DOS cosas:

1. **¿A qué servidor?** → `origin`
2. **¿A qué rama de ese servidor?** → `main`

```bash
git push -u origin main
```

El flag `-u` (o `--set-upstream`) hace el emparejamiento **una sola vez para siempre**: *"Esta rama local `main` queda ligada a `origin/main`"*.

**La ventaja:**
```bash
# Primera vez (necesario el -u):
git push -u origin main

# A partir de ahora, para siempre, basta con:
git push
git pull
```

---

### ¿Por qué falla `git pull` en un repositorio nuevo?

Es el error más frecuente y confuso. Ocurre cuando tu local y GitHub tienen historiales **paralelos e independientes** que nunca se han "conocido".

**El escenario que lo provoca:**

```
TU ORDENADOR:             GITHUB:
git init                  Creaste el repo
└── Commit A (local)      └── Commit B (lo creó GitHub)

Git dice: "No sé cómo fusionar A con B, son universos paralelos"
```

**Los dos errores clásicos que verás:**

```
fatal: refusing to merge unrelated histories
```
```
There is no tracking information for the current branch.
```

---

### Los 3 Flujos Correctos para Crear un Repositorio

#### ✅ Opción A — El repo en GitHub ya tiene archivos (README, licencia...)
**La forma más fácil: clónalo directamente. No hagas `git init`.**

```bash
# 1. Clona tu repositorio de GitHub
git clone git@github.com:izann06/nombre-repo.git

# 2. Entra en la carpeta
cd nombre-repo

# 3. Mete tus archivos y trabaja normal
git add .
git commit -m "primer commit"
git push   # Ya funciona sin -u porque clone lo configura todo solo
```

> Al clonar, Git configura `origin`, el emparejamiento (`-u`) y el tracking **automáticamente**. Es el flujo más limpio.

---

#### ✅ Opción B — Ya tienes archivos en local y el repo de GitHub está vacío
**Crea el repo en GitHub 100% vacío** (sin README, sin .gitignore, sin licencia).

```bash
git init
git add .
git commit -m "primer commit"
git branch -M main                                      # Asegurar que la rama se llama main
git remote add origin git@github.com:izann06/repo.git
git push -u origin main                                 # Primera vez: necesita el -u
```

Como GitHub estaba vacío, no hay conflicto de historias. Entra directo sin errores.

---

#### 🔧 Opción C — Repo local con commits + GitHub con archivos (el caso problemático)
Si ya hiciste `git init` y tienes commits, **pero en GitHub también hay cosas** (marcaste "Add README" al crearlo):

```bash
# 1. Conectas tu local a GitHub
git remote add origin git@github.com:izann06/repo.git

# 2. Renombrar rama a main si se llama master
git branch -M main

# 3. Descargas los cambios de GitHub sin fusionar aún
git fetch origin

# 4. Fusionas las dos historias independientes (flag especial)
git pull origin main --allow-unrelated-histories

# Git te pedirá un mensaje para el commit de merge
# En nano: escribe el mensaje y pulsa Ctrl+X → Y → Enter

# 5. Ahora ya puedes subir todo junto
git push -u origin main
```

> [!WARNING] ¿Qué hace `--allow-unrelated-histories`?
> Le dice a Git: *"Sé que estas dos historias no comparten ningún antepasado común. Fusiónalas de todas formas."* Sin este flag, Git se niega por seguridad.

---

### Lo que pasó en tu sesión de práctica (explicado)

```bash
mkdir Practica-GH-900
git init                # Se crea en rama "master" (versiones antiguas de Git)
git remote add origin git@github.com:izann06/Pruebas-GitHub.git
git pull                # ← ERROR: no hay tracking, rama se llama master pero GitHub tiene main
```

**¿Por qué falló?**
1. `git init` creó la rama `master` (nombre antiguo por defecto).
2. GitHub tenía la rama `main` (nombre moderno por defecto).
3. Git no sabía emparejar `master` local con `origin/main` remota porque nadie se lo dijo.
4. Además, la carpeta local estaba vacía (ningún commit), así que tampoco había base para hacer un merge.

**La solución correcta para ese caso:**
```bash
git branch -M main                              # Renombrar master → main
git pull origin main --allow-unrelated-histories  # Fusionar si GitHub tiene archivos

# O si el repo de GitHub no tiene nada importante, la alternativa limpia:
git fetch origin
git reset --hard origin/main                    # Descartar el local y usar el de GitHub
```
