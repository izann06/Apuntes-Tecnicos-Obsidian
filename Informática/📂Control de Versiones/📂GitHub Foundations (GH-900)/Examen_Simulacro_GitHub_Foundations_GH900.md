# Simulacro de Examen: GitHub Foundations (GH-900) - Nivel Avanzado

Este simulacro ha sido diseñado para evaluar tu comprensión profunda de Git y GitHub, simulando la dificultad y la ambigüedad que puedes encontrar en el examen real de certificación GitHub Foundations. Las preguntas están diseñadas para poner a prueba tu conocimiento más allá de lo básico, abordando escenarios reales y detalles específicos de la plataforma.

## Parte 1: Preguntas

**1. Un desarrollador acaba de ejecutar `git commit -m "Fix bug"` pero se dio cuenta de que olvidó añadir un archivo crucial (`config.yml`) que ya estaba modificado en su directorio de trabajo. ¿Cuál es la secuencia de comandos más eficiente y que mantiene el historial limpio para solucionar esto sin crear un commit adicional de "corrección"?**
- a) `git add config.yml` -> `git commit -m "Add config"` -> `git rebase -i HEAD~2`
- b) `git add config.yml` -> `git commit --amend --no-edit`
- c) `git reset --soft HEAD~1` -> `git add config.yml` -> `git commit -m "Fix bug"`
- d) `git stash` -> `git commit --amend` -> `git stash pop`

**2. En GitHub, tienes un archivo `.github/CODEOWNERS` configurado con la siguiente regla: `* @global-team` y en la siguiente línea `*.js @frontend-team`. Si un Pull Request modifica tanto un archivo `.js` como un archivo `.md`, ¿quiénes son solicitados automáticamente para la revisión según las reglas de CODEOWNERS?**
- a) Solo `@frontend-team`, ya que la regla más específica sobrescribe a la general para todo el PR.
- b) Ambos, `@global-team` (por el `.md`) y `@frontend-team` (por el `.js`).
- c) Solo `@global-team`, porque la regla global se evalúa primero y detiene la evaluación.
- d) Ninguno, ya que existe un conflicto de solapamiento en las reglas de extensión.

**3. Has clonado un repositorio de GitHub, creado una rama local, hecho varios commits y quieres subir tu rama al repositorio remoto (origin) por primera vez, estableciendo la conexión de seguimiento (tracking). ¿Cuál de los siguientes comandos debes utilizar?**
- a) `git push origin my-branch --force`
- b) `git push -u origin my-branch`
- c) `git push origin HEAD`
- d) `git branch --set-upstream origin/my-branch`

**4. En una organización de GitHub, se te ha asignado el rol de "Triage" (Clasificación) en un repositorio específico. ¿Cuál de las siguientes acciones NO tienes permitido realizar?**
- a) Asignar Issues a otros miembros del equipo.
- b) Aplicar etiquetas (labels) a los Pull Requests.
- c) Crear nuevas ramas (branches) en el repositorio.
- d) Cerrar Issues existentes.

**5. Estás revisando un Pull Request que tiene la opción "Squash and merge" seleccionada. El PR contiene 5 commits diferentes con mensajes detallados. ¿Qué ocurrirá con el historial de la rama base (`main`) después de hacer clic en "Squash and merge"?**
- a) Los 5 commits se copiarán a `main` manteniendo sus hashes originales pero agrupados bajo un commit de fusión.
- b) Se creará un único commit nuevo en `main` que contendrá todos los cambios, y los 5 commits originales desaparecerán del historial de `main`.
- c) Se creará un commit de fusión (merge commit) y los 5 commits originales se añadirán como padres de este nuevo commit.
- d) La operación fallará si hay conflictos de rebase antes del squash.

**6. ¿Cuál es el propósito principal de usar la palabra clave `Resolves owner/repo#123` en el cuerpo (body) de un Pull Request en lugar de simplemente escribir `#123`?**
- a) Permitir el cierre automático de un Issue que se encuentra en un repositorio diferente dentro de GitHub al hacer merge del PR.
- b) Asignar automáticamente el PR al propietario del repositorio referenciado.
- c) Crear un enlace permanente que no se rompe si el repositorio cambia de nombre.
- d) Evitar que GitHub cierre el Issue automáticamente, dejándolo solo como referencia.

**7. Un flujo de trabajo de GitHub Actions está configurado con `on: pull_request_target`. ¿En qué se diferencia este trigger principalemente del trigger estándar `on: pull_request`?**
- a) `pull_request_target` solo se ejecuta cuando el PR es aprobado por un revisor.
- b) `pull_request_target` ejecuta el flujo de trabajo en el contexto (y con los secretos) del repositorio base, no desde el fork de origen.
- c) `pull_request_target` previene la ejecución de acciones si el PR contiene modificaciones en archivos `.yml`.
- d) `pull_request_target` solo funciona para repositorios de organizaciones empresariales (Enterprise).

**8. Estás utilizando GitHub Projects (V2). Quieres crear una vista que muestre automáticamente los Issues que no han sido actualizados en los últimos 30 días. ¿Qué filtro en la barra de búsqueda del proyecto usarías?**
- a) `updated:<30-days`
- b) `last-updated: >30d`
- c) `updated:<@today-30`
- d) `status:stale`

**9. Al usar `git rebase main` estando en tu rama de características (`feature`), te encuentras con un conflicto. Después de resolver el conflicto en tus archivos y usar `git add`, ¿cuál es el siguiente paso correcto para continuar con la operación?**
- a) `git commit -m "Resolve rebase conflicts"`
- b) `git rebase --continue`
- c) `git merge --continue`
- d) `git push --force`

