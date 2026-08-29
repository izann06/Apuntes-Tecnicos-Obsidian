**Tags:** #aws #redes #vpc #subredes #internet-gateway #arquitectura #cloud-practitioner #cp-redes

> [!summary] El Concepto Clave
> Configurar una red en AWS es como diseñar el plano de un restaurante. Tienes que decidir dónde están las paredes exteriores (VPC), cuáles son las zonas públicas accesibles desde la calle (Subredes Públicas para los cajeros) y cuáles son las zonas restringidas solo para empleados (Subredes Privadas para la cocina/baristas).

---

## 🏗️ 1. Construyendo los Cimientos 

Para entender cómo se conecta todo, vamos de lo más grande a lo más pequeño:

1. **Nube de AWS (El Mundo):** Es toda la infraestructura global de Amazon.

2. **Región (La Ciudad):** Eliges una ubicación física (ej. París o Frankfurt) para poner tu negocio.

3. **Amazon VPC - Virtual Private Cloud (El Local):** Es tu servidor con red virtual, una sección privada y aislada lógicamente dentro de AWS pero eso no quiere decir que no se muestre cara al público.

 * *¿Qué hace por debajo?* Crea una frontera de seguridad. Nadie de internet puede entrar a tu VPC a menos que tú abras una puerta explícitamente. Es tu territorio.
 
![[🕸️ Redes en AWS. Entendiendo VPC, Subredes y Conexiones.png]]

---

## 🧱 2. Dividiendo el Local y Asegurando Supervivencia

Una vez que tienes el local (VPC), tienes que dividirlo por dentro para organizarte.

### Las Zonas de Disponibilidad (AZ)

* Fíjate que la VPC (el recuadro morado) **atraviesa dos Zonas de Disponibilidad (A y B)**. 

* *¿Por qué?* Porque si un centro de datos (Zona A) se queda sin electricidad, tu red sigue funcionando en el centro de datos de al lado (Zona B). Tu VPC abarca ambas zonas para garantizar la alta disponibilidad.

### Las Subredes Privadas (La Cocina / Los Baristas)

* Dentro de cada AZ, "levantas paredes" creando **Subredes** (los recuadros verdes continuos).

* *¿Qué es una Subred?* Es un trozo más pequeño de tu VPC. Un rango de direcciones IP.

* *¿Por qué son Privadas?* Porque **no tienen conexión directa a Internet**. 

* *¿Qué metes aquí?* Las **Bases de Datos** (donde guardas contraseñas, tarjetas de crédito o, en la analogía, a los baristas preparando el café en secreto). Nadie de la calle (Internet) puede hablar directamente con la base de datos.

![[🕸️ Redes en AWS. Entendiendo VPC, Subredes y Conexiones-1.png]]

---

## 🚪 3. Abriendo las Puertas al Público

Aquí es donde ocurre la magia de la conectividad y donde todo cobra sentido.

### Las Subredes Públicas (El Mostrador / Los Cajeros)

* Creas nuevas habitaciones (los recuadros verdes discontinuos) llamadas **Subredes Públicas**.

* *¿Qué metes aquí?* Las **Instancias EC2** (tus servidores web o "cajeros"). Estos servidores alojan la página web que ven tus clientes.

### La Puerta de Enlace a Internet (Internet Gateway - IGW)

* *¿Qué es?* Es la **puerta principal del restaurante**. Fíjate en el icono redondo morado que está justo en el borde de la VPC. 

* *¿Cómo funciona por debajo?* Una subred solo se vuelve "Pública" si tú la conectas mediante cables virtuales (llamados Tablas de Enrutamiento) a este Internet Gateway. Si no está conectada al IGW, la subred es privada.

![[🕸️ Redes en AWS. Entendiendo VPC, Subredes y Conexiones-2.png]]

---

## 🔄 ¿Cómo se conecta todo por debajo en un flujo real?

Imagina que un cliente quiere ver el menú de cafés en su móvil. Este es el viaje exacto de los datos:

1. **El Usuario** coge su móvil, se conecta a **Internet** y escribe `www.tu-cafeteria.com`.

2. La petición viaja por la red mundial hasta llegar a la **Puerta de Enlace a Internet (IGW)** de tu VPC.

3. El IGW deja pasar al cliente y lo dirige al mostrador: la **Subred Pública**.

4. La petición llega a tu **Instancia EC2 (Cajero)**. El cajero lee el pedido: *"El cliente quiere ver el menú"*.

5. *¡Atención aquí!* El EC2 no tiene el menú memorizado. Tiene que pedírselo a la Base de Datos. 

6. Como el EC2 (Cajero) y la Base de Datos (Barista) están **dentro de la misma VPC**, pueden hablar entre ellos de forma segura y privada a través de la red interna de AWS, sin salir a internet.

7. La **Base de Datos** le pasa el menú al **EC2**.

8. El **EC2** se lo envía de vuelta al usuario a través del **Internet Gateway**.

---

> [!important] Como hace el servidor privado para descargar actualizaciones de Windows.
> 
> - **Ubicación:** El NAT Gateway se coloca en la **Subred Pública**. Al estar ahí, tiene permiso para salir por la puerta principal (Internet Gateway).
>
> - **La Petición:** El servidor privado, a través de la red interna, le dice al NAT Gateway: _"Oye, ve a los servidores de Linux en internet y descárgame la actualización versión 2.0"_.
>
> - **El recado:** El NAT Gateway sale a internet, busca la actualización, vuelve a entrar al edificio y se la entrega en mano al servidor privado.

---

---
→ Volver al índice: [[📂Redes/00 - Índice Redes|🪐 Redes]]
