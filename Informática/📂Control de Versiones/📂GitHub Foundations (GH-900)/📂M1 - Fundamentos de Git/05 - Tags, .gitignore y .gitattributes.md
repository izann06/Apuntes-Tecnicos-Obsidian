#git #gh-foundations #modulo-1 #tags #gitignore #gitattributes #semver

> [!info] Navegación
> ◀ [[04 - Deshacer Cambios y Recuperación]] · ▶ [[01 - Ecosistema y Productos]]

---

# 05 — Tags, .gitignore y .gitattributes

> **Resumen ejecutivo:**
> 1. Los **Tags** son marcadores permanentes de versiones importantes en el historial (ej: `v1.0.0`).
> 2. El **`.gitignore`** le dice a Git qué archivos ignorar y no trackear jamás.
> 3. El **`.gitattributes`** controla cómo Git trata ciertos archivos (saltos de línea, diff, merge).

---

## 1. Tags (Etiquetas de Versión)

Imagina que el historial de Git es una cinta de fotos infinita. Cada commit es una foto. Los **Tags** son como poner un **Post-it** en una foto concreta que dice "¡Esta foto es especial! Esta es la versión 1.0 que mandamos a producción".

A diferencia de una rama, un Tag **no se mueve**. Siempre apunta al mismo commit para siempre, como un marcador de libro permanente.

### Tipos de Tags

| Tipo | Cómo se crea | ¿Tiene mensaje? | ¿Tiene firma? | Uso |
|:---|:---|:---:|:---:|:---|
| **Lightweight** (Ligero) | ``git tag v1.0`` | ❌ No | ❌ No | Marcadores rápidos y privados |
| **Annotated** (Anotado) | ``git tag -a v1.0 -m "mensaje"`` | ✅ Sí | ✅ Puede | **El recomendado para releases públicas** |

> [!TIP] Exam Tip — Annotated vs Lightweight
> Si el examen pregunta cuál tipo de tag es recomendado para versiones oficiales de producción, la respuesta es **Annotated**. Porque guarda el autor, la fecha y el mensaje, igual que un commit completo.

### Comandos de Tags

```bash
# Crear un tag ligero
git tag v1.0-beta

# Crear un tag anotado (el recomendado, con mensaje)
git tag -a v1.0.0 -m "Primera versión estable."

# Ver todos los tags
git tag

# Ver detalles de un tag anotado
git show v1.0.0

# Subir un tag concreto a GitHub (push NO sube tags por defecto)
git push origin v1.0.0

# Subir TODOS los tags de golpe
git push origin --tags

# Borrar un tag local
git tag -d v1.0-beta

# Borrar un tag remoto (en GitHub)
git push origin --delete v1.0-beta
```

### Semantic Versioning (SemVer) — El Lenguaje de las Versiones

Cuando ves una versión como `v2.4.1`, eso no es un número aleatorio. Es un lenguaje universal llamado **Semantic Versioning**:

```
  v  2  .  4  .  1
  │  │     │     │
  │  │     │     └── PATCH: Corrección de bugs menores (sin romper nada)
  │  │     └──────── MINOR: Nueva función añadida (compatible con lo anterior)
  │  └────────────── MAJOR: Cambio que rompe la compatibilidad anterior
  └───────────────── El prefijo "v" es opcional pero habitual
```

**Ejemplo práctico:**
- App en `v1.4.2` → arreglas un bug → `v1.4.3` (PATCH).
- Añades pantalla nueva → `v1.5.0` (MINOR, reseteas PATCH a 0).
- Rehaces toda la API → `v2.0.0` (MAJOR, reseteas todo).

---

## 2. `.gitignore` — Decirle a Git qué ignorar

Cuando trabajas en un proyecto, hay archivos que NO quieres que Git trackee:
- **Contraseñas y API keys** (ej: `.env` con `DATABASE_PASSWORD=...`)
- **Dependencias instaladas** (`node_modules/` que pesa 500MB)
- **Archivos de compilación** (`dist/`, `build/`)
- **Archivos del editor** (`.vscode/`, `.idea/`, `.DS_Store` de Mac)

### Sintaxis y Patrones

```
# Ignorar todos los archivos .log en cualquier carpeta
*.log

# Ignorar un archivo concreto solo en la raíz
/config.local.json

# Ignorar una carpeta entera
node_modules/
dist/

# EXCEPCIÓN: ignorar todos los .env pero no este
!.env.example

# Ignorar archivos dentro de cualquier subcarpeta llamada "logs"
**/logs

# Ignorar solo .txt en la carpeta doc/
doc/*.txt
```

> [!WARNING] El .gitignore no borra lo que ya está trackeado
> Si ya hiciste commit de un archivo antes de añadirlo al `.gitignore`, Git seguirá trackeándolo. Para dejar de seguirlo: `git rm --cached nombre_archivo` y vuelve a commitear.

### .gitignore Global (Para tu máquina entera)

```bash
# Configurar un .gitignore global para todos tus repos
git config --global core.excludesfile ~/.gitignore_global

# Edita ~/.gitignore_global y añade:
# .DS_Store, Thumbs.db, .vscode/, .idea/...
```

### Jerarquía de .gitignore

```
~/.gitignore_global          ← Aplica a toda tu máquina
/tu-proyecto/.gitignore      ← Aplica a todo el repo
/tu-proyecto/src/.gitignore  ← Solo aplica a la carpeta src/
```
Las reglas más específicas tienen prioridad sobre las generales.

---

## 3. `.gitattributes` — Controlar cómo Git trata los archivos

Mientras `.gitignore` decide qué archivos IGNORAR, `.gitattributes` decide **cómo** Git trata los archivos que sí trackea.

### El problema más habitual: Saltos de línea (CRLF vs LF)

- **Windows** usa `CRLF` (`\r\n`) para terminar líneas.
- **Linux/Mac** usan solo `LF` (`\n`).

Si un programador de Windows y uno de Linux editan el mismo archivo, Git ve que "todas las líneas cambiaron" aunque el texto sea idéntico. Genera diffs enormes y conflictos absurdos.

```
# .gitattributes en la raíz del repo

# Para TODOS los archivos de texto: normalizar a LF en el repo,
# convertir automáticamente al formato del SO al hacer checkout
* text=auto

# Forzar LF para scripts de Linux
*.sh text eol=lf
*.py text eol=lf

# Forzar CRLF para scripts de Windows
*.bat text eol=crlf

# Marcar binarios para que Git no intente hacer diff
*.png binary
*.jpg binary
*.zip binary
```

> [!TIP] Exam Tip — .gitattributes
> El examen puede preguntar qué archivo controla los saltos de línea (CRLF/LF) entre desarrolladores de distintos SO. La respuesta es **`.gitattributes`**.
