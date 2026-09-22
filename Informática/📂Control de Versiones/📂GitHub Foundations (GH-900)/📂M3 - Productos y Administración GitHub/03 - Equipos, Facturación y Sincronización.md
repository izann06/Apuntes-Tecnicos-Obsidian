#github #gh-foundations #modulo-3 #teams #facturacion #team-sync

> [!info] Navegación
> ◀ [[02 - Estructura Organizativa y Permisos]] · ▶ [[01 - Autenticación (2FA, SSH, PAT, SSO)]]

---

# 03 — Equipos, Facturación y Sincronización

> **Resumen ejecutivo:**
> 1. Los **Equipos (Teams)** agrupan usuarios y asignan permisos colectivos a repositorios.
> 2. **Team Sync** vincula equipos de GitHub con grupos de un proveedor de identidad (IdP) como Okta o Azure AD.
> 3. GitHub tiene facturación por **suscripción** (fija) y por **uso** (Actions, Codespaces, Packages).

---

## 1. Gestión de Equipos (Teams)

Un **equipo** es un subgrupo de miembros dentro de una organización. Permite asignar permisos a repositorios de forma colectiva en lugar de usuario a usuario, aplicando el **principio de privilegios mínimos**.

- Se referencian con `@org/nombre-equipo` (ej. `@my-company/backend`).
- Pueden tener **sub-equipos** (ej. `@my-company/backend/api`, `@my-company/backend/database`).
- Los sub-equipos heredan los permisos del equipo padre.

> [!WARNING] Límites de escalabilidad (Examen)
> Es fundamental conocer los límites oficiales de GitHub para organizaciones y equipos:
> - Máximo **10.000 miembros** por organización.
> - Máximo **1.500 equipos** por organización.
> - Máximo **5.000 miembros** por equipo.
> 
> *¿Qué pasa si tengo 3 equipos de 5.000 miembros?* Dado que una organización solo puede tener 10.000 miembros en total, no podrías tener a 15.000 personas distintas. Sin embargo, SÍ podrías tener 3 equipos de 5.000 miembros si los usuarios **se repiten** entre los equipos (ej: las mismas 5.000 personas metidas en 3 equipos diferentes).

### Crear un equipo (Solo en Organizaciones)

> [!NOTE] Cuidado
> Los equipos **solo existen en las Organizaciones**. Si estás mirando tu cuenta Personal, nunca vas a encontrar el botón de "Teams".

Para crearlo: Ve a la página principal de tu **Organización** > Pestaña **Teams** > Botón verde **New team**. Asigna:

- **Nombre** del equipo.
- **Visibilidad**: Visible (todos los miembros de la org lo ven) o Secreto (solo los miembros del equipo).
- **Repositorios** y su nivel de permiso (Read, Write, Maintain, Admin).

> [!TIP] Buena práctica
> Asignar permisos a **equipos**, no a usuarios individuales. Así cuando alguien entra o sale de la empresa, basta con añadirlo o quitarlo del equipo y hereda/pierde todos los permisos automáticamente.

---

## 2. Team Synchronization e IdP

En empresas grandes no se invita a los usuarios uno por uno a GitHub. Se usa **Team Synchronization** (disponible en GitHub Enterprise Cloud), que conecta GitHub con el sistema central de empleados de la empresa, llamado **IdP (Identity Provider)**.

* **¿Qué es un IdP?** Es el directorio digital de la empresa (ej: Microsoft Entra ID, Okta, Google Workspace). Ahí están las cuentas de correo corporativas de todos los empleados y los grupos a los que pertenecen (RRHH, Backend, Frontend).

* **¿Qué es SCIM?** (*System for Cross-domain Identity Management*). Es simplemente el "idioma" o protocolo técnico que usan el IdP y GitHub para hablar entre ellos de forma segura.

### El Ciclo de Vida del Empleado (Automatizado por SCIM)

