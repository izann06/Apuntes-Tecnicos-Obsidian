#github #open-source #comunidad #gh-foundations

> [!info] Navegación
> ◀ [[D6 - Seguridad y Administración]] · ▶ [[🎓 Índice - GitHub Foundations]]

---

# Dominio 7 — Beneficios de la Comunidad GitHub

## 7.1 Open Source

### ¿Qué es el Open Source?

El **Open Source** (Código Abierto) es un modelo de desarrollo de software donde el código fuente es **público, libre de ver, modificar y distribuir** bajo los términos de una licencia específica.

**Beneficios del Open Source:**

- **Transparencia:** Cualquiera puede auditar el código.
- **Colaboración global:** Desarrolladores de todo el mundo pueden contribuir.
- **Velocidad de innovación:** Más ojos detectan más bugs y proponen más mejoras.
- **Reducción de costes:** No hay que pagar licencias de software.
- **Comunidad:** Genera ecosistemas de usuarios y contribuidores muy activos.

### Cómo GitHub impulsa el Open Source

GitHub es el hogar de la mayor comunidad de Open Source del mundo. Lo hace posible con:

- Repositorios públicos gratuitos.
- Herramientas de colaboración (Issues, PRs, Discussions).
- GitHub Actions para CI/CD gratuito en repos públicos.
- El sistema de **Stars** y **Forks** que facilita el descubrimiento.

---

## 7.2 InnerSource

**InnerSource** es la práctica de aplicar **las metodologías y cultura del Open Source dentro de una empresa privada**.

En lugar de que los equipos trabajen en silos con código inaccesible para otros departamentos, InnerSource promueve que los equipos internos puedan ver, proponer cambios y contribuir al código de otros equipos, usando las mismas herramientas (Issues, PRs, Code Reviews) que en Open Source.

### InnerSource vs. Open Source

| | InnerSource | Open Source |
| :--- | :--- | :--- |
| **Visibilidad del código** | Interna (dentro de la empresa) | Pública (todo el mundo) |
| **¿Quién contribuye?** | Empleados de la organización | Cualquier persona |
| **Licencia** | Propietaria / Interna | Licencia Open Source (MIT, GPL...) |
| **Objetivo** | Mejorar colaboración interna | Beneficiar a la comunidad global |

---

## 7.3 Forking (Bifurcación)

**Forkear** un repositorio es crear una copia completa de ese repositorio bajo **tu propia cuenta de GitHub**. Es independiente del original, pero mantiene una referencia a él.

**Casos de uso del Fork:**

1. **Contribuir a Open Source:** Forkeas el repo, haces tus cambios en tu fork, y luego abres un PR al repositorio original.
2. **Usar un proyecto como base:** Quieres usar el código de alguien como punto de partida para tu propio proyecto.
3. **Experimentar:** Probar cambios drásticos sin miedo a romper el original.

```
Repositorio Original (upstream) ──fork──► Tu Fork (origin)
                                               │
                                           tus commits
                                               │
                                    ──Pull Request──► Repositorio Original
```

---

## 7.4 Descubrimiento en GitHub

### Repositorios Descubribles

Para que un repositorio sea fácil de encontrar:

- **Descripción clara** en la parte superior del repo.
- **Topics (Temas):** Etiquetas de búsqueda (ej. `python`, `machine-learning`, `api`). Se añaden desde `About > Topics`.
- **README.md completo.**
- **Licencia definida.**
- **Repositorio público** (los privados no aparecen en búsquedas).

### Seguir Personas y Organizaciones

- **Seguir a personas:** Recibes notificaciones de su actividad pública (repos que estrella, proyectos en los que contribuye). Te ayuda a descubrir proyectos interesantes en su comunidad.
- **Seguir organizaciones:** Recibes notificaciones sobre sus anuncios y nuevos repositorios.

---

## 7.5 GitHub Sponsors

**GitHub Sponsors** es un programa que permite financiar económicamente a desarrolladores y organizaciones Open Source que crean software que usas.

- Los patrocinadores (sponsors) pagan mensualmente a los creadores.
- GitHub no cobra comisión en el primer año y solo una pequeña comisión después.
- Para recibir sponsors, el desarrollador debe ser aprobado en el programa.

---

## 7.6 GitHub Marketplace

El **GitHub Marketplace** es una tienda integrada donde puedes encontrar y instalar **herramientas y servicios de terceros** que se integran con GitHub.

- Hay herramientas de CI/CD, monitorización de código, gestión de proyectos, seguridad, etc.
- Algunas son gratuitas, otras de pago.
- Se instalan directamente en tus repositorios u organización con los permisos que eliges.

---

## 7.7 Organizaciones de GitHub

### Miembros, Equipos y Roles

**Organización:** Una cuenta colectiva en GitHub que permite a grupos de personas colaborar en múltiples proyectos.

**Miembros (Members):** Usuarios que pertenecen a la organización. Pueden ser:

- **Owners:** Control total sobre la organización (facturación, miembros, seguridad).
- **Members:** Acceso estándar según los permisos que se les asigne.

**Equipos (Teams):** Subgrupos dentro de la organización. Los permisos se asignan al equipo, no individualmente. Ej: `@mi-empresa/backend`, `@mi-empresa/devops`.

### Gestión de la Organización

- **Configuración global:** Desde `github.com/organizations/nombre-org/settings`.
- **Roles de repositorio:** Los equipos se asignan a repos con niveles Read/Triage/Write/Maintain/Admin.
- **Visibilidad de miembros:** Puedes hacer que la lista de miembros sea pública o solo visible para otros miembros.

---

## 7.8 Templates de Issues y PRs (en contexto de comunidad)

### ¿Cuándo usar Issue Templates?

- Cuando recibes muchos issues mal formateados o sin la información necesaria para reproducir un bug.
- En proyectos Open Source con muchos contribuidores externos.
- Cuando quieres diferenciar entre "reporte de bug", "petición de feature" y "pregunta".

### ¿Cuándo usar Pull Request Templates?

- Cuando quieres que todos los PRs incluyan una checklist estándar: "¿Has añadido tests? ¿Has actualizado la documentación? ¿Los CI checks pasan?".
- En equipos grandes donde la revisión de código es un proceso formal.
