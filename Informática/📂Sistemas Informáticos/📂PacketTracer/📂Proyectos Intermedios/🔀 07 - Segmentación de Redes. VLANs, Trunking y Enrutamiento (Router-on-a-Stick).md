**Tags:** #sistemas-informaticos #packet-tracer #vlans #trunking #router-on-a-stick #802-1q #switching #routing #ccna #laboratorio

> [!abstract] 🎯 Objetivo del Proyecto: ¿Qué busco aprender y qué resuelve esta práctica?
> En este laboratorio abordo uno de los pilares más importantes de las redes corporativas: **la segmentación lógica en Capa 2 mediante VLANs y su interconexión controlada en Capa 3 a través de un único enlace compartido (Router-on-a-Stick con Trunking 802.1Q)**.
> 
> **El problema que resuelvo:**
> En una red empresarial real no puedo conectar todos los equipos a un mismo switch en plano. 
> 
> Si los departamentos de Contabilidad, Informática y Dirección comparten la misma red, cualquier usuario puede interceptar tráfico ajeno y las tormentas de difusión (*broadcast storms*) ralentizan toda la infraestructura. 
> 
> Por otro lado, conectar cada red con cables físicos dedicados hacia puertos separados del router es inviable: cuesta mucho dinero y agota los puertos físicos del router en cuanto crecen los departamentos.
> 
> **Lo que implemento y aprendo con esta práctica:**
> 1. **Aislamiento en Capa 2 (VLANs):** Creo dos redes lógicas independientes (**VLAN 10** y **VLAN 20**) en un switch Cisco Catalyst 2960. Los equipos de una VLAN no se pueden comunicar directamente con los de la otra, aunque compartan el mismo switch físico.
> 
> 2. **Enlace Troncal (Trunk 802.1Q):** Configuro un único cable físico entre el switch y el router que transporta el tráfico de todas las VLANs simultáneamente gracias al etiquetado **IEEE 802.1Q** (que inyecta 4 bytes con el VLAN ID en la cabecera Ethernet).
> 
> 3. **Subinterfaces en el Router (Router-on-a-Stick):** Divido un único puerto físico del router en subinterfaces lógicas (`g0/0/0.10` y `g0/0/0.20`), asignando a cada una la IP de Default Gateway de su subred.
> 
> 4. **Enrutamiento Inter-VLAN:** Permito que los equipos se comuniquen entre diferentes departamentos pasando obligatoriamente por el router, donde en el futuro puedo aplicar políticas de seguridad, listas de control de acceso (ACLs) y cortafuegos.

---

## 🗺️ Mapa de Direccionamiento y Topología del Laboratorio

### 📸 Topología de la Red en Packet Tracer

![[PT_Proyecto_07_VLANs_Router_on_a_Stick.png]]

| Dispositivo | Interfaz | Modo / VLAN | Dirección IP / Máscara | Default Gateway | Función en la Red |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **PC0** | FastEthernet0 | Acceso (VLAN 10) | `192.168.10.10 /24` | `192.168.10.1` | Equipo en VLAN 10 (ej. Ventas) |
| **PC1** | FastEthernet0 | Acceso (VLAN 10) | `192.168.10.11 /24` | `192.168.10.1` | Equipo en VLAN 10 (ej. Ventas) |
| **PC2** | FastEthernet0 | Acceso (VLAN 20) | `192.168.20.10 /24` | `192.168.20.1` | Equipo en VLAN 20 (ej. TI / Admin) |
| **PC3** | FastEthernet0 | Acceso (VLAN 20) | `192.168.20.11 /24` | `192.168.20.1` | Equipo en VLAN 20 (ej. TI / Admin) |
| **Switch0** (2960) | Fa0/1 - Fa0/2 | `switchport mode access vlan 10` | N/A (Capa 2) | N/A | Puertos de acceso a VLAN 10 |
| **Switch0** (2960) | Fa0/3 - Fa0/4 | `switchport mode access vlan 20` | N/A (Capa 2) | N/A | Puertos de acceso a VLAN 20 |
| **Switch0** (2960) | Gig0/1 | `switchport mode trunk` | N/A (Capa 2) | N/A | Enlace troncal etiquetado 802.1Q |
| **Router0** (ISR4321) | Gig0/0/0 | Físico (sin IP) | N/A | N/A | Interfaz portadora (`no shutdown`) |
| **Router0** (ISR4321) | Gig0/0/0.10 | Subinterfaz virtual | `192.168.10.1 /24` | N/A | Default Gateway para la VLAN 10 |
| **Router0** (ISR4321) | Gig0/0/0.20 | Subinterfaz virtual | `192.168.20.1 /24` | N/A | Default Gateway para la VLAN 20 |

