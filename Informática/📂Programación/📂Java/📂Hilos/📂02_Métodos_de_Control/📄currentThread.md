Método que contiene información del hilo.

```java

Thread hiloActual = Thread.currentThread(); 

System.out.println("------------------------------------"); System.out.println("👮 DOCUMENTACIÓN DEL HILO:"); 
System.out.println(" -> Nombre: " + hiloActual.getName()); System.out.println(" -> ID (Número único): " + hiloActual.getId()); System.out.println(" -> Prioridad (1-10): " + hiloActual.getPriority()); System.out.println("-> Estado (Running/Waiting): "+ hiloActual.getState()); 
System.out.println(" -> ¿Es un Demonio?: " + hiloActual.isDaemon()); System.out.println(" -> ¿Está vivo?: " + hiloActual.isAlive()); System.out.println("------------------------------------");


//Puedes cambiar todos esos métodos y asignarle lo que tu quieras.

hiloActual.setName("Hilo A"); 
hiloActual.setPriority(10);

```
