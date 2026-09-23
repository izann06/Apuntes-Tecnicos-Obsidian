#github #gh-foundations #modulo-5 #gists #wikis #discussions

> [!info] Navegación
> ◀ [[06 - Markdown y Búsqueda Avanzada]] · ▶ [[01 - GitHub Projects y Visualización]]

---

# 07 — Gists, Wikis y Discussions

> **Resumen ejecutivo:**
> 1. Los **Gists** son repositorios mini para compartir snippets de código o texto con un enlace.
> 2. Las **Wikis** son páginas de documentación extendida vinculadas a un repositorio.
> 3. Las **Discussions** son el foro de la comunidad del repo: debate abierto, Q&A, ideas (no bugs concretos).

---

## 1. Gists — Compartir Código al Vuelo

Un **Gist** es como un repositorio Git extremadamente simplificado, pensado para compartir **fragmentos de código, configuraciones o notas de texto** con un enlace directo. Se accede en `gist.github.com`.

### ¿Cuándo usar un Gist en vez de un repositorio?

| Situación | ¿Qué usar? |
|:---|:---|
| Quieres compartir un script corto de Python con un compañero | ✅ Gist |
| Quieres publicar tu configuración de `.vimrc` o `.zshrc` | ✅ Gist |
| Tienes un proyecto con múltiples archivos, carpetas y estructura | ✅ Repositorio |
| Quieres hacer un tutorial con varios pasos | ✅ Repositorio o Wiki |

### Tipos de Gist

| Tipo | ¿Quién puede verlo? | ¿Aparece en búsquedas? |
|:---|:---|:---:|
| **Public (Público)** | Cualquier persona de internet | ✅ Sí |
| **Secret (Secreto)** | Solo quien tenga el enlace exacto | ❌ No |

> [!WARNING] "Secret" no es lo mismo que "Privado"
> Un Gist **secreto** NO es privado. Si alguien tiene el enlace, puede verlo sin estar logueado. Es simplemente "no indexado" en búsquedas. Para código sensible, usa un repo privado.

### Qué puedes hacer con un Gist

- **Versionar:** Como es un mini repositorio Git, puedes ver el historial de cambios.
- **Forkear:** Cualquiera puede hacer fork de tu Gist y modificarlo.
- **Comentar:** La gente puede dejar comentarios.
- **Embeber:** Puedes pegar el código de un Gist en cualquier web con un `<script>` tag.
- **Clonar:** `git clone https://gist.github.com/HASH.git` para trabajar con él localmente.

---

## 2. Wikis — Documentación Extendida del Repositorio

La **Wiki** de un repositorio es un espacio dedicado para documentación larga y estructurada, separada del código. Es como tener un mini-Wikipedia para tu proyecto.

### ¿Cuándo usar Wiki en vez de README?

| | README.md | Wiki |
|:---|:---|:---|
| **Contenido ideal** | Introducción rápida, instalación básica, badge de estado | Guías detalladas, arquitectura, referencia de API, FAQ |
| **Edición** | Igual que código, requiere Pull Request | Directamente en GitHub, sin commit al repo principal |
| **Visibilidad** | Siempre visible en la portada del repo | Pestaña aparte, a un clic |
| **Control de versiones** | ✅ Historial de Git completo | ✅ Historial básico (es un repo Git separado) |

### Cómo activar y crear páginas

1. Ve a tu repositorio → pestaña **Wiki**.
2. Si no está habilitada: `Settings > Features > Wikis` → activar.
3. Haz clic en **"Create the first page"**.
4. Escribe en Markdown, pulsa **"Save Page"**.

> [!WARNING] Las Wikis se pueden desactivar
> El propietario del repo puede desactivar la Wiki en `Settings > Features > Wikis`. Si el examen pregunta si las Wikis son permanentes, la respuesta es NO: pueden desactivarse.

### Clonar la Wiki para editarla localmente

Internamente, la Wiki es un repositorio Git independiente. Puedes clonarla:

```bash
git clone https://github.com/usuario/mi-repo.wiki.git
cd mi-repo.wiki
# Edita los .md, haz commit y push
```

---

## 3. Discussions — El Foro de la Comunidad

Las **Discussions** son el espacio de conversación abierta de un repositorio. Son distintas a los Issues: mientras que un Issue es para algo concreto y accionable ("hay un bug"), una Discussion es para conversaciones más amplias.

### Issues vs. Discussions

| | Issue | Discussion |
|:---|:---|:---|
| **¿Para qué?** | Bug concreto, tarea accionable, petición específica | Preguntas abiertas, ideas, debate, anuncios |
| **¿Se cierra?** | ✅ Se cierra cuando se resuelve | ❌ NO se cierra. Se **"marca como respondida"** (Q&A) |
| **¿Se convierte?** | — | ✅ Una Discussion se puede convertir en Issue |
| **¿Tiene asignados?** | ✅ Assignees, Labels, Milestones | ❌ Solo categorías |

> [!IMPORTANT] Dato de examen clave
> Las Discussions **NO se cierran**. En la categoría **Q&A**, el autor puede **marcar una respuesta como la correcta** (como en Stack Overflow). Es la única forma de "resolver" una Discussion.

### Categorías de Discussions

GitHub permite crear categorías personalizadas. Las predefinidas son:

| Categoría | Uso típico |
|:---|:---|
| **Announcements** | Solo admins pueden publicar. Para noticias oficiales del proyecto. |
| **General** | Conversaciones generales sobre el proyecto. |
| **Ideas** | Proponer nuevas funciones o mejoras. |
| **Q&A** | Preguntas y respuestas. La respuesta correcta se puede marcar. |
| **Show and tell** | Mostrar proyectos o usos creativos que la comunidad ha hecho. |

### Cómo activar Discussions

`Settings > Features > Discussions` → activar el checkbox.

### Stars ⭐, Watchers 👁️ y Forks 🍴

Tres métricas que ves en la portada de todo repositorio público:

| Métrica | ¿Qué significa? | ¿Se reciben notificaciones? |
|:---|:---|:---:|
| **⭐ Stars** | Al usuario le gusta el proyecto / lo guarda como favorito | ❌ No |
| **👁️ Watchers** | El usuario quiere recibir notificaciones de toda la actividad del repo | ✅ Sí |
| **🍴 Forks** | Número de copias independientes que se han hecho del repo | ❌ No |

> [!TIP] Exam Tip — Stars vs Watchers
> **Starring** un repo es como darle un "me gusta" en redes sociales: lo guardas para volver. **Watching** un repo es suscribirse a todas sus notificaciones (issues, PRs, commits, comentarios). Son cosas muy distintas.
