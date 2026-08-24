# 💻 ¿Qué es una máquina virtual?

Una **máquina virtual (VM)** es como **una computadora dentro de tu computadora**.

👉 Ejemplo:  
Imagina que tienes un ordenador con Windows, pero quieres practicar con Linux.  
En lugar de comprar otro ordenador, instalas una máquina virtual (como VirtualBox).  
Dentro de ella, puedes instalar Ubuntu (Linux) como si fuera un ordenador nuevo.  
Tiene su propio disco, su memoria, y su sistema operativo.

➡️ En resumen:  
Una máquina virtual es **una copia virtual de un ordenador real** dentro del tuyo.

-------------------------------------------------

# 🧰  ¿Qué es WSL?

WSL (Windows Subsystem for Linux) es una forma más **ligera** de usar Linux dentro de Windows **sin una máquina virtual completa**.

👉 Ejemplo:  
En lugar de abrir VirtualBox, simplemente abres una ventana de terminal y escribes:

`wsl`

Y ¡pum! Aparece Linux dentro de Windows.

Puedes usar comandos como si estuvieras en un Linux real (crear carpetas, instalar cosas, programar).  
Usa los mismos archivos del sistema, así que es muy rápido.

-------------------------------------------------

# 🌐 ¿Qué es Port Forwarding (reenvío de puertos)?

Voy a explicártelo con un ejemplo más claro todavía:

👉 Imagina que tienes:

- Tu PC real con Windows.
    
- Una máquina virtual con Linux que tiene una app (por ejemplo, una web) funcionando en el **puerto 3000**.
    

Tu PC no puede entrar directamente dentro de la VM, pero si le dices:

> “Oye, cada vez que alguien entre a mi PC por el puerto 3000, mándalo a la máquina virtual.”

Eso es **port forwarding**.

🔹 Ejemplo real:

- Tu VM tiene una web en `http://localhost:3000`.
    
- En tu PC real pones en el navegador `http://localhost:3000`.
    
- Gracias al port forwarding, se abre **la web que está dentro de la VM**.
    

📦 Es como si pusieras una **ventana** entre tu PC y la máquina virtual.

-------------------------------------------------

# 🧱 ¿Qué es un Sistema Operativo?

Es el **jefe de todos los programas**.

👉 Ejemplo:  
Cuando abres Chrome, Spotify o Word, el sistema operativo (Windows, Linux o macOS) les dice:

> “Tú usa este trozo de memoria.”  
> “Tú guarda esto en el disco.”  
> “Tú pinta esto en la pantalla.”

Sin sistema operativo, la computadora no sabría organizarse.

-------------------------------------------------

# **⚙️Vagrant**

Es una herramienta que permite **crear entornos virtuales reproducibles**, con mayor rapidez y a mayor escala(poder crear muchas máquinas virtuales a la vez).

**Ejemplo real:**

- Configurar un servidor con Linux y todas las dependencias para tu proyecto sin tener que instalar manualmente nada en tu PC.

-------------------------------------------------

# **​🤖​Automatización**

Uso de **scripts o herramientas** para hacer tareas repetitivas sin intervención humana.

**Ejemplo real:**

- Actualizar automáticamente todas las copias de seguridad de una base de datos cada noche.
    
- Enviar emails a los clientes cuando se realiza un pedido online.

-------------------------------------------------

# **​💭​Startup**

Empresa joven que busca crecer rápidamente usando tecnología e innovación.

**Ejemplo real:**

- Una empresa que desarrolla una app de reparto de comida desde casa.
    
- Google empezó como startup antes de convertirse en una gran empresa.

-------------------------------------------------

## 🐳 **Contenedores y Docker**

Un **contenedor** es como una **caja que contiene tu aplicación lista para usar**, con todo lo que necesita (librerías, configuraciones, dependencias).  
Así funciona igual en cualquier ordenador o servidor.

**Ejemplo real:**

- Haces una aplicación web que usa Python y MySQL.
    
- En lugar de instalar todo en tu PC, lo metes en un **contenedor Docker**.
    
- En otro ordenador solo necesitas ejecutar `docker run` y listo, sin instalar nada.
    

**Ventajas:**

- Todo funciona igual en cualquier sitio.
    
- Es más rápido que usar una máquina virtual.
    
- Fácil de actualizar o eliminar.

-------------------------------------------------


## 🟪​ **Kubernetes**

Kubernetes es un **“organizador” de contenedores** (como Docker) que los gestiona automáticamente.  
Sirve para **mantener muchas aplicaciones corriendo al mismo tiempo**, repartiendo la carga y reiniciando contenedores si fallan.

**Ejemplo real:**

- Tienes una web con miles de usuarios.
    
- Kubernetes arranca más contenedores si entra mucha gente y los apaga cuando baja el tráfico.
    
- Si uno se cae, lo reemplaza solo.
    

**Idea fácil:**  
Piensa que Docker crea los contenedores, y Kubernetes es el “jefe” que los coordina para que todo siga funcionando.