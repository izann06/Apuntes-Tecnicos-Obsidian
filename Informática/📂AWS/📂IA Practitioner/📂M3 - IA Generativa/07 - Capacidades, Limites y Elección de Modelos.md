**Tags:** #capacidades #limitaciones #alucinaciones #eleccion-modelos #ia #m3-genai

> [!quote] Contexto
> Conocer las técnicas está muy bien, pero el examen evaluará fuertemente si entiendes **cuándo brilla** la GenAI y **dónde están sus riesgos o fallos estructurales**. Además, debes saber qué factores evaluar para elegir un modelo u otro en un entorno empresarial.

---

## ✨ Capacidades Clave (Dónde Brilla GenAI)

Para justificar el uso de IA Generativa en una empresa, debes apoyarte en estas tres ventajas fundamentales:

1. **Adaptabilidad (El "Chef Profesional"):** Un solo modelo fundacional (FM) puede realizar decenas de tareas diferentes de forma nativa (traducir, resumir, escribir código, clasificar) sin tener que entrenar un modelo por separado para cada caso.
2. **Capacidad de respuesta (Lenguaje Natural):** Interacción fluida mediante lenguaje humano, lo que elimina la necesidad de interfaces complejas (UI/UX) o de aprender lenguajes de consulta (como SQL) para extraer información.
3. **Simplicidad de adopción:** Reduce la barrera de entrada técnica; cualquier empleado de la empresa, independientemente de su perfil técnico, puede aprovechar su potencia.

---

## ⚠️ Limitaciones y Riesgos (Dónde Falla GenAI)

> [!warning] Alucinaciones
> Es el riesgo más crítico. El modelo inventa información falsa o inexistente, pero la redacta con una **seguridad y confianza absolutas**, haciendo que parezca 100% real. 
> 
> > [!abstract] La Analogía del Estudiante
> > Imagina a un estudiante que se presenta a un examen oral sin haber estudiado. El profesor le hace una pregunta y el estudiante improvisa una respuesta con tal elocuencia, vocabulario y convicción que el profesor casi se lo cree. Así alucina un LLM.

Otros riesgos importantes a considerar:

- **No determinismo:** Si le haces exactamente la misma pregunta al modelo dos veces, te dará respuestas ligeramente diferentes. Los modelos de GenAI trabajan con probabilidades estadísticas, no con reglas fijas de programación (salvo que configures la Temperature a 0, y aún así, la arquitectura base sigue siendo estadística).
- **Inexactitud y Desactualización:** Respuestas erróneas si los datos de entrenamiento iniciales tenían errores o si el modelo fue entrenado hace meses y no tiene acceso a internet para validar el presente (se soluciona con RAG).
- **Interpretabilidad Limitada (Caja Negra):** A diferencia de un árbol de decisión clásico, es extremadamente difícil auditar matemáticamente *por qué* un modelo con billones de parámetros tomó una decisión o generó una palabra específica.

---

## ⚖️ Factores de Elección de un Modelo en AWS

Al diseñar soluciones y elegir qué modelo habilitar en Amazon Bedrock, debes evaluar estos 4 factores:

| Factor | Consideración Arquitectónica |
| :--- | :--- |
| **Tipo de modelo** | ¿Necesito generar solo texto (Titan Text, Claude), necesito entender imágenes (Multimodal) o generar imágenes desde cero (Titan Image / Stable Diffusion)? |
| **Rendimiento / Latencia** | Los modelos más grandes (ej. Claude 3 Opus, Llama 3 405B) son mucho más precisos y razonadores, pero son más **lentos** y **costosos**. Para tareas simples (clasificar tickets), un modelo pequeño (Claude 3 Haiku) será más rápido y barato. |
| **Seguridad y Compliance** | Requisitos legales de privacidad y residencia de datos. Sectores como la salud (HIPAA), finanzas o gobierno pueden exigir modelos específicos o instancias privadas. |
| **Costo por Token** | Evaluar cuántos tokens consume la tarea en relación al presupuesto total del proyecto. |

---
→ Volver al índice: [[📂M3 - IA Generativa/00 - Índice Módulo 3|🪐 Módulo 3: IA Generativa]]