---

## 1. El aislamiento a nivel de enlace (Capa 2)

Un switch opera leyendo **direcciones MAC**. 

En una red plana estándar, si un equipo envía una trama de *broadcast* (como una petición ARP para descubrir la MAC de una IP), el switch replica esa trama por todos sus puertos físicos. 

Al configurar **VLANs**, el sistema operativo del switch divide lógicamente su tabla de direcciones MAC en dominios de difusión independientes. 

> [!INFO] Aislamiento de Hardware
> Si un puerto está asignado a la VLAN 10, cualquier trama de *broadcast* generada ahí solo será replicada hacia otros puertos de la VLAN 10. 
> 
> Las tramas dirigidas a puertos de la VLAN 20 son descartadas a nivel de hardware. 
> 
> Es un aislamiento idéntico al de los contenedores en distintas redes puente aisladas: las interfaces no comparten dominios de *broadcast*.

---

## 2. El enlace Trunk y la modificación de la trama (Estándar IEEE 802.1Q)

Antes de que existiera el concepto de Trunk, si querías enrutar tráfico de 5 VLANs distintas a través de un router, necesitabas conectar 5 cables físicos independientes desde el switch hasta 5 puertos físicos distintos en el router. 

Esto agotaba los puertos del hardware rápidamente y encarecía de forma innecesaria la infraestructura. 

Un enlace **Trunk (Troncal)** soluciona este problema permitiendo que un único cable físico transporte el tráfico de múltiples VLANs simultáneamente. 

> [!NOTE] El protocolo IEEE 802.1Q (dot1q)
> Para que los datos no se mezclen en este cable compartido, el switch aplica el estándar universal **IEEE 802.1Q**. 
> 
> Este protocolo funciona inyectando físicamente **4 bytes** adicionales justo en medio de la cabecera Ethernet original antes de enviar los datos por el Trunk. 
> 
> Esos 4 bytes contienen un campo con el identificador de la VLAN (VLAN ID, como el `10` o el `20`). 
> 
> Así, el dispositivo que recibe el tráfico sabe a qué red lógica pertenece cada paquete.

---

## 3. El procesamiento en las subinterfaces (Capa 3)

El router opera leyendo **direcciones IP** y enrutando tráfico entre redes lógicas diferentes. 

Como un puerto físico tradicional de router solo puede tener configurada una única dirección IP y pertenecer a una sola subred, no puede procesar de forma nativa el tráfico de múltiples redes que le llegan por el enlace Trunk.

Por eso se crean las **subinterfaces** (ej. `gig0/0/0.10` y `gig0/0/0.20`). 

Son divisiones virtuales, definidas por software, de una única interfaz física:

* **El propósito:** Permiten que un solo puerto físico actúe como múltiples puertas de enlace (*Default Gateways*). 

* **El funcionamiento:** Instruyes al router para que asigne una IP distinta a cada subinterfaz, escuche el tráfico entrante en ese único puerto físico, lea los 4 bytes de la etiqueta 802.1Q y dirija los datos a la puerta virtual correcta según su identificador.

---

## 4. El ciclo de vida técnico del paquete (Ping de VLAN 10 a VLAN 20)

### El viaje de ida (De PC1 a PC3)

1. **Generación y encapsulación (PC1):**  
   El PC1 (`192.168.10.10`) quiere hacer un ping al PC3 (`192.168.20.10`). 
   
   Al comparar las IPs y la máscara de subred, el PC1 determina que el destino está fuera de su red local. 
   
   Por lo tanto, encapsula el paquete IP dentro de una trama Ethernet dirigida a la **dirección MAC de su Default Gateway** (la MAC de la subinterfaz `.10` del router).

2. **Inyección de la etiqueta (Switch):**  
   El paquete llega al switch por un puerto de acceso. 
   
   El switch lee su tabla de direcciones MAC, ve que el destino de esa trama está a través del puerto Trunk y la procesa. 
   
   Antes de transmitirla por el cable físico hacia el router, el hardware del switch **inyecta la etiqueta 802.1Q (4 bytes)** con el valor `10` en la cabecera Ethernet.

