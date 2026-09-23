#github #gh-foundations #modulo-6 #releases #packages #github-packages

> [!info] Navegación
> ◀ [[04 - GitHub Copilot]] · ▶ [[🎓 Índice Maestro - GitHub Foundations]]

---

# 05 — Releases y GitHub Packages

> **Resumen ejecutivo:**
> 1. Una **Release** es una publicación oficial de tu software, atada a un Tag, que incluye notas y archivos descargables.
> 2. **GitHub Packages** es el registro de paquetes integrado en GitHub (npm, Maven, Docker, NuGet...).

---

## 1. Releases — Publicar Versiones Oficiales

Una **Release** es la forma que tiene GitHub de empaquetar y publicar una versión de tu software de forma oficial. Imagina que terminas de construir la versión 2.0 de tu aplicación. Quieres:
- Anunciar qué cambios hay en esta versión (notas de la versión).
- Dejar archivos descargables precompilados (el `.exe` para Windows, el `.dmg` para Mac).
- Todo vinculado a un Tag específico del historial de Git.

Eso es exactamente lo que hace una Release.

### Estructura de una Release

| Componente | Descripción |
|:---|:---|
| **Tag** | La versión del código (ej: `v2.0.0`). Puede crearse durante la release. |
| **Título** | Nombre descriptivo (ej: "Aurora — Versión 2.0") |
| **Release notes** | Notas de qué hay de nuevo, bugs corregidos, breaking changes |
| **Assets (archivos)** | Archivos adjuntos descargables: binarios, zips, instaladores |
| **Source code** | GitHub adjunta automáticamente el código fuente en `.zip` y `.tar.gz` |

### Cómo crear una Release

1. Ve a tu repositorio → panel derecho → **Releases** → **"Draft a new release"**.
2. En **"Choose a tag"**, escribe un nuevo tag (ej: `v2.0.0`) o selecciona uno existente.
3. Pon un título y las notas de la versión.
4. Adjunta archivos (binarios, instaladores) arrastrándolos.
5. Si no está lista del todo, guárdala como **"Draft"** (borrador privado). Si está lista, pulsa **"Publish release"**.

> [!TIP] Generate Release Notes automáticamente
> GitHub puede generar las notas de la versión automáticamente: lista todos los Pull Requests fusionados y los contribuidores desde la última release. Botón **"Generate release notes"** al crear la release.

### Pre-releases

Si quieres publicar una versión beta o de prueba, puedes marcarla como **"Set as a pre-release"**. Se publica públicamente pero con la etiqueta `Pre-release`, indicando que no es estable.

---

## 2. GitHub Packages — El Registro de Paquetes

**GitHub Packages** es un servicio de registro de paquetes integrado directamente en GitHub. En lugar de publicar tu librería en un servidor externo, la publicas en GitHub y queda vinculada al repositorio.

### ¿Qué es un registro de paquetes?

Cuando escribes `npm install axios` en tu proyecto Node.js, npm va a un servidor centralizado (el registro de npm) y descarga la librería. GitHub Packages es **ese servidor** pero dentro de GitHub, y soporta varios ecosistemas:

| Ecosistema | Tipo de paquete | Ejemplo de uso |
|:---|:---|:---|
| **npm** | JavaScript / Node.js | `npm install @tu-org/mi-libreria` |
| **Apache Maven** | Java | Dependencias en `pom.xml` |
| **Gradle** | Java / Android | Dependencias en `build.gradle` |
| **NuGet** | .NET / C# | Paquetes para proyectos .NET |
| **RubyGems** | Ruby | Gems de Ruby |
| **Docker** | Contenedores | Imágenes Docker |
| **Containers (GHCR)** | OCI / Docker | `docker pull ghcr.io/tu-org/tu-imagen` |

### ¿Por qué usar GitHub Packages en vez de npm/Docker Hub?

| | npm / Docker Hub público | GitHub Packages |
|:---|:---|:---|
| **Control de acceso** | Público por defecto | Sigue los permisos del repositorio |
| **Integración** | Separado de tu código | El paquete vive junto al código que lo genera |
| **Para paquetes privados** | De pago | Incluido en los planes de GitHub |
| **Ideal para** | Librerías Open Source masivas | Paquetes internos de empresa o de proyectos cerrados |

### Visibilidad de Packages

- Los paquetes de **repositorios públicos** son públicos.
- Los paquetes de **repositorios privados** son privados.
- Se puede cambiar la visibilidad de cada paquete individualmente en la configuración del paquete.

> [!IMPORTANT] GitHub Packages y el consumo de almacenamiento
> El uso de GitHub Packages consume del almacenamiento y del ancho de banda incluido en tu plan. En el plan gratuito, tienes 500 MB de almacenamiento y 1 GB de transferencia de datos al mes para paquetes de repositorios privados. Los paquetes de repositorios públicos son gratuitos.