**10. Has habilitado "Dependabot security updates" en tu repositorio. ¿Cómo actúa exactamente Dependabot cuando se descubre una nueva vulnerabilidad en una de tus dependencias declaradas (por ejemplo, en `package.json`)?**
- a) Actualiza silenciosamente la dependencia en la rama por defecto y crea un commit firmado.
- b) Crea un Issue detallando la vulnerabilidad y sugiere un parche en los comentarios.
- c) Abre un Pull Request automáticamente con la actualización a la versión mínima necesaria que parchea la vulnerabilidad.
- d) Envía un correo electrónico a los administradores del repositorio bloqueando los futuros pushes hasta que se resuelva manualmente.

**11. ¿Qué comando de Git te permite extraer un commit específico de una rama y aplicarlo directamente en tu rama actual, creando un nuevo commit con los mismos cambios y el mismo mensaje original?**
- a) `git merge <commit-hash>`
- b) `git cherry-pick <commit-hash>`
- c) `git revert <commit-hash>`
- d) `git rebase -i <commit-hash>`

**12. En GitHub Actions, si tienes un job de `build` y un job de `deploy`, ¿cómo configuras el flujo de trabajo para garantizar que `deploy` solo se ejecute si `build` se completa con éxito?**
- a) Utilizando la sintaxis `requires: [build]` dentro de la definición del job `deploy`.
- b) Definiendo ambos jobs bajo el mismo `step`.
- c) Utilizando la sintaxis `needs: build` dentro de la configuración del job `deploy`.
- d) Los jobs en GitHub Actions se ejecutan secuencialmente por defecto en el orden en que están escritos.

**13. Un equipo de desarrollo quiere evitar que cualquier miembro suba secretos (como tokens de API o claves privadas) al repositorio. ¿Qué función de GitHub deberían habilitar y configurar?**
- a) Code scanning alerts (CodeQL).
- b) Secret scanning con "Push protection" (Protección de push) activado.
- c) Branch protection rules exigiendo firmas de commits (signed commits).
- d) Dependabot version updates.

**14. Dentro de un archivo Markdown en GitHub (como un `README.md` o un comentario de Issue), quieres crear una lista de tareas (task list) interactiva. ¿Cuál es la sintaxis correcta?**
- a) `- [ ] Tarea pendiente`
- b) `* ( ) Tarea pendiente`
- c) `1. [x] Tarea completada`
- d) Ambos a) y c) son correctos si se usan en listas ordenadas o desordenadas.

**15. Estás usando GitHub Pages para alojar el sitio web de tu proyecto. Tienes un dominio personalizado (`www.miproyecto.com`). ¿Qué archivo especial debes crear en la raíz de tu fuente de publicación de GitHub Pages para que GitHub asocie correctamente el dominio?**
- a) Un archivo llamado `.domain` con el nombre de dominio en su interior.
- b) Un archivo llamado `CNAME` que contenga únicamente tu dominio personalizado.
- c) Modificar el archivo `_config.yml` añadiendo `url: "www.miproyecto.com"`.
- d) Un archivo `index.html` con un meta tag de redirección.

**16. Un repositorio tiene configurada una regla de protección de rama en `main` que requiere "Require linear history". Un desarrollador intenta hacer un merge de un PR usando el botón estándar "Create a merge commit". ¿Qué sucederá?**
- a) El merge se completará pero se enviará una alerta al administrador.
- b) El botón estará deshabilitado o el merge será rechazado, ya que se requiere usar "Squash and merge" o "Rebase and merge".
- c) El commit de merge se transformará automáticamente en un squash.
- d) Se creará el merge commit de todos modos, ya que las reglas de protección solo aplican a la línea de comandos (CLI).

**17. Ejecutas el comando `git reset --hard HEAD~2`. ¿Qué impacto tiene esto en tu repositorio local?**
- a) Mueve el puntero HEAD dos commits atrás, manteniendo los cambios de esos commits en el área de ensayo (staging area).
- b) Elimina permanentemente los dos últimos commits de la historia remota (origin).
- c) Deshace los últimos dos commits y elimina irrevocablemente los cambios de esos commits de tu directorio de trabajo y del área de ensayo.
- d) Crea dos nuevos commits de reversión (revert) para anular los cambios recientes.

**18. En el contexto de GitHub Issues, ¿cuál es la diferencia clave entre un "Issue Template" (plantilla de Issue en Markdown) y un "Issue Form" (formulario de Issue en YAML)?**
- a) Los Issue Forms permiten campos de entrada estructurados, menús desplegables y validación obligatoria, mientras que los Templates son solo texto pre-rellenado.
- b) Los Issue Templates solo están disponibles para repositorios Enterprise, mientras que los Forms son públicos.
- c) Los Issue Forms se almacenan en `.github/ISSUE_TEMPLATE` y los Templates en `.github/FORMS`.
- d) No hay diferencia funcional, solo es un cambio de sintaxis (YAML vs Markdown).

**19. Has creado un Fork de un repositorio "Upstream". El repositorio "Upstream" ha avanzado con varios commits nuevos. Quieres sincronizar la rama `main` de tu Fork desde la interfaz web de GitHub. ¿Qué funcionalidad utilizas?**
- a) "Compare & pull request" desde origin hacia upstream.
- b) "Sync fork" -> "Update branch" en la página principal de tu Fork.
- c) Crear un Pull Request desde `upstream/main` hacia `origin/main` y hacer merge.
- d) Tanto b) como c) son formas válidas, pero b) es el botón rápido dedicado.

