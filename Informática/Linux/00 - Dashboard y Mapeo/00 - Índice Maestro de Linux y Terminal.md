---
tags:
  - linux
  - moc
  - dashboard
  - índice
carpeta: "00 - Dashboard y Mapeo"
fecha: 2026-09-01
aliases:
  - MOC Linux
  - Dashboard Linux
  - Índice Linux
---

# 🐧 Índice Maestro de Linux, Terminal, Redes y Bash

> [!abstract] 🧠 Tu mapa de navegación central
> Este archivo es el **Mapa de Contenido (MOC)** de toda la sección de Linux. Funciona como un dashboard interactivo desde el que puedes saltar directamente a cualquier tema. Cada enlace te lleva a una nota extensa y detallada con ejemplos prácticos, analogías y comandos reales.

---

## 📚 Mapa de Contenido Completo

### 🟢 01 - Fundamentos y Arquitectura

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 01.1 | **¿Qué es Linux?** | [[01.1 - Qué es Linux (Kernel vs Aplicaciones)]] | Software libre, GNU/Linux, el kernel como corazón del sistema y las distribuciones como sabores |
| 01.2 | **Árbol de Directorios** | [[01.2 - El Árbol de Directorios y File System de Linux]] | El sistema de archivos único bajo `/`, propósito de cada directorio y comparativa con Windows |
| 01.3 | **Rutas** | [[01.3 - Rutas Absolutas vs Relativas]] | Cómo construir direcciones para llegar a cualquier archivo: absolutas, relativas, `.`, `..` y `~` |

---

### 🔵 02 - Comandos y Navegación Básica

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 02.1 | **Orientación y Ayuda** | [[02.1 - Orientación, Inspección y Ayuda]] | `pwd`, `cd`, `ls`, `tree`, información del sistema y los manuales `man`/`info`/`--help` |
| 02.2 | **Manipulación** | [[02.2 - Manipulación de Archivos y Carpetas]] | `touch`, `mkdir`, `rm`, `cp`, `mv` y la sensibilidad a mayúsculas de Linux |
| 02.3 | **Wildcards e Historial** | [[02.3 - Comodines (Wildcards) e Historial]] | Comodines `*`, `?`, `[]` para seleccionar archivos en masa y trucos del historial |

---

### 🟠 03 - Seguridad, Usuarios, Grupos y Permisos

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 03.1 | **Anatomía de Permisos** | [[03.1 - Anatomía de los Permisos en Linux]] | Los 10 caracteres de `ls -l`, bloques u/g/o y significado de r/w/x |
| 03.2 | **chmod** | [[03.2 - Modificación de Permisos (chmod)]] | Modo simbólico (`u+x`) y modo octal (`755`) para cambiar permisos |
| 03.3 | **UMask y Especiales** | [[03.3 - Seguridad por Defecto (UMask y Permisos Especiales)]] | La máscara UMask, SUID, SGID y Sticky Bit |
| 03.4 | **Usuarios y Grupos** | [[03.4 - Administración de Usuarios, Grupos y Propiedades]] | `/etc/passwd`, `su`, `sudo`, `chown`, `adduser` y gestión de cuentas |

---

### 🟣 04 - Flujo de Datos, Redes y Procesos

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 04.1 | **Pipes y Filtros** | [[04.1 - Redirecciones, Pipes y Filtros de Texto]] | stdin/stdout, `>`, `>>`, `\|`, `grep`, `wc`, `sort`, `head`, `tail -f` |
| 04.2 | **Redes** | [[04.2 - Configuración de Redes en Linux]] | `ifconfig`, `ip a`, `ping`, `wget`, `curl`, NAT vs Bridged |
| 04.3 | **Procesos** | [[04.3 - Gestión de Procesos, Señales y Control de Trabajos]] | PID, `ps`, `top`, `htop`, `kill`, señales, `jobs`, `fg`, `bg` y shutdown |

---

