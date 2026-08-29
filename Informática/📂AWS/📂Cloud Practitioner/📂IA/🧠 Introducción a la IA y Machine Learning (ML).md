
**Tags:** #aws #ia #machine-learning #sagemaker #inferencia #cloud-practitioner #cp-ia

> [!summary] El Concepto Clave
> La Inteligencia Artificial (IA) es el concepto amplio de hacer que las máquinas imiten el comportamiento humano. El Machine Learning (ML) es el *motor* que hace esto posible: en lugar de darle a la máquina reglas estrictas, le damos miles de datos para que ella misma descubra los patrones ocultos.

---

## 🤖 1. La Jerarquía: IA vs. ML

Es muy común confundir estos términos, pero en el examen debes diferenciarlos:

* **Inteligencia Artificial (IA):** Es el campo general. Cualquier sistema capaz de realizar tareas que normalmente requieren inteligencia humana (entender texto, hablar, reconocer una cara).

* **Machine Learning (ML):** Es un *subconjunto* de la IA. Es la técnica específica de entrenar a una máquina para que aprenda a hacer algo **sin darle instrucciones explícitas**.

---

## ☕ 2. Programación Clásica vs. Machine Learning

Para entender el ML, mira cómo ha cambiado la forma de programar con el ejemplo de la cafetería:

* **Programación Clásica (Reglas Estrictas):** Un programador humano escribe: *"SI el cliente compra un Latte de Caramelo, ENTONCES ofrécele un Pan de Queso"*. Es rígido y no se adapta a los gustos individuales.

* **Machine Learning (Patrones Flexibles):** Le das al sistema el historial de 1 millón de ventas de la cafetería. El sistema descubre por sí solo que a los clientes que compran Lattes los martes por la mañana les gustan las galletas, pero a los de la tarde les gusta el pan de queso. Se adapta de forma dinámica y personalizada.

---

## 🔄 3. El Ciclo de Vida del Machine Learning

Todo proyecto de ML tiene dos fases principales que nunca debes confundir:

1. **Entrenamiento (Training):** Es la fase de estudio. Le das a la máquina toneladas de **datos históricos** limpios. La máquina analiza estos datos buscando patrones ocultos.

 * *El Resultado:* El producto final del entrenamiento se llama **Modelo de Machine Learning**.
 
2. **Inferencia (Inference):** Es la fase de "examen" o puesta en producción. Coges ese Modelo que ya ha estudiado y le presentas **datos nuevos** que nunca ha visto para que haga una predicción o tome una decisión.

---

## 🛠️ 4. Servicios de AWS para IA/ML

En AWS, tienes dos caminos principales dependiendo de tu nivel de experiencia:

* **El Camino del Creador (Amazon SageMaker):** Es el servicio principal de ML en AWS. Permite a los científicos de datos construir, entrenar y desplegar sus propios modelos personalizados desde cero.

* **El Camino Rápido (Servicios de IA Pre-entrenados):** Si no sabes nada de Machine Learning, AWS ya ha entrenado modelos por ti. Solo tienes que usarlos a través de una API. *(Ejemplos: reconocimiento de voz, traducción de textos, lectura de documentos, motores de recomendación).*

> [!warning] La Regla de Oro del ML: "Basura entra, basura sale"
> Un modelo de Machine Learning es tan bueno como los datos con los que fue entrenado. Si le das a la máquina datos sucios, desordenados o incorrectos, sus predicciones (inferencia) serán un desastre. La preparación y limpieza de datos es el paso más crítico.

---

---
→ Volver al índice: [[📂IA/00 - Índice IA|🪐 IA]]