**20. ¿Qué comando de Git se utiliza para ver el registro de todos los movimientos del puntero HEAD, permitiéndote recuperar commits que parecen haber sido borrados o "perdidos" (por ejemplo, después de un `git reset --hard`)?**
- a) `git history`
- b) `git reflog`
- c) `git fsck`
- d) `git log --lost-found`

**21. ¿Qué es GitHub Copilot?**
- a) Una herramienta de análisis estático de código integrada en GitHub Actions.
- b) Un asistente de programación basado en Inteligencia Artificial que sugiere código y funciones completas en tiempo real dentro del IDE.
- c) Un bot de revisión de código (Code Review) automático exclusivo para Pull Requests.
- d) Una función de GitHub Projects para estimar automáticamente el esfuerzo de los Issues.

**22. Tienes un archivo en tu repositorio llamado `secret_config.ini` que has estado trackeando. Te das cuenta de que no deberías subirlo. Lo agregas al archivo `.gitignore`. ¿Por qué al ejecutar `git status` el archivo sigue apareciendo como modificado y siendo rastreado?**
- a) El archivo `.gitignore` necesita ser commiteado primero para que sus reglas surtan efecto.
- b) `.gitignore` solo ignora archivos que no están actualmente siendo rastreados (untracked) por Git.
- c) Necesitas ejecutar `git clean -fd` para aplicar el `.gitignore`.
- d) El archivo `secret_config.ini` tiene reglas de permisos a nivel de sistema operativo que bloquean a Git.

**23. ¿Cómo resolverías el problema descrito en la pregunta 22 (hacer que Git deje de rastrear un archivo ya trackeado, pero manteniéndolo en tu disco local)?**
- a) `git rm secret_config.ini` -> `git commit`
- b) `git rm --cached secret_config.ini` -> `git commit`
- c) `git reset HEAD secret_config.ini`
- d) Borrar el archivo manualmente, hacer commit, y luego restaurarlo de la papelera.

**24. GitHub Discussions permite crear foros dentro de un repositorio. ¿Qué tipo de discusión es ideal para cuando quieres que la comunidad vote por respuestas correctas (estilo Stack Overflow)?**
- a) Q&A (Preguntas y Respuestas)
- b) General
- c) Ideas
- d) Show and tell

**25. En GitHub Actions, necesitas pasar una variable generada dinámicamente en un Job (`job1`) para que sea utilizada por otro Job (`job2`) que se ejecuta después. ¿Cuál es el mecanismo correcto para lograr esto?**
- a) Usar variables de entorno a nivel de workflow (`env:` en la raíz del YAML).
- b) Usar la sintaxis de "outputs" del job (`jobs.<job_id>.outputs`) escribiendo en `$GITHUB_OUTPUT`.
- c) Subir la variable como un "artifact" usando `actions/upload-artifact`.
- d) Escribir el valor en un secreto del repositorio a través de la API de GitHub durante el `job1`.

**26. Eres administrador de una Organización en GitHub. Quieres asegurarte de que ningún miembro pueda borrar repositorios o cambiar su visibilidad a público sin autorización. ¿Dónde configuras esto a nivel global para la organización?**
- a) En las reglas de Branch Protection de cada repositorio individual.
- b) En los ajustes de "Member privileges" (Privilegios de miembros) dentro de la configuración de la Organización.
- c) Utilizando un archivo `.github/CODEOWNERS` a nivel de organización.
- d) Creando un equipo de "Seguridad" y asignándoles el rol de lectura exclusiva.

**27. ¿Cuál es la principal ventaja de utilizar "Draft Pull Requests" (Pull Requests en borrador) en GitHub?**
- a) Previenen que cualquier usuario, excepto los administradores, pueda ver el código modificado.
- b) Evitan que el PR sea fusionado (merged) accidentalmente y no notifican automáticamente a los CODEOWNERS hasta que se marca como "Ready for review".
- c) No consumen minutos de ejecución de GitHub Actions.
- d) Permiten hacer commits sin necesidad de proporcionar un mensaje de commit válido.

**28. Un equipo usa un Forking Workflow. El usuario "Alice" ha hecho un fork del repositorio `empresa/proyecto`. Ha clonado su fork localmente. ¿Cómo se denomina típicamente el remoto que apunta al repositorio original `empresa/proyecto` para poder traer los últimos cambios?**
- a) origin
- b) base
- c) upstream
- d) master

**29. Has añadido un secreto llamado `API_KEY` a los "Environment secrets" para un entorno llamado `production`. Tienes un workflow que despliega a producción. ¿Qué condición se debe cumplir en el workflow de GitHub Actions para poder acceder a ese secreto?**
- a) El workflow debe estar en la rama `main`.
- b) El job que necesita el secreto debe especificar `environment: production` en su configuración.
- c) El secreto debe invocarse usando `${{ secrets.production.API_KEY }}`.
- d) Los Environment secrets están obsoletos, se deben usar Repository secrets.

**30. En GitHub Markdown (GFM), ¿cómo se formatea correctamente una cita en bloque (block quote)?**
- a) `<quote>Texto de la cita</quote>`
- b) `>> Texto de la cita`
- c) `> Texto de la cita`
- d) `"Texto de la cita"` al inicio de la línea.

**31. Has escrito un script en bash y quieres compartirlo como un fragmento de código (snippet) rápido, con control de versiones, pero sin crear un repositorio completo. ¿Qué herramienta de GitHub es la más adecuada para este propósito?**
- a) GitHub Pages
- b) GitHub Wikis
- c) GitHub Gist
- d) GitHub Packages

