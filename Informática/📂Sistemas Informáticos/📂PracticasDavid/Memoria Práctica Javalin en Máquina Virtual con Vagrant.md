## **1. Objetivo de la práctica**

- Configurar una máquina virtual Ubuntu mediante Vagrant.
    
- Instalar herramientas necesarias: Git, Maven, JDK.
    
- Descargar y ejecutar un proyecto REST con Javalin.
    
- Hacer accesibles los servicios desde el host (Windows).
    
- Documentar problemas y soluciones durante el proceso.
    



## **2. Preparación de la máquina virtual**

Te metes a powershell,creas un directorio, te metes dentro de el y haces:

**vagrant init**

Con eso creas el vagrantFile y metes este código para añadir una **IP privada**, instalar **maven,git, y jdk...**

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant.png]]

Despues hacemos:

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-6.png]]

## **Problemas encontrados:**

**VM no arrancaba**

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-4.png]]

- **Causa:** Vagrant no podía conectarse por SSH porque la VM no levantaba correctamente la red host-only.
    
- Esto pasaba aunque la VM pareciera arrancar; el problema real era la **configuración de red**. Se debe a que definí una IP para la VM `192.168.1.33` que **ya estaba en uso** por otra red de VirtualBox, adaptador de Wi-Fi o incluso otra VM.

- Este conflicto impedía que la VM pudiera comunicarse con el host correctamente y provocaba el timeout de SSH.A si que añadí otra IP la 192.168.56.33

En el vagrantFile puse `virtualbox__intnet: false` que solo evita crear una red interna aislada entre VMs. No afecta Internet ni la comunicación host ↔ VM. No hace falta ponerlo, pero lo hice para asegurarme de que no fallará por la IP.


## **3. Descarga del proyecto**

- **Error inicial:** Intenté clonar directamente con la URL del aules `tree/master/...`
![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-2.png]]

y entonces me dió error:
    

`fatal: repository 'https://github.com/.../javalin_basico/' not found`

**Solución:** Clonar **todo el repositorio** desde la raíz:
    

`git clone https://github.com/davidscientistcom/Curso25_26.git`

- El repositorio lo cloné**en la misma carpeta que el Vagrantfile**, porque la carpeta `/vagrant` se comparte automáticamente entre host y VM.
![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-3.png]]




## **4. Compilación y ejecución del proyecto**

Entraste en la VM con:    

`vagrant ssh

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-9.png]]
![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-10.png]]

Vamos a ver si estamos dentro y que tenemos en la misma rama que vagrantfile.
(*/vagrant* indica que empieza justo donde esta el vagrantFile,y en la misma rama esta el repositorio)
![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-11.png]]

Ahora tienes que ir a donde está el código con:

`cd /vagrant/Curso25_26/Rest/javalin_basico`

Después hice:

`mvn exec:java`

Me dio **Error**,Maven no sabía qué clase `Main` ejecutar:

`The parameters 'mainClass' ... are missing or invalid`

**Solución:** Indicar explícitamente la clase principal:    

`mvn compile exec:java -Dexec.mainClass="Main"`

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-12.png]]
![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-13.png]]



## **5. Modificación del código para accesibilidad desde host**

Inicialmente Javalin arrancaba en localhost:

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-8.png]]

**Problema:** No se podía acceder desde el host (Windows).
    
**Solución:** Cambiar a escuchar todas las interfaces:
    

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-7.png]]

---

## **6. Prueba de los endpoints**

- Comprobación dentro de la VM:
    

`curl http://localhost:7001/users`

- Comprobación desde el host (Windows):
    

`http://192.168.56.33:7001/users`

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-15.png]]

## **7. Problema con el Object Mapper (JSON)**

Al hacer `curl`, aparecía:

`It looks like you don't have an object mapper configured.`

**Causa:** Javalin necesita una librería para convertir objetos Java a JSON (Jackson).

**Solución:** Añadir manualmente dependencia en `pom.xml`:    

![[Memoria Práctica Javalin en Máquina Virtual con Vagrant-14.png]]

Entonces recompilas y ejecutas de nuevo:

`mvn clean package mvn compile exec:java -Dexec.mainClass="Main"`    


