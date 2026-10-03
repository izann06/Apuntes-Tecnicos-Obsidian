#harness/contexto #agents-md #opencode/modos #memoria-persistente

> [!info] Navegación
> ◀ Anterior: [[01 - El Nuevo Programador y Fundamentos de LLM|El Nuevo Paradigma]] | Siguiente ▶: [[03 - Harness Avanzado Comandos Personales y Agent Skills|Harness Avanzado]]

---

# 02 — Harness Engineering: Contexto con AGENTS.md y Memoria

> [!abstract] 🎯 Idea central del módulo
> Un modelo de IA sin contexto es como contratar a un programador experto que tiene amnesia cada vez que le llamas. El **Harness** (arnés) es el sistema que rodea al modelo y le da memoria, instrucciones y límites para que pueda actuar como un agente autónomo real.

---

## 2.1 ¿Qué es el Harness (Arnés)?

El término **Harness** viene del mundo del motor: el arnés eléctrico de un coche es el sistema de cables, conectores y fundas que dirige la electricidad de forma segura y organizada hacia cada componente.

En el desarrollo con IA:

> [!info] 📖 Definición — Harness
> El **Harness** es el **entorno estructurado que rodea al modelo de IA** y que incluye:
> - Las instrucciones persistentes de cómo debe comportarse (`AGENTS.md`)
> - La memoria del estado actual del proyecto (`MEMORY.md`)
> - Los comandos y skills personalizados disponibles
> - Las reglas y guardarraíles que limitan sus acciones

Sin harness, el modelo trabaja en modo conversacional puro: útil pero frágil. Con harness, el modelo actúa como un **agente disciplinado con memoria y criterio**.

---

### Guardarraíles (Guardrails)

> [!info] 📖 Definición — Guardrails
> Los **Guardrails** son restricciones explícitas que le indicas al modelo para acotar su comportamiento. Son las líneas que **no puede cruzar**.

Ejemplos de guardrails comunes en un proyecto:

- `"Nunca modifiques los archivos de la carpeta /migrations sin confirmación explícita mía"`
- `"Siempre añade tests unitarios cuando implementes una función nueva"`
- `"No instales dependencias externas nuevas sin pedirme permiso"`
- `"El código debe funcionar en Node.js 18+ sin transpilación"`

> [!warning] ⚠️ Sin guardrails, el modelo optimiza para "resolver"
> La IA tiene el incentivo de darte una solución. Si no le dices que no puede tocar la base de datos de producción, puede hacerlo si lo considera "la solución más directa". Los guardrails son tu seguro de vida.

---

## 2.2 Context Engineering: El Fichero `AGENTS.md`

Este es el fichero más importante de todo tu proyecto cuando trabajas con IA. Es el **manual de instrucciones persistente** que el agente lee al inicio de cada sesión.

> [!important] ¿Por qué es tan crítico?
> Los modelos tienen una **ventana de contexto finita**. Cuanto más larga es la conversación, más "olvidan" las instrucciones del inicio. `AGENTS.md` se carga al principio y funciona como ancla permanente de instrucciones.

---

### Estructura Estándar de un `AGENTS.md`

```markdown
# AGENTS.md — Instrucciones del Agente para [Nombre del Proyecto]

## Stack Tecnológico
- Frontend: React 18 + TypeScript 5
- Backend: Node.js 18 + Express
- Base de datos: PostgreSQL 15 con Prisma ORM
- Tests: Vitest + Testing Library

## Estructura de Carpetas
src/
├── components/   # Componentes React reutilizables
├── pages/        # Vistas principales
├── services/     # Lógica de negocio y llamadas a API
├── utils/        # Funciones puras y helpers
└── types/        # Interfaces y tipos TypeScript

## Convenciones de Código
- Usa siempre TypeScript strict mode
- Nombres de funciones en camelCase, componentes en PascalCase
- Exportaciones nombradas (no default exports)
- Documenta con JSDoc toda función pública

## Guardrails — Reglas Innegociables
- NUNCA modifiques archivos en /migrations directamente
- SIEMPRE escribe tests para funciones nuevas
- NO instales dependencias sin pedirme confirmación
- Commits atómicos: un cambio lógico por commit

## Estado Actual del Proyecto
[Ver MEMORY.md para el estado actualizado]
```

---

### Inicialización Automática con `/init`

En OpenCode, el comando `/init` lee automáticamente la estructura de tu proyecto y **genera un borrador de `AGENTS.md`** adaptado a lo que ya existe:

```bash
# Dentro de OpenCode, en tu directorio de proyecto:
/init
```

> [!tip] 💡 Tip práctico
> Usa `/init` como punto de partida y luego **edita manualmente** el fichero generado para añadir tus guardrails específicos. La IA puede ver la estructura de carpetas, pero no sabe tus reglas de negocio.

