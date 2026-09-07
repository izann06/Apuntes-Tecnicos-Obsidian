#sistemas-informaticos #packet-tracer #peer-to-peer #cable-cruzado #ping #ip-estatica

> [!info] 🧭 Navegación
> ◀ [[🌐 README]] · 🔼 [[🌐 README]] · ▶ [[🖧 02 - La Oficina Pequeña (Red LAN con Switch)]]

---

## 🎯 1. Mi Objetivo y Caso de Uso Real

Mi objetivo en este primer proyecto es entender la forma más elemental de comunicación digital entre dos computadores (**red punto a punto o Peer-to-Peer**), familiarizarme con el espacio de trabajo de Cisco Packet Tracer y aprender a configurar parámetros de red de forma manual.

> [!abstract] 🏠 Caso Real: Compartir archivos sin Wi-Fi
> Pienso en este caso real: estoy en una localización remota (un barco, un refugio o una sala sin cobertura ni router) y necesito transferir una carpeta con vídeos y proyectos pesados de varios gigabytes de mi ordenador al portátil de un compañero. 
> 
> En lugar de esperar horas con una memoria USB lenta, tomo un cable de red Ethernet y conecto físicamente ambos equipos puerto con puerto.

---

## 🛠️ 2. Hardware e Infraestructura que Utilizo

Para este laboratorio utilizo:

- **2 PCs de sobremesa** (Dispositivos finales / *End Devices*).
- **1 Cable de Par Trenzado Cruzado** (*Copper Cross-Over*).

![[PT_Proyecto_01_Conexion_Directa.png]]

```mermaid
graph LR
    PC1["💻 PC1<br>FastEthernet0<br><b>192.168.1.10/24</b>"] <===|Cable Cruzado<br>Línea Discontinua Negra|===> PC2["💻 PC2<br>FastEthernet0<br><b>192.168.1.20/24</b>"]

    style PC1 fill:#1a365d,stroke:#2b6cb0,color:#fff
    style PC2 fill:#2d3748,stroke:#4a5568,color:#fff
```

> [!tip] 💡 ¿Por qué utilizo un Cable Cruzado y no Directo?
> En las conexiones directas entre dos tarjetas de red del mismo tipo (PC a PC), los pines de transmisión (**Tx**) del primer equipo deben conectarse a los pines de recepción (**Rx**) del segundo. Un cable directo conectaría Tx con Tx y Rx con Rx, impidiendo la comunicación. El **cable cruzado** invierte internamente los pares para que hablen y escuchen correctamente.

---

## ⚙️ 3. Pasos que Sigo en Packet Tracer

### 1️⃣ Paso 1: Saco los equipos al espacio de trabajo

1. Me dirijo a la esquina inferior izquierda de Packet Tracer.
2. Hago clic en la categoría **End Devices** (icono del ordenador de sobremesa).
3. En la subcategoría inferior, hago clic sobre **PC** (PC-PT) y arrastro dos unidades al lienzo en blanco. Los renombro como `PC1` y `PC2` para tenerlos bien identificados.

### 2️⃣ Paso 2: Conecto los equipos con el cable adecuado

1. Hago clic en el icono del **Rayo Naranja** (**Connections**).
2. Localizo el cable con **línea discontinua negra** llamado **Copper Cross-Over** (Cable Cruzado).
3. Hago clic sobre **PC1**: se despliega la lista de puertos disponibles y selecciono **FastEthernet0**.
4. Llevo el cable hasta **PC2**, hago clic sobre él y selecciono igualmente **FastEthernet0**.
5. Compruebo que en ambos extremos del cable aparecen dos triángulos de color verde brillante. Esto me indica que el enlace físico (Capa 1) está levantado.

### 3️⃣ Paso 3: Asigno Direccionamiento IP Estático en PC1

