#seguridad #hardware-hacking #gadgets #rubber-ducky #flipper-zero #badusb #rfid #pentesting #redteam

> [!info] Navegación
> ◀ Anterior: [[🛡️ 01 - Hardware de Privacidad y Defensa Táctica|Hardware Defensivo]] | 🗺️ Índice: [[🗺️ 00 - Índice de Seguridad Digital|Índice de Seguridad Digital]]

---

El acceso físico a un dispositivo suele significar el **compromiso total del sistema**. En esta guía cubrimos las herramientas físicas que usan los pentesters (Red Team) para auditorías autorizadas y que los atacantes reales también emplean.

> [!warning] Aviso legal
> Todos estos dispositivos son legales para comprar en la mayoría de países, **con la excepción de los inhibidores de frecuencia**. Sin embargo, utilizarlos contra sistemas sin autorización explícita es un **delito** tipificado en el Código Penal. Esta información es exclusivamente educativa y para auditorías autorizadas.

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
1. El atacante diseña el payload en casa usando **PayloadStudio**.
2. Graba el script en el Ducky.
3. Lo conecta al equipo objetivo.
4. En 2-5 segundos ejecuta todo el script sin que nadie lo vea.
5. Lo desenchufa y se va.

**¿Por qué es tan rápido?** El Ducky puede escribir a velocidades de hasta 1000 palabras por minuto — imposible para un humano.

