
# **🧠 ¿Qué es HTTP?

Piensa en **HTTP** como el idioma que usan los navegadores (como Chrome o Firefox) para hablar con las páginas web (los servidores).

👉 Ejemplo:  
Cuando escribes `https://www.youtube.com` y pulsas Enter, tu navegador dice:

> “Hola servidor de YouTube, ¿me puedes enviar la página principal?”

Y el servidor responde:

> “Aquí tienes el código de la página para que la muestres.”

Ese ir y venir de mensajes es **HTTP**.  
Tú (el navegador) eres el **cliente**, y el servidor (el ordenador donde está guardada la web) es quien **responde**.

---

# **🔒 ¿Qué es HTTPS?

Es lo mismo que HTTP, **pero con seguridad**.  
Las letras **S** significan “Seguro”.

👉 Ejemplo:  
Si entras a tu banco, no quieres que nadie vea tu contraseña o tus datos, ¿verdad?  
Pues HTTPS cifra (oculta) toda la información para que, aunque alguien la vea, no pueda entenderla.

--------------------------------------------------------------------


# **🌍 ¿Qué es DNS?

Cuando escribes `www.google.com`, tu PC necesita saber **qué dirección IP** tiene ese nombre.  
El **DNS** hace esa traducción.

👉 Ejemplo:

- Tú escribes `www.google.com`.
    
- DNS lo convierte a `142.250.72.46` (la dirección real del servidor).  
    Es como una **agenda telefónica** que convierte nombres en números.

--------------------------------------------------------------------
# **DHCP (Dynamic Host Configuration Protocol)

**DHCP** asigna automáticamente IPs a dispositivos en la red (evita que tengas que configurar manualmente cada IP).  
**Ejemplo:** cuando conectas tu teléfono al Wi-Fi, el router por DHCP le da una IP como `192.168.1.25`.

--------------------------------------------------------------------

# **🚗 TCP (Transmission Control Protocol)

Es como **un servicio de paquetería certificado (tipo Correos o Amazon Prime)**.

- Cada paquete llega **en orden**.
    
- Si algo se pierde, se vuelve a enviar.
    
- Muy **fiable**, pero un poco **más lento**.
    

👉 Ejemplo:

- Cuando cargas una **página web** o **descargas un archivo**,  
    necesitas que **todo llegue correcto**, sin errores.  
    → Por eso usan **TCP**.
    

# **✈️ UDP (User Datagram Protocol)

Es como **lanzar mensajes por walkie-talkie o gritar en un estadio**.

- Es **más rápido**, pero **no garantiza** que todos los mensajes lleguen.
    
- Perfecto para cosas **en tiempo real** donde la velocidad importa más que la perfección.
    

👉 Ejemplo:

- Videollamadas, juegos online, streaming, etc.  
    Si se pierde 1 milisegundo de sonido, no pasa nada, lo importante es que siga fluido.
    

➡️ En resumen:

|Protocolo|Fiabilidad|Velocidad|Ejemplo|
|---|---|---|---|
|TCP|Alta (garantiza entrega)|Menor|Web, Email, Archivos|
|UDP|Baja (puede perder paquetes)|Muy alta|Juegos, Llamadas, Streaming|

---

# **⚖️ Load Balancer (Balanceador de Carga)**

Un **load balancer** reparte el trabajo entre varios servidores  
para que ninguno se sobrecargue 💪

👉 Ejemplo fácil:  
Imagina una pizzería con **5 cocineros**.  
Si todos los pedidos van al mismo, se estresa.  
El jefe (el balanceador) reparte:

- Pedido 1 → Cocinero 1
    
- Pedido 2 → Cocinero 2
    
- Pedido 3 → Cocinero 3  
    Así todos trabajan parejo y la pizza llega más rápido 🍕.
    

👉 Ejemplo real:  
Cuando entras a YouTube, no te atiende un único servidor,  
sino uno de miles, según dónde estés y cuánta gente haya conectada.

➡️ En resumen:

> El **load balancer** es el **repartidor de tráfico** que evita que los servidores se saturen.

---

# IPs — Qué son realmente 

Tu idea básica está bien: una IP es un identificador para que los dispositivos se encuentren en la red. Ahora lo explico con más precisión y números.

## IPv4 — cuántas direcciones hay (paso a paso)

IPv4 usa 32 bits. Eso significa `2^32` direcciones en total.

Cálculo paso a paso:

- 210=10242^{10} = 1024210=1024
    