**32. ¿Qué significa el estado "Changes requested" (Se solicitaron cambios) en un Pull Request dejado por un revisor que tiene permisos de escritura?**
- a) Es solo un estado visual; el PR aún puede ser fusionado por el autor sin hacer los cambios.
- b) Si las reglas de protección de rama requieren aprobaciones, bloquea la fusión del PR hasta que el revisor original apruebe (apruebe la revisión) o la revisión sea descartada.
- c) Cierra automáticamente el PR. Tendrá que ser reabierto después de que se hagan los commits.
- d) Revierte (reverts) automáticamente los últimos commits realizados en el PR.

**33. Ejecutas `git status` y ves el siguiente mensaje: `Your branch is ahead of 'origin/main' by 3 commits.`. ¿Qué significa exactamente esto?**
- a) Hay 3 commits en el servidor remoto que tú no tienes en tu máquina local. Debes hacer `git pull`.
- b) Tienes 3 commits en tu repositorio local que aún no has enviado al servidor remoto. Debes hacer `git push`.
- c) Hay un conflicto de fusión pendiente de resolver en 3 archivos diferentes.
- d) Tu repositorio local está desactualizado y necesita ser sincronizado.

**34. GitHub CLI (`gh`) es una herramienta de línea de comandos potente. ¿Cuál de los siguientes comandos te permitiría clonar un repositorio y hacer fork al mismo tiempo, dejándolo listo para trabajar?**
- a) `gh clone --fork owner/repo`
- b) `gh repo clone owner/repo --fork`
- c) `gh repo fork owner/repo --clone`
- d) `git clone --gh-fork owner/repo`

**35. Tienes un commit local que contiene una contraseña por error. Aún no has hecho push al repositorio remoto. ¿Cuál es la forma más limpia de eliminar la contraseña antes de hacer push?**
- a) Hacer un nuevo commit eliminando la contraseña y luego hacer `git push`.
- b) Hacer un `git revert` del commit y luego un push.
- c) Usar `git commit --amend` si es el último commit, modificando el archivo y el índice sin la contraseña.
- d) Hacer push primero y luego borrar el commit del servidor remoto desde la interfaz de GitHub.

**36. En GitHub, ¿qué funcionalidad te permite crear plantillas base de repositorios (con estructura de carpetas, configuraciones CI/CD y código boilerplate) para que otros usuarios puedan iniciar nuevos proyectos a partir de ellas con un solo clic?**
- a) GitHub Packages.
- b) Repository Templates (marcar el repositorio como "Template repository").
- c) GitHub Releases.
- d) GitHub Gist Templates.

**37. Estás configurando una matriz de ejecución (matrix build) en GitHub Actions para probar tu código en Node.js 16, 18 y 20 en los sistemas operativos Ubuntu y Windows. Por defecto, si la prueba en Node.js 16/Ubuntu falla, ¿qué sucede con los demás jobs en la matriz que aún se están ejecutando?**
- a) Continúan ejecutándose de forma independiente hasta que terminan.
- b) Se cancelan inmediatamente porque la opción predeterminada `fail-fast` está establecida en `true`.
- c) Se pausan esperando a que el desarrollador resuelva el error.
- d) Se reinician automáticamente desde el principio.

**38. ¿Cuál es el comportamiento predeterminado del botón "Merge pull request" (Merge commit) en GitHub cuando fusionas un PR que tiene 10 commits en `main`?**
- a) Crea 10 commits nuevos en la rama `main` y un commit adicional de merge.
- b) Mantiene los 10 commits originales en la historia y crea 1 commit extra de merge que une las dos líneas temporales, conservando los hashes de los 10 commits.
- c) Aplasta los 10 commits en uno solo.
- d) Aplica un rebase de los 10 commits sobre `main` sin crear un commit de merge.

**39. ¿Qué rol de repositorio en una organización necesitas como mínimo para poder gestionar el acceso de los equipos (Teams) a dicho repositorio?**
- a) Write
- b) Maintain
- c) Admin
- d) Owner de la organización (exclusivamente)

**40. Tienes un repositorio donde los usuarios reportan muchos bugs idénticos. Quieres guiar a los usuarios para que proporcionen información específica (versión de SO, pasos para reproducir, logs) obligatoriamente. La mejor manera de forzar esta estructura en GitHub es:**
- a) Crear un archivo `.github/ISSUE_TEMPLATE.md` estándar y pedirles por favor que lo sigan.
- b) Utilizar un Issue Form creado con un archivo YAML (ej. `bug_report.yml`) definiendo los campos como requeridos.
- c) Usar GitHub Actions para cerrar automáticamente los issues que no tengan cierta longitud.
- d) Desactivar los Issues y obligarlos a usar Pull Requests.

**41. ¿Cuál es la diferencia principal entre usar `git fetch` y `git pull`?**
- a) `git fetch` descarga los cambios del remoto a tus ramas de seguimiento (tracking branches) locales pero no modifica tu espacio de trabajo (working directory). `git pull` hace un `fetch` e inmediatamente intenta fusionar (merge) esos cambios en tu rama actual.
- b) `git pull` solo actualiza el repositorio local, mientras que `git fetch` sincroniza en ambas direcciones (sube y baja cambios).
- c) No hay diferencia práctica; ambos son alias del mismo comando interno de Git.
- d) `git fetch` se usa para ramas secundarias y `git pull` solo debe usarse en la rama `main`.

**42. Has utilizado el comando `git stash` temporalmente para guardar tu trabajo inacabado. Luego de cambiar de rama y resolver otro problema, vuelves a tu rama original. ¿Qué comando usas para aplicar los cambios guardados y, al mismo tiempo, eliminarlos de la pila (stack) de stashes?**
- a) `git stash apply`
- b) `git stash pop`
- c) `git stash drop`
- d) `git stash show`