### Dónde comprarlo
| Tienda | Precio | Link |
|---|---|---|
| **Hak5 Official Store** | ~$80 USD | [shop.hak5.org](https://shop.hak5.org/products/usb-rubber-ducky) |
| **KSEC EU (distribuidor UE)** | Precio similar + IVA | [ksec.co.uk](https://www.ksec.co.uk) |

---

## 🔌 2. Cable O.MG — El Espía Invisible

![[omg_cable.jpg]]

### Qué es exactamente
Creado por el investigador "MG" y distribuido por Hak5, el **O.MG Cable** es una obra maestra de la miniaturización maliciosa. Por fuera, **se ve exactamente igual, se siente igual y funciona igual que un cable de carga normal** (por ejemplo, el típico cable blanco USB a Lightning de Apple).

Pero oculto dentro del propio conector, incrustado en la resina, hay un microordenador que contiene un servidor web, un punto de acceso Wi-Fi y capacidades de BadUSB.

### Cómo funciona — Paso a paso
1. El atacante sustituye el cable legítimo de la víctima por el cable O.MG.
2. La víctima lo usa. **El cable carga el móvil y sincroniza datos perfectamente**, por lo que es imposible sospechar nada.
3. Al recibir corriente, el micro-implante se enciende y crea una **red Wi-Fi oculta**.
4. El atacante (que puede estar aparcado en la calle o en la oficina de al lado) se conecta a esa red Wi-Fi desde su móvil.
5. A través de una interfaz web en su navegador, el atacante inyecta comandos que viajan por Wi-Fi hasta el cable, y del cable entran al PC de la víctima como si alguien los estuviera tecleando.

> [!warning] Capacidades avanzadas (Keylogger)
> Las versiones *Elite* del O.MG Cable actúan como un registrador de pulsaciones (Keylogger). Graban todo lo que la víctima teclea en su ordenador (contraseñas, correos) y lo transmiten por Wi-Fi al atacante.

### Dónde comprarlo
| Tienda | Precio | Link |
|---|---|---|
| **Hak5 Official Store** | ~$150 - $200 USD | [shop.hak5.org/collections/o-mg-cable](https://shop.hak5.org/collections/o-mg-cable) |

---

## 🐰 3. Bash Bunny — El Pendrive Multiherramienta

![[bash_bunny.jpg]]

### Qué es exactamente
Mientras el Ducky solo emula un teclado, el **Bash Bunny contiene un sistema operativo Linux completo**. Puede emular **múltiples dispositivos simultáneamente**: un teclado + un adaptador Ethernet + un pendrive de almacenamiento.

### El interruptor de 3 posiciones
Tiene un pequeño interruptor físico en el lateral:
```
Posición 1 → Ejecuta Payload 1 (ej: ataque a Windows)
Posición 2 → Ejecuta Payload 2 (ej: ataque a Mac)
Posición 3 → Modo armado: lo conectas a tu PC para editar los payloads.
```

### El ataque más famoso (robo de hash NTLM)
Funciona incluso con el PC **completamente bloqueado**:
1. Conectas el Bash Bunny al PC bloqueado.
2. El PC lo detecta como un adaptador de red Ethernet ultrarrápido.
3. Windows prioriza esta "nueva red" para el tráfico.
4. El Bash Bunny usa `Responder` para pedir credenciales.
5. Windows envía automáticamente el hash NTLMv2 de la contraseña del usuario.
6. El hash se crackea luego offline.

### Dónde comprarlo
| Tienda | Precio | Link |
|---|---|---|
| **Hak5 Official Store** | ~$120 USD (suele agotarse) | [shop.hak5.org/products/bash-bunny](https://shop.hak5.org/products/bash-bunny) |

---

## 🐬 4. Flipper Zero — La Navaja Suiza del Hacking RF

![[flipper_zero.jpg]]

### Qué es exactamente
Con aspecto de juguete noventero (un delfín pixelado), es una potente multiherramienta de radiofrecuencia (RF), NFC, RFID e infrarrojos.

### Sus protocolos
- **Sub-GHz (300-928 MHz):** Lee y repite señales de mandos de garaje antiguos (sin rolling code), timbres inalámbricos, barreras de parking.
- **NFC (13.56 MHz):** Lee, guarda y emula tarjetas de acceso de hotel o empresa.
- **RFID (125 kHz):** Clona tarjetas de acceso RFID antiguas.
- **Infrarrojo:** Apaga TVs, proyectores o aires acondicionados.

### Mito vs Realidad
> [!note] Lo que los medios exageraron
> Titulares como "El Flipper Zero roba coches y vacía tarjetas" son **falsos**:
> - Los coches modernos usan *rolling codes* (el código cambia cada vez). El Flipper no puede abrir un coche moderno con solo grabarlo una vez.
> - Las tarjetas bancarias usan criptografía EMV. El Flipper no puede clonarlas ni hacer pagos.

### Dónde comprarlo
| Tienda | Precio | Link |
|---|---|---|
| **Flipper Devices (oficial)** | **$169 USD** | [flipper.net/flipperzero](https://flipper.net/flipperzero) |

---

## 🍍 5. WiFi Pineapple — El Router del Mal

![[wifi_pineapple.jpg]]

### Qué es exactamente
Un router especializado de Hak5 diseñado para realizar **ataques Man-in-the-Middle (MitM) vía Wi-Fi** de forma automatizada.

### El ataque Karma — Cómo funciona
Los móviles están continuamente preguntando al aire: *"¿Hay por aquí alguna red llamada 'Mi_Casa'?"*.
El Pineapple escucha esas preguntas y responde: *"¡Sí, soy yo, conéctate!"*. Los dispositivos se conectan a él creyendo que es su red de confianza.

### Flujo de un ataque en campo
1. El auditor enciende el Pineapple (con batería externa) en un área pública.
2. Activa el ataque Karma ("PineAP").
3. Los dispositivos del entorno se conectan a él de forma transparente.
4. Lanza un "Evil Portal" (una web de login falsa idéntica a la legítima) para capturar contraseñas.

---

## 💳 6. Proxmark3 RDV4 — El Bisturí del RFID

![[proxmark3.jpg]]

### Qué es exactamente
Es la herramienta profesional y estándar de la industria para **análisis avanzado y pentesting de RFID/NFC**. 

### Por qué complementa (y supera) al Flipper
Mientras el Flipper Zero te sirve para un escaneo rápido y emulación básica, el Proxmark3 es para hackear la criptografía subyacente de las tarjetas seguras:
- Revienta claves criptográficas de tarjetas **MIFARE Classic** usando ataques como MFOC/MFCUK.
- Analiza protocolos corporativos complejos como **DESFire** o iCLASS.
- Permite hacer **ataques de relay** (puentear la señal de la tarjeta original hasta un lector lejano).

### Dónde comprarlo
Cuesta entre **$300 y $350 USD**. Se recomienda comprar en distribuidores como **KSEC** o **Hacker Warehouse**.

---

## 📻 7. HackRF One — La Radio que Todo lo Ve

![[hackrf_one.jpg]]

### Qué es exactamente
El **HackRF One** es un SDR (Radio Definida por Software). Físicamente es una placa y una antena que captura ondas brutas entre **1 MHz y 6 GHz** y se las pasa a tu ordenador. Todo el "cerebro" (descodificar la onda, entenderla) se hace por software.

### Para qué sirve y por qué complementa a los demás
- **El Flipper Zero** trae "recetas" hechas para protocolos muy específicos (NFC, mandos de garaje).
- **El Proxmark3** es exclusivo para sistemas de proximidad (RFID/NFC).
- **El HackRF One** es un lienzo en blanco absoluto. Literalmente te permite **"ver la Matrix del mundo invisible de las ondas"**. 

Puedes interceptar y visualizar en pantalla cualquier señal que flote en el aire: radares de aviones (ADS-B), comunicaciones de satélites meteorológicos, señales de llaves de coches, redes de telefonía GSM, telemetría de drones, etc. 

### Curva de Aprendizaje y Temario (Primeros Pasos)
> [!warning] Curva de aprendizaje MUY alta
> El HackRF no es "enchufar y hackear". Si no programas el software, el aparato no hace nada. Requiere comprender conceptos físicos de telecomunicaciones y procesado de señales.

**Plan de estudio recomendado si compras un HackRF:**
1. **Fundamentos de Radio:** Aprender qué es frecuencia, amplitud, modulación (AM/FM/FSK/QAM) y el espectro electromagnético.
2. **Exploración visual (GQRX):** Usar el programa `GQRX` para moverte por el espectro, ver las ondas como picos y escuchar emisoras de radio FM, walkie-talkies o servicios analógicos sin cifrar.
3. **Decodificación digital:** Aprender a usar software puente como `dump1090` para cazar transpondedores de aviones comerciales y pintarlos en un mapa.
4. **Ingeniería Inversa (GNU Radio):** El paso final. Usar *GNU Radio Companion* para grabar la señal digital de un sensor IoT, aislar los "unos y ceros" de la onda, y construir un diagrama de bloques para enviar de vuelta la misma señal modificada (*Replay Attack*).

### Dónde comprarlo
Su precio ronda los **$300-$350 USD** en **Astroradio** (España) o **Great Scott Gadgets**.

---

## 🔐 8. Herramientas de Infiltración de Red (Hak5)

Estos dispositivos buscan establecer *backdoors* en redes LAN con acceso físico.

### 🐢 LAN Turtle
![[lan_turtle.jpg]]
Un adaptador USB-a-Ethernet con un sistema Linux dentro.
- **Uso:** El atacante lo enchufa detrás de la torre del PC de la oficina.
- **Acción:** Crea un **túnel SSH inverso** permanente hacia el servidor del atacante, dándole acceso remoto total a la red interna desde su casa.

### 🦈 Shark Jack
![[shark_jack.jpg]]
Un pincho Ethernet autónomo de bolsillo.
- **Uso:** Se conecta directamente a una toma de red en la pared o a un router.
- **Acción:** En 60 segundos escanea silenciosamente la subred con `nmap`, captura hashes y guarda todo en su interior. Te lo llevas un minuto después.

### 🐿️ Packet Squirrel
![[packet_squirrel.jpg]]
Un interceptor pasivo (Network Tap).
- **Uso:** Se conecta "en medio" del cable de red entre un PC y la toma de pared.
- **Acción:** Copia silenciosamente todo el tráfico de red (archivos pcap) hacia un USB o por VPN sin interrumpir la conexión de la víctima.

---

## 📇 9. Hardware Histórico: RFIDler
El **RFIDler** (creado por Aperture Labs) fue una herramienta pionera en la investigación y manipulación de señales RFID de baja frecuencia (125kHz).

Actualmente es un proyecto **descatalogado**. Si bien fue vital para la comunidad hacker hace una década, a día de hoy ha sido completamente reemplazado por dispositivos modernos y con soporte activo como el **Proxmark3 RDV4** y el **Flipper Zero**. Es un componente histórico de esta disciplina.

---

## 🚫 10. Inhibidores de Frecuencia (Signal Jammers)

Pediste buscar esto en la sección 01 (defensa), pero **no pertenece allí**. Un inhibidor no es un dispositivo de privacidad ni de defensa, es un arma de ataque electrónico puro.

### Qué son exactamente
Un inhibidor de frecuencia es un dispositivo que emite "ruido blanco" de radio a una potencia extremadamente alta en bandas específicas (Wi-Fi, 3G/4G/5G, GPS, Bluetooth).

Al emitir tanto ruido de forma caótica, "grita" más fuerte que los dispositivos legítimos. Resultado: los móviles se quedan sin cobertura, el Wi-Fi se satura por completo, el GPS se "ciega" y **las alarmas de seguridad de las casas dejan de comunicar con las centrales**. Es un ataque de Denegación de Servicio (DoS) en el mundo físico.

### Marco Legal: Totalmente Ilegales en España y Europa

> [!CAUTION] Riesgo Penal Gravísimo
> En España, el uso, tenencia, venta, importación o instalación de inhibidores de frecuencia por parte de civiles **es estrictamente ilegal** bajo la Ley 11/2022 General de Telecomunicaciones. Solo las fuerzas y cuerpos de seguridad del Estado pueden usarlos.
>
> **¿Por qué?** Porque su uso bloquea redes críticas como el **112**, interfiere con ambulancias, radares aéreos, servicios de policía y redes pacíficas.
>
> - **Sanciones:** Consideradas infracciones muy graves, las multas por encender uno de estos dispositivos pueden llegar hasta **los 20 millones de euros** y conllevar penas de prisión, especialmente si se asocian a actividades delictivas (como robar coches o asaltar casas bloqueando la alarma).

---

## 🔓 11. Ganzúas y Lockpicking

![[lockpicks.jpg]]

### Por qué forma parte del pentesting de IT
La seguridad digital no existe sin seguridad física. Un servidor blindado lógicamente queda comprometido si alguien abre la puerta del CPD con una ganzúa en 15 segundos. Las auditorías *Red Team* maduras incluyen una fase de intrusión física con:
- **Set de ganzúas básico:** Raking y *single pin picking*.
- **Bump Keys:** Llaves maestras percutidas que abren cerraduras de pines por impacto.
- **Pick Guns:** Pistolas eléctricas o mecánicas que hacen saltar los pines a altísima velocidad.
- **Under-the-Door Tool:** Cable articulado para abrir manivelas desde debajo de la puerta.

> [!info] Legalidad en España
> Poseer ganzúas en casa como herramienta de cerrajería deportiva (Lockpicking) no es ilegal per se. Sin embargo, llevarlas encima en la vía pública puede acarrear problemas legales graves si las fuerzas del orden interpretan (según las circunstancias) que son útiles portados para cometer un robo.

---

## 📊 Tabla Resumen Completa

| Dispositivo | Vector Principal | Nivel | Precio aprox. | Dónde comprar |
|---|---|---|---|---|
| 🦆 USB Rubber Ducky | BadUSB / Inyección HID | Principiante | ~$80 USD | Hak5 / KSEC |
| 🔌 O.MG Cable | BadUSB invisible por Wi-Fi | Intermedio | ~$150 USD | Hak5 |
| 🐰 Bash Bunny | BadUSB + Adaptador de Red | Intermedio | ~$120 USD | Hak5 / KSEC |
| 🐬 Flipper Zero | RF / NFC / IR básico | Principiante | $169 USD | flipper.net |
| 🍍 WiFi Pineapple | MitM Wi-Fi / Phishing | Intermedio | ~$120 USD | Hak5 / KSEC |
| 💳 Proxmark3 RDV4 | RFID/NFC criptografía avanzada | Avanzado | ~$300 USD | KSEC / Hacker Warehouse |
| 📻 HackRF One | SDR (Análisis de ondas en bruto) | Avanzado | ~$350 USD | Astroradio / Great Scott |
| 🐢 LAN Turtle | Backdoor de red (SSH) | Intermedio | ~$80 USD | Hak5 |
| 🦈 Shark Jack | Escaneo rápido LAN (Nmap) | Intermedio | ~$100 USD | Hak5 |
| 🐿️ Packet Squirrel | Network Tap pasivo (Sniffing) | Intermedio | ~$60 USD | Hak5 |
| 📇 RFIDler | LF RFID (Legacy) | Obsoleto | Descatalogado | N/A |
| 🚫 Inhibidor (Jammer) | Bloqueo RF / DoS físico | N/A | **ILEGAL** | N/A |
| 🔓 Ganzúas / Kit | Seguridad física (Cerraduras) | Principiante | ~30€ | multipick.com |
