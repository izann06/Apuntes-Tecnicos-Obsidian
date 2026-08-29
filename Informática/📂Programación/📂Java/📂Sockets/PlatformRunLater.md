### 1. La Regla de Oro de JavaFX

En JavaFX existe una norma sagrada: **Solo el hilo principal (el UI Thread) puede tocar los botones, etiquetas o ventanas.**

- El hilo principal **(Main)** es el que pinta la pantalla.
 
- Tu hilo de escucha (`listenerThread`) <- Es un ejemplo.

- Es un hilo secundario que vive en el sótano leyendo datos del cable de red.
 

Si tu hilo del sótano intenta hacer un `lblStatus.setText()`, JavaFX se asusta y lanza una excepción: `IllegalStateException: Not on FX application thread`. Es como si un electricista intentara operar a un paciente en lugar del cirujano; no es su trabajo y puede romper algo.

---

### 2. ¿Qué hace exactamente `Platform.runLater`?

Cuando ejecutas `Platform.runLater(() ->...)`:

1. El hilo de escucha **no actualiza la interfaz** él mismo.
 
2. En su lugar, crea una **nota adhesiva** con la tarea (por ejemplo: "Actualiza el precio a 50€").
 
3. Pone esa nota en una **cola de tareas** que tiene el hilo principal.
 
4. El hilo principal, en cuanto termina de pintar el siguiente píxel, mira su cola, lee la nota y **él mismo hace el cambio** en la pantalla.
 

---

### 3. Explicación para tus comentarios (Línea por línea)

Aquí tienes cómo explicarlo en tu código:

Java

```java
listenerThread = new Thread(() -> { 
 try { 
 while (true) { 
 //Se queda esperando a que el servidor le conteste 
 GameStatus status = (GameStatus) ois.readObject(); 
 
 //El servidor le contesta,le ha pasado el item,mensaje... 
 //Tiene el estado del juego por lo que se lo paso a actualizarInterfaz para que lo gestione un hilo secundario y como un hilo secundario no puede actualizar la interfaz es por eso que llamo a Platform para decirle al hilo principal que se encargue de ello. 
 Platform.runLater(() -> actualizarInterfaz(status));
```

---

### 4. ¿Por qué es "Later" (Luego)?

Se llama Run Later porque no ocurre en ese microsegundo exacto. El hilo principal puede estar ocupado procesando un clic del ratón o una animación. Tu tarea se ejecutará **lo más pronto posible**, pero siempre respetando el orden de la interfaz.

