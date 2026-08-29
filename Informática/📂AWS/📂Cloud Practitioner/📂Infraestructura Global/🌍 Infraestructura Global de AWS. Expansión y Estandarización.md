**Tags:** #aws #infraestructura-global #regiones #edge-locations #cloudformation #iac #cloud-practitioner #cp-infraestructura-global


> [!summary] El Concepto Clave
> Llevar tu aplicación a nivel mundial implica decidir **dónde** colocar tus servidores principales (Regiones), usar "puntos de acceso rápido" para acelerar el contenido (Ubicaciones Periféricas) y automatizar la creación de servidores para que todo sea idéntico en cualquier país (CloudFormation).

---
## 🗺️ 1. Las Regiones de AWS

Cuando te expandes, no abres servidores al azar. Tienes que elegir estratégicamente dónde construir tus centros de datos principales. 

En AWS, debes considerar varios factores para elegir una Región:

*   **Proximidad a los clientes (Latencia):** Para que la web cargue rápido.

*   **Regulaciones locales (Cumplimiento normativo):** Algunas leyes exigen que los datos no salgan del país.

*   **Costes:** Los precios de los servicios de AWS varían de una región a otra por la electricidad por ejemplo.

--- 
## 🛒 2. Ubicaciones Periféricas / Edge Locations

No puedes instalar servidores gigantes en cada esquina del mundo, pero sí puedes poner puntos de distribución rápidos (Caché) en lugares estratégicos fuera de la región.

*   **¿Qué son?** Instalaciones de menor tamaño repartidas por todo el mundo, mucho más numerosas que las Regiones.

*   **¿Para qué sirven?** Para **almacenar en caché** (guardar copias temporales) el contenido estático que más se pide (imágenes, vídeos, páginas web). 

*   **El Beneficio:** Los usuarios obtienen el contenido casi al instante (baja latencia) conectándose al la edge location de su ciudad, sin tener que cruzar el océano para conectarse al servidor central.

---
## 📜 3. Infraestructura como Código (IaC) y AWS CloudFormation (La Receta Estándar)

Imagina que tienes una arquitectura perfecta funcionando en la Región A (París) y quieres copiarla exactamente igual en la Región B (Tokio) para tener alta disponibilidad.

**Hacerlo a mano:** Implica entrar a la consola, recordar cada configuración de red, cada tamaño de instancia EC2 y cada regla de seguridad. 

**Los riesgos:** Es un proceso lento, es muy fácil equivocarse (olvidar un puerto abierto) y es muy difícil de replicar a gran escala.

Esta es la manera de solucionar esto:

*   **Infraestructura como Código (IaC):** Escribes un archivo de texto (en formato YAML con CloudFormation o también puedes hacerlo HCL con Terraform) con todo lo que necesita tu sistema (ej. Quiero 2 EC2, 1 ELB y 1 Base de datos).

*   **AWS CloudFormation:** Es el servicio de AWS que lee esa receta y construye todo automáticamente por ti. Es como una impresora 3D tu le pasas el plano y te monta lo que le has indicado.

*   **El Beneficio:** Elimina el error humano. Puedes desplegar tu arquitectura en Europa, darle a un botón, y CloudFormation creará una copia milimétricamente exacta en Asia en cuestión de minutos.

---

---
→ Volver al índice: [[📂Infraestructura Global/00 - Índice Infraestructura Global|🪐 Infraestructura Global]]
