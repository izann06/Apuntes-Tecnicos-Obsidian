#seguridad #hardware-hacking #gadgets #rubber-ducky #flipper-zero #badusb #rfid #pentesting #redteam

> [!info] Navegación
> ◀ Anterior: [[🛡️ 01 - Hardware de Privacidad y Defensa Táctica|Hardware Defensivo]] | 🗺️ Índice: [[🗺️ 00 - Índice de Seguridad Digital|Índice de Seguridad Digital]]

---

El acceso físico a un dispositivo suele significar el **compromiso total del sistema**. En esta guía cubrimos las herramientas físicas que usan los pentesters (Red Team) para auditorías autorizadas y que los atacantes reales también emplean.

> [!warning] Aviso legal
> Todos estos dispositivos son legales para comprar en la mayoría de países. Sin embargo, utilizarlos contra sistemas sin autorización explícita es un **delito** tipificado en el Código Penal. Esta información es exclusivamente educativa y para auditorías autorizadas.

---

## 🦆 1. USB Rubber Ducky — El Teclado Asesino

![[rubber_ducky.jpg]]

### Qué es exactamente

El Rubber Ducky es fabricado por **Hak5** (la empresa de referencia en hardware de pentesting). Físicamente parece un pendrive USB normal. La diferencia está en sus tripas: en lugar de un controlador de almacenamiento, lleva un **microcontrolador que se presenta al ordenador como un teclado USB (HID — Human Interface Device)**.

El sistema operativo no sospecha absolutamente nada. Confía en los teclados. No hay antivirus que bloquee "alguien escribiendo en el teclado". En el momento en que se conecta, empieza a ejecutar su script de comandos.

### Cómo funciona — Paso a Paso

Los ataques se programan en **DuckyScript**, un lenguaje de scripting muy sencillo que cualquiera puede aprender:

```ducky
# Script ejemplo: Abrir PowerShell y descargar un archivo
DELAY 1000           # Espera 1 segundo a que el PC lo reconozca como teclado
GUI r                # Pulsa Windows+R (abre el cuadro "Ejecutar")
DELAY 300
STRING powershell -WindowStyle Hidden -Command "..."
# -WindowStyle Hidden → la ventana no aparece visiblemente
ENTER
```

**El flujo de un ataque real:**
1. El atacante diseña el payload en casa usando **PayloadStudio** (la IDE online de Hak5).
2. Graba el script en el Ducky.
3. Lo conecta al equipo objetivo.
4. En 2-5 segundos ejecuta todo el script (descarga, instalación, limpieza de rastros) sin que nadie lo vea.
5. Lo desenchufa y se va.

**¿Por qué es tan rápido?** El Ducky puede escribir a velocidades de hasta 1000 palabras por minuto — imposible para un humano. El PC lo procesa como si fuera un mecanógrafo sobrehumano.

### Cómo protegerse de él

