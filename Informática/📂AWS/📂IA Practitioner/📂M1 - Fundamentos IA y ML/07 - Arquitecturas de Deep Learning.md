#aws #ia-practitioner #aif-c01 #deep-learning #modulo-1

> [!info] Navegación
> ◀ Anterior: [[06 - Cheat Sheet Servicios AWS IA]]

---

# 07 — Las 9 Arquitecturas de Deep Learning (y su peso en el examen AIF-C01)

> **Contexto para el examen (AIF-C01):**
> No necesitas saber programar redes neuronales desde cero ni saber matemáticas complejas. Lo que **SÍ sale en el examen** es que sepas **cuándo usar cada arquitectura** según el tipo de datos (imágenes vs texto) y con qué servicio de AWS se relacionan. 
> - **Prioridad Alta:** Transformers (Generative AI, Bedrock), CNN (Computer Vision, Rekognition) y RNN.
> - **Prioridad Media/Baja:** El resto te pueden salir como respuestas incorrectas para descartar o en preguntas muy básicas de conceptos.

---

## 1️⃣ MLP (Multi-Layer Perceptron)

![[MLP.png|MLP]]

Es la red neuronal "clásica" o feedforward. La información fluye en una sola dirección: entra por un lado, se procesa en el medio (capas ocultas) y sale un resultado. 

> [!tip] Analogía
> Es como un jurado en un tribunal. Entran las pruebas (datos), cada miembro del jurado (neurona) evalúa las pruebas basándose en lo que le dice el compañero anterior, y al final emiten un veredicto (salida).

- **Ejemplo real:** Predecir si un cliente va a cancelar su suscripción a Netflix basándose en un Excel con su edad, horas vistas y tipo de plan.
- **Uso:** Problemas generales de clasificación o regresión con datos tabulares (hojas de cálculo).
- **Examen:** Es la base del Deep Learning, pero raramente será la respuesta a un caso de uso moderno complejo.

## 2️⃣ CNN (Convolutional Neural Network)

![[CNN.png|CNN]]

Las CNN son especialistas en "ver". Utilizan filtros (convoluciones) para escanear una imagen por partes y detectar primero cosas simples (bordes, líneas) y luego cosas complejas (ojos, caras, coches).

> [!tip] Analogía
> Imagina mirar un cuadro enorme a través de un tubo de cartón pequeño. Vas moviendo el tubo escaneando el cuadro poco a poco. Primero te das cuenta de que hay una línea curva, luego ves un color rojo, y al juntar todos esos "mini-escaneos" en tu cabeza, te das cuenta de que es una manzana.

- **Ejemplo real:** El Face ID de tu iPhone para desbloquear la pantalla, o los coches Tesla detectando peatones en la carretera.
- **Uso:** Imágenes y Vídeo (Computer Vision).
- **Examen (⭐ CRÍTICO):** Si la pregunta habla de **analizar imágenes, detectar objetos o usar el servicio Amazon Rekognition**, la respuesta es 100% CNN.

## 3️⃣ RNN (Recurrent Neural Network)

![[RNN.png|RNN]]

Diseñadas para trabajar con secuencias (cosas que van en orden). Tienen "memoria": lo que procesan en el paso 2 depende de lo que vieron en el paso 1.

> [!tip] Analogía
> Es como leer un libro. Para entender la palabra que estás leyendo ahora, necesitas recordar las palabras que acabas de leer en la misma frase. Si lees "El cielo es...", tu memoria te dice que la siguiente palabra probablemente sea "azul".

- **Ejemplo real:** El texto predictivo de tu móvil que te sugiere la siguiente palabra mientras escribes un WhatsApp.
- **Uso:** Texto simple, series de tiempo (bolsa de valores), audio.
- **Examen:** Útil para Procesamiento de Lenguaje Natural (NLP) clásico, aunque hoy en día están siendo reemplazadas por los Transformers.

## 4️⃣ LSTM (Long Short-Term Memory)

![[LSTM.png|LSTM]]

Las RNN tienen un defecto: tienen muy mala memoria a largo plazo (como Dory de Buscando a Nemo). Las LSTM son una evolución que soluciona esto, decidiendo qué información vieja es importante guardar y cuál olvidar.

> [!tip] Analogía
> Imagina leer una novela de 500 páginas. En el capítulo 1 se presenta al asesino. Una RNN se olvidaría de quién es en el capítulo 2. Una LSTM tiene una libreta especial donde anota "El asesino es Juan", y lo recuerda perfectamente cuando llega al final del libro en el capítulo 20.

- **Ejemplo real:** Google Translate al traducir párrafos largos y complejos donde el contexto importa.
- **Uso:** Traducción automática, generación de texto, predicciones del clima complejas.

<br>

## 5️⃣ GRU (Gated Recurrent Unit)

![[GRU.png|GRU]]

Es la hermana pequeña de la LSTM. Hace casi lo mismo (recordar a largo plazo), pero es más simple por dentro.

> [!tip] Analogía
> Si la LSTM es un contable que anota todo en tres libros de registro distintos para no olvidar nada, la GRU es un contable que usa un solo libro de registro muy eficiente. Hace el mismo trabajo pero consume mucha menos energía y tiempo.

