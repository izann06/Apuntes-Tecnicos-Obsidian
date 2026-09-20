#github #issues #pull-requests #discussions #gh-foundations

> [!info] Navegación
> ◀ [[D2 - Trabajando con Repositorios]] · ▶ [[D4 - Desarrollo Moderno (Actions, Copilot, Codespaces)]]

---

# Dominio 3 — Características de Colaboración

## 3.1 Issues

Los **Issues** son el sistema de seguimiento de trabajo (tickets) de GitHub. Se usan para reportar bugs, proponer funcionalidades, o hacer preguntas.

### Crear un Issue
Ve a la pestaña **"Issues"** del repositorio → "New issue". Puedes asignar:
- **Título y descripción** (en Markdown).
- **Assignees:** Personas responsables de resolverlo.
- **Labels:** Etiquetas para categorizar (ej. `bug`, `enhancement`, `documentation`).
- **Milestone:** Hito al que pertenece.
- **Projects:** Proyecto al que se asocia.

### Diferencias: Issue vs. Discussion vs. Pull Request

| | Issue | Discussion | Pull Request |
| :--- | :--- | :--- | :--- |
| **¿Para qué?** | Reportar bugs o tareas | Conversaciones abiertas, ideas, Q&A | Proponer cambios de código |
| **¿Tiene código?** | No necesariamente | No | Sí (siempre) |
| **¿Se cierra?** | Sí, al resolverse | Se puede marcar respuesta | Sí, al fusionarse o rechazarse |

### Crear una Rama desde un Issue
Dentro de un issue, en el panel derecho, hay la opción **"Create a branch"**. Esto crea automáticamente una rama vinculada al issue, facilitando el seguimiento.

### Buscar y Filtrar Issues
Puedes usar filtros avanzados en la barra de búsqueda:
```
is:open is:issue assignee:izanm label:bug
is:closed author:izanm
is:issue mentions:izanm
```

### Fijar un Issue (Pin)
Los issues más importantes pueden **fijarse** en la parte superior de la lista de issues del repositorio. Solo admite hasta **3 issues fijados**.

### Gestión Básica de Issues
- **Cerrar:** Marca el issue como resuelto. Se puede hacer desde un commit con keywords.
- **Reabrir:** Si el bug vuelve a aparecer, se puede reabrir.
- **Transferir:** Mover un issue a otro repositorio.

### Keywords para Cerrar Issues Automáticamente
Al hacer un commit o PR, si incluyes estas palabras seguidas del número de issue, GitHub lo cierra automáticamente al fusionar:
```
Closes #42
Fixes #42
Resolves #42
```

### Issue Templates vs. Issue Forms
- **Issue Templates:** Archivos Markdown en `.github/ISSUE_TEMPLATE/` que prerellenan el cuerpo del issue.
- **Issue Forms:** Formularios estructurados con campos específicos (dropdowns, checkboxes). Más controlados.

---

## 3.2 Pull Requests (PRs)

Un **Pull Request** es una propuesta formal para fusionar los cambios de una rama en otra. Es el corazón del flujo de trabajo colaborativo en GitHub.

### Anatomía de un PR
- **Base branch:** La rama destino (normalmente `main`). Es donde quieres fusionar.
- **Compare branch:** La rama con tus cambios (ej. `feature/login`).

### Pestaña del PR
| Pestaña | Contenido |
| :--- | :--- |
| **Conversation** | Comentarios generales del PR, historial de revisiones y la actividad |
| **Commits** | Lista de todos los commits incluidos en el PR |
| **Checks** | Resultados de las GitHub Actions/CI que se ejecutan automáticamente |
| **Files changed** | Diferencia (diff) de todos los archivos modificados |

### Estados de un PR
- **Open (Draft):** Borrador. Indica que el trabajo no está listo para revisión. No se puede fusionar.
- **Open (Ready for review):** Listo para que los revisores lo vean.
- **Merged:** Fusionado con la rama base. Acción irreversible.
- **Closed:** Cerrado sin fusionar (el trabajo fue descartado).

