#seguridad #hardware #privacidad #defensa #tails #pi-hole #opsec #vpn #linux

> [!info] Navegación
> ▶ Siguiente: [[⚔️ 02 - Gadgets de Hacking Ofensivo Explicados|Gadgets de Hacking Ofensivo]]

---

Esta guía cubre los dispositivos y herramientas físicas que usan los expertos en ciberseguridad, periodistas y cualquier persona que quiera tomar el control real de su privacidad digital.

No hace falta ser un hacker para usar la mayoría de estos. Algunos son tan sencillos como enchufar un adaptador.

---

## 🚫 1. Bloqueador de Datos USB (USB Data Blocker)

![[Pasted image 20261005182939.png]]

### Qué es exactamente

El "USB condom" (nombre coloquial, aunque en tiendas se vende como "USB Data Blocker") es un **adaptador diminuto** que se coloca entre tu cable de carga y el puerto USB público. Físicamente tiene los pines de datos cortados dentro — solo dejan pasar los dos pines de alimentación eléctrica.

El nombre vulgar viene de la analogía directa: igual que un preservativo evita el contagio pero no impide la función principal, este adaptador evita la transmisión de datos pero no impide la carga. Tiene la misma lógica exacta.

### Por qué lo necesitas

Los puertos USB públicos (aeropuertos, hoteles, aviones, cafeterías) son un vector de ataque conocido llamado **Juice Jacking**. El atacante instala un dispositivo malicioso dentro del cargador público. Cuando conectas tu móvil, el cable pasa tanto corriente como datos — y el dispositivo malicioso puede intentar extraer archivos, instalar malware o inyectar comandos. Con el Data Blocker, los pines de datos están cortados físicamente: aunque el puerto sea malicioso, es imposible que envíe o reciba datos de tu dispositivo.

> [!warning] No solo es teoría
> El FBI y la FCC han emitido alertas oficiales sobre el Juice Jacking en aeropuertos. En 2023, varios casos documentados en hoteles de lujo de Europa comprometieron dispositivos de ejecutivos usando este método en los cargadores de la habitación.

### Cómo se usa

1. Coges el adaptador (del tamaño de un tapón USB).
2. Lo enchufas **entre** tu cable de carga y el puerto USB público.
3. Conectas tu cable normal al adaptador.
4. Tu dispositivo carga con normalidad, pero a velocidad estándar (sin carga rápida, ya que la negociación de voltaje requiere los pines de datos).

### Qué modelos comprar

