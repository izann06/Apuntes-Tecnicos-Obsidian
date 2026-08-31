**Tags:** #inferencia #temperature #top-p #top-k #max-tokens #ia
 #m3-genai

> [!quote] Concepto
> Los parámetros de inferencia son los **controles** que tienes sobre cómo el LLM genera sus respuestas. Son como los mandos de un estudio de grabación: los mismos músicos (el modelo), pero el sonido final depende de cómo los ajustes.

---

## 🌡️ Temperature — El Control de Creatividad

> [!quote] Definición
> **Temperature** controla la **aleatoriedad** de las respuestas. Modifica la distribución de probabilidades sobre los tokens candidatos antes de muestrear.

Para entenderlo bien vamos con un prompt de ejemplo:

**"El animal de compañía más popular en España es el..."**

La IA calcula las probabilidades matemáticas (Base) de la siguiente palabra:

- "perro" → 60%

- "gato" → 30%

- "pájaro" → 5%

- "hámster" → 3%

- "dragón" → 2%

¿Qué hace **Temperature**? **Deforma (escala) estos porcentajes** antes de elegir:

- **Temperature Baja (ej: 0.1 - Frío):** Aplasta a los débiles y engorda al fuerte. "perro" sube al 99%. La IA casi siempre dirá "perro". Es aburrida pero exacta y determinista.

- **Temperature Alta (ej: 1.5 - Caliente):** Iguala las cosas. "perro" baja al 35%, "gato" 30%, y "dragón" sube al 20%. De repente la IA puede decir "dragón". Es muy creativa pero puede perder el sentido.

### Tabla de Referencia

| Valor | Comportamiento | Casos de Uso Ideales |
| :--- | :--- | :--- |
| **0.0 – 0.1** | Casi determinista. Siempre elige el token más probable | Extracción de datos, clasificación, Q&A factual, código crítico |
| **0.3 – 0.7** | Balance. Respuestas coherentes con algo de variación | Resumen de documentos, redacción corporativa, respuestas de chatbot |
| **0.8 – 1.0** | Creativo. Respuestas variadas e interesantes | Marketing, storytelling, generación de ideas, escritura creativa |
| **> 1.0** | Muy creativo / caótico. Puede perder coherencia | Brainstorming extremo, experimentación artística |

> [!tip] 🔥❄️ Mnemotécnico de Temperature
> **🥶 Frío (T ≈ 0) = Aburrido = Predecible = Factual** 
> **🔥 Caliente (T ≈ 1+) = Creativo = Caótico = Artístico**
>
> Si el examen dice "respuestas consistentes y predecibles" → **Temperature baja** 
> Si dice "respuestas creativas y variadas" → **Temperature alta**

---

## 🎯 Top-P (Nucleus Sampling) — El Portero de Discoteca

> [!quote] Definición
> **Top-P** limita el vocabulario candidato. NO cambia los porcentajes (como hace Temperature), sino que actúa como un límite acumulado dinámico. Corta la lista de palabras cuando la suma de sus probabilidades llega al valor P.

### El Mismo Ejemplo Práctico (Top-P = 0.90)

Volvamos a las probabilidades base de nuestro prompt: "perro" (60%), "gato" (30%), "pájaro" (5%), "hámster" (3%), "dragón" (2%).

Imagina que **Top-P (0.90 o 90%)** es un portero de discoteca que solo deja entrar palabras sumando sus porcentajes hasta llenar el 90% del aforo:

1. Entra "perro" (60%). *Llevamos 60% del aforo.*

2. Entra "gato" (30%). *60% + 30% = 90% del aforo.*

3. **¡LÍMITE ALCANZADO!** El portero cierra la puerta.

- **Resultado:** "pájaro", "hámster" y "dragón" son eliminados por completo (pasan al 0%). 

- La IA ahora **solo puede elegir entre perro o gato**, manteniendo sus porcentajes base (sigue siendo el doble de probable que elija perro). Nunca jamás dirá "dragón", asegurando que la frase mantenga el sentido lógico.

### Top-P vs Temperature — Diferencia Conceptual

| | **Temperature** | **Top-P** |
| :--- | :--- | :--- |
| **¿Qué hace?** | Cambia (deforma) las probabilidades de todas las palabras. | Corta (elimina) las palabras raras de la lista. |
| **Objetivo** | Controlar la "locura/creatividad". | Mantener la coherencia quitando opciones sin sentido. |
| **Recomendación AWS** | Ajusta uno u otro, no ambos | Ajusta uno u otro, no ambos |

> [!warning] Temperature y Top-P — No los uses en extremos opuestos simultáneamente
> Si pones Temperature muy alta Y Top-P muy alto al mismo tiempo, obtendrás respuestas completamente incoherentes. Para la mayoría de los casos, ajusta **uno y deja el otro en su valor por defecto**.

