#agentes/custom #subagentes #opencode/configuracion #yaml

> [!info] Navegación
> ◀ Anterior: [[04 - Metodologia Spec-Driven Development SDD|SDD]] | Siguiente ▶: [[06 - Sistemas Multiagente Orquestacion y Software Factory|Sistemas Multiagente]]

---

# 05 — Agentes y Subagentes Personalizados en OpenCode

> [!abstract] 🎯 Idea central del módulo
> Hasta ahora tenías **un agente** que lo hace todo. En proyectos complejos, la solución es tener **múltiples agentes especializados**: un equipo donde cada uno tiene su rol, sus herramientas y sus permisos. Aquí aprendes a crearlos y configurarlos.

---

## 5.1 Custom Agents vs Agente General

### ¿Por qué no usar siempre el agente general?

Imagina contratar a un único empleado que tiene que ser a la vez diseñador, programador backend, QA, DevOps y gestor de base de datos. Es posible, pero ineficiente y propenso a errores.

La solución profesional es el **equipo especializado**:

> [!info] 📖 Definición — Custom Agent
> Un **Custom Agent** es una instancia del modelo de IA configurada con:
> - Un **rol específico** y bien definido
> - Un conjunto **restringido de herramientas** y acciones permitidas
> - **Instrucciones propias** distintas al AGENTS.md general
> - **Permisos** ajustados a lo mínimo necesario para su función

> [!info] 📖 Definición — Subagente
> Un **Subagente** es un Custom Agent diseñado para ser **invocado por otro agente** (el primario), no directamente por el usuario. Ejecuta una tarea específica en segundo plano y devuelve el resultado al agente que lo llamó.

---

### La Diferencia en la Práctica

| Aspecto | Agente General | Custom Agent |
|---|---|---|
| **Rol** | Todo a la vez | Especializado (solo QA, solo backend...) |
| **Acceso** | Todos los archivos | Solo los archivos necesarios para su rol |
| **Quién lo invoca** | El usuario | El usuario o otro agente |
| **Instrucciones** | AGENTS.md general | Su propio archivo de configuración |
| **Riesgo** | Alto (puede tocar cualquier cosa) | Bajo (limitado por permisos) |

---

## 5.2 Estructura de Configuración de un Agente

En OpenCode, los agentes personalizados se definen como archivos Markdown con **encabezado YAML** en:

```
tu-proyecto/
└── .opencode/
    └── agents/
        ├── coordinator.md    ← Agente primario coordinador
        ├── planner.md        ← Subagente planificador
        ├── implementer.md    ← Subagente implementador
        └── reviewer.md       ← Subagente revisor de calidad
```

---

### Anatomía de un Archivo de Agente

```yaml
---
name: "Planificador SDD"
description: "Subagente especializado en crear specs, planes y tareas usando metodología SDD y sintaxis EARS"
mode: subagent
permissions:
  - read: ["docs/**", "specs/**", "AGENTS.md"]
  - write: ["specs/**"]
  - execute: []
tools:
  - read_file
  - write_file
  - search_files
---

# Instrucciones del Planificador

Eres un arquitecto de software especializado en convertir 
requisitos en especificaciones formales.

## Tu Rol
Cuando se te invoca, recibes una descripción de una feature 
y DEBES generar la documentación SDD completa:
1. `spec.md` con requisitos en sintaxis EARS
2. `plan.md` con la arquitectura técnica
3. `tasks.md` con la lista de implementación atómica

## Restricciones
- NUNCA escribas código de producción
- NUNCA modifiques archivos fuera de specs/
- SIEMPRE usa sintaxis EARS para los requisitos
- SIEMPRE espera revisión antes de pasar al plan

## Formato de Salida
Sigue estrictamente las plantillas en docs/sdd-templates/
```

---

### Los Campos del Encabezado YAML

| Campo | Descripción | Valores posibles |
|---|---|---|
| `name` | Nombre identificativo del agente | Cualquier string |
| `description` | Para qué sirve (lo usa el orquestador) | String descriptivo |
| `mode` | ¿Es primario o subagente? | `primary` / `subagent` |
| `permissions.read` | Patrones glob de archivos que puede leer | Array de globs |
| `permissions.write` | Patrones glob de archivos que puede escribir | Array de globs |
| `permissions.execute` | Comandos de terminal que puede ejecutar | Array de comandos |
| `tools` | Herramientas disponibles | Lista de herramientas |

---

### Principio de Mínimo Privilegio