- **Ejemplo real:** Sistemas integrados en dispositivos con poca batería (como smartwatches) que necesitan entender comandos de voz.

## 6️⃣ Autoencoders

![[Autoencoders.png|Autoencoders]]

Su objetivo es "comprimir" la información hasta su esencia más básica y luego intentar reconstruirla. Si la reconstruye igual, todo va bien. Si falla, es que el dato original era raro.

> [!tip] Analogía
> Es como el juego del teléfono escacharrado pero dibujando. (1) Te enseño un dibujo complejo de una casa. (2) Tienes que resumirlo en un post-it pequeñito con 3 palabras (Encoder). (3) Le pasas el post-it a tu amigo y él tiene que volver a dibujar la casa exacta (Decoder).

- **Ejemplo real:** Detectar fraudes bancarios. El modelo sabe reconstruir operaciones "normales". Si entra una operación fraudulenta, el modelo se atasca al intentar reconstruirla, y hace saltar la alarma.
- **Uso:** Compresión de imágenes, reducción de ruido (quitar granizo de una foto) y **detección de anomalías**.

## 7️⃣ GAN (Generative Adversarial Networks)

![[GAN.png|GAN]]

Son dos inteligencias artificiales peleando entre sí (compitiendo) para volverse mejores. 

> [!tip] Analogía
> Es el clásico juego del **Falsificador (Generador) y el Policía (Discriminador)**. El falsificador intenta pintar billetes falsos cada vez más perfectos. El policía intenta detectar cuáles son falsos y cuáles verdaderos. Con el tiempo, el falsificador se vuelve tan bueno que pinta billetes (o crea imágenes) indistinguibles de la realidad.

- **Ejemplo real:** Crear caras de personas que no existen (la web *ThisPersonDoesNotExist*), los Deepfakes de famosos, o envejecer tu cara en FaceApp.
- **Uso:** Generación de imágenes hiperrealistas, modificar fotos (Generative AI visual).

## 8️⃣ Transformers

![[Transformers.png|Transformers]]

A diferencia de las RNN que leen palabra por palabra en orden, los Transformers leen toda la frase de golpe y usan un truco llamado **"Atención" (Self-Attention)** para ver qué palabras están conectadas entre sí, sin importar lo lejos que estén en la frase.

> [!tip] Analogía
> Imagina una foto de un partido de fútbol. Una RNN miraría jugador por jugador de izquierda a derecha. Un Transformer mira todo el campo de golpe y traza "líneas rojas" (atención) entre el jugador que tiene el balón y el delantero que está a 50 metros corriendo para desmarcarse, entendiendo el contexto global de la jugada al instante.

- **Ejemplo real:** ChatGPT (la "T" es de Transformer), Claude, Gemini. Son la base absoluta de la revolución actual de la IA.
- **Uso:** Large Language Models (LLMs), Generative AI conversacional.
- **Examen (⭐ CRÍTICO):** Es la arquitectura subyacente de la **IA Generativa**. Cualquier pregunta sobre **Amazon Bedrock, LLMs o Foundation Models** apunta aquí.

## 9️⃣ GNN (Graph Neural Networks)

![[GNN.png|GNN]]

Están diseñadas para procesar datos que no son tablas ni imágenes, sino **redes o mallas** (grafos). Estudian las relaciones entre nodos.

> [!tip] Analogía
> Piensa en LinkedIn o Facebook. Tú (un nodo) estás conectado a tus amigos, y tus amigos están conectados a sus empresas. Una GNN viaja por esas conexiones para descubrir cosas, por ejemplo: "Como 5 de tus amigos trabajan en Google, es muy probable que a ti te interese un anuncio de Google".

- **Ejemplo real:** El algoritmo de recomendación de amigos de Facebook, Google Maps calculando la mejor ruta en una red de calles, o descubrir cómo se pliegan las proteínas en medicina.
- **Uso:** Redes sociales, sistemas de recomendación complejos, mapas, química molecular.
- **Examen:** Relaciónalo siempre con bases de datos de grafos como **Amazon Neptune**.

---

### 🧠 ¿Cómo enfocarlo para el examen?

En un proyecto (y en el examen de AWS), la pregunta clave no es "Voy a usar Deep Learning", sino:
✅ **“¿Qué arquitectura es adecuada para la estructura de mis datos y el objetivo del problema?”**

| Tipo de Dato | Arquitectura Ideal | Servicio AWS Relacionado |
| :--- | :--- | :--- |
| **Imágenes / Visión** | CNN | Amazon Rekognition |
| **Texto / Lenguaje Natural Moderno (GenAI)** | Transformers (LLMs) | Amazon Bedrock, Q |
| **Texto Secuencial / Audio (Clásico)** | RNN / LSTM | Amazon Comprehend, Transcribe |
| **Datos Estructurados (Grafos)** | GNN | Amazon Neptune + ML |
| **Generación de Imágenes** | GANs / Diffusion Models | Amazon Bedrock (Titan Image) |
