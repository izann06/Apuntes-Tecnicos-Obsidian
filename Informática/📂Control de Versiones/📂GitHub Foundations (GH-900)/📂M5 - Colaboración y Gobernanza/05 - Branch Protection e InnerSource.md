#github #gh-foundations #modulo-5 #branch-protection #innersource

> [!info] Navegación
> ◀ [[04 - Pull Requests y Code Review]] · ▶ [[01 - GitHub Projects y Visualización]]

---

# 05 — Branch Protection e InnerSource

> **Resumen ejecutivo:**
> 1. Las **Branch Protection Rules** protegen `main` de pushes directos y exigen PRs con aprobaciones.
> 2. Se pueden requerir **checks de CI verdes** antes de fusionar y **firma de commits**.
> 3. **InnerSource** aplica prácticas de Open Source dentro de empresas privadas.

---

## 1. Branch Protection Rules

Las **Branch Protection Rules** son reglas que se aplican a ramas específicas (normalmente `main`) para prevenir cambios no autorizados.

Se configuran en `Settings > Branches > Branch protection rules > Add rule`.

### Reglas Disponibles

| Regla | Efecto |
| :--- | :--- |
| **Require a pull request before merging** | Nadie puede hacer push directo a `main`. Obligatorio abrir un PR. |
| **Require approvals** | El PR necesita un número mínimo de aprobaciones (1, 2, 3...) antes de fusionarse. |
| **Dismiss stale pull request approvals** | Si se hacen nuevos commits después de la aprobación, la aprobación se invalida y hay que re-aprobar. |
| **Require review from Code Owners** | Los propietarios definidos en `CODEOWNERS` deben aprobar obligatoriamente. |
| **Require status checks to pass** | Los checks de CI/CD (GitHub Actions) deben pasar antes de permitir el merge. |
| **Require signed commits** | Solo se permiten commits firmados (GPG / SSH signing). |
| **Require linear history** | Solo permite merge por Squash o Rebase (no merge commits). |
| **Restrict who can push** | Solo ciertos usuarios/equipos pueden hacer push a la rama (bypass). |
| **Do not allow bypassing** | Ni siquiera los admins pueden saltarse las reglas. |
| **Restrict deletions** | Impide que alguien borre la rama protegida. |

> [!WARNING] Pregunta frecuente de examen
> El examen puede preguntar qué regla impide que un desarrollador haga push directamente a `main`. La respuesta es **"Require a pull request before merging"**. Con esta regla activada, la única forma de añadir código a `main` es mediante un PR aprobado.

### Ejemplo: Configuración típica para `main`

```
✅ Require a pull request before merging
  ✅ Require at least 2 approvals
  ✅ Dismiss stale approvals when new commits are pushed
  ✅ Require review from Code Owners
✅ Require status checks to pass before merging
  ✅ Require CI/build to pass
✅ Restrict deletions
```

---

## 2. Rulesets (Alternativa moderna a Branch Protection)

GitHub ha introducido **Rulesets** como una alternativa más flexible a las Branch Protection Rules:

| Característica | Branch Protection Rules | Rulesets |
| :--- | :--- | :--- |
| **Alcance** | Una rama a la vez | Múltiples ramas/tags con patrones |
| **Disponibilidad** | Todos los planes | GitHub Team / Enterprise |
| **Capas** | Una regla por rama | Múltiples rulesets se pueden apilar |
| **Importar/Exportar** | ❌ | ✅ JSON |

---

## 3. InnerSource

**InnerSource** es la práctica de aplicar las metodologías y cultura del **Open Source** dentro de los límites de una empresa privada.

### ¿Qué problema resuelve?

En empresas grandes, los equipos trabajan en silos: el equipo A no puede ver ni contribuir al código del equipo B. InnerSource rompe esos silos usando las mismas herramientas de GitHub.

### InnerSource vs. Open Source

| | InnerSource | Open Source |
| :--- | :--- | :--- |
| **Visibilidad** | Interna (dentro de la empresa) | Pública (todo el mundo) |
| **Contribuidores** | Empleados de la organización | Cualquier persona |
| **Licencia** | Propietaria | Open Source (MIT, GPL...) |
| **Repos** | Visibilidad **Internal** en GitHub | Visibilidad **Public** |
| **Objetivo** | Reutilización de código y colaboración interna | Beneficiar a la comunidad |

### Cómo se implementa en GitHub

1. **Repos Internal:** Visibles para todos los miembros de la organización.
2. **CONTRIBUTING.md:** Guía clara para que cualquier empleado sepa cómo contribuir.
3. **CODEOWNERS:** Define quién aprueba cambios en cada parte del código.
4. **Issues y PRs:** El mismo flujo que en Open Source, pero dentro de la empresa.
5. **Templates de repo:** Repositorios plantilla para que los equipos creen proyectos con la estructura estándar.

> [!TIP] Exam Tip — InnerSource
> El examen puede preguntar qué tipo de visibilidad de repositorio se recomienda para InnerSource. La respuesta es **Internal**, porque permite que todos los miembros de la organización vean y contribuyan sin necesidad de invitación individual.
