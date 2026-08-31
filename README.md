# 📚 Apuntes Técnicos & Conocimiento

¡Bienvenido/a a mi repositorio de apuntes! Este espacio es mi "segundo cerebro" 🧠. Aquí documento todo lo que voy aprendiendo, desarrollando y explorando en el mundo de la informática, la programación y la tecnología en general. 

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
- Infraestructura global, control de facturación (Pricing) y diseño de arquitecturas Cloud robustas.

### 💻 Programación y Desarrollo Móvil
- **Kotlin & Android**: Interfaces declarativas con Jetpack Compose, ViewModels y gestión de estados de interfaz (UI).
- **Persistencia de Datos**: Bases de datos locales robustas con **Room** (DAO, Flow, LiveData, Migraciones) y Datastore para Tokens.
- **Comunicación Remota**: Consumo de APIs REST y conexión con servidores usando **Retrofit**.
- **Desarrollo de Videojuegos**: Motor **LibGDX**, ciclo de vida, renderizado 2D y simulaciones de físicas realistas con **Box2D**.

### 🖥️ Sistemas Informáticos
- Componentes de hardware e historia de la informática (desde la electricidad y los transistores hasta las puertas lógicas, ALU y CPUs modernas).
- **Virtualización y DevOps**: Uso de máquinas virtuales, automatización y despliegue con **Vagrant**.
- Fundamentos sólidos de Bases de Datos, Redes e Internet y APIs (ej. Javalin).

---

## ⚙️ ¿Cómo funciona este repositorio y su sincronización automática?
Este proyecto utiliza un sistema completamente automatizado para que mis apuntes pasen de estar en mi ordenador a verse en la web sin que tenga que hacer nada de forma manual:

1. Trabajo local: Primero, escribo, modifico o añado nuevos archivos de notas en local en Obsidian.

2. Sincronización automática con Git: Gracias al plugin de Git instalado en Obsidian y a la carpeta oculta .git, la aplicación está conectada directamente con este repositorio remoto. Con el plugin puedes configurar que si hay cambios se haga un commit, push o pull cada 'X' tiempo, por lo que detecta mis cambios de manera autónoma en segundo plano, empaqueta los archivos (commit) y los sube a la nube (push) sin que yo me entere.

3. Despliegue en la web (CI/CD): Tan pronto como los cambios llegan a GitHub, una GitHub Action entra en juego de fondo. Esta acción compila el sitio web estático utilizando Quartz v4, ajusta la configuración al vuelo y lo despliega públicamente en GitHub Pages para que la web esté siempre actualizado al instante.

Todo esto sin yo enterarme, ni abrir terminal, ni tocar absoulutamente nada.

## 🌐 Visita la Web
Puedes ver la versión interactiva, renderizada y navegable de todos estos apuntes visitando el enlace del entorno de **GitHub Pages** (disponible en la sección de *Deployments* a la derecha de este repositorio).

También puedes acceder desde aqui: https://izann06.github.io/Apuntes-Tecnicos-Obsidian/

---
*Repositorio creado con esfuerzo, mucha curiosidad y ganas de aprender.* 🚀