**43. En el ecosistema de GitHub, un "Release" se basa fundamentalmente en ¿qué elemento de Git?**
- a) Un branch (rama).
- b) Un commit específico.
- c) Un tag (etiqueta), típicamente un tag anotado.
- d) Un Pull Request fusionado.

**44. Si quieres referenciar un Issue específico de un repositorio diferente pero dentro de la misma organización en un comentario, ¿cuál es la sintaxis correcta?**
- a) `#123`
- b) `org/repo#123`
- c) `repo#123`
- d) `https://github.com/issue/123`

**45. En GitHub Pages, si configuras la publicación desde GitHub Actions, ¿qué ventaja obtienes sobre la publicación desde una rama clásica (ej. `gh-pages`)?**
- a) Obtienes un certificado SSL gratuito (las ramas clásicas no lo tienen).
- b) Puedes utilizar cualquier generador de sitios estáticos (SSG) sin necesidad de hacer commit de los archivos construidos (`build`) en tu repositorio, manteniendo el historial limpio.
- c) El sitio carga un 50% más rápido por estar en una CDN diferente.
- d) Te permite crear sitios dinámicos con bases de datos MySQL.

**46. El comando `git clone --bare` se utiliza comúnmente para:**
- a) Clonar un repositorio ignorando todo su historial y trayendo solo el último commit (shallow clone).
- b) Clonar un repositorio sin directorio de trabajo (working tree), ideal para usarlo como servidor central para recibir "pushes".
- c) Clonar solo los archivos de texto, ignorando binarios para ahorrar espacio.
- d) Clonar un repositorio sin copiar la configuración de las remotos.

**47. En GitHub Actions, la expresión `${{ github.event_name }}` en un workflow disparado por un Pull Request devolverá:**
- a) `push`
- b) `pull_request`
- c) El título del Pull Request.
- d) `workflow_dispatch`

**48. ¿Para qué se utiliza comúnmente la carpeta `.github` en la raíz de un repositorio?**
- a) Para alojar el código fuente compilado por GitHub Actions.
- b) Para almacenar configuraciones específicas de la plataforma GitHub, como workflows de Actions, plantillas de Issues/PRs y CODEOWNERS.
- c) Para guardar una copia de seguridad local del wiki de GitHub.
- d) Para definir los estilos CSS personalizados de la página del repositorio.

**49. GitHub Advanced Security (GHAS) incluye varias funcionalidades Premium. ¿Cuál de las siguientes **NO** forma parte de GHAS?**
- a) Code scanning (escaneo de código con CodeQL o herramientas de terceros).
- b) Secret scanning avanzado (incluyendo custom patterns).
- c) Dependency review.
- d) Dependabot version updates (actualización automática de versiones menores/mayores de librerías).

**50. Has transferido un repositorio personal de tu cuenta (`usuarioA/repo`) a la organización de tu empresa (`empresa/repo`). ¿Qué pasa con los Pull Requests y Issues existentes, así como con las URLs de clonado locales que apuntan a `usuarioA/repo`?**
- a) Los Issues y PRs se pierden; hay que volver a crearlos. Las URLs locales dejan de funcionar.
- b) Los Issues y PRs se transfieren intactos. GitHub automáticamente redirige el tráfico de la antigua URL a la nueva, por lo que las operaciones `git fetch/push` locales seguirán funcionando.
- c) Los Issues se transfieren pero los PRs se cierran. Las URLs locales requerirán actualización inmediata.
- d) GitHub impide la transferencia si hay Pull Requests abiertos.

---

## Parte 2: Respuestas y Explicaciones

**1. b) `git add config.yml` -> `git commit --amend --no-edit`**
*Explicación:* `git commit --amend` toma el commit actual (HEAD), le añade los archivos del área de ensayo (staging) y reemplaza el commit antiguo por uno nuevo. `--no-edit` indica que se mantendrá el mensaje de commit original, haciendo la operación rápida y limpia.

**2. b) Ambos, `@global-team` (por el `.md`) y `@frontend-team` (por el `.js`).**
*Explicación:* En GitHub, si diferentes archivos modificados en un PR coinciden con diferentes reglas en `CODEOWNERS`, todos los equipos o individuos correspondientes a esas reglas serán agregados como revisores.

**3. b) `git push -u origin my-branch`**
*Explicación:* La bandera `-u` (o `--set-upstream`) le dice a Git que suba la rama actual a `origin` y establezca la relación de seguimiento (tracking). Esto permite que futuros comandos en esa rama sean simplemente `git push` o `git pull` sin tener que especificar el remoto y la rama cada vez.

**4. c) Crear nuevas ramas (branches) en el repositorio.**
*Explicación:* El rol "Triage" en GitHub está diseñado para gestionar Issues y PRs (etiquetar, asignar, cerrar, mover en proyectos), pero NO otorga permisos de escritura en el código (no permite push, crear ramas o hacer merges). Para crear ramas se necesita al menos el rol "Write".

**5. b) Se creará un único commit nuevo en `main` que contendrá todos los cambios, y los 5 commits originales desaparecerán del historial de `main`.**
*Explicación:* "Squash and merge" toma todos los cambios de los commits en la rama del PR, los comprime (squash) en un solo commit nuevo y lo añade a la rama base. El historial de la rama base queda lineal y no contiene los commits intermedios de la feature.

