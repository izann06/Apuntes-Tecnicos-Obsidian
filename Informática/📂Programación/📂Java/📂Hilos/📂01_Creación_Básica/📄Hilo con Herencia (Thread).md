
```java

public class MiHiloPersonal extends Thread 
{ 
	@Override public void run() 
	{ 
		System.out.println("Soy un hilo creado por herencia."); 
		} 
} 

// En el Main: 

 MiHiloPersonal h = new MiHiloPersonal();
 h.start();

```