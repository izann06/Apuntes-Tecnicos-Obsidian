**Tags:** #ml #metricas #precision #recall #f1 #rmse #confusion-matrix #ia
 #m1-fundamentos

> [!quote] Concepto fundamental
> Las métricas son el lenguaje con el que medimos el rendimiento de un modelo. Elegir la métrica incorrecta puede llevarte a confiar en un modelo que en realidad falla cuando más importa.

---

## 🗺️ La Matriz de Confusión — La Base de Todo

Antes de calcular cualquier métrica de clasificación, debes dominar la **Matriz de Confusión**: una tabla que resume todos los aciertos y errores de un clasificador.

### Desglose de las Cuatro Celdas

| Celda | Nombre completo | Qué significa | Consecuencia práctica |
| :---: | :--- | :--- | :--- |
| **TP** | True Positive | Modelo predijo POSITIVO y **era** POSITIVO ✅ | Acierto: detectó el fraude que era fraude |
| **TN** | True Negative | Modelo predijo NEGATIVO y **no era** POSITIVO ✅ | Acierto: la operación legítima no fue bloqueada |
| **FP** | False Positive | Modelo predijo POSITIVO pero **no era** POSITIVO ❌ | Error Tipo I: la tarjeta fue bloqueada sin motivo |
| **FN** | False Negative | Modelo predijo NEGATIVO pero **sí era** POSITIVO ❌ | Error Tipo II: el fraude pasó desapercibido |

> [!tip] Truco mnemotécnico para la matriz
> La primera palabra (True/False) indica **si el modelo acertó**.
> La segunda palabra (Positive/Negative) indica **lo que el modelo predijo**.
>
> - True = Acertó | False = Se equivocó
>
> - Positive = Dijo SÍ | Negative = Dijo NO

---

## 📊 Las Cinco Métricas Clave

### 1️⃣ Accuracy (Exactitud)

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

**¿Qué mide?** El porcentaje de predicciones correctas (aciertos totales / total de predicciones).

> [!warning] ⚠️ La trampa del Accuracy — Muy habitual en el examen
> El Accuracy es **engañoso con datasets desbalanceados**. 
> 
> **Ejemplo:** Si el 99% de los correos son legítimos, un modelo que clasifique TODO como "no spam" tendría **99% de Accuracy** y sería completamente inútil (nunca detecta spam).
> 
> → Cuando el dataset está desbalanceado, usa **F1-Score** en su lugar.

---

### 2️⃣ Precision (Precisión)

$$\text{Precision} = \frac{TP}{TP + FP}$$

**¿Qué mide?** De todo lo que el modelo **predijo como positivo**, ¿qué porcentaje **realmente lo era**? Mide la **calidad de las alarmas**: cuántas falsas alarmas genera el modelo.

**Pregunta que responde:** "Cuando el modelo dice SÍ, ¿con qué frecuencia tiene razón?"

> [!tip] 🧠 Regla mnemotécnica — ¿Cuándo priorizar PRECISION?
> Usa **Precision** cuando los **Falsos Positivos (FP)** son muy costosos.
> 
> **FP = Alarma falsa = Incordio o daño sin necesidad**
> 
> | Escenario | Por qué queremos alta Precision |
> | :--- | :--- |
> | 🛡️ Filtro de SPAM | Un FP = email legítimo importante marcado como spam → el usuario pierde un correo relevante |
> | 💊 Ensayo clínico | Un FP = declarar eficaz un medicamento inútil → pacientes toman medicamento que no funciona |
> | ⚖️ Sistema judicial predictivo | Un FP = condenar a un inocente → injusticia grave |

---

### 3️⃣ Recall (Sensibilidad / Exhaustividad)

$$\text{Recall} = \frac{TP}{TP + FN}$$

**¿Qué mide?** De todos los casos que **realmente eran positivos**, ¿cuántos **capturó** el modelo? Mide la **cobertura**: cuántos casos positivos se pierden.

**Pregunta que responde:** "De todos los que SÍ eran positivos, ¿cuántos encontró el modelo?"

> [!tip] 🧠 Regla mnemotécnica — ¿Cuándo priorizar RECALL?
> Usa **Recall** cuando los **Falsos Negativos (FN)** son muy costosos.
> 
> **FN = Perderse un positivo = Consecuencia grave al no detectar**
> 
> | Escenario | Por qué queremos alto Recall |
> | :--- | :--- |
> | 🏥 Diagnóstico de cáncer | Un FN = decirle a un enfermo que está sano → no recibe tratamiento, puede morir |
> | 🔒 Detección de fraude grave | Un FN = dejar pasar una transacción fraudulenta millonaria |
> | ☢️ Detección de virus/malware | Un FN = un malware crítico no es detectado → brecha de seguridad |