### 🔴 05 - Automatización y Scripting en Bash

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 05.1 | **Estructura de Scripts** | [[05.1 - Estructura Básica de un Script en Bash]] | Shebang `#!/bin/bash`, variables, `export` y `.bashrc` |
| 05.2 | **Entrada de Datos** | [[05.2 - Lectura de Datos y Argumentos de Script]] | `read`, parámetros posicionales `$1`-`$9`, `$#`, `$@` |
| 05.3 | **Condicionales** | [[05.3 - Operaciones Aritméticas y Estructuras Condicionales]] | `if/elif/else`, operadores de comparación, `case/esac` |
| 05.4 | **Bucles** | [[05.4 - Bucles y Control de Iteraciones]] | `for`, `while`, `until`, `continue` y `break` |
| 05.5 | **Funciones** | [[05.5 - Funciones y Manejo de Errores]] | Definir funciones, `local`, `exit`, `$?`, `&&` y `\|\|` |
| 05.6 | **Cron** | [[05.6 - Programación de Tareas con Cron (Crontab)]] | Tareas programadas con los 5 campos de cron y `crontab` |

---

### 🟤 06 - Terminales Modernas y Entornos de Trabajo

| # | Tema | Nota | Descripción |
|---|------|------|-------------|
| 06.1 | **Warp Terminal** | [[06.1 - Warp Terminal - Entorno Integrado con IA]] | Terminal moderna con IA integrada, bloques, workflows y modo agente |
| 06.2 | **ZSH y Oh My ZSH** | [[06.2 - Transición a ZSH y Oh My ZSH]] | Migración de Bash a ZSH, autocompletados, temas y plugins |

---

## 🗺️ Diagrama de Aprendizaje

```
 FUNDAMENTOS
 ┌─────────────────────────────────────────────┐
 │ Qué es Linux ──► Árbol de Directorios ──► Rutas │
 └───────────────────────┬─────────────────────┘
                         │
                         ▼
 COMANDOS BÁSICOS
 ┌─────────────────────────────────────────────┐
 │ Orientación ──► Manipulación ──► Wildcards     │
 └───────────────────────┬─────────────────────┘
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
 SEGURIDAD          FLUJO DATOS     REDES
 ┌──────────┐    ┌──────────┐    ┌──────────┐
 │ Permisos │    │ Pipes    │    │ ifconfig │
 │ chmod    │    │ grep     │    │ ping     │
 │ UMask    │    │ Filtros  │    │ curl     │
 │ Usuarios │    │ Procesos │    │ wget     │
 └────┬─────┘    └────┬─────┘    └────┬─────┘
      └───────────────┼───────────────┘
                      ▼
 SCRIPTING BASH
 ┌─────────────────────────────────────────────┐
 │ Scripts ──► read ──► if/case ──► Bucles       │
 │    ──► Funciones ──► Cron                     │
 └───────────────────────┬─────────────────────┘
                         ▼
 TERMINALES MODERNAS
 ┌─────────────────────────────────────────────┐
 │ Warp Terminal ──► ZSH + Oh My ZSH             │
 └─────────────────────────────────────────────┘
```

---

> [!tip] 🧭 ¿Cómo usar esta guía?
>
> - Si eres **principiante total**: Sigue el orden numérico (01 → 06). Cada nota enlaza a la siguiente.
>
> - Si ya conoces Linux y quieres **profundizar**: Salta directo a la sección que necesites usando la tabla de arriba.
>
> - Si buscas una **referencia rápida de comandos**: Consulta [[02.1 - Orientación, Inspección y Ayuda]] y [[02.2 - Manipulación de Archivos y Carpetas]].
>
> - Si quieres aprender **Bash scripting**: Ve directo a la carpeta 05, empezando por [[05.1 - Estructura Básica de un Script en Bash]].
>
> - Si quieres montar un **entorno moderno de terminal**: Consulta [[06.1 - Warp Terminal - Entorno Integrado con IA]] y [[06.2 - Transición a ZSH y Oh My ZSH]].