- 220=1024×1024=1 048 5762^{20} = 1024 \times 1024 = 1\,048\,576220=1024×1024=1048576
    
- 230=1 073 741 8242^{30} = 1\,073\,741\,824230=1073741824 (esto es 210×210×2102^{10} \times 2^{10} \times 2^{10}210×210×210)
    
- 232=230×22=1 073 741 824×4=4 294 967 2962^{32} = 2^{30} \times 2^2 = 1\,073\,741\,824 \times 4 = 4\,294\,967\,296232=230×22=1073741824×4=4294967296.
    

Entonces **IPv4 tiene 4,294,967,296 direcciones** en total (aprox. 4.29 mil millones).

> Problema práctico: muchísimas ya están reservadas (para redes privadas, multicast, loopback, etc.), por eso se empezó a usar IPv6.

## IPv6 — cuántas direcciones hay (y por qué "no nos vamos a quedar cortos")

IPv6 usa 128 bits: hay 21282^{128}2128 direcciones.

Ese número en decimal es:  
**340,282,366,920,938,463,463,374,607,431,768,211,456**  
(es decir, ~3.4 × 10^38).  
Conclusión: **prácticamente ilimitado para cualquier necesidad humana conocida**.

---

#  Clases de IP (históricas) y lo que significan

Antes se hablaba de “clases” A, B, C para dividir direcciones en bloques grandes/medios/pequeños. Hoy se usa CIDR (prefijos `/n`), pero la idea de clases te ayuda a entender tamaños:

- **Clase A (aprox):** equivalente a /8 → host bits = 24 → direcciones totales por red = 2^24 =16,777,216. Restando dirección de red y broadcast → **16,777,214 hosts usables**.  
    (Se diseñó para redes gigantes: ISPs grandes, empresas enormes).
    
- **Clase B (aprox):** equivalente a /16 → host bits = 16 → direcciones totales = 2^16= 65,536 -2 -> Usables = **65,534**.
    
- **Clase C (aprox):** equivalente a /24 → host bits = 8 → direcciones totales = 2^8=256
- Usables = **254** (256 menos la dirección de red y la de broadcast).
    

Notas:

- Las “clases” ya no son la forma recomendada; hoy se usan máscaras/prefijos `CIDR` como `/24`, `/16`, `/8`.
    
- Cuando dices “hasta 255 dispositivos” la cifra correcta es **254 hosts usables** en una /24 (porque 256 totales menos 2 reservadas).
    

---

#  Máscaras y subredes — explicado con ejemplos concretos

La **máscara** (o prefijo `/n`) indica cuántos bits de la IP corresponden a la **parte de red**. Los bits restantes son para **hosts** (dispositivos).

Ejemplos concretos:

- **/24** → host bits = 8 → direcciones totales =  2^8 = 256 → usables = **254**.
    
    - Red: `192.168.1.0/24` → hosts `192.168.1.1` … `192.168.1.254`.
        
    - `192.168.1.0` = dirección de red.
        
    - `192.168.1.255` = dirección de broadcast (envío a _todos_ los hosts de ese segmento).
        
- **/16** → host bits = 16 → totales = 2^16 = 65,536→ usables = **65,534**.
    
    - Ej: `172.16.0.0/16`.
        
- **/8** → host bits = 24 → totales = 2^24 = 16,777,216 → usables = **16,777,214**.
    
    - Ej: `10.0.0.0/8`.
        

¿Por qué no todas son `/24`?

- Depende de cuántos hosts necesitas en una red.
    
- `/24` es típico para redes pequeñas (oficina, casa). `/16` para campus/universidad; `/8` para enormes bloques. CIDR permite asignar exactamente lo que necesitas.
    

---

#  Red (LAN), router, direcciones públicas y privadas — aclaración y ejemplos

## LAN (Local Area Network)

- Es la **red local** que conecta tus dispositivos (ordenador, móvil, impresora) en una casa, oficina o aula.
    
- Normalmente administrada por un router/switch.
    
- Ejemplo: tu Wi-Fi en casa crea la LAN `192.168.1.0/24`.
    

## IP privada vs pública

- **IP privada**: dirección dentro de la LAN (no accesible directamente desde Internet). Rangos privados comunes:
    
    - `10.0.0.0/8` (10.x.x.x)
        
    - `172.16.0.0/12` (172.16.x.x–172.31.x.x)
        
    - `192.168.0.0/16` (192.168.x.x)
        
- **IP pública**: la dirección que tu ISP asigna a tu router y que es visible en Internet.
    

