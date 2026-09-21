#github #gh-foundations #modulo-5 #repositorios #readme #codeowners #licencias

> [!info] Navegación
> ◀ [[03 - Secret Scanning y Políticas]] · ▶ [[02 - Issues y Gestión de Incidencias]]

---

# 01 — Repositorios y Documentación

> **Resumen ejecutivo:**
> 1. Los repos pueden ser **Public**, **Private** o **Internal** (solo en Enterprise).
> 2. Un buen repo tiene `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODEOWNERS` y `.gitignore`.
> 3. El `CODEOWNERS` asigna automáticamente revisores según los archivos modificados en un PR.

---

## 1. Visibilidad de Repositorios

| Visibilidad | ¿Quién puede verlo? | Disponible en |
| :--- | :--- | :--- |
| **Public** | Cualquier persona en internet | Todos los planes |
| **Private** | Solo el propietario y colaboradores invitados | Todos los planes |
| **Internal** | Todos los miembros de la organización Enterprise (automáticamente) | Solo Enterprise |

> [!WARNING] Pregunta frecuente de examen
> **Internal** NO es lo mismo que Private. En un repo Private, debes invitar a cada colaborador uno a uno. En un repo Internal, **todos los miembros de la organización** tienen acceso de lectura automáticamente, sin invitación.

---

## 2. Archivos de Documentación Estándar

| Archivo | Propósito | ¿Dónde se pone? |
| :--- | :--- | :--- |
| `README.md` | Descripción del proyecto, instrucciones de instalación, uso | Raíz del repo |
| `LICENSE` | Términos legales de uso y distribución del código | Raíz del repo |
| `CONTRIBUTING.md` | Guía para contribuidores: cómo reportar bugs, cómo hacer PRs | Raíz o `.github/` |
| `CODE_OF_CONDUCT.md` | Normas de comportamiento de la comunidad | Raíz o `.github/` |
| `SECURITY.md` | Cómo reportar vulnerabilidades de seguridad | Raíz o `.github/` |
| `CODEOWNERS` | Asigna revisores automáticos por archivo/carpeta | `.github/CODEOWNERS` |
| `.gitignore` | Archivos que Git debe ignorar | Raíz del repo |

### El README.md — La Puerta de Entrada

Un buen README debe incluir:

- **Nombre y descripción** del proyecto.
- **Badges / Insignias** (estado del build, cobertura de tests, licencia).
- **Instrucciones de instalación** paso a paso.
- **Ejemplos de uso** con código.
- **Cómo contribuir** (o enlace a `CONTRIBUTING.md`).
- **Licencia** (o enlace a `LICENSE`).

### GitHub Markdown (GFM)

GitHub usa **GitHub Flavored Markdown**, que extiende Markdown estándar con:

- Tablas, listas de tareas (`- [x]`), tachado (`~~texto~~`).
- Autoenlace de URLs, menciones (`@usuario`), referencias (`#123`).
- Bloques de código con resaltado de sintaxis.
- Emojis (`:rocket:` → 🚀).

---

## 3. CODEOWNERS

El archivo `CODEOWNERS` (ubicado en `.github/CODEOWNERS`) define quién es automáticamente solicitado como **revisor** cuando se abre un PR que modifica ciertos archivos.

```bash
# .github/CODEOWNERS

# Todo el repositorio: el equipo lead revisa todo
* @my-org/tech-leads

# Los archivos JavaScript los revisa el equipo frontend
*.js @my-org/frontend-team

# La carpeta /docs la revisa Izan
/docs @izanm

# Los archivos de configuración de CI los revisa DevOps
/.github/workflows/ @my-org/devops
```

> [!TIP] Exam Tip — CODEOWNERS + Branch Protection
> La combinación más poderosa: activas Branch Protection con "Require review from Code Owners" y defines el `CODEOWNERS`. Así, nadie puede fusionar cambios en `/docs` sin que `@izanm` lo apruebe, ni cambios en `*.js` sin la aprobación del equipo frontend.

---

## 4. Licencias

| Licencia | ¿Permite uso comercial? | ¿Obliga a compartir código? | Uso típico |
| :--- | :--- | :---: | :--- |
| **MIT** | ✅ Sí | ❌ No | La más permisiva. Haz lo que quieras. |
| **Apache 2.0** | ✅ Sí | ❌ No | Como MIT pero con protección de patentes. |
| **GPL v3** | ✅ Sí | ✅ Sí (copyleft) | Si usas mi código, el tuyo también debe ser GPL. |
| **Sin licencia** | ⚠️ Ambiguo | — | Sin licencia = copyright por defecto. Nadie puede usar tu código legalmente. |

---

## 5. Zona de Peligro (Danger Zone)

En `Settings > Danger Zone` de un repositorio:

- **Transfer ownership:** Transferir la propiedad del repo a otro usuario u organización.
- **Change visibility:** Cambiar entre Public / Private / Internal.
- **Archive repository:** Hacer el repo de solo lectura (nadie puede hacer push, abrir issues ni PRs).
- **Delete repository:** Borrado permanente e irreversible.

> [!WARNING] Solo el Owner puede acceder a la Danger Zone
> Estas acciones requieren permisos de **Admin** en el repositorio.