---

## 2.3 Memoria Persistente: El Fichero `MEMORY.md`

Si `AGENTS.md` es el **manual de instrucciones** (qué soy, qué puedo hacer, cómo trabajo), `MEMORY.md` es el **diario de trabajo** (qué estamos haciendo ahora mismo).

> [!info] 📖 Definición — MEMORY.md
> Archivo que el agente **actualiza** al final de cada sesión con el estado actual del proyecto, las decisiones tomadas y los próximos pasos. Garantiza **continuidad entre sesiones**.

---

### Estructura Estándar de un `MEMORY.md`

```markdown
# MEMORY.md — Estado del Proyecto

## Estado Actual (actualizado: 2026-10-02)
- Feature de autenticación: COMPLETADA ✅
- Módulo de notificaciones: EN PROGRESO 🔄 (50%)
- Tests de integración: PENDIENTE ⏳

## Decisiones Técnicas Tomadas
- Elegimos JWT sobre sesiones por el requisito de API stateless (2026-09-30)
- Descartamos Redis por complejidad de infra en la fase actual (2026-10-01)
- El endpoint /auth/refresh usa rotación de tokens por seguridad (2026-10-02)

## Problemas Conocidos y Workarounds
- El middleware de rate-limiting tiene un bug en tests en paralelo → workaround: tests secuenciales por ahora

## Próximos Pasos (en orden de prioridad)
1. Completar el servicio de envío de emails (EmailService)
2. Escribir tests de integración del módulo de auth
3. Revisar el schema de la DB para la feature de equipos
```

> [!tip] 💡 Actualiza MEMORY.md al final de cada sesión
> Pídele al agente explícitamente: *"Antes de cerrar la sesión, actualiza `MEMORY.md` con lo que hemos hecho hoy y los próximos pasos"*. Esto te costará 30 segundos y te ahorrará 10 minutos de re-contextualización la próxima vez.

---

## 2.4 Modos de Trabajo: Plan vs. Build

Los agentes de código modernos tienen dos modos de operación bien diferenciados:

| Modo | Alias | ¿Qué puede hacer? | ¿Cuándo usarlo? |
|---|---|---|---|
| **Plan** | Análisis / Diseño | Leer ficheros, razonar, proponer soluciones | **Antes** de tocar código. Para entender el problema. |
| **Build** | Execution / Construcción | Editar ficheros, ejecutar comandos, crear archivos | Cuando ya tienes el plan aprobado. |

---

### El Flujo Recomendado

```
1. [PLAN] "Analiza el fichero auth.service.ts y propónme cómo
            añadir soporte para OAuth2 sin romper lo existente"
         ↓
2. [REVISIÓN] Tú lees y apruebas (o corriges) el plan
         ↓
3. [BUILD] "Implementa el plan que acabamos de acordar, paso a paso"
```

> [!warning] ⚠️ El error más común
> Saltar directamente al modo **Build** sin pasar por **Plan**. El modelo empieza a editar archivos con una interpretación que puede ser incorrecta, y deshacerlo es más costoso que haberlo planificado.

---

## 2.5 Proyecto Práctico del Módulo: Diario de Estudio

Para anclar los conceptos de este módulo, el proyecto práctico es una **aplicación web de diario de estudio**, construida guiando al agente con un harness correcto.

### Funcionalidades clave:
- ✅ Registro diario de horas y temas estudiados
- ✅ Persistencia con `localStorage` (sin backend)
- ✅ Cálculo automático de **racha de días consecutivos**
- ✅ Visualización de progreso semanal

### Stack elegido:
- HTML5 semántico + CSS custom properties
- JavaScript ES2022 puro (sin frameworks)
- `localStorage` para persistencia

> [!example] 📝 Así es cómo lo construirías con harness
> 1. Creas `AGENTS.md` con el stack, la estructura de carpetas y los guardrails
> 2. Entras en **modo Plan**: "Diseña la arquitectura de la app de diario de estudio"
> 3. Revisas y ajustas el plan
> 4. Entras en **modo Build**: "Implementa el plan paso a paso"
> 5. Al terminar, pides que actualice `MEMORY.md`

---

> [!quote] 🌟 Conclusión del Módulo 2
> *El harness no es burocracia: es la diferencia entre tener un agente que entiende tu proyecto y uno que improvisa en cada sesión. `AGENTS.md` + `MEMORY.md` son el mínimo viable para trabajar profesionalmente con IA.*

→ Siguiente: [[03 - Harness Avanzado Comandos Personales y Agent Skills|Módulo 3 → Harness Avanzado]]
→ Volver al índice: [[00 - MOC Curso Desarrollo con IA|🗺️ MOC del Curso]]
