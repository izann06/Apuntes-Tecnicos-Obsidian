### 1. El Jefe: `ExecutorService` (El ThreadPool)

**El problema de la forma antigua:**

Si tienes que enviar 10.000 emails, hacer `new Thread()` 10.000 veces revienta el ordenador (mucha memoria, mucho tiempo creando y destruyendo hilos).

**La solución (`ThreadPool`):**

Creas una "piscina" (pool) con, digamos, **5 hilos fijos**.

- Tienes 10.000 tareas.
 
- Los 5 hilos cogen las 5 primeras.
 
- En cuanto uno termina, **NO MUERE**, sino que coge inmediatamente la tarea 6.
 
- Así reciclas los hilos. Es mucho más rápido y seguro.
 

**Código:**


```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class EjemploPool {
 public static void main(String[] args) {
 // 1. CONTRATAMOS LA EMPRESA (Pool de 2 hilos fijos)
 ExecutorService empresa = Executors.newFixedThreadPool(2);

 // 2. MANDAMOS 5 TAREAS (Runnable)
 for (int i = 1; i <= 5; i++) {
 int numeroTarea = i;
 empresa.execute(() -> {
 System.out.println("Hilo " + Thread.currentThread().getName() + 
 " haciendo tarea " + numeroTarea);
 try { Thread.sleep(1000); } catch (Exception e){}
 });
 }

 // 3. ECHAMOS EL CIERRE
 // Si no pones esto, el programa NUNCA termina, 
 // porque la empresa se queda esperando más trabajo eternamente.
 empresa.shutdown(); 
 }
}
```

**Lo que verás:** Solo verás `pool-1-thread-1` y `pool-1-thread-2` turnándose para hacer las 5 tareas. Nunca verás un hilo 3.

---

### 2. `ScheduledExecutorService` (El Programador de Tareas)

Es una versión especial del `Executor` para cosas que pasan **en el futuro** o **repetitivamente**.

Es como poner una alarma.

- **`schedule(tarea, tiempo, unidad)`**: "Haz esto dentro de 5 segundos" (una sola vez).
 
- **`scheduleAtFixedRate(...)`**: "Haz esto cada 10 segundos, pase lo que pase".
 
- **`scheduleWithFixedDelay(...)`**: "Haz esto, y cuando termines, espera 10 segundos y vuelve a hacerlo".
 

**Ejemplo Rápido:**

Cuando pasen 5 segundos mostrará el mensaje de `Bip`.

```java
ScheduledExecutorService reloj = Executors.newScheduledThreadPool(1);

// Tarea: Imprimir "Bip"
Runnable alarma = () -> System.out.println("¡Bip!");

// Ejecutar dentro de 5 segundos
reloj.schedule(alarma, 5, TimeUnit.SECONDS);

reloj.shutdown();
```

---


