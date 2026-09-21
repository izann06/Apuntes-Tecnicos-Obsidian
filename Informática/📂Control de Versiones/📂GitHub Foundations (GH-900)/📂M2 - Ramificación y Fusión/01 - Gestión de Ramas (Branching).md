#git #gh-foundations #modulo-2 #ramas #branching

> [!info] Navegación
> ◀ [[04 - Deshacer Cambios y Recuperación]] · ▶ [[02 - Fusión y Resolución de Conflictos]]

---

# 01 — Gestión de Ramas (Branching)

> **Resumen ejecutivo:**
> 1. Una **rama** es un puntero móvil a un commit. Crear una rama es instantáneo y barato en [[Git]].
> 2. `git switch` (moderno) o `git checkout` (clásico) cambian de rama. `-c` / `-b` crean y cambian en un paso.
> 3. La rama principal se llama `main` (antes `master`). Nunca se trabaja directamente en ella.

---

## 1. Concepto de Rama

Una **rama** en Git no es una copia del código. Es simplemente un **puntero ligero** que apunta a un commit específico. Cuando haces un nuevo commit en esa rama, el puntero avanza automáticamente al nuevo commit.

```
main:      A --- B --- C     (HEAD apunta aquí)
```

Cuando creas una rama nueva, Git crea un segundo puntero al mismo commit:

```
main:      A --- B --- C     (main apunta aquí)
                       |
feature:               C     (feature también apunta aquí)
                              (HEAD → feature)
```

Al hacer commits en la nueva rama, solo su puntero avanza:

```
main:      A --- B --- C
                        \
feature:                 D --- E     (HEAD → feature)
```

---

## 2. Crear, Cambiar y Listar Ramas

### Crear una rama

```bash
git branch feature/login

# Git es silencioso. Confirma con:
git branch

# Salida esperada:
#   feature/login
# * main               ← El asterisco indica en qué rama estás
```

### Cambiar de rama

```bash
# Forma moderna (recomendada)
git switch feature/login

# Forma clásica (equivalente)
git checkout feature/login

# Salida esperada:
# Switched to branch 'feature/login'
```

### Crear y cambiar en un solo paso

```bash
# Forma moderna
git switch -c feature/registro

# Forma clásica
git checkout -b feature/registro

# Salida esperada:
# Switched to a new branch 'feature/registro'
```

> [!TIP] Exam Tip — `switch` vs `checkout`
> `git switch` fue introducido en Git 2.23 para simplificar el cambio de ramas. `git checkout` sigue funcionando, pero tiene demasiadas funciones mezcladas (cambiar ramas, restaurar archivos). El examen puede mencionar ambos.

### Listar todas las ramas

```bash
# Ramas locales
git branch

# Ramas locales y remotas
git branch -a

# Salida esperada:
# * main
#   feature/login
#   remotes/origin/main
#   remotes/origin/feature/login
```

---

## 3. Renombrar y Borrar Ramas

### Renombrar

```bash
# Renombrar la rama actual
git branch -m nuevo-nombre

# Renombrar una rama específica
git branch -m nombre-viejo nombre-nuevo
```

### Borrar

```bash
# Borrado seguro (solo si ya fue fusionada)
git branch -d feature/login

# Salida esperada:
# Deleted branch feature/login (was a1b2c3d).

# Borrado forzado (aunque NO haya sido fusionada)
git branch -D feature/experimento

# Salida esperada:
# Deleted branch feature/experimento (was 9f8e7d6).
```

> [!WARNING] Diferencia entre `-d` y `-D`
> - `-d` (minúscula): Borrado **seguro**. Git se niega a borrar la rama si tiene commits que no han sido fusionados en ningún otro sitio. Te protege de perder trabajo.
> - `-D` (mayúscula): Borrado **forzado**. Borra la rama sin importar si tiene commits sin fusionar. Úsalo solo si estás seguro de que quieres descartarla.

---

## 4. La Rama Principal (`main`)

| Concepto | Detalle |
| :--- | :--- |
| **Nombre histórico** | `master` (usado hasta 2020) |
| **Nombre actual** | `main` (estándar en GitHub desde octubre 2020) |
| **Propósito** | Contiene el código estable y listo para producción |
| **Regla de oro** | Nunca se trabaja directamente en `main`. Se crean ramas, se desarrolla ahí y se fusionan mediante Pull Requests. |

> [!WARNING] Pregunta frecuente de examen
> Si el examen pregunta cuál es la rama **por defecto** al crear un repositorio en GitHub, la respuesta es `main`. Si pregunta cuál era el nombre antiguo, es `master`. Ambos son solo convenciones; Git no obliga a usar ningún nombre.
