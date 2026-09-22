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
