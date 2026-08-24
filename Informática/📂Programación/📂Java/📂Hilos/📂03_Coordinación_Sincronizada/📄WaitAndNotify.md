


```java
package org.example.Ejercicio3;  
  
public class SalaDeReuniones {  
  
    // Esta es la "bandera" o condición que esperamos  
    private boolean jefeHaLlegado = false;  
  
    // MÉTODO PARA EL EMPLEADO (El que espera)  
    public synchronized void esperarAlJefe() {  
        System.out.println("EMPLEADO: Entro a la sala. ¿Está el jefe?");  
  
        // Mientras el jefe NO haya llegado...  
        while (jefeHaLlegado == false) {  
            System.out.println("EMPLEADO: No está. Me siento a esperar (wait)...");  
            try {  
                // AQUÍ OCURRE LA MAGIA:  
                // 1. Suelta la llave del synchronized.                
                // 2. Se queda dormido en esta línea exacta.                
                wait();  
            } catch (InterruptedException e) { }  
        }  
  
        // Si el código llega aquí es porque:  
        // a) Alguien hizo notify()        
        // b) La condición del while ya es falsa (el jefe llegó)   
        System.out.println("EMPLEADO: ¡Hombre jefe! Ya podemos empezar.");  
    }  
  
    // MÉTODO PARA EL JEFE (El que avisa)  
    public synchronized void llegar() {  
        System.out.println("JEFE: Ya estoy aquí.");  
  
        jefeHaLlegado = true; // Cambio la condición  
  
        System.out.println("JEFE: Aviso a todos (notifyAll).");  
        notifyAll(); // ¡DESPERTAD!  
    }  
}
```

```java
package org.example.Ejercicio3;  
  
public class App {  
    public static void main(String[] args) {  
        SalaDeReuniones sala = new SalaDeReuniones();  
  
        // HILO 1: El empleado impaciente  
        Thread empleado = new Thread(() -> {  
            sala.esperarAlJefe();  
        });  
  
        // HILO 2: El jefe tardón  
        Thread jefe = new Thread(() -> {  
            try { Thread.sleep(3000); } catch (Exception e){} // Tarda 3 seg  
            sala.llegar();  
        });  
  
        empleado.start();  
        jefe.start();  
    }  
}
```

### La Analogía: El Probador de Ropa

Imagina que el objeto (tu clase) es un **probador de ropa** y el método `synchronized` es la **puerta con pestillo**.

1. **Situación Normal (`synchronized`):**
    
    - El Hilo A entra al probador y echa el pestillo.
        
    - Nadie más puede entrar.
        
    - El Hilo A se prueba la ropa y sale.
        
2. **El problema con `sleep()`:**
    
    - El Hilo A entra, echa el pestillo y decide echarse una siesta (`sleep`) dentro.
        
    - **Problema:** El Hilo B está fuera esperando, pero como el A tiene el pestillo echado y está durmiendo dentro, el B nunca puede entrar. Se bloquea todo.
        
3. **La Solución Mágica: `wait()`:**
    
    - El Hilo A entra, echa el pestillo, pero se da cuenta de que **le falta la camisa** (le falta un dato o una condición).
        
    - El Hilo A dice: "No puedo seguir". Entonces llama a `wait()`.
        
    - **¡MAGIA!**: Al hacer `wait()`, el Hilo A **abre el pestillo, sale del probador y se sienta en un banco de espera fuera**.
        
    - Ahora el probador está libre.
        
    - El Hilo B (el dependiente) entra, deja la camisa (`notify`) y sale.
        
    - El Hilo A ve que le han avisado, se levanta del banco, entra de nuevo, echa el pestillo y termina.