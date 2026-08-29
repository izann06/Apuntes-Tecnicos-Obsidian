**Tags:** #aws #ec2 #computacion #cloud-practitioner #maquinas-virtuales #cp-computacion

> [!summary] ¿Qué es la Computación en la Nube?
> Es la capacidad de procesamiento bajo demanda para ejecutar aplicaciones y administrar datos de forma remota. Implica usar máquinas virtuales de un proveedor en internet sin necesidad de comprar ni mantener hardware físico.

---
## 1. El Problema Local vs. La Solución EC2

Hay una comparación directa que es fundamental para entender por qué existe EC2:
### El Desafío Local (On-Premises)

Si tienes que montar un servidor físico tradicional en tu empresa:

* Debes comprar el hardware por adelantado y esperar a que te lo entreguen.

* Tienes que gestionar la instalación y la configuración manualmente.

* Es un proceso caro, que consume mucho tiempo y es muy inflexible frente a los cambios de demanda.

![[🖥️ Amazon EC2 (Elastic Compute Cloud) Fundamentos.png]]

### El Beneficio de Amazon EC2

EC2 resuelve esos problemas ofreciendo máquinas virtuales (instancias) bajo demanda:

* Es mucho más rápido, flexible y rentable para empezar.

* Puedes iniciar, escalar (aumentar/reducir recursos) y terminar servidores en cuestión de minutos según tus necesidades.

* Solo pagas por el uso activo; es decir, solo se te cobra por las instancias en ejecución, no por las que están detenidas o terminadas.

![[🖥️ Amazon EC2 (Elastic Compute Cloud) Fundamentos-1.png]]

---

## 2. El Concepto Clave: Tenencia Múltiple (Multitenancy)

* **Definición:** La tenencia múltiple significa que varias máquinas virtuales (de distintos clientes o proyectos) comparten los recursos físicos del mismo servidor o "host" en el centro de datos de AWS.

* **Seguridad:** Aunque compartan el hardware físico, cada máquina virtual está estrictamente aislada de las demás.

---

## 3. El Ciclo de Vida de una Instancia EC2 (Los 3 Pasos)

#### ¿Qué es exactamente una Instancia?

> [!summary] ¿Qué es exactamente una Instancia?
> Una **Instancia de EC2** es simplemente un **Servidor Virtual**. 


> [!warning] ¿Qué pasa si la **instancia** que tengo se me ha quedado **grande** o **pequeña**?
> No te preocupes se puede cambiar y eso se llama **escalamiento vertical**.
> El escalamiento vertical consiste en **aumentar (o disminuir) el TAMAÑO y la POTENCIA** de una instancia existente. Significa cambiar el tipo de instancia. Por ejemplo, pasar de una instancia con 2 CPUs y 4GB de RAM a una con 8 CPUs y 32GB de RAM.
> Ten en cuenta que si haces eso, tienes que **detener tu servidor** por un momento, así que tu aplicación estará **caída** por unos minutos.

---

Cuando quieres montar un servidor en EC2, siempre sigues este flujo de trabajo:

### Paso 1: Iniciar la instancia

Al crearla, debes tomar dos decisiones críticas:

* **Elegir la AMI (Imagen de máquina de Amazon):** Esto define el sistema operativo (Linux, Windows) y el software base preinstalado.

* **Elegir el Tipo de Instancia:** Esto determina la potencia del servidor, es decir, el rendimiento de la CPU, la memoria RAM y la capacidad de red.

### Paso 2: Conectar con la instancia

Una vez encendida, necesitas acceder a ella para configurarla:

* Si es **Linux**, te conectas mediante el protocolo SSH.

* Si es **Windows**, te conectas mediante el protocolo RDP (Escritorio Remoto).

* *Alternativa de AWS:* Puedes usar herramientas seguras como AWS Systems Manager para acceder sin necesidad de abrir puertos de red.

* Las aplicaciones interactúan con tu instancia directamente a través de la red.

### Paso 3: Usar la instancia

Ya dentro del servidor, tienes control total para realizar tareas de administrador:

* Puedes ejecutar comandos e instalar tu software

* Puedes añadir más almacenamiento u organizar archivos.

---

---
→ Volver al índice: [[📂Computacion/00 - Índice Computacion|🪐 Computacion]]
