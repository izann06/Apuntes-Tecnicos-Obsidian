# 📚 Apuntes Técnicos & Segundo Cerebro

![Obsidian](https://img.shields.io/badge/Obsidian-483699?style=for-the-badge&logo=obsidian&logoColor=white)
![Quartz](https://img.shields.io/badge/Quartz-v4-31b35b?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

¡Bienvenido/a a mi repositorio de apuntes! Este espacio funciona como mi **segundo cerebro** 🧠. Aquí documento todo lo que voy aprendiendo, desarrollando y explorando en el mundo de la informática, programación, sistemas, infraestructura en la nube y devops.

Esta bóveda de conocimiento está construida en **Obsidian** y se publica automáticamente en la web como un jardín digital (*digital garden*) gracias a **Quartz** y **GitHub Actions**.

---

## 🛠️ Tecnologías y Temáticas

A medida que avanzo en mis estudios y proyectos, voy estructurando el contenido en diferentes áreas clave. En estos apuntes encontrarás:

### 🔒 Seguridad Digital
- **Bases y Fundamentos:** Conceptos clave de redes, servidores y tipologías de malware.
- **Identidad y Accesos:** Gestión de identidades, buenas prácticas, seguridad de contraseñas, 2FA y MFA.
- **Vectores de Ataque:** Ingeniería Social (Phishing), Session Hijacking y análisis de amenazas/ataques reales.

### ☁️ Cloud & IA (AWS Practitioner)
- **Cómputo (Compute):** Despliegue de servidores (EC2), arquitecturas Serverless (AWS Lambda) y balanceo de carga.
- **Almacenamiento (Storage):** Diferencias clave entre S3 (objetos), EBS (bloques) y EFS (archivos).
- **Bases de Datos:** Motores relacionales (RDS, Amazon Aurora) y bases de datos NoSQL (DynamoDB).
- **Redes y Seguridad:** VPCs, Subredes, Control de Accesos (IAM), Grupos de Seguridad (Firewalls) y WAF.
- **Inteligencia Artificial (IA Generativa):**
  - **Amazon Bedrock:** Catálogo de modelos, RAG Gestionado (*Knowledge Bases*) y Agents for Bedrock.
  - **Amazon Q:** Asistentes de IA aplicados en entornos Developer, Business y QuickSight.
  - **SageMaker:** Plataforma gestionada para el ciclo de vida completo de modelos de Machine Learning (ML) a gran escala.
- **Arquitectura Global:** Infraestructura global de AWS, control de facturación (Pricing) y diseño robusto (*Well-Architected*).

### 🐧 Linux, Terminal & Bash Scripting
- **Fundamentos y Arquitectura:** Software libre, el Kernel vs Espacio de Usuario, distribuciones GNU/Linux y la estructura del árbol de directorios (`/`) bajo el estándar FHS.
- **Navegación y Comandos Esenciales:** Inspección (`pwd`, `ls`, `tree`), manipulación de archivos (`touch`, `mkdir`, `cp`, `mv`, `rm`) y uso de *wildcards*.
- **Seguridad y Permisos POSIX:**
  - Control mediante notación octal y simbólica (`chmod`).
  - Administración de usuarios, grupos y propietarios (`chown`, `chgrp`, `sudo`).
  - Seguridad avanzada: Máscaras (`umask`) y permisos especiales (SUID, SGID, Sticky Bit).
- **Flujo de Datos, Redes y Procesos:**
  - Redirección de flujos estándar (`stdin`, `stdout`, `stderr`) y tuberías (`|`).
  - Filtros de texto (`grep`, `wc`, `sort`, `awk`, `tail -f`).
  - Monitorización y control de procesos (`ps`, `top`, `htop`, `kill`, señales).
  - Diagnóstico de red (`ip`, `ping`, `curl`, `wget`).
- **Automatización y Scripting en Bash:**
  - *Shebang*, variables de entorno (`export`), lectura interactiva y argumentos posicionales (`$1`, `$@`).
  - Lógica y control de flujo (condicionales `if/case`, bucles `for/while`), evaluación matemática y funciones.
  - Automatización desatendida mediante el demonio `cron` y `crontab`.
- **Entornos Modernos:** Productividad con **Warp Terminal** (IA integrada) y configuración avanzada de **ZSH** con **Oh My ZSH** (temas y plugins).

### 💻 Programación y Desarrollo (Desktop & Móvil)
- **C# & WPF (Desktop):**
  - **Arquitectura MVVM:** Separación estricta entre Vista (XAML), ViewModel y Modelo para proyectos escalables.
  - **Data Binding & Comandos:** Enlace bidireccional de datos reactivos, *Triggers* y *Behaviors* para sustituir el *code-behind*.
  - **Modularidad:** Creación de componentes reutilizables (*UserControls*), validación de interfaces y abstracción en capas de servicios.
- **Kotlin & Android (Móvil):**
  - Interfaces declarativas con **Jetpack Compose** y gestión de estados de UI con ViewModels.
  - Consumo de APIs REST utilizando **Retrofit**.
  - Persistencia de datos local robusta con **Room** (DAO, Flow, LiveData, Migraciones) y Datastore.
  
### 🖥️ Sistemas Informáticos & Hardware
- **Historia y Hardware:** Desde la electricidad y los transistores hasta las puertas lógicas, ALU y CPUs modernas.
- **Virtualización:** Uso de máquinas virtuales, automatización y despliegue rápido con **Vagrant** (conceptos básicos).
- **Redes e Internet:** Fundamentos sólidos de protocolos, bases de datos y creación de APIs web (ej. Javalin).

---

## ⚙️ Arquitectura de Sincronización Automatizada (CI/CD)

Este proyecto cuenta con una canalización (*pipeline*) totalmente invisible y automatizada para mantener la web siempre actualizada sin ningún esfuerzo manual:

1. **Trabajo Local:** Escribo, modifico o estructuro mis notas directamente en la aplicación de Obsidian.
2. **Auto-Sincronización (Git):** Mediante el plugin *Obsidian Git*, mi bóveda local detecta los cambios y realiza de forma autónoma operaciones de *commit* y *push* hacia este repositorio de GitHub cada determinado tiempo.
3. **Despliegue Instantáneo (GitHub Actions):** En el momento en que los cambios tocan el repositorio remoto, se dispara una acción de CI/CD en segundo plano. Esta acción compila todo el sitio web estático usando **Quartz v4** y lo publica al instante en **GitHub Pages**.

> ⚡ ¡Todo el proceso ocurre en segundo plano sin que yo tenga que abrir la terminal ni introducir comandos!

---

## 🌐 Visita la Web

Puedes interactuar con mis apuntes a través de una interfaz limpia, navegable y estructurada como grafo directamente en la web.

🚀 **Enlace directo al Jardín Digital:**
👉 [https://izann06.github.io/Apuntes-Tecnicos-Obsidian/](https://izann06.github.io/Apuntes-Tecnicos-Obsidian/)

También está disponible en la sección de *Deployments* (a la derecha en este repositorio).

---
*Repositorio creado con esfuerzo, mucha curiosidad y ganas de aprender.* 🚀