**6. a) Permitir el cierre automático de un Issue que se encuentra en un repositorio diferente dentro de GitHub al hacer merge del PR.**
*Explicación:* El uso de la palabra clave `Resolves` (o Fixes, Closes) seguida de la referencia cruzada `owner/repo#123` instruye a GitHub para que vincule el PR con el Issue remoto y lo cierre automáticamente cuando el PR sea fusionado, lo cual no ocurre usando solo `#123` si están en distintos repos.

**7. b) `pull_request_target` ejecuta el flujo de trabajo en el contexto (y con los secretos) del repositorio base, no desde el fork de origen.**
*Explicación:* Este es un concepto crítico de seguridad. `pull_request_target` se introdujo para permitir que los PRs desde forks tengan acceso a los secretos del repositorio base de manera segura, ya que el workflow que se ejecuta proviene del código verificado en la rama base (ej. `main`), no del código potencialmente malicioso subido al PR del fork.

**8. c) `updated:<@today-30`** (Siendo estrictos, se usan filtros como `<YYYY-MM-DD` en general, pero en Projects v2 a menudo hay helpers o se escriben queries más complejas. Asumiendo la lógica de "más antiguo que").  (*Nota del creador: en la interfaz de GitHub Search estándar, las fechas se usan en ISO o rangos. Para fines de examen, entender que GitHub permite filtrar por la propiedad `updated` y el operador `<` con una fecha/tiempo relativo es la clave*).

**9. b) `git rebase --continue`**
*Explicación:* Durante un rebase, cuando Git se detiene por conflictos, debes resolver el conflicto en el archivo, marcarlo como resuelto con `git add <archivo>`, y luego reanudar el proceso de rebase ejecutando `git rebase --continue`. No se debe hacer un nuevo commit.

**10. c) Abre un Pull Request automáticamente con la actualización a la versión mínima necesaria que parchea la vulnerabilidad.**
*Explicación:* "Dependabot security updates" actúa creando Pull Requests automáticamente en tu repositorio. Estos PRs actualizan la dependencia vulnerable a la versión más cercana que contenga el parche de seguridad, sin necesidad de intervención manual inicial.

**11. b) `git cherry-pick <commit-hash>`**
*Explicación:* `cherry-pick` toma los cambios introducidos por un commit específico (usando su hash) y los aplica en la rama actual en la que te encuentras (HEAD), creando un nuevo commit allí con un hash diferente.

**12. c) Utilizando la sintaxis `needs: build` dentro de la configuración del job `deploy`.**
*Explicación:* Por defecto, los Jobs en GitHub Actions se ejecutan en paralelo. Para crear una dependencia secuencial (que `deploy` espere a que `build` termine y sea exitoso), se usa la palabra clave `needs`.

**13. b) Secret scanning con "Push protection" (Protección de push) activado.**
*Explicación:* Secret scanning busca patrones de tokens conocidos. Si "Push protection" está habilitado, GitHub interceptará el comando `git push` a nivel del servidor, escaneará los commits entrantes y rechazará activamente el push si detecta un secreto expuesto, evitando que llegue a subirse.

**14. a) `- [ ] Tarea pendiente`**
*Explicación:* La sintaxis de GitHub Flavored Markdown (GFM) para listas de tareas (Task Lists) utiliza guiones, corchetes y espacios. `- [ ]` es una tarea incompleta, y `- [x]` es una tarea completada.

**15. b) Un archivo llamado `CNAME` que contenga únicamente tu dominio personalizado.**
*Explicación:* Para asociar un dominio personalizado, GitHub Pages requiere un archivo `CNAME` en el directorio raíz de la fuente de publicación (o configurarlo en los ajustes, lo que automáticamente crea/modifica este archivo) que contenga la URL, como `www.miproyecto.com`.

**16. b) El botón estará deshabilitado o el merge será rechazado, ya que se requiere usar "Squash and merge" o "Rebase and merge".**
*Explicación:* La protección "Require linear history" impide la creación de commits de fusión (merge commits). Solo permite estrategias de integración que mantengan la historia en una sola línea recta, es decir, Squash and merge o Rebase and merge.

**17. c) Deshace los últimos dos commits y elimina irrevocablemente los cambios de esos commits de tu directorio de trabajo y del área de ensayo.**
*Explicación:* `git reset --hard` mueve el HEAD al commit especificado (en este caso 2 commits atrás) y sobreescribe tu área de ensayo (index) y tu directorio de trabajo (working directory) para que coincidan exactamente con ese commit. Todo progreso no commiteado o de los commits reseteados se pierde.

**18. a) Los Issue Forms permiten campos de entrada estructurados, menús desplegables y validación obligatoria, mientras que los Templates son solo texto pre-rellenado.**
*Explicación:* Los Issue Forms (definidos en YAML en `.github/ISSUE_TEMPLATE/*.yml`) son una evolución de los Issue Templates clásicos en Markdown. Proveen una interfaz web interactiva rica con validaciones de campos requeridos.

**19. d) Tanto b) como c) son formas válidas, pero b) es el botón rápido dedicado.**
*Explicación:* Históricamente, se usaba un "Reverse PR" (desde el upstream al fork). Recientemente, GitHub introdujo la funcionalidad nativa de la interfaz de usuario (UI) "Sync fork" que hace un fetch y merge/rebase (fast-forward) del repositorio base (upstream) a tu fork con un solo clic.

**20. b) `git reflog`**
*Explicación:* `git reflog` (Reference logs) registra los cambios en la punta (tip) de las ramas y otras referencias en tu repositorio local. Te permite ver dónde ha estado el HEAD en el pasado, lo cual es invaluable para recuperar commits "perdidos" que ya no tienen una rama apuntándoles.

