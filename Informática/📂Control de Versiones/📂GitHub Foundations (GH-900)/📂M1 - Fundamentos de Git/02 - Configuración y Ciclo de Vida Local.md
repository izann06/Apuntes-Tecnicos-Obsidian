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

---

### Parte 1: ¿Qué es un remoto?

Cuando haces `git init` y empiezas a hacer commits, todo eso existe **únicamente en tu ordenador**. Es como escribir un diário en un cuaderno físico: está solo en tu casa.

Un **remoto** es ese mismo repositorio pero guardado en un servidor de internet (GitHub). Es la versión "en la nube" de tu cuaderno. Sirve para:

- Tener una copia de seguridad si tu ordenador se rompe.
- Que otras personas puedan ver y contribuir a tu proyecto.
- Colaborar en equipo.

Pero Git no sabe dónde está ese servidor hasta que tú se lo dices.

---

### Parte 2: ¿Qué es `origin`?

Piensa en la **agenda de contactos de tu móvil**.

En tu móvil tienes guardado a tu madre. Tú no marcas su número completo cada vez que la llamas: simplemente buscas "Mamá" y pulsas llamar. El número real es `+34 612 345 678`, pero tú lo has guardado con un **nombre corto**.

`origin` funciona exactamente igual:

```
Nombre en la agenda:   origin
Número real (URL):     git@github.com:izann06/mi-proyecto.git
```

En vez de escribir esa URL larga cada vez que quieras subir o bajar código, Git te deja guardarla con un apodo. El convenio mundial es llamarla siempre `origin`, como el "inicio", el servidor principal.

**Cuando ejecutas esto:**

```bash
git remote add origin git@github.com:izann06/mi-proyecto.git
```

Estás haciendo exactamente esto: *"Guarda este número de teléfono en mi agenda con el nombre 'origin'"*.

Desde ese momento, en vez de escribir la URL entera, usas el apodo:

```bash
# Sin apodo (tedioso, propenso a errores):
git push git@github.com:izann06/mi-proyecto.git main

# Con el apodo "origin" (cómodo):
git push origin main
```

**Comprueba qué tienes guardado en tu "agenda" (remotos):**

```bash
git remote -v

# Salida:
# origin  git@github.com:izann06/mi-proyecto.git (fetch)
# origin  git@github.com:izann06/mi-proyecto.git (push)
```

Aparece dos veces porque Git puede tener una URL diferente para descargar (fetch) y otra para subir (push). Normalmente son la misma.

**Gestionar la agenda de remotos:**

```bash
# Ver los remotos actuales
git remote -v

# Añadir un remoto
git remote add origin git@github.com:izann06/repo.git

# Cambiar la URL de un remoto (ej: cambiaste de HTTPS a SSH)
git remote set-url origin git@github.com:izann06/repo.git

# Eliminar un remoto (NO borra el repo en GitHub, solo el apodo local)
git remote remove origin

# Renombrar un remoto
git remote rename origin nuevo-nombre
```

---

### Parte 3: ¿Qué hace el `-u` en `git push -u origin main`?

Ahora que tienes la "agenda" configurada con `origin`, puedes llamar a GitHub. Pero hay otro problema:

Tu Git local tiene una rama llamada `main`. GitHub también tiene una rama llamada `main`. Pero **no están conectadas entre sí automáticamente**. Son como dos habitaciones en casas distintas con el mismo nombre: no se conocen.

Cuando haces el primer push, Git local necesita saber:

1. **¿A qué servidor subo esto?** → A `origin` (GitHub).
2. **¿A qué rama de ese servidor?** → A la rama `main`.
3. **¿Y en el futuro, cuando haga `git push` a secas, dónde va?** → Aquí entra el `-u`.

```bash
git push -u origin main
```

El flag `-u` (abreviatura de `--set-upstream`) hace dos cosas a la vez:

1. Sube tus commits a `origin/main`.
2. **Empareja para siempre** tu rama `main` local con la `main` de GitHub.

**Después de ese primer push con `-u`, Git ya sabe el camino de memoria:**

```bash
# Primera vez (obligatorio el -u):
git push -u origin main

# Todos los días a partir de entonces:
git push   # Sin poner nada más, ya sabe dónde ir
git pull   # Igual, ya sabe de dónde bajar
```

> [!TIP] Analogía del `-u`
> Es como cuando la primera vez que llamas a un taxi le das tu dirección completa. Le dices: *"Puerta de mi casa es Calle Mayor 5, y el trabajo es Avenida del Puerto 22"*. A partir de entonces, cuando llamas solo dices "al trabajo" y ya sabe a dónde ir sin que se lo repitas.

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

#### Opción A — El repo en GitHub ya tiene archivos (README, licencia...)

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

#### Opción B — Ya tienes archivos en local y el repo de GitHub está vacío

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

#### Opción C — Repo local con commits + GitHub con archivos (el caso problemático)

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