---

### Precision vs Recall — El Trade-off Fundamental

> [!warning] ⚖️ El dilema clásico: no puedes maximizar los dos a la vez
> Precision y Recall son **antagónicos**. Si haces el modelo más conservador (que solo diga SÍ cuando está muy seguro), sube la Precision pero baja el Recall. Si lo haces más agresivo (que diga SÍ ante cualquier sospecha), sube el Recall pero baja la Precision.
> 
> ```
> ← Más conservador Más agresivo →
> Alta Precision Alto Recall
> Menos falsas alarmas Menos positivos perdidos
> (pocos FP) (pocos FN)
> ```

---

### 4️⃣ F1-Score

$$\text{F1} = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

**¿Qué mide?** La **media armónica** entre Precision y Recall. Es alta solo cuando **ambas** métricas son altas simultáneamente.

**¿Por qué media armónica y no media aritmética?** La media armónica penaliza más los valores extremos. Si Precision = 1.0 y Recall = 0.0, la media aritmética sería 0.5 (parece aceptable), pero la media armónica (F1) sería 0 (revela que el modelo es inútil).

> [!tip] ¿Cuándo usar F1-Score?
>
> - Cuando **tanto FP como FN** son igualmente costosos (quieres equilibrio)
>
> - Cuando el dataset está **desbalanceado** y el Accuracy es engañoso
>
> - Es la métrica "por defecto" para clasificación con clases desiguales

---

### 5️⃣ RMSE (Root Mean Square Error)

$$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

**¿Qué mide?** El error promedio de predicción en **problemas de Regresión** (salida numérica continua). Está expresado en las **mismas unidades** que la variable objetivo.

**Características clave:**

- Penaliza los **errores grandes** más que los pequeños (por el cuadrado)

- Es sensible a **outliers**

- Un RMSE de 0 sería predicción perfecta

> [!example] Interpretando el RMSE
> Si predices precios de casas en euros y obtienes RMSE = 15,000€, significa que en promedio tus predicciones se desvían ~15,000€ del precio real.
> 
> Si hay una sola casa que el modelo predice con $200,000€ de error, el RMSE subirá drásticamente por ese único outlier.

---

## 📋 Tabla Resumen Final — Guía Rápida de Métricas

| Métrica | Fórmula | Tipo de problema | Cuándo es la mejor opción |
| :--- | :--- | :--- | :--- |
| **Accuracy** | `(TP+TN) / Total` | Clasificación | Dataset **balanceado** |
| **Precision** | `TP / (TP+FP)` | Clasificación | Minimizar **Falsos Positivos** (SPAM, medicamentos) |
| **Recall** | `TP / (TP+FN)` | Clasificación | Minimizar **Falsos Negativos** (cáncer, fraude) |
| **F1-Score** | `2×(P×R)/(P+R)` | Clasificación | Dataset **desbalanceado**, balance P/R |
| **RMSE** | `√(media de errores²)` | **Regresión** | Predecir **valores numéricos** continuos |

---

## 🎯 Escenarios de Examen — Elige la Métrica Correcta

> [!example] Escenario A
> *"Un sistema detecta si los rayos X muestran neumonía. Es más grave pasar por alto un enfermo que dar una falsa alarma."*
> → Prioriza **Recall** (el FN —decir sano a un enfermo— es el peor error)

> [!example] Escenario B
> *"Un sistema clasifica correos como spam para ocultarlos automáticamente. El usuario nunca ve esos correos."*
> → Prioriza **Precision** (el FP —ocultar un correo importante— es el peor error)

> [!example] Escenario C
> *"El dataset tiene 95% de transacciones normales y 5% de fraude. ¿Qué métrica usas para evaluar el modelo?"*
> → **F1-Score** (dataset desbalanceado; el Accuracy sería engañoso)

> [!example] Escenario D
> *"Quieres medir qué tan bien predice Amazon Forecast las ventas de mañana."*
> → **RMSE** (predicción numérica continua = problema de regresión)

---
→ Volver al índice: [[📂M1 - Fundamentos IA y ML/00 - Índice Módulo 1|🪐 Módulo 1: Fundamentos IA y ML]]