**21. b) Un asistente de programación basado en Inteligencia Artificial que sugiere código y funciones completas en tiempo real dentro del IDE.**
*Explicación:* GitHub Copilot utiliza modelos de lenguaje (LLMs) como OpenAI Codex/GPT para sugerir autocompletado de código directamente en editores como VS Code, JetBrains o Visual Studio, basándose en el contexto del archivo actual.

**22. b) `.gitignore` solo ignora archivos que no están actualmente siendo rastreados (untracked) por Git.**
*Explicación:* Si un archivo ya ha sido añadido al índice de Git en el pasado (trackeado), añadirlo al `.gitignore` no lo elimina de la vista de Git retrospectivamente. Git seguirá rastreando sus modificaciones.

**23. b) `git rm --cached secret_config.ini` -> `git commit`**
*Explicación:* El comando `git rm --cached` le dice a Git que elimine el archivo del área de ensayo y del seguimiento (lo quite del index), pero que lo mantenga intacto en el sistema de archivos local (working directory). Luego, el `.gitignore` hará efecto.

**24. a) Q&A (Preguntas y Respuestas)**
*Explicación:* Las categorías de tipo Q&A en GitHub Discussions permiten la funcionalidad específica de "Upvoting" (votos positivos) en las respuestas y la posibilidad de que el creador del post o un mantenedor marque una respuesta como la "Aceptada" (Mark as Answer).

**25. b) Usar la sintaxis de "outputs" del job (`jobs.<job_id>.outputs`) escribiendo en `$GITHUB_OUTPUT`.**
*Explicación:* En versiones modernas de GitHub Actions, para pasar datos entre Jobs (que corren en runners diferentes), debes definir `outputs` en la configuración del Job 1, escribiendo pares clave-valor en el archivo de entorno `$GITHUB_OUTPUT`, y referenciarlos en el Job 2 usando `needs.job1.outputs.variable_name`.

**26. b) En los ajustes de "Member privileges" (Privilegios de miembros) dentro de la configuración de la Organización.**
*Explicación:* Dentro de los Settings de la Organización, en el apartado "Member privileges", puedes configurar permisos base globales, incluyendo si los miembros tienen permitido crear repositorios, borrarlos, cambiar visibilidad o invitar a colaboradores externos.

**27. b) Evitan que el PR sea fusionado (merged) accidentalmente y no notifican automáticamente a los CODEOWNERS hasta que se marca como "Ready for review".**
*Explicación:* Los Draft PRs son ideales para compartir trabajo en progreso. Dejan claro que el código no está listo para ser mergeado (el botón de merge está bloqueado por defecto en la UI) y reducen el "ruido" al no solicitar revisiones formales inmediatamente.

**28. c) upstream**
*Explicación:* Por convención de la comunidad, en un flujo de forking, `origin` apunta a tu repositorio personal en GitHub (el fork), y `upstream` se configura para apuntar al repositorio central/original de donde provino el fork, para poder sincronizar cambios.

**29. b) El job que necesita el secreto debe especificar `environment: production` en su configuración.**
*Explicación:* Los Environment Secrets están vinculados a entornos específicos (ej. dev, staging, production). Para que un job en Actions pueda acceder a esos secretos de entorno, debe declarar que se ejecuta dentro de ese contexto usando la palabra clave `environment: nombre_entorno`.

**30. c) `> Texto de la cita`**
*Explicación:* El signo de mayor que `>` al inicio de una línea seguido de un espacio es la sintaxis estándar en Markdown (y GFM) para crear un bloque de cita (blockquote).

**31. c) GitHub Gist**
*Explicación:* Gist es un servicio de GitHub para compartir fragmentos de código, notas o pequeños scripts. Cada Gist es en realidad un repositorio Git completo en miniatura, lo que significa que soporta control de versiones, clones y forks.

**32. b) Si las reglas de protección de rama requieren aprobaciones, bloquea la fusión del PR hasta que el revisor original apruebe (apruebe la revisión) o la revisión sea descartada.**
*Explicación:* Cuando alguien solicita cambios (Changes requested), actúa como un veto. Si la rama destino está protegida y requiere revisiones, el PR no podrá ser fusionado hasta que el estado se cambie a "Aprobado".

**33. b) Tienes 3 commits en tu repositorio local que aún no has enviado al servidor remoto. Debes hacer `git push`.**
*Explicación:* "Ahead of" significa que tu rama local tiene trabajo avanzado (commits) que la rama remota correspondiente no tiene. Para sincronizarlos, debes subir (push) tus cambios al servidor.

**34. c) `gh repo fork owner/repo --clone`**
*Explicación:* El comando en la CLI de GitHub `gh repo fork` permite crear un fork de un repositorio. Al agregar la bandera `--clone`, automáticamente clona ese repositorio resultante (el fork) en tu máquina local.

**35. c) Usar `git commit --amend` si es el último commit, modificando el archivo y el índice sin la contraseña.**
*Explicación:* Dado que no has hecho push al repositorio remoto, la historia local puede ser rescrita sin afectar a otros. Eliminas la contraseña en el archivo, haces `git add`, y usas `git commit --amend` para reemplazar el commit que tenía el error.

**36. b) Repository Templates (marcar el repositorio como "Template repository").**
*Explicación:* Al activar la opción "Template repository" en los Settings de un repositorio, permites a otros (y a ti mismo) usar un botón de "Use this template" para crear un repositorio nuevo limpio copiando los archivos y la estructura base, pero sin copiar el historial de commits.