## ¿Un dispositivo tiene 2 IPs?

- El **dispositivo** suele tener **1 IP privada** en la LAN.
    
- El **router** tiene **1 IP pública** (la que ve Internet) y una IP privada (por ejemplo `192.168.1.1`) en la LAN.
    
- Gracias al **NAT** (Network Address Translation), **muchos dispositivos privados comparten una sola IP pública** cuando salen a Internet. Así que no necesitas que cada dispositivo tenga una IP pública distinta.
    

---

#  NAT (Network Address Translation) — cómo funciona con ejemplo

**Qué hace NAT:** cambia la dirección origen (privada) de los paquetes salientes por la IP pública del router, y gestiona las respuestas para devolverlas al dispositivo correcto.

Ejemplo práctico:

- Tu móvil `192.168.1.10` envía petición HTTP a `example.com`. Router reemplaza origen `192.168.1.10:54321` → `85.12.34.56:40001` (IP pública con puerto).
    
- Respuesta vuelve a `85.12.34.56:40001`; el router mira su tabla NAT y la redirige a `192.168.1.10:54321`.
    

**Port forwarding (reenvío de puertos):** si quieres que alguien de Internet acceda a un servidor en tu LAN, configuras el router para que reenvíe un puerto público a la IP privada del servidor.

---

# Broadcast y dirección de red — qué son

- **Dirección de red** (`network address`): identifica la red entera (ej. `192.168.1.0` en /24). No es asignable a dispositivos.
    
- **Broadcast**: dirección usada para enviar un mensaje a **todos** los dispositivos de esa subred (ej. `192.168.1.255` en /24). Tampoco se asigna a hosts.
    

Eso es por lo que al total de direcciones hay que restar 2 para obtener los hosts usables.

---

#  DNS y dominios — explicado punto por punto

**Dominio:** nombre que identifica un servicio en Internet (ej. `mipagina.com`). Es más fácil de recordar que una IP.

**DNS (Domain Name System):** la “agenda” de Internet que traduce `mipagina.com` → `IP`.

Proceso simplificado de resolución:

1. Escribes `mipagina.com` en el navegador.
    
2. Tu sistema pregunta al **resolver** (normalmente el del ISP o un DNS público como 1.1.1.1).
    
3. Si no está en caché, el resolver pregunta a los **servidores raíz**, luego al **servidor TLD** (`.com`), luego al **servidor autoritativo** del dominio y consigue la IP.
    
4. Tu navegador usa esa IP para conectarse.

---

# VPN — qué es exactamente y para qué sirve

**VPN (Virtual Private Network)** crea un **túnel cifrado** entre tu dispositivo y otro punto (un servidor o una red). Todo el tráfico viaja cifrado por ese túnel.

Usos típicos:

- **Acceso remoto seguro:** conectarte a la red de tu empresa desde casa como si estuvieras físicamente en la oficina.
    
- **Privacidad:** navegar como si estuvieras en la ubicación del servidor VPN (útil para acceder a contenido regional).
    
- **Cifrado en redes públicas:** protege frente a sniffing en Wi-Fi público.
    

Tipos:

- **Remote access VPN:** usuario individual conecta su PC/ móvil a una red (ej. empresa).
    
- **Site-to-site VPN:** conecta dos redes completas (sucursales).
    

Efecto en IP:

- Cuando te conectas por VPN, **tu tráfico sale desde la IP del servidor VPN** (aparece esa IP pública a los sitios web). No “añade” otra IP al dispositivo, sino que el túnel cambia la ruta del tráfico.
    

---

# URI, URL y URN — diferencia práctica (HAY QUE EXPLICARLO MEJOR PORQUE NO SE ENTIENDE)

- **URI (Uniform Resource Identifier):** identifica _qué_ es un recurso.
    
- **URL (Uniform Resource Locator):** es un tipo de URI que _dice cómo localizar_ el recurso (protocolo+dirección). Ej: `https://example.com/path?x=1`.
    
- **URN (Uniform Resource Name):** identifica un recurso por nombre en un espacio de nombres (menos usado): `urn:isbn:0451450523`.
    

Ejemplo de desglose de URL:  
`https://example.com:443/path/page.html?search=hola#section`

- `https` = esquema/protocolo
    
- `example.com` = host
    
- `:443` = puerto (opcional)
    
- `/path/page.html` = ruta
    
- `?search=hola` = query string (parámetros)
    
- `#section` = fragmento