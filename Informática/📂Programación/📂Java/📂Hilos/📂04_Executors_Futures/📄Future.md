### El Recibo: `Future`

Aquí es donde la cabeza suele explotar. Si pides un cálculo que tarda 10 segundos... ¿cómo recoges el resultado?

1. Tú envías la tarea (`submit`).
 
2. Como la tarea tarda, Java no te da el resultado inmediatamente (sería imposible).
 
3. Te da un **`Future`** (un "Vale" o "Resguardo").
 
4. Tú sigues haciendo tus cosas.
 
5. Cuando necesitas el resultado, vas con tu resguardo y llamas a **`future.get()`**.
 

**Analogía del Burger King:**

1. Pides tu hamburguesa (Envías `Callable`).
 
2. No te la dan al momento. Te dan un **Ticket con un número** (Te dan un `Future`).
 
3. Tú te vas a la mesa a mirar el móvil (Haces otras cosas en el Main).
 
4. Cuando tienes hambre, miras el ticket (`future.isDone()`) o vas al mostrador a esperar (`future.get()`).
 

**Código Completo (Callable + Future):**



```java
import java.util.concurrent.*;

public class EjemploPizza {
 public static void main(String[] args) {
 
 // 1. EL JEFECILLO (Executor)
 // Contratamos a un camarero (gestor de hilos)
 ExecutorService camarero = Executors.newSingleThreadExecutor();


 // ---------------------------------------------------------
 // PARTE 1: EL CALLABLE (La Tarea)
 // Definimos qué tiene que hacer el cocinero.
 // Fíjate que devuelve un String ("Pizza Margarita").
 // ---------------------------------------------------------
 Callable<String> ordenCocina = () -> {
 System.out.println("(COCINA): Horneando pizza...");
 Thread.sleep(10000); // Simulamos tiempo de horno(10s)
 return "Pizza Margarita Calentita";//Devuelve la pizza
 };


 // ---------------------------------------------------------
 // PARTE 2: EL FUTURE (El Ticket)
 // Le damos la orden al camarero (submit).
 // Él NO nos da la pizza ya. Nos da un 'Future' (el ticket).
 // ---------------------------------------------------------
 System.out.println("CLIENTE: Pido mi pizza.");
 Future<String> ticket = camarero.submit(ordenCocina);

 System.out.println("CLIENTE: Tengo el ticket (Future). Mientras espero, miro el móvil.");
 
 // Aquí el programa principal SIGUE ejecutándose mientras la cocina trabaja.
 try {
 Thread.sleep(1000);
 System.out.println("CLIENTE: Sigo esperando...");
 } catch (InterruptedException e) {}


 // ---------------------------------------------------------
 // PARTE 3: EL MOMENTO DE LA VERDAD (.get)
 // Ahora quiero mi pizza. Llamo a ticket.get()
 // OJO: Si la pizza no está lista, ME BLOQUEO aquí esperando.
 // ---------------------------------------------------------
 try {
 System.out.println("CLIENTE: Voy al mostrador a por la pizza...");
 
 String pizza = ticket.get(); // <--- AQUÍ SE CANJEA EL TICKET
 
 System.out.println("CLIENTE: ¡Ya la tengo! Es una: " + pizza);
 
 } catch (Exception e) {
 e.printStackTrace();
 }

 // Cerramos el chiringuito
 camarero.shutdown();
 }
}
```

---

### 4. Métodos Clave del `Future` (Para el examen)

Imagina que tienes el ticket en la mano (`future`). ¿Qué puedes hacer con él?

1. **`future.get()`**: "Dame la hamburguesa ya".
 
 - Si está lista: Te la da.
 
 - Si no está lista: **Te quedas plantado** en el mostrador esperando (Bloquea el hilo actual).
 
 - Si la cocina se quemó (excepción en el hilo): Te lanza la excepción aquí.
 
2. **`future.isDone()`**: "¿Está lista?".
 
 - Devuelve `true` o `false`. No bloquea. Sirve para preguntar sin quedarte pegado.
 
3. **`future.cancel(true)`**: "Oye, cancela el pedido, ya no lo quiero".
 
 - Intenta detener el hilo si aún está trabajando.