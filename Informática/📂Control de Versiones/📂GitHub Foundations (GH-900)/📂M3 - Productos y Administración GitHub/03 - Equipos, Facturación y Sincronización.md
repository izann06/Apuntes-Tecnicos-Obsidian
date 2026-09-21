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

### Crear un equipo

En la organización: `Settings > Teams > New team`. Asigna:

- **Nombre** del equipo.
- **Visibilidad**: Visible (todos los miembros de la org lo ven) o Secreto (solo los miembros del equipo).
- **Repositorios** y su nivel de permiso (Read, Write, Maintain, Admin).

> [!TIP] Buena práctica
> Asignar permisos a **equipos**, no a usuarios individuales. Así cuando alguien entra o sale de la empresa, basta con añadirlo o quitarlo del equipo y hereda/pierde todos los permisos automáticamente.

---

## 2. Team Synchronization (Sincronización de Equipos)

Disponible en **GitHub Enterprise Cloud**, Team Sync conecta los equipos de GitHub con los **grupos de un proveedor de identidad (IdP)** externo. Se utiliza el estándar **SCIM** (*System for Cross-domain Identity Management*) para aprovisionar y desaprovisionar cuentas de forma automatizada.

| IdP soportado | Ejemplo |
| :--- | :--- |
| **Microsoft Entra ID** (antes Azure AD) | Grupo "Backend Developers" en Azure → Equipo `@company/backend` en GitHub |
| **Okta** | Grupo "Frontend Team" en Okta → Equipo `@company/frontend` en GitHub |

### Ciclo de Vida del Empleado (Vía SCIM)

| Evento | ¿Qué pasa automáticamente? |
| :--- | :--- |
| **Onboarding** (nuevo empleado) | Se añade al grupo en el IdP → Aparece automáticamente en el equipo de GitHub → Recibe permisos. |
| **Offboarding** (sale de la empresa) | Se elimina del IdP → Desaparece automáticamente de GitHub → Pierde todo acceso. |
| **Cambio de rol** | Se mueve de grupo en el IdP → Los equipos y permisos de GitHub se actualizan solos. |

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
| **GitHub Actions** | Minutos de cómputo | 2.000 min/mes |
| **GitHub Packages** | GB de almacenamiento y transferencia | 500 MB |
| **GitHub Codespaces** | Horas de cómputo + GB de almacenamiento | 120 horas core/mes |

### Gestión y Auditoría de Costes

- **Rastreo de Puestos (Seats):** En GitHub Enterprise, se facturan las licencias asignadas. Las **cuentas de máquina** (bots, cuentas de CI/CD) consumen una licencia de pago igual que un humano, salvo que se usen GitHub Apps, que son gratuitas.
- **Spending Limits:** Puedes configurar un límite máximo de gasto mensual para cada servicio en `Settings > Billing > Spending limits`. Al alcanzar el límite, el servicio se desactiva (no te cobra más).
- **Informes de consumo y Auditoría:** Descarga de informes CSV detallados desde la Consola de Administración. También puedes hacer consultas avanzadas de uso de licencias mediante **GraphQL API** y **REST API**.
- **Estrategias de optimización:**
  - Desasignar licencias de usuarios inactivos.
  - Implementar **SCIM** para asegurar que quienes dejan la empresa pierdan su licencia automáticamente.
  - Auditar permisos regularmente.

> [!WARNING] Pregunta frecuente de examen
> El examen puede preguntar qué pasa cuando un servicio alcanza el spending limit. La respuesta: **se desactiva** (los workflows de Actions fallan, los Codespaces no arrancan). No te cobra de más automáticamente a menos que tú incrementes el límite.
