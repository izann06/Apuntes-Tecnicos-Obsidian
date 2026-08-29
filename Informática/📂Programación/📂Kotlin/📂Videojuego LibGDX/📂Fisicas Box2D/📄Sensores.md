- Un **Cuerpo normal** (como el suelo) es un muro de ladrillos. Si corres hacia él, te chocas y te paras.
 
- Un **Sensor** (como una moneda) es un láser de seguridad. Si corres hacia él, lo atraviesas como si nada, pero hace saltar una alarma.
 
- El **ContactListener** es el guardia de seguridad que está mirando las cámaras. Cuando ve que cruzas el láser, avisa por el walkie-talkie.
 

Vamos a ver cómo se escribe esto en código paso a paso, usando monedas de ejemplo.

---

### Paso 1: Ponerle el "láser" a la moneda

Cuando creamos la moneda en `Moneda.kt`, le decimos a Box2D dos cosas vitales: _"Eres un fantasma (sensor)"_ y _"Te llamas 'moneda' (userData)"_.

```Kotlin
val body: Body = world.body {
 // 1. Posición de la moneda
 position.set(x, y) 
 
 // 2. Le damos forma de círculo
 circle(radius = 0.3f) {
 isSensor = true // <--- ¡MAGIA! Esto hace que el jugador la atraviese.
 userData = "moneda" // <--- Le ponemos una etiqueta con su nombre.
 }
}
```

Al mismo tiempo, el jugador también tiene su propia etiqueta: `userData = "jugador"`.

---

### Paso 2: El guardia de seguridad (`ContactListener`)

En el archivo `WorldManager.kt`, creamos al guardia. Su trabajo es estar callado hasta que dos cosas se tocan. Cuando se tocan, se ejecuta automáticamente el método `beginContact`.

```Kotlin
override fun beginContact(contact: Contact) {
 // El guardia mira las etiquetas de las dos cosas que han chocado
 val etiquetaA = contact.fixtureA.userData as? String
 val etiquetaB = contact.fixtureB.userData as? String

 // El guardia se pregunta: "¿Ha chocado el jugador con una moneda?"
 // (Box2D no sabe quién es A y quién es B, así que comprobamos las dos opciones)
 
 val chocaJugador = (etiquetaA == "jugador" && etiquetaB == "moneda")
 val chocaAlReves = (etiquetaB == "jugador" && etiquetaA == "moneda")

 if (chocaJugador || chocaAlReves) {
 // ¡BINGO! El jugador ha tocado una moneda.
 
 // Ahora tenemos que averiguar cuál de los dos es el cuerpo de la moneda
 // para apuntarlo en una lista de "monedas a destruir".
 val cuerpoMoneda = if (etiquetaA == "moneda") contact.fixtureA.body else contact.fixtureB.body
 
 monedasARecoger.add(cuerpoMoneda) 
 }
}
```

---

### Paso 3: ¡La Regla de Oro de Box2D! (Por qué usamos una lista)

Te habrás fijado en que el código de arriba **no destruye la moneda directamente**, sino que la guarda en una lista llamada `monedasARecoger`.

> [!ATTENTION] Las monedas recogidas se guardan en una lista.
¿Por qué? Porque Box2D es muy estricto. Cuando se ejecuta el `ContactListener`, Box2D está en medio de cálculos matemáticos súper complejos. Es como si un contable estuviera en mitad de una multiplicación larguísima. Si en ese milisegundo borras un objeto del mundo (la moneda), el contable se vuelve loco y **el juego se cierra (Crash)**.

Por eso, el guardia (`ContactListener`) solo apunta en una libreta: _"Oye, cuando termines de hacer los cálculos matemáticos, acuérdate de borrar esta moneda"_.

Luego, en `GameScreen.kt` (fuera de la física), el juego lee esa libreta, borra la moneda visualmente, suma los puntos y reproduce el sonido:

```Kotlin
// En GameScreen.kt, después de que la física haya terminado:
val recogidas = worldManager.monedasARecoger.toList()

recogidas.forEach { bodyMoneda ->
 // 1. Destruimos el cuerpo físico
 worldManager.world.destroyBody(bodyMoneda)
 // 2. Sumamos un punto
 game.monedasRecogidas++
 // 3. ¡Din, din! Sonido de moneda
 sfxMoneda.play()
}
// 4. Limpiamos la libreta
worldManager.monedasARecoger.clear()
```