---

## 🔢 Top-K — El Control de Vocabulario Fijo

> [!quote] Definición
> **Top-K** limita el vocabulario candidato a los **K tokens más probables** de forma fija, independientemente de sus probabilidades relativas.

### Top-K vs Top-P

```
Ejemplo con los 5 tokens más probables:
"Madrid" → 50%
"Barcelona" → 20%
"Sevilla" → 10%
"Valencia" → 10%
"Bilbao" → 3%

Top-K = 3: considera siempre {Madrid, Barcelona, Sevilla} (los 3 más probables)

Top-P = 0.90: considera {Madrid, Barcelona, Sevilla, Valencia} (los que suman ≥ 90%)
```

| Parámetro | Tipo de límite | Comportamiento |
| :--- | :--- | :--- |
| **Top-K = 1** | Fijo: 1 candidato | Greedy decoding → completamente determinista |
| **Top-K = 50** | Fijo: 50 candidatos | Diversidad moderada |
| **Top-P = 0.9** | Dinámico: varía cada paso | Se adapta a la confianza del modelo |

---

## 📏 Max Tokens — El Límite de Longitud

> [!quote] Definición
> **Max Tokens** (también llamado **Max New Tokens** o **Max Length**) establece el número máximo de tokens que el modelo puede generar en su respuesta.

### Comportamiento

- Si el modelo completa su respuesta **antes** de llegar al límite → para naturalmente.

- Si el modelo llegaría al límite **antes** de terminar → la respuesta se corta abruptamente.

- El coste de salida está directamente relacionado con los tokens generados.

> [!warning] Max Tokens ≠ Context Window
> | | **Max Tokens** | **Context Window** |
> | :--- | :--- | :--- |
> | **Qué limita** | Los tokens de la **respuesta** | Total de tokens procesados (prompt + historial + respuesta) |
> | **Lo controla** | El desarrollador (parámetro de la API) | El modelo (límite fijo de arquitectura) |
> | **Ejemplo** | `max_tokens=500` → respuesta máx 500 tokens | Claude 3.5 Sonnet: 200K tokens en total |

---

## 🛑 Stop Sequences — La Señal de "Para"

> [!quote] Definición
> Las **Stop Sequences** son cadenas de texto que, cuando aparecen en la respuesta generada, detienen inmediatamente la generación del modelo.

### Casos de Uso

```python
# Ejemplo 1: Generar solo hasta la primera pregunta en un cuestionario
stop_sequences=["2."] # Para cuando empieza la segunda pregunta

# Ejemplo 2: Diálogo — evitar que el modelo adopte el rol del humano
stop_sequences=["Usuario:", "Human:", "User:"]

# Ejemplo 3: JSON estructurado — parar al cerrar el objeto
stop_sequences=["}"]

# Ejemplo 4: Código — parar al final de la función
stop_sequences=["```"]
```

> [!example] Caso de uso real en Bedrock
> Estás construyendo un generador de preguntas de examen. Quieres una pregunta por llamada. Configuras:
> ```json
> {
> "stop_sequences": ["2.", "Pregunta 2"]
> }
> ```
> El modelo genera la pregunta 1 y para exactamente cuando va a empezar la 2.

---

## 📊 Tabla Resumen de Todos los Parámetros

| Parámetro | Rango típico | ↑ Subir efecto | ↓ Bajar efecto | Para qué usarlo |
| :--- | :--- | :--- | :--- | :--- |
| **Temperature** | 0.0 – 2.0 | Más creativo / aleatorio | Más determinista / predecible | Creatividad vs consistencia |
| **Top-P** | 0.0 – 1.0 | Más vocabulario disponible | Menos vocabulario (más conservador) | Control fino del vocabulario |
| **Top-K** | 1 – 500 | Más diversidad | Más determinista | Control fijo del vocabulario |
| **Max Tokens** | 1 – 4096+ | Respuestas más largas | Respuestas más cortas | Controlar longitud y coste |
| **Stop Sequences** | N/A | N/A | N/A | Controlar punto de parada |

---

## 🎯 Escenarios de Examen — Elige el Parámetro

> [!example] Escenario A
> *"Quieres que tu chatbot de atención al cliente dé siempre exactamente la misma respuesta a preguntas sobre horarios y políticas de devolución."*
> → **Temperature = 0** (o muy baja, ej. 0.1). Respuestas deterministas y factuales.

> [!example] Escenario B
> *"Estás construyendo un generador de slóganes de marketing y quieres respuestas sorprendentes y originales."*
> → **Temperature alta** (0.8-1.0). Máxima creatividad y variedad.

> [!example] Escenario C
> *"Quieres que el modelo genere exactamente un párrafo de resumen, no más."*
> → **Max Tokens** apropiado (ej. 150) + **Stop Sequences** con el delimitador de párrafo si procede.

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
