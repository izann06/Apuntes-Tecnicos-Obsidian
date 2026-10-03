#harness/avanzado #opencode/commands #opencode/skills #automatizacion

> [!info] Navegación
> ◀ Anterior: [[02 - Harness Engineering Contexto con AGENTS e Historias de Memoria|Harness Básico]] | Siguiente ▶: [[04 - Metodologia Spec-Driven Development SDD|Spec-Driven Development]]

---

# 03 — Harness Avanzado: Custom Commands y Agent Skills

> [!abstract] 🎯 Idea central del módulo
> Si el harness básico es la **base del agente** (quién es y qué puede hacer), el harness avanzado es la **caja de herramientas** (qué atajos tiene para ser más eficiente). Los Custom Commands y Agent Skills eliminan la fricción en tareas recurrentes.

---

## 3.1 Custom Commands (Comandos Personalizados)

### ¿Qué es un Custom Command?

> [!info] 📖 Definición — Custom Command
> Un **Custom Command** es un **prompt estructurado y reutilizable** que se guarda como archivo y se puede invocar con una sintaxis corta del tipo `/<nombre-del-comando>`.
>
> En lugar de escribir el mismo prompt largo cada vez, lo defines una vez y lo reutilizas indefinidamente.

Piénsalo como crear tus propios **atajos de teclado para prompts complejos**.

---

### Dónde se Guardan

En OpenCode, los custom commands se almacenan como archivos Markdown dentro de:

```
tu-proyecto/
└── .opencode/
    └── commands/
        ├── feature.md      ← /feature
        ├── init.md         ← /init  
        ├── review.md       ← /review
        └── bugfix.md       ← /bugfix
```

Cada archivo `.md` contiene el prompt completo que se enviará al agente cuando invocas el comando.

---

### Anatomía de un Custom Command

```markdown
# /feature — Planificación de Nueva Funcionalidad

## Propósito
Analiza el contexto del proyecto y crea un plan estructurado 
para implementar una nueva feature antes de tocar código.

## Instrucciones para el Agente
1. Lee el fichero AGENTS.md para entender el stack actual
2. Lee MEMORY.md para conocer el estado del proyecto
3. Analiza los archivos relacionados con la feature solicitada
4. **Sin editar ningún fichero todavía**, propón:
   - Una lista de archivos que serán afectados
   - Los cambios concretos necesarios en cada uno
   - Posibles efectos secundarios o riesgos
   - Estimación de complejidad (Baja / Media / Alta)
5. Espera confirmación del usuario antes de proceder

## Formato de Salida
Usa una tabla para el resumen de cambios y listas numeradas para los pasos.
```

**Cómo invocarlo:**
```
/feature Añadir sistema de notificaciones por email
```

---

### Comandos Esenciales para Tener

| Comando | Para Qué Sirve |
|---|---|
| `/feature` | Planificar una nueva funcionalidad antes de codificar |
| `/init` | Generar o actualizar el `AGENTS.md` del proyecto |
| `/review` | Revisar el código de un módulo o PR contra las convenciones |
| `/bugfix` | Analizar un error concreto y proponer solución |
| `/refactor` | Proponer refactorización de un módulo específico |
| `/test` | Generar suite de tests para un archivo o función |
| `/commit` | Generar mensaje de commit convencional basado en los diffs |

> [!tip] 💡 Cuándo crear un nuevo comando
> Si te encuentras escribiendo el mismo tipo de prompt **más de 3 veces**, es el momento de convertirlo en un custom command. El criterio es la recurrencia.

---

## 3.2 Agent Skills (Habilidades de Agente)

### ¿Qué es una Agent Skill?

> [!info] 📖 Definición — Agent Skill
> Una **Agent Skill** es un **paquete modular de instrucciones especializadas** que el agente puede **invocar autónomamente** cuando detecta que una situación lo requiere, sin que el usuario tenga que pedirlo explícitamente.

La diferencia clave con los comandos:

| | Custom Command | Agent Skill |
|---|---|---|
| **¿Quién lo invoca?** | El **usuario** explícitamente con `/comando` | La **IA** automáticamente cuando lo necesita |
| **Propósito** | Automatizar prompts recurrentes del usuario | Dar capacidades especializadas al agente |
| **Ejemplo** | `/review` → "Revisa este código" | Skill de UI: el agente la usa solo cuando genera CSS |

---

### Ejemplos de Agent Skills Útiles

**Skill de Diseño UI:**
```markdown
# Skill: UI Design Standards

Cuando generes cualquier código CSS o componentes de interfaz, aplica siempre:
- Variables CSS custom properties para todos los colores
- Sistema de espaciado en múltiplos de 8px (8, 16, 24, 32...)
- Tipografía: Inter como fuente principal, fallback system-ui
- Modo oscuro por defecto con prefers-color-scheme
- Animaciones: máximo 300ms, easing ease-in-out
- Accesibilidad: siempre añade aria-labels y roles semánticos
```

**Skill de Seguridad:**
```markdown
# Skill: Security Checklist

Cuando implementes cualquier endpoint o función que toque datos de usuario:
- Valida y sanitiza TODOS los inputs antes de procesarlos
- Nunca loguees datos sensibles (emails, contraseñas, tokens)
- Usa prepared statements / ORM queries para prevenir SQL injection
- Verifica autenticación Y autorización, no solo autenticación
```

**Skill de Documentación:**
```markdown
# Skill: Auto-Documentation

Cuando generes una función o clase pública:
- Añade JSDoc/docstring completo con @param, @returns y @example
- Si la función tiene efectos secundarios, documéntalos en @remarks
- Si lanza excepciones, documéntalas con @throws
```

---

### Cómo Integrar Skills en el Proyecto

Las skills se pueden incluir directamente en el `AGENTS.md` o en archivos separados que el `AGENTS.md` referencia:

```markdown
# AGENTS.md

## Skills Activas
- @.opencode/skills/ui-standards.md
- @.opencode/skills/security-checklist.md
- @.opencode/skills/auto-documentation.md
```

> [!tip] 💡 Modularidad es la clave
> Mantén las skills en archivos separados. Así puedes **activar o desactivar** skills según el proyecto. Una skill de React no tiene sentido en un proyecto Python.

---

## 3.3 La Diferencia Real en la Práctica

Imagina que estás construyendo una app y le dices al agente:

> *"Crea un componente de formulario de login"*

**Sin harness avanzado:** El agente genera un formulario genérico, sin seguir tus convenciones, sin tipos TypeScript estrictos, sin aria-labels, con colores hardcodeados.

**Con harness avanzado:**
1. El agente detecta que va a generar UI → activa la **Skill de UI Standards** automáticamente
2. Genera con variables CSS, espaciado de 8px, modo oscuro
3. Detecta que toca datos de usuario → activa la **Skill de Seguridad** automáticamente  
4. Valida y sanitiza los inputs
5. Al crear la función de submit → activa la **Skill de Documentación**
6. Añade JSDoc completo

El resultado es **consistente con tu proyecto** sin que hayas tenido que recordar decirle cada regla.

---

> [!quote] 🌟 Conclusión del Módulo 3
> *Los Custom Commands eliminan la fricción de los prompts repetitivos. Las Agent Skills dan al agente capacidades especializadas que se activan solas. Juntos, convierten al agente en un colaborador que sigue tus estándares sin que tengas que recordárselos cada vez.*

→ Siguiente: [[04 - Metodologia Spec-Driven Development SDD|Módulo 4 → Spec-Driven Development]]
→ Volver al índice: [[00 - MOC Curso Desarrollo con IA|🗺️ MOC del Curso]]
