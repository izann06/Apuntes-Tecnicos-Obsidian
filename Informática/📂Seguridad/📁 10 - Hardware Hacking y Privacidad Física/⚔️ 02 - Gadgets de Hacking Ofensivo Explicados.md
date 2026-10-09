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

## 💾 2. Bash Bunny y O.MG Cable: Robo y Transferencia de Datos

Ambos son dispositivos de inyección física (actúan como un teclado superrápido) orientados a **extraer datos** de un ordenador y llevártelos. 

> [!warning] Requisito indispensable
> El ordenador objetivo debe estar encendido y con la sesión de usuario desbloqueada.

### Bash Bunny
![[bash_bunny.jpg]]

Es un microordenador Linux con forma de pendrive que emula teclado, almacenamiento masivo y tarjeta de red a la vez.

- **Cómo extrae datos:** Al conectarlo, abre una terminal oculta (como [[PowerShell]]), busca archivos específicos (ej. fotos, PDFs, contraseñas de Chrome) y los copia directamente a la memoria interna del propio Bash Bunny.
- **Precio:** ~200 €.

> [!EXAMPLE]
> Un payload típico de [[Bash Bunny]] tarda menos de 4 segundos en abrir la consola, volcar las credenciales cacheadas de Windows en un archivo de texto, guardarlo en su memoria USB particionada y cerrar la ventana sin que la víctima tenga tiempo de reaccionar.

### O.MG Cable
![[omg_cable.jpg]]

Es un cable aparentemente normal (USB a USB-C/Lightning) que esconde un chip [[Wi-Fi]] diminuto.

- **Cómo extrae datos:** Alguien conecta su móvil al PC con este cable. Tú, desde otra habitación, te conectas a la red Wi-Fi oculta del cable con tu móvil. Le ordenas abrir una terminal oculta en el PC, buscar los archivos y te los envía a tu pantalla a través del aire.
- **Precio:** ~200 € - 295 € (Versiones Elite).

### Curva de aprendizaje y Utilidad
- **Curva Baja-Media:** Utilizan [[DuckyScript]], un lenguaje muy fácil de aprender que simplemente simula teclas pulsadas, combinado con scripts básicos de [[Bash]] o PowerShell.
- **Utilidad:** Muy alta para intrusiones físicas rápidas o para demostrar a empresas el peligro de dejar sesiones desbloqueadas.

---

## 🐬 3. Flipper Zero — La Navaja Suiza del Hacking RF

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

## 🍍 4. WiFi Pineapple — El Router del Mal

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

## 💳 5. Proxmark3: El Rey del Control de Accesos

![[proxmark3.jpg]]

Es la herramienta definitiva para clonar e investigar tarjetas físicas, llaves de proximidad y abonos de transporte.

### Usos
- **Clonar y emular tarjetas antiguas [[RFID]]** (125 kHz) como garajes, gimnasios o portales comunes.
- **Auditar y descifrar tarjetas inteligentes modernas [[NFC]]** (13.56 MHz) mediante ataques criptográficos (ej. tarjetas de fichar en oficinas de alta seguridad).

### Precios
- **Versión Proxmark3 Easy (Clon funcional):** ~50 € - 80 €.
- **Versión Proxmark3 RDV4 (Oficial para profesionales):** ~350 € - 400 €.

### Curva de aprendizaje y Utilidad
- **Curva Media-Alta:** Funciona puramente por línea de comandos (CLI) y requiere entender formatos de bloques de memoria.
- **Utilidad:** Máxima. Es indispensable si auditas seguridad física de edificios o sistemas de identificación personal.

> [!TIP]
> Si solo quieres clonar tu llave del portal rápidamente sin aprender criptografía, el [[Flipper Zero]] es más amigable. El [[Proxmark3]] es para auditorías profesionales profundas.

---

## 📻 6. HackRF One: El Dominio de la Radiofrecuencia

![[hackrf_one.jpg]]

Es un transceptor [[SDR]] (Radio Definida por Software) que abarca desde 1 MHz hasta 6 GHz. Se utiliza para interactuar con señales que viajan por el aire a larga distancia.

### 1. Usos del HackRF (Versión Base conectada al PC)
Por sí solo (conectado por USB a un portátil con software como [[SDRSharp]] o [[GNU Radio]]), estos son todos sus usos reales:

- **Ataques de Replay (Captura y Reproducción):** Grabar la señal de un mando de garaje, grúa industrial o alarma, y volver a emitirla para abrir la puerta sin tener el mando original.
- **Intercepción de Aviación y Marina:** Escuchar comunicaciones de voz no cifradas entre pilotos y torres de control, o decodificar telemetría [[ADS-B]] para ver la posición de aviones en tiempo real.
- **Ingeniería Inversa IoT:** Analizar cómo se comunican estaciones meteorológicas inalámbricas, monitores de presión de neumáticos (TPMS) o timbres inteligentes.
- **Spoofing (Falsificación):** Emitir coordenadas [[GPS]] falsas para engañar a la navegación de drones, móviles o vehículos cercanos (altamente ilegal).

### 2. Mod Portátil (El PortaPack)
Le añade una carcasa, batería interna, pantalla táctil y ranura MicroSD.
- **Uso:** Transforma el HackRF de una placa de laboratorio atada a un PC a un dispositivo táctico independiente. Permite hacer ataques de Replay o grabar espectro en la calle, llevándolo en la mano.

### 3. Amplificadores (LNA y PA)
- **Amplificador LNA (Recepción):** Se enrosca en la antena para "escuchar mejor". Limpia el ruido y permite captar señales débiles que vengan de muy lejos.
- **Amplificador PA (Emisión):** Aumenta radicalmente la potencia en vatios con la que gritas al aire.
- **Uso real del PA:** Sirve para emitir el GPS falso a kilómetros o para hacer [[Jamming]] (emitir ruido bruto en 2.4 GHz para tirar abajo conexiones [[Wi-Fi]] y [[Bluetooth]] por fuerza bruta). No sirve para descifrar ni leer datos de esas redes, solo para anularlas.

### Precios
- **HackRF Original + PortaPack:** ~500 €.
- **HackRF Clon preensamblado + PortaPack (AliExpress):** ~150 € - 200 €.
- **Amplificadores:** ~20 € - 40 € cada uno.

### Curva de aprendizaje y Utilidad
- **Curva Alta:** Entender el procesamiento de señales digitales (DSP) y el espectro electromagnético es complejo.
- **Utilidad:** Indispensable para auditar telecomunicaciones, sensores inalámbricos y protocolos de radio no estándar. Inútil para protocolos rápidos con salto de canal como el Bluetooth moderno.

> [!WARNING]
> Emitir interferencias (Jamming) o falsificar señales GPS con un HackRF amplificado constituye un delito federal en la mayoría de países, ya que interrumpe infraestructuras críticas y de emergencia.

---

## 🔐 7. Herramientas de Infiltración de Red (Hak5)

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

## 📇 8. Hardware Histórico: RFIDler
El **RFIDler** (creado por Aperture Labs) fue una herramienta pionera en la investigación y manipulación de señales RFID de baja frecuencia (125kHz).

Actualmente es un proyecto **descatalogado**. Si bien fue vital para la comunidad hacker hace una década, a día de hoy ha sido completamente reemplazado por dispositivos modernos y con soporte activo como el **Proxmark3 RDV4** y el **Flipper Zero**. Es un componente histórico de esta disciplina.

---

## 🚫 9. Inhibidores de Frecuencia (Signal Jammers)

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

## 🔓 10. Ganzúas y Lockpicking

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
| 💾 Bash Bunny | BadUSB + Adaptador de Red | Intermedio | ~200 € | Hak5 / KSEC |
| 🔌 O.MG Cable | BadUSB invisible por Wi-Fi | Intermedio | ~200 € | Hak5 |
| 🐬 Flipper Zero | RF / NFC / IR básico | Principiante | $169 USD | flipper.net |
| 🍍 WiFi Pineapple | MitM Wi-Fi / Phishing | Intermedio | ~$120 USD | Hak5 / KSEC |
| 💳 Proxmark3 | RFID/NFC criptografía avanzada | Avanzado | ~350 € | KSEC / Hacker Warehouse |
| 📻 HackRF One | SDR (Análisis de ondas en bruto) | Avanzado | ~500 € | Astroradio / Great Scott |
| 🐢 LAN Turtle | Backdoor de red (SSH) | Intermedio | ~$80 USD | Hak5 |
| 🦈 Shark Jack | Escaneo rápido LAN (Nmap) | Intermedio | ~$100 USD | Hak5 |
| 🐿️ Packet Squirrel | Network Tap pasivo (Sniffing) | Intermedio | ~$60 USD | Hak5 |
| 📇 RFIDler | LF RFID (Legacy) | Obsoleto | Descatalogado | N/A |
| 🚫 Inhibidor (Jammer) | Bloqueo RF / DoS físico | N/A | **ILEGAL** | N/A |
| 🔓 Ganzúas / Kit | Seguridad física (Cerraduras) | Principiante | ~30€ | multipick.com |
