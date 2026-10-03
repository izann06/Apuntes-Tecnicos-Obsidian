import os

base_dir = "/home/izanmm/Cosas_Personales/Apuntes-Tecnicos-Obsidian/Informática/📂Control de Versiones/📂GitHub Foundations (GH-900)"

updates = {
    "📂M1 - Fundamentos de Git/04 - Deshacer Cambios y Recuperación.md": """

## 💡 Conceptos Avanzados de Examen
- **Modificar el último commit silenciosamente:** Si olvidaste un archivo en tu último commit, añádelo con `git add <archivo>` y usa `git commit --amend --no-edit`. Esto integrará el archivo en el commit anterior sin pedirte que cambies el mensaje, manteniendo el historial limpio.
- **Diferencia entre resets:** `git reset --hard HEAD~2` no solo mueve el puntero 2 commits atrás, sino que **borra irrevocablemente** los cambios del directorio de trabajo y del área de ensayo (staging).
- **Recuperar commits perdidos:** Si usaste `git reset --hard` por error, puedes usar `git reflog` para ver el historial de movimientos de HEAD y encontrar el hash del commit "borrado" para recuperarlo.
- **Dejar de rastrear un archivo (untrack):** Si commiteaste un archivo por error (ej. `secret.ini`) y luego lo pones en el `.gitignore`, Git lo seguirá rastreando. Para solucionarlo debes sacarlo del index con `git rm --cached secret.ini` y luego hacer un nuevo commit.
""",
    "📂M1 - Fundamentos de Git/02 - Configuración y Ciclo de Vida Local.md": """

## 💡 Conceptos Avanzados de Examen
- **Clonado Bare (`git clone --bare`):** Crea una copia del repositorio que **no tiene directorio de trabajo** (working tree). Es decir, solo contiene la carpeta `.git`. Se usa casi exclusivamente para configurar servidores centrales que recibirán pushes de otros desarrolladores, no para trabajar en el código.
""",
    "📂M1 - Fundamentos de Git/03 - Historial y Comparación de Cambios.md": """

## 💡 Conceptos Avanzados de Examen
- **Estado 'Ahead of origin':** Si al ejecutar `git status` ves el mensaje `Your branch is ahead of 'origin/main' by X commits`, significa que tienes commits en tu máquina local que aún no has subido (pusheado) al servidor remoto. La solución es ejecutar `git push`.
""",
    "📂M3 - Productos y Administración GitHub/02 - Estructura Organizativa y Permisos.md": """

## 💡 Conceptos Avanzados de Examen
- **Rol Triage:** Permite gestionar Issues y Pull Requests (asignar, etiquetar, cerrar, mover en proyectos), pero **no permite crear ramas** ni hacer push al código.
- **Rol Admin de Repositorio:** Es el único rol de repositorio que puede gestionar el acceso de los equipos (Teams) a dicho repositorio. Los Maintainers pueden cambiar ajustes, pero no gestionar los accesos generales.
- **Privilegios Globales de la Organización:** Para evitar que miembros normales cambien la visibilidad de repositorios a público o los borren, un dueño de la organización debe configurar esto en los ajustes globales bajo **"Member privileges"**.
""",
    "📂M5 - Colaboración y Gobernanza/01 - Repositorios y Documentación.md": """

## 💡 Conceptos Avanzados de Examen
- **Template Repositories:** Puedes marcar cualquier repositorio en sus ajustes como "Template repository". Esto añade un botón "Use this template" que permite a otros crear un repositorio nuevo con la misma estructura y código inicial, pero **con un historial de commits completamente limpio**.
- **Transferencia de Repositorios:** Al transferir un repo de un usuario a otro (o a una organización), GitHub transfiere los Issues, Pull Requests y URLs intactas. Además, configura redirecciones automáticas para que los clones locales antiguos sigan funcionando al hacer `git push`/`git pull`.
""",
    "📂M5 - Colaboración y Gobernanza/02 - Issues y Gestión de Incidencias.md": """

## 💡 Conceptos Avanzados de Examen
- **Palabras Clave de Cierre:** Al hacer un PR, usar palabras como `Resolves #123` cierra automáticamente el Issue 123 al fusionarse el PR. 
- **Cierre cruzado (Cross-repo):** Si quieres cerrar un Issue en OTRO repositorio distinto, debes usar la sintaxis completa: `Resolves owner/repo#123`.
- **Issue Forms vs Templates:** Los Issue Forms usan **YAML** y permiten campos estructurados y validaciones (ej. marcar un campo como requerido). Los Issue Templates usan **Markdown** y son solo plantillas de texto.
""",
    "📂M5 - Colaboración y Gobernanza/03 - Fork vs Clone y Sincronización.md": """

## 💡 Conceptos Avanzados de Examen
- **Sincronización de Forks (Sync fork):** GitHub incluye un botón en la interfaz web de los forks llamado "Sync fork". Este botón hace un fetch del repositorio base (upstream) e intenta hacer un "Update branch" (fast-forward) a tu rama local directamente desde la interfaz, sin usar la línea de comandos.
- **Nomenclatura típica:** En un workflow de forks, `origin` es tu fork local, y `upstream` es el remoto que apunta al repositorio original del cual hiciste el fork.
""",
    "📂M5 - Colaboración y Gobernanza/04 - Pull Requests y Code Review.md": """

## 💡 Conceptos Avanzados de Examen
- **CODEOWNERS con reglas superpuestas:** Si un Pull Request modifica múltiples archivos, y cada archivo coincide con una regla distinta en `.github/CODEOWNERS`, **todos** los equipos involucrados serán solicitados como revisores. (Ej. `@global-team` por un `.md` y `@frontend-team` por un `.js`).
- **Draft Pull Requests:** Evitan que un PR sea fusionado accidentalmente y **no notifican automáticamente a los CODEOWNERS** hasta que el autor lo marca explícitamente como "Ready for review".
- **Changes Requested:** Cuando un revisor solicita cambios, actúa como un veto. Si el branch tiene reglas de protección activadas, el PR **no se podrá mergear** hasta que ese revisor lo apruebe o la revisión sea descartada.
- **Squash and Merge:** Comprime todos los commits de la rama de feature en un único commit en la rama base (`main`), perdiendo el rastro de los commits individuales pero manteniendo el historial lineal.
""",
    "📂M5 - Colaboración y Gobernanza/05 - Branch Protection e InnerSource.md": """

## 💡 Conceptos Avanzados de Examen
- **Require linear history:** Esta regla de protección impide que se hagan merge commits estándar ("Create a merge commit"). Obliga a los desarrolladores a integrar los PRs usando únicamente **Squash and merge** o **Rebase and merge**, manteniendo la línea temporal completamente recta.
""",
    "📂M5 - Colaboración y Gobernanza/06 - Markdown y Búsqueda Avanzada.md": """

## 💡 Conceptos Avanzados de Examen
- **Listas de Tareas (Task Lists):** La sintaxis en GitHub Flavored Markdown (GFM) es `- [ ] Tarea pendiente` y `- [x] Tarea completada`.
- **Citas en Bloque (Blockquotes):** Se utiliza el signo mayor que al inicio de la línea: `> Texto de la cita`.
- **Referencias de Issues entre repositorios:** Para enlazar o referenciar un Issue de un repositorio distinto dentro de tu misma organización, usa `owner/repo#123`. Usar solo `#123` buscará en el repositorio actual.
""",
    "📂M6 - Proyectos, Automatización e Integración/01 - GitHub Projects y Visualización.md": """

## 💡 Conceptos Avanzados de Examen
- **Búsqueda y Filtros Temporales:** En GitHub Projects (y en la búsqueda global), puedes usar operadores temporales relativos y absolutos. Por ejemplo, para buscar elementos no actualizados en los últimos 30 días, puedes usar el filtro `updated:<@today-30` o variaciones similares.
""",
    "📂M6 - Proyectos, Automatización e Integración/02 - GitHub Actions (CI-CD).md": """

## 💡 Conceptos Avanzados de Examen
- **Dependencias entre Jobs:** Por defecto, los Jobs corren en paralelo. Para ejecutar `deploy` solo después de `build`, añade `needs: build` en la configuración del job de deploy.
- **Compartir datos entre Jobs:** Puesto que corren en runners distintos, se hace mediante "outputs". En el Job 1 escribes al entorno `$GITHUB_OUTPUT`, y en el Job 2 lo referencias mediante `needs.<job1>.outputs.<var>`.
- **`pull_request` vs `pull_request_target`:** El trigger `pull_request_target` se usa por seguridad. Ejecuta el workflow usando el contexto y los secretos del repositorio **base** (ej. main), no del repositorio del fork. Esto previene que código malicioso de un fork robe secretos durante la ejecución.
- **Environment Secrets:** Para que un job acceda a un secreto de entorno (`production`), el job debe declarar explícitamente `environment: production`.
- **Matrices (Matrix builds) y fail-fast:** Por defecto, las matrices tienen `fail-fast: true`. Si pruebas en Node 16, 18 y 20, y la de Node 16 falla, las de 18 y 20 se **cancelarán automáticamente** para ahorrar recursos.
""",
    "📂M6 - Proyectos, Automatización e Integración/03 - GitHub Pages y Codespaces.md": """

## 💡 Conceptos Avanzados de Examen
- **Dominios Personalizados:** Para que GitHub asocie tu dominio personalizado (ej. `miweb.com`) a tu sitio de Pages, se debe crear un archivo llamado `CNAME` en la raíz de tu rama de publicación con el nombre del dominio dentro.
- **Despliegues con Actions vs rama `gh-pages`:** Al desplegar GitHub Pages mediante GitHub Actions, puedes tener tu repositorio limpio (solo con código fuente) y compilar todo dinámicamente en el runner, sin necesidad de hacer commits de tu carpeta de "build" o "dist" en tu historial de Git.
"""
}

for rel_path, content in updates.items():
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {rel_path}")
    else:
        print(f"WARNING: File not found {rel_path}")