1. Hago clic sobre **PC1** para abrir su ventana de configuración.
2. Me dirijo a la pestaña superior **Desktop** (Escritorio).
3. Hago clic en la aplicación **IP Configuration**.
4. Me aseguro de que está marcado el modo **Static**.
5. Asigno los siguientes valores:
   - **IPv4 Address**: `192.168.1.10`
   - **Subnet Mask**: Al hacer clic en la casilla, Packet Tracer rellena automáticamente `255.255.255.0`.
6. Cierro la ventana de configuración IP.

### 4️⃣ Paso 4: Asigno Direccionamiento IP Estático en PC2

1. Hago clic sobre **PC2** y entro a **Desktop > IP Configuration**.
2. Relleno los datos:
   - **IPv4 Address**: `192.168.1.20`
   - **Subnet Mask**: `255.255.255.0`
3. Cierro la ventana.

---

## 🧪 4. Verificación y Pruebas que Realizo

Para comprobar que los datos viajan físicamente de un ordenador a otro, utilizo el comando universal de diagnóstico: `ping` (protocolo ICMP).

1. Abro de nuevo la ventana de **PC1**.
2. En la pestaña **Desktop**, abro la aplicación **Command Prompt** (la terminal).
3. Escribo el siguiente comando y pulso **Enter**:

```bash
ping 192.168.1.20
```

### 📋 Resultado que obtengo:

```text
Pinging 192.168.1.20 with 32 bytes of data:

Reply from 192.168.1.20: bytes=32 time<1ms TTL=128
Reply from 192.168.1.20: bytes=32 time<1ms TTL=128
Reply from 192.168.1.20: bytes=32 time<1ms TTL=128
Reply from 192.168.1.20: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.1.20:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

> [!NOTE] 🔍 Lo que observo en esta respuesta:
> - **Reply from**: El destinatario recibe mi paquete y me responde satisfactoriamente.
> - **time<1ms**: La velocidad de respuesta es instantánea debido a la cercanía física.
> - **TTL=128**: *Time To Live* predeterminado en sistemas Windows para paquetes de red.
> - **0% loss**: Ningún bit se ha perdido en el camino.

### 👁️ Inspección visual en Modo Simulación

1. En la esquina inferior derecha, cambio a la pestaña **Simulation** (o presiono `Shift + S`).
2. En el panel de simulación, pulso el botón **Capture / Forward**.
3. Observo cómo viaja un sobre de color azul por el cable desde PC1 hasta PC2, y luego regresa con una marca de verificación verde.

---

## 🚨 5. Errores con los que Me Puedo Encontrar y Soluciones

| Error Posible | Causa Raíz | Cómo lo Soluciono |
|:---|:---|:---|
| **Triángulos rojos en el cable** | He utilizado un tipo de cable incompatible (ej. cable de consola o fibra) o la tarjeta de red está apagada. | Borro el cable con la herramienta de supresión (tecla `Del` o la cruz roja) y uso el cable negro discontinuo (**Copper Cross-Over**). |
| **Request timed out** | He configurado las direcciones IP en subredes distintas (ej. `192.168.1.10` y `192.168.2.20` con máscara `255.255.255.0`). | Compruebo en ambos PCs que los tres primeros números de la IP coinciden exactamente (`192.168.1.X`). |
| **Destination host unreachable** | La tarjeta de red del equipo emisor no tiene IP configurada o la máscara de subred es incorrecta. | Entro en **IP Configuration** y verifico que la IP está escrita correctamente sin espacios en blanco. |

---

## 📌 6. Resumen de lo Aprendido y Siguiente Paso

En este primer proyecto he aprendido a:
- Elegir el cable cruzado para conectar directamente dos dispositivos del mismo nivel.
- Asignar direccionamiento IP estático en el rango `/24`.
- Validar la comunicación mediante paquetes ICMP `ping` y mediante el modo simulación.

**La limitación que detecto**: Con este esquema solo puedo conectar **dos** ordenadores. Si quiero montar una oficina con 4 o más equipos, necesito un dispositivo central inteligente: el **Switch**.

👉 Continúo a mi siguiente reto: [[🖧 02 - La Oficina Pequeña (Red LAN con Switch)]]