Gracias a SCIM, GitHub se convierte en un "esclavo" del IdP. Esto automatiza el ciclo de vida del empleado sin que los admins de GitHub tengan que hacer nada manualmente:

1. **Onboarding (Contratación):** El departamento de IT crea la cuenta del nuevo empleado en el IdP de la empresa y lo mete en el grupo "Backend". GitHub, al instante, recibe la orden por SCIM, le crea una cuenta corporativa en GitHub y lo mete en el Team "Backend", dándole todos los permisos de acceso de golpe.

2. **Cambio de rol:** Si el empleado pasa de "Backend" a "Frontend", IT lo cambia de grupo en el IdP. GitHub le quita los permisos antiguos y le da los nuevos al instante.

3. **Offboarding (Despido/Baja):** El empleado se va de la empresa. IT borra o suspende su cuenta en el IdP. En ese mismo milisegundo, SCIM avisa a GitHub, que le corta el acceso a todos los repositorios. Esto evita el riesgo gravísimo de seguridad de que un ex-empleado siga teniendo acceso al código.

---

## 3. Modelo de Facturación

### Facturación por Suscripción (Fija)

Coste fijo mensual por usuario para el plan de la organización:

| Plan | Precio |
| :--- | :--- |
| GitHub Free (org) | 0 $ |
| GitHub Team | ~4 $/usuario/mes |
| GitHub Enterprise | ~21 $/usuario/mes |

### Facturación por Uso (Metered Billing)

Ciertos servicios se cobran según el consumo real:

| Servicio | Unidad de cobro | Incluido en Free |
| :--- | :--- | :--- |
| **GitHub Actions** | Minutos de cómputo (tiempo que pasas ejecutando CI/CD) | 2.000 min/mes |
| **GitHub Packages** | GB de almacenamiento y transferencia (es el registro de GitHub para guardar dependencias como Docker, npm, Maven...) | 500 MB |
| **GitHub Codespaces** | Horas de cómputo + GB de almacenamiento | 120 horas core/mes |

### Gestión y Auditoría de Costes

La auditoría de costes sirve para que a la empresa no le llegue una factura de 50.000$ por sorpresa porque alguien dejó encendido un Codespace o consumió demasiados minutos de Actions.

1. **Budgets and Alerts (Spending Limits):** 
   Como ves en la captura de pantalla, puedes ir a `Settings > Billing and licensing > Budgets and alerts` para poner un límite mensual (en dólares) a cada servicio que cobra por uso (Codespaces, Packages, Actions y Git LFS). 

![[03 - Equipos, Facturación y Sincronización-1.png]]



   * **¿Qué pasa cuando llegas al 100% del límite?** GitHub tiene un mecanismo de seguridad (esa columna que dice *"Stop usage: Yes"*). Cuando tocas el límite, el servicio **se bloquea**. Los workflows de Actions darán error, los Codespaces no arrancarán y no podrás descargar Packages. **Nunca te van a cobrar de más**, simplemente te cortan el grifo hasta el mes siguiente o hasta que subas el presupuesto.

2. **Rastreo de Puestos (Seats):** 
   En planes de pago, GitHub te cobra por cada "asiento" (usuario). Si usas cuentas de máquina (bots) para automatizar cosas, GitHub te las cobrará como si fuesen humanos. Por eso, la mejor estrategia para ahorrar dinero es **usar GitHub Apps** en lugar de cuentas bot, ya que las Apps no consumen licencia (asiento).

3. **Informes de consumo:** 
   Los administradores pueden descargar archivos CSV detallados o usar la API de GraphQL/REST para analizar exactamente qué equipos o usuarios están consumiendo más minutos de Actions o más gigas en Packages.

> [!WARNING] Pregunta frecuente de examen
> El examen puede preguntar qué pasa cuando un servicio alcanza el spending limit. La respuesta: **se desactiva** (los workflows de Actions fallan, los Codespaces no arrancan). No te cobra de más automáticamente a menos que tú incrementes el límite.
