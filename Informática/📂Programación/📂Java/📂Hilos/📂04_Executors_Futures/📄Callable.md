
Hasta ahora usábamos `Runnable`.

- **`Runnable` (`void run()`):** "Vete a comprar pan". (El hilo va, lo hace y termina. No te devuelve nada).
 
- **`Callable` (`Object call()`):** "Vete a comprar pan y **tráeme el cambio**". (El hilo va, lo hace y **te devuelve un dato**).
 

**Diferencia clave:** `Callable` puede lanzar Excepciones (throws Exception) y devuelve un resultado.