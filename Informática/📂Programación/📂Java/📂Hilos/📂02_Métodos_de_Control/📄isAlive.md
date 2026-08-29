* Devuelve `true` si el hilo está en marcha,si está vivo como dice el método.

* Si no está activo, ha acabado... estará en `false`.
```java

public class PruebaVidaMuerte {
 public static void main(String[] args) throws InterruptedException {
 
 // 1. CREAMOS EL HILO
 Thread trabajador = new Thread(() -> {
 try {
 // Simulamos que trabaja durante 2 segundos
 Thread.sleep(2000); 
 System.out.println("(Trabajador): ¡Terminé mi turno!");
 } catch (InterruptedException e) {}
 });

 // MOMENTO 1: Antes del start()
 System.out.println("¿Está vivo?: " + trabajador.isAlive()); // FALSE

 //ARRANCAMOS EL HILO
 trabajador.start();
 
 // MOMENTO 2: Justo después de arrancar
 // Ahora sí está corriendo.
 System.out.println("¿Está vivo?: " + trabajador.isAlive()); // TRUE
 }
}

```