
# **MEMORIA COMPLETA: Problema y solución para crear una VM en Vagrant**

---

## **1️⃣ Problema inicial**

Al ejecutar:

`vagrant up`

- La VM se quedaba **bloqueada en “Importing base box 'ubuntu/focal64'...”**
 
- No aparecía ninguna ventana de VirtualBox ni avanzaba el progreso.
 

**Síntomas:**

- Todas las boxes probadas (`focal64`, `bionic64`, `jammy64`) se quedaban colgadas.
 
- Mensajes de error como `VBOX_E_IPRT_ERROR` al intentar importar manualmente el OVF.
 

---

## **2️⃣ Causas detectadas**

1. **Box corrupta:**
 
 - La box `ubuntu/focal64` estaba dañada.
 
2. **Bloqueos de VirtualBox por Windows:**
 
 - **Integridad de memoria (Memory Integrity)** activada.
 
 - **WSL2 habilitado** (usa su propio hypervisor).
 
 - `hypervisorlaunchtype = Auto` → Windows arranca un hypervisor interno que bloquea VirtualBox.
 

> 2.Estos tres bloqueos provocan que VirtualBox se quede en 20% al importar cualquier VM.

---

## **3️⃣ Solución paso a paso**

### **Paso 1: Borrar boxes corruptas**

En **PowerShell como administrador**:

`vagrant box remove ubuntu/focal64 --force vagrant box remove ubuntu/bionic64 --force vagrant box remove ubuntu/xenial64 --force vagrant box remove ubuntu/jammy64 --force`

Esto borra todos los boxes que hemos hecho en VirtualBox tanto de Xenial,Bionic,Jammy,Focal... Ya que puede haber un error que arrastremos de ahí.

Opcional: borrar la carpeta de boxes manualmente si no queires borrarla con el codigo de arriba:

`C:\Users\izanm\.vagrant.d\boxes\`

---

### **Paso 2: Desactivar bloqueos de Windows

1. **Integridad de memoria**
 
 - Seguridad de Windows → Seguridad del dispositivo → Aislamiento del núcleo → Desactivar **Integridad de memoria**
 
2. **Ahora ve a PowerShell Admin** para apagar el hypervisor de Windows:**
 

`bcdedit /set hypervisorlaunchtype off`

3. **Apagar WSL2 y VirtualMachinePlatform**:
 

`wsl --shutdown
`Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux 
`Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform`

4. **Reiniciar el PC** después de estos cambios.
 

---

### **Paso 3: Reinstalar VirtualBox**

1. Desinstalar VirtualBox completamente.
 
2. Reiniciar Windows.
 
3. Instalar **VirtualBox 7.0.0** como administrador.
 
4. Instalar el **Extension Pack** (opcional pero recomendado).
	En virtualBox arriba en Archivo,Herramientas,Extension Pack Manager ahi tiene que estar esta extensión.

5. ![[Oracle_VM_VirtualBox_Extension_Pack-7.0.0.vbox-extpack]]
 

---

### **Paso 4: Probar con una box ligera y confiable**

En una carpeta vacía:

`mkdir pruebaVM 
`cd pruebaVM 
`vagrant init bento/ubuntu-20.04 
`vagrant up`

- Esta box es ligera y no suele corromperse.

- No hace falta tocar el codigo de vagrantFile.
 
- Si funciona, tu VirtualBox está correcto.
 

---

## **4️⃣ Vagrantfile definitivo con Git, Maven y JDK23**

`Vagrant.configure("2") do |config| config.vm.box = "bento/ubuntu-20.04" config.vm.provider "virtualbox" do |vb| vb.cpus = 2 vb.memory = 2048 end config.vm.provision "shell", inline: <<-SHELL sudo apt update -y sudo apt install -y git maven software-properties-common sudo add-apt-repository -y ppa:openjdk-r/ppa sudo apt update -y if ! sudo apt install -y openjdk-23-jdk; then sudo apt install -y openjdk-21-jdk fi java -version javac -version git --version mvn -version SHELL end`

- Instala **Git, Maven y JDK23**
 
- Configura **2 CPUs y 2GB RAM**
 
- Box ligera y estable: `bento/ubuntu-20.04`
 

---

## **5️⃣ Crear y arrancar la VM**

En la carpeta del Vagrantfile (PowerShell Admin):

`vagrant up`

---

## **6️⃣ Conectarse a la VM**

**Desde Windows / host**:

`vagrant ssh`

> **Importante:**
> 
> - Este comando se ejecuta **en Windows**, no dentro de la VM.
> 
> - Dentro de la VM ya no necesitas usuario ni contraseña.
> 

Dentro de la VM puedes comprobar:

`git --version mvn -version java -version javac -version`

---

## **✅ Resultado final**

- VM creada correctamente
 
- Git, Maven y JDK23 funcionando
 
- Carpeta compartida `/vagrant` para trabajar con Windows
 
- VM estable, sin quedarse colgada en import
 
- Preparada para proyectos Java/Maven
 

---