3. **Desencapsulación y enrutamiento (Router):**  
   El router recibe la trama modificada. 
   
   Su interfaz de red lee la etiqueta `10` y envía los datos a la subinterfaz virtual `gig0/0/0.10`. 
   
   El router descarta por completo la cabecera Ethernet (Capa 2) para leer el paquete IP original (Capa 3). 
   
   Lee la IP de destino (`192.168.20.10`), consulta su tabla de enrutamiento interna y comprueba que esa subred está directamente conectada a su subinterfaz `gig0/0/0.20`.

4. **Re-etiquetado (Router):**  
   El router genera una trama Ethernet completamente nueva. 
   
   Ahora la MAC de origen es la de la subinterfaz `.20` y la MAC de destino es la del PC3. 
   
   El router inyecta una **nueva etiqueta 802.1Q**, esta vez con el valor `20`, y transmite la trama hacia abajo por el mismo cable físico.

5. **Limpieza y entrega (Switch):**  
   El switch recibe la trama, lee la etiqueta `20` y sabe que debe procesarla en la tabla MAC de la VLAN 20. 
   
   Antes de entregarla al PC3, el switch **elimina los 4 bytes** de la etiqueta 802.1Q para devolver la trama a su formato Ethernet original. 
   
   El PC3 recibe una petición de ping (*Echo Request*) estándar, ignorando por completo que la red está segmentada.

### El viaje de vuelta (De PC3 a PC1)

Para completar el ping, el PC3 debe enviar una respuesta (*Echo Reply*) al origen. 

El PC3 mira la IP de origen del paquete que acaba de recibir (`192.168.10.10`) y determina que está en otra red. 

El proceso se repite a la inversa:

1. PC3 envía la respuesta hacia su Default Gateway (la MAC de la subinterfaz `.20`).

2. El switch recibe la trama, le **inyecta la etiqueta `20`** y la sube por el Trunk.

3. El router la recibe en la subinterfaz `gig0/0/0.20`, lee la IP de destino (el PC1), y enruta el paquete hacia la subinterfaz `gig0/0/0.10`.

4. El router crea una nueva trama, le **pone la etiqueta `10`** y la baja por el Trunk.

5. El switch recibe la trama, ve la etiqueta `10`, **la retira (quita los 4 bytes)** y entrega la respuesta final al PC1. El ping se ha completado exitosamente.

---

## 💻 Chuleta Rápida de Comandos Cisco CLI

### En el Switch Catalyst 2960:
```cisco
Switch> enable
Switch# configure terminal

! 1. Crear las VLANs
Switch(config)# vlan 10
Switch(config-vlan)# name Ventas
Switch(config-vlan)# exit
Switch(config)# vlan 20
Switch(config-vlan)# name TI_Admin
Switch(config-vlan)# exit

! 2. Asignar puertos de acceso a sus VLANs
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# exit

Switch(config)# interface range fa0/3 - 4
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20
Switch(config-if-range)# exit

! 3. Configurar el puerto Trunk hacia el router
Switch(config)# interface gig0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# exit
```

### En el Router ISR 4321:
```cisco
Router> enable
Router# configure terminal

! 1. Encender la interfaz física (sin asignarle IP)
Router(config)# interface gig0/0/0
Router(config-if)# no shutdown
Router(config-if)# exit

! 2. Configurar Subinterfaz para VLAN 10
Router(config)# interface gig0/0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
Router(config-subif)# exit

! 3. Configurar Subinterfaz para VLAN 20
Router(config)# interface gig0/0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
Router(config-subif)# exit
```

### Comandos de Verificación Clave:
* `show vlan brief` *(en switch)*: Compruebo qué puertos pertenecen a cada VLAN.
* `show interfaces trunk` *(en switch)*: Verifico que el puerto hacia el router está en modo troncal y qué VLANs están permitidas.
* `show ip interface brief` *(en router)*: Confirmo que las subinterfaces `.10` y `.20` están en estado `up / up` con sus IPs.
* `show ip route` *(en router)*: Verifico que ambas subredes aparecen directamente conectadas (`C`).

---
→ Volver al índice: [[🌐 README|📁 Proyectos Intermedios de Packet Tracer]]
