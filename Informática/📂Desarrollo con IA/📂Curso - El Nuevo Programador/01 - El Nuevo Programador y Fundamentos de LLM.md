#desarrollo-ia/fundamentos #llm/herramientas #prompting

> [!info] Navegación
> ◀ Índice: [[00 - MOC Curso Desarrollo con IA|🗺️ MOC del Curso]] | Siguiente ▶: [[02 - Harness Engineering Contexto con AGENTS e Historias de Memoria|Harness Básico]]

---

# 01 — El Nuevo Programador y Fundamentos de LLM

> [!abstract] 🎯 Idea central del módulo
> El mercado no necesita a alguien que recuerde la sintaxis de `forEach`. Necesita a alguien capaz de **dirigir un modelo de IA** para que construya software robusto, mantenible y seguro. Ese es el Nuevo Programador.

---

## 1.1 La Evolución del Rol del Desarrollador

El acto de programar ha cambiado más en los últimos 2 años que en los 20 anteriores.

Antes, el flujo era:
1. El programador piensa el problema
2. El programador **escribe** el código a mano
3. El programador lo prueba y depura

Ahora, el flujo es:
1. El programador piensa el problema y **diseña la arquitectura**
2. El programador **dirige a la IA** para que escriba el código
3. El programador **revisa y valida** el resultado

> [!important] 🔑 El cambio clave
> **La IA genera el código, pero el desarrollador garantiza la arquitectura y aporta el criterio.**
>
> La IA es un ejecutor brillante pero sin juicio propio. Tú eres el que sabe qué construir, por qué y con qué restricciones.

---

### El Valor Diferencial del Nuevo Programador

Las habilidades que **aumentan de valor** en la era de la IA:
- 📐 **Diseño de arquitectura** — Decidir cómo se estructura el sistema
- 📋 **Definición de requisitos** — Saber qué problema se quiere resolver realmente
- 🧠 **Context Engineering** — Saber cómo alimentar al modelo con la información correcta
- 🔍 **Revisión técnica** — Detectar errores conceptuales en el código generado
- 🛡️ **Supervisión de calidad** — Asegurarse de que el resultado es seguro y mantenible

Las habilidades que **pierden peso relativo**:
- ❌ Memorizar sintaxis de lenguajes
- ❌ Escribir código boilerplate a mano
- ❌ Recordar nombres exactos de funciones de API

---

## 1.2 Vibe Coding vs. Ingeniería de Software Profesional

> [!warning] ⚠️ La trampa del Vibe Coding
> **Vibe Coding** es el acto de pedirle a la IA que "haga algo" sin un plan, sin especificaciones y sin revisión. Funciona para prototipos de 10 minutos. Falla estrepitosamente en proyectos reales.
>
> **Síntomas del Vibe Coding:**
> - Le pides a la IA que añada una feature y rompe 3 cosas más
> - No sabes exactamente qué hace el código que la IA generó
> - El proyecto crece y nadie puede mantenerlo
> - La IA "alucina" una solución que parece correcta pero tiene bugs ocultos

| | Vibe Coding | Ingeniería con IA |
|---|---|---|
| **Enfoque** | "Hazme esto" | "Aquí el contexto, aquí la spec, aquí las restricciones" |
| **Arquitectura** | Improvisada | Diseñada antes de codificar |
| **Tests** | Ninguno | Definidos en la spec (EARS) |
| **Mantenibilidad** | Caos en semanas | Sostenible con harness |
| **Escala** | Prototipos de un día | Proyectos de producción |

---

## 1.3 Funcionamiento y Selección de LLMs

### El Triángulo Operativo

Todo modelo de lenguaje existe en tensión entre 3 dimensiones:

```
         POTENCIA
           /\
          /  \
         /    \
        /      \
  COSTE ——————— VELOCIDAD
```

