#git #gh-foundations #modulo-1 #git-log #git-diff #git-show

> [!info] Navegación
> ◀ [[02 - Configuración y Ciclo de Vida Local]] · ▶ [[04 - Deshacer Cambios y Recuperación]]

---

# 03 — Historial y Comparación de Cambios

> **Resumen ejecutivo:**
> 1. `git log` muestra el historial cronológico. Se puede filtrar por número, archivo, fecha y autor.
> 2. `git show <hash>` inspecciona un commit específico mostrando sus metadatos y el diff completo.
> 3. `git diff` compara estados: Working Directory vs Staging, Staging vs HEAD, o dos commits entre sí.

---

## 1. Visualización del Historial (`git log`)

```bash
git log

# Salida esperada:
# commit a1b2c3d4e5f6... (HEAD -> main)
# Author: Izan <izan@email.com>
# Date:   Sun Sep 21 19:00:00 2026 +0200
#
#     Añade formulario de login
#
# commit 9f8e7d6c5b4a...
# Author: Izan <izan@email.com>
# Date:   Sat Sep 20 14:30:00 2026 +0200
#
#     Configuración inicial del proyecto
```

### Formato compacto (`--oneline`)

```bash
git log --oneline

# Salida esperada:
# a1b2c3d (HEAD -> main) Añade formulario de login
# 9f8e7d6 Configuración inicial del proyecto
# 3c4d5e6 Initial commit
```

### Historial visual con gráfico de ramas (`--graph`)

```bash
git log --oneline --graph --all

# Salida esperada:
# * a1b2c3d (HEAD -> main) Merge branch 'feature/login'
# |\
# | * e5f6g7h (feature/login) Añade validación
# | * 8h9i0j1 Crea formulario de login
# |/
# * 9f8e7d6 Configuración inicial
```

---

## 2. Filtrado Avanzado del Historial

### Limitar número de commits

```bash
git log -3

# Muestra solo los 3 commits más recientes
```

### Filtrar por archivo específico

```bash
git log -- report.md

# Salida esperada (solo commits que modificaron report.md):
# commit 3c4d5e6...
# Author: Izan <izan@email.com>
#
#     Actualiza sección de conclusiones en report.md
```

### Combinar filtros

```bash
# Los 2 últimos commits que afectaron a un archivo concreto
git log -2 -- mental_health_survey.csv
```

### Filtrar por rango de fechas

```bash
# Commits desde una fecha específica
git log --since="2026-09-01"

# Commits hasta una fecha
git log --until="2026-09-15"

# Combinar ambos (rango)
git log --since="2026-09-01" --until="2026-09-15"

# Usando lenguaje natural
git log --since="2 weeks ago"
git log --since="yesterday"
```

**Tabla de Formatos de Fecha:**

| Formato | Ejemplo | ¿Válido? | Notas |
| :--- | :--- | :---: | :--- |
| **ISO 8601** | `2026-09-21` | ✅ | **Recomendado**. Sin ambigüedad. |
| **Lenguaje natural** | `"2 weeks ago"`, `"yesterday"` | ✅ | Útil para búsquedas rápidas. |
| **ISO preciso** | `2026-09-21T14:30:00` | ✅ | Máxima precisión. |
| **Local ambiguo** | `09/21/2026` | ⚠️ | Puede fallar según la configuración regional. Evitar. |

### Filtrar por autor

```bash
git log --author="Izan"

# Salida esperada:
# commit a1b2c3d...
# Author: Izan <izan@email.com>
# [...]
```

---

## 3. Inspección de un Commit Específico (`git show`)

```bash
git show a1b2c3d4

# Salida esperada:
# commit a1b2c3d4e5f6...
# Author: Izan <izan@email.com>
# Date:   Sun Sep 21 19:00:00 2026 +0200
#
#     Añade formulario de login
#
# diff --git a/login.html b/login.html
# new file mode 100644
# --- /dev/null
# +++ b/login.html
# @@ -0,0 +1,5 @@
# +<form id="login-form">
# +  <input type="email" placeholder="Email">
# +  <input type="password" placeholder="Contraseña">
# +  <button type="submit">Entrar</button>
# +</form>
```

> [!TIP] Hashes cortos
> No necesitas los 40 caracteres del hash SHA-1. Git identifica un commit con solo los **primeros 8 a 10 caracteres**: `git show a1b2c3d4` funciona perfectamente.

---

## 4. Comparación de Cambios (`git diff`)

### Working Directory vs. Último Commit (cambios NO preparados)

```bash
git diff

# Salida esperada:
# diff --git a/app.js b/app.js
# --- a/app.js
# +++ b/app.js
# @@ -10,3 +10,4 @@
#  function login() {
# -  console.log("old login");
# +  console.log("new secure login");
# +  validateInput();
#  }
```

### Staging Area vs. Último Commit (cambios YA preparados)

```bash
git diff --staged

# Salida esperada (misma estructura pero comparando lo que ya hiciste git add):
# diff --git a/styles.css b/styles.css
# --- a/styles.css
# +++ b/styles.css
# @@ -1,3 +1,4 @@
# +.login-form { padding: 20px; }
```

### Comparar un archivo individual

```bash
git diff app.js
git diff --staged styles.css
```

### Comparar dos Commits del historial

```bash
# Mediante Hashes (el más ANTIGUO va primero)
git diff 9f8e7d6 a1b2c3d

# Mediante referencias relativas (HEAD)
git diff HEAD~1 HEAD

# Salida esperada:
# diff --git a/login.html b/login.html
# new file mode 100644
# +++ b/login.html
# +<form id="login-form">
# [...]
```

> [!WARNING] Cuidado con el orden de los hashes
> Si escribes los hashes al revés (`git diff <reciente> <antiguo>`), **verás el diff invertido**: los añadidos aparecen como borrados y viceversa. Pon siempre **el más antiguo a la izquierda** y **el más reciente a la derecha**.

### Comparar dos ramas

```bash
git diff main feature/login

# Muestra todas las diferencias entre la rama main y la rama feature/login
```
