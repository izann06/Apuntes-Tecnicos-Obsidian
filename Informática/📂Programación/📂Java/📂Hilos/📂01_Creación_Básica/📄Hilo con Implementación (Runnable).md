
```java
public class TareaRepetitiva implements Runnable { 

	@Override public void run() { 
		System.out.println("Soy una tarea ejecutándose."); 
	} 
}



public static void main(String[] args) { 

// Creas el Hilo y le metes el 'new TareaRepetitiva()' directamente dentro// 

	Thread hilo = new Thread(new TareaRepetitiva()); 
	hilo.start(); 
}

```

