**Tags:** #aws #seguridad #autenticacion #autorizacion #responsabilidad-compartida #cloud-practitioner #cp-seguridad

> [!summary] El Concepto Clave
> En AWS, la seguridad no es un extra, es la prioridad cero ("Job Zero"). Para proteger tu entorno debes entender quién entra (Autenticación), qué puede hacer una vez dentro (Autorización) y de qué partes de la seguridad te encargas tú y de cuáles se encarga Amazon.

---
## 🔑 1. Autenticación vs. Autorización (La Puerta y la Llave Maestra)

* **Autenticación (Authentication): "¿Eres quién dices ser?"**

    * *Definición:* Es el proceso de verificar la identidad.
    * *El Método:* Normalmente se hace usando un usuario y contraseña, o con sistemas más seguros como MFA (Autenticación Multifactor, donde pones un código de tu móvil).
    * *La Analogía:* Es enseñar tu DNI al guardia de seguridad de la puerta principal del edificio para que te deje entrar al vestíbulo.

* **Autorización (Authorization): "¿Qué tienes permitido hacer aquí?"**
*
    * *Definición:* Es el proceso de otorgar o denegar permisos específicos una vez que ya estás dentro.
    * *El Método:* Se usan Políticas (Policies) que dictan reglas exactas (ej. "Puede leer archivos, pero no borrarlos").
    * *La Analogía:* Ya estás dentro del edificio, pero tu tarjeta de acceso solo abre la puerta de la sala de reuniones, no te deja entrar al despacho del director.

---

## ⚖️ 2. El Modelo de Responsabilidad Compartida (Pilar del Examen)

AWS no hace que tu sistema sea mágicamente seguro si tú cometes errores. Se dividen el trabajo.
### AWS: La Seguridad "DE LA" Nube (Responsabilidad de Amazon)

AWS protege todo lo que tú no puedes tocar físicamente.

* **Infraestructura Global:** Las Regiones, Zonas de Disponibilidad (AZ) y Ubicaciones Periféricas (Edge Locations).
* **Hardware físico:** Servidores, cables de red, discos duros físicos, refrigeración de los centros de datos, guardias de seguridad en las puertas de los edificios de Amazon.
* **Capa de virtualización:** El software maestro que separa tu máquina virtual (EC2) de la máquina virtual de tu vecino.

### El Cliente (Tú): La Seguridad "EN LA" Nube (Tu Responsabilidad)

Tú controlas todo el software y los datos que metes dentro de las máquinas que AWS te presta.

* **Tus Datos (Lo más importante):** Qué subes, si los cifras (les pones contraseña) o no. AWS no mira tus datos.
* **Gestión de Identidades y Accesos (IAM):** Crear los usuarios, darles contraseñas difíciles y configurar sus permisos (Autorización).
* **Sistemas Operativos (EC2):** Si alquilas un servidor virtual, AWS te lo da limpio. Tú debes instalarle el antivirus y aplicar las actualizaciones de Windows o Linux.
* **Configuración del Firewall:** Abrir o cerrar puertos en los Grupos de Seguridad o Listas de Control de Acceso (NACLs).

---

## 🛡️ 3. Los Tres Tipos de Controles de Seguridad

Cuando diseñas seguridad en AWS, aplicas controles en tres frentes:

1.  **Prevención:** Evitar que los malos entren. (Ej. Usar MFA y limitar los permisos al mínimo necesario).

2.  **Protección:** Poner barreras a los recursos críticos. (Ej. Cifrar la base de datos para que si alguien la roba, no pueda leer el contenido).

3.  **Detección y Respuesta:** Saber cuándo te están atacando y actuar rápido. (Ej. Sistemas de alarmas y registros que te avisan si alguien inicia sesión desde un país sospechoso a las 3 de la madrugada).

---

---
→ Volver al índice: [[📂Seguridad/00 - Índice Seguridad|🪐 Seguridad]]
