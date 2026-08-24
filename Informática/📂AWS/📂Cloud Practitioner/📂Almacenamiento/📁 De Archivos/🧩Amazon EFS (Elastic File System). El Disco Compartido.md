**Tags:** #aws #efs #almacenamiento #nfs #efs-vs-ebs #cloud-practitioner #cp-almacenamiento

> [!summary] El Concepto Clave
> Amazon EFS es un sistema de archivos compartido y elástico para servidores **Linux**. Permite que miles de instancias EC2 lean y escriban en el mismo disco duro virtual **al mismo tiempo**, creciendo y encogiendo su tamaño automáticamente según lo necesites.

---
## 🤝 1. ¿Por qué necesitamos EFS? (La Analogía)

* **El Problema con EBS:** Imagina que tienes 3 servidores web (EC2) que necesitan leer la misma carpeta llena de configuraciones. Si usas EBS, es como un disco duro USB normal: solo puedes enchufarlo a **un** ordenador a la vez.

* **La Solución (EFS):** EFS es como la **"Carpeta Compartida" de la oficina** (un NAS por red). Puedes "enchufar" ese mismo sistema de archivos a los 3 servidores web a la vez, incluso si están en diferentes Zonas de Disponibilidad (AZ). 

---

## 🥊 2. El Duelo Final: EBS vs. EFS

Esta comparativa te va a dar muchos puntos en el Cloud Practitioner. Tienes que tener muy claras sus diferencias.

| Característica | Amazon EBS (El Disco Individual) | Amazon EFS (La Carpeta Compartida) |
| :--- | :--- | :--- |
| **Conexiones simultáneas** | Normalmente **1** sola instancia EC2. | **Miles** de instancias EC2 a la vez. |
| **Alcance geográfico** | Bloqueado en **1 sola Zona de Disponibilidad (AZ)**. | Disponible en **Múltiples AZs** (a nivel de Región). |
| **Escalabilidad (Tamaño)** | Fijo. Si pides 2TB y lo llenas, te quedas sin espacio (tienes que pedir más a mano). | **Elástico**. Crece y se encoge automáticamente a medida que añades o borras archivos. ¡No hay que aprovisionar tamaño! |
| **Sistema Operativo** | Windows, Linux, Mac... (cualquiera). | **Solo Linux** (usa el protocolo NFS v4). |

---

## 📚 3. Clases de Almacenamiento y Ciclo de Vida

Al igual que S3, EFS sabe que no todos los archivos que guardas en esa carpeta compartida se usan todos los días. Para ahorrar dinero, tiene "estantes" y mueve los archivos automáticamente mediante **Políticas de Ciclo de Vida**.

### Las Clases (Los Estantes)

1. **EFS Standard:** Archivos a los que se accede con frecuencia. Es Multi-AZ (sobrevive si un centro de datos arde).

2. **EFS Standard-Infrequent Access (IA):** Archivos que casi no tocas. Es más barato, pero te cobran una penalización mínima al leerlos.

3. **EFS Archive:** Datos muy fríos que tocas unas pocas veces al año. El coste de almacenamiento es bajísimo.

4. **Opciones "One Zone" (Una Zona):** Versiones más baratas de las clases anteriores que **NO** se replican en varios centros de datos. Si esa zona cae, pierdes la conexión.

### El Ciclo de Vida en Acción

* *Por defecto:* Si no abres un archivo en **30 días**, EFS lo empuja de *Standard* a *IA*.
* *Por defecto:* Si pasa a no abrirse en **90 días**, lo empuja al trastero de *Archive*.
* Si un día decides abrir ese archivo antiguo, la política dictará si se queda en el trastero o si lo vuelve a subir al estante principal (*Standard*).

---
→ Volver al índice: [[📂Almacenamiento/00 - Índice Almacenamiento|🪐 Almacenamiento]]