- **Alta Potencia** (ej. Claude Opus, GPT-4o, Gemini Ultra): Para arquitectura, razonamiento complejo, decisiones críticas
- **Alta Velocidad** (ej. Claude Haiku, GPT-4o-mini): Para tareas repetitivas, refactorizaciones, comentarios
- **Equilibrio** (ej. Claude Sonnet, GPT-4o estándar): Para el trabajo diario de desarrollo

> [!tip] 💡 Estrategia práctica de selección de modelo
> - **Diseño y arquitectura** → Modelo más potente disponible
> - **Codificación diaria** → Modelo equilibrado (relación calidad/precio)
> - **Tareas mecánicas repetitivas** → Modelo rápido y barato
>
> Cambiar de modelo a mitad de sesión es perfectamente válido según la complejidad de la tarea.

---

### Panorama de Herramientas de Desarrollo con IA

| Herramienta | Tipo | Mejor Para |
|---|---|---|
| **[[📂Desarrollo con IA/📂OpenCode/01 - Introducción a OpenCode\|OpenCode]]** | CLI / Terminal | Control total, agnóstico de IDE, agentic coding |
| **Cursor** | IDE (fork de VS Code) | Integración visual, chat en contexto de ficheros |
| **Claude Code** | CLI oficial de Anthropic | Workflows agénticos profundos con Claude |
| **GitHub Copilot** | Plugin de IDE | Autocompletado en tiempo real |
| **Warp** | Terminal inteligente | Terminal con IA integrada para DevOps |
| **Codex (OpenAI)** | API / CLI | Automatización de tareas vía API |

> [!info] ℹ️ ¿Por qué este curso usa OpenCode?
> OpenCode es **independiente del IDE** y **agnóstico del proveedor de LLM**. Esto significa que lo que aprendes aquí aplica igual si usas Claude, GPT, Gemini o cualquier modelo futuro. Es la herramienta con mayor transferibilidad de conocimiento.

---

## 1.4 Evolución del Prompt Engineering

### La Estructura Clásica (todavía válida)

Un buen prompt siempre necesita:

```
ROL → "Actúas como un senior developer de TypeScript"
CONTEXTO → "Estoy construyendo una API REST para gestión de usuarios"
TAREA EXACTA → "Implementa el endpoint POST /users con validación Zod"
RESTRICCIONES → "Sin dependencias externas más allá de las ya instaladas"
FORMATO → "Devuelve solo el código, sin explicaciones"
```

---

### El Prompt Engineering Moderno: Brain Dump + Síntesis

En sesiones de trabajo real, el enfoque ha evolucionado:

1. **Brain dump por voz o texto libre**: Le "divulgas" al modelo todo el contexto del problema sin estructura, como si hablaras con un compañero: *"Mira, estoy montando una app de tareas, tengo una tabla en Postgres, el usuario tiene que poder crear tareas con fecha límite y quiero que me avise por email cuando falten 24 horas..."*

2. **La IA sintetiza y estructura**: El modelo extrae los requisitos concretos, los organiza y te pregunta por los puntos ambiguos.

3. **Generación estructurada**: A partir de esa síntesis, se genera la spec o el código.

> [!tip] 💡 Por qué funciona el brain dump
> Los modelos modernos son excelentes en la comprensión de lenguaje natural ambiguo. No necesitas ser preciso desde el principio; necesitas ser **completo**. El modelo detecta las lagunas y te las pregunta.

---

> [!quote] 🌟 Conclusión del Módulo 1
> *El nuevo programador no escribe código. El nuevo programador diseña sistemas, define contexto y supervisa a la IA que los construye. La creatividad y el criterio siguen siendo humanos.*

→ Siguiente: [[02 - Harness Engineering Contexto con AGENTS e Historias de Memoria|Módulo 2 → Harness Básico y Gestión de Contexto]]
→ Volver al índice: [[00 - MOC Curso Desarrollo con IA|🗺️ MOC del Curso]]