**37. b) Se cancelan inmediatamente porque la opción predeterminada `fail-fast` está establecida en `true`.**
*Explicación:* En GitHub Actions, por defecto, una matriz (matrix) tiene `fail-fast: true`. Esto significa que si un solo job dentro de la matriz falla, la ejecución completa de la matriz se detiene y todos los jobs restantes (en ejecución o pendientes) son cancelados para ahorrar recursos.

**38. b) Mantiene los 10 commits originales en la historia y crea 1 commit extra de merge que une las dos líneas temporales, conservando los hashes de los 10 commits.**
*Explicación:* El merge estándar ("Create a merge commit") en GitHub añade todos los commits de la rama característica a la rama principal (main) tal y como estaban, y adicionalmente crea un commit de fusión (Merge commit) con dos padres, representando el punto de integración.

**39. c) Admin**
*Explicación:* El rol de "Admin" (Administrador) en un repositorio es necesario para gestionar los accesos, agregar colaboradores, asignar permisos a Equipos (Teams) o cambiar configuraciones críticas como reglas de protección de ramas o visibilidad del repo. Maintainers pueden gestionar el contenido y los settings, pero no el acceso general y borrado total.

**40. b) Utilizar un Issue Form creado con un archivo YAML (ej. `bug_report.yml`) definiendo los campos como requeridos.**
*Explicación:* Los Issue Forms (YAML) en GitHub permiten definir elementos de UI como cajas de texto, menús desplegables y casillas de verificación. Se puede definir `validations: required: true` en ciertos campos, obligando al usuario a proveer esa información antes de que GitHub le permita abrir el Issue.

**41. a) `git fetch` descarga los cambios del remoto a tus ramas de seguimiento (tracking branches) locales pero no modifica tu espacio de trabajo (working directory). `git pull` hace un `fetch` e inmediatamente intenta fusionar (merge) esos cambios en tu rama actual.**
*Explicación:* `git pull` es funcionalmente una combinación de `git fetch` seguido por `git merge` (o `git rebase` dependiendo de la configuración). `fetch` es la acción segura para ver qué hay nuevo sin alterar tu trabajo en curso.

**42. b) `git stash pop`**
*Explicación:* `git stash pop` aplica el último cambio guardado (stash superior de la pila) a tu directorio de trabajo actual y, si se aplica sin conflictos críticos, lo elimina (drop) de la lista de stashes. `apply` lo aplicaría pero lo mantendría en la lista.

**43. c) Un tag (etiqueta), típicamente un tag anotado.**
*Explicación:* Los GitHub Releases están indisolublemente unidos a los Git Tags. Cuando creas un Release en GitHub, internamente se está creando y apuntando a un Tag (como `v1.0.0`) en el historial de commits.

**44. b) `org/repo#123`**
*Explicación:* Cuando trabajas dentro de la misma organización, puedes hacer referencias directas a issues en otros repositorios usando la sintaxis abreviada `repositorio#numero` (si estás en la misma org) o más explícitamente `owner/repo#123`. Simplemente `#123` referenciaría al issue en el repositorio local.

**45. b) Puedes utilizar cualquier generador de sitios estáticos (SSG) sin necesidad de hacer commit de los archivos construidos (`build`) en tu repositorio, manteniendo el historial limpio.**
*Explicación:* Históricamente, alojar en la rama `gh-pages` implicaba a menudo commitear el código fuente compilado (HTML/CSS/JS minificado). Usar GitHub Actions permite mantener tu rama `main` solo con código fuente base (React, Vue, Hugo, etc.), el Action realiza la compilación en un runner y sube el artifact directamente al servicio de Pages sin ensuciar la historia de Git.

**46. b) Clonar un repositorio sin directorio de trabajo (working tree), ideal para usarlo como servidor central para recibir "pushes".**
*Explicación:* Un repositorio `bare` solo contiene el directorio `.git` (objetos, referencias). No tiene una copia de trabajo (los archivos legibles). Se usa fundamentalmente en servidores centralizados que actúan como "origin" remoto a donde los desarrolladores envían su código con `git push`.

**47. b) `pull_request`**
*Explicación:* La expresión de contexto `github.event_name` devuelve el nombre del webhook de evento que desencadenó la ejecución del workflow de GitHub Actions. Si el trigger fue `on: pull_request`, devolverá el string `"pull_request"`.

**48. b) Para almacenar configuraciones específicas de la plataforma GitHub, como workflows de Actions, plantillas de Issues/PRs y CODEOWNERS.**
*Explicación:* El directorio `.github/` es la convención estándar adoptada por GitHub para alojar archivos de configuración nativos de la plataforma, separando la lógica del producto final de las configuraciones de automatización y comunidad (como `.github/workflows/`, `.github/ISSUE_TEMPLATE/`, `CODEOWNERS`).

**49. d) Dependabot version updates (actualización automática de versiones menores/mayores de librerías).**
*Explicación:* "Dependabot version updates" (mantener las dependencias actualizadas incluso si no son vulnerables) y "Dependabot alerts" son funcionalidades gratuitas en todos los repositorios. GHAS es un producto de pago (Premium para repos privados) que añade Code Scanning, Secret Scanning custom, y Dependency review policies.

**50. b) Los Issues y PRs se transfieren intactos. GitHub automáticamente redirige el tráfico de la antigua URL a la nueva, por lo que las operaciones `git fetch/push` locales seguirán funcionando.**
*Explicación:* GitHub gestiona las transferencias de repositorio de manera muy robusta. Todos los metadatos (issues, PRs, wikis, stars) viajan con el repositorio. Además, GitHub configura redirecciones automáticas a nivel web y Git a nivel de servidor, por lo que los clones locales existentes que apunten a la vieja URL no se romperán (aunque es buena práctica actualizar el `remote`).
