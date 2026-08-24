
```java

public static void main(String[] args) { 

	Thread hiloModerno = new Thread(() -> { 
		System.out.println("Soy un hilo con Lambda."); 
		System.out.println("Hago cosas y termino."); 
	}); 
	
	hiloModerno.start(); }

```