### Draft Pull Requests
Los **Draft PRs** se usan para compartir trabajo en progreso sin pedir revisión formal. Comunica "esto existe, puedes verlo, pero aún no está listo". Para convertirlo en PR listo, haz clic en "Ready for review".

### Opciones de Code Review
Al revisar un PR, un revisor puede elegir:
- **Comment:** Deja comentarios sin aprobar ni rechazar.
- **Approve:** Aprueba los cambios. Si el repo lo requiere, el PR ya puede fusionarse.
- **Request Changes:** Rechaza la fusión hasta que el autor corrija los problemas señalados.
- **Suggested Changes:** El revisor propone cambios de código directamente en el diff. El autor puede aceptarlos con un clic ("Apply suggestion").

### Enlazar actividad dentro de un PR
Puedes referenciar issues, commits, otros PRs o mencionar usuarios en los comentarios:
```
#42          → Referencia al issue o PR número 42
@izanm       → Menciona a un usuario
SHA-hash     → Referencia a un commit específico
```

---

## 3.3 Discussions

Las **Discussions** son un foro integrado en el repositorio para conversaciones más abiertas que no son bugs ni tareas concretas.

### Categorías disponibles
- **Announcements:** Noticias del proyecto (solo mantenedores pueden crear).
- **Ideas:** Propuestas de funcionalidades.
- **Polls:** Encuestas a la comunidad.
- **Q&A:** Preguntas y respuestas. Permite marcar un comentario como la respuesta correcta.
- **Show and tell:** Para que la comunidad muestre sus proyectos.

### Acciones con Discussions
- **Marcar respuesta:** En categoría Q&A, el autor o un mantenedor puede marcar un comentario como la respuesta oficial.
- **Convertir a Issue:** Si una discusión deriva en una tarea concreta, se puede convertir directamente en un Issue.
- **Fijar una Discussion:** Similar a los issues, se pueden fijar hasta 4 discussions.

---

## 3.4 Notificaciones

### Gestionar Suscripciones
Puedes controlar cuándo recibes notificaciones:
- **Watching:** Recibe notificaciones de toda la actividad del repositorio.
- **Participating:** Solo cuando participas (comentas, te mencionan, se te asigna).
- **Ignoring:** No recibes ninguna notificación del repositorio.

### Suscribirse a un hilo
Puedes suscribirte a un issue o PR específico sin seguir todo el repositorio. Botón "Subscribe" en el panel derecho.

### Encontrar menciones
En la página de notificaciones, usa el filtro `@mention` para ver todos los hilos donde alguien te ha mencionado directamente.

### Opciones de configuración
- **GitHub.com:** Configurable en `Settings > Notifications`.
- **Email vs. Web:** Puedes elegir recibir por email, por la web o ambos.
- **Scheduled reminders:** Envía resúmenes periódicos de notificaciones a Slack.

---

## 3.5 Gists, Wikis y GitHub Pages

### GitHub Gist
Un **Gist** es un repositorio Git simplificado para compartir fragmentos de código o notas. Puede ser **público** (aparece en búsquedas) o **secreto** (solo accesible con el enlace directo).

- **Crear:** Ir a [gist.github.com](https://gist.github.com).
- **Forkear un Gist:** Como con los repos, puedes crear tu propia copia para modificarla.
- **Clonar un Gist:** Es un repo Git normal, puedes clonarlo con `git clone`.

### GitHub Wiki
Cada repositorio puede tener su propio **Wiki**, que es un sistema de documentación colaborativa integrado.
- **Crear/Editar/Borrar páginas:** Directamente desde la interfaz web del wiki.
- **Visibilidad:** En repos públicos, el wiki es público. En repos privados, es privado. Pero **no existe la opción de hacer el wiki privado dentro de un repo público**.

### GitHub Pages
**GitHub Pages** es un servicio de alojamiento web estático directamente desde un repositorio.
- Puedes publicar tu web desde la rama `main`, desde la carpeta `/docs`, o desde una rama `gh-pages`.
- La URL por defecto es `https://usuario.github.io/nombre-del-repositorio`.
- Acepta HTML/CSS/JS puros o generadores de sitios estáticos como Jekyll o (como tú usas) **Quartz**.
