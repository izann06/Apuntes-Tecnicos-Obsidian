**Tags:** #slm #edge #foundation-models #ia #m4-bedrock
#m4-bedrock

> [!quote] Concepto fundamental
> No todos los problemas requieren un modelo de 400 mil millones de parámetros ejecutándose en la nube. Los **Small Language Models (SLMs)** son la respuesta para casos de uso donde la velocidad extrema, la privacidad total o la falta de conectividad son críticas.

---

## 📱 Despliegue en Edge (Dispositivos Locales)

En el examen AIF-C01, a menudo se presentan escenarios donde se necesita la **menor latencia posible** o donde el dispositivo **no tiene conexión a internet constante** (ej. un coche autónomo, maquinaria industrial, teléfonos móviles). 

Para estos casos, la solución no es usar un Large Language Model (LLM) en la nube mediante API, sino desplegar un **Small Language Model (SLM)** directamente en el dispositivo (en el "Edge" o borde de la red).

### 🚀 Ventajas de los SLMs en Edge

| Ventaja | Explicación para el examen |
| :--- | :--- |
| **Latencia Mínima** | Al procesar los datos localmente en el dispositivo, no hay viajes de ida y vuelta al servidor (network round-trip), lo que ofrece respuestas casi instantáneas. |
| **Privacidad y Seguridad** | Los datos confidenciales nunca abandonan el dispositivo, ideal para entornos médicos o gubernamentales altamente regulados. |
| **Operación Offline** | Funcionan sin necesidad de conexión a internet o en entornos de red inestables (ej. minería, plataformas petrolíferas). |
| **Bajo Coste de Cómputo** | Al ser modelos pequeños, pueden ejecutarse en hardware limitado (CPUs de móviles o pequeños aceleradores IoT) sin incurrir en costes continuos de API en la nube. |

> [!tip] Identificando Casos de Uso SLM en el Examen
> Si la pregunta menciona "inferencia local", "baja potencia computacional", "sin conexión a internet" o "reducir latencia al extremo en el dispositivo", la respuesta siempre involucrará el despliegue de **modelos más pequeños (SLMs)** en el borde (Edge computing), por ejemplo usando AWS IoT Greengrass o SageMaker Edge Manager.

---
→ Volver al índice: [[📂M4 - Bedrock y Amazon Q/00 - Índice Módulo 4|🪐 Módulo 4: Bedrock y Amazon Q]]
