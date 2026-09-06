# 📚 Apuntes Técnicos & Conocimiento

¡Bienvenido/a a mi repositorio de apuntes! Este espacio es mi segundo cerebro 🧠. Aquí documento todo lo que voy aprendiendo, desarrollando y explorando en el mundo de la informática, la programación, software, cloud, devops... 

Esta bóveda de conocimiento está construida en **Obsidian** y publicada automáticamente en la web como un jardín digital gracias a **Quartz** y **GitHub Actions**.

---

## 🛠️ Tecnologías y Temáticas

A medida que avanzo en mis estudios y proyectos, voy subiendo contenido organizado en diferentes áreas. Actualmente, en estos apuntes podrás encontrar:

### 🔒 Seguridad Digital
- Conceptos base de redes, servidores y malware.
- Gestión de identidades, buenas prácticas, Contraseñas, 2FA y MFA.
- Ingeniería Social: Phishing, Session Hijacking y análisis de amenazas y ataques reales.

### ☁️ Cloud & IA (AWS Practitioner)
- **Cómputo (Compute)**: Despliegue de servidores (EC2), arquitecturas Serverless (AWS Lambda) y balanceo de carga.
- **Almacenamiento (Storage)**: Diferencias clave entre S3 (objetos), EBS (bloques) y EFS (archivos).
- **Bases de Datos**: Motores relacionales (RDS, Amazon Aurora) y bases de datos NoSQL (DynamoDB).
- **Redes y Seguridad**: VPCs, Subredes, Control de accesos (IAM), Grupos de Seguridad (Firewalls) y WAF.
- **Inteligencia Artificial (IA Generativa)**:
  - **Amazon Bedrock**: Catálogo de modelos, RAG Gestionado (Knowledge Bases) y Agents for Bedrock.
  - **Amazon Q**: Asistentes IA aplicados en entornos Developer, Business y QuickSight.
  - **SageMaker**: Servicio completamente gestionado que permite a los desarrolladores y científicos de datos construir, entrenar y desplegar modelos de Machine Learning (ML) a cualquier escala, facilitando todo el ciclo de vida de los proyectos de IA.
- Infraestructura global, control de facturación (Pricing) y diseño de arquitecturas Cloud robustas.

### 🐧 Linux, Terminal & Bash Scripting
- **Fundamentos y Arquitectura**: Conceptos de software libre, el Kernel vs espacio de usuario, distribuciones GNU/Linux y estructura del árbol de directorios único bajo `/` (FHS) con rutas absolutas y relativas.
- **Navegación y Comandos Esenciales**: Inspección y ayuda (`pwd`, `ls`, `tree`, manuales `man`/`--help`), manipulación de archivos y carpetas (`touch`, `mkdir`, `cp`, `mv`, `rm`) y comodines (wildcards).
- **Seguridad y Permisos POSIX**:
  - **Permisos y Propiedad**: Notación octal y simbólica (`chmod`), control de usuarios/grupos/otros (`u/g/o`, `r/w/x`) y cambio de propietarios (`chown`, `chgrp`).
  - **Seguridad Avanzada**: Máscaras con `umask`, permisos especiales (SUID, SGID, Sticky Bit) y administración de identidades (`/etc/passwd`, `sudo`, `visudo`).
- **Flujo de Datos, Redes y Procesos**:
  - **Pipes y Filtros**: Redirección de flujos estándar (`stdin`, `stdout`, `stderr`), tuberías (`|`) y procesamiento con `grep`, `wc`, `sort`, `uniq`, `head` y `tail -f`.
  - **Gestión de Procesos**: Monitorización (`ps`, `top`, `htop`), control de señales (`kill`, `SIGTERM`, `SIGKILL`) y administración en segundo plano (`jobs`, `fg`, `bg`).
  - **Redes y Conectividad**: Diagnóstico de interfaces (`ip`, `ifconfig`), pruebas de conectividad (`ping`), transferencia con `curl`/`wget` y modos de red (NAT vs Bridged).