- **Deshabilitar puertos USB no usados** en la BIOS.
- **Políticas de dispositivos HID** en Windows (Group Policy → solo permitir teclados registrados).
- **No dejar el equipo desbloqueado** ni un solo momento con extraños cerca.

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Hak5 Official Store** | Ver precio actual | [shop.hak5.org](https://shop.hak5.org/products/usb-rubber-ducky) |
| **KSEC EU (distribuidor oficial UE)** | Precio similar + IVA | [ksec.co.uk](https://www.ksec.co.uk) |
| **Lab401 (distribuidor EU)** | Precio similar | [lab401.com](https://lab401.com) |

> [!tip] Cómo comprar desde España
> Hak5 envía desde California, lo que implica gastos de aduana. Para evitarlos, compra a través de **KSEC** o **Lab401**, distribuidores oficiales autorizados dentro de la Unión Europea.

---

## 🐰 2. Bash Bunny — El Pendrive Multiherramienta

![[bash_bunny.jpg]]

### Qué es exactamente

El hermano mayor del Rubber Ducky, también de Hak5. Mientras el Ducky solo puede hacer una cosa (emular teclado), el **Bash Bunny contiene un sistema operativo Linux completo** en un formato de USB. Puede emular **múltiples dispositivos simultáneamente**: un teclado + un adaptador Ethernet + un pendrive de almacenamiento, todo al mismo tiempo.

### El interruptor de 3 posiciones — Su característica clave

El Bash Bunny tiene un pequeño interruptor físico en el lateral con 3 posiciones:

```
Posición 1 → Ejecuta Payload 1 (ej: ataque a Windows con Responder)
Posición 2 → Ejecuta Payload 2 (ej: exfiltración de credenciales Mac)
Posición 3 → Modo armado (arming mode): lo pones en modo configuración
              para editar los payloads cómodamente desde tu PC
```

### Cómo funciona — El ataque más famoso (robo de hash NTLM)

Este ataque funciona incluso con el PC **completamente bloqueado** (pantalla de bloqueo de Windows):

```
1. Conectas el Bash Bunny al puerto USB del PC bloqueado.
2. El PC lo detecta como un adaptador de red Ethernet.
3. Windows prioriza la red más rápida para el tráfico → elige el Bash Bunny.
4. El Bash Bunny ejecuta "Responder": un servidor que intercepta
   las peticiones de autenticación automáticas que hace Windows.
5. Windows, sin que nadie lo pida, envía el hash NTLMv2 de la contraseña
   del usuario al Bash Bunny intentando autenticarse en la "red".
6. Hash capturado → se crackea offline con hashcat/John The Ripper.

Tiempo total: 30-60 segundos. Con el PC bloqueado. Sin tocar nada.
```

### Dónde comprarlo

| Tienda | Estado | Link |
|---|---|---|
| **Hak5 Official Store** | Puede estar agotado (demanda alta) | [shop.hak5.org/products/bash-bunny](https://shop.hak5.org/products/bash-bunny) |
| **KSEC EU** | Consultar stock | [ksec.co.uk](https://www.ksec.co.uk) |

> [!warning] Agotado frecuentemente
> El Bash Bunny Mark II suele tener problemas de stock. Puedes apuntarte a las notificaciones en la web oficial de Hak5 para saber cuándo vuelve.

---

## 🐬 3. Flipper Zero — La Navaja Suiza del Hacking RF

![[flipper_zero.jpg]]

### Qué es exactamente

El Flipper Zero es el dispositivo de hacking más popular de los últimos años entre la comunidad de ciberseguridad. Tiene un aspecto de juguete de los años 90 (con su delfín pixelado en la pantalla) pero esconde capacidades multiprotocolo reales. Fue financiado en Kickstarter en 2020 y superó su objetivo en más de 2000%.

**Web oficial (importante):** [flipper.net](https://flipper.net) — el antiguo `flipperzero.one` ya no es oficial.

### Sus protocolos — Qué puede hacer de verdad

**Sub-GHz (300-928 MHz):**
Puede leer, grabar y repetir señales de radio de baja frecuencia. Funciona con mandos de garaje **antiguos** (sin rolling code), barreras de parking, mandos de puertas. Los coches y garajes modernos usan rolling codes (cambian con cada uso) y NO son vulnerables al simple replay.

**NFC (13.56 MHz):**
Lee tarjetas NFC, las guarda en memoria y puede emularlas. Sirve para auditar tarjetas de acceso de hotel, pases de transporte público (abono), tarjetas de empresa con protocolo NFC básico.

**RFID (125 kHz):**
Lee y clona tarjetas de acceso RFID de baja frecuencia. Son las tarjetas de empresa de los años 90-2000, sin ninguna criptografía. Muchas oficinas todavía las usan.

**Infrarrojo:**
Base de datos de comandos IR de miles de dispositivos. Puede apagar televisores, controlar aires acondicionados, proyectores.

**BadUSB:**
Conectado por cable a un PC, puede actuar como Rubber Ducky básico inyectando scripts HID.

**GPIO y protocolos digitales:**
Interfaz de pines para comunicarse con hardware electrónico usando UART, SPI, I2C — para desarrollo y hardware hacking avanzado.

### Cómo se usa — Ejemplo real paso a paso

```
Escenario: Leer y emular una tarjeta RFID 125 kHz de empresa

1. En el menú del Flipper: 125 kHz RFID → Read
2. Acercas el Flipper a la tarjeta de acceso objetivo (a <5 cm)
3. El Flipper lee los datos de la tarjeta y los muestra en pantalla
4. Guardas la tarjeta con un nombre: "Tarjeta_Oficina"
5. Para emularla: 125 kHz RFID → Saved → Tarjeta_Oficina → Emulate
6. Acercas el Flipper al lector de acceso en lugar de la tarjeta
7. La puerta se abre como si fuera la tarjeta original
```

### Mito vs Realidad

> [!note] Lo que los medios exageraron
> En 2022, varios medios publicaron titulares como "El Flipper Zero puede robar coches y vaciar tu tarjeta bancaria". Esto es **falso**:
> - Los coches modernos usan rolling codes → inmunes al replay del Flipper.
> - Las tarjetas bancarias (Visa/MasterCard) usan EMV con criptografía fuerte → el Flipper no puede clonarlas.
> - Lo que SÍ puede afectar: sistemas RFID legacy sin cifrado (muchas oficinas, hoteles viejos, transporte público en algunos países).

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Flipper Devices (oficial)** | **$169 USD** | [flipper.net/flipperzero](https://flipper.net/flipperzero) |
| **Amazon ES** | ~180-200€ | Buscar "Flipper Zero" (verificar vendedor oficial) |

> [!warning] Cuidado con falsificaciones
> Han aparecido clones del Flipper Zero en AliExpress. Solo compra en **flipper.net** o distribuidores oficiales listados en su web. Un clon puede tener firmware malicioso.

---

## 🍍 4. WiFi Pineapple — El Router del Mal

![[wifi_pineapple.jpg]]

### Qué es exactamente

El WiFi Pineapple de Hak5 es un router especializado diseñado para realizar **ataques Man-in-the-Middle (MitM) vía Wi-Fi** de forma automatizada. Lo que en un router normal requeriría configuración compleja y conocimientos avanzados, aquí se hace con un par de clics desde una interfaz web.

### El ataque Karma — Cómo funciona

Los dispositivos (móviles, portátiles) guardan listas de redes Wi-Fi a las que se han conectado antes. Y están continuamente preguntando al aire: *"¿Hay por aquí alguna red llamada 'Casa_de_Izar'? ¿Y la red del trabajo? ¿Y la del aeropuerto?"*

El Pineapple escucha esas preguntas y responde a todas ellas: *"¡Sí, soy yo, conéctate!"*. Los dispositivos se conectan automáticamente creyendo que están en su red de confianza.

### Cómo funciona — Paso a paso de un ataque en campo

```
Escenario: Auditoría en un café (autorizada)

1. El auditor enciende el Pineapple en su mochila (batería externa).
2. Abre la interfaz web del Pineapple desde su móvil (192.168.0.1).
3. Activa el módulo "PineAP" (karma attack) → el Pineapple empieza
   a responder a todas las sondas Wi-Fi que detecta.
4. Los dispositivos del entorno se conectan automáticamente al Pineapple.
5. El auditor puede:
   a) Ver todo el tráfico HTTP no cifrado (contraseñas sin HTTPS).
   b) Activar el "Evil Portal": redirigir a los usuarios a una página
      de login falsa idéntica a la de la cafetería para capturar emails.
   c) Lanzar módulos adicionales (SSLstrip, DNS spoofing, etc.).
6. Al finalizar, genera un informe de todo lo capturado.
```

### Por qué HTTPS te protege de esto

Aunque estés conectado al Pineapple, si la web que visitas usa **HTTPS** (TLS), el tráfico va cifrado de extremo a extremo. El Pineapple solo ve tráfico cifrado incomprensible. La defensa contra este ataque es tan simple como verificar siempre el candado verde y no ignorar advertencias de certificados.

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Hak5 Official Store** | Ver precio actual | [shop.hak5.org](https://shop.hak5.org/products/wifi-pineapple) |
| **KSEC EU (distribuidor oficial)** | Precio + envío EU | [ksec.co.uk](https://www.ksec.co.uk) |
| **Lab401** | Distribuidor oficial EU | [lab401.com](https://lab401.com) |

---

## 💳 5. Proxmark3 RDV4 — El Bisturí del RFID

![[proxmark3.jpg]]

### Qué es exactamente

El Proxmark3 es la herramienta profesional de referencia para **análisis, investigación y pentesting de sistemas RFID y NFC**. No es un gadget de consumo — es un instrumento de laboratorio. La diferencia con el Flipper Zero es como comparar un bisturí de cirujano con un cuchillo de cocina.

El firmware oficial que se usa es el **Iceman/RRG Firmware**, mantenido activamente por la comunidad y mucho más potente que el firmware original.

### Qué puede hacer que el Flipper no puede

- Leer tarjetas **MIFARE Classic** y realizar el ataque **MFOC/MFCUK** para recuperar las claves criptográficas por fuerza bruta o ataque de claves conocidas.
- Leer y analizar tarjetas **DESFire** (las más comunes en accesos corporativos modernos).
- Realizar **ataques de relay** en tarjetas NFC (el atacante acerca una antena a la tarjeta original y la otra al lector objetivo a distancia).
- Sniffing pasivo de comunicaciones RFID entre tarjeta y lector en tiempo real.

### Cómo funciona — Ejemplo de lectura y análisis

```bash
# Conectar el Proxmark3 por USB al PC y abrir el cliente:
./pm3

# Detectar qué tipo de tarjeta hay cerca:
pm3 --> auto

# Si detecta MIFARE Classic, intentar recuperar las claves:
pm3 --> hf mf autopwn
# Ejecuta una batería completa de ataques automáticamente.
# Si tiene éxito, vuelca todo el contenido de la tarjeta.

# Clonar la tarjeta a una tarjeta en blanco:
pm3 --> hf mf restore --1k --uid <uid_leido>

# Emular la tarjeta sin necesidad de clonarla:
pm3 --> hf mf sim --1k --uid <uid>
```

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Hacker Warehouse** | ~$300-350 USD (kit) | [hackerwarehouse.com](https://hackerwarehouse.com) |
| **KSEC EU (distribuidor oficial)** | Precio similar + IVA EU | [ksec.co.uk](https://www.ksec.co.uk) |
| **MTools Tec** | ~$300-350 USD | [mtoolstec.com](https://www.mtoolstec.com) |

> [!warning] Evita AliExpress y eBay
> Existen muchísimos clones del Proxmark3 baratos (~$40-60). Funcionan parcialmente pero son incompatibles con el firmware oficial Iceman y no sirven para ataques avanzados. Un Proxmark3 auténtico RDV4 cuesta ~$300 por una razón.

---

## 📻 6. HackRF One — La Radio que Todo lo Ve

![[hackrf_one.jpg]]

### Qué es exactamente

El **HackRF One** de Great Scott Gadgets es un **SDR (Software Defined Radio)**: una radio cuyo hardware solo captura y emite señales, y todo el procesamiento de esas señales se hace en software en tu PC. Cubre de **1 MHz a 6 GHz**, abarcando prácticamente cualquier señal de radio de uso civil.

Una radio convencional solo puede sintonizar frecuencias de FM/AM. El HackRF puede procesar **cualquier señal** en ese rango descomunal.

### Qué puede hacer — El espectro a tu disposición

| Frecuencia | Qué hay ahí |
|---|---|
| 87-108 MHz | Radio FM comercial |
| 433 / 868 MHz | Mandos de garaje, sensores IoT, alarmas |
| 315 / 433 MHz | Mandos de coche antiguos |
| 1090 MHz | ADS-B: posición de todos los aviones en vuelo |
| 1575 MHz | Señal GPS |
| 2.4 GHz | Wi-Fi, Bluetooth, drones |
| 5.8 GHz | Wi-Fi 5 GHz, vídeo FPV de drones |

### Cómo empezar — Software necesario

```bash
# Linux (instalación básica):
sudo apt install gqrx-sdr     # Receptor visual de espectro (el más fácil para empezar)
sudo apt install gnuradio      # Suite completa de procesado de señal
sudo apt install hackrf        # Drivers y utilidades de línea de comandos

# Primer uso con GQRX (ver el espectro de radio):
gqrx
# 1. Selecciona "HackRF One" como dispositivo de entrada.
# 2. Ajusta la frecuencia a 100.0 MHz (radio FM).
# 3. Verás las emisoras como picos en el espectro.
# 4. Haz clic en un pico → escuchas la radio en tiempo real.
```

**Escuchar aviones (ADS-B) — Ejemplo práctico para empezar:**

```bash
# Instala dump1090 (decodificador ADS-B):
sudo apt install dump1090-mutability

# Ejecuta y abre el navegador en localhost:8080
dump1090 --interactive --net

# Verás en tiempo real todos los aviones cercanos con:
# - Vuelo, altitud, velocidad, posición GPS
# - Se muestra en un mapa interactivo
```

### Marco legal — Muy importante

> [!warning] Transmitir es ilegal sin licencia
> Usar el HackRF **solo para recibir y analizar señales** es completamente legal en España y la UE.
>
> **Transmitir** señales en frecuencias sin licencia es ilegal según la Ley General de Telecomunicaciones y puede acarrear multas de hasta 500.000€ y responsabilidad penal.
>
> Los radioaficionados con licencia (examen HAREC/CEPT) pueden transmitir en las bandas autorizadas.

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Great Scott Gadgets (resellers oficiales)** | ~$300-350 USD | [greatscottgadgets.com/where-to-buy](https://greatscottgadgets.com/where-to-buy/) |
| **Astroradio (España, distribuidor oficial)** | ~310€ | [astroradio.com](https://www.astroradio.com) |
| **Nooelec (con bundle de antenas)** | ~$350+ USD | [nooelec.com](https://www.nooelec.com) |

> [!tip] HackRF Pro — El sucesor
> Great Scott Gadgets ha lanzado el **HackRF Pro**, con rango de frecuencias extendido, USB-C y mayor precisión. Si vas a comprar uno nuevo, infórmate en su web sobre disponibilidad del Pro.

---

## 🔐 7. LAN Turtle, Shark Jack y Packet Squirrel — Los Espías de Red

Estos tres dispositivos de Hak5 comparten el mismo propósito: **infiltrarse silenciosamente en una red local** desde dentro. Se compran todos en [shop.hak5.org](https://shop.hak5.org).

### 🐢 LAN Turtle

Un adaptador USB-a-Ethernet con un sistema Linux completo dentro. Se conecta entre el cable de red y el PC de la víctima.

**Qué hace:**
- Establece un **túnel SSH inverso** permanente hacia el servidor del atacante.
- Ejecuta scripts de reconocimiento de red de forma autónoma.
- El PC de la víctima funciona con total normalidad.

**Caso real:**
```
El auditor entra a la oficina con excusa de "técnico de mantenimiento".
Conecta la Turtle detrás de una torre de PC junto a la pared.
Sale de la oficina.
Desde su casa, abre el túnel SSH → tiene acceso a toda la red interna
de la empresa de forma continua hasta que alguien encuentre el dispositivo.
```

### 🦈 Shark Jack

Un pincho Ethernet autónomo de bolsillo. Se conecta a un puerto de red libre (en un switch, toma de pared) y ejecuta automáticamente herramientas de reconocimiento.

**En 60 segundos puede:**
- Escanear toda la subred con `nmap`
- Capturar hashes NTLMv2 con `Responder`
- Guardar todo en memoria interna

**Lo recoges 5 minutos después y te vas.** Los datos están en el dispositivo.

### 🐿️ Packet Squirrel

Un interceptor pasivo (Network Tap) que se conecta en línea entre dos puntos de red.

**Captura silenciosamente:**
- Todo el tráfico que pasa por él (pcaps completos)
- Puede exfiltrar por túnel VPN a un servidor externo en tiempo real
- La víctima no percibe ninguna degradación del rendimiento

---

## 🔓 8. Ganzúas y Lockpicking — El Hacking Más Antiguo

### Por qué forma parte del pentesting de IT

La seguridad digital no existe sin seguridad física. Un servidor con cifrado AES-256 y firewall de última generación queda comprometido si alguien abre la puerta del CPD en 15 segundos con una ganzúa.

Las **auditorías Red Team completas** siempre incluyen una fase de intrusión física:
- Intentar abrir cerraduras de armarios rack.
- Abrir puertas de salas de servidores.
- Acceder a zonas restringidas mediante bump keys o pick guns.

### Herramientas básicas de lockpicking

| Herramienta | Uso | Precio |
|---|---|---|
| **Set de ganzúas básico** | Raking y single pin picking | ~20-40€ |
| **Bump Keys** | Abre la mayoría de cerraduras de pines con golpeo | ~15-30€ |
| **Pick Gun eléctrica** | Abre cerraduras en segundos, muy efectiva | ~40-80€ |
| **Under-the-Door Tool** | Abre puertas con manivela desde el exterior | ~60-100€ |

**Dónde comprar (España):**
- [multipick.com](https://www.multipick.com) — fabricante alemán de referencia
- [lockpickworld.com](https://www.lockpickworld.com)

> [!warning] Legalidad en España
> Poseer ganzúas en España **no es ilegal por sí mismo** (no están en la lista de útiles especialmente aptos para robo si no hay intención delictiva probada). Sin embargo, llevarlas encima en situación sospechosa puede considerarse tenencia de útiles para robo. Úsalas solo en entrenamientos propios o con autorización escrita del propietario.

---

## 📊 Tabla Resumen Completa

| Dispositivo | Vector | Nivel | Precio aprox. | Dónde comprar |
|---|---|---|---|---|
| 🦆 USB Rubber Ducky | BadUSB / HID | Principiante | ~$80 USD | [shop.hak5.org](https://shop.hak5.org) |
| 🐰 Bash Bunny Mark II | BadUSB + Red | Intermedio | ~$120 USD | [shop.hak5.org](https://shop.hak5.org) |
| 🐬 Flipper Zero | RF / NFC / RFID / BadUSB | Principiante/Medio | **$169 USD** | [flipper.net](https://flipper.net) |
| 🍍 WiFi Pineapple | MitM Wi-Fi | Intermedio | Ver en web | [shop.hak5.org](https://shop.hak5.org) |
| 💳 Proxmark3 RDV4 | RFID/NFC avanzado | Avanzado | ~$300-350 USD | [ksec.co.uk](https://www.ksec.co.uk) |
| 📻 HackRF One | SDR / Radiofrecuencia | Avanzado | ~$300-350 USD | [astroradio.com](https://www.astroradio.com) |
| 🐢 LAN Turtle | Backdoor de red | Intermedio | ~$80 USD | [shop.hak5.org](https://shop.hak5.org) |
| 🦈 Shark Jack | Reconocimiento LAN | Intermedio | ~$100 USD | [shop.hak5.org](https://shop.hak5.org) |
| 🐿️ Packet Squirrel | Network Tap pasivo | Intermedio | ~$60 USD | [shop.hak5.org](https://shop.hak5.org) |
| 🔓 Ganzúas / Kit | Seguridad física | Principiante | ~20-80€ | [multipick.com](https://www.multipick.com) |
