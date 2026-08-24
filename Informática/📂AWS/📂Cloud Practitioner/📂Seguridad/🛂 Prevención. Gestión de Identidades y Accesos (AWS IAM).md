**Tags:** #aws #seguridad #iam #minimo-privilegio #roles #cloud-practitioner #cp-seguridad

> [!summary] El Concepto Clave
> Para evitar que alguien rompa algo (o robe datos), nunca debes darle las llaves de toda la empresa. **AWS IAM (Identity and Access Management)** te permite aplicar el "Principio de Mínimo Privilegio": darle a cada usuario o máquina *únicamente* los permisos que necesita para hacer su trabajo y absolutamente nada más.

---
## 👑 1. El Usuario Raíz (The Root User)

* **¿Qué es?** Es la dirección de correo electrónico con la que creaste originalmente la cuenta de AWS. Es el Dios absoluto de tu cuenta.

* **El Peligro:** Puede borrar bases de datos, cancelar la cuenta de AWS o ver información de facturación sin que ninguna política pueda detenerlo.

* **Prácticas recomendadas:**

    1.  Ponle una contraseña larguísima y guárdala bajo llave.
    2.  **Activa siempre la MFA (Autenticación Multifactor):** Exigir un código del móvil además de la contraseña.
    3.  **¡NO LO USES NUNCA para tareas diarias!** Créate a ti mismo un usuario IAM de Administrador para el día a día, y guarda el Usuario Raíz solo para emergencias o cambios de facturación extremos.

---

## 👥 2. Los Componentes de IAM

Dentro del servicio IAM, configuras el acceso diario usando estos 4 elementos:

### A. Usuarios de IAM

* Representan a una persona o una aplicación específica (ej. "Juan", "Maria", "App-Ventas").

* **Regla de Oro:** Por defecto, un usuario recién creado **NO TIENE PERMISOS DE NADA**. Todo en AWS está denegado por defecto hasta que lo permites expresamente.

### B. Grupos de IAM

* Son contenedores para usuarios (ej. Grupo "Desarrolladores", Grupo "RecursosHumanos").

* *¿Para qué sirven?* En lugar de darle permisos a "Juan", metes a Juan en el grupo "Desarrolladores" y le das los permisos al grupo. Si Juan se cambia de departamento, simplemente lo cambias de grupo. Ahorra muchísimo tiempo.

### C. Políticas de IAM (IAM Policies)

* Son los documentos escritos en formato JSON que dictan la **Autorización** (Lo que puedes o no hacer).

* Tienen 3 partes principales:

    * **Efecto (Effect):** ¿Permitir o Denegar? (*Allow / Deny*).
    
    * **Acción (Action):** ¿Qué llamada a la API quieres hacer? (ej. `s3:GetObject` para descargar archivos).
    
    * **Recurso (Resource):** ¿Sobre qué objeto exacto? (ej. Solo sobre el bucket llamado "datos-rrhh").

### D. Roles de IAM 

* A diferencia de un Usuario, un Rol **no tiene contraseña ni credenciales estáticas**.

* Es un "sombrero" temporal que se puede poner y quitar.

* **Casos de Uso:**

    * **Para Máquinas (EC2):** Si un servidor EC2 necesita leer una base de datos, no le creas un usuario con contraseña (porque alguien podría robarla del código). Le asignas un Rol y el EC2 asume el permiso mágicamente por detrás.
    
    * **Para Federar Usuarios Externos:** Si tu empresa ya usa Microsoft Active Directory para que los empleados enciendan su ordenador, pueden usar esas mismas credenciales para entrar a AWS asumiendo un Rol temporal, sin tener que crearles un "Usuario IAM" nuevo.



---

## 🛠️ 3. Servicios Complementarios de Seguridad

* **AWS IAM Identity Center (Antes AWS SSO):** Es el servicio que permite la **Federación** de forma fácil. Los empleados inician sesión una sola vez (Single Sign-On) con sus cuentas corporativas y ven un portal con todos los servicios y cuentas de AWS a los que tienen acceso.

* **AWS Secrets Manager:** Si tienes una contraseña de una base de datos o una clave de API secreta, **nunca debes escribirla en el código de tu aplicación**. La guardas en Secrets Manager. Este servicio cifra la contraseña y, lo más importante, **puede rotarla (cambiarla) automáticamente** cada X días sin que el programador tenga que hacer nada.

* **AWS Systems Manager:** Te da un panel de control gigante para ver todos tus servidores (nodos) juntos, ya estén en AWS, en tu oficina o en otra nube, permitiéndote aplicar parches de seguridad de Windows a todos a la vez.

---

---
→ Volver al índice: [[📂Seguridad/00 - Índice Seguridad|🪐 Seguridad]]