| Modelo | Tipo | Precio | Link |
|---|---|---|---|
| **PortaPow USB-A Data Blocker** | USB-A ↔ USB-A | ~£4.50 (~5€) | [portablepowersupplies.co.uk](https://portablepowersupplies.co.uk) |
| **PortaPow USB-C Data Blocker** | USB-C ↔ USB-C | ~£6.00 (~7€) | [portablepowersupplies.co.uk](https://portablepowersupplies.co.uk) |
| **También en Amazon ES** | Varios tipos | ~5-9€ | Buscar "PortaPow data blocker" |

> [!tip] Consejo de compra
> Busca modelos con una **ventanita transparente** que te deje ver que los pines de datos están físicamente ausentes. Algunos falsificadores venden adaptadores normales como "data blocker" — el hueco visible es la prueba de que es auténtico.

---

## 🌐 2. Router de Viaje con VPN (GL.iNet)

![[glinet_router.jpg]]

### Qué es exactamente

Un mini-router del tamaño de un cargador de móvil grande. Se conecta a la red Wi-Fi o cable del hotel/aeropuerto y crea **tu propia red Wi-Fi privada cifrada** para todos tus dispositivos.

El modelo estrella es el **GL.iNet Beryl AX (GL-MT3000)**: Wi-Fi 6, puerto WAN de 2.5G, cliente VPN integrado por hardware y un sistema operativo basado en OpenWrt (Linux), totalmente configurable.

### Por qué lo necesitas

Cuando te conectas al Wi-Fi de un hotel, **el hotel ve todo tu tráfico**. También puede haber atacantes haciéndose pasar por la red del hotel (Evil Twin). Usando el router de viaje:

- Todos tus dispositivos (móvil, portátil, tablet) se conectan a **tu** red, no a la del hotel.
- El router establece un túnel VPN (WireGuard o OpenVPN) hacia un servidor de confianza **antes** de que el tráfico salga a internet.
- El hotel solo ve un único dispositivo emitiendo tráfico cifrado incomprensible.

### Cómo se usa — paso a paso

```
1. Llega al hotel y conéctate con el router (Ethernet o Wi-Fi del hotel) → primer salto.
2. Abre la interfaz web del GL.iNet (normalmente 192.168.8.1) desde tu móvil.
3. En el menú VPN, añade tu servidor WireGuard o el perfil de tu VPN (Mullvad, ProtonVPN, etc.).
4. Activa la VPN.
5. Todos tus dispositivos se conectan al SSID que emite el GL.iNet → ya están protegidos.
```

> [!note] ¿Necesito una VPN de pago también?
> Sí, el router GL.iNet **es el cliente VPN** (gestiona la conexión), pero necesitas un **servidor VPN** al que conectarte. Las opciones recomendadas son **Mullvad VPN** (~5€/mes, acepta pago en efectivo y Monero) o **ProtonVPN** (tiene plan gratuito básico).

### Dónde comprarlo

| Modelo | Velocidad Wi-Fi | Precio aprox. | Link oficial |
|---|---|---|---|
| **Beryl AX (GL-MT3000)** | Wi-Fi 6 AX3000 | ~103€ | [gl-inet.com](https://www.gl-inet.com/products/gl-mt3000/) |
| **Slate AX (GL-AXT1800)** | Wi-Fi 6 AX1800 | ~90-120€ | [gl-inet.com](https://www.gl-inet.com/products/gl-axt1800/) |
| **También en Amazon ES** | Ambos modelos | Precio similar | Buscar "GL.iNet Beryl AX" |

> [!tip] ¿Cuál elegir?
> Para viajes: el **Beryl AX** (más compacto y moderno). Si quieres usarlo también en casa como router principal y servidor de servicios: cualquiera de los dos vale. Consulta la página oficial [gl-inet.com/where-to-buy](https://www.gl-inet.com/where-to-buy/) para distribuidores autorizados en España.

---

## 🐧 3. Sistema Operativo Tails (en USB)

![[tails_usb.jpg]]

### Qué es exactamente

Tails (The Amnesic Incognito Live System) es un **sistema operativo completo que arranca desde un pendrive USB**. No se instala en el disco duro — vive y muere en la memoria RAM de tu ordenador.

El nombre lo dice todo: es **amnésico** (no recuerda nada) e **incógnito** (todo el tráfico va por Tor).

### Por qué es tan especial

Cuando cierras sesión o apagas el ordenador, Tails **borra activamente la RAM**. No hay rastro en el disco duro del ordenador host. Desde el punto de vista forense, es como si nunca hubieras usado ese equipo. Además, todo el tráfico de red pasa obligatoriamente por la red **Tor**, que anonimiza el origen encadenando tu conexión por varios relays cifrados en distintos países.

Lo usan periodistas de investigación en zonas de conflicto, activistas en países autoritarios, abogados con clientes en riesgo y whistleblowers (Edward Snowden lo recomendó explícitamente).

### Cómo instalarlo y usarlo

**Requisitos mínimos:**
- Un pendrive USB de **mínimo 8 GB** (se recomienda 16 GB para tener almacenamiento persistente cifrado).
- Un ordenador que pueda arrancar desde USB (prácticamente cualquier PC de los últimos 15 años).

**Proceso de instalación:**

```bash
# 1. Ve a la web oficial y descarga la imagen
#    → https://tails.net/install/
#
# 2. Descarga también la app "Balena Etcher" o el "Tails Installer"
#    → https://etcher.balena.io/
#
# 3. Abre Etcher, selecciona el archivo .img de Tails
#    y selecciona tu pendrive → Click "Flash!"
#
# ATENCIÓN: El pendrive se borrará completamente.
```

**Para arrancar:**

```
1. Inserta el pendrive en el ordenador objetivo.
2. Reinicia el ordenador.
3. Al arrancar, pulsa la tecla de Boot Menu (varía por fabricante):
   - F12 → Lenovo, Dell, Acer
   - F9  → HP
   - F11 → ASUS
   - Escape / F8 → otros
4. Selecciona el USB como dispositivo de arranque.
5. Tails arranca en ~60 segundos.
```

> [!warning] Secure Boot
> Algunos ordenadores tienen Secure Boot activado en la BIOS/UEFI, que impide arrancar sistemas no firmados por Microsoft. Puede que necesites desactivarlo temporalmente en la configuración de la BIOS para usar Tails.

**Almacenamiento Persistente cifrado:**
Tails permite crear una partición cifrada (con contraseña) en el mismo pendrive para guardar archivos, configuraciones y contraseñas entre sesiones. Sin ella, todo desaparece al apagar.

> [!note] Descarga SIEMPRE desde la web oficial
> Solo desde **[tails.net](https://tails.net)** — nunca de repositorios de terceros ni torrents. La web incluye verificación criptográfica de la imagen para confirmar que no ha sido manipulada.

**Precio:** Gratis y de código abierto. Solo necesitas un pendrive (3-15€).

---

## 🕳️ 4. Pi-hole + Unbound (en Raspberry Pi)

![[pihole_rpi.jpg]]

### Qué es exactamente

**Pi-hole** es un software de bloqueo de DNS que actúa como un "agujero negro" para todo el tráfico publicitario y de rastreo de tu red doméstica. Funciona a nivel de toda la red, no solo en un navegador.

**Unbound** es un resolvedor DNS recursivo. En lugar de preguntarle a Google (8.8.8.8) o a tu operadora "¿cuál es la IP de amazon.com?", tú mismo resuelves la dirección preguntando directamente a los servidores raíz de internet — sin que nadie en el camino sepa qué webs visitas.

Juntos, bloquean publicidad + evitan el espionaje de DNS de tu operadora.

### Por qué es tan potente

Un bloqueador de anuncios en el navegador (uBlock Origin) solo bloquea en ese navegador. Pi-hole bloquea **antes de que la petición salga de tu red**:

- Bloquea anuncios en apps móviles (donde no puedes instalar extensiones).
- Bloquea la telemetría de tu Smart TV que envía datos a Samsung o LG.
- Bloquea el rastreo de Windows 10/11 (el infame "telemetry" de Microsoft).
- Bloquea rastreadores en cualquier dispositivo conectado al Wi-Fi: consolas, tablets, etc.

### Qué hardware necesitas

| Opción | Para qué | Precio aprox. | Dónde comprar |
|---|---|---|---|
| **Raspberry Pi Zero 2 W** | Solo Pi-hole, lo más económico | ~18-25€ | [raspberrypi.com](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) |
| **Raspberry Pi 4 (2GB)** | Pi-hole + otros servicios a la vez | ~67€ | [raspberrypi.com](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) |
| **MicroSD 16GB+** | Sistema operativo | ~5-10€ | Amazon / MediaMarkt |
| **Cable USB de alimentación** | Energía | ~5€ | Cualquier tienda |

### Cómo instalarlo — guía rápida

```bash
# PASO 1: Instala "Raspberry Pi Imager" en tu PC
# → https://www.raspberrypi.com/software/
# Graba "Raspberry Pi OS Lite (64-bit)" en la MicroSD.
# En el imager, configura Wi-Fi y activa SSH antes de grabar.

# PASO 2: Enciende la Raspberry Pi con la MicroSD y conéctate por SSH
ssh pi@raspberrypi.local

# PASO 3: Instala Pi-hole con UN solo comando
curl -sSL https://install.pi-hole.net | bash
# Sigue el asistente visual que aparece.

# PASO 4: Instala Unbound
sudo apt install unbound -y
# (Configura /etc/unbound/unbound.conf.d/pi-hole.conf según la wiki de Pi-hole)

# PASO 5: Apunta el DNS de tu router a la IP de la Raspberry Pi
# En la config del router: DNS primario = IP_de_tu_RaspberryPi
```

Una vez configurado, **todos los dispositivos de tu casa** quedan protegidos automáticamente sin tocar ninguno de ellos individualmente.

> [!tip] Resultado real
> En una red doméstica media, Pi-hole bloquea entre el 15% y el 45% de todas las peticiones DNS. Eso es todo ese porcentaje de tráfico de rastreo que antes salía de tu casa sin que lo supieras.

**Precio total del proyecto:** ~25-35€ (solo la Raspberry Pi Zero 2 W y la MicroSD). El software es gratuito y de código abierto.

---

## ⌚ 5. Smartwatch de Hardware Libre (PineTime)

![[pinetime.jpg]]

### Qué es exactamente

El **PineTime** es un smartwatch de código abierto creado por la comunidad Pine64. Tiene un hardware muy sencillo, un procesador nórdico de bajo consumo, pantalla táctil y batería de larga duración. El firmware que ejecuta (**InfiniTime**) es 100% código abierto, auditado y sin telemetría de ningún tipo.

### Por qué importa

Un Apple Watch o un Galaxy Watch están conectados permanentemente a servidores de Apple y Samsung. Envían datos de salud (ritmo cardíaco, calidad del sueño, patrones de actividad física, ubicaciones), que luego se usan para publicidad y pueden venderse a aseguradoras. Varios países ya han usado datos de smartwatch como evidencia en juicios.

El PineTime **no tiene conexión a internet propia**. Solo se sincroniza por Bluetooth con tu móvil cuando tú lo pides, y solo con apps compatibles que no envían datos a ningún servidor externo.

### Qué puede hacer

- Hora, fecha, alarmas, temporizadores.
- Notificaciones de llamadas y mensajes del móvil (sin que el watch las almacene).
- Monitor de ritmo cardíaco.
- Contador de pasos.
- Control de música.
- Batería de 7-10 días de duración.

### Dónde comprarlo

| Tienda | Precio | Link |
|---|---|---|
| **Pine Store (oficial)** | ~26.99$ | [pine64.com](https://pine64.com/product-category/pinetime/) |
| **ameriDroid (distribuidor autorizado)** | Precio similar | [ameridroid.com](https://ameridroid.com) |

> [!note] Es un dispositivo de comunidad
> No esperes la pulición de un Apple Watch. Es un proyecto open-source: el firmware se actualiza con frecuencia, las funciones son básicas pero sólidas. Si lo que buscas es privacidad y no un smartwatch de gama alta, es perfecto. Si quieres un reloj "bonito" con miles de funciones, no es tu dispositivo.

---

## 💻 6. Laptop Framework con Linux

![[framework_linux.jpg]]

### Qué es exactamente

**Framework** es una empresa americana que fabrica portátiles 100% modulares. Cada componente es intercambiable con un destornillador: los puertos del lateral son módulos de expansión intercambiables (USB-A, USB-C, HDMI, DisplayPort, SD, Ethernet...), la pantalla, el teclado, la placa base y la batería son piezas que puedes comprar por separado y sustituir tú mismo en 5 minutos.

Pero lo más importante para la privacidad: incluyen **interruptores físicos (kill switches)** que cortan el circuito eléctrico de la cámara y el micrófono. No es software — es hardware. Es imposible que un malware te grabe aunque tenga control total del sistema operativo.

### Por qué Linux y no Windows

Windows 10/11 tiene telemetría activada por defecto: envía a Microsoft datos sobre las aplicaciones que usas, búsquedas, hábitos de uso, ubicación y más. Puedes desactivarla parcialmente, pero nunca del todo.

Linux no envía nada a ningún sitio por defecto. Tú controlas exactamente qué se ejecuta, qué se instala y qué sale a internet.

### ¿Qué Linux instalar en un Framework?

Framework recomienda oficialmente varias distros y tiene guías de instalación específicas para su hardware:

| Distro | Para quién | Nivel |
|---|---|---|
| **Fedora Linux** ⭐ | La más recomendada por Framework. Moderna, estable, drivers perfectos | Principiante/Intermedio |
| **Ubuntu 24.04 LTS** | La más conocida. Muy buena compatibilidad y comunidad enorme | Principiante |
| **Linux Mint** | La más parecida a Windows. Perfecta para empezar en Linux | Principiante |
| **Arch Linux / CachyOS** | Control total, máximo rendimiento, requiere configuración manual | Avanzado |

> [!tip] Si vienes de Windows, empieza con Fedora o Linux Mint
> Framework publica guías detalladas de instalación en su wiki oficial para cada modelo y cada distro recomendada: [frame.work/linux](https://frame.work/linux)

### Cómo se instala Linux

```bash
# 1. Descarga la ISO de tu distro elegida:
#    Fedora  → https://fedoraproject.org/
#    Ubuntu  → https://ubuntu.com/download
#    Mint    → https://linuxmint.com/download.php

# 2. Graba la ISO en un pendrive USB con Balena Etcher
#    → https://etcher.balena.io/

# 3. Arranca el Framework desde el pendrive (tecla F12 al encender)

# 4. Sigue el instalador gráfico (tan sencillo como instalar cualquier app)

# 5. Cuando el instalador pregunte dónde instalar:
#    → Selecciona "Borrar disco e instalar [distro]"
#    → Activa el cifrado de disco completo (LUKS) con contraseña

# ¡Listo! En 15-20 minutos tienes Linux instalado.
```

> [!note] El cifrado de disco (LUKS) es clave
> Activa siempre el cifrado de disco durante la instalación. Si te roban el portátil, sin la contraseña los datos son completamente ilegibles. Framework + Linux + LUKS es una de las combinaciones más seguras disponibles en el mercado de consumo.

### Dónde comprarlo

| Modelo | Precio desde | Link |
|---|---|---|
| **Framework Laptop 13** | ~549$ (DIY) / ~699$ (preconfigurado) | [frame.work](https://frame.work/products/laptop13) |
| **Framework Laptop 16** | ~1049$ (DIY) | [frame.work](https://frame.work/products/laptop16) |
| **Framework Laptop 12** | ~549$ | [frame.work](https://frame.work/) |

> [!warning] ¿No lo venden en España directamente?
> Framework vende a través de su web oficial con envío a la UE. Comprueba la disponibilidad y los costes de envío/impuestos desde [frame.work](https://frame.work). A veces también aparecen unidades en Wallapop o Ebay de usuarios europeos que venden los suyos.

---

## 📚 7. Kiwix (Wikipedia Offline)

### Qué es exactamente

Kiwix es una **aplicación gratuita** (no hardware, pero imprescindible en cualquier kit de privacidad) que descarga enciclopedias completas en tu dispositivo para consultarlas sin conexión a internet.

Puedes descargar la Wikipedia española completa (con imágenes) en un archivo de ~90 GB, o la versión en texto puro en ~20 GB. También descarga StackOverflow, TED talks, documentación de proyectos y mucho más.

### Por qué importa para la privacidad

Cada búsqueda que haces en Google o Wikipedia online queda registrada: por Google (que la usa para publicidad), por tu ISP (que puede venderla o entregarla a autoridades) y por los servidores de Wikipedia (que registran tu IP).

Si consultas Kiwix desde tu dispositivo, **nadie sabe qué estás leyendo**. Es especialmente útil para investigar temas sensibles, médicos, legales o cualquier cosa que prefieras mantener en privado.

### Cómo usarlo

```
1. Descarga la app Kiwix:
   → PC/Linux: https://kiwix.org/en/applications/
   → Android: Play Store → "Kiwix"
   → iOS: App Store → "Kiwix"

2. Dentro de la app, ve a "Biblioteca" y descarga el archivo .zim que quieras.
   Ejemplo: "Wikipedia ES (sin imágenes)" → ~20 GB

3. Ya puedes buscar y leer todo sin conexión, sin rastro.
```

**Precio:** Completamente gratuito y de código abierto. Solo necesitas espacio en disco.

---

## 🎧 8. iPod Classic Modificado (con Rockbox)

### Qué es exactamente

Un iPod Classic de segunda mano (5ª, 6ª o 7ª generación) **actualizado y modernizado** con:
- Sustitución de la batería (nueva).
- Eliminación del disco duro interno y sustitución por una tarjeta **MicroSD o iFlash** (más rápido, sin partes mecánicas).
- Instalación del firmware libre **Rockbox** (compatible con prácticamente todos los formatos de audio).

El resultado es un reproductor de música sin Wi-Fi, sin Bluetooth, sin GPS, sin cuenta de Apple — **electromagnéticamente mudo**.

### Por qué tiene relevancia para la privacidad

Los centros comerciales y tiendas escanean continuamente las señales Bluetooth de los dispositivos cercanos para construir mapas de movimiento de clientes. Si llevas AirPods o auriculares Bluetooth, tu posición dentro del centro se registra y vende a las marcas.

Spotify sabe exactamente qué escuchas y cuándo, correlacionando tu estado emocional con tu historial de compras. Ese perfil se vende.

Un iPod modificado con tu propia librería de música no emite ninguna señal y no transmite nada a nadie.

### Cómo hacerlo

```
1. Compra un iPod Classic en Wallapop/Ebay (5th, 6th o 7th gen): 20-60€.

2. Compra un kit iFlash:
   → https://www.iflash.xyz/ (adaptadores para MicroSD)
   Precio: ~20-35€ + MicroSD de 256GB/512GB (~25-50€).

3. Instala Rockbox (firmware libre):
   → https://www.rockbox.org/
   Es un proceso guiado de 15 minutos.

4. Copia tu música al iPod directamente desde el explorador de archivos.
   No necesitas iTunes ni ningún software de Apple.
```

**Precio total del proyecto:** ~70-150€ dependiendo de la capacidad de MicroSD que elijas.

---

## 📊 Resumen de Todo el Arsenal Defensivo

| Dispositivo | Protege de... | Precio | Dificultad |
|---|---|---|---|
| 🚫 USB Data Blocker (PortaPow) | Juice Jacking en puertos públicos | ~5€ | ⭐ Ninguna |
| 🌐 Router GL.iNet + VPN | Espionaje en redes públicas y del hotel | ~103€ + VPN | ⭐⭐ Baja |
| 🐧 Tails OS en USB | Rastreo forense, vigilancia total | ~10€ (USB) | ⭐⭐⭐ Media |
| 🕳️ Pi-hole + Raspberry Pi | Publicidad, telemetría en toda la red | ~25-35€ | ⭐⭐⭐ Media |
| ⌚ PineTime (smartwatch) | Datos de salud enviados a corporaciones | ~27$ | ⭐⭐ Baja |
| 💻 Framework + Linux | Telemetría de SO, espionaje de cámara/micro | ~549€+ | ⭐⭐⭐ Media |
| 📚 Kiwix | Historial de búsquedas e ISP | Gratis | ⭐ Ninguna |
| 🎧 iPod + Rockbox | Rastreo Bluetooth y datos de Spotify | ~70-150€ | ⭐⭐ Baja |
