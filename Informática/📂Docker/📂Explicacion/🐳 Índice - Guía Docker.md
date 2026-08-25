# 🐳 Guía Definitiva de Docker y Docker Compose

> [!info] 📌 Sobre esta guía
> Guía completa basada en el **roadmap oficial de Docker** ([roadmap.sh/docker](https://roadmap.sh/docker)). Cada concepto se explica desde cero con analogías, ejemplos prácticos y profundidad técnica real. Escrita en formato **Obsidian** con callouts, enlaces internos y tablas comparativas.

---

## 📚 Mapa de Contenido (MOC)

### 🟢 Fundamentos

| # | Sección | Archivos |
|---|---|---|
| 01 | **Introducción al Mundo Docker** | [[🐳Introducción al Mundo Docker]] |
| 02 | **Tecnologías Subyacentes** | [[Namespaces]] · [[Cgroups]] · [[Union Filesystems]] |
| 03 | **Instalación y Setup** | [[Instalación y Setup]] |

### 🔵 Uso Diario

| # | Sección | Archivos |
|---|---|---|
| 04 | **CLI y Conceptos Básicos** | [[Imágenes en Docker]] · [[Contenedores en Docker]] · [[Redes en Docker]] |
| 05 | **Persistencia de Datos** | [[Sistema de Archivos Efímero]] · [[Volume Mounts]] · [[Bind Mounts]] |

### 🟣 Construcción y Distribución

| # | Sección | Archivos |
|---|---|---|
| 06 | **Construcción de Imágenes** | [[Dockerfile - Anatomía Completa]] · [[Caché de Capas y Optimización]] |
| 07 | **Registries** | [[Registries y Etiquetado de Imágenes]] |

### 🟠 Orquestación y Producción

| # | Sección | Archivos |
|---|---|---|
| 08 | **Docker Compose** | [[Docker Compose]] |
| 09 | **Seguridad y Redes Avanzadas** | [[Seguridad en Docker]] |
| 10 | **Developer Experience** | [[Hot Reloading y DX]] |

---

## 🗺️ Diagrama de aprendizaje

```
Introducción ──► Tecnologías Subyacentes ──► Instalación
                  (Namespaces, Cgroups,        │
                   Union FS)                   ▼
                                          CLI Básica
                                     (Imágenes, Contenedores,
                                          Redes)
                                              │
                            ┌─────────────────┼─────────────────┐
                            ▼                 ▼                 ▼
                      Persistencia      Dockerfiles        Registries
                     (Volumes, Binds)  (Build, Cache)     (Hub, Tags)
                            │                 │                 │
                            └─────────────────┼─────────────────┘
                                              ▼
                                       Docker Compose
                                              │
                                    ┌─────────┴─────────┐
                                    ▼                   ▼
                              Seguridad            Dev Experience
                            (Runtime, Redes)      (Hot Reload, DX)
```

---

> [!tip] ¿Cómo usar esta guía?
> - Si eres **principiante total**: Sigue el orden numérico (01 → 10).
> - Si ya conoces Docker y quieres **profundizar**: Ve directo a la sección que necesites.
> - Si buscas una **referencia rápida de comandos**: Consulta [[Imágenes en Docker]], [[Contenedores en Docker]] y [[Redes en Docker]].
> - Si quieres **montar un proyecto con Compose**: Ve directo a [[Docker Compose]].
