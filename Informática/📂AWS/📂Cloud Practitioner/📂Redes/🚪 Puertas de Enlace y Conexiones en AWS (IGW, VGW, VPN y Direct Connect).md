**Tags:** #aws #redes #vpc #vpn #direct-connect #internet-gateway #cloud-practitioner #cp-redes

> [!summary] El Concepto Clave
> Tu VPC es un edificio cerrado sin puertas ni ventanas. Para que los datos entren o salgan, tienes que abrir un agujero en la pared y poner una "Puerta". El tipo de puerta que pongas determinará quién puede entrar: todo el público (IGW), empleados autorizados por internet (VPN/VGW) o empleados por un túnel secreto subterráneo (Direct Connect).

---

## 🌎 1. La Puerta Pública: Internet Gateway (IGW)

* **¿Qué es?** Es la puerta principal de tu restaurante que da a la calle.
* **¿Para qué sirve?** Permite que cualquier persona de Internet entre a tu VPC y que tus recursos (como tus servidores web en las *Subredes Públicas*) puedan salir a Internet a navegar.
* **Seguridad:** Está abierta al público general. Si tienes recursos aquí, cualquiera puede intentar acceder a ellos (por lo que necesitas tener buena seguridad).

---

## 🔐 2. La Puerta Privada (Virtual Private Gateway - VGW) y la VPN

Aquí es donde suele haber confusión. Vamos a separarlo:

### El Túnel (La Conexión VPN)

* **¿Qué es?** Internet es como la calle principal de la ciudad. Cualquiera puede ver por dónde caminas. Una **VPN (Virtual Private Network)** es como construir un pasadizo de cristal opaco e insonorizado en medio de esa calle. Caminas por el mismo sitio público (Internet), pero el cristal (el **cifrado**) impide que nadie vea quién eres ni qué llevas en las manos.

* **Analogía:** Ir desde tu casa a la cafetería del edificio corporativo cruzando la calle en un coche blindado con los cristales tintados.

### La Puerta del Túnel (Virtual Private Gateway - VGW)

* **¿Qué es?** El túnel VPN tiene que "enchufarse" a algún sitio para entrar a tu VPC. Ese enchufe, esa "puerta trasera" de tu local, es el **Virtual Private Gateway (VGW)**.

* **¿Cómo funciona?** El VGW es el portero de seguridad en la entrada trasera del edificio. Solo deja pasar el tráfico si viene a través del túnel VPN seguro (de una red autorizada como la oficina central de tu empresa) y tiene las credenciales correctas.

* **El Problema:** Aunque el coche esté blindado (VPN), sigues yendo por la calle pública (Internet). Si hay atasco (mucho tráfico), tu coche blindado irá despacio.

> [!faq] ¿Por qué pagarías por el VGW entonces si ambos van por la calle y sufren atascos?
> Porque podrías montar tu propia conexión VPN usando la puerta pública (IGW) y poniendo un servidor tuyo (EC2) a hacer de portero. Pero con esa opción, si tu "guardia de seguridad" (EC2) se pone enfermo, nadie entra. Tienes que ir tú a curarlo (reiniciar el servidor, actualizar el software). 
> 
> Al usar la opción del **VGW**, Amazon te garantiza que esa puerta trasera nunca se va a estropear y ellos hacen todo el mantenimiento tecnológico por ti (Alta Disponibilidad).

---

## 🚀 3. El Cable Secreto: AWS Direct Connect

A veces, la conexión VPN no es suficiente si necesitas pasar cantidades monstruosas de datos o si tu empresa no puede permitirse que "haya un atasco en Internet".

* **¿Qué es?** Es un cable de fibra óptica **físico** y dedicado que conecta directamente el centro de datos de tu empresa (tus oficinas) con el centro de datos de AWS.

* **Analogía:** Es la "puerta mágica supersecreta" o un pasadizo subterráneo privado que va desde tu escritorio directo a la máquina de café de AWS.

* **Las Ventajas:**
    * **NO usa el Internet público.** No hay atascos, la velocidad es alta y constante.
    * **Máxima Seguridad:** Es literalmente un cable privado para ti. Ideal para cumplir normativas bancarias o gubernamentales muy estrictas.

---

## 📊 Chuleta de Conexiones a la VPC

| Si quieres conectar tu VPC con...                              | Usarás esta "Puerta" o Servicio                          |
| :------------------------------------------------------------- | :------------------------------------------------------- |
| *El mundo entero (Internet público)*                         | *Internet Gateway (IGW)*                               |
| *La red de tu oficina (A través de Internet cifrado)*        | *VPN enchufada a un Virtual Private Gateway (VGW)* |
| *La red de tu oficina (A través de un cable físico privado)* | *AWS Direct Connect*                                   |

---

---
→ Volver al índice: [[📂Redes/00 - Índice Redes|🪐 Redes]]
