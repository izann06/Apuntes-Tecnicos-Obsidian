#github #seguridad #administracion #2fa #gh-foundations

> [!info] Navegación
> ◀ [[D5 - Gestión de Proyectos]] · ▶ [[D7 - Comunidad y Open Source]]

---

# Dominio 6 — Privacidad, Seguridad y Administración

## 6.1 Autenticación y Seguridad

### Autenticación en Dos Factores (2FA)

La **2FA** añade una segunda capa de seguridad a tu cuenta de GitHub. Aunque alguien obtenga tu contraseña, no podrá acceder sin el segundo factor.

**Métodos de 2FA en GitHub:**

- **Authenticator App:** Apps como Google Authenticator, Authy (generan un código TOTP de 6 dígitos que cambia cada 30 segundos). **Recomendado.**
- **SMS:** Código enviado por mensaje de texto. **Menos seguro** (vulnerable a SIM swapping).
- **Security Keys (Hardware):** Llaves físicas como YubiKey. El método más seguro.
- **GitHub Mobile:** Aprueba el acceso desde la app móvil.

> [!important] GitHub requiere 2FA cada vez más
> GitHub ha empezado a exigir 2FA a los contribuidores activos. Es una buena práctica tenerlo activado siempre.

### Permisos de Acceso (Access Permissions)

Los permisos controlan qué pueden hacer los usuarios en tus repositorios:

| Permiso | Descripción |
| :--- | :--- |
| **Read** | Ver y clonar el repositorio |
| **Triage** | Gestionar issues y PRs sin poder hacer push |
| **Write** | Push de código, gestión de issues/PRs |
| **Maintain** | Gestión del repositorio sin acceso a configuración destructiva |
| **Admin** | Control total, incluida la configuración del repo y borrado |

### Enterprise Managed Users (EMU)

Los **EMUs** son cuentas de GitHub creadas y gestionadas por una empresa a través de su proveedor de identidad (IdP, como Azure AD o Okta).

- Las cuentas EMU **no pueden actuar fuera de la organización** (no pueden contribuir a repos públicos con esa cuenta).
- La empresa tiene control total sobre la cuenta (puede desprovisionarla cuando el empleado se va).
- Diferencia con cuentas normales en una Enterprise: Una cuenta personal normal puede existir fuera de la organización. Una EMU no.

---

## 6.2 Administración de GitHub

### Habilitar/Deshabilitar Características

Los administradores de una organización o repositorio pueden activar o desactivar funcionalidades como:

- Issues, Wikis, Discussions, Pages, Sponsorships, Projects.
- Se hace desde `Settings > General` del repositorio o de la organización.

### Niveles de Permisos de Repositorio

Los mismos 5 niveles vistos arriba (Read, Triage, Write, Maintain, Admin) se aplican tanto a colaboradores individuales como a equipos dentro de una organización.

### Visibilidad del Repositorio

| Visibilidad | ¿Quién puede verlo? |
| :--- | :--- |
| **Public** | Cualquier persona en internet |
| **Private** | Solo el propietario y los colaboradores invitados |
| **Internal** | Solo los miembros de la organización Enterprise (ni siquiera el público general) |

> [!warning] Cambiar de público a privado tiene consecuencias
> Si haces un repositorio privado que era público, los forks existentes permanecen pero se desconectan. Las GitHub Pages dejan de ser accesibles si no tienes el plan adecuado.

### Opciones de Privacidad del Repositorio

**Branch Protection Rules:** Reglas que protegen ramas específicas de cambios no autorizados:

- Requerir PRs antes de fusionar (no se puede hacer push directo a `main`).
- Requerir revisiones aprobadas (1, 2 o más aprobaciones).
- Requerir que los checks de CI pasen antes de fusionar.
- Requerir firma de commits.

**Required Reviewers:** Número mínimo de aprobaciones necesarias antes de poder fusionar un PR.

**CODEOWNERS:** Asigna automáticamente revisores según el archivo modificado (explicado en Dominio 2).

### Pestaña de Seguridad (Security Tab)

La pestaña **Security** de un repositorio incluye:

- **Security Policy:** Archivo `SECURITY.md` que indica cómo reportar vulnerabilidades.
- **Dependabot Alerts:** Alertas automáticas de vulnerabilidades en las dependencias del proyecto.
- **Code Scanning:** Análisis estático del código para encontrar vulnerabilidades.
- **Secret Scanning:** Detecta si accidentalmente has subido claves API, tokens o contraseñas al repositorio.

### Repository Insights

La pestaña **Insights** del repositorio incluye métricas de:

- Actividad de la comunidad (contributors, commits por semana).
- Traffic (visitantes únicos, clonaciones).
- Dependency graph (árbol de dependencias del proyecto).

### Gestión de Colaboradores

- **Invitar colaboradores:** `Settings > Collaborators` → Buscar por username o email.
- **Eliminar colaborador:** Desde la misma pantalla.
- **Equipos (Teams) en organizaciones:** Permite gestionar permisos de forma grupal en lugar de usuario a usuario.
