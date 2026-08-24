```java

public class EjemploInterrupt {
    public static void main(String[] args) {
        Thread dormilon = new Thread(() -> {
            try {
                System.out.println("Me voy a dormir 10 años...");
                Thread.sleep(10000 * 365 * 24); 
            } catch (InterruptedException e) {
                // Aquí cae si le llaman 'interrupt()' mientras duerme
                System.out.println("¡Eh! ¡Me han despertado/interrumpido!");
            }
        });

        dormilon.start();
        
        // El main espera un poquito y luego lo interrumpe
        try { Thread.sleep(2000); } catch (Exception e){}
        
        System.out.println("Main: Voy a despertar al dormilón.");
        dormilon.interrupt(); // ¡ZAS!
    }
}

```