> [!warning] ⚠️ Regla de oro de los permisos
> Dale a cada agente **exactamente los permisos que necesita** para su rol y **ni uno más**.
>
> - El agente de QA no necesita escribir en `/src`, solo leer
> - El agente de documentación no necesita ejecutar comandos
> - El agente planificador no necesita tocar el código de producción
>
> Esta práctica evita que un agente con un error o una instrucción ambigua pueda causar daño fuera de su área.

---

## 5.3 Invocación de Subagentes con `@`

La sintaxis `@` es la forma de **delegar tareas a subagentes** sin perder el hilo de la conversación principal.

### Uso Básico

```
# En la conversación con el agente coordinador:
@planner "Crea la spec para el sistema de notificaciones por email"

# El coordinador invoca al subagente 'planner' con esa tarea
# El planner trabaja en segundo plano
# El resultado vuelve al coordinador
```

---

### Casos de Uso del `@`

**Delegación de investigación:**
```
@explore "Analiza la carpeta src/services y dime qué patrones 
          de diseño usa el código existente"
```

**Delegación de revisión:**
```
@reviewer "Revisa el archivo auth.service.ts contra la 
            spec en specs/001-autenticacion/spec.md"
```

**Investigación paralela:**
```
@planner "¿Cómo implementarías la caché de Redis para esta feature?"
@reviewer "¿Qué problemas de seguridad ves en el enfoque actual?"
```

> [!tip] 💡 Cuándo usar `@` vs hablar directamente
> Usa `@subagente` cuando:
> - La tarea es especializada y tiene un agente configurado para ella
> - Quieres que trabaje en segundo plano sin interrumpir el flujo
> - Necesitas resultados de múltiples agentes en paralelo
>
> Habla directamente con el agente coordinador para:
> - Decisiones arquitectónicas
> - Revisión del contexto general
> - Orchestración del flujo de trabajo

---

## 5.4 Ejemplos de Agentes Especializados Completos

### Agente Implementador

```yaml
---
name: "Implementador"
description: "Implementa tareas atómicas del tasks.md siguiendo el plan técnico"
mode: subagent
permissions:
  - read: ["**"]
  - write: ["src/**", "tests/**"]
  - execute: ["node --test", "npm run lint", "npm run typecheck"]
---

# Implementador

Eres un programador senior especializado en implementación precisa.

## Proceso
1. Lee el task.md y encuentra la primera tarea no completada ([ ])
2. Lee el plan.md para entender la arquitectura esperada
3. Lee la spec.md para conocer los criterios de aceptación
4. Implementa SOLO esa tarea, sin tocar nada más
5. Escribe los tests correspondientes
6. Ejecuta `npm run typecheck` y `node --test`
7. Si pasan, marca la tarea como completada ([x]) en tasks.md
8. Informa al coordinador del resultado

## Restricciones
- NUNCA implementes más de una tarea por invocación
- NUNCA modifiques spec.md ni plan.md
- Si los tests no pasan, reporta el error; no intentes arreglar
  algo que no es parte de la tarea actual
```

---

### Agente Revisor de Calidad

```yaml
---
name: "Reviewer QA"
description: "Valida implementaciones contra la spec y la constitución del proyecto"
mode: subagent
permissions:
  - read: ["**"]
  - write: []
  - execute: ["node --test", "npm run lint"]
---

# Reviewer QA

Eres un QA engineer con obsesión por la calidad y la seguridad.

## Proceso de Revisión
Para cada archivo que te pasen, verifica:

1. **Correctitud funcional**: ¿Cumple todos los requisitos EARS de la spec?
2. **Constitución**: ¿Viola algún principio de docs/constitution.md?
3. **Seguridad**: ¿Hay inputs sin validar? ¿Datos sensibles expuestos?
4. **Tests**: ¿Hay cobertura adecuada? ¿Los tests prueban los casos borde?
5. **Legibilidad**: ¿El código es comprensible sin comentarios adicionales?

## Formato de Reporte
Devuelve siempre:
- ✅ Aprobado / ❌ Rechazado / ⚠️ Aprobado con observaciones
- Lista numerada de issues encontrados (vacía si ninguno)
- Sugerencias concretas de mejora para cada issue
```

---

> [!quote] 🌟 Conclusión del Módulo 5
> *Un Custom Agent no es magia: es un archivo de texto con instrucciones y permisos. La potencia viene de la **especialización y los límites**. Un agente que solo puede hacer una cosa la hace muy bien. Un equipo de agentes especializados construye software que ninguno podría hacer solo.*

→ Siguiente: [[06 - Sistemas Multiagente Orquestacion y Software Factory|Módulo 6 → Sistemas Multiagente]]
→ Volver al índice: [[00 - MOC Curso Desarrollo con IA|🗺️ MOC del Curso]]