- **Automatización y Scripting en Bash**:
  - **Estructura y Parámetros**: Shebang (`#!/bin/bash`), variables locales/entorno (`export`), lectura interactiva (`read`) y argumentos posicionales (`$1`, `$@`, `$#`).
  - **Lógica y Control de Flujo**: Evaluación matemática, condicionales (`if/elif/else`, `case`), operadores de test, bucles (`for`, `while`, `until`) y funciones modulares con control de errores (`exit`, `$?`).
  - **Programación de Tareas**: Automatización periódica desatendida mediante el demonio `cron` y sintaxis en `crontab`.
- **Entornos Modernos de Terminal**: Productividad con **Warp Terminal** (IA integrada, bloques interactivos y workflows) y configuración avanzada de **ZSH** con **Oh My ZSH** (temas y plugins).

### 💻 Programación y Desarrollo (Desktop & Móvil)
- **C# & WPF (Desktop)**:
  - **Arquitectura MVVM**: Separación estricta de responsabilidades entre Vista (XAML), ViewModel (lógica) y Modelo (datos) para proyectos escalables y desacoplados.
  - **Data Binding & Comandos**: Enlace de datos reactivo y bidireccional, sustitución de métodos de *code-behind* mediante comandos e integración de **Triggers y Behaviors** (`Microsoft.Xaml.Behaviors.Wpf`).
  - **Modularidad y Lógica**: Creación de componentes reutilizables con **UserControls**, validaciones de interfaz y estructuración de capas de servicios (`Services`).
- **Kotlin & Android**: Interfaces declarativas con Jetpack Compose, ViewModels y gestión de estados de interfaz (UI).
- **Persistencia de Datos**: Bases de datos locales robustas con **Room** (DAO, Flow, LiveData, Migraciones) y Datastore para Tokens.
- **Comunicación Remota**: Consumo de APIs REST y conexión con servidores usando **Retrofit**.
  
### 🖥️ Sistemas Informáticos
- Componentes de hardware e historia de la informática (desde la electricidad y los transistores hasta las puertas lógicas, ALU y CPUs modernas).
- **Virtualización y DevOps**: Uso de máquinas virtuales, automatización y despliegue con **Vagrant** (Muy por encima).
- Fundamentos sólidos de Bases de Datos, Redes e Internet y APIs (ej. Javalin).

---

## ⚙️ ¿Cómo funciona este repositorio y su sincronización automática?
Este proyecto utiliza un sistema completamente automatizado para que mis apuntes pasen de estar en mi ordenador a verse en la web sin que tenga que hacer nada de forma manual:

1. Trabajo local: Primero, escribo, modifico o añado nuevos archivos de notas en local en Obsidian.

2. Sincronización automática con Git: Gracias al plugin de Git instalado en Obsidian y a la carpeta oculta .git, la aplicación está conectada directamente con este repositorio remoto. Con el plugin puedes configurar que si hay cambios se haga un commit, push o pull cada 'X' tiempo, por lo que detecta mis cambios de manera autónoma en segundo plano, empaqueta los archivos (commit) y los sube a la nube (push) sin que yo me entere.

3. Despliegue en la web (CI/CD): Tan pronto como los cambios llegan a GitHub, una GitHub Action entra en juego de fondo. Esta acción compila el sitio web estático utilizando Quartz v4, ajusta la configuración al vuelo y lo despliega públicamente en GitHub Pages para que la web esté siempre actualizada al instante.

Todo esto sin yo enterarme, ni abrir terminal, ni tocar absolutamente nada.

## 🌐 Visita la Web
Puedes ver la versión interactiva, renderizada y navegable de todos estos apuntes visitando el enlace del entorno de **GitHub Pages** (disponible en la sección de *Deployments* a la derecha de este repositorio).

También puedes acceder desde aquí: https://izann06.github.io/Apuntes-Tecnicos-Obsidian/

---
*Repositorio creado con esfuerzo, mucha curiosidad y ganas de aprender.* 🚀
