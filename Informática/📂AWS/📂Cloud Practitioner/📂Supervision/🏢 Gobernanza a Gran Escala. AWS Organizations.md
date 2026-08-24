**Tags:** #aws #organizations #gobernanza #scp #facturacion #cloud-practitioner #cp-supervision

> [!summary] El Concepto Clave
> A medida que una empresa crece, no debe meter todos sus proyectos en una sola cuenta de AWS (es peligroso y desordenado). Lo ideal es tener múltiples cuentas separadas (una para Desarrollo, otra para Producción, otra para Recursos Humanos...). **AWS Organizations** es el servicio maestro que te permite agrupar, asegurar y pagar todas esas cuentas de forma centralizada.

---
## 🌳 1. La Estructura Jerárquica (El Árbol de la Empresa)

AWS Organizations organiza tus cuentas como si fuera el organigrama de una empresa:

1.  **La Raíz (Root):** Es el nivel más alto. Contiene la **Cuenta Principal (Management Account)**. Esta es la cuenta que "paga la factura" y desde donde los administradores supremos dictan las reglas.

2.  **Unidades Organizativas (OUs):** Son como las "carpetas" o los "departamentos" de tu empresa. Puedes tener una OU llamada `Finanzas`, otra `Desarrollo` y otra `Producción`. Las OUs pueden contener otras OUs anidadas dentro de ellas.

3.  **Cuentas Miembro (Member Accounts):** Son las cuentas de AWS individuales reales donde viven los servidores y las bases de datos. Se meten dentro de las OUs correspondientes.

---

## 💳 2. Beneficios Financieros: Facturación Consolidada

Este es uno de los motivos principales por los que las empresas activan AWS Organizations:

* **Una sola factura:** En lugar de tener 50 tarjetas de crédito diferentes y 50 facturas separadas a final de mes, la cuenta Root recibe una única factura maestra unificada que detalla el gasto de todas las subcuentas.

* **Descuentos por Volumen (Pricing Tiers):** AWS te cobra menos cuanto más usas un servicio (ej. los primeros 50 TB de S3 cuestan "X", los siguientes cuestan "X - 10%"). Con Organizations, **AWS suma el consumo de todas tus cuentas juntas**. Si entre 10 cuentas pequeñas superan los 50 TB, a todas se les aplica el descuento por volumen automáticamente.

---
## 🛡️ 3. Seguridad Suprema: Políticas de Control de Servicios (SCPs)

Presta mucha atención a esto, porque es una trampa clásica de examen y la diferencia entre aprobar o fallar una pregunta de control de accesos.

* **¿Qué es una SCP?** Es un filtro de seguridad masivo. Sirve para establecer los **permisos máximos** disponibles para las cuentas dentro de una organización.

* **¿A qué se aplican?** Se aplican a **Unidades Organizativas (OUs)** o a **Cuentas Miembro completas**. 

* **El Poder de la SCP:** Si aplicas una SCP a la OU de "Desarrollo" que dice *"DENEGAR el uso de bases de datos RDS"*, **nadie** dentro de esa OU podrá crear una RDS. Ni siquiera el Usuario Raíz de esa cuenta, ni el Administrador de esa cuenta. La SCP es la ley suprema y anula cualquier política de IAM interna.

> [!warning] 🚨 IAM Policies vs. SCPs (Clave de Examen)
> * Las **Políticas de IAM** se aplican a **Usuarios, Grupos y Roles** específicos dentro de una sola cuenta (Ej. "Darle permiso a Juan").
> * Las **SCPs** se aplican a **Cuentas o OUs enteras** desde arriba (Ej. "Nadie en la cuenta de Finanzas puede apagar CloudTrail"). Las SCP **NO** se pueden aplicar directamente a usuarios de IAM individuales.

---

## 🎯 Casos de Uso Típicos

1.  **Aislamiento de Recursos:** Si el equipo de pruebas rompe un servidor, al estar en una cuenta separada, no afecta en absoluto a la cuenta de Producción.

2.  **Automatización:** Permite crear nuevas cuentas de AWS de forma programática (mediante código o API) en segundos cuando llega un equipo nuevo a la empresa.

3.  **Límites de Seguridad Estrictos:** Asegurar que ciertas cuentas (ej. las que procesan datos médicos o financieros) no puedan usar servicios de AWS que no estén aprobados por el equipo legal.

---

---
→ Volver al índice: [[📂Supervision/00 - Índice Supervision|🪐 Supervision]]
