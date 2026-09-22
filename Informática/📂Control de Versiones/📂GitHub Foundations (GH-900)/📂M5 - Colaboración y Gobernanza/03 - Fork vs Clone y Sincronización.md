#github #gh-foundations #modulo-5 #fork #clone #upstream

> [!info] Navegación
> ◀ [[02 - Issues y Gestión de Incidencias]] · ▶ [[04 - Pull Requests y Code Review]]

---

# 03 — Fork vs Clone y Sincronización

> **Resumen ejecutivo:**
> 1. **Clonar** = descargar una copia del repo a tu máquina. Necesitas permisos de escritura para hacer push.
> 2. **Forkear** = crear una copia independiente del repo en tu cuenta de GitHub. No necesitas permisos.
> 3. Para contribuir a Open Source: Fork → Clone → Haz cambios → Push a tu fork → Abre Pull-Request al repo original.

---

## 1. Clone vs. Fork

|                                  | `git clone`                              | Fork (GitHub)                                 |
| :------------------------------- | :--------------------------------------- | :-------------------------------------------- |
| **¿Qué crea?**                   | Copia local en tu máquina                | Copia del repo en tu cuenta de GitHub         |
| **¿Dónde vive?**                 | En tu disco duro                         | En github.com bajo tu usuario                 |
| **¿Necesitas permisos?**         | Para clonar no, para hacer push sí       | No, cualquiera puede forkear un repo público  |
| **¿Está vinculado al original?** | Sí (remote `origin`)                     | Sí (GitHub mantiene la referencia)            |
| **¿Cuándo se usa?**              | Cuando eres colaborador directo del repo | Cuando quieres contribuir a un proyecto ajeno |

```
Repositorio Original (upstream)
        │
        ├── Fork ──────► Tu copia en GitHub (origin)
        │                       │
        │                  git clone
        │                       │
        │                Tu copia local
        │                       │
        │                  git push
        │                       │
        │                Tu fork actualizado
        │                       │
        └──── Pull Request ◄────┘
```

---

## 2. Flujo Completo: Contribuir a Open Source

```bash
# 1. Haz Fork del repo en GitHub (botón "Fork" en la web)

# 2. Clona TU fork (no el original)
git clone git@github.com:izanm/proyecto-ajeno.git
cd proyecto-ajeno

# 3. Configura el remoto "upstream" (el repo original)
git remote add upstream https://github.com/autor-original/proyecto-ajeno.git

# 4. Verifica los remotos
git remote -v

# Salida esperada:
# origin    git@github.com:izanm/proyecto-ajeno.git (fetch)
# origin    git@github.com:izanm/proyecto-ajeno.git (push)
# upstream  https://github.com/autor-original/proyecto-ajeno.git (fetch)
# upstream  https://github.com/autor-original/proyecto-ajeno.git (push)
```

```bash
# 5. Crea una rama para tus cambios
git switch -c fix/typo-readme

# 6. Haz tus cambios y commitea
git add .
git commit -m "Fix typo in README.md"

# 7. Sube los cambios a TU fork
git push origin fix/typo-readme

# 8. Abre un Pull Request en GitHub (desde tu fork al repo original)
```

---

## 3. Sincronizar tu Fork con el Original

Con el tiempo, el repositorio original avanza y tu fork se queda desactualizado.

### Opción 1: Desde la Terminal

```bash
# Descarga los últimos cambios del repo original
git fetch upstream

# Cambia a tu rama main
git switch main

# Fusiona los cambios del upstream en tu main
git merge upstream/main

# Sube tu main actualizado a tu fork en GitHub
git push origin main
```

### Opción 2: Desde GitHub (Sin terminal)

GitHub muestra un banner en tu fork: **"This branch is X commits behind autor-original:main"**. Haz clic en **"Sync fork" > "Update branch"** y se actualiza automáticamente.

> [!TIP] Exam Tip — `git fetch` vs `git pull`
> El examen puede preguntar la diferencia:
> - **`git fetch`**: Descarga los cambios del remoto pero **NO los fusiona** en tu rama. Solo actualiza las referencias remotas.
> - **`git pull`**: Es un `git fetch` + `git merge` en un solo comando. Descarga Y fusiona automáticamente.
> 
> | Comando | Descarga | Fusiona |
> | :--- | :---: | :---: |
> | `git fetch` | ✅ | ❌ |
> | `git pull` | ✅ | ✅ |
