
Memoria de Práctica: Configuración de una IP Estática en una Máquina Virtual

## Objetivo de la práctica

El objetivo de esta práctica es **configurar una dirección IP estática** en una máquina virtual para que su dirección de red no cambie cada vez que se reinicie.

Esto es importante porque, cuando usamos una IP dinámica (asignada por DHCP, por eso nosotros desactivamos esa parte ya que es justo lo contrario a lo que queremos hacer), la máquina puede recibir una dirección diferente en cada arranque, lo que complica la conexión desde el host o desde otras máquinas virtuales.  

Con una IP estática, **sabemos siempre qué dirección tiene la máquina** y podemos acceder a ella fácilmente (por ejemplo, para hacer pruebas de red, conectar por SSH, montar servicios, etc.).

## Tipos de red usados: Host-Only y NAT

### Modo Host-Only

El modo **Host-Only** crea una red privada **solo entre el equipo anfitrión (nuestro ordenador real)** y la **máquina virtual**.  
Esto significa que:

- El host y la máquina virtual **pueden comunicarse entre sí**.
    
- La máquina **no tiene acceso directo a Internet**.
    
- Sirve para hacer pruebas de red local o configuraciones internas sin depender de una red externa.
    

Se usa este modo cuando queremos probar configuraciones de red o conectar varias máquinas virtuales entre sí sin que intervenga Internet.

### Modo NAT

El modo **NAT (Network Address Translation)** permite que la máquina virtual **salga a Internet usando la conexión del equipo anfitrión**.  
El host actúa como una especie de router: traduce las direcciones IP internas de las máquinas virtuales y las deja comunicarse con el exterior.

Esto es útil cuando queremos **instalar actualizaciones, descargar paquetes o acceder a recursos online** desde la máquina virtual.

### Configuración de estas redes en Ubuntu Server

Te vas al apartado de 'Herramientas' y dentro de ahí 'Red'

![[Pasted image 20251007094235.png]]

Te creas una red Host-Only con una ip que pondrás manualmente y una máscara .El DHCP tiene que estar desactivado.

![[Pasted image 20251007094446.png]]



Creamos la red Nat


![[Pasted image 20251007094425.png]]


Una vez configurados los adaptadores en VirtualBox, debes proceder a configurar la interfaz de red dentro de la máquina virtual de Ubuntu Server. Sigue estos pasos:

1. Crea una máquina virtual de Ubuntu Server.
    
2. Edita el archivo de configuración de red de netplan: ![[Pasted image 20251007094744.png]]
3. Agrega la siguiente configuración, reemplazando los valores de IP y puerta de enlace según tu entorno: **Recordad la dirección de red que hemos puesto en el adaptador Host Only**
   ![[Pasted image 20251007095631.png]]
4. Aplica los cambios
![[Pasted image 20251007094904.png]]
Verifica que la configuración se haya aplicado correctamente:
![[Pasted image 20251007094949.png]]


### A tener en cuenta:

En la configuración que hemos puesto tenemos la primera enp0s3 (conigurada como NAT) y la segunda enp0s8( Configurada como Host only).

Esto es así porque yo, en mi configuración tengo los adaptadores en ese orden. Si lo cambiamos, eso hay que cambiarlo también en el fichero yaml.
