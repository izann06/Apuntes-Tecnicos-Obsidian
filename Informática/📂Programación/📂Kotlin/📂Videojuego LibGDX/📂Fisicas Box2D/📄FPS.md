![[FPS.png]]

Si un frame tarda más de lo normal (lag, carga del sistema), `delta` varía. Si Box2D recibe pasos de tiempo irregulares, la simulación se vuelve inestable: objetos que atraviesan paredes, rebotes raros, etc. La solución es el `accumulator`: acumulas el tiempo real transcurrido y lo consumes en trozos fijos de `1/60s` si son 60 FPS. 

**Delta compensa exactamente la diferencia de velocidad dependiendo de los FPS que tenga**.

Piénsalo así. Tienes un personaje que quieres que se mueva a 5 unidades por segundo.

A 60 FPS, `render()` se llama 60 veces en un segundo. Cada vez, `delta = 1/60 = 0.0167s`. Haces `5 × 0.0167 = 0.083` unidades ese frame. 
Al cabo de 60 frames: `0.083 × 60 = 5` unidades. ✅

A 30 FPS, `render()` se llama solo 30 veces en un segundo. Pero cada frame dura el doble, así que `delta = 1/30 = 0.033s`. Haces `5 × 0.033 = 0.166` unidades ese frame. Cada paso es más grande, pero hay la mitad de pasos.
Al cabo de 30 frames: `0.166 × 30 = 5` unidades. ✅

**Delta es pequeño cuando hay muchos frames, y grande cuando hay pocos.** Se compensan exactamente. No es magia, es simplemente que delta mide tiempo real transcurrido, y en un segundo siempre pasa un segundo.

**Por qué Box2D no puede usar delta directamente**

Ya entiendes que delta varía. El problema es que Box2D no es un simple `posicion += velocidad * delta`. Por dentro hace cálculos complejos de colisiones, fuerzas, rozamientos y restricciones entre cuerpos. Si le metes un delta grande porque hubo un frame lento, puede pasar esto:


![[FPS-1.png]]![[FPS-2.png]]

Esto se llama **tunneling**: el objeto va tan rápido en ese paso que Box2D lo calcula directamente al otro lado de la pared, sin haber pasado por ella. Resultado: bala que atraviesa paredes, personaje que cae a través del suelo en momentos de lag.

La solución es el **accumulator**.


```kotlin
accumulator += delta.coerceAtMost(0.25f) // acumulas tiempo real
while (accumulator >= TIME_STEP) { // mientras haya tiempo pendiente
 world.step(TIME_STEP, 6, 2) // avanzas en trozos exactos de 1/60s
 accumulator -= TIME_STEP // descontamos ese trozo
}
```

Si hubo un frame lento con `delta = 0.05s`, el bucle simplemente corre **tres veces** con `TIME_STEP = 0.0167s` en lugar de una. Box2D siempre recibe pasos pequeños y controlados. El `coerceAtMost(0.25f)` es un tope de seguridad: si el juego se congela varios segundos (alt-tab, carga pesada), no dejas que el accumulator acumule 3 segundos de física y los ejecute todos de golpe.