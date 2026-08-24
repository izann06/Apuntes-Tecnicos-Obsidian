**Tags:** #aws #api #consola #cli #sdk #cloud-practitioner #gestion #cp-computacion

> [!summary] El Motor Oculto: Las APIs
> En AWS, todo lo que haces (encender un servidor, crear un usuario, subir una foto) se realiza mediante **solicitudes a las API**. Las API son los "mensajeros" que llevan tus órdenes a los servidores de Amazon. AWS te ofrece 3 herramientas principales para enviar estos mensajes.

---

## 1. Consola de Administración de AWS (Web)

Es la página web visual donde entras con tu navegador. Seguramente es lo que usaste en tu proyecto anterior para montar el servidor.

* **Características:** Interfaz gráfica amigable, buscador rápido de servicios y procesos guiados paso a paso. Permite iniciar sesión con varias identidades.

* **App Móvil:** Muy útil para cuando estás fuera de la oficina. Te permite ver alarmas, vigilar la facturación (los gastos) y supervisar recursos.

* **Ideal para:** Usuarios visuales, principiantes y tareas de administración rápidas que no requieran repetición.

![[🎛️ Cómo Intercomunicarse con AWS (Aprovisionar Recursos).png]]

## 2. AWS CLI (Interfaz de Línea de Comandos)

Es la Terminal en Mac/Linux o CMD en Windows.

* **Características:** Permite enviar comandos de texto directos a AWS (ejemplo: `aws ec2 start-instances`).

* **El Superpoder (Automatización):** Puedes escribir un "script" (un archivo de texto con varios comandos seguidos) que cree 100 servidores en 5 segundos, sin tener que hacer 500 clics en la web.

* **Ideal para:** Administradores de sistemas avanzados y usuarios que necesitan automatizar tareas repetitivas de forma eficiente.

![[🎛️ Cómo Intercomunicarse con AWS (Aprovisionar Recursos)-1.png|697]]

## 3. AWS SDK (Kits de Desarrollo de Software)

Son paquetes de código (librerías) que Amazon te proporciona para que tu propia aplicación hable directamente con AWS.

* **Características:** Ofrece código prefabricado y documentación para lenguajes de programación reales (Java, Python, C++, .NET).

* **El Superpoder:** Permite que *tu código* controle AWS. Por ejemplo, si programas un videojuego, usas el SDK para que, al guardar la partida, el juego hable directamente con la base de datos de AWS.

* **Ideal para:** Desarrolladores (programadores) que necesitan integrar los servicios de AWS dentro de las aplicaciones que están construyendo.

![[🎛️ Cómo Intercomunicarse con AWS (Aprovisionar Recursos)-2.png|697]]

---

## ⚖️ EC2 y la Responsabilidad: Un Servicio "No Administrado"

Vuelvo a insistir en la Responsabilidad Compartida porque es crucial diferenciar qué tipo de servicio estás usando.

**Amazon EC2 es un servicio NO ADMINISTRADO (IaaS).**

* AWS se encarga de la **Seguridad DE la nube** (hardware físico, cables, electricidad).

* Tú te encargas de la **Seguridad EN la nube**. Al ser un servicio "no administrado", AWS te da la máquina en blanco y se lava las manos con el software. 

**Tus obligaciones directas en EC2 incluyen:**
1. Administrar el Sistema Operativo (instalarlo y configurarlo).
2. Aplicar parches de seguridad y actualizaciones de Windows/Linux.
3. Configurar los Firewalls (que en AWS se llaman **Grupos de Seguridad** o *Security Groups*).

---

> [!important] Todo se queda guardado en el Historial 
> Como todas las interacciones con los servicios de AWS se realizan mediante **solicitudes a las API**, Amazon puede rastrear cada una de ellas, sin importar desde dónde vengan. Así que da igual si usas la consola o terminal, se guarda todo.

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
